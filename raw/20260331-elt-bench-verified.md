---
type: raw
title: "ELT-Bench-Verified: Benchmark Quality Issues Underestimate AI Agent Capabilities"
source: "https://arxiv.org/abs/2603.29399"
author:
  - "Christopher Zanoli"
  - "Andrea Giovannini"
  - "Tengjun Jin"
  - "Ana Klimovic"
  - "Yotam Perlitz"
published: "2026-03-31"
created: "2026-09-20"
description: "ELT-Bench-Verified：100 个 ELT tasks 中审计 81 个有 transformation outputs 但 column-level evaluation 失败的任务，82.7% 至少含一个 benchmark-attributable error；三工程师盲标验证，修正 evaluation logic 并移除 30 个无法可靠校正的 GT columns 后，同一 SWE-Agent + Claude Sonnet 4.5 的 transformation success 22.66%→32.51%。"
tags:
  - clippings
  - verification
  - agent-evaluation
---

# ELT-Bench-Verified

> Canonical source: https://arxiv.org/abs/2603.29399
> Version used: v2, 2026-04-02.

## Source locator

- Benchmark contains 100 ELT pipeline tasks.
- With the upgraded model, 96 tasks pass extraction/loading; 87 fail transformation; 81 produce transformation outputs but fail column-level evaluation and form the main audit scope.
- Auditor-Corrector methodology combines LLM-driven root-cause analysis with independent human validation.
- Three annotators achieve:
  - Fleiss kappa 0.851 for high-level attribution;
  - Fleiss kappa 0.755 for the full 14-category taxonomy.
- 82.7% of the 81 audited failed transformation tasks contain at least one benchmark-attributable error.
- Error classes include:
  - rigid evaluation scripts penalizing semantically equivalent values;
  - ambiguous data-model specifications;
  - ground-truth calculation errors.
- For 30 columns across 24 tasks flagged as ground-truth calculation errors, three data engineers independently reconstruct SQL using only specification, schemas and source data.
- Pairwise exact-match agreement across those engineers averages 57.8%, indicating no reliable authoritative correction for the affected columns.
- The verified benchmark therefore:
  - refines comparison logic for booleans, floats, formats, NULLs and ordering;
  - removes the 30 unreliable ground-truth columns rather than inventing replacements.
- Using the same SWE-Agent with Claude Sonnet 4.5, transformation success rises from 22.66% to 32.51%, a 9.85 percentage-point increase attributable to benchmark correction in that comparison.

## Evidence boundary

The 82.7% figure applies to the 81 transformation-failure tasks in the audit scope, not all 100 tasks. Benchmark correction changes evaluation logic and removes unreliable ground-truth columns; it is not a randomized reference-only intervention. The 22.66% to 32.51% comparison holds agent/model setup fixed, but does not by itself prove a universal ranking effect across all agents. Low agreement on the 30 ground-truth columns is evidence for ambiguity, not a license to replace them by majority vote.
