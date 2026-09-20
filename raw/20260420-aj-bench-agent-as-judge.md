---
type: raw
title: "AJ-Bench: Benchmarking Agent-as-a-Judge for Environment-Aware Evaluation"
source: "https://arxiv.org/abs/2604.18240"
author:
  - "Wentao Shi"
  - "Yu Wang"
  - "Yuyang Zhao"
  - "Yuxin Chen"
  - "Fuli Feng"
  - "Xueyuan Hao"
  - "Xi Su"
  - "Qi Gu"
  - "Hui Su"
  - "Xunliang Cai"
  - "Xiangnan He"
published: "2026-04-20"
created: "2026-09-19"
description: "ACL Findings 2026；155 tasks / 516 trajectories，按 information acquisition、state verification、process verification 评估 Agent-as-a-Judge。"
tags:
  - clippings
  - verification
  - agent-evaluation
---

# AJ-Bench: Benchmarking Agent-as-a-Judge for Environment-Aware Evaluation

> Canonical source: https://arxiv.org/abs/2604.18240
> Project: https://aj-bench.github.io/
> Venue: Findings of ACL 2026.

## Source locator

- Benchmark scope: Search, Data Systems, GUI.
- Dataset size: 155 tasks and 516 annotated trajectories.
- Judge capabilities: information acquisition, state verification, process verification.
- Evaluation: F1 alignment to ground-truth annotations.
- Official repository reports Agent-as-a-Judge gains up to 13.41 percentage points overall F1 over LLM-as-a-Judge baselines.

## Evidence boundary

AJ-Bench tests whether a judge can actively acquire environment evidence and verify state/process. It does not isolate verifier-family independence, and its labels remain benchmark-provided ground truth rather than an independent study of reference integrity.
