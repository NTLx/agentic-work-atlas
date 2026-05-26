---
type: entity
title: Dual-Tier LLM Architecture
aliases:
  - 双层 LLM 架构
  - 分层模型路由
definition: "按任务复杂度在小模型与大模型之间路由请求的 LLM 系统架构"
created: 2026-05-10
updated: 2026-05-25
tags:
  - AI-Architecture
  - Multi-Agent
  - Model-Routing
related_entities:
  - "[[Agent-Orchestration]]"
  - "[[Agentic-Engineering]]"
  - "[[Corrective-RAG]]"
  - "[[Sequence-Packing]]"
  - "[[Layered-AI-Sourcing]]"
  - "[[Evaluation-Set]]"
  - "[[Verifiable-Agent-Engineering]]"
source_raw:
  - "[[OncoAgent A Dual-Tier Multi-Agent Framework for Privacy-Preserving Oncology Clinical Decision Support]]"
  - "[[MachinaCheck Building a Multi-Agent CNC Manufacturability System on AMD MI300X]]"
---

> [!definition] 定义
> 双层 LLM 架构是一种模型路由模式：通过加权复杂度评分器（如肿瘤类型、分期、突变数量等因子）量化查询复杂度，低于阈值的路由到速度优化的小模型（如 9B），高于阈值的路由到深度推理的大模型（如 27B），实现速度与质量的最优平衡。

## 关键数据点

- **复杂度评分公式**: `S = w_cancer + w_stage + w_mutations + w_treatment`
- **决策边界**: S >= 0.5 → Tier 2（27B 深度推理）；S < 0.5 → Tier 1（9B 速度分诊）
- **OncoAgent 实例**: 罕见癌 +0.40、未知原发 +0.30、IV 期 +0.25、>=2 突变 +0.30、既往治疗 +0.10
- **验证案例**: IV 期胰腺癌 + KRAS + BRCA2 突变 → S = 0.80，正确路由到 Tier 2
- **人工覆盖**: 临床医生可通过 UI 手动覆盖层级选择
- **模型选择**: Tier 1 = Qwen 3.5-9B，Tier 2 = Qwen 3.6-27B
- **人工门控**: OncoAgent 对 Tier 2 查询和低 RAG 置信度查询触发 HITL，说明大模型路由常常也意味着更高审查等级
- **训练基础**: 双层模型由 266,854 个真实与合成病例微调，依赖 QLoRA、Unsloth 与 [[Sequence-Packing]] 提高训练效率

## 设计逻辑

双层架构的目标不是“省钱用小模型”，而是把不同风险、复杂度和成本的任务放进不同执行路径。

| 路径 | 适合任务 | 主要收益 | 主要风险 |
|------|----------|----------|----------|
| Tier 1 小模型 | 高频、常见、低风险、边界清楚 | 低延迟、低成本、可本地运行 | 复杂病例误判、罕见场景覆盖不足 |
| Tier 2 大模型 | 罕见、复杂、高风险、多条件推理 | 更强推理与综合能力 | 成本高、延迟高、更需要人工审查 |
| HITL | 高风险或置信度不足 | 保留临床责任和最终判断 | 吞吐下降，需要专业人员介入 |

这个模式可以迁移到企业 AI：客服、合规审查、工程支持和采购分析都可以先由复杂度评分器分流，而不是默认把所有请求交给最大模型。

## 前提与局限性

- **前提**: 需要明确定义的复杂度因子和权重，这依赖领域专家知识
- **前提**: 需要两个不同规模的模型，且都需要经过领域微调
- **局限性**: 加权评分是线性的，可能无法捕捉因子间的非线性交互
- **局限性**: 阈值和权重需要根据实际效果持续调优
- **局限性**: 如果复杂度评分器过粗，小模型会接到不该接的高风险任务，大模型也可能被低价值问题淹没
- **局限性**: 双层架构增加了评测复杂度，需要分别评估路由准确率、各层模型质量、人工覆盖率和端到端安全性

## 关联概念

- [[Agent-Orchestration]] — 双层路由是 Agent 编排中的请求分发模式
- [[Agentic-Engineering]] — 分层架构是 Agentic 工程中优化资源利用的关键策略
- [[Corrective-RAG]] — CRAG 为两个层级的模型提供质量可控的上下文
- [[Sequence-Packing]] — 训练优化让双层专门模型更容易本地微调
- [[Layered-AI-Sourcing]] — 企业模型采购也需要按任务层级分配能力来源
- [[Evaluation-Set]] — 路由阈值和模型层级必须用真实任务集校准
- [[Verifiable-Agent-Engineering]] — 分层路由必须与拒绝、HITL 和验证闭环一起设计
