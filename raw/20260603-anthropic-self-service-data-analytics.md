---
title: "How Anthropic enables self-service data analytics with Claude"
source: "https://claude.com/blog/how-anthropic-enables-self-service-data-analytics-with-claude"
author:
  - "Chen Chang"
  - "Clement Peng"
  - "Justin Leder"
  - "Johanne Jiao"
  - "Josh Cherry"
published: "2026-06-03"
created: "2026-06-03"
tags:
  - "clippings"
  - "agentic-analytics"
  - "AI-deployment"
  - "context-engineering"
  - "skills"
---

# How Anthropic enables self-service data analytics with Claude

**Authors:** Chen Chang, Clement Peng, Justin Leder, Johanne Jiao, and Josh Cherry (Data Science and Data Engineering team). Additional thanks to Michael Segner.

**Source:** [Anthropic Claude Blog](https://claude.com/blog/how-anthropic-enables-self-service-data-analytics-with-claude)

**Published:** June 3, 2026

---

## Introduction

The article addresses the traditional difficulty of enabling self-service business analytics. Data teams historically faced a tradeoff: denormalized "wide" tables caused overlapping, inconsistent views as businesses scaled, while ringfenced environments missed the long tail of business questions and produced metric/dashboard bloat.

LLMs offer a third path, but simply pointing Claude at a warehouse and letting agents execute creates what the authors describe as "a false sense of precision." Initial elation turns to dread when stakeholders become separated from the underlying infrastructure, documentation, and expertise that previously guided them.

**Key data point:** At Anthropic, 95% of business analytics queries are automated via Claude, with ~95% accuracy in aggregate. This frees the data science team to focus on "causal modeling, forecasting, and machine learning."

The post promises to share tips for maximizing Claude's ability to drive self-serve business insights, including why accuracy is a context/verification problem rather than a code generation issue, three failure modes causing most errors, the agentic analytics stack built to address them, effectiveness measurement, and a basic skill template (in the appendix).

---

## Data is not software

The authors argue LLMs' generative abilities are "a double-edged sword" — mechanisms enabling creative solutions can also hallucinate erroneous output.

**Comparison with coding agents:** Coding is "an open-ended solution space that rewards the models' creativity," where documentation and tests provide natural guardrails. Analytics, by contrast, "often [has] only a single correct answer using a single correct source in which there's no deterministic way of proving the correctness."

**Central problem statement (paraphrased):** For self-service agentic analytics, the core challenge is the ability to map a user's question to specific, up-to-date entities in the data model and know the correct way of working with them. If that mapping succeeds, the resulting SQL execution becomes trivial.

### Three failure modes accounting for most inaccurate responses

1. **Concept <> entity ambiguity:** With hundreds of viable options in a data model, the agent cannot choose the correct fields. Example: measuring active users — what actions constitute "active"? Are fraudulent users included? What lookback window?

2. **Data staleness:** Data sources, business definitions, and schemas change constantly; assets and agent knowledge go stale and return subtly wrong answers.

3. **Retrieval failure:** The right information may be in the data model and properly annotated, but given the vastness of the search space, the agent simply doesn't find it.

---

## Agentic analytics stack

Each layer of the stack attacks one or more of the three problems:

1. **Entity ambiguity** → data foundations and sources of truth shrink the space of plausible entities until there's a single governed answer.
2. **Staleness** → maintenance and validation processes keep everything from rotting as the business changes.
3. **Retrieval failure** → skills make sure the agent reliably finds and correctly uses that answer.

### Data foundations

The most important aspect of accuracy is strong data foundations: data models, transforms, tests, tables in a warehouse, and the metadata describing them. Standard practices still apply, including dimensional modeling, shift-left testing, and freshness/completeness checks.

What changes is that "the end user of your data model is no longer a data expert (e.g. data scientist), but rather agents acting on behalf of users with varying degrees of data expertise." Results cannot require the user to validate underlying correctness because the end user doesn't know how.

**Practices that work especially well:**

- **Create canonical datasets:** The most common failure is the agent's inability to map a concept to the single correct table, column, and metric definition when multiple plausible candidates exist with subtly different implementations. The fix is "fewer, more heavily governed logical models" — curate a small set of canonical, single source-of-truth datasets, then "aggressively deprecate the near-duplicates." Physical rollups/caches should derive mechanically from canonical models.

- **Enforce your standards:** Foundations only hold if canonical models and metric definitions are enforced by tooling (agent structurally routed to them first), by CI (changes that bypass them fail review), and by mandate (downstream teams build on the governed layer or explain why not). Without enforcement, governance "quickly decays back to the multiple candidates problem."

- **Colocate artifacts:** Nearly all data code (modeling, semantic layer, reference docs, canonical dashboard definitions) lives in a single repo, with CI checks protecting cross-layer integrity. If a modeling change would break a downstream dashboard or invalidate a documented metric, CI flags it and the fix ships in the same PR.

- **Treat metadata as a first-class product:** Coding agents perform well partly because codebases are "legible" — READMEs, type signatures, docstrings. A warehouse can be equally legible if column/table descriptions, canonical metric definitions, grain documentation, valid value ranges, lineage, ownership, and model tiering are maintained with the same rigor as transformations.

### Sources of truth

If data foundations are the warehouse itself, sources of truth are the reference surfaces the agent consults to navigate it. This layer reduces concept-entity ambiguity. Listed roughly in descending order of trust:

- **Semantic layer:** The compiled metric and dimension definitions. If a question maps cleanly to a defined metric, the agent calls a function and gets one number — "the same number every other surface in the company produces." Agents are "structurally required (by skill instruction) to leverage the semantic layer first." One idea that did NOT work: bootstrapping the semantic layer by having an LLM auto-generate metric definitions from raw tables and query logs. It "produced plausible-looking definitions that encoded the very ambiguities we were trying to eliminate" and was net-negative on evals. The recommendation: generate the documentation with Claude, but have a human own the definition.

- **Lineage and the transformation graph:** When the semantic layer doesn't cover a question, lineage and table ranking let the agent reason about which upstream models feed a concept, which are deprecated, and which share grain.

- **Query corpus:** Historical SQL from dashboards, notebooks, and prior analyses. Key finding: "giving the agent raw retrieval access to thousands of prior queries moved accuracy by less than a point." Unstructured retrieval couldn't map a new question to the right precedent. What works is distilling the corpus into structured per-domain reference docs and reusable analysis patterns described in skills. Treat query history "as raw material for curation, not as a source of truth the agent reads directly."

- **Business context:** "The layer most teams skip, and the one we underrated the longest." An agent that doesn't understand your business will answer what the user asked, but not what they meant. Anthropic pipes in a company knowledge graph of indexed docs, roadmaps, decision logs, and organizational structure so the agent can resolve ambient references and ask better clarifying questions.

The common failure pattern across all four: poor or stale documentation. Claude is useful for closing the gap (drafting column descriptions, proposing metric docs, flagging undocumented models in CI), but curation and ownership are managed by humans.

### Skills

If sources of truth are the agent's declarative knowledge (what a metric means), a skill is its procedural knowledge: which sources to consult in what order, how to navigate ambiguous data, and what a finished analysis looks like.

In Claude Code, a skill is "a folder of markdown the agent reads on demand."

**Key data point:** Without skills, Claude's ability to answer analytics questions accurately "didn't exceed 21% on our evals." Adding skills gets these numbers "consistently above 95% in aggregate and regularly around 99% in certain domains."

**Best practices:**

- **Create pairwise skills:** A **knowledge** skill acts as a thin top-level router that allows additional domain details to load on demand. It says "try the semantic layer first, but if there's no coverage, here are ~30 reference files for this domain." This router is the answer to retrieval failure: "rather than letting the agent search a million-field warehouse, it narrows the space to a few dozen curated files before a query is ever written." The **unbook** skill encodes the process a senior analyst would follow: clarify the question, find sources (via the knowledge skill), run the query, and loop the result through adversarial review sub-agents. It also bundles reusable analysis patterns (retention curves, rate decomposition, funnel analysis).

- **Create proper reference docs:** Written for retrieval by an LLM. They describe tables (grain, scope, and exclusions), the mechanics of gotchas, and explicit routing triggers without prescriptive recipes that go stale. The article includes a reference doc skeleton template with sections: Quick Reference (Business Context, Entity Grain, Standard Hygiene Filter), Dimensions, Key Tables, Gotchas, Best Practices / Common Query Patterns, and Cross-References.

- **Treat skill maintenance as a first class citizen:** "Skill docs describe a data model that changes daily, so without active maintenance they're wrong within weeks." Offline accuracy drifted from ~95% at launch to ~65% over a month before they treated this as an engineering problem. Solution: colocating skill markdown files in the same repo as transformation models, so the PR that changes a model is the same PR that updates the doc. A code-review hook flags any reporting-model change that doesn't touch a skill file. Roughly 90% of data-model PRs now include a skill change in the same diff.

- **Create a consistent and seamless experience across all surfaces:** The same skill must provide the same answer in Slack, in the IDE, in a dashboard tool, and in standalone agent sessions. Achieved by ensuring one canonical source (the data repo) and that skill changes sync automatically. On merge, skills sync to a plugin marketplace (for IDE users), to cloud-storage blobs (for hosted apps), and are served directly as resources over MCP. Designed for portability by avoiding hardcoded repo paths and surface-specific namespaces.

---

## Validation

### Offline evaluations

A common pattern: data teams set up elaborate analytic environments without any process to understand agent accuracy.

**Two kinds of offline evals at Anthropic:**
- **Dashboard-based evals:** Auto-generated by Claude (then human validated), covering the most common stakeholder questions.
- **Long tail evals:** Feed Claude business context (roadmaps, table docs) and have it generate plausible questions across the rest of the domain.
- They also continuously harvest every time a stakeholder corrects the agent in a thread.

**Best practices:**
- **Anchor ground truth so it can't drift:** Pin every eval to a snapshot date, write it against a stable fact table, or have the grader judge the agent's query rather than its number. Wire the suite into CI.
- **Store results like telemetry, not like test logs:** Every run lands in a warehouse table with the skill version, git SHA, model ID, per-assertion pass/fail, token count, and wall-clock.
- **Gate launches per domain:** A domain owner can't announce the agent to stakeholders until their slice of the eval set clears some threshold (~90% initially).
- **Create the appropriate number of evals:** Depends on business area complexity and data model complexity. Diminishing returns past a few dozen per topic (e.g., "growth"), and the ceiling drops with each new model generation.
- **Offline eval accuracy should be ~100%** — every correct answer should also be hitting the semantic layer. This doesn't tell you the system won't produce a wrong answer, just that there are no obvious gaps.

### Ablation techniques

Every structural decision about the skill is made by holding the offline eval set fixed, varying exactly one component, and comparing pass rates. Each run takes about an hour.

- **Design for null results:** "Our most useful ablation was a negative one." They gave the agent direct grep access to their entire dashboard, transformation, and analyst-notebook SQL (thousands of files), verified in transcripts that it actually read them before every answer. "Accuracy moved by less than a point in either direction." They checked confounds: was the answer actually in the corpus for the questions it got wrong? About 80% of the time, yes. Did "answer present" predict "now gets it right"? No. "The information was there, the agent saw it, and it still didn't use it." That experiment revealed the bottleneck wasn't access to prior work — it was structure (mapping a question to the right entity). That insight redirected months of roadmap.

- **Ablate at PR granularity:** Every meaningful skill edit gets a before/after run on the relevant eval slice, with the delta in the PR description.

- **Keep a short list of what didn't work:** Two examples: stacking additional rounds of doc refinement past a certain point (three consecutive net-negative iterations — docs getting longer, not better), and swapping the adversarial reviewer to a cheaper model to cut latency (lost most of the accuracy wins, for no real speedup).

### Online validation

- **Adversarial review:** Employing a Claude skill to aggressively challenge all underlying assumptions on a potential final answer "increased accuracy by 6% within our eval set, but at the cost of 32% more tokens and 72% higher latency."
- **Provenance footer:** Every response carries a footer with which source tier it came from (semantic layer > curated reference > raw table), how fresh the underlying data is, and who owns the model. A "raw table, freshness unknown" footer is a signal to verify before forwarding upstream.
- **Data quality checks:** Adding basic data quality checks to ensure the referenced field is up-to-date, complete, and has no anomalies.
- **Passive monitoring:** Two production signals tracked continuously: the share of agent queries that resolve through the semantic layer, and the share of responses that use correction language. Both feed a dashboard reviewed weekly alongside the offline pass rate.
- **Active correction harvesting:** A scheduled agent scans stakeholder channels every few hours for correction language, drafts a one-line fix to the relevant reference doc, and opens a PR tagged to the domain owner. The same corrections feed back into the offline eval set.

**Silent failures:** The failure mode none of this fully catches — the answer is wrong but looks plausible and is used without objection. Mitigations include the provenance footer, explicit human sign-off on anything leadership-bound, and a standing eval for each domain's top KPIs that sanity-checks against the blessed dashboard daily. The authors note "we don't have a robust solution yet."

---

## Getting started

For those starting from zero: "a handful of canonical datasets, a few dozen offline evals, and a thin knowledge skill will capture most of the upside; everything else in this post is what we added once those were built."

Key questions to align on with your organization:

- **How important is a correct answer today vs. in the future?** "We often see companies building a significant amount of infrastructure to account for current model shortfalls that become moot once those models improve."
- **How do you anticipate the complexity of your business to change over time?** Some processes may be overkill if you don't produce much data, have few consumers, or your data model will remain simple.
- **How technical is the intended audience of the output?** If building for data scientists who can recognize incorrect answers, you may tolerate more errors than if the audience has no familiarity with the underlying data model.
- **How much are you willing to spend for improved accuracy?** Processes like adversarial validation can significantly improve accuracy but at higher cost and latency.
- **What is your comfort around access controls and internal data privacy?** Agents are more performant with more context, but broad data access cuts against most companies' governance posture. This determines whether you build one agent or many scoped ones.

Closing insight: "Our greatest gains have come from addressing each of the three failure modes: collapsing ambiguity into a single governed answer, making the answer easily discoverable, and flagging when either has gone stale."

---

## Appendix: Skill File Skeleton

The article provides a detailed skeleton of their main warehouse skill file. It is a large YAML-front-matter + markdown template with bracketed placeholders, structured as follows:

**Front matter:** name, version, description (with invocation triggers and exclusions).

**Top-level sections:**
- **Description:** "The single source of truth for safe and effective [warehouse] querying." Agent acts as a Data Analyst providing strategic insights. Out-of-scope decisions are surfaced as data only, with the owning team noted.
- **Executing queries:** Priority order: managed connection (if available), CLI fallback (if installed), or ask user to authenticate then stop.

**Semantic Layer (REQUIRED first step):**
- Described as "the mandatory default path for every data question." Raw SQL via reference docs is the fallback, used only after the semantic-layer path is shown not to cover the ask.
- Required workflow: Load > Discover (search measures/dimensions by keyword; always check segments) > Compile + run > Fallback.
- Explicit "Don't bail early" guidance listing common excuses agents use to skip the semantic layer (custom date filtering/cohorts, needs a join, etc.) and rebutting each.
- Date windows & timezone conventions decided before querying.

**PART 1: MUST KNOW (Read First for Every Request)**
- Quick Start Workflow: check for red flags, escalate out-of-scope items, clarify the request, check for existing dashboards, identify the data source, execute the analysis, deliver insights.
- Business Context: Entity Disambiguation (MUST CLARIFY), Business Terminology, Data Integrity Requirements.

**PART 2: HOW TO DO (Follow During Execution)**
- Technical Execution Guide with PII protection guidance.
- Analysis Best Practices Guide including mandatory adversarial SQL review via a sub-agent for every query before the final answer, and provenance reporting with source tier, confidence, reviewer, freshness, and owner.

**PART 3: DATA REFERENCES & RESOURCES**
- Knowledge Base Navigation with per-domain entries (a few dozen in total), each pointing to reference markdown files and dashboard JSON files.
- Troubleshooting Guide covering missing information scenarios and field naming gotchas.

---

## Key Quantitative Data Points

| Metric | Value |
|--------|-------|
| Business analytics queries automated via Claude at Anthropic | 95% |
| Aggregate accuracy of those queries | ~95% |
| Accuracy without skills (on evals) | Did not exceed 21% |
| Accuracy with skills (aggregate) | Consistently above 95% |
| Accuracy with skills (certain domains) | Regularly around 99% |
| Offline accuracy drift (no maintenance, 1 month) | ~95% to ~65% |
| Data-model PRs including a skill change | ~90% |
| Adversarial review accuracy improvement | +6% |
| Adversarial review token cost increase | +32% |
| Adversarial review latency increase | +72% |
| Accuracy gain from raw query corpus access | Less than 1 point |
| Launch gate threshold (initial) | ~90% |
| Answer present in corpus for wrong answers | ~80% |
