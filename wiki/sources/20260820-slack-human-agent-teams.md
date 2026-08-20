---
type: source-summary
title: "Turning conversation into knowledge: how Slack builds human-agent teams"
source_raw:
  - "[[20260820-slack-human-agent-teams]]"
created: 2026-08-20
updated: 2026-08-20
tags:
  - source-summary
  - anthropic
  - slack
  - human-agent-teams
  - organization
  - knowledge-management
evidence_level: medium
claim_type: mixed
---

# Turning conversation into knowledge: how Slack builds human-agent teams

## 编译摘要

### 1. 浓缩

- **核心结论1**：Slack 的核心命题是"会话即知识库"——过去 workplace conversation 没能自动变成 organizational knowledge 因为人无法消化 exhaust；agent 的出现让会话从 noise 变成 KB，前提是 default to public channels（DMs 和 private threads 对 agent 不可见）
  - 关键证据: Slack 早年研究"conversation doesn't turn into knowledge"——people still have to repeat themselves; Jaime 2026 Medium essay "The Work is the Conversation" 把同一论断延伸到 agent
- **核心结论2**：human-agent 团队的核心节律是 handoff 循环——agent 做 production work（drafting/summarizing/monitoring/preparing），人做 review/decide/redirect；具体表现是周一早上 agent-built briefing、emoji reaction 触发 agent 任务、shared channel 中三方 triage
  - 关键证据: Anthropic + Slack 联合观察的 handoff cycle；具体动作：每日 briefing、escalation flag、meeting prep、web roundup、stale bio rewrite
- **核心结论3**：推广策略是"show-and-tell"——公开演示新工作方式（PM 写 canvas 分享怎么用 Claude、Salesforce "How I Slackbot" 数千成员 channel），让 adoption 自组织传播，而非 mandate
  - 关键证据: Salesforce "How I Slackbot" channel by Jaime's count has thousands of members; Slack 内 PM 推 Claude adoption 是 "most self-organized thing you could possibly imagine"

### 2. 质疑

- **关于"会话即 KB"的隐含前提**：前提是 channel public + 内容高质量；如果 channel 都是 noise（bot 通知、状态消息），agent 仍然消化不了。Slack 自家 channel 的"内容质量治理"未在本文讨论
- **关于 handoff cycle 的效率假设**：人 review → decide → redirect 每步是 synchronous bottleneck；agent 24/7 工作但等 human review 才能继续——cycle 实际 throughput 受 human availability 限制。文中未量化 handoff latency
- **关于 show-and-tell 推广的 selection bias**：Jaime 给的例子都成功（thousands of members，self-organized），未提失败的 attempt。低 quality 内容、噪音、表演性 show-and-tell（[[Slop-Proxy]] 的变种）会让 channel 失去 signal
- **关于"outcomes vs activity"的测量困境**：作者承认 "no dashboard or usage stat will prove it for you"——意味着 AI 价值测量本质上不可量化。这是 structural limitation，不是 Slack 独有的问题
- **关于"psychological safety"驱动的 public-by-default**：这是 Slack 文化前提；在 hierarchical / blame-oriented 组织中，员工不会 open 工作因为怕出错。模式可移植性受限
- **关于"agent as coworker"的隐喻**：agents 是 coworkers（社交比喻）vs agents 是 tools（技术比喻）——隐喻选择影响设计。若 agents 是 tools，metrics 更结构化；若 agents 是 coworkers，metrics 更社交（声誉、信任）。本文偏 coworker 隐喻

### 3. 对标与旁逸

- **跨域关联1**: "default to public channels" 与 [[Claude-Tag]] 的 on-call agent 共构——Claude Tag 在 Slack channel 实时观察 incident 并参与 triage；agent 必须能在 channel 看见才能行动，与本文"agents can only learn from what they can see" 同源
- **跨域关联2**: "shared channel as anchor" 与 [[On-Call-Agent]] 的 multi-player mode 同构——人和 agent 共享 channel、实时 steer、Claude Tag 设计的核心就是这条
- **跨域关联3**: "human-agent handoff cycle" 与 [[Agent-Orchestration]] 同构——human review = human-in-the-loop orchestration; agent 准备 = executor subagent
- **跨域关联4**: "show-and-tell" 与 [[Show-and-Tell-Adoption]]（新建）共构——内部传播机制
- **跨域关联5**: "outcomes not activity" 与 [[Goodharts-Law]] + Activity Metrics vs Outcomes（forward reference，未建 entity） 同源——token 用量、消息数等指标成为目标则失效
- **跨域关联6**: "agent roles" 与 [[Skills-as-Products]] 同源——agent 应有清晰 scope（filing tickets / status update），避免 mandate vs felt value 的张力

## 关联概念

- [[Human-Agent-Teams]]（新建）— 人 + agent 协作的形态总览
- [[Conversation-as-Knowledge-Base]]（新建）— Slack 的核心命题
- [[Show-and-Tell-Adoption]]（新建）— 内部传播机制
- [[Claude-Tag]]（已有，更新 source_raw）— Slack-resident agent 实例
- [[On-Call-Agent]]（已有）— multi-player 模式与本文同构
- [[Agent-Orchestration]]（已有）— handoff cycle 的编排层
- [[Skills-as-Products]]（已有）— agent 角色清晰化与 scope 治理
- [[Goodharts-Law]] — outcomes vs activity 的方法论根
- Activity Metrics vs Outcomes（forward reference，未建 entity） — 具体测量困境
- [[AI-Adoption-Barbell]] — adoption 分布的中间层问题
- [[Slop-Proxy]] — show-and-tell 失败的潜在形态