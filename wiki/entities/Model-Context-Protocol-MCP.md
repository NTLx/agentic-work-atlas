---
type: entity
title: Model Context Protocol (MCP)
aliases:
  - MCP
  - Model Context Protocol
definition: "让 AI client 通过统一客户端-服务器协议连接工具和数据源的开放标准，用来替代模型与工具之间的一对一硬编码集成"
created: 2026-05-13
updated: 2026-05-25
tags:
  - AI-Agent
  - tool-use
evidence_level: medium
claim_type: mixed
related_entities:
  - "[[MCP-Registry]]"
  - "[[Pinterest-Engineering]]"
  - "[[Harness-Engineering]]"
  - "[[Context-Engineering]]"
  - "[[Tool-Use-Architecture]]"
source_raw:
  - "[[Building an MCP Ecosystem at Pinterest]]"
---

# Model Context Protocol (MCP)

> **核心洞察**：MCP 是 AI 时代的“USB 接口”，它标准化了工具与模型之间的连接方式。

> [!definition] 定义
> Model Context Protocol (MCP) 是让 AI client 通过统一客户端-服务器协议连接工具和数据源的开放标准，用来替代模型与工具之间的一对一硬编码集成。

## 为什么重要

MCP 的核心价值不是“多一个 API 标准”，而是把 agent tool use 从临时集成变成可治理基础设施。没有标准协议，每个模型、IDE、chat surface 和内部系统都要写一套连接逻辑；有了 MCP，工具提供方可以通过 server 暴露能力，消费方可以通过 client 发现、连接和调用。

但 Pinterest 案例也说明，协议只解决连接问题，不自动解决生产问题。真正进入企业后，MCP 必须和 [[MCP-Registry]]、身份系统、安全 review、human-in-the-loop、observability 和领域特定 server 设计一起出现。

## Pinterest 的实践模式

[[Pinterest-Engineering]] 在其生产环境中应用了 MCP，并总结了以下关键架构选择：

1. **云端托管 (Cloud-hosted)**：不同于本地 stdio 模式，Pinterest 把生产路径优化为内部云托管 MCP servers，以便实施集中路由、安全审计、身份校验、部署和负载管理。
2. **领域特定服务器 (Domain-specific Servers)**：不使用单一巨型服务器，而是为 Presto、Spark、Airflow、Knowledge 等领域建立独立小型 server。
3. **中心注册表 (Registry)**：把 server approval、tool discovery、安全姿态、live status 和用户授权放到同一个治理层。
4. **接入日常 surface**：MCP 不只在实验环境中运行，而是进入内部 Web Chat、IDE integration 和内部聊天机器人，让 agent 在员工实际工作场景中调用工具。

这些选择说明：企业 MCP 的重点不是连接数量，而是最小权限、上下文清洁度和工具 owner 责任。

## 核心组件

- **MCP Client**：集成 LLM 的应用（如 Pinterest 内部的 AI 聊天平台）。
- **MCP Server**：暴露具体工具能力的后端服务（如 Presto 查询、日志读取）。
- **MCP Registry**：中心化的注册表，负责发现和治理。
- **AuthN / AuthZ 层**：通过 end-user JWT、mesh identity、Envoy 和 policy decorator 把真实用户或服务身份传递到工具调用。
- **Human-in-the-loop 层**：对敏感或高成本动作要求人类确认，避免 agent 自动扩大操作半径。

---

## 关键数据点

- Pinterest 在 2025 年 1 月时已达到每月 **66,000 次** MCP 调用。
- 覆盖了 844 名月活用户。
- 估算每月为工程师节省约 **7,000 小时** 的工作时间。
- Pinterest 以多个领域特定 MCP server 替代单一巨型 server，以降低权限耦合和上下文噪声。
- 非实验 server 需要 owning team、registry entry 和 Security、Legal/Privacy、GenAI review。

## 前提与局限性

- **前提**：需要工具提供方（Server）和消费方（Client）都遵循同一套协议规范。
- **局限性**：虽然标准化了连接，但“如何教导 Agent 正确使用工具”这一 Prompt 难题依然存在。
- **安全风险**：统一的接口意味着如果鉴权失效，Agent 可能会获得极大的系统操作权限，因此必须配合严格的 [[Harness-Engineering|驾驭工程]]。
- **上下文风险**：工具太多会污染模型上下文。MCP server 设计必须考虑工具描述长度、领域边界和按需加载策略。
- **治理风险**：协议本身不定义企业内谁能批准 server、谁承担 owner、如何审计调用、如何废弃低质量工具；这些必须由组织 harness 补齐。

## 关联概念

- [[MCP-Registry]] - 治理核心
- [[Pinterest-Engineering]] - MCP 进入企业生产环境的案例
- [[Harness-Engineering]] - Pinterest 将 MCP 视为其 Agent 基础设施（Harness）的底座
- [[Context-Engineering]] - 通过分领域服务器管理 Agent 的上下文空间
- [[Agent-Native]] - MCP 是 Agent 原生基础设施的典型代表
