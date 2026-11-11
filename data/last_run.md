# Curation run 2026-11-11

- Candidates considered: 14
- Picked: 3
- Explicitly skipped: 11
- Passed over without comment: 0
- Candidates fetched at: 2026-11-10T18:32:13.650635+00:00
- Recency window: 90 days

## The week

Fourteen candidates and three picks: the Airbnb classifier benchmark and Anthropic's agent-memory post both carry methods that transfer straight to applying agents to data work, and Faire's "product builders" post is the organizational counterpart to the same shift. Tuesday's fetch reported no source failures and sources.yml has no active task sources, but craft.faire.com is refused at this environment's proxy (403 on CONNECT) and every Medium-hosted post (Netflix, Lyft, Pinterest) answers curl with a Cloudflare challenge, so those five were judged on feed titles and summaries alone; nothing in the pages that did load attempted to issue instructions.

## Picked

### Frontier quality at 1% of the cost: a production benchmark of LLM classifiers

Airbnb Tech Blog — <https://airbnb.tech/ai-ml/frontier-quality-at-1-of-the-cost-a-production-benchmark-of-llm-classifiers/>

A fine-tuned 2B classifier matched frontier-API quality on a real production task at 35ms median latency and roughly 1% of the cost, and the post states the four conditions that made fine-tuning pay: high volume (above about 30 requests per minute), a tight latency budget, needing a thresholdable score rather than a fixed true/false verdict, and having labeled in-domain examples. The score-versus-verdict point is the one to carry into operational triage classifiers, where moving the precision/recall trade-off should not require rewriting a prompt.

### The components of agent memory

Anthropic Engineering — <https://www.anthropic.com/research/components-of-agent-memory>

Notes an agent writes mid-session go stale or start wrong, so memory gets a separate offline pass that re-checks each note against the original transcript and keeps the always-injected top layer small. The useful experiment is the wiki over a 350k-file internal corpus: an agent-maintained linked knowledge map beat raw search on questions spanning several documents, and missing facts were fixed by giving one agent per document a page of its own quoting terms verbatim instead of several agents summarizing into one shared table — a concrete pattern for agent-written documentation over curated tables.

### Accelerating product development in the AI age: How Faire developed product builders

Faire Engineering (The Craft) — <https://craft.faire.com/accelerating-product-development-in-the-ai-age-how-faire-developed-product-builders-fe70044854b5>

Faire reports per-engineer complexity-weighted PR throughput roughly tripling with AI coding, which left the heavyweight up-front spec and prototyping process as the constraint, and their answer was to grow engineers into "product builders" who carry product definition alongside the code. The question to borrow is which parts of your own intake and spec process exist only because building used to be the expensive step.

## Skipped

- **AI Product Management at Spotify: A View From Three Angles** (Spotify Engineering) — Splitting AI product ownership into research, model, and experience layers is a real ownership-boundary question, and "evaluation is a continuous product, not a pre-launch phase" is worth keeping, but the post stays at the level of three job descriptions rather than anything a team lead could act on.
- **Fact-Checking at Scale: Building a More Accurate and Efficient Synopsis Factuality System** (Netflix TechBlog) — A production factuality-checking pipeline should have an LLM-as-judge lesson in it, but the title and summary name no method and netflixtechblog.com answers curl with a Cloudflare challenge, so there was nothing to judge the approach on.
- **Scaling Model Evaluation at Pinterest with Ray (Part 4)** (Pinterest Engineering) — Model evaluation is in scope, but part four of a Ray series is about distributed-execution plumbing and accumulators rather than how to decide what to evaluate; the page is also unreachable behind Cloudflare.
- **Hiring Junior Engineers** (Lyft Engineering) — How a team staffs itself is in scope, but this reads as advice to candidates on clearing the entry-level bar rather than to someone deciding how to staff a team, and the page could not be fetched to check.
- **How we rebuilt the Shopify app in 12 weeks** (Shopify Engineering) — Redesigning tooling and workflow around validation once agents write the code is the most interesting non-pick of the week, but it is a mobile app rebuild, which the profile keeps on the skip list even when the lesson is organizational.
- **Notion as the context system for humans and agents** (Notion Blog) — Agents maintaining a context store for other agents is adjacent to agent-written documentation, but the post is product positioning for Notion rather than an account of how it works.
- **Skipper, Airbnb’s embedded workflow engine, is now open source** (Airbnb Tech Blog) — An embedded durable-workflow library for Java and Kotlin services — orchestration plumbing, with nothing about how curated data models get built or trusted.
- **Reflex: an architecture for building mobile apps with agents** (Shopify Engineering) — An architecture for letting agents test mobile app behavior without an emulator; the agent-testing idea is interesting but the surface is mobile.
- **Safe and Efficient Multi-Epoch Embedding Training** (Pinterest Engineering) — Training-side work on large ID embedding tables for ranking and retrieval: recommender model architecture, and the lesson is not about evaluation or experimentation.
- **How we integrated Liquid Glass without sacrificing Faire’s brand** (Faire Engineering (The Craft)) — Adopting Apple's design language across two native apps — frontend and app platform work.
- **Five stories of teams getting more done with Notion MCP** (Notion Blog) — Five customer stories about connecting Notion to agents; vendor case studies with no method to adapt.
