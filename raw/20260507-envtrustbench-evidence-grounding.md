---
type: raw
title: "EnvTrustBench: Evaluating LLM Agents' Evidence-Grounding Robustness"
source: "https://github.com/EnvTrustBench/EnvTrustBench"
published: "2026-05-07"
created: "2026-09-19"
description: "公开 project draft；把 true environment state、false path、verification opportunity 与 validation oracle 分离，测量 agent 对误导性环境证据的过度信任。"
tags:
  - clippings
  - verification
  - agent-evaluation
---

# EnvTrustBench: Evaluating LLM Agents' Evidence-Grounding Robustness

> Canonical source: https://github.com/EnvTrustBench/EnvTrustBench
> Public project page: https://envtrustbench.github.io/EnvTrustBench/
> Public release uses the 2026-05-07 final aggregate matrix; submitted manuscript and raw traces are withheld.

## Source locator

- Framework objects: initial workspace W0, environment evidence E0, task q, validation oracle Omega.
- Each case distinguishes true environment state, correct path, false path, and a verification opportunity.
- Five evidence-grounding patterns: persistent observation poisoning, runtime feedback manipulation, temporal state misgrounding, stale derived memory, unverified executable artifact.
- Public matrix: 11 scenarios, 55 machine-scoreable cases, 14 model-scaffold stacks, 3,850 accepted pass/fail runs.
- Aggregate public result: 3,206 false-path runs, FPCR 83.3%; stack-average FPCR spans 55.3% to 96.7%.

## Evidence boundary

The public manuscript and raw run directories are not released. The available evidence is a project draft, aggregate tables, public dataset metadata and code/docs; therefore the aggregate findings are useful but less independently auditable than a fully released paper plus raw traces.
