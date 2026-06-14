---
type: entity
title: Memory Summary Page
aliases:
  - Memory Summary Page
  - 记忆摘要页
  - Memory Dashboard
definition: "LLM 应用中向用户暴露后台合成的记忆内容的可审可改界面；OpenAI Dreaming V3 的标志设计——把 AI 关于用户的状态从黑盒变白盒"
created: 2026-06-06
updated: 2026-06-06
tags:
  - memory-system
  - openai
related_entities:
  - "[[Dreaming]]"
  - "[[Memory-Architecture]]"
  - "[[Memory-Synthesis]]"
  - "[[Staleness-Problem]]"
  - "[[OpenAI]]"
  - "[[Personal-AI-Assistant]]"
source_raw:
  - "[[20260604-openai-dreaming-memory]]"
---

# Memory Summary Page（记忆摘要页）

> [!definition] 定义
> **Memory Summary Page** 是 LLM 应用中向用户暴露后台合成的记忆内容的可审可改界面。OpenAI Dreaming V3 的标志设计——把 AI 关于用户的状态从黑盒变白盒。用户在页面上能：浏览 AI 知道的关于自己的要点、添加/更新信息、设置"什么主题何时该被提到"。

## 形式化

```
信任 = 可观察性 + 可修改性 + 可撤回性
memory summary page = 可观察性 + 可修改性 + 可撤回性的物理实现
```

## 三大能力

| 能力 | 含义 | 用户动作 |
|------|------|----------|
| 可观察性 | 浏览 AI 知道的内容 | 读 summary |
| 可修改性 | 修正错误记忆 | 编辑/添加 |
| 可撤回性 | 删除某条记忆 | 删除 |
| 可指令化 | 设置"什么何时该提" | 配置规则 |

## 关键设计取舍

| 维度 | 风险 | 缓解 |
|------|------|------|
| 摘要失真 | summary 本身有信息损失 | 多层 summary（按主题） |
| 用户疲劳 | 频繁看耗费认知 | 推送关键变化而非全量 |
| 策略性修改 | sycophancy 训练回授 | 标注真实修改 vs 训练修改 |
| 隐私 | 内容暴露给 UI | 本地存储 + 选择性公开 |

## 前提与局限性
- **summary of summary 失真** — 当记忆量巨大（用户 5 年），summary page 仍要降维
- **用户不主动看** — 实际多数用户不会主动查看
- **修改信号 = 训练数据** — 用户修改 = 标注员行为，可能违反知情同意

## 关联概念
| 本库主题 | Memory Summary Page 的连接 |
|---------|------------------------|
| [[Dreaming]] | OpenAI Dreaming V3 标志设计 |
| [[Memory-Architecture]] | 三大组件之一（合成 + 存储 + 暴露） |
| [[Memory-Synthesis]] | 暴露综合结果 |
| [[Staleness-Problem]] | 暴露 staleness 给用户 |
| [[OpenAI]] | 系统化设计 |
| [[Personal-AI-Assistant]] | 助理透明度的核心 |
| [[Memex]] | 个人数据主权的用户界面 |

- [[OpenAI]] — 系统化设计

## 关键数据点

（关键事实、统计、时间线从原 raw 源沉淀，见 source_raw 字段）
