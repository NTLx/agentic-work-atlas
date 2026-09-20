---
type: raw
title: "HarnessEvolve: Learning from Reference Trajectories for Reliable Agent Self-Evolution"
source: "https://arxiv.org/abs/2609.00829"
author:
  - "Wen Jiang"
  - "Mingmin Chu"
  - "Yimeng Tian"
  - "Qianxin Zhang"
  - "Haofei Yang"
  - "Rui Yang"
  - "Yang Liu"
  - "Tao Lv"
  - "Fangming Li"
published: "2026-09-01"
created: "2026-09-19"
description: "将 execution/evaluation/optimization/gating 解耦，使用 reference trajectories、质量门、近期批次回归门和 held-out validation 约束 harness 自演化。"
tags:
  - clippings
  - verification
  - agent-evaluation
---

# HarnessEvolve: Learning from Reference Trajectories for Reliable Agent Self-Evolution

> Canonical source: https://arxiv.org/abs/2609.00829

## Source locator

- Harness includes prompts, skills, tools and execution logic.
- Four modules: execution, evaluation, optimization and gating.
- Reference trajectories are generated with ground-truth answers, then checked by an evaluation agent for legitimate tool/reasoning paths.
- Quality gate checks data leakage and prompt bloat.
- Performance gate accepts a candidate only if it improves the current batch while not degrading recent batches beyond tolerance.
- Accepted harnesses enter a snapshot pool; epoch-end validation selects the best snapshot on a held-out validation set.
- Five reported benchmarks include open-domain and enterprise tasks; CloudCoreNetwork-QA reports a 21.6 percentage-point improvement over the strongest baseline in the paper's setting.

## Evidence boundary

Structural separation and held-out validation improve auditability and regression control, but the evaluator, reference generation and gates still belong to the experimental system. The paper does not establish an immutable independent safety policy, production canary, deployment rollback or post-rollback behavioral verification.
