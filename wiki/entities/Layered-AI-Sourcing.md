---
type: entity
title: Layered AI Sourcing
aliases:
  - Layered AI Sourcing
  - 分层 AI 来源策略
  - 分层 AI 能力采购
  - 混合 AI 部署策略
definition: "按工作流敏感度、调用频率、成本曲线和前沿能力需求，把 AI 能力分配给 on-prem、cloud API、FDE 或内部团队的采购与部署策略"
created: 2026-05-23
updated: 2026-05-23
tags:
  - AI-deployment
  - enterprise
  - sourcing
related_entities:
  - "[[Hardware-Sovereignty]]"
  - "[[Forward-Deployed-Engineer]]"
  - "[[Evaluation-Set]]"
  - "[[Tacit-Knowledge-Lock-In]]"
  - "[[Integration-Wall]]"
  - "[[AI-Ready-Organization]]"
source_raw:
  - "[[The Return of the Deployment Company]]"
---

# Layered AI Sourcing（分层 AI 来源策略）

> [!definition] 定义
> **Layered AI Sourcing（分层 AI 来源策略）** 是企业在 AI 采购和部署中避免单一答案的方法：按工作流敏感度、调用频率、成本曲线和是否需要前沿模型能力，把不同 AI 能力分配给 on-prem、本地开源模型、cloud API、FDE 服务或内部团队。

## 关键数据点

- 文章反对把企业 AI 决策简化成“FDE vs on-prem”，认为正确问题是：哪些能力应该本地化，哪些能力可以外部采购。
- 推荐分层：核心、高频、高敏感应用优先 on-prem；低频但需要前沿能力的应用可用 FDE 或 cloud API；过渡期可以用 FDE 加速学习，同时建设内部能力。
- 文章判断 2026 年开源模型、企业 GPU、本地推理框架、RAG 工具和 UI 工具已经让多数企业任务的 on-prem 门槛下降。
- 分层策略的关键资产是评测集和内部 AI operations 能力。没有可迁移评测集，企业无法比较不同模型或供应商；没有内部团队，企业无法接管。

## 前提与局限性

- “核心”和“前沿”的边界会动态变化。今天需要外部前沿能力的任务，可能在下一代开源模型成熟后变成本地核心能力。
- on-prem 不是银弹。企业需要内部 AI operations 人才、模型维护能力和更长的 ROI 视角。
- 分层 sourcing 要求组织能清楚描述自己的流程、数据边界和风险等级；如果组织自身混乱，分层会退化成供应商驱动的采购。

## 关联概念

- [[Hardware-Sovereignty]] — 分层策略中高敏感、高频核心能力的本地化基础
- [[Forward-Deployed-Engineer]] — 外部 FDE 适合加速学习或补足前沿能力缺口
- [[Evaluation-Set]] — 比较、迁移和接管不同 AI 能力的共同标尺
- [[Tacit-Knowledge-Lock-In]] — 分层策略要避免的单一供应商依赖
- [[Integration-Wall]] — 不同层级的 sourcing 需要面对不同厚度的集成约束
- [[AI-Ready-Organization]] — 组织自知越强，分层边界越清楚

