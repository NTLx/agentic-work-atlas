---
type: entity
title: Deterministic Retrieval
aliases:
  - 确定性检索
  - deterministic retrieval
definition: "在 Agent 工作流中，通过引入专门设计的工具层（而非直接由 LLM 驱动界面），确保数据获取过程 100% 准确、可重复且符合领域规范的技术。"
created: 2026-06-10
updated: 2026-07-29
evidence_level: medium
claim_type: mixed
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
  - "[[20260728-bytebytego-llm-search-integration-depth]]"
---

# Deterministic Retrieval（确定性检索）

> [!definition] 定义
> **Deterministic Retrieval** 是一种上下文工程（Context Engineering）实践。它主张：Agent 应被赋予能够“无聊地可靠”执行检索任务的特定工具，而不是让模型通过复杂的 Web 界面或模糊的自然语言描述去“撞大运”。

## 关键数据点
- 性能飞跃: 引入确定性层后，模型对病毒序列检索的准确率可从 16.9% 提升至 99.7%（GPT-5.5）。
- **生成侧镜像：DoorDash RAG 倒置（07-29）**：DoorDash 搜索把 RAG 用作 guardrail 而非 generator——ANN 检索 top-100 taxonomy 概念，LLM 从列表选取而非生成（"RAG defines the entire output space"），系统只产出设计已知的概念，热门菜品 carousel 触发率约 +30%（[[20260728-bytebytego-llm-search-integration-depth]]）。确定性检索约束"取什么"（输入端），RAG 倒置约束"输出什么"（输出端）——同属"把 LLM 关进无聊可靠的空间"设计家族。

## 前提与局限性
- **前提**: 需要深度理解目标领域的业务规则（如 virology 中的过滤习惯）。
- **局限**: 构建成本高，需要为不同的垂直领域数据库定制专属工具隧道。

## 关联概念
- [[Agent-Harness]]
- [[Context-Engineering]]
- gget-virus
- [[Scientific-Discovery-AI]]
