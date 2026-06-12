---
type: entity
title: Auto Mode
aliases:
  - 自动模式
  - Claude Code Auto Mode
definition: "Claude Code 的自动执行模式——agent 自主决定运行工具，无需逐条等待用户确认；通过路由到分类器模型做安全检查，比人类审批更可靠"
created: 2026-06-12
updated: 2026-06-12
tags:
  - claude-code
  - agentic-engineering
  - security
related_entities:
  - "[[Claude-Code-CLI]]"
  - "[[Agent-Verification]]"
  - "[[Agent-Loops]]"
source_raw:
  - "[[20260608-reflecting-on-year-of-claude-code]]"
---

> [!definition] 定义
> Auto Mode 是 Claude Code 的自动执行模式。Agent 运行工具时不再逐条询问用户确认，而是路由到另一个分类器模型做安全检查。可疑操作会被拒绝，用户可以事后允许。

## 关键数据点

- 安全机制: 收集数千条 agent 轨迹 + permission prompt → 训练分类器判断是否安全
- 红队测试: 外部红队尝试 prompt inject / hack codebase → 创建 evals → 确保全部拒绝
- 内部验证: Anthropic 内部团队尝试攻击 auto mode → 持续改进
- 演进: 从 Opus 4 的 plan mode → 4.6/4.7 的 auto mode（新模型不需要 planning step）
- 安全哲学: "auto mode 比人类审批更安全，因为人类会 eyes glaze over"

## 前提与局限性

- **依赖模型对齐**: 需要模型足够 aligned 才能判断安全边界
- **自我评估偏差**: Anthropic 自己训练分类器评估自己的产品，存在 self-serving bias
- **无独立审计**: 红队测试是内部进行的，没有独立第三方验证
- **模型版本依赖**: 不同模型版本（Opus 4 vs 4.7）的 auto mode 行为可能不同

## 关联概念

- [[Claude-Code-CLI]] — Auto mode 是 Claude Code 的核心功能
- [[Agent-Verification]] — Auto mode 让 verification 循环可以无人值守
- [[Agent-Loops]] — Auto mode 是 loop 的基础——agent 可以持续运行而不用等待确认
