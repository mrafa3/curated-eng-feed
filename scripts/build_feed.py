"""Turn the week's picks into feed.xml, mark every candidate as seen, and log the run.

Usage: python scripts/build_feed.py data/week_picks.json

week_picks.json is written by the curator, in either form:

    [{"link": ..., "note": ...}, ...]

    {"picks":   [{"link": ..., "note": ...}, ...],
     "skipped": [{"link": ..., "reason": ...}, ...],
     "summary": "optional sentence about the week as a whole"}

Every link must appear in data/candidates.json. Picks are appended to
data/picks.json (the running history), feed.xml is rebuilt from the newest
picks, and every candidate link is added to data/seen.json so it is never
evaluated twice. data/last_run.md records what was considered, what was
picked and why, and which near-misses were skipped and why.
"""
import json
import sys
from datetime import datetime, timezone
from email.utils import format_datetime
from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parent.parent
CANDIDATES = ROOT / "data" / "candidates.json"
PICKS = ROOT / "data" / "picks.json"
SEEN = ROOT / "data" / "seen.json"
LAST_RUN = ROOT / "data" / "last_run.md"
FEED = ROOT / "feed.xml"
CONFIG = ROOT / "feed_config.json"
MAX_ITEMS = 60


def load(path, default):
    return json.loads(path.read_text()) if path.exists() else default


def rfc822(iso):
    dt = datetime.fromisoformat(iso) if iso else datetime.now(timezone.utc)
    if dt.tzinfo is None:  # a feed's naive timestamp is UTC, not the runner's local zone
        dt = dt.replace(tzinfo=timezone.utc)
    return format_datetime(dt.astimezone(timezone.utc), usegmt=True)


def write_feed(picks, cfg):
    now = rfc822(datetime.now(timezone.utc).isoformat())
    items = []
    for p in picks[:MAX_ITEMS]:
        desc = f"{p['note']}\n\nSource: {p['source']}"
        items.append(
            "    <item>\n"
            f"      <title>{escape(p['title'])}</title>\n"
            f"      <link>{escape(p['link'])}</link>\n"
            f"      <guid isPermaLink=\"true\">{escape(p['link'])}</guid>\n"
            f"      <pubDate>{rfc822(p['curated_at'])}</pubDate>\n"
            f"      <category>{escape(p['source'])}</category>\n"
            f"      <description>{escape(desc)}</description>\n"
            "    </item>"
        )
    FEED.write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">\n'
        "  <channel>\n"
        f"    <title>{escape(cfg['title'])}</title>\n"
        f"    <link>{escape(cfg['site_url'])}</link>\n"
        f"    <atom:link href=\"{escape(cfg['feed_url'])}\" rel=\"self\" type=\"application/rss+xml\"/>\n"
        f"    <description>{escape(cfg['description'])}</description>\n"
        "    <language>en-us</language>\n"
        f"    <lastBuildDate>{now}</lastBuildDate>\n"
        + "\n".join(items) + "\n"
        "  </channel>\n"
        "</rss>\n"
    )


def write_last_run(candidates, new_picks, skipped, summary, by_link):
    """Record what this run considered and decided, so a bad week can be diagnosed.

    Picks and skips come from the curator; the counts come from the candidate
    file. Candidates the curator said nothing about are reported as a number,
    which is the signal that the profile is filtering more than it explains.
    """
    meta = load(CANDIDATES, {})
    accounted = {p["link"] for p in new_picks} | {s["link"] for s in skipped}
    lines = [
        f"# Curation run {datetime.now(timezone.utc).strftime('%Y-%m-%d')}",
        "",
        f"- Candidates considered: {len(candidates)}",
        f"- Picked: {len(new_picks)}",
        f"- Explicitly skipped: {len(skipped)}",
        f"- Passed over without comment: {len(candidates) - len(accounted)}",
        f"- Candidates fetched at: {meta.get('fetched_at') or 'unknown'}",
    ]
    if meta.get("max_age_days"):
        lines.append(f"- Recency window: {meta['max_age_days']} days")
    for f in meta.get("failures", []):
        lines.append(f"- FEED FAILED: {f['source']} ({f['error']})")
    if summary:
        lines += ["", "## The week", "", summary.strip()]

    lines += ["", "## Picked", ""]
    if new_picks:
        for p in new_picks:
            lines += [f"### {p['title']}", "", f"{p['source']} — <{p['link']}>", "", p["note"], ""]
    else:
        lines += ["Nothing cleared the bar this week.", ""]

    lines += ["## Skipped", ""]
    if skipped:
        for s in skipped:
            c = by_link.get(s["link"], {})
            lines += [f"- **{c.get('title', s['link'])}** ({c.get('source', '?')}) — {s['reason'].strip()}"]
        lines.append("")
    else:
        lines += ["No near-misses recorded.", ""]

    LAST_RUN.write_text("\n".join(lines))


def main():
    cfg = load(CONFIG, None)
    candidates = load(CANDIDATES, {"candidates": []})["candidates"]
    by_link = {c["link"]: c for c in candidates}
    raw = load(Path(sys.argv[1]), []) if len(sys.argv) > 1 else []
    # the curator may send a bare list of picks, or an object that also explains the skips
    if isinstance(raw, dict):
        week, skipped, summary = raw.get("picks", []), raw.get("skipped", []), raw.get("summary", "")
    else:
        week, skipped, summary = raw, [], ""

    now = datetime.now(timezone.utc).isoformat()
    new_picks = []
    for w in week:
        c = by_link.get(w["link"])
        if not c:
            sys.exit(f"Pick not found in candidates: {w['link']}")
        new_picks.append({"title": c["title"], "link": c["link"], "source": c["source"],
                          "published": c.get("published"), "note": w["note"].strip(), "curated_at": now})

    picks = new_picks + load(PICKS, [])
    PICKS.write_text(json.dumps(picks, indent=2) + "\n")

    seen = set(load(SEEN, [])) | set(by_link)
    SEEN.write_text(json.dumps(sorted(seen), indent=2) + "\n")

    write_feed(picks, cfg)
    write_last_run(candidates, new_picks, skipped, summary, by_link)
    print(f"Added {len(new_picks)} picks; feed has {min(len(picks), MAX_ITEMS)} items; {len(seen)} links seen")
    print(f"Wrote {LAST_RUN.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
