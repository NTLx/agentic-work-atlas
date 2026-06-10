---
type: entity
title: AGENTS.md
aliases:
  - AGENTS-md
definition: "放置在代码库根目录的 Markdown 规范文件，作为 Agent 的“棘轮（Ratchet）”规则手册，记录特定代码库的约束、习惯和过去错误的补丁。"
created: 2026-06-10
updated: 2026-06-10
tags:
  - documentation
  - configuration
related_entities:
  - "[[Agent-Harness]]"
  - "[[CLAUDE-md]]"
  - "[[Harness-Engineering]]"
source_raw:
  - "[[20260419-agent-harness-engineering]]"
---

# AGENTS.md

> [!definition] 定义
> **AGENTS.md** 是 Agentic Engineering 中的一种核心配置文件。它与 `CLAUDE.md` 类似，但更强调作为**针对 Agent 失败的永久补丁集**。

## 关键数据点
- 在 OpenAI Codex 的优先级栈中，`AGENTS.md` 内容通常被级联并拥有极高的 System Prompt 优先级。
- 建议保持在 60 行以内。

## 前提与局限性
- **前提**: Agent 必须有读取文件系统的权限，且 Harness 能够将其内容注入 System Prompt。
- **局限**: 随着规则增加，可能导致 Prompt 竞争模型有限的注意力，加剧上下文腐烂。

## 关联概念
- [[Agent-Harness]]
- [[CLAUDE-md]]
- [[Harness-Engineering]]
- [[Context-Rot]]
