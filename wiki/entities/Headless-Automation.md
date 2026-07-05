---
type: entity
title: Headless-Automation
aliases:
  - 无头自动化
definition: "通过编程方式访问AI代理能力，无需图形用户界面的自动化模式"
created: 2026-06-30
updated: 2026-06-30
tags:
  - automation
  - sdk
related_entities:
  - "[[Claude-Code-CLI]]"
  - "[[SDK-Design]]"
source_raw:
  - "[[20260630-building-headless-automation-claude-code]]"
  - "[[Building headless automation with Claude Code — Code w Claude]]"
---

# Headless-Automation

## 定义

通过编程方式访问AI代理能力，无需图形用户界面的自动化模式。允许将AI代理集成到命令行管道、CI/CD流程和自定义应用中。

## 关键数据点

- Claude Code SDK支持`claude -b`命令行调用，可管道输入输出
- 支持JSON结构化输出，便于程序解析
- 可集成到GitHub Actions等CI/CD平台

## 前提与局限性

- 需要开发者理解命令行和编程概念
- 权限管理需要仔细配置，避免安全风险
- 输出解析需要额外开发工作

## 关联概念

- [[Claude-Code-CLI]]：无头自动化的命令行接口
- [[SDK-Design]]：软件开发工具包设计模式