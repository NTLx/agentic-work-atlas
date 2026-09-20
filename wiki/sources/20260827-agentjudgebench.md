---
type: source-summary
title: "AgentJudgeBench: A Multi-Difficulty Benchmark for Evaluating LLM Judges on Agentic Tool-Calling"
source_raw:
  - "[[20260827-agentjudgebench]]"
canonical_url: "https://arxiv.org/abs/2608.26623"
raw_state: full
source_locator:
  - "3,808 instances / six DAG topologies / three difficulty tiers"
  - "paired with-ground-truth vs without-ground-truth conditions across five generators and six judges"
  - "difficulty degradation, hard no-GT 77–82% band, over-anchoring cases and rubric mitigation"
created: 2026-09-19
updated: 2026-09-19
tags:
  - source-summary
  - verification
  - agent-evaluation
evidence_level: high
claim_type: mixed
---

# AgentJudgeBench: A Multi-Difficulty Benchmark for Evaluating LLM Judges on Agentic Tool-Calling

## 编译摘要

### 1. 浓缩

- **核心结论 1：reference availability 本身是 judge 行为变量，而不是天然“越多越好”。**
  - 关键证据：benchmark 对同一类 judge 做 paired with/without-ground-truth 对照；总体上无 ground truth 时随难度退化更快，但部分 frontier judge 暴露 ground truth 后 alignment 反而下降。
- **核心结论 2：task difficulty 可以形成与模型规模无关的 judge ceiling。**
  - 关键证据：hard、无 ground-truth 条件下六个 judge 收敛到约 77–82% alignment，模型规模没有消除该窄带。
- **核心结论 3：judge quality 依赖“拿什么当 reference”。**
  - 关键证据：有 ground truth 时某模型最匹配 programmatic reference，而 human validation 又由另一 judge 最贴近人工判断，说明“最佳 judge”依赖评测锚点。

### 2. 质疑

- programmatic reference 本身不是不可错的绝对真值；这正是 EX-004 要继续区分 reference truth 与 judge alignment 的原因。
- 77–82% band 是特定 DAG/tool-calling 构造中的结果，不应外推为所有 Agent judge 的普遍上限。
- ground-truth exposure 同时改变可用信息与 anchoring 行为，不能仅凭总 alignment 判断哪一种条件更“真实”。

### 3. 对标

- 对 EX-004：首次在当前证据簇中提供明确的 **reference condition paired intervention**，证明 reference availability 会直接改变 judge 行为。
- 对 EX-001：即使使用多个不同规模 judge，也可能在困难条件下收敛到相近误差区间；但这不等价于独立性因果检验。
- 对 [[Evaluator-Miscalibration]]：judge 对 programmatic reference 与 human judgment 的最佳匹配者不同，说明 evaluator calibration 必须绑定目标定义。

## 关联概念

- [[Verifiable-Agent-Engineering]]
- [[LLM-as-a-Judge]]
- [[Evaluator-Miscalibration]]
- [[Agent-Verification]]
