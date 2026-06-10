---
type: entity
title: HaaS (Harness-as-a-Service)
aliases:
  - Harness-as-a-Service
  - Harness 即服务
definition: "从提供底层模型 API转向提供成熟、预配置的 Agent 运行时（Runtime）环境，包括循环编排、工具分发和上下文管理能力。"
created: 2026-06-10
updated: 2026-06-10
tags:
  - cloud-service
  - infrastructure
related_entities:
  - "[[Agent-Harness]]"
  - "[[Harness-Engineering]]"
source_raw:
  - "[[20260419-agent-harness-engineering]]"
---

# HaaS (Harness-as-a-Service)

> [!definition] 定义
> **HaaS (Harness-as-a-Service)** 代表了 AI 基础设施演进的下一个阶段：开发者不再只是调用 `model.generate()` 接口，而是接入一个完整的智能体运行时。

## 关键数据点
- 代表产品: Claude Agent SDK, OpenAI Agents SDK, Codex SDK。

## 前提与局限性
- **前提**: 模型能力需达到一定阈值（如具备稳定的工具调用能力）。
- **局限**: 高度依赖厂商的 SDK，可能导致比单一模型更深的生态锁定。

## 关联概念
- [[Agent-Harness]]
- [[Harness-Engineering]]
- [[Agent-Infra]]
