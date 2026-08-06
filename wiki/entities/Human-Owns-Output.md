---
type: entity
title: Human-Owns-Output
aliases:
  - Human Owns Output
  - 人类拥有输出
  - 人类拥有输出原则
definition: "把 agent 输出的质量、测试与工作流责任归属给人类使用者的原则——AI 是工具和工具制造者而非团队成员；agent 输出责任随岗位继承（离职交接给管理者），共享 agent 不转移责任"
created: 2026-08-06
updated: 2026-08-06
evidence_level: medium
claim_type: extracted
tags:
  - governance
  - organization
  - Human-Potential
related_entities:
  - "[[Ownership]]"
  - "[[Human-Governor-Agent-Operator]]"
  - "[[Escalation-Based-Human-Oversight]]"
  - "[[Agent-First-Enterprise]]"
  - "[[Permission-Ratchet-Mechanism]]"
  - "[[AI-Era-Taste-and-Judgment]]"
source_raw:
  - "[[20260805-how-we-use-ai-cloudflare-os]]"
---

# Human-Owns-Output（人类拥有输出原则）

> [!definition] 定义
> Human-Owns-Output 是把 agent 输出（质量、测试、工作流定义）的责任归属给人类使用者的原则：AI 是工具和工具制造者（tool and toolmaker），不是团队成员（team member）。使用者负责定义依赖 AI 输出的质量、测试和工作流；部署 agent 的用户和团队对 agent 的输出负责。

## 核心主张

Cloudflare CIO Sam Rhea 将其列为 AI 落地五原则之一（2026-08）：

> We view AI as a tool and toolmaker, not a team member. We expect humans to take responsibility for defining the quality, testing, and workflows that rely on AI output. The users and teams that ship agents are responsible for the output of those agents.

## 责任随岗位继承：agent 时代的组织机制

Human-Owns-Output 最具可操作化的部分是**责任继承**：

> Someone leaves? Their manager inherits the responsibility of their agents in the same way they inherit their other workflows.

这把 Ownership（个人承担后果的意愿）从价值观转成组织机制：agent 不是可以"一删了之"的临时物，而是像员工工作流一样拥有持续责任对象。离职交接时，agent 的责任像其他职责一样被管理者继承——agent 的"无自然终点"（见 [[Permission-Ratchet-Mechanism]]）在这里被责任链条兜住。

## 与相关概念的区别

| 概念 | 讲什么 | 差异 |
|------|--------|------|
| [[Ownership]] | 个人承担后果的意愿与能力 | Human-Owns-Output 是 Ownership 在 agent 时代的组织机制化：不是"愿不愿负责"，而是"组织规定责任归谁、如何继承" |
| [[Human-Governor-Agent-Operator]] | 人机分工模式（人设定目标/约束，agent 执行） | Governor 讲分工边界；Human-Owns-Output 讲责任归属与继承时点 |
| [[Escalation-Based-Human-Oversight]] | AI 自主处理常规、人类审查例外 | 监督模式的一种；Human-Owns-Output 是责任原则，不规定具体监督时点 |

## 边界与张力

- **与"外包"的张力**：Cloudflare 同时用"魔法邮箱"让员工把"不想做的活"交给真人+AI 值守——当员工把工作外包给 AI 邮箱，责任归员工（使用者）还是值守团队？原则 3 在"人类外包给 AI"的中间态下归属模糊（综合判断，来源仅单方叙事）。
- **不规定技术实现**：该原则声明责任归属，但不规定 agent 需要何种可观测性/日志/审计才能让责任可追（对照 [[Agent-Observability]]、[[Agent-Legibility]]）。责任的"可追性"依赖 harness 基础设施。
- **与权限的关系**：责任继承若无权限同步（agent 权限随 owner 转岗/离职收缩），会与 [[Permission-Ratchet-Mechanism]] 的"持久授予 + 无自然终点"叠加。Human-Owns-Output 解决"谁负责"，Permission-Ratchet 处理"权限何时收回"，二者需要协同设计。

## 关键数据点

- Cloudflare AI 落地五原则之一，由 CTO+CIO 起草、各组织领导评审后确立（2026-08-05，来源 [[20260805-how-we-use-ai-cloudflare-os]]）
- 责任继承机制原文："Someone leaves? Their manager inherits the responsibility of their agents in the same way they inherit their other workflows"
- "AI 是工具和工具制造者（tool and toolmaker），不是团队成员（team member）"——原则的定位表述
- 共享 agent 时责任归属不变：接收者用自己权限认证（gatekeeper 共享语义），agent 输出责任不随共享转移

## 前提与局限性

- **单来源自述**：来自 Cloudflare CIO 博客，成效数据无独立验证（evidence_level: medium, claim_type: extracted——原则陈述为原文提取，但"生效"主张未实证）。
- **外包中间态的归属模糊**：当员工把"不想做的活"交给魔法邮箱（真人+AI 值守），输出责任归员工（使用者）还是值守团队？原则 3 在此中间态下未定义清楚（综合判断）。
- **不规定技术实现**：原则声明责任归属，但 agent 需要何种可观测性/日志/审计才能让责任可追（[[Agent-Observability]]、[[Agent-Legibility]]）不在原则内——责任的"可追性"依赖 harness 基础设施。
- **责任继承与权限回收需协同**：若 agent 权限不随 owner 转岗/离职收缩，责任继承会与 [[Permission-Ratchet-Mechanism]] 的"持久授予 + 无自然终点"叠加——Human-Owns-Output 解决"谁负责"，权限何时收回仍需另外设计。

## 关联概念

- [[Ownership]] — 责任原则的个体价值观基础
- [[Human-Governor-Agent-Operator]] — 责任分工的另一面
- [[Escalation-Based-Human-Oversight]] — 人类审查的实现模式之一
- [[Agent-First-Enterprise]] — Agent 运营流程时的责任分配
- [[Permission-Ratchet-Mechanism]] — 责任继承与权限回收的协同
- [[AI-Era-Taste-and-Judgment]] — 人类负责输出质量的判断力要求
