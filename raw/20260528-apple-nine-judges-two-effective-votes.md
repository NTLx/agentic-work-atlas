---
type: raw
title: "Nine Judges, Two Effective Votes: Correlated Errors Undermine LLM Evaluation Panels"
source: "https://machinelearning.apple.com/research/correlated-llm-evaluation-panels"
author:
  - "Guneet Kohli"
published: "2026-05-28"
created: "2026-09-19"
description: "Apple/2605.29800：9 个 frontier judges、7 个模型家族的面板只有约 2.18 个有效独立投票；实际准确率较独立投票基线低 8–22 个百分点，聚合算法只能弥补很小部分缺口。"
tags:
  - clippings
  - verification
  - agent-evaluation
---

# Nine Judges, Two Effective Votes: Correlated Errors Undermine LLM Evaluation Panels

> Apple research page: https://machinelearning.apple.com/research/correlated-llm-evaluation-panels
> arXiv: https://arxiv.org/abs/2605.29800

## Source locator

- Submitted to arXiv on 2026-05-28; Apple research page lists publication in June 2026.
- Evaluates 9 frontier LLM judges from 7 model families.
- Three natural-language-inference datasets each have 100 human annotations per item; RewardBench is used as an additional pairwise-preference test.
- Kish effective sample size estimates the 9-judge panel at roughly 2.18 effective independent votes.
- Roughly three quarters of nominal panel independence is lost because judges make errors on many of the same items.
- Actual panel accuracy is reported 8–22 percentage points below the independent-voting ideal.
- The strongest single judge matches or outperforms the full panel across the tested conditions.
- Alternative aggregation methods close at most 11% of the gap, even when given correct-answer information.
- Findings remain qualitatively stable across prompt variants, temperature, chain-of-thought and RewardBench.

## Evidence boundary

This study measures correlated errors in static LLM-as-a-judge panels. It does not establish a universal lower bound for every AI-supervision system, does not test interactive environment inspection, and does not show that model-family labels are useless. The result is that family diversity alone does not guarantee statistical independence.
