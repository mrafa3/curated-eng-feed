"""Pull every feed in sources.yml and write the posts not seen before to data/candidates.json.

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

ROOT = Path(__file__).resolve().parent.parent
SOURCES = ROOT / "sources.yml"
SEEN = ROOT / "data" / "seen.json"
OUT = ROOT / "data" / "candidates.json"

ATOM = "{http://www.w3.org/2005/Atom}"
CONTENT = "{http://purl.org/rss/1.0/modules/content/}encoded"
SUMMARY_CHARS = 1500
MAX_AGE_DAYS = 90  # some feeds serve a full archive; only recent posts are worth curating


def load_sources():
    """Read name/url pairs from sources.yml, skipping commented-out lines."""
    sources, name = [], None
    for line in SOURCES.read_text().splitlines():
        line = line.split(" #")[0].strip()
        if line.startswith("#"):
            continue
        m = re.match(r"-?\s*(name|url):\s*(.+)", line)
        if not m:
            continue
        key, value = m.groups()
        if key == "name":
            name = value.strip()
        elif name:
            sources.append({"name": name, "url": value.strip()})
            name = None
    return sources


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


def is_recent(post, cutoff):
    """Keep posts published on or after cutoff.

    A post with no date is kept: every source currently dates every post, so a
    missing date means the feed's format changed, not that the post is old.
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
        try:
            posts = parse_feed(fetch(src["url"]), src["name"])
        except Exception as exc:  # one bad feed shouldn't stop the rest
            failures.append({"source": src["name"], "url": src["url"], "error": str(exc)[:200]})
            continue
        unseen = [p for p in posts if p["link"] not in seen]
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
