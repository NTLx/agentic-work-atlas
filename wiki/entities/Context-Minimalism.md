---
type: entity
title: Context Minimalism
aliases:
  - 上下文极简主义
  - Context Minimalist
definition: "Boris Cherny 提出的按需拉取上下文设计偏好：提供充分任务约束及工具，让模型选择获取补充信息；它是 Context Engineering 的候选策略，不是其必然替代阶段。"
created: 2026-06-12
updated: 2026-11-28
evidence_level: medium
claim_type: mixed
tags:
  - agentic-engineering
  - context-engineering
  - claude-code
related_entities:
  - "[[Claude-Code-CLI]]"
  - "[[Agent-Verification]]"
  - "[[Agent-Harness]]"
source_raw:
  - "[[20260608-reflecting-on-year-of-claude-code]]"
---

> [!definition] 定义
> Context Minimalism 是一种 agent 设计哲学：只告诉模型它需要知道的最小信息，让模型自己决定如何获取更多上下文。减少不必要的预填充上下文可能降低干扰，但必须保留关键目标、证据、约束与权限；按需读取也需要可达性和检查。

## 关键数据点

- 历史访谈中 Boris 按 Sonnet 3.5、Opus 4 和当时模型说明个人工作方式变化；并非跨模型对照或所有任务的最优上下文策略。
- 核心原则: "tell the model only what it needs to know and let it figure out the rest"
- 实践: Claude Code 的 harness 越来越 lean，给用户更多空间放自己的 prompt
- 关键前提: 模型需要有"拉取上下文的方式"（工具、文件系统、API 等）

## 前提与局限性

- **依赖模型推理能力**: 如果模型推理能力不足，过少 context 可能导致幻觉或错误决策
- **"minimal" 边界模糊**: 什么是最小必要信息没有明确标准，依赖开发者判断
- **Claude 特定建议**: 这是 Claude Code 团队基于 Claude 模型能力的建议，不一定适用于所有模型
- **需要工具支撑**: 模型必须有拉取上下文的工具（文件读取、搜索等），否则 minimal = 无知

## 关联概念

- [[Claude-Code-CLI]] — Context minimalism 的实践载体
- [[Agent-Harness]] — 精简 Harness 可与按需检索组合，但运行控制与权限检查不应因精简而移除
- [[Agent-Verification]] — 按需取证可以辅助验证，证据充分性和独立判定仍需另验
