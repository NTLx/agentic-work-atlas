---
type: source-summary
title: "Access change propagation in Google Cloud IAM"
source_raw:
  - "[[20260920-google-iam-access-change-propagation]]"
canonical_url: "https://docs.cloud.google.com/iam/docs/access-change-propagation"
raw_state: full
source_locator:
  - "eventual-consistency boundary for access changes"
  - "policy change typically ≈2 min, potentially 7+ min"
  - "group membership changes can take minutes to hours or longer"
created: 2026-09-20
updated: 2026-09-20
tags:
  - source-summary
  - agent-security
  - verification
evidence_level: high
claim_type: extracted
---

# Access change propagation in Google Cloud IAM

## 编译摘要

### 1. 浓缩

- **核心结论 1：revoke request 与 deny-effective 是两个时间点。**
  - Google 明确把 IAM 访问变更定义为 eventual consistency；近期撤销的角色或权限在传播完成前仍可能被使用。
- **核心结论 2：传播时间依赖变更路径。**
  - 直接 policy 变更通常约 2 分钟、可能 7 分钟以上；group / nested-group membership 变化可能达到数小时或更久。
- **核心结论 3：撤销链需要记录具体 authority surface。**
  - 同样是“撤销访问”，policy、group、nested group 的传播对象与时间特征不同，不能只有一个 revoked=true。

### 2. 质疑

- 官方数字是平台级经验范围，不是 hard SLA，也不是 Agent 工具调用的 p95/p99。
- IAM deny-effective 只覆盖未来授权判断，不覆盖已经进入目标系统的请求或外部 effect。
- 不能把最慢 group propagation 直接外推到所有 Google Cloud 权限撤销。

### 3. 对标

- 对 EX-005：提供 authority-stop propagation 的生产平台边界，强化 revoke_requested_at → deny_effective_at 必须分开记录。
- 对 [[Agent-Security]]：权限撤销指标需要带 surface/type，而不能把 role/policy/group/session 混成一个状态。
- 对 CR-004：应同时记录策略更新时间与真实 deny-effective observation，避免只凭配置写入时间推断生效。

## 关联概念

- [[Agent-Security]]
- [[Long-Lived-Credential-Risk]]
- [[Distinct-Principal-Identity]]
- [[Agent-Observability]]
