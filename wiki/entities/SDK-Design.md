---
type: entity
title: SDK-Design
aliases:
  - 软件开发工具包设计
definition: "为开发者提供编程接口和工具集，以便将AI能力集成到自有应用中的设计模式"
created: 2026-06-30
updated: 2026-06-30
tags:
  - sdk
  - api-design
  - developer-tools
related_entities:
  - "[[Headless-Automation]]"
  - "[[Claude-Code-CLI]]"
source_raw:
  - "[[20260630-building-headless-automation-claude-code]]"
---

# SDK-Design

## 定义

为开发者提供编程接口和工具集，以便将AI能力集成到自有应用中的设计模式。包括命令行工具、结构化输出、会话管理等功能。

## 关键数据点

- Claude Code SDK支持Python和TypeScript绑定
- 提供结构化输出（JSON和流式JSON）模式
- 支持会话状态恢复和权限提示工具

## 前提与局限性

- 需要平衡功能丰富性和使用简洁性
- 权限管理需要细粒度控制
- 跨语言支持需要维护多个绑定

## 关联概念

- [[Headless-Automation]]：无头自动化的实现基础
- [[Claude-Code-CLI]]：SDK的命令行接口实现