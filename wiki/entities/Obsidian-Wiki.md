---
type: entity
title: Obsidian-Wiki
aliases:
  - Obsidian Wiki
definition: "基于 Skill 的多 Agent 框架，工程化实现 Karpathy 的 LLM Wiki 模式——Agent 无关、Skill 驱动、Obsidian 原生，支持 Agent 历史自动摄入和 Delta 追踪"
created: 2026-05-13
updated: 2026-05-13
tags:
  - knowledge-management
  - AI
  - agent
  - obsidian
related_entities:
  - "[[LLM-Wiki]]"
  - "[[GBrain]]"
  - "[[Progressive-Disclosure]]"
  - "[[Andrej-Karpathy]]"
source_raw:
  - "[[深度解析LLM Wiki  Obsidian-Wiki  GBrain：Agent时代知识的“自组织”与“自进化”]]"
---

# Obsidian-Wiki

> [!definition] 定义
> **Obsidian-Wiki** 是一个基于 Skill 的多 Agent 框架，将 Andrej Karpathy 的 LLM Wiki 理念工程化实现。它支持 9+ 种 Agent（Claude Code、Cursor、Windsurf、Codex、OpenClaw、Hermes 等），所有操作通过标准化的 Markdown Skill 文件定义，利用 Obsidian 的 wikilink、图谱视图、Dataview 等功能。

## 关键数据点

- **Agent 支持**: 9+ 种 Agent，包括 Claude Code、Cursor、Windsurf、Codex、OpenClaw、Hermes、Gemini CLI、Kiro 等
- **Skill 数量**: 定义 20+ 个标准化 Skill，每个是详细的 Markdown 文件
- **Delta 追踪**: 使用 `.manifest.json` + SHA-256 哈希追踪所有来源，分类为 new/modified/touched/unchanged/deleted
- **溯源标记**: 三级置信度——`^[extracted]`（直接提取）、`^[inferred]`（推断）、`^[ambiguous]`（歧义）
- **隐私保护**: `visibility/internal` 和 `visibility/pii` 标签，查询时过滤敏感内容
- **热缓存**: `hot.md` 500 字语义快照，记录最近活动

## 前提与局限性

- 依赖 Obsidian 生态，非 Obsidian 用户无法直接使用核心功能
- Agent History Ingest Skills 仅支持特定 Agent（Claude/Codex/OpenClaw/Hermes），覆盖面有限
- 增量扫描减少重复处理但可能存在边缘情况遗漏
- 知识图谱 Skills（如 cross-linker）需手动触发，非 Always-on

## 关联概念

- [[LLM-Wiki]] — Obsidian-Wiki 是 LLM Wiki 理念的工程化实现
- [[GBrain]] — 并行的 LLM Wiki 工程化方案，侧重混合检索和图谱关系
- [[Progressive-Disclosure]] — 渐进式披露在 Obsidian-Wiki 中的具体实现
- [[Andrej-Karpathy]] — LLM Wiki 概念提出者
- [[Knowledge-Compilation]] — Obsidian-Wiki 的 Ingest 流程本质是知识编译
- [[Memex]] — LLM Wiki 的思想先驱
