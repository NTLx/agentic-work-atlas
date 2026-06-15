---
type: entity
title: Staleness Problem
aliases:
  - Staleness Problem
  - 记忆过时
  - Memory Staleness
definition: "LLM 长期记忆内容随时间过时的核心难题——用户当下事实与记忆里的事实产生偏差，时间对偏好的改变不是函数式可预测的，只能被设计缓冲"
created: 2026-06-06
updated: 2026-06-16
evidence_level: medium
claim_type: mixed
tags:
  - memory-system
  - context-engineering
related_entities:
  - "[[Dreaming]]"
  - "[[Memory-Architecture]]"
  - "[[Memory-Synthesis]]"
  - "[[Memory-Summary-Page]]"
  - "[[Multi-Layer-Memory]]"
  - "[[OpenAI]]"
source_raw:
  - "[[20260604-openai-dreaming-memory]]"
---

# Staleness Problem（记忆过时问题）

> [!definition] 定义
> **Staleness Problem** 是 LLM 长期记忆内容随时间过时的核心难题——用户当下事实与记忆里的事实产生偏差。OpenAI 在 Dreaming V3 文档中列为三大挑战之首。时间对偏好的改变不是函数式可预测的，所以 staleness 不能被数据完全解决，只能被设计缓冲。

## 形式化

```
staleness = 用户当前事实 - 记忆里的事实
时间 → 用户变化 → 记忆偏差
当偏差影响 AI 回答质量时，staleness 触发问题
```

## 典型场景

| 场景 | 旧记忆 | 当前事实 | 触发问题 |
|------|--------|----------|----------|
| 短期事件 | "用户 7 月去新加坡" | 用户已回 | 推荐新加坡景点 |
| 长期偏好 | "用户素食者" | 用户开始吃肉 | 推荐素食餐厅 |
| 职业身份 | "用户是 PM" | 用户转岗 | 给 PM 建议 |
| 居住地 | "用户住北京" | 用户搬家 | 北京天气提醒 |
| 关系状态 | "用户单身" | 用户结婚 | 给单身建议 |

## 解决路径与限制

| 路径 | 限制 |
|------|------|
| 加时间戳 | 变化不是函数式可预测的 |
| 主动询问 | 违反"不打扰"原则 |
| 后台自动更新（Dreaming V3） | 仍需用户确认/纠正 |
| Memory summary page | 用户主动看才有价值 |
| 自动 trust 用户输入 | 易被 sycophancy 操纵 |

## 前提与局限性
- **可预测 vs 不可预测** — 工作变动、搬家、关系变化有信号但难预测；偏好变化（口味、立场）几乎无信号
- **用户主动纠正成本** — 频繁查看 memory summary page 耗费认知带宽，多数用户不会做
- **新信息 vs 旧记忆冲突** — 当新信息与旧记忆冲突，AI 倾向信任哪个？需要明确规则

## 关联概念
| 本库主题 | Staleness Problem 的连接 |
|---------|----------------------|
| [[Dreaming]] | Dreaming V3 试图解决 |
| [[Memory-Architecture]] | 三大挑战之首 |
| [[Multi-Layer-Memory]] | 分层可隔离 staleness 影响 |
| [[Memory-Summary-Page]] | 暴露 staleness 给用户 |
| [[Continual-Learning]] | 持续学习对应 staleness 的模型层 |
| [[OpenAI]] | 在 V3 文档中系统化提出 |

- [[OpenAI]] — 在 Dreaming V3 文档中系统化提出

## 关键数据点

（关键事实、统计、时间线从原 raw 源沉淀，见 source_raw 字段）
