---
type: source-summary
title: "Decentralized Granular Access Control for Agentic AI Systems in Critical Infrastructure"
source_raw:
  - "[[20260614-decentralized-granular-access-control-agentic-ai]]"
canonical_url: "https://arxiv.org/abs/2607.22611"
raw_state: full
source_locator:
  - "20+ agents / 60+ deterministic playbooks / thousands of daily operations"
  - "8 months production; zero unauthorized writes reported"
  - "compound identity + five-level permissions + decentralized policy ownership"
created: 2026-09-19
updated: 2026-09-19
tags:
  - source-summary
  - agent-security
  - governance
evidence_level: medium
claim_type: mixed
---

# Decentralized Granular Access Control for Agentic AI Systems in Critical Infrastructure

## 编译摘要

### 1. 浓缩

- **核心结论 1：细粒度权限是可以在生产 Agent fleet 中长期运行的，不只是架构白皮书。**
  - 关键证据：20+ agents、60+ deterministic playbooks、每日数千操作、8 个月生产周期。
- **核心结论 2：写权限可以按风险从 autonomous read 分离出来。**
  - 关键证据：compound identity、五层权限和 progressive trust escalation 将高风险写入放入更强控制路径。
- **核心结论 3：零未授权写入不能替代数据最小化指标。**
  - 关键证据：论文没有报告 read volume、query scope、context retention、deletion/TTL。

### 2. 质疑

- 部署主体匿名，效果为论文自报。
- “zero unauthorized writes” 是 action safety 指标，不是 privacy/data minimization 指标。
- 即使所有 agent 都只读，也可能发生过度读取、过宽检索或长期上下文积累。

### 3. 对标

- 对 CR-002：削弱“Agent 形态必然导致过宽权限”的强版本，但不能证伪“实际读取/保留可能过度”的风险。
- 对 [[Least-Agency]]：提供 production-scale 细粒度授权实证。
- 对 [[Agent-Data-Minimization]]：明确 permission minimization 与 read/retention minimization 是不同测量轴。

## 关联概念

- [[Least-Agency]]
- [[Agent-Data-Minimization]]
- [[Agent-Security]]
