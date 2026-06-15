---
type: entity
title: Role Merging
aliases:
  - 角色融合
  - 角色边界模糊
definition: "AI 让 PM/设计师/财务等非工程角色也能写代码，同时让工程师端到端交付产品；'谁写代码'不再重要，'谁有产品判断力'更重要"
created: 2026-06-12
updated: 2026-06-16
evidence_level: medium
claim_type: mixed
tags:
  - agentic-engineering
  - organization
  - claude-code
related_entities:
  - "[[Claude-Code-CLI]]"
  - "[[Agent-Loops]]"
  - "[[Knowledge-Work]]"
source_raw:
  - "[[20260608-reflecting-on-year-of-claude-code]]"
---

> [!definition] 定义
> 角色融合是 AI 时代组织结构的变化趋势：PM、设计师、财务、数据科学等非工程角色开始使用 AI 编程工具直接写代码，同时工程师开始端到端交付产品（从想法到法律/营销）。

## 关键数据点

- Anthropic 内部案例: 设计师提 PR、PM 改代码、财务团队用 Claude Code 做预测、数据科学家全员使用
- 企业观察: "工程师先 adopt → 相邻角色看一眼 → 也开始用"
- 设计师效率: "making prototypes and making changes directly in the app instead of paying an engineer"
- 工程师转变: "ship products end to end"——从想法到构建到法律/安全/营销
- Boris 的判断: "AI really benefits people who have a lot of curiosity, have a lot of product taste"

## 前提与局限性

- **选择性偏差**: Anthropic 招的人本来就技术素养高，不代表所有公司的设计师都能提 PR
- **工具依赖**: 需要 AI 编程工具足够易用，非工程角色才能上手
- **质量控制**: 角色融合后代码质量如何保证？是否需要新的 review 机制？
- **组织文化**: 传统组织可能抵制这种角色边界模糊

## 关联概念

- [[Claude-Code-CLI]] — 角色融合的工具载体
- [[Knowledge-Work]] — AI 如何改变知识工作的定义
- [[Agent-Loops]] — Agent 让非工程角色也能驱动开发流程
