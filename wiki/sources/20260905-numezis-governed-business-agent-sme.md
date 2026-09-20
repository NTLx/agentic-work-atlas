---
type: source-summary
title: "A governed business agent, in production at a Swiss services SME"
source_raw:
  - "[[20260905-numezis-governed-business-agent-sme]]"
canonical_url: "https://advisory.numezis.com/en/work/business-agent-platform-sme"
raw_state: full
source_locator:
  - "6-month anonymised Swiss SME production engagement"
  - "client/legal-entity retrieval segregation + tool-specific permissions"
  - "no-retention/no-training model calls + immutable read/proposal/decision audit log"
created: 2026-09-19
updated: 2026-09-19
tags:
  - source-summary
  - privacy
  - governance
evidence_level: medium
claim_type: mixed
---

# A governed business agent, in production at a Swiss services SME

## 编译摘要

### 1. 浓缩

- **核心结论 1：任务代理架构不必然要求“全库可见”。**
  - 关键证据：检索按法人和客户文件隔离，连接器按工具单独授权。
- **核心结论 2：权限最小化与模型侧数据保留可以同时做。**
  - 关键证据：模型调用标注为 no retention / no training on client data。
- **核心结论 3：读取本身可以进入审计面。**
  - 关键证据：每次 read、proposal、decision 都进入不可变审计日志，并由外部审计方参与检查。
- **核心结论 4：治理强度可随风险分层，而不是只有“全人工/全自动”二选一。**
  - 关键证据：前三个月所有 outbound action 人工批准，后续低风险动作转为抽样审批。

### 2. 质疑

- 匿名且由实施顾问方发布，缺独立复核。
- 没有披露每个任务实际读取多少记录/文件，因此不能证明“只读必要数据”。
- “模型无保留”不等于整个 agent stack 无持久化；本地日志、检索缓存、memory、DMS 都可能保留数据。
- 6 个月不足以证明长期 privacy drift 不发生。

### 3. 对标

- 对 CR-002：直接反驳“任务代理架构必然导致过宽权限/模型保留”的强版本。
- 对 [[Agent-Data-Minimization]]：证明 permission scope、retrieval segregation、provider retention 可以分别控制。
- 对 [[Least-Agency]]：它补的是“读什么/保留什么”，不只是“能做什么动作”。

## 关联概念

- [[Agent-Data-Minimization]]
- [[Least-Agency]]
- [[MosaicLeaks]]
