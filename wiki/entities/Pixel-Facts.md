---
type: entity
title: Pixel Facts
aliases:
  - 像素事实
definition: "从指定设备、视口及界面状态提取元素边界框，将可观察几何关系转为 Agent 可用且可测试的布局约束；不等同完整视觉真值或跨端不变坐标。"
created: 2026-06-10
updated: 2026-11-28
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
> **Pixel Facts** 是 Qwen 案例中从真机界面 dump 提取 bounds，再用程序推导布局约束的做法。坐标是特定观测条件下的几何记录，而非无条件真实、无损的完整 UI 规格；布局规则本身仍是推断。

## 关键数据点
- **核心机制**：原文 `ui_summary.txt` 中的 bounds 推导网格、宽高比、通栏卡片（宽度≥90%屏宽）等案例约束；容器类型及图标实现方式仍为规则推断。
- **案例结果**：作者报告移动端、Web 端各约4个多小时，输入约15万字调研材料、12个关键页面，隔离环境和种子数据，声称主要界面及交互近似还原。没有像素级误差、独立验收、等任务量对照或单独移除 bounds 的消融；不能把全部效果归因于坐标。

## 前提与局限性
- **前提**：标明设备、视口、缩放/密度、滚动状态、组件状态和坐标空间；独立检查 dump 的覆盖与映射。未指定的像素不能自动当作全局常量。
- **局限**：绝对坐标不宜直接套到不同屏幕与响应式布局；层叠、裁剪、交互可达性、颜色、字体、无障碍和视觉一致性需另验。
- **可证伪验证建议（综合）**：同一模型/任务/预算下比较文字、bounds、混合输入，报告几何误差、不同视口的布局失败、功能正确性与重试成本。当前仅有单一案例，保留 Strengthen，不制造第二来源。

## 关联概念
- [[Constraint-Driven-Engineering]]
- [[Context-Engineering]]
- [[Automated-Criteria]]
