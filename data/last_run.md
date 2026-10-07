# Curation run 2026-10-07

- Candidates considered: 4
- Picked: 2
- Explicitly skipped: 2
- Passed over without comment: 0
- Candidates fetched at: 2026-10-06T17:05:56.735654+00:00
- Recency window: 90 days

## The week

A thin week - four candidates, all feeds fetched cleanly with no failures. Two cleared the bar on the same theme of making definitions and environments explicit enough for machines to use: Pinterest enforcing metric quality at creation so agents can query the metrics layer, and Shopify's reproducible sandbox for scoring shopping agents.

## Picked

### Metrics Board: Building an Agent-ready Metrics Layer

Pinterest Engineering — <https://medium.com/pinterest-engineering/metrics-board-building-an-agent-ready-metrics-layer-2c8fefe68756>

Metric quality and ownership are enforced when a metric is created rather than audited later, which is the thing that makes the same definitions safe for an agent to query instead of letting it loose on raw tables. Worth reading as a design for your own metric layer: the intake checks and the producer-ownership model are the transferable parts, not the petabyte scale.

### ShopGym: Realistic, reproducible sandboxes for shopping agents

Shopify Engineering — <https://shopify.engineering/shopgym>

A generated store plus generated tasks gives every agent run the same fixed environment, so a change to the agent can be measured rather than demoed. The same shape applies to your data agents: a frozen snapshot of the warehouse and a generated question set turn text-to-SQL or triage evaluation into a repeatable regression test.

## Skipped

- **Introducing AgentHub: Booking.com Platform for Modular Travel AI Agents** (Booking.com ML & DS) — A config-driven internal agent platform announcement; the reusable-component and democratization framing leaves no evaluation or operations lesson to adapt, and Booking's earlier agent-evaluation and observability posts already covered the useful ground.
- **Personalization without user identity** (Airbnb Tech Blog) — Cold-start ranking features and their serving path - recommender architecture on the skip list, and the lesson is not about evaluation or experimentation.
