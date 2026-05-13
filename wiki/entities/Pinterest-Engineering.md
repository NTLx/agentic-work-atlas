---
type: entity
title: Pinterest Engineering
aliases:
  - Pinterest Engineering
definition: "Pinterest 的工程团队，致力于通过标准协议（如 MCP）和自研工具构建 AI Agent 驱动的自动化工程生态。"
validated_source: "https://medium.com/pinterest-engineering"
validated_at: "2026-05-13"
created: 2026-05-13
updated: 2026-05-13
tags:
  - organization
  - software-engineering
  - AI-Agent
source_raw:
  - "[[Building an MCP Ecosystem at Pinterest]]"
---

# Pinterest Engineering

> **核心贡献**：率先在生产环境大规模部署 MCP 生态系统，并建立了中心化注册表治理模式。

## 简介

Pinterest 的工程团队在 AI Agent 的工程化落地方面走在前列。他们不仅仅是将 AI 作为聊天辅助，而是通过标准化的协议（[[Model-Context-Protocol-MCP]]）让 Agent 具备了操作内部 Presto、Spark 和 Airflow 等生产系统的能力。

## 核心实践

1. **统一注册表治理**：通过 [[MCP-Registry]] 解决了工具发现和安全授权的难题。
2. **量化价值**：以“时间节省（Time Saved）”作为北斗星指标，通过每项工具的估算收益 × 触发次数来量化 AI 的生产力贡献。
3. **安全第一**：与安全团队深度合作，定义了专门的“MCP Security Standard”，并实施了基于业务组的访问门控。

---

## 关联概念

- [[Model-Context-Protocol-MCP]] - 他们采用的连接标准
- [[MCP-Registry]] - 他们的治理模式
- [[Harness-Engineering]] - 他们的工程实践是驾驭工程的典型案例
- [[Agent-Native]] - 致力于构建 Agent 原生的工程环境
