---
type: entity
title: Agent-Development-Lifecycle
aliases:
  - ADLC
  - Agent Development Lifecycle
  - 代理开发生命周期
definition: "AI 时代取代 SDLC 的软件生产生命周期范式——当 AI 让 implementation 从最慢最贵变为最快最便宜，SDLC 的线性人本假设崩塌；ADLC 让 agent 覆盖全生命周期，并以 Workflow 取代 CI/CD 作为编排原语"
created: 2026-08-13
updated: 2026-08-13
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
> **ADLC（Agent Development Lifecycle）** 是 Cloudflare（2026-08）提出的生命周期范式：SDLC（可溯至 RAND 1975 的 Systems Development Lifecycle）假设"许多人协作写代码"，而 AI 把最慢最贵的 implementation 变成最快最便宜，使下游所有环节超载；ADLC 主张 agent 覆盖整个生命周期而非只覆盖 generate 端——"The SDLC is for software teams. The ADLC is for software factories."

## 核心命题

### 实现加速悖论
- AI 把 implementation 从最慢最贵 → 最快最便宜
- 下游超载：开源维护者被成千 PR/issue 淹没；生产工程师被数量级上升的交付速率压垮
- "We are all trying to save our systems, our customers, and ourselves from slop."

### 七项工厂需求（平台必须重做的部分）
Programmatic / Horizontally scalable / Reproducible / Real-time push-based / Atomic / Permissioned / Self-improving——每个原先靠人手的步骤必须变成 agent 可驱动、可复现、可观测、可授权、可学习的形式。

### 自驾车类比（80% → 99%+）
"To give agents the keys to drive the SDLC, you can't give them a car designed for humans." 自动驾驶 10 年前就达到 80% 人类水平，但交钥匙的标准是 >99% 且更安全——所以自动驾驶车有 lidar/远程接管等人类车没有的东西；软件工厂同理需要 purpose-built 技术（Agent Traces、Remote Bindings、Permission escalation、Preview URLs）。

### Workflow 是新 CI/CD
CI/CD pipeline 只是 Workflow 的特例：Workflow 持久化状态、可重试、可嵌套、可动态定义、可 spawn agents/containers/browsers，配合 Artifacts 作为存储层——"A CI/CD pipeline is just a Workflow. But a Workflow can be so much more than a CI/CD pipeline."

## 与 SDLC 的对照

| 维度 | SDLC | ADLC |
|------|------|------|
| 假设 | 多人协作写代码 | agent 驱动流水线 |
| 人的位置 | 管理每一步 | 只留 inspiration/taste/judgement |
| 编排原语 | CI/CD pipeline（线性步骤） | Workflow（状态机 + 事件触发 + spawn） |
| 关键约束 | 人工审批 | programmatic / reproducible / atomic / permissioned |

## 关键数据点

- SDLC 溯源：RAND 1975 的 Systems Development Lifecycle
- 七项工厂需求：Programmatic / Horizontally scalable / Reproducible / Real-time push-based / Atomic / Permissioned / Self-improving
- 概念来源：Cloudflare (2026-08)

## 前提与局限性

- **vendor 视角**：ADLC 由 Cloudflare 提出并映射到自家产品栈，是平台叙事，需剥离营销层
- **范式声称**："SDLC 假设崩塌"是应然判断，文章未提供崩塌的量化数据（"orders of magnitude"无具体数字）
- **类比边界**：软件失败通常可回滚，未必需要自驾车级的 n nines 才能交钥匙——类比可能为 over-engineering 背书
- **治理盲区**：permissioned 需求讲了 escalation，未讲"agent 拿到更多权限后如何被审计/回收"

## 关联概念

- [[Software-Factory]] — ADLC 是工厂的生命周期范式
- [[Agent-Orchestration]] — Workflow 编排是 [[Agent-Orchestration|编排层]] 的声明式持久化版本
- [[Secure-Paved-Path]] — permissioned/atomic 需求是 paved path 的 agent 版
- [[Escalation-Based-Human-Oversight]] — escalation 权限机制的既有讨论
- [[Grindability-vs-Verifiability]] — 80%→99% 鸿沟的可验证性维度
- [[Knowledge-Work-Redefinition]] — implementation 贬值后人的剩余价值转移