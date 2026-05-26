---
type: entity
title: Accessibility-High-Risk-Patterns
aliases:
  - Accessibility High Risk Patterns
  - 无障碍高风险模式
definition: "无障碍 Agent 默认不应自动修改的复杂交互模式清单"
created: 2026-05-18
updated: 2026-05-25
tags:
  - accessibility
  - AI-Agent
  - anti-patterns
related_entities:
  - "[[Accessibility-Agent]]"
  - "[[Accessibility-Complexity-Evaluation]]"
  - "[[Verifiable-Agent-Engineering]]"
  - "[[Bias-to-Action-LLM]]"
  - "[[WCAG]]"
source_raw:
  - "[[Building a general-purpose accessibility agent—and what we learned in the process]]"
---

# Accessibility-High-Risk-Patterns

> [!definition] 定义
> **无障碍高风险模式** 是那些即使通过自动化无障碍检测，实际使用中仍可能无法被辅助技术正常使用的交互模式。GitHub 的无障碍 Agent 被明确禁止为这些模式生成代码，包括：拖放（drag and drop）、Toast 通知、富文本编辑器（rich text editors）、树形视图（tree views）和数据网格（data grids）。

## 已知高风险模式清单

| 模式 | 风险原因 |
|------|---------|
| 拖放 | 需要同时支持鼠标、键盘和触摸操作，状态反馈复杂 |
| Toast 通知 | 需要在不干扰当前任务的前提下让用户感知重要通知 |
| 富文本编辑器 | 涉及复杂的键盘快捷键和屏幕阅读器交互 |
| 树形视图 | 层级展开/折叠与屏幕阅读器阅读顺序的协调困难 |
| 数据网格 | 大量单元格需要支持排序、选择和键盘导航 |

## 为什么代码检测通过但实际不可用

一个微妙但关键的认识：**代码通过自动无障碍检测 ≠ 功能上可用**。自动检测器验证的是代码层面的合规性（如 ARIA 属性是否存在），但无法验证实际辅助技术使用体验。

## 关键数据点

- 这些模式需要大量专注和细致工作，当前超出 LLM 的生成能力
- 禁止 Agent 碰高风险模式避免了不必要的时间浪费和可访问性团队声誉风险
- 该清单是 explicit exclusion list：命中后不是“更谨慎地生成”，而是退出自动修复路径
- 高风险判断来自无障碍团队经验，而不是让模型自行推断

## 工程含义

高风险模式的价值在于承认“可访问性不是局部补丁”。拖放、Toast、富文本、树形视图、数据网格这类模式通常需要同时满足：

- 键盘路径完整。
- 焦点移动可预测。
- 状态变化能被辅助技术感知。
- 屏幕阅读器阅读顺序和视觉结构一致。
- 错误、选择、排序、展开和通知都有清楚语义。

这些要求很难由一次代码生成保证。即使自动检查器没有报错，也可能只是说明 ARIA 属性存在，而不是说明真实用户能完成任务。

## 与 Agent 行动偏差的关系

LLM 往往会把“用户要求修复”理解为“必须生成补丁”。在无障碍场景，这种行动偏差会制造额外风险：一个看似合理的改动可能让辅助技术体验更糟，还让后续人工审查成本上升。

因此高风险模式清单是一种拒绝机制。它把“不要碰这些模式”写进 harness，而不是期待模型每次都能自觉克制。

## 前提与局限性

- 清单基于当前（2026 年）无障碍团队的经验判断，会随着技术进步和 LLM 能力提升而变化
- "高风险"判断本身依赖人工经验，Agent 自己无法可靠判断某个模式是否高风险
- 不在清单上的模式不自动等于"安全"——清单是已知的，不是全部的
- 清单不能替代真实用户测试，也不能替代无障碍专家对设计阶段的介入
- 如果长期不回放失败案例，清单会滞后于组件库和前端框架变化

## 关联概念

- [[Accessibility-Agent]] — 高风险模式是无障碍 Agent 的核心约束条件
- [[Accessibility-Complexity-Evaluation]] — 与复杂度评估配合，形成两层保护
- [[Verifiable-Agent-Engineering]] — 高风险模式清单是行为验证和拒绝机制
- [[Bias-to-Action-LLM]] — 清单对抗模型默认动手倾向
- [[WCAG]] — 自动通过 WCAG 检查不等于高风险交互真实可用
