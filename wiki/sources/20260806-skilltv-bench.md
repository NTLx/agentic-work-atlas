---
type: source-summary
title: "SkillTV-Bench: Benchmarking How Well Judges Perform on Skill-Augmented Agentic Execution"
source_raw:
  - "[[20260806-skilltv-bench]]"
canonical_url: "https://arxiv.org/abs/2608.05573"
raw_state: full
source_locator:
  - "681 trajectories / 50 tasks / 11 domains; task-disjoint evaluation and evolution splits"
  - "case package: trajectory + task-time skills + artifacts + inspectable environment + hidden verifier label"
  - "JudgeSkill inspection plan/log and +14.8 pp same-judge accuracy result"
created: 2026-09-19
updated: 2026-09-19
tags:
  - source-summary
  - verification
  - agent-evaluation
evidence_level: high
claim_type: mixed
---

# SkillTV-Bench: Benchmarking How Well Judges Perform on Skill-Augmented Agentic Execution

## 编译摘要

### 1. 浓缩

- **核心结论 1：证据可见还不够，judge 还需要知道“该检查什么、按什么过程检查”。**
  - 关键证据：每个 SkillTV case 同时提供 trajectory、task-time skills、artifact 与可检查环境；JudgeSkill 显式生成 inspection plan 与 inspection log。
- **核心结论 2：验证知识本身可以外化为可复用资产，而不必修改 judge 模型参数。**
  - 关键证据：同一 agent judge 使用 refined JudgeSkill 后 accuracy 从 43.8% 提升到 58.6%，balanced accuracy 从 56.8% 提升到 63.4%。
- **核心结论 3：judge 改善可以传导到 rollout selection，而不只是离线评分。**
  - 关键证据：10-rollout 条件下，使用 refined JudgeSkill 的 selected-trajectory success 为 45.5%，高于无 refined skill 的 33.9%。

### 2. 质疑

- JudgeSkill 同时改变检查知识、检查顺序与实际执行步骤，因此不能把 +14.8pp 解释成单一“知识变量”的纯因果效应。
- benchmark 与 skill evolution 使用 task-disjoint split，降低直接泄漏，但 JudgeSkill 仍可能学习该 benchmark 家族的共性验证模式。
- verifier-side hidden label 提供稳定裁决锚点，但其 reference correctness 本身不在本研究的主要操纵范围。

### 3. 对标

- 对 EX-002：在 physical visibility 与 active inspection 之间补出第三层——**inspection procedure / verification knowledge**。
- 对 EX-007：JudgeSkill evolution 使用固定 gate 且不改模型参数，是“变更对象可分离”的较干净实例，但仍不是完整 offline→online 安全晋级证据。
- 对 [[Verifiable-Agent-Engineering]]：生产验证不只是“给 judge 工具”，还要把领域性检查程序显式化、版本化并可审计。

## 关联概念

- [[Verifiable-Agent-Engineering]]
- [[Agent-Verification]]
- [[LLM-as-a-Judge]]
- [[Skill-Internalization]]
