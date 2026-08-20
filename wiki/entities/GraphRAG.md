---
type: entity
title: GraphRAG
aliases:
  - GraphRAG
  - Graph RAG
  - Graph-based RAG
  - Knowledge Graph RAG
definition: "微软研究院提出的 retrieval architecture——把 corpus 转换为 knowledge graph（entity + typed relationship）+ hierarchical Leiden community + 预生成 community reports；query 时通过 local/global/DRIFT 三种 mode 跨越 single-document similarity 检索的局限；解决 global query（跨语料推理）的 vector RAG 根本盲区"
created: 2026-08-20
updated: 2026-08-20
tags:
  - retrieval
  - knowledge-graph
  - rag
  - agentic-engineering
evidence_level: medium
claim_type: mixed
related_entities:
  - "[[Agentic-RAG]]"
  - "[[Knowledge-Graph]]"
  - "[[RAG-vs-LLM-Wiki]]"
  - "[[Corrective-RAG]]"
  - "[[Structured-Agent-Memory]]"
  - "[[Decision-Centric-Architecture]]"
  - "[[Knowledge-Compilation]]"
  - "[[Skills-as-Products]]"
source_raw:
  - "[[20260820-bytebytego-graphrag.md]]"
---

# GraphRAG（图增强检索）

> [!definition] 定义
> **GraphRAG** 是微软研究院提出的 retrieval architecture——把 corpus 转换为 **knowledge graph**（entity + typed relationship with descriptions）+ **hierarchical Leiden community** + **预生成 community reports**；query 时通过 **local/global/DRIFT** 三种 mode 跨越 single-document similarity 检索的局限。核心解决 **global query**（跨语料推理）的 vector RAG 根本盲区。

## 核心问题：Vector RAG 的 blind spot

```
Query: "Which service owns the payments retry logic?"
→ Local query: answer lives in 1-2 documents → vector retrieval works ✓

Query: "Which failure causes recur most often across all postmortems?"
→ Global query: answer exists as distribution across 200 documents
→ Vector retrieval returns "recurring" / "frequent" vocabulary matches
→ Real pattern NOT retrieved ✗
```

Microsoft 测试：Vector RAG with 8K vs 64K token context——**larger window 不解决 gap**（comprehensiveness, diversity, source material 仍差）

## Microsoft 6 阶段 Indexing Pipeline

| Phase | 输出 |
|-------|------|
| 1. **Text unit chunking** | 数百到数千 token 的 chunks |
| 2. **Entity/Relationship Extraction** | LM 抽 entity（title, type, description）+ relationship（source, target, description） |
| 3. **Merge with Description Compression** | 同 title/type 的 entity 合并；二次 LM pass 压缩 description |
| 4. **Optional Claim Extraction** | 时间约束的事实声明 |
| 5. **Hierarchical Leiden Clustering** | 递归分区成 communities，多层级（level 0 粗，level N 细） |
| 6. **Community Report Generation** | 每个 community 每个 level 都有 summary；text units + entity descriptions + report contents 嵌入 vector store |

**Cost note**: Phase 2 占 indexing 总成本约 **75%**——是 cost reduction 首选

## 三种 Query Modes

| Mode | 适用 | 机制 |
|------|------|------|
| **Local Search** | local queries（who/what/when/where） | match entities → 5 个并行 expansion（text units / community reports / neighbors / relationships / claims）→ rank → 装入 context window |
| **Global Search** | global queries（summary/aggregation） | 不碰 entity graph；shuffled community report batches → map stage（LM + importance rating）→ reduce stage（top-rated points → final answer） |
| **DRIFT Search** | hybrid | 先 query community reports 得 initial answer + follow-up questions → 对 follow-ups 跑 local search → 返回按 relevance 排序的 questions/answers hierarchy |

## 衍生优化

- **LazyGraphRAG**: 用 NLP 替代 LM extraction + 推迟所有 LM 工作到 query time——indexing cost 降至 full GraphRAG 的 **0.1%**，query cost 降 **700×**，global-query quality comparable
- **FastGraphRAG**: 完全用 NLP（noun phrases = entities, co-occurrence = relationships）——更便宜但"considerably more noise"
- **Microsoft 立场**: 不推荐 every deployment LazyGraphRAG——community reports 有独立价值（人阅读和分享），是副产物

## 实证案例

| Case | Metric | Result |
|------|--------|--------|
| **LinkedIn Customer Service** (SIGIR 2024) | MRR | **+77.6%** |
| **LinkedIn Customer Service** | median per-issue resolution time | **-28.6%** |

## 与传统 RAG 的对比

| 维度 | Vector RAG | GraphRAG |
|------|-----------|----------|
| Local queries | **强**（similarity assumption 成立） | 弱（over-engineered） |
| Global queries | 弱（vocabulary 共现 ≠ underlying pattern） | **强**（community reports 预生成） |
| Faithfulness | comparable | comparable |
| Comprehensiveness | comparable | **优** |
| Diversity | comparable | **优** |
| Supporting source material | comparable | **优** |
| Indexing cost | 低（embedding pass） | **1000×（full GraphRAG）** |
| Index maintenance | low（re-embed chunks） | 高（re-extract + re-cluster） |

## 前提与局限性

- **不减少 hallucination**: faithfulness 与 baseline RAG 相当
- **indexing 成本高**: 75% extraction 是首要优化目标
- **index perishable**: corpus 变化需 re-extract + re-cluster + re-report——日常运营负担
- **prompts domain-specific**: 跨 domain robustness 较弱
- **community report level 选择影响质量**: lower level 更详尽但 token 多
- **DRIFT search 缺乏独立 benchmark**

## 与相关 concept 的关系

- **[[Knowledge-Graph]]**: GraphRAG 底层基础设施
- **[[RAG-vs-LLM-Wiki]]**: GraphRAG vs Wiki 是 retrieval architecture 层面的对比
- **[[Corrective-RAG]]**: 都处理 retrieval quality 问题，但 CRAG 是 post-retrieval 修正
- **[[Agentic-RAG]]**: GraphRAG 的三种 mode 是 agentic RAG 的策略池
- **[[Structured-Agent-Memory]]**: 多属性结构化记忆与 GraphRAG 的 entity/relationship 都暴露 similarity gap
- **[[Decision-Centric-Architecture]]**: ontology pipeline 与 GraphRAG indexing pipeline 同构
- **[[Knowledge-Compilation]]**: 都是把分散源材料压缩成可重用语义层

## 关键数据点

- 提出者: Microsoft Research
- 文章作者: ByteByteGo (Alex Xu 等) 2026-08-19
- LinkedIn SIGIR 2024 实证: MRR +77.6% / resolution time -28.6%
- Microsoft Graph extraction cost 占总 indexing 75%
- LazyGraphRAG indexing cost = full GraphRAG 0.1%
- LazyGraphRAG query cost 降 700×
- Vector RAG with 64K context 仍输给 GraphRAG on global queries
- Community detection: hierarchical Leiden algorithm

## 适用决策

- **Vector RAG 优先**: local queries 主导、corpus 小、indexing 预算低
- **GraphRAG 优先**: global queries 重要、corpus 大且变化慢、indexing 预算足
- **LazyGraphRAG 优先**: global queries 重要但 corpus 变化快、indexing 预算低
- **Agentic RAG 优先**: 多种 query 类型共存、需要 router 动态选择

## 关联概念

- [[Agentic-RAG]] — query-level 路由策略
- [[Knowledge-Graph]] — entity/relationship graph
- [[RAG-vs-LLM-Wiki]] — retrieval architecture 对比
- [[Corrective-RAG]] — retrieval quality 修正
- [[Structured-Agent-Memory]] — 结构化暴露 gap
- [[Decision-Centric-Architecture]] — ontology pipeline 同构
- [[Knowledge-Compilation]] — 语义层压缩
- [[Skills-as-Products]] — prompt quality 治理
- Prompt Caching（forward reference，未建 entity） — LLM call 成本优化