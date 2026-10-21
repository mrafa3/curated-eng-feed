# Curation run 2026-10-21

- Candidates considered: 31
- Picked: 3
- Explicitly skipped: 8
- Passed over without comment: 20
- Candidates fetched at: 2026-10-20T15:35:51.542668+00:00
- Recency window: 90 days

## The week

A large Netflix backlog landed alongside thirteen GrowthBook posts, and three Netflix pieces cleared the bar: DataJunction as a shared metric layer for dashboards and experiments, the lifecycle of an LLM judge, and measuring the value of personalization as its own problem. Two fetch caveats: Medium-hosted blogs (Netflix, Booking) return a Cloudflare block to curl and growthbook.io is refused at this environment's proxy with a 403, so every candidate this week was judged on its title and feed summary rather than its body; no source failed Tuesday's fetch.

## Picked

### DataJunction as Netflix’s answer to the missing piece of the modern data stack

Netflix TechBlog — <https://netflixtechblog.com/datajunction-as-netflixs-answer-to-the-missing-piece-of-the-modern-data-stack-92af926b40a5>

An open-source metric layer sitting between the warehouse and both the dashboards and the experimentation platform, so an experiment metric and the same metric on a dashboard resolve to one definition instead of drifting apart. Worth comparing against how the gold layer and the experiment metrics are defined today, and it is installable rather than an internal-only system.

### The Lifecycle of LLM-as-a-Judge: Building, Aligning, and Monitoring at scale

Netflix TechBlog — <https://netflixtechblog.com/the-lifecycle-of-llm-as-a-judge-building-aligning-and-monitoring-at-scale-c95bd8283508>

Treats a judge as a model with a lifecycle: align it to human ratings before trusting it, then keep monitoring that agreement, because a judge shipped once silently drifts away from what the raters meant. The directly usable part is the discipline of measuring judge-to-human agreement as an ongoing metric for any documentation or triage agent scored by an LLM.

### Measuring the Impact of Personalized Recommendations

Netflix TechBlog — <https://netflixtechblog.com/measuring-the-impact-of-personalized-recommendations-4c26be3a4d96>

Frames the value of a personalization system as a measurement problem in its own right - what it adds over a non-personalized baseline - rather than something read off the online metrics of individual model changes. The same framing applies when asked what a production forecast or a curated model is worth, where incremental tests on single changes never add up to the system-level number.

## Skipped

- **Headspace's Guardrails for AI Tests** (GrowthBook Blog) — Guardrails for AI experiments where more engagement is not the goal is a genuinely useful angle, but growthbook.io is blocked at this environment's proxy and the one-line teaser does not say what the guardrails actually are.
- **How Grubhub Tests Big Product Bets** (GrowthBook Blog) — De-risking big bets when classic A/B tests do not fit a three-sided marketplace is on target, but the post was unreachable and the teaser alone gives no method.
- **Walmart Connect on Cross-Sell and Intent** (GrowthBook Blog) — A failed test that redirected what the team tested next is the right shape of story, but unreachable this week and the visible text is an interview blurb about ad cross-sell.
- **Designing Experiments That Produce Trustworthy Results: A Pre-Launch Guide to Validity Threats** (GrowthBook Blog) — A pre-launch validity checklist would be usable with a team, but it is vendor explainer content and the page could not be fetched to check whether it goes past the familiar list.
- **Beyond evals: A/B test AI features with LLM traces** (GrowthBook Blog) — Wiring Langfuse and Arize trace data into experiment metrics is a real idea for testing prompts against cost and quality, but this is a product launch announcement.
- **Running Apache Spark experiments in my sleep (and on a plane)** (Netflix TechBlog) — The reframe from speeding up one Spark run to running many tuning runs unattended is a nice workflow idea, but the post is pipeline performance tuning rather than anything about how curated models get built or trusted.
- **From Static Help Content to a RAG-Based Onboarding Agent for Partners** (Booking.com ML & DS) — A RAG agent for partner onboarding support, not for data work, and the body was unreachable to check whether the evaluation setup transfers.
- **Ontology-Driven Observability: Building an End-to-End Knowledge Graph at Netflix Scale** (Netflix TechBlog) — An ontology over services and signals sounds adjacent to semantic modeling, but it is infrastructure observability at a scale where the problem is a different one.
