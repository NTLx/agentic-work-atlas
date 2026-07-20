---
title: "If AI is so great, why isn't it working?"
source: "https://www.varickagents.com/blog/if-ai-is-so-great-why-isn-t-it-working"
author: "Daniel Kornum (Varick Agents)"
date: "2026-07-19"
added: "2026-07-20"
tags:
  - ai-enterprise
  - ai-failure
  - ai-implementation
  - agentic-engineering
  - organizational-change
  - ai-operations
---

Companies are spending millions on AI, but nothing's really changed. At Varick Agents, we've seen why most efforts fail, and what actually works.

by Daniel Kornum

In the last 12 months, I've had the opportunity to chat with over 100 C-Suite executives at the largest companies across America. The conversation usually goes as follows: they spent millions trying to bring AI into their business. Leadership buzzes non-stop about "going AI-first", yet when asked point-blank what has changed in the day-to-day, the answer is some version of nothing.

## The models are good enough. Stop blaming the models.

It's been a year and a half since GPT-o3, the first model where I could hand off a real task and not babysit the output too much. Then came Opus 4, GPT-5, and Gemini 3. Now we have Opus 4.7 and GPT 5.5. Pricing fell off a cliff, context windows expanded massively, and tool calling became much more accurate.

In the same window, harnesses became very robust and more scientific. Two years ago "harnesses" meant copy-pasting prompts off Twitter. Today it's recursive context engineering, eval pipelines, and tool stacks that genuinely stick. Anthropic wrote a canonical text on it (Building Effective Agents), and the punchline of that paper is "find the simplest solution possible, only increase complexity when needed."

## So why isn't it working inside enterprise?

**MIT NANDA's GenAI Divide report, August 2025**: 5% of integrated AI pilots are pulling millions in value. The other 95% have nothing to show for it. BCG, Deloitte, RAND, IBM, Gartner, McKinsey all ran their own studies with their own methodologies and they all converge on the same number. BCG: 4% have hit AI value at scale. Deloitte: 6% achieve AI ROI within a year. RAND: 80%+ of AI projects fail, twice the rate of normal IT projects. That number has been flat through every model generation. **Despite models improving, failure rates have not come down. The model is not the bottleneck.**

## AI is working for one group: software engineers

The biggest winner from 18 months of AI improvement has been engineers writing code in Cursor, Claude Code, Codex, etc. GitHub's 2024 study clocked Copilot users at 55% faster on real tasks. Anthropic internal study August 2025: AI cuts developer task completion time by roughly 80%. Sundar Pichai at start of 2026: 75% of new code at Google is AI-generated and engineer-approved.

## Every other category vendors promised: flat metrics

- **Sales ops**: reps spend 28% of their time selling. 24% hit quota. Unchanged from 2022.
- **Finance**: average close cycle has barely moved.
- **Marketing**: AI content tools save an hour a week. Pipeline contribution unchanged.
- **Operations**: arguably more bogged down trying to wrangle AI products.

## Why AI works for engineers and not anyone else

Engineering work has four properties no other enterprise function has:
1. **Bounded**: functions take inputs and return outputs. Dependencies are explicit and importable.
2. **Checkable**: compilers, tests, type systems. Feedback loop: seconds.
3. **Structured**: code lives in files, version control, deterministic build pipeline.
4. **Verifiable**: a PR is a discrete artifact. Reviewer can assess in 10 minutes.

Contrast with finance close: AP, AR, intercompany reconciliations, FX, accruals, journal entries spanning NetSuite, Concur, three banks, two ERPs from acquisitions. "Process" is documented in an SOP that doesn't match reality. None of it is bounded, checkable, structured, or verifiable.

## The four failure modes

### 1. They skip the audit
Building before understanding the actual workflow. The gap between SOP and actual workflow is the **conformance gap**: typically 30%+, in heavy exception-driven workflows over 70%. When you build for the documented process, you automate 70% of volume and break on 30%. The 30% creates more work than before.

### 2. They throw everything at LLMs
Using LLM for parts that don't need it. Production systems that work are 85% code and 15% LLM. LLM goes where judgment lives. The rest is deterministic logic.

### 3. Agent sprawl
Every employee with AI access turns into their own agent factory. A 200-person ops org ends up with 50-100+ separate AI workflows, each solving similar problems in 7 different ways. No common spine, no shared memory. When a model gets deprecated or an employee leaves, engineering spends half its time playing janitor. Fix: single orchestration layer with shared infrastructure.

### 4. They treat AI as a side-project instead of infrastructure
AI deployments that pay off treat AI as continuously evolving infrastructure with a dedicated team. They monitor quality, swap models, retire agents, renegotiate vendors. Anthropic alone has retired roughly 9 models in 18 months. In April 2026 Anthropic acknowledged engineering errors degraded Claude Code performance for over a month.

## What the 5% that succeeds does

1. **Audit before building.** 4+ weeks mapping actual workflow. Digital twin showing conformance gaps, pattern-matchable vs judgment-required.
2. **Decompose until mostly deterministic.** 5-10 deterministic steps with one or two model calls in specific places.
3. **Single orchestration layer.** One platform for all agents. Shared context, shared infrastructure. Sprawl dead on arrival.
4. **Model-agnostic.** Route to best-fit model at any moment. When models change, routing layer absorbs it.
5. **Continuously evolving infrastructure.** Dedicated team for ongoing tuning, retiring, shipping improvements.

## The labs are quietly conceding the same point

Every model lab has figured out that selling the model alone isn't enough. You need the model, plus the runtime, plus a team that embeds inside the enterprise. **Process is the bottleneck. It's been the bottleneck the whole time.**

## 6-month deployment path

- Month 1: audit (digital twin of actual workflow)
- Month 2: architect (pattern vs judgment, deterministic vs probabilistic)
- Months 2.5-4: build (soft launch, humans approve every action)
- Month 4-6: go live (watch metrics that matter for 2 weeks before declaring victory)
- Month 6: stand up continuous-tuning function

"The 'models got smart' chapter is over. The next decade belongs to the companies that build the operational layer underneath the models."
