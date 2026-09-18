---
type: raw
source: "https://intelligentartifact.com/posts/gpt-5-6-luna-vs-gpt-6-astra-code-review/"
author:
  - "Intelligent Artifact / Entelligence"
published: "2026-09-15"
created: "2026-09-18"
description: "对低成本模型与前沿模型进行代码审查路由比较的厂商实验。"
tags:
  - clippings
  - agentic-engineering
  - code-review
  - verification
  - model-routing
---


Entelligence sells model routing and AI code review tooling, so this is a vendor testing its own premise: what do you give up if every pull request goes to the cheapest model? The test ran 50 public pull requests from Cal.com, Sentry, Discourse, Keycloak and Grafana — each with a bug deliberately introduced — through GPT-5.6 Luna and GPT-6 Astra with an identical prompt on identical diffs. Every PR predates both models’ training cutoffs, so the code was new to them.

Two terms matter. A “verified” bug is one that two models independently judged to be real against the diff; “precision” is the share of a model’s comments that survived that judgment. One Luna review cost $0.0041. One Astra review cost $0.113.

**The headline numbers**

- Luna found 69 verified bugs, Astra 92 — about 75% of the total for $0.20 against $5.66 across all 50 pull requests, 3.6% of the spend.
- Per verified bug: $0.0030 for Luna, $0.061 for Astra. Astra cost 20x more.
- Luna was noisier. 74% of its 93 findings held up against 96% of Astra’s 96, so roughly one Luna comment in four was wrong.
- It was faster and more verbose: 23 seconds per review against 36, and 3.1x more output tokens — still far cheaper, because its output price is 42x lower.

**Where the cheap model falls over**

- Per repository, Luna stayed within two bugs of Astra on Sentry, Discourse and Grafana, but fell to 21 against 30 on Cal.com.
- Keycloak was the wide gap. It is an identity and access management server, so most of its benchmark pull requests change authentication and permission logic: Luna found 6 verified bugs to Astra’s 14, and only 50% of its Keycloak findings held up against 93% for Astra.
- By bug class, security was the worst split — 9 of 24 for Luna against 19 for Astra — with concurrency at 10 to 13 and data and logic bugs at 39 to 47.
- The two examples the authors quote are invisible line by line: federated recovery codes never marked as used, so one could be redeemed more than once; and a global view permission overriding denials set on individual clients. You only see them by working out what the permission model permits after the change.

The authors’ own line: Luna is good enough for everyday correctness bugs at that price, and they would not let it review authentication or permission code on its own.

**The structural point**

A diff alone does not tell a model what kind of change it is reviewing. Knowing a file sits on an authorization path, that a function is called from a login flow, or that a similar change caused an incident last quarter is what should decide how carefully the change gets read — and that context is exactly what a diff-only reviewer lacks.

So the useful shape is not “which model” but “which changes deserve which model,” and the routing decision depends on information the diff does not carry.

**What the methodology can and cannot show**

- The defects were planted in the pull requests for the benchmark, so a model cannot simply have memorized the fix — though the surrounding code is public and old, which helps a model that knows what the correct version looks like.
- Every pull request predates both models’ cutoffs, so the date split one reader asked for — do the rankings hold on changes the models could not have seen? — cannot be run here. The post says so plainly.
- Astra is both a contestant and one of the two judges. Requiring GPT-5.6 Sol to agree reduces that bias without removing it.
- Repeat runs move a lot. Ten pull requests were reviewed three times per model: Astra re-found 67% of its verified bugs in both repeats, Luna 47%. Every single-run number in the post, including the 92, is one draw.
- The models were not rivals so much as complements. Of 143 verified bugs, 44 were found by both, 48 only by Astra and 25 only by Luna. Running both would have caught 117 of 143 for $5.86 — 25 extra bugs for twenty cents.
- 26 bugs were found by neither, caught only by Sol or the vendor’s own reviewer, and that is a floor: bugs nobody flagged never entered the pool.

[The 137-comment thread on Hacker News](https://news.ycombinator.com/item?id=49703003) mostly argues about the thing the article measures last: what surrounds the model.

**What the thread adds**

- **CharlieDigital** — a concrete setup that made cheap models work: run review in multiple cycles on the diff only, emit a few findings at a time, give the reviewer memory of previous findings so it can check whether they were fixed, feed it canonical docs encoding your human reviewers’ heuristics, and run several narrow reviewers rather than one general one (“Security, performance, structural, database, etc. Each a separate prompt and persona”). They report Luna and even 5.4-mini reliably found issues in code written by Opus and Fable.
- **jbellis** — the same idea as architecture: a stronger model as coordinator with six specialist subagents on the cheap model. “Narrowing down what a smaller model like Luna needs to look for / care about helps them do better work; then the larger model synthesizes and fills in any gaps.”
- **therealdrag0** and **amluto** — the harness objection, from two directions. therealdrag0, replying to the diff-only advice: “I found AI reviews garbage until they stopped being only on the diff and were actually able to query real context.” amluto: “This article is missing an incredibly important detail: what is the harness doing?” — they get good results pointing a coding harness at a built checkout so the model can use the shell to understand the repo, and doubt a weaker harness would score the same.
- **gregwebs**, with **samusiam** and **rektomatic** — the counter to the price framing. gregwebs: “They state Luna is good enough, but its accuracy of findings is 74% whereas Astra is 96%. Dealing with false positives is expensive.” rektomatic adds the compounding case: if a stronger model reads a review full of false positives, “it burns tokens to figure out.” samusiam calls the 22-point gap “massive.”
- **nonethewiser**, whose comment heads HN’s ordering with 14 replies — process rather than tooling: use AI in review, but do not pipe raw model output into the pull request for the author to sort out. “Everything it says is something the PR author needs to validate as relevant, helpful, etc. A human needs to do that before confronting the author with it.” **stefangordon** answers with the opposite practice — agents reviewing pull requests, the author’s agent reading the feedback and fixing it, then merging when green, with the reviewer cloning dependent repositories, reading open and historical issues and checking post-deploy logs.
- **InsideOutSanta** — a reason to pick by something other than price: Chinese models for review “because you can actually tell them to take an adversarial stance and actively look for security issues without risking refusals,” naming GLM-5.3 as good but slow on large pull requests.
- **SwellJoe** — the failure mode nobody benchmarked. A Copilot review suggestion accepted without close human attention turned an administrative config tool into an overlay service; later models read the change and its changelog entry as policy rather than a mistake, so subsequent “fixes” piled bandages on it — “a fractal of fuckery I had to untangle with a good model and some close human supervision.”

**Where the thread disagrees**

- **StevenWaterman** thinks the cost debate is a distraction: “$0.10 extra per pr review is nothing. What software company is willing to accept worse reviews and less bugs found to save 10 cents?” **mooman219** answers that “worse” is the wrong frame when each model finds bugs the other misses, and reads the post as an argument for a blend. **jstummbillig** argues cheapness may matter after all if more code becomes short-lived and frequently rewritten.
- **avadodin** goes furthest: “Any model is good enough. Even tiny local models can provide some value.” **nvch** pushes back hard — “With tiny models, we’re getting into the territory of horoscopes and divination. While it is possible for a sentient being to derive value by using them as a random seed for thinking, the value is produced by something different from the seed.” **6thbit** lands between them on the specific claim under test: “Luna is not able to find non-trivial impacts from the changes at hand.”

**The question the thread kept asking**

Three commenters converge from different angles on the same missing detail: the post reports model quality while leaving the system around the model undescribed. amluto asks what the harness is doing; therealdrag0 argues context access decided whether reviews were any use at all; aleksi notes the article never states reasoning levels, and that its closing line — “the prompts, raw model outputs, judge verdicts, bug-class labels, repeat runs and scoring scripts are committed with this article” — reads well but does not say where, concluding “this, and the fact that the article doesn’t mention reasoning levels, sounds fishy to me.”

That gap is worth taking seriously on its own terms, because it is the same gap the article’s central finding points at from the other side. Its conclusion is that a reviewer needs to know which changes are security-sensitive before it can review them at the right level of care; the thread’s complaint is that we cannot see what the reviewers here knew. OriginalPenguin raises the adjacent coverage question — why Sol and Terra were left out — and **samuelknight** answers that the comparison was deliberately narrow: Luna because OpenAI cut its price 5x, Astra because it is the frontier model, and the specific question was whether the cheap one is usable.

*On reading comments as evidence: HN handles are pseudonymous and the site publishes no per-comment scores, so the ordering here is HN’s own ranking, not a vote. This is a slice of the thread, not a consensus — the setups described are individual practices, reported as such.*

