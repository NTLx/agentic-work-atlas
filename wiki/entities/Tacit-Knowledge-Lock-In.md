---
type: entity
title: Tacit Knowledge Lock-In
aliases:
  - Tacit Knowledge Lock-In
  - 隐性知识锁定
  - 默会知识锁定
definition: "供应商通过掌握客户未写成文档的业务规则、评测集和流程调优经验形成的锁定，比传统 UI 习惯锁定更隐蔽、更难迁移"
created: 2026-05-23
updated: 2026-05-23
tags:
  - AI-deployment
  - enterprise
  - vendor-lock-in
related_entities:
  - "[[Evaluation-Set]]"
  - "[[Forward-Deployed-Engineer]]"
  - "[[Integration-Wall]]"
  - "[[Deployment-Product-Flywheel]]"
  - "[[Layered-AI-Sourcing]]"
source_raw:
  - "[[The Return of the Deployment Company]]"
---

# Tacit Knowledge Lock-In（隐性知识锁定）

> [!definition] 定义
> **Tacit Knowledge Lock-In（隐性知识锁定）** 是 AI 部署中的新型供应商锁定：锁定点不再主要是人类界面习惯或数据迁移，而是供应商掌握了客户未写成文档的业务规则、评测集、提示链、流程配置和现场调优经验。

## 关键数据点

- 文章指出，Agent 会削弱传统 SaaS 基于人类 UI 熟悉度的锁定，但 FDE 会建立另一种锁定：把客户的隐性工作流知识编码进供应商系统。
- 典型时间线是：第 1 个月搭出 v1，第 3 到第 6 个月积累大量边界案例和评测样本，第 12 个月业务流程开始围绕 AI 重写，第 18 个月切换供应商需要重建评测集、流程和员工习惯。
- 这种锁定会削弱客户的 walk-away option。即使竞品便宜，客户也要承担评测集重建、服务质量下降和组织再训练成本。
- 文章建议用评测集导出权、续约价格上限、退出交接条款和内部接管计划降低锁定风险。

## 前提与局限性

- 隐性知识锁定在高频、核心、高敏感工作流中最强；一次性低风险场景中的 FDE 不一定会形成长期依赖。
- 如果企业共同拥有评测集、保留提示配置和运行文档，并培养内部 AI operations 团队，锁定强度会下降。
- 供应商把现场经验抽象成通用平台能力并不必然有害；风险发生在客户的专有规则被不可见、不可导出、不可约束地沉淀到供应商侧。

## 关联概念

- [[Evaluation-Set]] — 隐性知识被显式化后的关键载体
- [[Forward-Deployed-Engineer]] — 进入现场提取隐性知识的人
- [[Integration-Wall]] — 真实企业约束越厚，隐性知识锁定越容易形成
- [[Deployment-Product-Flywheel]] — 供应商飞轮可能与客户知识主权发生张力
- [[Layered-AI-Sourcing]] — 分层 sourcing 用来降低单一供应商锁定

