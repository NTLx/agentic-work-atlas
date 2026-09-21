---
type: entity
title: SDK-Design
aliases:
  - 软件开发工具包设计
definition: "为开发者提供编程接口和工具集，以便将AI能力集成到自有应用中的设计模式"
created: 2026-06-30
updated: 2026-06-30
evidence_level: medium
claim_type: mixed
tags:
  - sdk
related_entities:
  - "[[Headless-Automation]]"
  - "[[Claude-Code-CLI]]"
source_raw:
  - "[[20260630-building-headless-automation-claude-code]]"
---

# SDK-Design

## 定义

为开发者提供编程接口和工具集，以便将 AI 能力集成到自有应用中的设计模式。本页的具体能力来自单一 Claude Code SDK 演示，不能当作所有 SDK 的共同规格；示例包括命令行调用、结构化输出、会话管理和权限提示。

## 关键数据点

- Claude Code SDK 演示支持 Python 和 TypeScript 绑定。
- 演示提供结构化输出（JSON 和流式 JSON）模式。
- 演示支持会话状态恢复和权限提示工具；权限范围仍需由集成方配置和审查。

## 前提与局限性

- 需要平衡功能丰富性和使用简洁性
- 权限管理需要细粒度控制
- 跨语言支持需要维护多个绑定

## 关联概念

- [[Headless-Automation]]：无头自动化的实现基础
- [[Claude-Code-CLI]]：SDK的命令行接口实现
