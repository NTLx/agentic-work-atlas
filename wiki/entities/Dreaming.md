---
type: entity
title: Dreaming
aliases:
  - Dreaming
  - Dreaming V0
  - Dreaming V3
  - ChatGPT Dreaming
  - 后台记忆整理
definition: "OpenAI ChatGPT 2025-04 推出、2026-06 升级为 V3 的后台记忆整理机制——从聊天历史中自动合成用户记忆状态，对应人脑睡眠期的记忆巩固"
created: 2026-06-06
updated: 2026-06-16
evidence_level: medium
claim_type: mixed
tags:
  - memory-system
  - context-engineering
  - openai
  - personal-ai-assistant
related_entities:
  - "[[OpenAI]]"
  - "[[Memory-Architecture]]"
  - "[[Memory-Synthesis]]"
  - "[[Memory-Summary-Page]]"
  - "[[Staleness-Problem]]"
  - "[[Context-Engineering]]"
  - "[[Multi-Layer-Memory]]"
  - "[[Three-Layer-Agent-Memory]]"
  - "[[Personal-AI-Assistant]]"
  - "[[Memex]]"
source_raw:
  - "[[20260604-openai-dreaming-memory]]"
---

# Dreaming（ChatGPT 后台记忆整理）

> [!definition] 定义
> **Dreaming** 是 OpenAI ChatGPT 在 2025-04 推出、2026-06 升级为 V3 的后台记忆整理机制——从聊天历史中自动合成用户记忆状态，对应人脑睡眠期的记忆巩固。V3 是 compute-efficient 的独立可扩展架构，能跑在亿级用户 × 多年时间窗口。

## 演化时间表

| 时间 | 阶段 | 特征 |
|------|------|------|
| 2024-04 | Saved memories | 用户显式说"记住 X"才存 |
| 2025-04 | Dreaming V0 | 后台从聊天历史自动整理；补充 saved memories |
| 2025-06 | Memory improvements | 短期连续性 rollout 到 free users |
| 2026-06 | Dreaming V3 | 独立可扩展系统，可替代 saved memories |

## 三大设计目标

| 目标 | 含义 | V3 解法 |
|------|------|---------|
| 携带上下文 | "告诉我一次，未来记得" | 跨会话检索 |
| 跟随偏好/约束 | "我是素食者"→ 未来回答考虑 | 偏好识别 + 应用 |
| 保持时新 | "我 7 月去新加坡" → 8 月变成"我 7 月去了" | 时间感知 + 自动更新 |

## 与 saved memories 的关键差异

| 维度 | Saved memories (2024) | Dreaming V3 (2026) |
|------|------------------------|---------------------|
| 触发 | 用户显式说"记住" | 后台持续运行 |
| 范围 | 显式 mention 的事实 | 聊天历史自动综合 |
| 失效 | 容易 stale | 自动时间感知 + 更新 |
| 评审 | 难（要主动看） | Memory summary page 暴露 |
| 算力 | 偶发 | 持续 compute cost |

## 形式化

```
旧: 记忆 = 标注事件（用户驱动，偶发）
新: 记忆 = 后台进程（系统驱动，持续）
dreaming = 后台整理 + 时间感知 + 跨会话综合 + 用户可审可改
```

## 前提与局限性
- **持续 compute cost** — 用户不在时也在跑 GPU；商业模式必须覆盖
- **staleness 难解** — 时间对偏好的改变不是函数式可预测的；只能缓冲
- **summary 失真** — 当记忆量巨大，summary page 仍要降维
- **数据归属** — 记忆属用户数据，监管风险陡增
- **训练回授** — 用户修改 = 标注员行为

## 关联概念
| 本库主题 | Dreaming 的连接 |
|---------|---------------|
| [[Context-Engineering]] | 持续记忆是 context engineering 的核心场景 |
| [[Multi-Layer-Memory]] | 平行概念：Three-Layer Agent Memory（[[Three-Layer-Agent-Memory]]） |
| [[Agent-Harness]] | Dreaming 是个人 AI 助理的 harness 组件 |
| [[Memex]] | 个人数据主权的历史范式 |
| [[Continual-Learning]] | 持续学习的应用案例 |
| [[Personal-AI-Assistant]] | 是个人 AI 助理的标志能力 |
| [[Staleness-Problem]] | Dreaming 试图解决的核心难题 |
| [[Memory-Architecture]] | Dreaming 是 V3 架构的具体实现 |

- [[OpenAI]] — 开发与运营方

## 关键数据点

（关键事实、统计、时间线从原 raw 源沉淀，见 source_raw 字段）

