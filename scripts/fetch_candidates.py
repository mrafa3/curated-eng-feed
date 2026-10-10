"""Pull every source in sources.yml and write the posts not seen before to data/candidates.json.

Most sources are RSS/Atom feeds. A source marked `type: page` is a blog index page
with no feed: its post links are scraped, and each new post's own page supplies
the description and publish date.

Standard library only. Runs in GitHub Actions; the curator reads the output.
"""
import json
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from email.utils import parsedate_to_datetime
from html import unescape
from pathlib import Path
from urllib.parse import urljoin, urlparse

ROOT = Path(__file__).resolve().parent.parent
SOURCES = ROOT / "sources.yml"
SEEN = ROOT / "data" / "seen.json"
OUT = ROOT / "data" / "candidates.json"

ATOM = "{http://www.w3.org/2005/Atom}"
CONTENT = "{http://purl.org/rss/1.0/modules/content/}encoded"
SUMMARY_CHARS = 1500
MAX_AGE_DAYS = 90  # some feeds serve a full archive; only recent posts are worth curating
MAX_PAGE_POSTS = 8  # page sources list the archive undated, so only the newest links are taken


def load_sources():
    """Read sources from sources.yml, skipping comments.

    Each entry starts with `- name:`; the following `key: value` lines (url, type,
    pattern) belong to it. Entries without a url are ignored.
    """
    sources = []
    for line in SOURCES.read_text().splitlines():
        line = line.split(" #")[0].strip()
        if not line or line.startswith("#"):
            continue
        m = re.match(r"(-\s*)?(name|url|type|pattern):\s*(.+)", line)
        if not m:
            continue
        starts_entry, key, value = m.groups()
        if key == "name" and starts_entry:
            sources.append({})
        if sources:
            sources[-1][key] = value.strip().strip("'\"")
    return [s for s in sources if s.get("name") and s.get("url")]


def clean_link(link):
    return link.split("?")[0].strip() if link else ""


def strip_html(text):
    text = re.sub(r"<[^>]+>", " ", text or "")
    return re.sub(r"\s+", " ", unescape(text)).strip()


def parse_date(value):
    if not value:
        return None
    try:
        return parsedate_to_datetime(value).astimezone(timezone.utc).isoformat()
    except (TypeError, ValueError):
        pass
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00")).astimezone(timezone.utc).isoformat()
    except ValueError:
        return None


def parse_feed(xml_bytes, source_name):
    root = ET.fromstring(xml_bytes)
    posts = []
    for item in root.iter("item"):  # RSS 2.0
        body = item.findtext(CONTENT) or item.findtext("description")
        posts.append({
            "title": strip_html(item.findtext("title")),
            "link": clean_link(item.findtext("link")),
            "published": parse_date(item.findtext("pubDate")),
            "summary": strip_html(body)[:SUMMARY_CHARS],
        })
    for entry in root.iter(f"{ATOM}entry"):  # Atom
        # Element truthiness depends on child count, so compare to None explicitly.
        link_el = entry.find(f"{ATOM}link[@rel='alternate']")
        if link_el is None:
            link_el = entry.find(f"{ATOM}link")
        body = entry.findtext(f"{ATOM}content") or entry.findtext(f"{ATOM}summary")
        posts.append({
            "title": strip_html(entry.findtext(f"{ATOM}title")),
            "link": clean_link(link_el.get("href") if link_el is not None else ""),
            "published": parse_date(entry.findtext(f"{ATOM}published") or entry.findtext(f"{ATOM}updated")),
            "summary": strip_html(body)[:SUMMARY_CHARS],
        })
    for p in posts:
        p["source"] = source_name
    return [p for p in posts if p["link"] and p["title"]]


ANCHOR = re.compile(r"<a\b[^>]*?\bhref\s*=\s*[\"']([^\"']+)[\"'][^>]*>(.*?)</a>", re.I | re.S)
HEADING = re.compile(r"<h[1-6]\b[^>]*>(.*?)</h[1-6]>", re.I | re.S)


def parse_page(html_bytes, page_url, pattern, source_name):
    """Pull post links from a blog index page, newest first as the page lists them.

    `pattern` is a regex matched against each link's path, e.g. ^/engineering/[^/]+$.
    A card often links the same post twice (image and title), so links are merged
    and the most title-like text wins: a heading inside the anchor, else its text.
    """
    html = html_bytes.decode("utf-8", errors="replace")
    host = urlparse(page_url).netloc
    order, titles, from_heading = [], {}, set()
    for href, inner in ANCHOR.findall(html):
        url = urljoin(page_url, unescape(href))
        parsed = urlparse(url)
        if parsed.netloc != host or not re.search(pattern, parsed.path.rstrip("/")):
            continue
        link = clean_link(url.split("#")[0]).rstrip("/")
        if link not in titles:
            order.append(link)
            titles[link] = ""
        heading = HEADING.search(inner)
        if heading and link not in from_heading:
            titles[link] = strip_html(heading.group(1))
            from_heading.add(link)
        elif not titles[link]:
            titles[link] = strip_html(inner)
    posts = []
    for link in order[:MAX_PAGE_POSTS]:
        slug = urlparse(link).path.rstrip("/").split("/")[-1]
        posts.append({
            "title": titles[link] or slug.replace("-", " ").capitalize(),
            "link": link,
            "published": None,
            "summary": "",
            "source": source_name,
        })
    return posts


def meta_content(html, *names):
    for name in names:
        for pat in (
            rf"<meta\b[^>]*?(?:name|property)\s*=\s*[\"']{re.escape(name)}[\"'][^>]*?content\s*=\s*[\"']([^\"']*)[\"']",
            rf"<meta\b[^>]*?content\s*=\s*[\"']([^\"']*)[\"'][^>]*?(?:name|property)\s*=\s*[\"']{re.escape(name)}[\"']",
        ):
            m = re.search(pat, html, re.I | re.S)
            if m and m.group(1).strip():
                return unescape(m.group(1)).strip()
    return None


def enrich_from_post(post):
    """Fill a scraped post's title, summary and date from the post's own page meta tags."""
    try:
        html = fetch(post["link"]).decode("utf-8", errors="replace")
    except Exception:
        return post  # keep the bare link; the curator can still judge it by title
    post["summary"] = (meta_content(html, "og:description", "description", "twitter:description") or "")[:SUMMARY_CHARS]
    # The post's own title tag is cleaner than card text, which can carry dates and tags.
    title = meta_content(html, "og:title", "twitter:title")
    if title:
        # Drop a trailing site-name suffix ("Title | Notion", "Title \ Anthropic") but nothing else.
        site = urlparse(post["link"]).netloc.split(".")[-2]
        title = re.sub(rf"\s*[|\\–—-]\s*[^|\\–—-]*{re.escape(site)}[^|\\–—-]*$", "", title, flags=re.I)
        post["title"] = title.strip() or post["title"]
    date = meta_content(html, "article:published_time", "datePublished", "date")
    if not date:
        m = re.search(r"\"datePublished\"\s*:\s*\"([^\"]+)\"", html)
        date = m.group(1) if m else None
    post["published"] = parse_date(date)
    return post


def is_recent(post, cutoff):
    """Keep posts published on or after cutoff.

    A post with no date is kept. Feeds date every post, so a missing date there
    means the format changed; a page-source post is undated only when its own page
    has no date tag, and it is still one of that page's newest links.
    """
    if not post["published"]:
        return True
    try:
        return datetime.fromisoformat(post["published"]) >= cutoff
    except ValueError:
        return True


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "curated-eng-feed/1.0 (personal RSS curator)"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read()


def main():
    seen = set(json.loads(SEEN.read_text())) if SEEN.exists() else set()
    cutoff = datetime.now(timezone.utc) - timedelta(days=MAX_AGE_DAYS)
    candidates, failures, stale = [], [], 0
    for src in load_sources():
        if src.get("type") == "task":
            continue  # fetched by the Wednesday curator instead; see scripts/add_candidates.py
        try:
            if src.get("type") == "page":
                posts = parse_page(fetch(src["url"]), src["url"], src.get("pattern", "."), src["name"])
                if not posts:
                    raise ValueError("no post links matched the pattern; the page layout may have changed")
            else:
                posts = parse_feed(fetch(src["url"]), src["name"])
        except Exception as exc:  # one bad source shouldn't stop the rest
            failures.append({"source": src["name"], "url": src["url"], "error": str(exc)[:200]})
            continue
        unseen = [p for p in posts if p["link"] not in seen]
        if src.get("type") == "page":
            unseen = [enrich_from_post(p) for p in unseen]
        fresh = [p for p in unseen if is_recent(p, cutoff)]
        stale += len(unseen) - len(fresh)
        candidates.extend(fresh)

    candidates.sort(key=lambda p: p["published"] or "", reverse=True)
    OUT.write_text(json.dumps({
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "max_age_days": MAX_AGE_DAYS,
        "failures": failures,
        "candidates": candidates,
    }, indent=2) + "\n")
    print(f"{len(candidates)} new posts, {stale} older than {MAX_AGE_DAYS} days, {len(failures)} failed feeds")
    for f in failures:
        print(f"  FAILED {f['source']}: {f['error']}", file=sys.stderr)


if __name__ == "__main__":
    main()
