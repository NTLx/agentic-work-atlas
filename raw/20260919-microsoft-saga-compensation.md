---
type: raw
title: "Saga pattern with Dataverse or Dynamics 365"
source: "https://learn.microsoft.com/en-us/dynamics365/guidance/reference-architectures/saga-pattern-dataverse"
author:
  - "Microsoft"
created: "2026-09-19"
description: "Microsoft 官方 Saga 参考架构：跨独立系统的本地事务、重试、补偿事务和最终一致性；补偿需要显式处理已在前序系统提交的变化。"
tags:
  - clippings
  - agent-security
  - distributed-systems
---

# Saga pattern with Dataverse or Dynamics 365

> Canonical source: https://learn.microsoft.com/en-us/dynamics365/guidance/reference-architectures/saga-pattern-dataverse
> Accessed: 2026-09-19.

## Source locator

- Workflow spans Dataverse and one or more independently managed non-Microsoft systems.
- Each target system needs an explicit retry strategy.
- Fatal errors can start compensating transactions for systems that have already processed earlier steps.
- The reference architecture uses separate queues/functions for compensation paths when required.
- Each stage records monitoring/log information; successful response advances the workflow, fatal error can reverse the compensable path.

## Evidence boundary

This is an official reference architecture, not an Agent-specific security experiment. It establishes distributed-systems semantics: cross-system rollback is explicit compensation, not automatic restoration of a prior local checkpoint. Compensation itself can fail and does not make inherently irreversible effects reversible.
