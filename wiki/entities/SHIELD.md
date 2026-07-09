---
type: entity
title: "SHIELD（Safeguarding Human Expertise and Incidental Learning in Development）"
aliases:
  - Agents That Teach
definition: "Accenture Labs 提出的多 agent 系统，通过观察 coding agent 的推理链，在不打断开发流程的前提下，以 out-of-band 渠道（Probe Queue + Microlearning Feed）偿还 Knowledge Debt。"
created: 2026-07-09
updated: 2026-07-09
source_raw:
  - "[[20260709-agents-that-teach-knowledge-debt]]"
tags:
  - entity
  - agentic-engineering
evidence_level: medium
claim_type: extracted
---

# SHIELD（Safeguarding Human Expertise and Incidental Learning in Development）

## 定义

[[SHIELD]] 是 Accenture Labs 提出的多 agent 系统，是 [[Incidental-Learning|附带学习]] 恢复六原则的实例化。它观察 AI coding agent 的推理和行为，识别真正的学习机会，通过 out-of-band 渠道（Probe Queue + Microlearning Feed）在不打断开发流程的前提下向开发者呈现上下文绑定的微学习内容，偿还 [[Knowledge-Debt]]。

## 核心机制

### Agent 流水线

```
Telemetry Observer Agent
    ↓ （遥测流：agent 的每次代码变更 + 推理 + 替代方案 + 置信度）
Teachability Triage Agent
    ↓ （识别候选概念 → 检查 Developer's Evolving Concept Map → 评估 teachability signals）
Probe Generator Agent
    ↓ （生成针对性问题 → 异步推入 Probe Queue）
Knowledge Assessor Agent
    ↓ （评估开发者回答 → 判断知识缺口深度 → 更新 Concept Map）
Microlearning Generator Agent
    ↓ （生成上下文绑定的微学习 → 推入微学习 Feed）
Knowledge Assessor Agent（再次）
    ↓ （学完后 comprehension check → 闭环验证 → 更新 Concept Map）
```

### 六原则到组件的映射

| 原则 | 实现组件 | 机制 |
|------|---------|------|
| Contextual | Microlearning Generator | 内容与具体代码变更绑定 |
| Grounded | Telemetry Observer | 基于 agent 推理链而非仅代码变更 |
| Ambient | Probe Queue + Microlearning Feed | IDE 内异步渠道，开发者选择何时参与 |
| Selective | Teachability Triage | 只针对通过 teachability signals 检查的概念 |
| Adaptive | Developer's Evolving Concept Map | 适配开发者知识水平和历史 |
| Closed-Loop | Knowledge Assessor | 验证学习是否内化，更新 Concept Map |

### 冷启动处理

Developer's Evolving Concept Map 在冷启动时通过分析开发者自己编写的代码（非 AI 生成）初始化——假设开发者自己写的代码涉及的概念是已知的。

## 关键数据点

- Accenture Labs 提出的多 agent 系统
- 通过 Probe Queue + Microlearning Feed 在不打断开发流程的前提下偿还 [[Knowledge-Debt]]

## 技术栈

- IDE：VSCode 扩展
- 多 agent 框架：CrewAI
- 知识图谱：Neo4j（Developer's Concept Map）
- LLM：GPT-5.1（遥测解释、分诊、探测生成、评估、微学习生成）
- 云平台：Azure
- 被观察的 coding agent：Claude Code（当前），扩展到其他 agent 中

## 前提与局限性

- **仅有原型 demo**：无用户研究验证学习效果。"Stakeholder promising feedback" 不等于教育有效性
- **技术栈重型**：Neo4j + GPT-5.1 + CrewAI + Azure，采纳门槛高
- **冷启动可靠性未知**：通过开发者自己写的代码推断已知概念——这个推断在多大程度上准确？
- **教学 agent vs 生成 agent 的角色分化**：论文隐含"优化代码生成的模型可能不适合做教学 agent"，但 SHIELD 使用的 GPT-5.1 与 coding agent 使用的 Claude Code 是不同模型，这一选择是否有实证依据未说明
- **单源**：仅来自 Accenture Labs 一篇论文，无独立复现

## 与 Agent-Harness 的关系

[[SHIELD]] 可被理解为一种特殊类型的 [[Agent-Harness]]——它不是约束 coding agent 的输出质量，而是约束和观察 coding agent 的行为来服务于人的长期能力发展。这扩展了 harness 的定义：

- 传统 harness：服务于代码质量、安全性、合规性
- SHIELD 式 harness：服务于人的认知发展

## 关联概念

- [[Knowledge-Debt]] — SHIELD 的目标：偿还知识债务
- [[Incidental-Learning]] — SHIELD 恢复的学习路径
- [[Agent-Harness]] — SHIELD 是一种特殊类型的 harness
- [[Agentic-Engineering]] — SHIELD 是 agentic engineering 中学习感知设计的实例
