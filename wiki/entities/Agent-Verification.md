---
type: entity
title: Agent Verification
aliases:
  - Agent 自主验证
  - Agentic Verification
definition: "Agent 能自主运行验证循环的能力——不是 lint/type check，而是 agent 能自己启动测试环境、执行操作、观察结果并判断是否通过"
created: 2026-06-12
updated: 2026-06-22
evidence_level: medium
claim_type: mixed
tags:
  - agentic-engineering
  - verification
  - claude-code
related_entities:
  - "[[Claude-Code-CLI]]"
  - "[[Agent-Loops]]"
  - "[[Auto-Mode]]"
  - "[[Validation-Pipeline]]"
  - "[[Captain-Mindset]]"
source_raw:
  - "[[20260608-reflecting-on-year-of-claude-code]]"
  - "[[20260620-l8-principal-agentic-workflow]]"
---

> [!definition] 定义
> Agent 验证不是传统意义上的自动化测试（lint、type check、unit test），而是 agent 能**自主运行验证循环**——自己启动测试环境、执行操作、观察结果、判断是否通过，并在失败时自行修复。

## 关键数据点

- Claude Code 的 verification 路径: agent 打开 CLI → 测试自己写的 feature → 观察结果 → 修复
- Desktop development skill: Claude 启动本地 desktop app → 用 computer use 点击测试 UX → 测试 edge cases → 修复并重新检查
- 验证循环示例: iOS simulator / Android simulator / desktop computer use
- 从 Opus 4 开始实现 self-testing，到今天已成常态

## 前提与局限性

- **依赖工具使用能力**: Agent 必须能访问运行环境（terminal、simulator、browser），无法访问时 verification 仍然是外部的
- **内部案例为主**: 当前最佳实践来自 Anthropic 内部，外部企业是否同样适用存疑
- **需要 skill 支撑**: 复杂验证（如 desktop app 测试）需要专门的 skill 教 agent 如何操作

## 关联概念

- [[Claude-Code-CLI]] — Agent verification 的主要载体
- [[Agent-Loops]] — Verification 是 loop 的核心环节
- [[Auto-Mode]] — Auto mode 让 verification 循环可以无人值守运行
- [[Validation-Pipeline]] — 系统化验证管线：对抗审查 + e2e 测试 + 证据生成 + PR babysitting
- [[Captain-Mindset]] — 验证能力的组织意义：人类从审 diff 转向看证据
