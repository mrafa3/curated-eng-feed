"""Merge posts fetched by the curator into this week's data/candidates.json.

Usage: python scripts/add_candidates.py posts.json

posts.json is a list of {"title", "link", "source"} with optional "published"
(ISO 8601) and "summary". It covers sources marked `type: task` in sources.yml:
blogs that block the Tuesday GitHub Actions fetch but load fine for the curator.

Links already in data/seen.json or already in candidates.json are skipped, so
running this twice is harmless.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from fetch_candidates import OUT, SEEN, SUMMARY_CHARS, clean_link, parse_date  # noqa: E402


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    posts = json.loads(Path(sys.argv[1]).read_text())
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
