---
type: entity
title: Context Rot
aliases:
  - 上下文腐烂
  - context rot
definition: "随着上下文窗口逐渐填充，LLM 的推理、指令遵循和任务完成能力逐渐下降的现象，特别是关键信号落在窗口中间位置时表现最差。"
created: 2026-06-10
updated: 2026-06-16
evidence_level: medium
claim_type: mixed
tags:
  - LLM
  - context-engineering
related_entities:
  - "[[Agent-Harness]]"
  - "[[Context-Engineering]]"
  - "[[Token-Efficiency]]"
source_raw:
  - "[[20260419-agent-harness-engineering]]"
  - "[[The Anatomy of an Agent Harness]]"
  - "[[20260702-anthropic-context-engineering]]"
---

# Context Rot（上下文腐烂）

> [!definition] 定义
> **Context Rot** 指的是随着上下文窗口（Context Window）的填充，模型对信息的处理质量非线性下降的现象。这种现象不仅受 Token 总量影响，还受信息分布位置的影响（如 "Lost in the Middle" 效应）。

## 关键数据点
- 关键内容落在窗口中间位置时，模型性能可能下降 30% 以上（Stanford 研究）。

## 前提与局限性
- 随着模型架构改进（如线性注意力、更强的长文本模型），腐烂的速度可能变慢，但目前仍是生产级 Agent 的核心瓶颈。

## 关联概念
- [[Agent-Harness]]
- [[Context-Engineering]]
- [[Agentic-Workflow-Token-Efficiency]]
- [[Ralph-Loops]]
