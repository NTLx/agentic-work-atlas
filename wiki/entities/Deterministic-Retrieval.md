---
type: entity
title: Deterministic Retrieval
aliases:
  - 确定性检索
  - deterministic retrieval
definition: "在 Agent 工作流中，通过引入专门设计的工具层（而非直接由 LLM 驱动界面），确保数据获取过程 100% 准确、可重复且符合领域规范的技术。"
created: 2026-06-10
updated: 2026-06-10
tags:
  - deterministic-retrieval
  - Context-Engineering
  - science
related_entities:
  - "[[Agent-Harness]]"
  - "[[Context-Engineering]]"
  - "[[Scientific-Discovery-AI]]"
source_raw:
  - "[[20260608-paving-the-way-for-agents-in-biology]]"
---

# Deterministic Retrieval（确定性检索）

> [!definition] 定义
> **Deterministic Retrieval** 是一种上下文工程（Context Engineering）实践。它主张：Agent 应被赋予能够“无聊地可靠”执行检索任务的特定工具，而不是让模型通过复杂的 Web 界面或模糊的自然语言描述去“撞大运”。

## 关键数据点
- 性能飞跃: 引入确定性层后，模型对病毒序列检索的准确率可从 16.9% 提升至 99.7%（GPT-5.5）。

## 前提与局限性
- **前提**: 需要深度理解目标领域的业务规则（如 virology 中的过滤习惯）。
- **局限**: 构建成本高，需要为不同的垂直领域数据库定制专属工具隧道。

## 关联概念
- [[Agent-Harness]]
- [[Context-Engineering]]
- gget-virus
- [[Scientific-Discovery-AI]]
