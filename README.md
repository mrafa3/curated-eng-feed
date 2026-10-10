# Curated Engineering Reads

A weekly RSS feed of engineering-blog posts picked for relevance, each with a short note on why it's worth reading.

Subscribe: `https://mrafa3.github.io/curated-eng-feed/feed.xml`

## What it's like week to week

**Tuesday, 5:00 a.m. Mountain.** GitHub Actions pulls all the feeds in `sources.yml`, drops anything already judged or older than the recency window, and commits `data/candidates.json`. Nothing needs you.

**Wednesday morning.** The Claude scheduled task reads `profile.md` and the candidates, decides what clears the bar, writes a note for each pick, and runs `scripts/build_feed.py`. The feed is live a minute later.

**Whenever you next open your reader.** A few new items, each with a sentence or two on the specific idea worth taking. Some weeks nothing arrives — `profile.md` says an empty week is fine, so the curator won't pad.

Expect roughly **3 to 5 candidates a week** in steady state. The first run is much larger, because `data/seen.json` starts nearly empty and the fetch sweeps the whole recency window at once.

## How it works

1. **Tuesday, GitHub Actions** (`.github/workflows/fetch.yml`) pulls every feed in `sources.yml` and writes posts not seen before, published within `MAX_AGE_DAYS`, to `data/candidates.json`. No judgment happens here, just fetching.
2. **Wednesday morning, a Claude scheduled task** reads `profile.md` and the candidates, picks the ones that clear the bar, writes a note for each, and runs `scripts/build_feed.py`. That rebuilds `feed.xml`, appends to `data/picks.json`, marks every candidate as seen in `data/seen.json`, and logs the run to `data/last_run.md`.
3. **GitHub Pages** serves `feed.xml`. Your reader picks it up.

## Turning it on

The loop does not start on its own. Three one-time steps:

1. **Push the repo to GitHub.**
2. **Enable GitHub Pages** for the repo (Settings → Pages, deploy from the default branch root). Until then the feed URL 404s.
3. **Create the Wednesday Claude scheduled task.** Nothing else triggers curation — without it, Tuesday's fetch just accumulates candidates and the feed never updates.

The fetch workflow also has `workflow_dispatch`, so you can run step 1 of the pipeline by hand at any time to see what a week's candidates look like.

## The curator's input

`build_feed.py` takes one JSON file. A bare list of picks works:

```json
[{"link": "https://...", "note": "The specific idea worth taking."}]
```

The fuller form also records why near-misses were passed over, which is what makes `data/last_run.md` worth reading:

```json
{
  "picks":   [{"link": "https://...", "note": "..."}],
  "skipped": [{"link": "https://...", "reason": "Relevant topic, no transferable idea."}],
  "summary": "Optional sentence about the week as a whole."
}
```

Every link must already appear in `data/candidates.json`; a link that doesn't is a hard error rather than a silent drop.

## Tuning

| To change | Edit |
|---|---|
| How the Wednesday curation runs | `CURATOR.md` (the scheduled task reads it each week) |
| What counts as relevant | `profile.md` |
| Which blogs are read | `sources.yml` (feeds; `type: page` for blogs with no feed; `type: task` for blogs that block GitHub Actions but load for the curator, which downloads them with curl) |
| How many links a page source takes | `MAX_PAGE_POSTS` in `scripts/fetch_candidates.py` |
| How far back the fetch looks | `MAX_AGE_DAYS` in `scripts/fetch_candidates.py` |
| Feed title or description | `feed_config.json` |
| Fetch schedule | `cron` in `.github/workflows/fetch.yml` |
| How many items the feed carries | `MAX_ITEMS` in `scripts/build_feed.py` |

Changes take effect on the next run. There is no build or deploy step.

## When the picks feel off

Read `data/last_run.md`. It records what was considered, what was picked and why, which near-misses were skipped and why, and how many candidates were passed over without comment. That last number is the useful one: if it is high on a week the picks felt wrong, the bar in `profile.md` needs adjusting rather than the curator's reasoning.

Failed feeds are logged there too, and in `data/candidates.json` under `failures`, so a blog that quietly starts returning 403 shows up instead of just going silent.

## Files

- `profile.md`: what counts as relevant — the only place taste is defined
- `sources.yml`: the blogs the fetch reads, plus notes on ones deliberately excluded
- `data/candidates.json`: this week's unseen, in-window posts (overwritten weekly)
- `data/picks.json`: every pick ever made, newest first
- `data/seen.json`: every link already evaluated, so nothing is judged twice
- `data/last_run.md`: the most recent run's reasoning (overwritten weekly)
- `feed.xml`: the published feed (latest 60 picks)
- `index.html`: a small landing page for the feed
