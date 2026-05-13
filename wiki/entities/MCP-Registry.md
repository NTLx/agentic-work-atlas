---
type: entity
title: MCP Registry (MCP 注册表)
aliases:
  - MCP 注册表
  - MCP Registry
definition: "MCP 生态系统中的中心化组件，作为所有经批准的 MCP 服务器的单一事实来源，负责服务发现、安全验证和治理。"
created: 2026-05-13
updated: 2026-05-13
tags:
  - AI-Agent
  - governance
  - infrastructure
source_raw:
  - "[[Building an MCP Ecosystem at Pinterest]]"
---

# MCP Registry

> **核心洞察**：没有治理的工具集只是乱堆的积木，注册表是 Agent 工具生态的“交通指挥中心”。

## 定义

**MCP 注册表**（MCP Registry）是 [[Pinterest-Engineering]] 为其 MCP 生态系统设计的核心治理组件。它解决了“有哪些工具可用”、“谁有权使用”以及“工具是否安全”这三大核心问题。

## 核心功能

1. **服务发现 (Discovery)**：
   - **面向人类 (Web UI)**：展示服务器所有者、支持渠道、安全姿态、在线状态及可用工具列表。
   - **面向 Agent (API)**：允许 AI 客户端动态查询并校验可连接的服务器。
2. **安全与准入 (Governance)**：
   - 只有出现在注册表中的服务器才被视为“生产环境已批准”。
   - 记录 Security、Legal、Privacy 的审核状态。
3. **权限校验 (AuthZ)**：
   - 在 Agent 调用工具前，先向注册表确认：“当前用户是否被允许使用该服务器 X？”。

## Pinterest 的双层鉴权模型

1. **JWT 令牌 (End-user JWTs)**：在前端（如 Slack 或 Web Chat）捕获用户身份，确保 Agent 操作具有用户归属。
2. **网格身份 (Mesh Identities/SPIFFE)**：对于低风险、无人在场（No human in the loop）的场景，基于服务网格身份进行机器间验证。

---

## 关键数据点

- 注册表是所有非一次性实验的 MCP 服务器必须注册的地方。
- 通过注册表，Pinterest 实现了基于**业务组（Business Group）**的权限隔离，例如只有财务组能访问包含敏感收入指标的 Presto 服务器。

## 前提与局限性

- **前提**：所有 Agent 客户端必须集成了对注册表的 API 调用流程。
- **局限性**：注册表本身成为单点故障风险（SPOF），需要高可用的架构保障。

## 关联概念

- [[Model-Context-Protocol-MCP]] - 协议基础
- [[Harness-Engineering]] - 注册表是驾驭系统的关键治理组件
- [[Context-Engineering]] - 决定 Agent 看到哪些工具
