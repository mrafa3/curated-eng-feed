# Curation run 2026-11-04

- Candidates considered: 6
- Picked: 1
- Explicitly skipped: 5
- Passed over without comment: 0
- Candidates fetched at: 2026-11-03T18:18:36.116279+00:00
- Recency window: 90 days

## The week

A thin week: all six candidates came from the GrowthBook blog, two of them outright product marketing, and www.growthbook.io is refused at this environment's proxy (403 on CONNECT), so everything was judged on feed titles and summaries alone. One pick, the Winsorization explainer, because outlier capping is squarely on the profile and its summary names the actual bias-variance-power trade-off; the near-misses are either unreadable interview teasers or methods aimed at ranking surfaces. Tuesday's fetch reported no source failures.

## Picked

### Should You Cap Outliers? Winsorization in A/B Testing

GrowthBook Blog — <https://www.growthbook.io/blog/cap-outliers-winsorization-ab-testing>

Winsorizing a heavy-tailed metric buys lower variance and more power at the cost of some bias, so the decision to cap belongs to whether it improves the experiment decision rather than to a house rule. Relevant whenever revenue or usage metrics with a few extreme accounts drive an experiment readout.

## Skipped

- **Interleaving Experiments: How to Test Rankers Faster** (GrowthBook Blog) — Interleaving to make each user their own control is a legitimate traffic-efficiency idea, but it only pays off when comparing rankers on the same surface, which is not this reader's surface area.
- **How Preply runs 1,000 tests a year** (GrowthBook Blog) — High experiment volume, expecting losing tests, and two-sided marketplace interference are all on topic, but the teaser is an interview blurb with no method behind the claims and the page could not be fetched.
- **Why Product and Marketing Should Experiment Together to Protect the User Experience** (GrowthBook Blog) — Shared metrics, guardrails, and holdouts across product and marketing is a real metric-governance question, but the framing is a one-platform pitch and the page was unreachable.
- **GrowthBook 5.2: Interleaving experiments and Human in the Loop for agents** (GrowthBook Blog) — Product release notes; the profile skips company news, and the interleaving method it mentions has its own post.
- **Why migrate from LaunchDarkly to GrowthBook** (GrowthBook Blog) — Competitive migration marketing with no transferable method.
