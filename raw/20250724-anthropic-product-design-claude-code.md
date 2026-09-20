---
type: raw
title: "How Anthropic teams use Claude Code — Product Design"
source: "https://claude.com/blog/how-anthropic-teams-use-claude-code"
author:
  - "Anthropic"
published: "2025-07-24"
created: "2026-09-19"
description: "Anthropic 官方内部团队案例：Product Design team 将 Claude Code 用于直接前端实现、state-management 修改、交互原型、error/logic/status 枚举与跨法务文案变更；自报 2–3x execution speed 与部分 coordination cycle 从周级缩到小时级。"
tags:
  - clippings
  - design
  - ai-era
---

# How Anthropic teams use Claude Code — Product Design

> Canonical source: https://claude.com/blog/how-anthropic-teams-use-claude-code
> Published: 2025-07-24.

## Source locator

Anthropic's official internal-team case study includes a Product Design section covering designers who support Claude Code, Claude.ai and the Anthropic API.

Reported workflow changes include:

- designers directly implementing front-end polish rather than only handing off static specifications;
- designers making larger state-management changes that would traditionally be engineering work;
- turning mockups into functional interactive prototypes that engineers can immediately iterate on;
- mapping error states, logic flows and system statuses during design to surface edge cases earlier;
- using codebase-wide search/change workflows for product-copy and legal-compliance coordination;
- keeping Figma and Claude Code open together for much of the working day.

Reported internal impact includes:

- roughly 2–3x faster execution for visual/state-management changes;
- some coordination workflows moving from roughly a week to two short calls / hours;
- increased designer understanding of system constraints and implementation details.

## Evidence boundary

This is Anthropic's own case study based on interviews with internal power users. The performance figures are self-reported and not independently audited. It supports workflow expansion from static artifacts toward executable prototypes, code and system-state reasoning, but does not establish that every designer should code, that quality improved proportionally to speed, or that design owns model behavior / launch authority.
