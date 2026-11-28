---
type: entity
title: HaaS (Harness-as-a-Service)
aliases:
  - Harness-as-a-Service
  - Harness 即服务
definition: "由服务提供方托管 Agent Harness/Runtime 的交付方式，责任范围由实际产品契约确定；不同于仅提供本地 SDK 或模型 API"
created: 2026-06-10
updated: 2026-11-28
evidence_level: medium
claim_type: mixed
tags:
  - infrastructure
related_entities:
  - "[[Agent-Harness]]"
  - "[[Harness-Engineering]]"
source_raw:
  - "[[20260419-agent-harness-engineering]]"
---

# HaaS (Harness-as-a-Service)

> [!definition] 定义
> **HaaS (Harness-as-a-Service)** 是本库用于讨论托管 Agent 运行时交付形态的术语，不是所有 AI 基础设施必然演进的下一个阶段。模型 API、本地 SDK、用户自部署 runtime 和厂商托管 runtime 可以并存。

## 关键数据点
- **边界核验（2026-11-28）**：[Claude 官方迁移文档](https://platform.claude.com/docs/en/managed-agents/migration) 明确 SDK 在用户运营的进程中执行，Managed Agents 在 Anthropic 基础设施中运行；[OpenAI Agents SDK 指南](https://developers.openai.com/api/docs/guides/agents/sdk) 同样区分应用内 SDK 与服务托管的 Agents API。SDK 可以封装 harness 机制，但不能据 SDK 名称判定已托管或转移运维责任。按实际状态持久化、执行位置、凭证、计费、升级、迁移和恢复契约判断。

## 前提与局限性
- **前提**：任务需要的能力、数据、权限、运行位置和恢复边界与服务契约匹配；无统一能力阈值。
- **局限**: 高度依赖厂商的 SDK，可能导致比单一模型更深的生态锁定。

## 关联概念
- [[Agent-Harness]]
- [[Harness-Engineering]]
- [[Agent-Infra]]
