---
type: entity
title: AI Deployment Valley of Death
aliases:
  - AI Deployment Valley of Death
  - AI 部署死亡谷
  - 部署到 ROI 死亡谷
definition: "AI 项目从试点或部署到可衡量 ROI 之间的断层，常由流程重构、组织阻力、数据质量和治理边界造成"
created: 2026-06-01
updated: 2026-10-22
tags:
  - enterprise-ai
  - ai-deployment
evidence_level: high
claim_type: mixed
related_entities:
  - "[[AI-Deployment-Invisible-Costs]]"
  - "[[The-GenAI-Divide]]"
  - "[[Integration-Wall]]"
  - "[[Forward-Deployed-AI-Enablement]]"
  - "[[Alert-Closed-Loop]]"
source_raw:
  - "[[20260601-stanford-enterprise-ai-playbook]]"
  - "[[20260601-mit-nanda-genai-divide]]"
  - "[[20260702-ai-layoffs-reversed]]"
  - "[[20260719-if-ai-is-so-great-why-isnt-it-working]]"
  - "[[20260729-nejm-ai-triggered-rapid-response-mortality]]"
  - "[[20261022-latentspace-moshi]]"
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
- 以 [[Alert-Closed-Loop]] 为交付单元：RWJBarnabas（NEJM AI, 2026）把“模型 + 通知 + 责任人 + 流程 + 监控”作为整体交付并持续数年打磨，院内死亡率下降 4.5 个百分点——交付一个模型不等于交付一条产生结局的责任链。

## “系统已交付，但没人点”：采用本身是独立工程问题（Moshi / AIE，2026-10）

[[20261022-latentspace-moshi]] 记录了 AIE 会后 AI engineers 向 Moshi 创始人反馈的一类失败：团队/管理层认为存在真实痛点，工程师也已经把系统做出来并放进用户邮箱，但用户仍然**不点击、不进入工作流**。

同一访谈中，Anekha 对“人人都能做自己的 Claude dashboard”的观察提供了原因框架：一个界面可以很好地表达构建者自己的思维方式，但这不等于其他人会自然采用。她因此把 UI 与 recommendation system 连在一起——优秀产品不是只等待用户提出 query，而要在正确时机把高相关信息推到现有工作流表面。

这给本页的 `production → workflow adoption` 增加了一个极简但有代表性的中间链：

~~~text
problem stated
  → system built
  → system delivered
  → user notices it
  → user trusts it
  → user changes workflow
  → measurable outcome
~~~

**判断**：AI 显著降低前两三个节点的成本之后，后半段反而更容易暴露为 bottleneck。`delivery` 不是 `adoption`，`adoption` 也不是 `outcome`。

- **证据**：[[20261022-latentspace-moshi]]，Transcript 12:15、18:28–20:32。
- **边界**：这是 AIE 现场来访者的 selection-biased anecdotal evidence，不是企业 adoption 调查；它只能支持“这种失败模式存在”，不能估计发生频率。

## 前提与局限性

- “死亡谷”是分析框架，不是固定阶段。不同组织可能卡在 demo 到 pilot、pilot 到 production，或 production 到 ROI 的不同位置。
- 对研发助手、写作助手等个人工具，ROI 可能分散在时间节省和满意度里，短期难以被 P&L 精确捕捉。
- 如果组织只追求短期财务指标，可能错过能力建设、学习曲线和流程重构的长期价值。

## 关联概念

- [[AI-Deployment-Invisible-Costs]] — 死亡谷中的隐性成本。
- [[The-GenAI-Divide]] — 大量企业卡在试点和生产前后。
- [[Integration-Wall]] — demo 到生产的主要阻力。
- [[Forward-Deployed-AI-Enablement]] — 穿越死亡谷的一种现场方法。
- [[Alert-Closed-Loop]] — 项目常死于告警责任链的某个节点，而非模型性能。
