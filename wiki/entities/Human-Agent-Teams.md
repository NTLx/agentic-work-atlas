---
type: entity
title: Human Agent Teams
aliases:
  - Human Agent Teams
  - human-agent team
  - Multiplayer AI
  - Human-Agent Collaboration
  - 人机协作团队
definition: "人类 + AI agent 在共享工作环境中循环 handoff 的协作形态——agent 做 production work（drafting/summarizing/monitoring/preparing），人做 review/decide/redirect；核心节律是 handoff loop 而非 one-shot delegation"
created: 2026-08-20
updated: 2026-08-31
tags:
  - organization
  - agentic-engineering
  - workflow
  - human-agent-teams
evidence_level: medium
claim_type: mixed
related_entities:
  - "[[Claude-Tag]]"
  - "[[On-Call-Agent]]"
  - "[[Agent-Orchestration]]"
  - "[[Conversation-as-Knowledge-Base]]"
  - "[[Show-and-Tell-Adoption]]"
  - "[[Skills-as-Products]]"
  - "[[Twilight-Factory]]"
source_raw:
  - "[[20260820-slack-human-agent-teams]]"
  - "[[20260831-agency-and-agents]]"
---

# Human Agent Teams（人机协作团队）

> [!definition] 定义
> **Human Agent Teams** 是 Anthropic + Slack 联合提出的协作形态：人类 + AI agent 在共享工作环境（Slack channel）中循环 handoff——**agent 负责 production work**（drafting、summarizing、monitoring、preparing），**人类负责 review、decide、redirect**。核心节律是 handoff loop 而非 one-shot delegation，是 distributed cognition 的工程化。

## 核心节律

```
Human: 设定目标 / 提供 context
    ↓
Agent: 执行 production work
    ↓
Human: review / decide / redirect
    ↓
Agent: 重做 / 准备下一步
    ↓
循环到目标完成
```

## Twilight Factory：主动式 handoff

[[Twilight-Factory|Twilight Factory]] 把本页的 handoff loop 再向前推进一步：不是只等人类发起任务或审查结果，而是由 facilitator agent 主动判断什么时候需要人类介入。文章列出四类触发点：

| 触发点 | 人类介入的理由 | 人类提供的价值 |
|--------|----------------|----------------|
| **审批** | 行动涉及外部世界、金钱、敏感资料或超出授权 | 授权、拒绝和责任承担 |
| **专业知识** | Agent 缺少领域经验或现场上下文 | 专业事实、约束和经验 |
| **观点方差** | Agent 输出过度收敛，多个方案只是同一答案的变体 | 反例、异质视角和替代路径 |
| **有趣的决策** | 选择本身承载工作意义和判断训练 | 参与方向选择并形成经验 |

这一区分了两个层次：Human Agent Teams 主要定义人和 Agent 如何在共享环境中交接；Twilight Factory 主要定义由谁决定何时交接，以及人类介入不只为了拦截风险，也为了补知识、补多样性和保留判断力。

## 关键实践（Slack + Anthropic 观察）

- **Daily briefing**: 周一早上 agent 准备 briefing（上周 recap、escalation flag、meeting prep、web roundup），人 review
- **Emoji reaction as trigger**: 一个 emoji reaction → list 加入 → agent 自动 pick up task
- **Shared channel as anchor**: 人 + agent 在同一 channel，三方 triage，human lead prioritization
- **Agent roles**: 类比 coworker 给 agent 明确 scope（filing tickets / status update），避免 mandate 而 felt value
- **Public-by-default**: channel 默认 public（除非 sensitive），agent 才能 learn from what they see

## 与相关 concept 的区别

| 形态 | 主导模型 | 适合场景 |
|------|----------|----------|
| Chatbot (1-1) | 人问 → AI 答 | 简单查询 |
| Automation | 预设 trigger → 执行 | 重复任务 |
| **Human-Agent Teams** | **handoff loop + shared context** | **复杂判断 + 持续工作** |
| Agent-only | agent 自治 | 高 confidence 任务 |

## 核心原则

1. **Production work by agents**: drafting、summarizing、monitoring、preparing
2. **Decisions by humans**: review、decide、redirect（"human in the loop" 是真实判断点）
3. **Shared channel as memory**: 人 + agent 共同上下文，不在 agent 黑盒内
4. **Show, don't mandate**: 通过演示让 adoption 自组织传播
5. **Outcomes > activity**: token 用量、消息数不能证明价值

## 关键数据点

- Anthropic + Slack 联合观察（Anthropic 2026-08, Jaime DeLanghe Slack CPO）
- Slack Salesforce "How I Slackbot" channel：thousands of members
- 与 [[On-Call-Agent]] 同构（multi-player mode）
- 与 [[Claude-Tag]] 同构（Slack-resident agent 实例）

## 前提与局限性

- **前提 1**: 组织有公开工作文化（hierarchical/blame culture 不适用）
- **前提 2**: handoff latency < task cycle（否则 throughput 受限）
- **前提 3**: agent 有清晰 scope（避免 mandate 而非 felt value）
- **不适用**: 完全自治任务（无 human review 必要）
- **测量困境**: outcome measurement 本质不可量化（Jaime 承认）
- **心理安全门槛**: public 工作需 employee 信任组织
- **Facilitator 风险**: 主动求助仍依赖 facilitator agent 的判断；如果它漏掉未知的专业知识或把少数视角判为噪声，系统可能把人类引入错误节点。Twilight Factory 目前是设计主张，不是生产验证结果。

## 配套机制

- **[[Claude-Tag]]** 作为 Slack-resident agent 产品实例
- **[[On-Call-Agent]]** 作为 multi-player 模式实例
- **[[Agent-Orchestration]]** 提供 handoff 编排技术底座
- **[[Conversation-as-Knowledge-Base]]** 解释为什么 channel 是知识层
- **[[Show-and-Tell-Adoption]]** 解释 adoption 推广机制
- **[[Skills-as-Products]]** 提供 agent scope 治理框架

## 关联概念

- [[Claude-Tag]] — Slack-resident agent 实例
- [[On-Call-Agent]] — multi-player mode
- [[Agent-Orchestration]] — handoff 编排层
- [[Conversation-as-Knowledge-Base]] — Slack 的核心命题
- [[Show-and-Tell-Adoption]] — adoption 推广机制
- [[Skills-as-Products]] — agent 角色治理
- [[Twilight-Factory]] — 由 facilitator agent 主动路由人类介入的组织设计
- [[Organization-as-Agent-Harness]] — 组织层是 agent harness 的一种
- [[AI-Ready-Organization]] — readiness 前提
