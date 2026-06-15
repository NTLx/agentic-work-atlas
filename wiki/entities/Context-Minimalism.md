---
type: entity
title: Context Minimalism
aliases:
  - 上下文极简主义
  - Context Minimalist
definition: "给 agent 最小可能的 system prompt 和工具集，让模型自己决定如何拉取上下文；与 context engineering 的演进关系类似 prompt engineering → context engineering → context minimalism"
created: 2026-06-12
updated: 2026-06-16
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
> Context Minimalism 是一种 agent 设计哲学：只告诉模型它需要知道的最小信息，让模型自己决定如何获取更多上下文。给太多 context 等于微管理。

## 关键数据点

- 演进路径: Sonnet 3.5 时代需要 prompt engineering → Opus 4 时代需要 context engineering → 今天的模型只需要最小 prompt + 工具
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
- [[Agent-Harness]] — Harness 的 lean 化是 context minimalism 的体现
- [[Agent-Verification]] — 验证循环需要 agent 自主拉取上下文
