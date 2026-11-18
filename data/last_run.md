# Curation run 2026-11-18

- Candidates considered: 22
- Picked: 3
- Explicitly skipped: 19
- Passed over without comment: 0
- Candidates fetched at: 2026-11-18T05:35:22.228531+00:00
- Recency window: 90 days

## The week

Twenty-two candidates, fourteen of them a backlog from the newly added AI Analyst Lab, and three picks that all come down to evaluation: Pinterest's paired test suites and tuning loop for analytics-agent compliance, Anthropic's recommendations for grader calibration and eval statistics, and Netflix's plan-validating agent harness with per-request traces. Tuesday's fetch reported no source failures and sources.yml has no active task sources, but aianalystlab.ai is refused at this environment's proxy (403 on CONNECT), so all fourteen of its posts were judged on a one-line teaser alone; Medium post pages still answer curl with a Cloudflare challenge, though the publication feeds listed in sources.yml carry full post text, so the Netflix, Lyft and Pinterest posts could be read in full this week. Nothing that was fetched attempted to issue instructions.

## Picked

### How Pinterest Improved Analytics Agent Compliance with Loop Engineering

Pinterest Engineering — <https://medium.com/pinterest-engineering/how-pinterest-improved-analytics-agent-compliance-with-loop-engineering-d3c52d0abaa2>

Every compliance rule gets a paired test suite — chats where the rule should fire and chats where it should not — so a prompt change that makes the agent always inspect table metadata or always search dashboards registers as a regression instead of a win, and each tuning iteration starts from a fresh context plus a structured handoff (best change so far, what not to repeat, which suites may not regress). Before trusting any of it they measured their own eval's noise: 10.3% of cases flipped verdict between identical runs, which is the reason a one- or two-case score move is not evidence that a change to a text-to-SQL or triage agent worked.

### Building strong safety evaluations

Anthropic Engineering — <https://www.anthropic.com/research/building-strong-safety-evaluations>

The grader section is the part that transfers to any LLM-as-judge setup: validate the judge against human labels and benchmark that agreement against how often the humans agree with each other, break a rubric into atomic yes/no criteria instead of one overall score, keep design metadata out of the judge's view, and re-grade a sample with a different model to check the conclusion is about the system and not the grader. The statistics advice is the familiar experimentation toolkit pointed at evals — report confidence intervals, and detect small differences between two versions with paired comparisons on the same items rather than comparing aggregate scores.

### Engineering AI Discover

Netflix TechBlog — <https://netflixtechblog.com/engineering-ai-discover-e244944cdc38>

Rather than a free-running reason-call-reason loop, each request produces a plan that code validates before anything executes: capabilities declare their inputs, outputs and failure behavior, and the controller checks that every step is approved, every input has a producer, nothing loops, and the graph terminates — an LLM may propose the path, but code decides whether it runs. Each request also leaves a structured record of plan, step outcomes and rules applied, so a bad answer can be attributed to the plan, the data, a rule or the model, and old requests can be replayed against a new prompt or model; that is the trace layer you need before you can tell an agent regression from noise.

## Skipped

- **Smooth Cruiser at Lyft: Built for Safety and Transparency** (Lyft Engineering) — The best non-pick of the week: scoring each event against the local norm for that road and time, grouping markets by event-rate characteristics with k-means so a score means the same thing in any city, and choosing the rolling window as an explicit stability-versus-responsiveness tradeoff is real metric design — but it is a driver-facing safety score built on phone telemetry, and the ideas are well-executed standard practice rather than something to take back and apply.
- **The Weekly Query: How do you think critically when AI does the analysis?** (AI Analyst Lab) — Newsletter roundup bundling commentary with news links, job listings and workshop promos; aianalystlab.ai refuses this session's requests at the proxy, so the only thing to judge was a one-line teaser.
- **Rebuilding Guardian: How Pinterest Upgraded Its Real-Time Abuse Platform to Modern Infrastructure…** (Pinterest Engineering) — A real-time abuse platform rebuilt onto StarRocks and Flink; the lesson that scale came from splitting wide sparse streams rather than a faster engine is sound, but this is stream-processing infrastructure.
- **Cyber Chaos Monkey: Staying ahead of security threats with AI agents** (Shopify Engineering) — Running a second, differently-aligned judge agent over the executor's live session log with authority to kill it is a genuinely good containment pattern, but the post is offensive security against production infrastructure, which the profile keeps on the skip list.
- **Shopify’s generative discovery model** (Shopify Engineering) — Training and serving a generative retrieval model for search and recommendation — tokenizer choices and recall benchmarks; recommender model architecture, and the evaluation content is lift numbers rather than a method to adapt.
- **Beyond Test Cards: A Fake Payment Provider for Testing at Scale** (Lyft Engineering) — A simulated third-party payment processor for integration testing: test infrastructure for a payments stack, with nothing about data models or experiments.
- **The Weekly Query: How do you build and maintain the context your AI analyst needs to scale to the rest of the company?** (AI Analyst Lab) — Company context and semantic models for an AI analyst is dead-center in scope, but the post is unreadable from this session (proxy refuses aianalystlab.ai) and the teaser also advertises a paid workshop and job listings.
- **The Weekly Query: What is the new job of a data leader?** (AI Analyst Lab) — Data-team leadership is in scope, but the teaser describes a roundup of takeaways, leadership job listings and upcoming workshops, and the page could not be fetched to find the argument.
- **The Weekly Query: Why is AI analytics harder than AI coding?** (AI Analyst Lab) — The capability-versus-reliability framing sounds relevant, but it arrives as one line in a newsletter summary alongside headlines and job listings, and aianalystlab.ai could not be reached to read it.
- **The Weekly Query: What should data teams actually learn about AI right now?** (AI Analyst Lab) — Another weekly roundup of skills commentary, product news, job listings and free workshops; not readable from this session and the teaser offers no method.
- **Onboarding a New Analyst Is Building an AI Analyst** (AI Analyst Lab) — Mapping analyst onboarding onto what an AI analyst needs is exactly this reader's problem, but aianalystlab.ai refuses this session's requests, so the six things it names were never visible and there is no specific idea to write down.
- **ChatGPT's Data Agent: Senior Technical Execution, Junior Business Judgment** (AI Analyst Lab) — Seventy tests on a data agent, with statistical traps passed and organizational judgment failed, is the kind of agent evaluation worth reading; the post could not be fetched, and a two-sentence teaser is not enough to say what the tests were or what to copy.
- **I Quit Three Jobs Over Fake Data Work. Now I Ask Two Questions First.** (AI Analyst Lab) — Metrics that change no decision is a real metric-governance problem, but this is a personal career essay by its own framing, and the page was unreachable.
- **What 8,000 Job Postings Say About AI in Data Roles** (AI Analyst Lab) — An analysis of job postings is closer to labor-market news than to practice, and the profile skips hiring content.
- **Ten Ways an AI Analyst Breaks** (AI Analyst Lab) — A failure catalogue from building AI analysts in production would likely clear the bar if it could be read; aianalystlab.ai is refused at the proxy and the teaser names none of the ten.
- **When the Domain Expert Writes the Exam, the Answer Key, and the Grade** (AI Analyst Lab) — Experts writing evals their own product passes is the LLM-as-judge failure mode this reader cares about, but the five things that keep an eval honest are behind an unreachable page, and Anthropic's eval post covers the same ground readably.
- **What People Still Own When the Analysis Is Automated** (AI Analyst Lab) — Ownership boundaries when analysis is automated is in scope, but with the page unreachable there is only the claim that four things matter and no account of them.
- **Five Things That Took My Base Salary From $92,000 to $286,000 in Four Years** (AI Analyst Lab) — Individual career and compensation advice, not data or engineering practice.
- **Some of the Best Analysts I Ever Worked With Were Product Managers** (AI Analyst Lab) — An argument that analytical work is not bounded by job title; closer to opinion piece than to anything about how a team is structured or how work gets done, and unreadable from this session.
