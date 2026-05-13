---
type: entity
title: Model Context Protocol (MCP)
aliases:
  - MCP
  - Model Context Protocol
definition: "一种开放标准，允许 AI 模型通过统一的客户端-服务器协议与各种工具和数据源进行通信，替代了传统的一对一硬编码集成。"
created: 2026-05-13
updated: 2026-05-13
tags:
  - AI-Agent
  - standard
  - tool-use
source_raw:
  - "[[Building an MCP Ecosystem at Pinterest]]"
---

# Model Context Protocol (MCP)

> **核心洞察**：MCP 是 AI 时代的“USB 接口”，它标准化了工具与模型之间的连接方式。

## 定义

**Model Context Protocol (MCP)** 是由 Anthropic 提出的开放标准，旨在解决 LLM 在调用外部工具（Tool Use）时面临的碎片化问题。它将“模型（Client）”与“工具/数据（Server）”解耦，使得一个 MCP Server 可以服务于多个不同的模型或应用（如 Claude Desktop, Cursor, IDE 插件等）。

## Pinterest 的实践模式

[[Pinterest-Engineering]] 在其生产环境中应用了 MCP，并总结了以下关键架构选择：

1. **云端托管 (Cloud-hosted)**：不同于本地 stdio 模式，Pinterest 优化了运行在内部云端的 MCP 服务器，以便实施集中的安全审计、身份校验和负载均衡。
2. **领域特定服务器 (Domain-specific Servers)**：不使用单一的巨型服务器，而是为 Presto、Spark、Airflow 等不同领域建立独立的小型服务器。
   - **好处**：粒度更细的权限控制，减少模型上下文窗口的“工具干扰”。

## 核心组件

- **MCP Client**：集成 LLM 的应用（如 Pinterest 内部的 AI 聊天平台）。
- **MCP Server**：暴露具体工具能力的后端服务（如 Presto 查询、日志读取）。
- **MCP Registry**：中心化的注册表，负责发现和治理。

---

## 关键数据点

- Pinterest 在 2025 年 1 月时已达到每月 **66,000 次** MCP 调用。
- 覆盖了 844 名月活用户。
- 估算每月为工程师节省约 **7,000 小时** 的工作时间。

## 前提与局限性

- **前提**：需要工具提供方（Server）和消费方（Client）都遵循同一套协议规范。
- **局限性**：虽然标准化了连接，但“如何教导 Agent 正确使用工具”这一 Prompt 难题依然存在。
- **安全风险**：统一的接口意味着如果鉴权失效，Agent 可能会获得极大的系统操作权限，因此必须配合严格的 [[Harness-Engineering|驾驭工程]]。

## 关联概念

- [[MCP-Registry]] - 治理核心
- [[Harness-Engineering]] - Pinterest 将 MCP 视为其 Agent 基础设施（Harness）的底座
- [[Context-Engineering]] - 通过分领域服务器管理 Agent 的上下文空间
- [[Agent-Native]] - MCP 是 Agent 原生基础设施的典型代表
