# Curation run 2026-11-25

- Candidates considered: 6
- Picked: 2
- Explicitly skipped: 4
- Passed over without comment: 0
- Candidates fetched at: 2026-11-24T21:02:26.646502+00:00
- Recency window: 90 days

## The week

Six candidates, no feed failures, and two picks that sit on either side of the same question: Spotify formalizes when an offline eval score can replace an A/B test (surrogate thresholds, measurement-error correction, an audit pool to catch drift), and Airbnb's de-identification post, read past the privacy subject matter, is a worked example of per-slice metrics and a ship-only-if-nothing-regressed gate. sources.yml has no active task sources. Two candidate pages could not be read: aianalystlab.ai and craft.faire.com both return 403 at this environment's proxy on CONNECT, after one retry each, so those two were judged on their feed text alone. Nothing fetched tried to issue instructions.

## Picked

### When Can You Ship on Offline Evals Alone?

Spotify Engineering — <https://engineering.atspotify.com/2026/11/when-can-you-ship-on-offline-evals-alone/>

Treats offline evals as a surrogate metric and asks what has to be true before an eval score alone can gate a ship decision: you need paired offline/online effects from a homogeneous class of changes, and because both numbers are noisy the naive correlation is attenuated — in their example the eval looked like it explained 24% of online variation when the true figure was 60%, so a weak-looking eval may actually be informative once measurement error is modeled. The practical artifact is the gate itself: thresholds that get stricter as the surrogate relationship weakens, with the middle band still going to an A/B test, plus a random audit pool of ship/kill decisions that keeps being A/B tested so you can detect drift in exactly the region where you stopped observing ground truth. The judge-bias point is the one to carry into agent evals — bias that is the same in both arms cancels, bias that depends on the arm can flip the sign, which is the risk when the thing you changed is the underlying model.

### De-identifying text at scale: How Airbnb protects personal data in AI training

Airbnb Tech Blog — <https://airbnb.tech/infrastructure/de-identifying-text-at-scale-how-airbnb-protects-personal-data-in-ai-training/>

Ignore the privacy plumbing and read section 3 as an evaluation design: no aggregate score is ever reported, every metric is broken out per entity type and per language with the number of labeled instances behind it, plus a confusion table of which type claimed spans belonging to another, because a recognizer that misses and a recognizer that swallows another's spans are different fixes and both vanish in an average. They also score the output the system actually emits rather than an intermediate stage, keep the backend a parameter so candidate models are compared on the same golden sets and adopted only on measured gain, fold every newly found gap into the benchmark, and ship only when no language or entity type that previously worked has regressed — a concrete regression gate to copy for a text-to-SQL or triage agent. The distribution half is a data-contract pattern: the library is a step in the shared ML workflow that a team joins by declaring which columns are sensitive, and the resulting dataset tag plus recorded version and config follows into the model registry to gate deployment, rather than a policy every pipeline is trusted to implement.

## Skipped

- **The Shape of Context at Work** (Notion Blog) — The best non-pick: the one durable observation is that AI workflows built for a shared recurring need (intake, Q&A, support triage) spread to several people while the far more numerous personal ones never do, which is a decent prioritization rule for where to point agents first — but the headline claim that advanced-AI teams make 4.3x the contributions per person is a correlation across its own customers with no attempt at identification, and the rest is a vendor research brief ending in a demo request.
- **Reading between the pixels: what image overlays cost brands and how we detect them at catalog scale** (Faire Engineering (The Craft)) — The transferable piece is a cost cascade — screen with embeddings you already store so the expensive vision model sees under one in ten items — but it is one idea wrapped in catalog image moderation, and craft.faire.com refuses this session's requests at the proxy, so only the feed excerpt was available to judge.
- **The Weekly Query: Where do you find the context your AI analyst needs, and how do you make sure it uses it?** (AI Analyst Lab) — Where an AI analyst's context comes from and how to make it actually get used is dead-center in scope, but this is the weekly newsletter format bundling the tutorial with job listings and promos, and aianalystlab.ai is still refused at this environment's proxy (403 on CONNECT) after a retry, so only the one-line teaser was readable.
- **Building secure mobile apps in the agentic era** (Shopify Engineering) — Attack surface maps and AI code review for mobile app security — mobile platform work and security plumbing, both on the skip list.
