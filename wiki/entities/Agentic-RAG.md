---
type: entity
title: Agentic RAG
aliases:
  - Agentic RAG
  - Agentic Retrieval
  - Query Routing RAG
  - Agent-driven retrieval
definition: "用 LLM classifier 按 query 类型路由到不同 retrieval strategy（vector / graph / SQL / web）的 retrieval architecture——避免单策略 trade-off；LlamaIndex two-layer (composite retriever + auto-routed mode) 是典型实现；代价是 latency + cost + routing error 风险"
created: 2026-08-20
updated: 2026-08-20
tags:
  - retrieval
  - agentic-engineering
  - routing
  - rag
evidence_level: medium
claim_type: mixed
related_entities:
  - "[[GraphRAG]]"
  - "[[Knowledge-Graph]]"
  - "[[Skills-as-Products]]"
  - "[[Rubric-Based-Evaluation]]"
  - "[[Decision-Centric-Architecture]]"
source_raw:
  - "[[20260820-bytebytego-graphrag.md]]"
---

# Agentic RAG（Agent 驱动检索）

> [!definition] 定义
> **Agentic RAG** 是用 LLM classifier 按 query 类型路由到不同 retrieval strategy（vector search / graph search / SQL / web）的 retrieval architecture——**避免单策略 trade-off**；典型实现是 LlamaIndex two-layer (composite retriever 选 index + auto-routed mode 选 method)。代价：增加 latency + per-query cost + routing error 风险（"完美 retrieval 跑在错策略上"）。

## 核心动机

```
不同 query 类型需要不同 retrieval 策略：
- local queries → vector search
- global queries → GraphRAG / community reports
- structured data → SQL query
- current events → web search

单策略架构无法同时服务多种 query 类型
```

## 架构

### LlamaIndex Two-Layer Routing

| Layer | 决策 |
|-------|------|
| **Composite Retriever** | 选 index（依据每个 index 的 description） |
| **Auto-Routed Mode** | 在 selected index 内选 retrieval method（依据 specific query） |

两层都有 routing 决策——meta 选择 + instance 选择

### 完整流程

```
User Query
  ↓
[LLM Classifier]
  ├─ Query Type: "local"
  │   ↓
  │   [Vector Search over prebuilt index]
  │   ↓
  │   Top-k chunks → LLM synthesis
  │
  ├─ Query Type: "global"
  │   ↓
  │   [GraphRAG Global Search]
  │   ↓
  │   Map-reduce over community reports → final answer
  │
  └─ Query Type: "current event"
      ↓
      [Web Search]
      ↓
      Recent results → LLM synthesis
```

## 经济与质量权衡

| 维度 | 影响 |
|------|------|
| **Latency** | +（每个 query 增加一次 LM classification call） |
| **Per-query cost** | +（classification LLM call） |
| **Quality (correct routing)** | ↑↑（策略匹配 query 类型） |
| **Quality (incorrect routing)** | ↓↓（完美 retrieval 跑在错策略上 = 失败） |
| **Debugging complexity** | ↑↑（需要 trace 路由决策） |

## 与 GraphRAG 的关系

GraphRAG 提供策略池（local/global/DRIFT），Agentic RAG 提供路由层——两者互补：

```
Agentic RAG routes to:
  - Vector Search (for local queries)
  - GraphRAG Local Search (for entity-named queries)
  - GraphRAG Global Search (for corpus-wide queries)
  - GraphRAG DRIFT Search (for hybrid)
  - SQL (for structured data)
  - Web (for current events)
```

## 前提与局限性

- **Routing error 风险**: poor answer 可能来自"完美 retrieval 跑在错策略"——不易 debug
- **延迟增加**: classification LLM call 是必要 overhead
- **路由逻辑本身需要 LM quality**: 弱 classifier 把所有 query 都路由到 vector → 退化为 plain RAG
- **prompt injection risk**: 攻击者构造 query 让 classifier 路由到不合适的 strategy

## 与相关 concept 的关系

- **[[GraphRAG]]**: Agentic RAG 路由的策略池之一
- **[[Skills-as-Products]]**: skill scope 治理与 routing 决策同构——"input 决定调用哪个 capability"
- **[[Rubric-Based-Evaluation]]**: routing decision 可被 rubric-based eval 验证质量
- **[[Decision-Centric-Architecture]]**: ontology 决定的 routing 与 agentic RAG routing 同构

## 关键数据点

- 提出者/框架: LlamaIndex
- 文章: ByteByteGo 2026-08-19
- 与 GraphRAG 配合：Agentic RAG 决定何时用 vector / graph / SQL / web
- LlamaIndex two-layer: composite retriever + auto-routed mode

## 适用决策

| 场景 | 推荐 |
|------|------|
| 单一 query 类型 | 单策略（vector 或 graph 或 SQL）——避免 Agentic RAG overhead |
| 多种 query 类型共存 | Agentic RAG |
| Budget 紧张 | 单策略 |
| Latency 敏感 | 单策略（避免 classification overhead） |
| Routing quality 可量化 | Agentic RAG（可评估） |

## 关联概念

- [[GraphRAG]] — Agentic RAG 路由的策略池
- [[Knowledge-Graph]] — graph search 基础
- [[Skills-as-Products]] — scope 治理同构
- [[Rubric-Based-Evaluation]] — 路由质量评估
- [[Decision-Centric-Architecture]] — ontology routing 同构
- [[RAG-vs-LLM-Wiki]] — retrieval architecture 对比
- [[Corrective-RAG]] — post-retrieval 修正