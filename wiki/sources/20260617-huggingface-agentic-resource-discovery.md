---
type: source-summary
title: "Agentic Resource Discovery: Let agents search for tools, skills, and other agents"
source_raw:
  - "[[20260617-huggingface-agentic-resource-discovery]]"
created: 2026-06-17
updated: 2026-06-17
tags:
  - source-summary
  - agentic-engineering
  - MCP
  - A2A
  - agent-discovery
  - open-specification
evidence_level: medium
claim_type: mixed
---

# Agentic Resource Discovery: Let agents search for tools, skills, and other agents

## 编译摘要

### 1. 浓缩
- **核心结论1**: ARD（Agentic Resource Discovery）是 MCP/Skills/A2A 之上的发现层，将 agent 能力发现从"安装后使用"转为"意图搜索"
  - 关键证据: 开放规范由 Microsoft、Google、GoDaddy、Hugging Face 等贡献；定义 `ai-catalog.json` 静态清单 + `POST /search` 动态注册 API
- **核心结论2**: HuggingFace Discover 是 ARD 参考实现，将 Hub 上的 Spaces 语义搜索结果转换为 ARD 目录条目（skills / MCP servers / raw metadata）
  - 关键证据: 支持三种媒体类型（`application/ai-skill`、`application/mcp-server+json`、`application/vnd.huggingface.space+json`）；自动过滤运行中 Spaces
- **核心结论3**: ARD 将选择移出 LLM 上下文窗口——注册表以发布者身份、代表性查询、合规证明等富信号索引能力，客户端自然语言搜索后模型调用返回结果
  - 关键证据: 当前 fallback 是将所有工具描述 dump 到上下文窗口；ARD 通过 REST 端点提供有排名的发现结果

### 2. 质疑
- **关于"发现层"的实际采用**: ARD 是 draft 规范，实际采纳程度未知；MCP 本身仍在早期，发现层是否过早抽象化尚不确定
- **关于"联邦搜索"的质量**: 跨注册表联邦搜索时，不同注册表的信号质量和排名标准不一致，可能导致搜索结果质量参差不齐
- **关于与现有生态的竞争**: HuggingFace Discover 直接与 OpenRouter、Smithery 等工具发现平台竞争；ARD 作为开放规范是否能统一生态取决于大厂支持持续性

### 3. 对标
- **MCP-Registry**: ARD 是 [[MCP-Registry]] 概念的扩展——从 MCP 工具注册扩展到跨协议（MCP/Skills/A2A）发现
- **Tool-Use-Architecture**: ARD 将工具发现从 harness 内部移到外部注册表，改变了 [[Tool-Use-Architecture]] 中工具选择的架构位置
- **Agent-Infra**: ARD 作为发现层是 [[Agent-Infra]] 基础设施的重要组件——agent 不仅需要执行工具，还需要发现工具
- **Open-Source-Operational-AI-Framework**: ARD 的开放规范策略与 [[Open-Source-Operational-AI-Framework]] 中开源运营框架的思路一致

### 关联概念
- [[MCP-Registry]]
- [[Tool-Use-Architecture]]
- [[Agent-Infra]]
- [[Open-Source-Operational-AI-Framework]]
