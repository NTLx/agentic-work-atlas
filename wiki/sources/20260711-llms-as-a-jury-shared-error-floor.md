---
type: source-summary
title: "LLMs as a Jury: Cross-Model Consensus Can Outperform Process Reward Models for LLM Reasoning"
source_raw:
  - "[[20260711-llms-as-a-jury-shared-error-floor]]"
canonical_url: "https://arxiv.org/abs/2607.10139"
raw_state: full
source_locator:
  - "cross-family verifier panel across seven reasoning benchmarks"
  - "task-conditioned empirical shared-error floor"
  - "generator-family robustness check"
created: 2026-09-19
updated: 2026-09-19
tags:
  - source-summary
  - verification
  - agent-evaluation
evidence_level: high
claim_type: mixed
---

# LLMs as a Jury

## 编译摘要

### 1. 浓缩

- **核心结论 1：跨模型 consensus 的收益来自错误去相关，而不是“模型多”本身。**
  - 关键证据：独立训练模型各自解题，错误答案通常分散，正确答案更容易形成 modal agreement。
- **核心结论 2：shared-error floor 是任务条件量，不是普遍常数。**
  - 关键证据：AIME 两个数据集的经验 floor 为 0，MATH-500 为 0.004；GPQA 为 0.030，MMLU-Pro 为 0.143。
- **核心结论 3：任务的错误吸引子结构决定 consensus 上限。**
  - 关键证据：科学/多选任务更容易让不同模型落入同一个 plausible wrong answer；数学错误更分散。
- **核心结论 4：generator 与 verifier panel 要分开。**
  - 关键证据：换用 DeepSeek-V3.2 生成 candidate 后，跨模型 consensus 的相对优势仍复现。

### 2. 质疑

- shared-error floor 只约束 agreement-based verifier；外部 theorem checker、执行 oracle、human adjudicator 不受这个 floor 直接约束。
- “跨家族”仍不是统计独立的同义词，panel composition 需要实测。
- GPQA 的 0.030 中包含 grading artifact；因此不能把表面 unanimous-wrong 全部解释成模型共同 misconception。

### 3. 对标

- 对 CR-003：直接否定“所有 AI 监督都有一个不可消除的正 shared-error floor”的强版本；应改写为某些任务 × panel × evidence 条件下存在可测 shared-error floor。
- 对 [[LLM-as-a-Judge]]：jury consensus 可以优于单模型 self-scoring，但其 ceiling 由 shared error 决定。
- 对 [[Verifiable-Agent-Engineering]]：独立性门需要任务条件化，且不能取代外部 truth/provenance 门。

## 关联概念

- [[LLM-as-a-Judge]]
- [[Verifiable-Agent-Engineering]]
- [[Agent-Verification]]
