---
type: entity
title: Corrective RAG
aliases:
  - Corrective RAG
  - CRAG
definition: "一种 RAG 改进模式，通过文档相关性评分和查询重构来消除检索到的语义不相关内容，从而减少幻觉。由 Shi et al. (2024) 提出。"
created: 2026-05-10
updated: 2026-05-10
tags:
  - RAG
  - AI-Architecture
  - Multi-Agent
related_entities:
  - "[[Agent-Orchestration]]"
  - "[[Agentic-Engineering]]"
  - "[[Dual-Tier-LLM-Architecture]]"
source_raw:
  - "[[OncoAgent A Dual-Tier Multi-Agent Framework for Privacy-Preserving Oncology Clinical Decision Support]]"
---

> [!definition] 定义
> Corrective RAG (CRAG) 是一种检索增强生成的改进模式，在标准 RAG 流程中增加文档相关性评分环节。检索到的文档先经过二元相关性分类，不相关的文档触发自动查询重构和重新检索，从而消除"标题看似相关但语义不匹配"的幻觉来源。

## 关键数据点

- **四阶段流水线**: 召回（Bi-Encoder top-15）→ 距离门控（cosine < 0.10）→ 重排序（Cross-Encoder top-5）→ 上下文裁剪（max 6,000 字符）
- **反幻觉策略**: 任何查询在距离门控阶段失败即返回安全拒绝，不调用生成模型，保证零幻觉输出
- **OncoAgent 实践**: 文档评分修复后成功率 100%，RAG 置信度从 0.0 提升至 2.3+
- **并行评分延迟**: 3-5 篇文档 < 5 秒
- **距离阈值校准**: 医学查询 ~0.06-0.09，域外查询 ~0.11-0.15，硬阈值 0.10

## 前提与局限性

- **前提**: 需要高质量的领域向量知识库；通用嵌入模型（如 all-MiniLM-L6-v2）在临床术语语义上表现不佳，需使用领域专用嵌入模型
- **前提**: 需要足够的文档覆盖度；知识库外的查询只能返回安全拒绝
- **局限性**: 距离阈值需要针对特定领域进行校准，不同领域的最优阈值不同
- **局限性**: 查询重构最多重试 1 次，复杂查询可能需要更多轮迭代

## 关联概念

- [[Agent-Orchestration]] — CRAG 常作为多 Agent 系统中的检索节点
- [[Dual-Tier-LLM-Architecture]] — CRAG 为不同层级的模型提供质量可控的上下文
- [[Agentic-Engineering]] — CRAG 是 Agentic 工程中提升 RAG 质量的核心模式之一
