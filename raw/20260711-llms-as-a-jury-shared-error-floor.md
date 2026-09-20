---
type: raw
title: "LLMs as a Jury: Cross-Model Consensus Can Outperform Process Reward Models for LLM Reasoning"
source: "https://arxiv.org/abs/2607.10139"
author:
  - "Ning Liu"
published: "2026-07-11"
created: "2026-09-19"
description: "跨模型 consensus verifier 在 7 个 reasoning benchmark 上测量 error decorrelation 与 shared-error floor；数学任务接近零，GPQA 为 0.030，MMLU-Pro 为 0.143，显示共模误差下界强依赖任务错误结构。"
tags:
  - clippings
  - verification
  - agent-evaluation
---

# LLMs as a Jury: Cross-Model Consensus Can Outperform Process Reward Models for LLM Reasoning

> Canonical source: https://arxiv.org/abs/2607.10139
> Version used: v3, revised 2026-08-17.

## Source locator

- Studies cross-model consensus as a verifier signal: independently trained models solve the same problem independently; the agreement structure selects among candidate reasoning chains.
- Seven benchmarks: AIME-2024, AIME-2025, MATH-500, OlympiadBench, GPQA, MMLU-Pro and GSM8K.
- Main cross-family panel includes Qwen3-235B, DeepSeek-V3.2, Claude Sonnet 4.6 and Kimi-K2.5.
- With Qwen3-235B candidate generation, cross-model consensus is the strongest non-oracle selector on all seven reported benchmarks.
- The paper models a shared-error floor: cases in which the full panel converges on the same wrong answer.
- Reported empirical floors include:
  - AIME-2024: 0.000
  - AIME-2025: 0.000
  - MATH-500: 0.004
  - GSM8K: 0.014
  - OlympiadBench: 0.040
  - GPQA: 0.030
  - MMLU-Pro: 0.143
- Repeating with DeepSeek-V3.2 as generator preserves the cross-model advantage, reducing concern that the result is specific to one generator family.
- The paper also notes that two of six unanimous-wrong GPQA cases were grading artifacts, making the 0.030 empirical figure a conservative upper bound for genuine shared misconceptions in that inspection.

## Evidence boundary

The shared-error floor is conditional on the task, answer space, panel composition, common evidence and consensus rule. Near-zero floors on several math benchmarks directly reject a universal positive lower bound. The study does not test human adjudicators, deterministic external checkers, interactive evidence acquisition or production-agent supervision.
