---
type: raw
title: "Rethinking the Evaluation of Harness Evolution for Agents"
source: "https://arxiv.org/abs/2607.12227"
author:
  - "Yike Wang"
  - "Huaisheng Zhu"
  - "Zhengyu Hu"
  - "Yige Yuan"
  - "Zhengyu Chen"
  - "Shakti Senthil"
  - "Hannaneh Hajishirzi"
  - "Yulia Tsvetkov"
  - "Pradeep Dasigi"
  - "Teng Xiao"
published: "2026-07-14"
created: "2026-09-19"
description: "用 matched feedback/inference budget 的 test-time search 对照与 disjoint held-out tasks 重新评估 harness evolution，揭示搜索预算和 benchmark 过拟合混淆。"
tags:
  - clippings
  - verification
  - agent-evaluation
---

# Rethinking the Evaluation of Harness Evolution for Agents

> Canonical source: https://arxiv.org/abs/2607.12227
> Version used: v2, revised 2026-08-27.

## Source locator

- Requires harness evolution to be compared with simple task-level search under matched feedback and inference budgets.
- Evaluates on Terminal-Bench 2.1 with GPT-5.4 and Claude Opus 4.6.
- Without unit tests, reported average pass@1: initial harness 68.2, parallel sampling 72.3, harness evolution 67.4, harness scaling 71.8.
- With unit tests, average pass@1: parallel sampling 86.0, sequential refinement 84.3, harness evolution 75.8; reported pass@5: 86.0, 91.8 and 86.2 respectively.
- Generalization setting uses 45 train, 10 validation and 34 held-out test tasks; harness evolution improves Claude Opus 4.6 by 1.2 pp and GPT-5.4 by 0 pp, 0.6 pp average.

## Evidence boundary

These results are a counterexample to interpreting benchmark gains as harness benefit under the studied methods and Terminal-Bench setting. They do not establish that all harness evolution is ineffective; instead they show that search budget and same-benchmark reuse must be controlled before attributing a reusable capability gain.
