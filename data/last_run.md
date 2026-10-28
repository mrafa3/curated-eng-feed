# Curation run 2026-10-28

- Candidates considered: 13
- Picked: 3
- Explicitly skipped: 6
- Passed over without comment: 4
- Candidates fetched at: 2026-10-27T16:18:17.993952+00:00
- Recency window: 90 days
- FEED FAILED: Anthropic Engineering (no post links matched the pattern; the page layout may have changed)

## The week

Three picks, all on evaluating and operating LLM agents: Netflix routing only unknown job failures to a model while rules keep the known ones, Notion calibrating a pointwise judge against pairwise Elo rankings, and Shopify setting a judge's bar at human inter-annotator agreement and recycling failed conversations into training data. Fetch caveats repeat from last week - Medium-hosted Netflix posts return 403 to curl and growthbook.io is refused at this environment's proxy, so the Netflix pick and every GrowthBook near-miss were judged on feed text alone - and Tuesday's fetch reported one source failure, Anthropic Engineering, where no links matched the pattern.

## Picked

### Making Failure Diagnosis Reliable with Pensive AI

Netflix TechBlog — <https://netflixtechblog.com/making-failure-diagnosis-reliable-with-pensive-ai-6b0811a1c015>

Netflix kept its deterministic regex-and-rules classifier for known Spark/Trino/Druid failures and aimed the LLM only at the unknown bucket, which was about half of seven million job-failure classifications in three months. That split - rules stay the trusted path, the model expands coverage where no rule exists - is the design to copy for a pipeline triage agent, along with the framing that the useful output is a decision (my code or the platform, retry, reconfigure, or escalate) rather than a summary of the logs.

### Inside Notion’s upgraded model router, Auto

Notion Blog — <https://www.notion.com/blog/inside-notions-upgraded-model-router-auto>

Notion found a single LLM judge too noisy even with a detailed rubric, so they ran pairwise comparisons by an ensemble of judges, turned those into Elo rankings, and then tuned a cheap pointwise judge until its scores reproduced the Elo order - agreeing over 80% of the time, and checked against customer thumbs up/down. A pairwise-calibrate-then-score pattern worth borrowing when a pointwise judge on documentation or triage output drifts, and their sandbox approach of replaying real tasks against a saved copy of a workspace is a good model for evaluating an agent on real data work.

### How Shopify turns open models into task experts

Shopify Engineering — <https://shopify.engineering/open-model-task-experts>

Two ideas transfer from Shopify's text-to-GraphQL subagent: set the LLM judge's accuracy bar at how well two human experts agree on the same conversations rather than at an absolute score, and turn failed production conversations into training and eval data by having a critic write a hint, rerunning the task, then dropping the hint if the judge passes it. Skim past the NVIDIA hardware benchmarks, which are the vendor half of the post.

## Skipped

- **How to Run Multiple Experiments at Once and Keep Results Trustworthy** (GrowthBook Blog) — Interaction effects, mutual exclusion, and conflict health checks are squarely on topic, but growthbook.io is refused at this environment's proxy and the teaser does not say whether it goes beyond the standard advice.
- **The Bottlenecks Slowing Down Your Experimentation Velocity** (GrowthBook Blog) — Where experimentation programs plateau is a useful lens for a team ramping up testing, but the page was unreachable and the teaser reads like a generic vendor funnel piece.
- **Testing culture is a relationship problem** (GrowthBook Blog) — Experimentation buy-in across sales, support, and product is the right subject, but this is an unreachable interview blurb with no method behind the claim.
- **New York Red Bulls on testing fan value** (GrowthBook Blog) — Measuring total engagement instead of the obvious conversion metric is a real metric-definition lesson, but the post could not be fetched and the summary is a podcast teaser.
- **Beyond API Compatibility: Building a Tool to Measure the Blast Radius of Library Changes** (Netflix TechBlog) — Measuring who actually depends on the symbols you are about to change rhymes with impact analysis before a gold-layer schema change, but the post is Java library release tooling and the body was blocked to curl.
- **We gave AI agents a mobile dev environment** (Shopify Engineering) — Giving agents their own environments so they can work in parallel is an interesting constraint on agent workflows, but the post is about mobile app build environments, which the profile skips.
