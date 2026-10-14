# Curation run 2026-10-14

- Candidates considered: 8
- Picked: 4
- Explicitly skipped: 3
- Passed over without comment: 1
- Candidates fetched at: 2026-10-14T00:41:51.339740+00:00
- Recency window: 90 days

## The week

Eight candidates, five of them a Faire backlog surfacing now that The Craft feed is live, and the set was unusually well aimed at AI adoption and agent harness design. Four picks: Faire's agent-driven ML exploration loop and its build-the-harness stance, Anthropic's account of what changed organizationally at 30,000 merges a day, and Airbnb's method for getting relevance labels without an LLM judge. Two caveats: craft.faire.com returns 403 at this environment's network proxy, so all five Faire posts were judged on feed summaries rather than their bodies, and no source failed Tuesday's fetch.

## Picked

### Autoscience: How we built agent-driven ML exploration at Faire

Faire Engineering (The Craft) — <https://craft.faire.com/autoscience-how-we-built-agent-driven-ml-exploration-at-faire-f3183e7deb29>

An agent runs the whole propose-train-score-keep-or-revert loop, so the number of modeling ideas tried stops being bounded by how much engineer attention is free to review each one. The precondition worth noting is that the accept/reject criterion has to be automated and trusted before the loop is worth anything, which is the same gate to clear before letting an agent iterate on forecast specifications.

### Faire’s agentic development culture

Faire Engineering (The Craft) — <https://craft.faire.com/faires-agentic-development-culture-7aeb03f04bcb>

Faire's stance is to build the agent harness in-house rather than wait for vendors, on the premise that the harness is what converts raw model capability into reliability. A useful frame for deciding which parts of a data-agent setup are worth owning and which are safe to buy.

### Redesigning source control at Anthropic

Anthropic Engineering — <https://www.anthropic.com/engineering/redesigning-source-control>

Skip the version control internals; the liftable pattern is the "superfan" - a per-component agent with access to telemetry and logs, parked in its own Slack channel, which catches subtle anomalies that threshold alerts miss. Also a candid account of the review shift: engineers now check a change's intent rather than every line, and much of the job becomes telling the agent no when it violates a constraint to satisfy a pattern.

### CASTLE: training natural language search before the first real query

Airbnb Tech Blog — <https://airbnb.tech/ai-ml/castle-training-natural-language-search-before-the-first-real-query/>

Relevance labels come out correct by construction - booked-over-viewed pairs decide positive and negative, and the LLM only writes the query - which keeps LLM-as-judge error out of the training set entirely. They also check the synthetic query distribution against real queries with KL divergence rather than assuming realism, both worth copying when building a golden set for an analytics assistant that has no query history yet.

## Skipped

- **Virtual Packer: How Faire estimates shipping costs at checkout** (Faire Engineering (The Craft)) — Replacing a fit on each brand's shipping history with a simulation of the packing priced against live carrier rates is a genuine structural-versus-historical forecasting reframe, but craft.faire.com was unreachable this week and what the listing shows is specific to shipping logistics.
- **Spec, review, ship: How AI is changing the way Faire builds software** (Faire Engineering (The Craft)) — A recap of four conference talks rather than an account of operating the practice, and the agentic development culture post from the same blog covers the same ground with more depth.
- **Staying close to the craft in a rapidly shifting industry** (Faire Engineering (The Craft)) — A candid reflection on moving between IC and manager roles, but it is personal design-career advice rather than how a team is structured, staffed, or sets priorities.
