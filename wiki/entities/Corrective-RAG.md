---
type: entity
title: Corrective RAG
aliases:
  - Corrective RAG
  - CRAG
definition: "在生成前先评分、重构和拒绝低质量检索结果的 RAG 纠错模式"
created: 2026-05-10
updated: 2026-05-25
tags:
  - RAG
  - AI-Architecture
  - Multi-Agent
related_entities:
  - "[[Agent-Orchestration]]"
  - "[[Agentic-Engineering]]"
  - "[[Dual-Tier-LLM-Architecture]]"
  - "[[Reflexion]]"
  - "[[Zero-PHI-Policy]]"
  - "[[Evaluation-Set]]"
  - "[[Verifiable-Agent-Engineering]]"
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
- **知识库来源**: OncoAgent 从 138 个 NCCN 页面抽取 77 个医师级 PDF，覆盖 70+ 专业指南，并排除 patient-facing 材料
- **嵌入与存储**: 使用医学向量模型和本地 ChromaDB，避免通用 embedding 无法理解临床术语
- **失败路径**: 文档评分不合格时最多触发一次 query reformulation；仍失败时进入安全拒答，而不是让生成模型硬答

## 工程价值

CRAG 的价值不只是“检索更准”，而是把 RAG 从“找一些上下文给模型”改成可验证流水线：

1. 先用召回扩大候选集。
2. 再用距离门控筛掉明显域外内容。
3. 再用 cross-encoder 或 judge 评分判断语义相关性。
4. 如果证据不足，重写查询或拒绝回答。
5. 最后才把上下文交给生成模型。

这让高风险 Agent 不再把检索错误静默传递给 LLM。对医疗、法律、金融和合规问答来说，最危险的不是“没有答案”，而是“拿错证据回答得很自信”。

## 前提与局限性

- **前提**: 需要高质量的领域向量知识库；通用嵌入模型（如 all-MiniLM-L6-v2）在临床术语语义上表现不佳，需使用领域专用嵌入模型
- **前提**: 需要足够的文档覆盖度；知识库外的查询只能返回安全拒绝
- **局限性**: 距离阈值需要针对特定领域进行校准，不同领域的最优阈值不同
- **局限性**: 查询重构最多重试 1 次，复杂查询可能需要更多轮迭代
- **局限性**: CRAG 只能纠正“检索证据质量”问题，不能保证生成模型正确解释证据
- **局限性**: 如果知识库本身过时、缺失或来源混杂，评分流程只能暴露缺口，不能凭空补齐权威知识

## 关联概念

- [[Agent-Orchestration]] — CRAG 常作为多 Agent 系统中的检索节点
- [[Dual-Tier-LLM-Architecture]] — CRAG 为不同层级的模型提供质量可控的上下文
- [[Agentic-Engineering]] — CRAG 是 Agentic 工程中提升 RAG 质量的核心模式之一
- [[Reflexion]] — CRAG 处理上下文质量，Reflexion 处理生成结果质量
- [[Zero-PHI-Policy]] — 医疗场景中，CRAG 查询应先经过隐私前置处理
- [[Evaluation-Set]] — CRAG 阈值和评分器需要用真实失败样本校准
- [[Verifiable-Agent-Engineering]] — CRAG 是“上下文可验证”的代表机制
