---
type: entity
title: Friction as Design Signal
aliases:
  - Friction as Design Signal
  - 摩擦作为设计信号
definition: "把开发中的困难、停顿和理解阻力视为架构、学习和边界选择的反馈，而不是一律需要被自动化消除的浪费。"
created: 2026-05-22
updated: 2026-05-22
tags:
  - Software-Engineering
  - AI-Agent
  - human-skill
related_entities:
  - "[[Essential-Complexity]]"
  - "[[Ownership]]"
  - "[[Judgment]]"
  - "[[Agentic-Engineering]]"
  - "[[Technical-Debt-Avoidance]]"
source_raw:
  - "[[Why I Don’t Vibe Code]]"
---

# Friction as Design Signal（摩擦作为设计信号）

> [!definition] 定义
> Friction as Design Signal 是一种工程判断：开发中的困难、停顿和理解阻力不一定是浪费，它们可能是在提示架构、抽象、数据模型或团队协作方式有问题。

## 为什么 AI 时代更重要

Vibe Coding 的吸引力在于消除摩擦：更快生成代码、更快看到产品、更少手动查资料。Harris 的反向提醒是，摩擦本身常常携带信息。

当开发者逐行阅读陌生代码、写 ADR、暂停实现、出门散步、重新审视架构时，他们不是低效，而是在让系统的真实约束浮上来。LLM 可以帮助执行，但如果它直接把所有阻力都“编码穿过去”，团队可能错过更早的设计信号，最后留下只有 prompt 历史、没有设计理由的系统。

## 关键数据点

- 作者把 close reading 视为理解代码选择、语言惯用法和约束来源的必要过程。
- 当写代码变难时，作者把它当作当前架构路径可能错误的信号，而不是单纯的生产力问题。
- 作者用 ADR 固化当下假设、设计理由和后果，以便未来团队能重建“当时为什么这么做”。

## 前提与局限性

- **前提**: 摩擦来自真实复杂性，而不是文档缺失、工具损坏或重复劳动。
- **前提**: 团队愿意把停顿视为理解系统的机会，而不是只用速度衡量工程价值。
- **局限**: 低价值摩擦仍应被工具消除，例如机械查参数、重复格式转换、可完全自动验证的小改动。
- **局限**: 摩擦不能被浪漫化；没有验证、没有记录、没有设计产出的停顿也可能只是拖延。

## 关联概念

- [[Essential-Complexity]] — 摩擦经常是本质复杂性显形的方式。
- [[Ownership]] — 愿意面对摩擦，是对系统后果负责的一部分。
- [[Judgment]] — 判断哪些摩擦该消除、哪些摩擦该保留。
- [[Agentic-Engineering]] — 好的 Agentic Engineering 应保留关键设计反馈，而不是只追求生成速度。
- [[Technical-Debt-Avoidance]] — 提前识别摩擦可避免把结构问题沉淀为技术债。
