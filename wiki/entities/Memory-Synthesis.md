---
type: entity
title: Memory Synthesis
aliases:
  - Memory Synthesis
  - 记忆合成
  - 记忆综合
  - Background Memory Curation
definition: "LLM 应用中后台持续运行的记忆综合过程——从多会话、多时间点的聊天历史中自动提取、合成、更新用户记忆状态；OpenAI Dreaming 是代表实现"
created: 2026-06-06
updated: 2026-06-06
tags:
  - memory-system
  - context-engineering
  - openai
related_entities:
  - "[[Dreaming]]"
  - "[[Memory-Architecture]]"
  - "[[Staleness-Problem]]"
  - "[[Memory-Summary-Page]]"
  - "[[Multi-Layer-Memory]]"
  - "[[OpenAI]]"
  - "[[Personal-AI-Assistant]]"
source_raw:
  - "[[20260604-openai-dreaming-memory]]"
---

# Memory Synthesis（记忆合成）

> [!definition] 定义
> **Memory Synthesis** 是 LLM 应用中后台持续运行的记忆综合过程——从多会话、多时间点的聊天历史中自动提取、合成、更新用户记忆状态。OpenAI Dreaming（2025-04 V0，2026-06 V3）是代表实现。区别于"显式记忆写入"（用户说"记住 X"），memory synthesis 是系统驱动的持续行为。

## 与显式记忆的对比

| 维度 | 显式记忆（saved memories） | Memory Synthesis（Dreaming） |
|------|------------------------------|------------------------------|
| 触发 | 用户说"记住 X" | 后台持续运行 |
| 范围 | 用户提到的事实 | 聊天历史自动综合 |
| 时间感知 | 无 | 自动时间戳 + 更新 |
| 用户成本 | 高（要主动说） | 低（自动） |
| 算力成本 | 低 | 持续（商业模式挑战） |

## 形式化

```
memory_synthesis(t+1) = f(聊天历史[t0..t], 旧 memory state, 时间)
memory_state 持续 = ∫ memory_synthesis(τ) dτ
```

## 三大子过程

| 子过程 | 含义 | Dreaming V3 实现 |
|--------|------|------------------|
| 提取 | 从聊天中识别值得记的内容 | LLM-as-judge |
| 合成 | 整合多条相关内容 | 多信号融合 |
| 更新 | 修改过期记忆 | 时间感知 + staleness 检测 |

## 关键设计模式

- **后台运行** — 用户不在时持续处理
- **时间感知** — 记忆带时间戳、自动改写
- **去重** — 相同信号不重复记
- **冲突解决** — 新旧信息冲突时取舍
- **隐私过滤** — 不记敏感内容

## 前提与局限性
- **持续 compute cost** — 后台进程算力开销
- **sycophancy 风险** — 用户修改 = 标注员
- **summary 失真** — 综合结果有信息损失
- **跨设备同步** — 多端使用时 memory 状态合并

## 关联概念
| 本库主题 | Memory Synthesis 的连接 |
|---------|----------------------|
| [[Dreaming]] | OpenAI 代表实现 |
| [[Memory-Architecture]] | 核心组件 |
| [[Staleness-Problem]] | 试图解决的核心问题 |
| [[Memory-Summary-Page]] | 综合结果的用户界面 |
| [[Multi-Layer-Memory]] | 与分层记忆是不同维度的解 |
| [[OpenAI]] | 系统化提出 |
| [[Personal-AI-Assistant]] | 持续助理的核心能力 |

- [[OpenAI]] — 在 Dreaming V3 文档中系统化提出

## 关键数据点

（关键事实、统计、时间线从原 raw 源沉淀，见 source_raw 字段）

