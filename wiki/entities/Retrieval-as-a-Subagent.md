---
type: entity
title: Retrieval-as-a-Subagent
aliases:
  - retrieval as a subagent
  - agentic retrieval
  - 检索子代理
definition: "将检索操作包装在 agentic 循环中的架构模式——检索不再是 one-shot 函数调用，而是一个小型 Agent：规划查询源、执行查询、评估结果、在失败时重试或切换源，穷尽后返回结构化失败信号而非强制幻觉。"
created: 2026-07-14
updated: 2026-07-14
evidence_level: high
claim_type: extracted
tags:
  - architecture
  - context-engineering
  - RAG
related_entities:
  - "[[Agent-Harness]]"
  - "[[Context-Engineering]]"
  - "[[Agent-Loops]]"
  - "[[Deterministic-Retrieval]]"
  - "[[Context-Rot]]"
source_raw:
  - "[[20260713-microsoft-ships-ai-agents-enterprise-scale]]"
---

# Retrieval-as-a-Subagent

> [!definition] 定义
> **Retrieval-as-a-Subagent** 是将检索操作包装在 agentic 循环中的架构模式——检索不再是 one-shot 函数调用（经典 RAG），而是一个小型 Agent：规划查询源、执行查询、评估结果、在失败时重试或切换源，穷尽后返回结构化失败信号而非强制幻觉。

## 经典 RAG 的局限

经典 RAG 是 one-shot 模式：用户提问 → embed → 搜索单一索引 → 返回 top-k → 传给模型。在以下场景中失败：
- 问题模糊
- 语料异构（跨多种数据源）
- 正确答案需要组合多个来源
- 首次检索返回空结果

Agent 无法从坏检索中恢复——"when RAG isn't working well, the whole agent isn't working well"（Marco Casalaina, Microsoft）。

## 生产级检索循环

```
规划查询 → 尝试源A → 评估结果 → 
  不充分 → 精化查询 → 尝试源B → 评估 → 
  不充分 → ... → 穷尽迭代 → 返回结构化 "I don't know"
```

Microsoft Foundry IQ 是此模式的最清晰生产实现：四个 IQ 服务（Foundry IQ / Fabric IQ / Web IQ / Work IQ）分别处理非结构化数据、结构化数据、实时网络和 Microsoft 365 生产力面，均通过 MCP 被 Agent 调用。

## 从数据到工具的推广

同一循环不仅适用于数据检索，也适用于工具选择：
- 少量工具：全量列表注入 prompt
- 大量工具：Agent 搜索所需工具 → 获取 → 调用（tool search）

OpenAI 和 Anthropic 的 Agent 已收敛到相同的 tool search 模式。**同一检索循环既拉取知识也拉取能力。**

## 与 Deterministic Retrieval 的关系

[[Deterministic-Retrieval]] 解决的是特定领域的检索可靠性问题（如 gget-virus 将生物数据检索准确率从 16.9% 提升至 99.7%）。Retrieval-as-a-Subagent 解决的是通用场景下的检索恢复能力——两者互补：确定性检索可以作为 agentic 循环中的单个检索源。

## 前提与局限性

- 迭代检索增加延迟和 token 消耗，对实时场景可能不可接受
- "何时穷尽迭代"的阈值设计是开放问题（静态 vs 自适应）
- 结构化 "I don't know" 需要调用方 Agent 能正确处理此信号

## 关联概念

- [[Agent-Harness]] — Retrieval-as-a-Subagent 是 harness 上下文层的核心架构模式
- [[Context-Engineering]] — 迭代检索是上下文管理的生产级实现
- [[Agent-Loops]] — 检索循环是 Agent 循环在数据获取层的特化
- [[Deterministic-Retrieval]] — 确定性检索可作为 agentic 循环的可靠检索源
- [[RAG-vs-LLM-Wiki]] — Retrieval-as-a-Subagent 是 RAG 的生产级进化

## 关键数据点

- Microsoft Foundry IQ (2026-07): 四个 IQ 服务（Foundry/Fabric/Web/Work）均通过 MCP 被 Agent 调用，是此模式的最清晰生产实现
- 迭代检索比 one-shot RAG 显著提高检索成功率，但增加延迟和 token 消耗
