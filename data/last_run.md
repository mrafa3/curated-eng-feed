# Curation run 2026-09-30

- Candidates considered: 38
- Picked: 5
- Explicitly skipped: 8
- Passed over without comment: 25
- Candidates fetched at: 2026-09-29T16:50:30.429835+00:00
- Recency window: 90 days

## The week

A strong week for experimentation: Booking on treating hypothesis quality as the gate before launch, and two Spotify posts on analysis-method choice and on the limits of letting an LLM stand in for a human outcome. Airbnb on fast LLM evaluation and Instacart's on-call reasoning harness round it out; all feeds fetched cleanly with no failures.

## Picked

### A problem well-defined is half solved: Measuring Hypothesis Quality at Booking.com

Booking.com ML & DS — <https://booking.ai/a-problem-well-defined-is-half-solved-measuring-hypothesis-quality-at-booking-com-a85e845178a3>

Booking makes the hypothesis itself the quality gate: the evidence behind the idea, the user response expected, and the decision criteria all written down before launch, then scored. That is a rubric you can drop into your own experiment intake so a clear result arrives already attached to a decision instead of a debate.

### Why Spotify Is Not Using Bayesian A/B Testing

Spotify Engineering — <https://engineering.atspotify.com/2026/9/why-spotify-is-not-using-bayesian-a-b-testing/>

A team that runs experimentation at scale explaining why it stayed frequentist and what the Bayesian label does and does not actually change. Read it before your team spends a quarter evaluating a switch, and keep it for the next time someone asks why you haven't.

### When Can LLMs Replace Humans in A/B Tests?

Spotify Engineering — <https://engineering.atspotify.com/2026/8/when-can-llms-replace-humans-in-a-b-tests/>

The useful part is the framing: LLM-predicted outcomes substitute for human ones only under assumptions you have to state and defend, not as a free measurement upgrade. Directly relevant if you are tempted to let a judge model stand in for a real metric in a test.

### From weeks to a day: how we made LLM evaluation fast enough to iterate on

Airbnb Tech Blog — <https://airbnb.tech/ai-ml/from-weeks-to-a-day-how-we-made-llm-evaluation-fast-enough-to-iterate-on/>

Airbnb's cut from weeks to a day came from ordinary engineering on the eval harness - caching, determinism, handling judges that disagree with themselves - not from better models. The layered breakdown is a good checklist for why your own agent evals are too slow to iterate on.

### Blueberry: Force Multiplier For The On-Call Engineer

Instacart Tech — <https://tech.instacart.com/blueberry-force-multiplier-for-the-on-call-engineer-98c446dfcc12>

A Slack-native reasoning harness aimed at the worst minutes of an incident, when nobody yet agrees what is broken, and at turning tribal knowledge into context the agent can reuse. Close to the operational triage work you are building, and concrete about where the harness boundary sits.

## Skipped

- **Agentic Machine Learning Modeling at Instacart** (Instacart Tech) — Candid on where agents help and where they fail, but framed around the ML model research loop rather than data modeling or triage, so less of it transfers.
- **AI Changed How Spotify Builds. What We Learned (and Fixed) About Quality at Higher Velocity** (Spotify Engineering) — The AI-adoption and quality-at-velocity angle is in scope, but the quality story is service and app release engineering with little that carries over to data work.
- **Helix: The internal tool powering our Shopify app's native migration** (Shopify Engineering) — Small checkpoints and strict quality gates is a real harness-design idea, but the post is a mobile native rewrite, which the profile skips even for the org lesson.
- **Sidekick's continual learning loop** (Shopify Engineering) — A genuinely interesting failure-to-weights feedback loop, but it needs daily fine-tuning infrastructure well outside the reader's setting.
- **Gisting: Compressing LLM Agent context to ↑ throughput and ↓ cost** (Shopify Engineering) — Context compression to cut agent cost is on-topic, but the method is training learned tokens rather than anything adaptable to a team buying inference.
- **How we selected the next vector database at Booking.com** (Booking.com ML & DS) — A selection framework is portable, but this is vector-store procurement rather than the curated-model and metric layer.
- **Indexing the Data Lake for Online Point Queries** (Spotify Engineering) — Lakehouse-adjacent, though it is a low-latency serving index rather than how curated tables get built or trusted.
- **Refreshing the Travel-Time Map Behind Lyft’s Marketplace: Rebuilding Neighborhood Reachability…** (Lyft Engineering) — Has a real when-to-rebuild-a-stale-model thread for forecasting, but it is buried in a geospatial routing pipeline.
