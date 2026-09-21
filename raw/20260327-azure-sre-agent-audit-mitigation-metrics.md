---
type: raw
title: "Azure SRE Agent: governed mitigations, audit events, and incident metrics"
source: "https://learn.microsoft.com/en-us/azure/sre-agent/audit-agent-actions"
author:
  - "Microsoft"
created: "2026-09-20"
description: "Microsoft Azure SRE Agent 官方材料族：动作执行、审批、工具调用与 incident lifecycle 可通过 Application Insights 事件和关联键审计，但公开文档仍未给出同案外部副作用、撤销后在途结局与权威 post-state 的完整导出。"
tags:
  - clippings
  - agent-security
  - verification
---

# Azure SRE Agent: governed mitigations, audit events, and incident metrics

> Canonical source: https://learn.microsoft.com/en-us/azure/sre-agent/audit-agent-actions
> Related primary sources:
> - https://learn.microsoft.com/en-us/azure/sre-agent/execute-mitigations
> - https://learn.microsoft.com/en-us/azure/sre-agent/incident-platforms
> Accessed: 2026-09-20.

## Source locator

- Audit page: every agent action is logged to Application Insights customEvents; event types include AgentToolExecution, AgentAzCliExecution, IncidentActivitySnapshot and ApprovalDecision.
- Shared correlation fields include TraceId, SpanId, ParentSpanId, ThreadId, LogTimestamp and CorrelationId; tool execution adds CallId.
- IncidentActivitySnapshot includes IncidentId, IncidentCreatedOn, IncidentHandledOn, IncidentMitigatedOn, AgentAutonomyLevel and response-plan fields.
- Execute-mitigations page describes diagnose → identify action → check permissions → execute/propose → verify, with Review / Autonomous modes, managed-identity scope and command-level guardrails.
- Incident metrics distinguish incidents reviewed, mitigated by agent, assisted by agent, mitigated by user and pending user action.

## Evidence boundary

These pages document a production product's telemetry schema and control model, not a public incident-level export. The existence of IncidentId / TraceId / CorrelationId / CallId proves joinable control-plane fields exist, but does not prove that a real incident record joins through downstream effect receipts, revoke-after-send outcomes, provider-authoritative post-state, rollback success or independent review completion. "Mitigated" is a product outcome category, not by itself a proof of external-state reconciliation.
