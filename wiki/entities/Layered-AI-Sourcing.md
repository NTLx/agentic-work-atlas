---
type: entity
title: Layered AI Sourcing
aliases:
  - Layered AI Sourcing
  - 分层 AI 来源策略
  - 分层 AI 能力采购
  - 混合 AI 部署策略
definition: "按工作流敏感度、调用频率、成本曲线、任务分布和前沿能力需求，把 AI 能力分配给 on-prem、专门化小模型、cloud API、FDE 或内部团队的采购与部署策略"
created: 2026-05-23
updated: 2026-05-23
tags:
  - AI-deployment
  - enterprise
evidence_level: medium
claim_type: mixed
related_entities:
  - "[[Hardware-Sovereignty]]"
  - "[[Forward-Deployed-Engineer]]"
  - "[[Evaluation-Set]]"
  - "[[Tacit-Knowledge-Lock-In]]"
  - "[[Integration-Wall]]"
  - "[[AI-Ready-Organization]]"
  - "[[Specialized-Small-Models]]"
  - "[[Distributional-Alignment]]"
source_raw:
  - "[[The Return of the Deployment Company]]"
  - "[[Specialization Beats Scale A Strategic Variable Most AI Procurement Decisions Overlook]]"
---

# Layered AI Sourcing（分层 AI 来源策略）

> [!definition] 定义
> **Layered AI Sourcing（分层 AI 来源策略）** 是企业在 AI 采购和部署中避免单一答案的方法：按工作流敏感度、调用频率、成本曲线、任务分布和是否需要前沿模型能力，把不同 AI 能力分配给 on-prem、本地开源模型、专门化小模型、cloud API、FDE 服务或内部团队。

## 关键数据点

- 文章反对把企业 AI 决策简化成“FDE vs on-prem”，认为正确问题是：哪些能力应该本地化，哪些能力可以外部采购。
- 推荐分层：核心、高频、高敏感应用优先 on-prem；低频但需要前沿能力的应用可用 FDE 或 cloud API；过渡期可以用 FDE 加速学习，同时建设内部能力。
- 文章判断 2026 年开源模型、企业 GPU、本地推理框架、RAG 工具和 UI 工具已经让多数企业任务的 on-prem 门槛下降。
- 分层策略的关键资产是评测集和内部 AI operations 能力。没有可迁移评测集，企业无法比较不同模型或供应商；没有内部团队，企业无法接管。
- DharmaOCR 案例补充了模型层的分层变量：在巴西葡萄牙语 OCR benchmark 中，专门化 3B 模型同时领先被测试的商业 API，并以约 52 倍更低的每百万页推理成本运行。
- 因此分层采购不只是在 on-prem、cloud API 和 FDE 之间选择，也要区分通用 frontier model、开源通用模型、领域模型和业务域专门模型。

## 前提与局限性

- “核心”和“前沿”的边界会动态变化。今天需要外部前沿能力的任务，可能在下一代开源模型成熟后变成本地核心能力。
- on-prem 不是银弹。企业需要内部 AI operations 人才、模型维护能力和更长的 ROI 视角。
- 分层 sourcing 要求组织能清楚描述自己的流程、数据边界和风险等级；如果组织自身混乱，分层会退化成供应商驱动的采购。
- 专门化小模型只适合任务边界清楚、输出可验证、数据分布可获得的场景；开放式推理和探索型任务仍可能需要 frontier model。

## 关联概念

- [[Hardware-Sovereignty]] — 分层策略中高敏感、高频核心能力的本地化基础
- [[Forward-Deployed-Engineer]] — 外部 FDE 适合加速学习或补足前沿能力缺口
- [[Evaluation-Set]] — 比较、迁移和接管不同 AI 能力的共同标尺
- [[Tacit-Knowledge-Lock-In]] — 分层策略要避免的单一供应商依赖
- [[Integration-Wall]] — 不同层级的 sourcing 需要面对不同厚度的集成约束
- [[AI-Ready-Organization]] — 组织自知越强，分层边界越清楚
- [[Specialized-Small-Models]] — 高频、可验证、分布清楚的工作流可以形成单独模型层
- [[Distributional-Alignment]] — 模型选择需要评估训练历史与部署任务的贴近程度
