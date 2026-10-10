# Curation run 2026-10-10

- Candidates considered: 19
- Picked: 2
- Explicitly skipped: 7
- Passed over without comment: 10
- Candidates fetched at: 2026-10-10T01:31:30.530092+00:00
- Recency window: 90 days
- FEED FAILED: DoorDash Engineering (HTTP Error 403: Forbidden)

## The week

Nineteen candidates, mostly Notion and Uber backlog surfacing now that those page sources are live. Two picks, both Notion agents grounded in governed data: the internal analytics assistant and the documentation-upkeep workflow. Two caveats on this run: DoorDash Engineering failed for the second step too (Tuesday's fetch got a 403, and this session's network policy blocks the domain outright), and no post body on any source was reachable, so every judgment rests on titles and feed summaries rather than the posts themselves.

## Picked

### How we built a personal data scientist for every Notion employee

Notion Blog — <https://www.notion.com/blog/how-we-built-a-personal-data-scientist-for-every-notion-employee>

An internal analytics assistant grounded in governed Snowflake tables plus the company's own written context, rather than in the warehouse alone. The pairing is the transferable part: a data agent needs the curated layer and the docs that define it, or it answers confidently from tables nobody agreed on.

### How Notion built a Custom Agent workflow to keep Academy content current

Notion Blog — <https://www.notion.com/blog/how-notion-built-a-custom-agent-workflow-to-keep-academy-content-current>

An agent spots content gaps, drafts the fix, and only approved drafts get written back to the live platform. That propose-then-approve shape is the one to copy for keeping data model documentation current: the agent does the detection and drafting, a human gate stands between it and anything that ships.

## Skipped

- **From Activity to Intent: Generating User Journeys with LLMs** (Pinterest Engineering) — Using an LLM to name intent across long event histories is a real idea, but the payoff here is personalization and notification ranking, which the skip list covers, and the lesson is not about evaluation or experimentation.
- **Building Shared Memory for AI Agents in Notion** (Notion Blog) — Durable facts and decisions written down for later agents is close to the memory an operational triage agent needs, but it is framed as a product feature rather than a design or evaluation account to adapt.
- **A skills library for every agent** (Notion Blog) — Governing reusable agent instructions is in scope, but this reads as a product announcement rather than a lesson from operating it.
- **Designing MCP Gateway Uber's MCP Management Platform** (Uber Engineering) — A central registry and governance layer for agent tools touches harness design, but it is platform plumbing sized for Uber's service mesh rather than something a single data team could lift.
- **Scaling AI in Legal: Building Uber’s Redlining Agent** (Uber Engineering) — An agent rollout outside data work; it would clear the bar if it taught evaluation or adoption, but the listing shows neither and the post body was unreachable this week.
- **Taming the ML Firehose: Scaling Feature Consistency** (Uber Engineering) — Offline and online feature consistency rhymes with data contracts, but the post is ML-platform plumbing rather than a modeling or governance idea.
- **Rebuilding Notion’s lexical search reindexer** (Notion Blog) — Replacing a manual multi-week process with a proper pipeline is sound hygiene, but this is search-index infrastructure, not curated-model or metric work.
