---
type: entity
title: Agentic RAG
aliases:
  - Agentic RAG
  - Agentic Retrieval
  - Query Routing RAG
  - Agent-driven retrieval
definition: "由 Agent 或编排器根据查询、已获取证据及任务状态选择、组合或迭代检索策略的架构；单次 LLM 路由是其中一种实现，不是定义所要求的唯一机制。"
created: 2026-08-20
updated: 2026-11-28
tags:
  - retrieval
  - agentic-engineering
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
  - "[[20260902-bytebytego-rag-translator-model]]"
---

# Agentic RAG（Agent 驱动检索）

> [!definition] 定义
> **Agentic RAG** 在此指检索策略可根据任务与证据动态调整的系统；包括单次路由、问题分解、多路并行、证据不足时重试或改路。ByteByteGo 举例为 LLM classifier 与两层路由，其产品实现描述未核当前 LlamaIndex 版本。策略选择引入新的延迟、成本、权限与错误面。

## 核心动机

```
不同 query 类型需要不同 retrieval 策略：
- local queries → vector search
- global queries → GraphRAG / community reports
- structured data → SQL query
- current events → web search

同一策略可能服务多种问题，但不同任务的质量与成本曲线不同；是否需要路由由实际评测决定
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
| **Latency** | 可能增加（额外决策、重试），也可能因避免昂贵检索下降；可用规则路由 |
| **Per-query cost** | 比较端到端路径成本，不预设增加或降低 |
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
- **延迟与成本**: LLM 分类不是必要条件；比较规则、确定性 metadata 策略、LLM 路由与混合路由
- **路由逻辑本身需要 LM quality**: 弱 classifier 把所有 query 都路由到 vector → 退化为 plain RAG
- **prompt injection risk**: 攻击者构造 query 让 classifier 路由到不合适的 strategy

## 与相关 concept 的关系

- **[[GraphRAG]]**: Agentic RAG 路由的策略池之一
- **[[Skills-as-Products]]**: skill scope 治理与 routing 决策同构——"input 决定调用哪个 capability"
- **[[Rubric-Based-Evaluation]]**: routing decision 可被 rubric-based eval 验证质量
- **[[Decision-Centric-Architecture]]**: ontology 决定的 routing 与 agentic RAG routing 同构

## 关键数据点

- 既有来源以 LlamaIndex 为实现例，不构成首创归因
- 文章: ByteByteGo 2026-08-19
- 与 GraphRAG 配合：Agentic RAG 决定何时用 vector / graph / SQL / web
- LlamaIndex two-layer: composite retriever + auto-routed mode

## 适用决策

| 场景 | 推荐 |
|------|------|
| 单一 query 类型 | 单策略（vector 或 graph 或 SQL）——避免 Agentic RAG overhead |
| 多种 query 类型共存 | 比较固定、规则路由与 Agentic RAG 的实测收益 |
| Budget 紧张 | 单策略 |
| Latency 敏感 | 单策略（避免 classification overhead） |
| Routing quality 可量化 | 用同一问题集比较证据召回、引用正确性、失败恢复、延迟/成本；不能只测路由标签 |

## 关联概念

- [[GraphRAG]] — Agentic RAG 路由的策略池
- [[Knowledge-Graph]] — graph search 基础
- [[Skills-as-Products]] — scope 治理同构
- [[Rubric-Based-Evaluation]] — 路由质量评估
- [[Decision-Centric-Architecture]] — ontology routing 同构
- [[RAG-vs-LLM-Wiki]] — retrieval architecture 对比
- [[Corrective-RAG]] — post-retrieval 修正