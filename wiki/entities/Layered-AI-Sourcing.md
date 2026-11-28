---
type: entity
title: Layered AI Sourcing
aliases:
  - Layered AI Sourcing
  - 分层 AI 来源策略
  - 分层 AI 能力采购
  - 混合 AI 部署策略
definition: "按任务分布、敏感度、调用频率、成本、能力需求、供应商可得性与退出约束，把 AI 工作负载分配给本地/开放模型、专门化小模型、cloud API、FDE 或内部团队的采购与部署策略。"
created: 2026-05-23
updated: 2026-11-28
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
  - "[[20260831-the-price-of-entry-to-the-frontier]]"
---

# Layered AI Sourcing（分层 AI 来源策略）

> [!definition] 定义
> **Layered AI Sourcing（分层 AI 来源策略）** 是企业在 AI 采购和部署中避免单一答案的方法：按工作流敏感度、调用频率、成本曲线、任务分布和是否需要前沿模型能力，把不同 AI 能力分配给 on-prem、本地开源模型、专门化小模型、cloud API、FDE 服务或内部团队。

## 关键数据点

- 文章反对把企业 AI 决策简化成“FDE vs on-prem”，认为正确问题是：哪些能力应该本地化，哪些能力可以外部采购。
- 将本地、私有托管、共享API及FDE作为候选；数据/许可/质量门是硬约束，之后比较全部请求、失败、复核及分摊成本/验收成功数。高频不自动意味着本地更便宜，敏感不自动等于自托管安全。
- 早期来源判断 2026 年开源模型、企业 GPU、本地推理框架、RAG 工具和 UI 工具正在降低部分企业任务的 on-prem 门槛；这是一种产业判断，不应外推成“多数任务都适合本地化”。
- 分层策略的关键资产是评测集和内部 AI operations 能力。没有可迁移评测集，企业无法比较不同模型或供应商；没有内部团队，企业无法接管。
- DharmaOCR是供应商特定葡语OCR基准及推理费用估计，报告3B领先被测试API、每百万页约52倍费用差；本轮未独立核算训练、硬件、人工、失败及部署成本，不作全成本或普遍质量排序。
- 因此分层采购不只是在 on-prem、cloud API 和 FDE 之间选择，也要区分通用 frontier model、开放权重模型、领域模型和业务域专门模型。
- 2026-08 的新边界是**可得性与退出权**：即使某个 frontier API 当前质量最好，也要评估地区/组织访问限制、默认供应商绑定、数据驻留、替代路径与迁移能力。

## 前提与局限性

- “核心”和“前沿”的边界会动态变化。今天需要外部前沿能力的任务，可能在下一代开源模型成熟后变成本地核心能力。
- on-prem 不是银弹。企业需要内部 AI operations 人才、模型维护能力和更长的 ROI 视角。
- 分层 sourcing 要求组织能清楚描述自己的流程、数据边界和风险等级；如果组织自身混乱，分层会退化成供应商驱动的采购。
- 任务清楚可验证有利于评测专门化；模型大小与开放程度都不是绝对适用界限，先验证任务表现和总成本。

## 关联概念

- [[Hardware-Sovereignty]] — 分层策略中高敏感、高频核心能力的本地化基础
- [[Forward-Deployed-Engineer]] — 外部 FDE 适合加速学习或补足前沿能力缺口
- [[Evaluation-Set]] — 比较、迁移和接管不同 AI 能力的共同标尺
- [[Tacit-Knowledge-Lock-In]] — 分层策略要避免的单一供应商依赖
- [[Integration-Wall]] — 不同层级的 sourcing 需要面对不同厚度的集成约束
- [[AI-Ready-Organization]] — 组织自知越强，分层边界越清楚
- [[Specialized-Small-Models]] — 高频、可验证、分布清楚的工作流可以形成单独模型层
- [[Distributional-Alignment]] — 模型选择需要评估训练历史与部署任务的贴近程度
