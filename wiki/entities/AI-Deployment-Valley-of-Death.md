---
type: entity
title: AI Deployment Valley of Death
aliases:
  - AI Deployment Valley of Death
  - AI 部署死亡谷
  - 部署到 ROI 死亡谷
definition: "AI 项目从试点或部署到可衡量 ROI 之间的断层，常由流程重构、组织阻力、数据质量和治理边界造成"
created: 2026-06-01
updated: 2026-06-01
tags:
  - enterprise-ai
  - ai-deployment
  - roi
related_entities:
  - "[[AI-Deployment-Invisible-Costs]]"
  - "[[The-GenAI-Divide]]"
  - "[[Integration-Wall]]"
  - "[[Forward-Deployed-AI-Enablement]]"
source_raw:
  - "[[20260601-stanford-enterprise-ai-playbook]]"
  - "[[20260601-mit-nanda-genai-divide]]"
---

# AI Deployment Valley of Death（AI 部署死亡谷）

> [!definition] 定义
> **AI Deployment Valley of Death** 是 AI 项目从 demo、pilot 或初步部署走向可衡量 ROI 之间的断层。项目在这里经常被流程重构、数据质量、治理边界、组织阻力和业务指标闭环卡住。

## 核心问题

AI 项目最容易误把“能跑”当成“能创造业务结果”。但企业价值产生在更后面：

```text
demo
  -> pilot
  -> production
  -> workflow adoption
  -> measurable business outcome
```

死亡谷存在于 production 与 measurable business outcome 之间，也可能更早出现在 pilot 到 production 之间。

## 关键数据点

- Stanford 报告专门讨论“deployment and ROI”之间的 valley of death，并强调组织条件决定同样 use case 的结果差异。
- MIT/NANDA 报告显示，60% 的组织评估过企业级系统，20% 到达 pilot，只有 5% 到达 production。
- Stanford 报告称 77% 的最难挑战是变革管理、数据质量、流程重设计等无形成本。

## 降低死亡谷的路径

- 先确认流程有明确输入、输出、指标和失败退出条件。
- 让 executive sponsor 每周清障，而不是只批准预算。
- 用 [[Escalation-Based-Human-Oversight]] 设计常规路径和例外路径。
- 将部署经验回流为评测集、模板、数据接入规范和运维 playbook。
- 避免只把 adoption 当成功，必须追踪工作流是否改变、成本是否下降、速度是否提升。

## 前提与局限性

- “死亡谷”是分析框架，不是固定阶段。不同组织可能卡在 demo 到 pilot、pilot 到 production，或 production 到 ROI 的不同位置。
- 对研发助手、写作助手等个人工具，ROI 可能分散在时间节省和满意度里，短期难以被 P&L 精确捕捉。
- 如果组织只追求短期财务指标，可能错过能力建设、学习曲线和流程重构的长期价值。

## 关联概念

- [[AI-Deployment-Invisible-Costs]] — 死亡谷中的隐性成本。
- [[The-GenAI-Divide]] — 大量企业卡在试点和生产前后。
- [[Integration-Wall]] — demo 到生产的主要阻力。
- [[Forward-Deployed-AI-Enablement]] — 穿越死亡谷的一种现场方法。
