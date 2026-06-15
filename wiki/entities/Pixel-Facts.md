---
type: entity
title: Pixel Facts
aliases:
  - 像素事实
definition: "在 UI 自动化还原任务中，通过从真机界面 dump 出的元素精确边界框（Bounds）作为不可违反的几何事实注入 Agent，以替代有损文字描述的上下文工程技术。"
created: 2026-06-10
updated: 2026-06-16
evidence_level: medium
claim_type: mixed
tags:
  - context-engineering
  - automation
related_entities:
  - "[[Constraint-Driven-Engineering]]"
  - "[[Context-Engineering]]"
source_raw:
  - "[[20260610-qwen-constraint-driven-engineering-experiment]]"
---

# Pixel Facts（像素事实）

> [!definition] 定义
> **Pixel Facts** 是一种高分辨率的上下文注入技术。它主张：对于布局这类强几何任务，Agent 需要的是确定性的坐标数据，而非“首页有两个卡片”这类高度模糊的文字描述。

## 关键数据点
- **核心机制**: 将 `bounds="[左,上][右,下]"` 自动计算为容器类型、行列数等硬规则。
- **实验表现**: 使无视觉能力的 Qwen3.7-Max 在 4 小时内精准复刻了双端应用的界面布局。

## 前提与局限性
- **前提**: 必须能够从现有 App 或设计稿原型中提取精确的几何 dump 文件。
- **局限**: 仅限于布局还原，无法直接解决非几何的审美要素（如氛围、光影）。

## 关联概念
- [[Constraint-Driven-Engineering]]
- [[Context-Engineering]]
- [[Automated-Criteria]]
