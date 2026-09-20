---
type: raw
title: "MemSecBench: Tracking Agent Memory Poisoning from Persistence to Consequence and Repair"
source: "https://arxiv.org/abs/2607.27080"
author:
  - "Xuanze Chen"
  - "Xukang Xie"
  - "Wentao Fu"
  - "Jiajun Zhou"
  - "Shanqing Yu"
  - "Qi Xuan"
published: "2026-07-29"
created: "2026-09-19"
description: "310 cases / 48 contexts / 24 stack configurations；用 Write→Execute→Forget 协议把 memory 持久化、下游动作后果与 selective repair 串成同一生命周期。"
tags:
  - clippings
  - agent-security
  - verification
---

# MemSecBench: Tracking Agent Memory Poisoning from Persistence to Consequence and Repair

> Canonical source: https://arxiv.org/abs/2607.27080

## Source locator

- 310 cases from 48 realistic contexts.
- Controlled Write–Execute–Forget protocol.
- Exact stack configuration = agent harness × memory backend × LLM backend.
- 24-configuration matrix: two harnesses, four memory backends, three LLM backends.
- Across all configurations, malicious memory persists in 84.2% of cases and full Write–Execute succeeds in 50.3%.
- Among successfully poisoned cases, 59.6% complete the full Execute chain; 56.1% achieve selective repair.
- Largest matched Native configuration differences: 16.1 pp end-to-end attack success and 41.3 pp selective repair.

## Evidence boundary

The benchmark links memory persistence to consequence and repair more directly than single-stage memory tests, but it remains an isolated runtime with benchmark-defined checkpoints and adjudication. Selective repair is not equivalent to revoking all downstream external effects already propagated beyond the memory system.
