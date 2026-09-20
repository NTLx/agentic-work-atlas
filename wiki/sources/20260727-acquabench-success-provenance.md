---
type: source-summary
title: "Success Is Not Self-Explanatory: Auditing Success Provenance in Agent Evaluation"
source_raw:
  - "[[20260727-acquabench-success-provenance]]"
canonical_url: "https://arxiv.org/abs/2607.24054"
raw_state: full
source_locator:
  - "success provenance definition and CLEAN/GOLD/SHAM matched intervention"
  - "D0 GOLD-SHAM 19.1–25.9 pp result"
  - "D2 distributed-sufficiency result and model-gap compression example"
created: 2026-09-19
updated: 2026-09-19
tags:
  - source-summary
  - verification
  - agent-evaluation
evidence_level: high
claim_type: mixed
---

# Success Is Not Self-Explanatory: Auditing Success Provenance in Agent Evaluation

## 编译摘要

### 1. 浓缩

- **核心结论 1：Agent 得分正确并不能解释它为什么成功。**
  - 关键证据：AcquaBench 把 success provenance 定义为独立评测对象，并使用 CLEAN/GOLD/SHAM 对同一任务的信息状态做 matched intervention。
- **核心结论 2：正确目标值的可得性可以显著改变成功率。**
  - 关键证据：D0 中 GOLD 比 SHAM 高 19.1–25.9 个百分点；两者共享暴露机会与来源结构，区别在于暴露值是否正确。
- **核心结论 3：暴露可以压缩甚至扭曲模型间原有差距。**
  - 关键证据：一个 CLEAN 条件下有支持的 5.0 分模型差距，在 GOLD 原始分数上压缩为 -0.6 分；作者明确指出这不足以证明真实 rank inversion。

### 2. 质疑

- CLEAN/GOLD/SHAM 是受控 benchmark intervention，不代表生产系统中的所有数据泄漏、检索污染或工具旁路。
- “成功依赖正确 target availability”并不自动说明 agent 有意利用泄漏；它测的是信息状态对 outcome 的因果响应，而非主观意图。
- 四个 standardized surfaces 提供较强内部效度，但外部任务结构仍需复现。

### 3. 对标

- 对 EX-004：这是当前证据簇中最直接的 **success provenance intervention**；它把“拿到正确答案”与“按授权路径完成任务”分开。
- 对 [[20260218-openai-evmbench]]：EVMbench 强化 execution truth；AcquaBench 则回答 execution/outcome 即使为真，成功是否由被允许的信息状态产生。
- 对 [[Verifiable-Agent-Engineering]]：高质量 evaluation 不只需要 post-state，还需要记录 agent 在成功前获得了哪些信息、这些信息是否被授权。

## 关联概念

- [[Verifiable-Agent-Engineering]]
- [[Agent-Verification]]
- [[Evaluator-Miscalibration]]
- [[Agent-Observability]]
