---
type: source-summary
title: "ACRFence: Preventing Semantic Rollback Attacks in Agent Checkpoint-Restore"
source_raw:
  - "[[20260321-acrfence-semantic-rollback]]"
canonical_url: "https://arxiv.org/abs/2603.20625"
raw_state: full
source_locator:
  - "Action Replay: 10/10 duplicate commits after checkpoint restore vs 0/10 no-checkpoint"
  - "Authority Resurrection: stateless token reuse 2/2; stateful validation rejects tested reuses"
  - "ACRFence replay-or-fork design; mitigation itself not yet evaluated"
created: 2026-09-19
updated: 2026-09-19
tags:
  - source-summary
  - agent-security
  - verification
evidence_level: medium
claim_type: mixed
---

# ACRFence: Preventing Semantic Rollback Attacks in Agent Checkpoint-Restore

## 编译摘要

### 1. 浓缩

- **核心结论 1：恢复 Agent 本地状态，不会恢复外部世界。**
  - 关键证据：checkpoint-restore 试验中 10/10 产生重复外部 commit，而无 checkpoint 基线为 0/10。
- **核心结论 2：传统幂等键可能被 LLM 的重新生成破坏。**
  - 关键证据：恢复后 LLM 可生成新的 request ID 或参数组合，目标服务会把它视作新请求。
- **核心结论 3：授权状态也会发生“复活”。**
  - 关键证据：stateless 单次 token 在恢复后被重新使用的测试 2/2 成功；有服务端消费状态的验证全部拒绝。

### 2. 质疑

- 论文证明了攻击，不等于证明 ACRFence 本身有效；作者明确说明 mitigation 尚未实现评测。
- 10 次和 2 次试验样本很小，只适合作为机制证据。
- 工具边界 effect log 能避免重复执行，但仍不自动提供第三方 provider 的权威 post-state 对账。

### 3. 对标

- 对 EX-005：直接区分 **local rollback / external commit / provider post-state**，支持保留 commit-state uncertainty。
- 对 EX-006：Authority Resurrection 表明控制状态必须绑定到不可回滚的消费记录；只把 token 放在可回退的 Agent 状态中不够。
- 对 [[Agent-Security]]：撤销/恢复阶段必须显式处理 output commit，而不是把 checkpoint 当作事务回滚。

## 关联概念

- [[Agent-Security]]
- [[Agent-Containment]]
- [[Long-Lived-Credential-Risk]]
- [[Verifiable-Agent-Engineering]]
