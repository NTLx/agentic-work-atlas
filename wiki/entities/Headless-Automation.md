---
type: entity
title: Headless-Automation
aliases:
  - 无头自动化
definition: "通过编程方式访问AI代理能力，无需图形用户界面的自动化模式"
created: 2026-06-30
updated: 2026-11-28
evidence_level: medium
claim_type: mixed
tags:
  - automation
  - sdk
related_entities:
  - "[[Claude-Code-CLI]]"
  - "[[SDK-Design]]"
source_raw:
  - "[[20260630-building-headless-automation-claude-code]]"
---

# Headless-Automation

## 定义

通过编程方式访问AI代理能力，无需图形用户界面的自动化模式。允许将AI代理集成到命令行管道、CI/CD流程和自定义应用中。

## 关键数据点

- Code w/ Claude 演示使用 `claude -p` 进行 headless 调用，可通过管道组合输入输出
- 支持JSON结构化输出，便于程序解析
- 可集成到GitHub Actions等CI/CD平台

## 前提与局限性

- 当前直接证据来自 Claude Code 的单一官方演示；“Headless Automation”作为跨产品通用模式是本库抽象，不能把 Claude Code 的具体参数或能力直接外推到其他 Agent runtime。
- 需要开发者理解命令行和编程概念。
- 非交互不等于无权限确认或安全隔离；工具暴露、免确认规则、拒绝规则、身份、进程权限及外部验收是不同层面。Claude Code 具体语义见 [[Headless-Mode]]。
- 输出解析需要额外开发工作。

## 关联概念

- [[Claude-Code-CLI]]：无头自动化的命令行接口
- [[Headless-Mode]]：Claude Code 具体 CLI 实现与当前参数边界
- [[SDK-Design]]：SDK 集成接口的案例，与非交互执行方式不同