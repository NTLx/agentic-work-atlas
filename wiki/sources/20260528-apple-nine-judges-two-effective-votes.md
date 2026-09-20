---
type: source-summary
title: "Nine Judges, Two Effective Votes: Correlated Errors Undermine LLM Evaluation Panels"
source_raw:
  - "[[20260528-apple-nine-judges-two-effective-votes]]"
canonical_url: "https://machinelearning.apple.com/research/correlated-llm-evaluation-panels"
raw_state: full
source_locator:
  - "9 frontier judges / 7 model families"
  - "Kish effective sample size about 2.18"
  - "8–22 pp deficit vs independent-voting ideal; aggregation closes at most 11% of gap"
created: 2026-09-19
updated: 2026-09-19
tags:
  - source-summary
  - verification
  - agent-evaluation
evidence_level: high
claim_type: mixed
---

# Nine Judges, Two Effective Votes

## 编译摘要

### 1. 浓缩

- **核心结论 1：模型数量和模型家族数量都不是独立性的充分代理。**
  - 关键证据：9 个 frontier judges 来自 7 个模型家族，但有效样本量只有约 2.18。
- **核心结论 2：面板增益被共同错误显著压缩。**
  - 关键证据：实际准确率比独立投票理想基线低 8–22 个百分点；最佳单 judge 在测试条件下可匹配或超过完整面板。
- **核心结论 3：聚合算法不能修复输入判断信号本身的相关性。**
  - 关键证据：多种 aggregation strategy 最多只补回约 11% 的缺口。
- **核心结论 4：相关性不是一个明显可由 prompt trick 消掉的局部现象。**
  - 关键证据：结论对 prompt、temperature、CoT 与 RewardBench 变体保持稳定。

### 2. 质疑

- 数据主要是静态 judgement/pairwise evaluation，不包含 live environment state verification。
- 研究证明的是 panel error correlation，不是“不同模型家族没有价值”。
- 有效样本量约 2.18 是该面板/任务分布上的测量结果，不是所有 LLM jury 的固定常数。

### 3. 对标

- 对 CR-003：把“跨家族”从名义独立降为待测变量；真正要测的是 error covariance / effective sample size。
- 对 [[LLM-as-a-Judge]]：ensemble 不能仅凭模型品牌多样性宣称独立。
- 对 [[Verifiable-Agent-Engineering]]：verifier independence 应由错误结构实测，而不是由模型数量推断。

## 关联概念

- [[LLM-as-a-Judge]]
- [[Verifiable-Agent-Engineering]]
- [[Evaluator-Miscalibration]]
