---
type: source-summary
title: "Saga pattern with Dataverse or Dynamics 365"
source_raw:
  - "[[20260919-microsoft-saga-compensation]]"
canonical_url: "https://learn.microsoft.com/en-us/dynamics365/guidance/reference-architectures/saga-pattern-dataverse"
raw_state: full
source_locator:
  - "per-system retry strategy and fatal-error branch"
  - "compensation transactions for systems that already processed earlier steps"
  - "separate compensation queues/functions and stage logging"
created: 2026-09-19
updated: 2026-09-19
tags:
  - source-summary
  - agent-security
evidence_level: high
claim_type: extracted
---

# Saga pattern with Dataverse or Dynamics 365

## 编译摘要

### 1. 浓缩

- **核心结论 1：跨系统失败恢复不是“把全局状态回滚到过去”。**
  - 关键证据：Saga 把流程拆成各系统自己的本地事务；前序系统已经提交的变化需要后续 compensation 显式处理。
- **核心结论 2：retry 与 compensation 是不同机制。**
  - 关键证据：瞬时错误走 retry；fatal error 才触发补偿路径，两者需要独立策略。
- **核心结论 3：补偿本身是新的外部动作。**
  - 关键证据：参考架构为补偿配置独立 queue/function，并要求逐阶段记录结果。

### 2. 质疑

- 这是分布式系统参考架构，不是 Agent 安全效果研究。
- 补偿不能保证恢复到完全相同的历史世界状态，尤其是通知、数据泄露、付款结算等不可逆后果。
- 文档定义了架构语义，没有提供 Agent 场景的 rollback success / MTTR 实测。

### 3. 对标

- 对 EX-005：给“撤销/恢复”提供成熟分布式系统基线：**stop future work ≠ compensate committed work ≠ verify canonical post-state**。
- 对 [[20260321-acrfence-semantic-rollback]]：ACRFence 展示 Agent checkpoint 如何触发 output-commit 问题，Saga 则提供传统系统如何显式设计补偿的参照。
- 对 [[Agent-Security]]：recovery 应作为一条有状态工作流审计，而不是一个 cancelled=true 标志。

## 关联概念

- [[Agent-Security]]
- [[Operational-Responsibility]]
- [[Alert-Closed-Loop]]
- [[Verifiable-Agent-Engineering]]
