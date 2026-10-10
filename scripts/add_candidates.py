"""Merge posts fetched by the curator into this week's data/candidates.json.

Usage:
  python scripts/add_candidates.py --page "<source name>" page.html
      page.html is a task source's index page downloaded with curl. The source's
      url and pattern are looked up in sources.yml, and post links are extracted
      the same way the Tuesday fetch handles page sources.

  python scripts/add_candidates.py posts.json
      posts.json is a list of {"title", "link", "source"} with optional
      "published" (ISO 8601) and "summary", for a page the extractor can't read.

Both cover sources marked `type: task` in sources.yml: blogs that block the
Tuesday GitHub Actions fetch but load for the curator.

Links already in data/seen.json or already in candidates.json are skipped, so
running this twice is harmless.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from fetch_candidates import (  # noqa: E402
    OUT, SEEN, SUMMARY_CHARS, clean_link, load_sources, parse_date, parse_page,
)


def posts_from_page(source_name, html_path):
    src = next((s for s in load_sources() if s["name"] == source_name), None)
    if not src:
        sys.exit(f"No active source named {source_name!r} in sources.yml")
    posts = parse_page(Path(html_path).read_bytes(), src["url"], src.get("pattern", "."), src["name"])
    if not posts:
        sys.exit(f"No post links matched the pattern for {source_name}; the page may be a block page or redesigned")
    return posts


def main():
    args = sys.argv[1:]
    if len(args) == 3 and args[0] == "--page":
        posts = posts_from_page(args[1], args[2])
    elif len(args) == 1:
        posts = json.loads(Path(args[0]).read_text())
    else:
        sys.exit(__doc__)
    data = json.loads(OUT.read_text()) if OUT.exists() else {"failures": [], "candidates": []}
    seen = set(json.loads(SEEN.read_text())) if SEEN.exists() else set()
    present = {c["link"] for c in data["candidates"]}

    added = 0
    for p in posts:
        link = clean_link(p.get("link", "")).rstrip("/")
        title = (p.get("title") or "").strip()
        source = (p.get("source") or "").strip()
        if not (link and title and source):
            sys.exit(f"Each post needs title, link and source: {p}")
        if link in seen or link in present:
            continue
        data["candidates"].append({
            "title": title,
            "link": link,
            "published": parse_date(p.get("published")),
            "summary": (p.get("summary") or "")[:SUMMARY_CHARS],
            "source": source,
        })
        present.add(link)
        added += 1

    data["candidates"].sort(key=lambda c: c["published"] or "", reverse=True)
    OUT.write_text(json.dumps(data, indent=2) + "\n")
    print(f"Added {added} of {len(posts)} posts; {len(posts) - added} already seen or present")


if __name__ == "__main__":
    main()
