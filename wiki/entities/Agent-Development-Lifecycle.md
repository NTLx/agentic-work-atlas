---
type: entity
title: Agent-Development-Lifecycle
aliases:
  - ADLC
  - Agent Development Lifecycle
  - 代理开发生命周期
definition: "Cloudflare 提出的 Agent Development Lifecycle（ADLC）工程范式：面向 Agent 驱动的软件生产，把 agent 能力扩展到规划、实现、验证、部署与维护，并以可持久化 Workflow 等机制补充传统 SDLC/CI-CD；它是厂商提出的框架，不等于 SDLC 已被普遍取代。"
created: 2026-08-13
updated: 2026-11-28
evidence_level: medium
claim_type: mixed
tags:
  - software-engineering
  - lifecycle
  - agentic-engineering
related_entities:
  - "[[Software-Factory]]"
  - "[[Agent-Orchestration]]"
  - "[[Secure-Paved-Path]]"
  - "[[Agent-Observability]]"
  - "[[Escalation-Based-Human-Oversight]]"
  - "[[Grindability-vs-Verifiability]]"
  - "[[Knowledge-Work-Redefinition]]"
source_raw:
  - "[[20260804-agent-development-lifecycle-adlc]]"
  - "[[20260805-how-we-use-ai-cloudflare-os]]"
---

# Agent-Development-Lifecycle（ADLC）

> [!definition] 定义
> **ADLC（Agent Development Lifecycle）** 是 Cloudflare（2026-08）提出的生命周期范式：作者以传统多人协作的 SDLC 为对照，认为实现加速可能超过审查、部署和维护容量；这是厂商提出的瓶颈迁移解释，不是所有项目的经验定律；ADLC 主张 agent 覆盖整个生命周期而非只覆盖 generate 端——"The SDLC is for software teams. The ADLC is for software factories."

## 核心命题

### 实现加速悖论
- 候选实现生成成本下降时，若验收和发布容量未同步增长，队列和维护压力可能上升。
- 原文给出维护者与生产工程师的描述，未提供可比较的跨组织增长率或任务总成本。
- "We are all trying to save our systems, our customers, and ourselves from slop."

### 七项工厂设计目标（Cloudflare 提议）
Programmatic / Horizontally scalable / Reproducible / Real-time push-based / Atomic / Permissioned / Self-improving——按委派范围选择必要机制；保留人工例外、风险控制、独立验证和停机/撤销路径，不要求每项活动都自动化。

### 自驾车类比（80% → 99%+）
"To give agents the keys to drive the SDLC, you can't give them a car designed for humans." 作者以未经本文测量的自动驾驶百分比作类比，不能用于标定软件任务成功率或生产授权门槛；可迁移的是按失效影响设计专用反馈与接管机制（Agent Traces、Remote Bindings、Permission escalation、Preview URLs）。

### Workflow 是新 CI/CD
CI/CD pipeline 只是 Workflow 的特例：Workflow 持久化状态、可重试、可嵌套、可动态定义、可 spawn agents/containers/browsers，配合 Artifacts 作为存储层——"A CI/CD pipeline is just a Workflow. But a Workflow can be so much more than a CI/CD pipeline."

## 与 SDLC 的对照

| 维度 | SDLC | ADLC |
|------|------|------|
| 假设 | 多人协作写代码 | agent 驱动流水线 |
| 人的位置 | 管理大量具体步骤 | 更集中于目标、边界、验证、风险与例外处理 |
| 编排原语 | CI/CD 可支持 DAG、事件、审批等 | 持久状态、动态委派的 Workflow，可与 CI/CD 组合 |
| 关键约束 | 人工审批 | programmatic / reproducible / atomic / permissioned |

## AI-Native SDLC 契约产物（Anthropic 独立 playbook，08-22 补充）

Anthropic（Louis Claxton，2026-08-21，[[20260822-the-ai-native-sdlc-playbook]]）提出相近目标的六阶段（Plan / Design / Build / Test / Deploy / Maintain）playbook，不是 Cloudflare ADLC 的官方版本。核心是 **loop 非 pipeline** + **intent 第一公民**：

- **intent.md**（第一公民 = source of truth）：发起人用自己语言写问题/目标/约束三段式，Design/Build 分别派生 spec.md 与 plan.md；
- **四大基础设施**：CLAUDE.md（context）/ Skills（机构知识）/ Hooks（build-time 硬门禁）/ Evals（20-50 真实任务 + CI 周期，stage-gate 版 QA）；
- **瓶颈左移的来源主张**：该材料认为 code 不再是主要瓶颈后，瓶颈会左移到 build 之前（plan / design / review / test），并把人的剩余角色概括为 inspiration / taste / judgement；本页将其收窄为目标、边界、验证、风险与例外处理，而非普遍的人机分工事实。

## 关键数据点

- SDLC 溯源：Cloudflare 原文追溯至 RAND 1975 的 Systems Development Lifecycle；未独立复核历史起源
- 七项工厂需求：Programmatic / Horizontally scalable / Reproducible / Real-time push-based / Atomic / Permissioned / Self-improving
- 概念来源：Cloudflare (2026-08)

## 前提与局限性

- **vendor 视角**：ADLC 由 Cloudflare 提出并映射到自家产品栈，是平台叙事，需剥离营销层
- **范式声称**："SDLC 假设崩塌"是应然判断，文章未提供崩塌的量化数据（"orders of magnitude"无具体数字）
- **类比边界**：软件有可回滚部署也有不可逆外部效果、数据泄漏与破坏；可靠性门槛取决于风险、任务分布和补偿能力，不能从驾驶类比得出——类比可能为 over-engineering 背书
- **治理盲区**：permissioned 需求讲了 escalation，未讲"agent 拿到更多权限后如何被审计/回收"

## 关联概念

- [[Software-Factory]] — ADLC 是工厂的生命周期范式
- [[Agent-Orchestration]] — Workflow 编排是 [[Agent-Orchestration|编排层]] 的声明式持久化版本
- [[Secure-Paved-Path]] — permissioned/atomic 需求是 paved path 的 agent 版
- [[Escalation-Based-Human-Oversight]] — escalation 权限机制的既有讨论
- [[Grindability-vs-Verifiability]] — 自治风险与验证边界的类比，不作量化依据
- [[Knowledge-Work-Redefinition]] — implementation 贬值后人的剩余价值转移
