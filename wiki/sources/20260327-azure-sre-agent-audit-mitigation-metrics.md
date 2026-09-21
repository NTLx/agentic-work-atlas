---
type: source-summary
title: "Azure SRE Agent: governed mitigations, audit events, and incident metrics"
source_raw:
  - "[[20260327-azure-sre-agent-audit-mitigation-metrics]]"
canonical_url: "https://learn.microsoft.com/en-us/azure/sre-agent/audit-agent-actions"
raw_state: full
source_locator:
  - "Application Insights customEvents: tool, CLI, incident lifecycle and approval events"
  - "TraceId / CorrelationId / ThreadId / CallId plus IncidentId and incident timestamps"
  - "diagnose → permission check → execute/propose → verify; incident outcome metrics"
created: 2026-09-20
updated: 2026-09-20
tags:
  - source-summary
  - agent-security
  - verification
evidence_level: high
claim_type: extracted
---

# Azure SRE Agent: governed mitigations, audit events, and incident metrics

## 编译摘要

### 1. 浓缩

- **核心结论 1：控制面已经具备把 incident、approval 与 tool execution 串起来的关联骨架。**
  - AgentToolExecution / AgentAzCliExecution 记录工具或 CLI 调用，ApprovalDecision 记录审批，IncidentActivitySnapshot 记录 incident 生命周期；TraceId、CorrelationId、ThreadId、CallId 与 IncidentId 提供关联键。
- **核心结论 2：动作链明确区分判断、权限检查、执行与验证。**
  - 官方执行文档把流程写成 diagnose → identify action → check permissions → execute/propose → verify，并通过 managed identity、run mode、management lock 与命令级禁止项限制执行。
- **核心结论 3：运营指标可以区分 agent mitigated / assisted / human mitigated / pending user action，但“mitigated”仍是控制面结果。**
  - 当前公开指标没有同时给出 revoke-after-send、unknown commit、rollback success、provider post-state reconciliation 或 independent review 的分母。

### 2. 质疑

- 这是产品 schema/机制文档，不是某次真实 incident 的完整导出；字段存在不等于每个 incident 都完整填充并跨系统可 join。
- Application Insights 主要记录 Agent 控制面；Azure Activity Log 主要记录 Azure Resource Manager 操作。目标业务系统的外部副作用仍需要自己的 audit/effect ledger。
- “Result success”或“IncidentMitigatedByAgent=True”不能自动证明外部世界已经恢复到正确状态。

### 3. 对标

- 对 EX-005：补上 policy/action receipt 前后的最小关联字段，但没有闭合 revoke → in-flight → effect reconciliation。
- 对 CR-004：这是可观测性 schema 的强一手证据；真正缺口从“有没有 trace ID”收窄为“关联键能否穿透到目标系统 effect receipt 与 canonical post-state”。
- 对 [[Agent-Security]]：生产闭环应保存 IncidentId / TraceId / CorrelationId / CallId、approval、tool start/end、action result 与 post-action verification，并标出未覆盖的外部状态。

## 关联概念

- [[Agent-Security]]
- [[Agent-Observability]]
- [[Operational-Responsibility]]
- [[Alert-Closed-Loop]]
