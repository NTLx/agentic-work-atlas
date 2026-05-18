---
type: entity
title: World Model
aliases:
  - World Model
  - 世界模型
definition: "AI 系统对环境状态、因果关系和未来变化的内部表示，使 Agent 能在持续学习中预测行动后果并调整策略"
created: 2026-05-18
updated: 2026-05-18
tags:
  - AI
  - AGI
  - cognitive-architecture
related_entities:
  - "[[Continual-Learning]]"
  - "[[Tool-Use-Architecture]]"
  - "[[Scientific-Discovery-AI]]"
source_raw:
  - "[[Demis Hassabis: Agents, AGI & The Next Big Scientific Breakthrough]]"
---

# World Model

> [!definition] 定义
> **World Model** 是 AI 系统对外部环境、状态转移和因果结构的内部表示。它让 Agent 不只是响应当前输入，而是能预测行动后果、整合新经验，并在长期任务中保持一致策略。

## 关键数据点

- 在 Demis Hassabis 的 AGI 讨论中，世界模型与 [[Continual-Learning|持续学习]] 共同构成当前系统的关键缺口。
- 只扩大上下文窗口不能等同于世界模型；上下文是存储，世界模型是可更新、可预测的内部结构。
- 对科学发现类 Agent 而言，世界模型需要连接实验结果、假设空间和工具调用结果。

## 前提与局限性

- 世界模型的质量依赖高质量反馈和可验证环境；仅靠静态文本很难学到可靠因果结构。
- 过强的内部模型可能固化错误假设，需要外部工具和实验数据持续校正。
- 在开放世界任务中，世界模型通常只能是局部、可修正的近似。

## 关联概念

- [[Continual-Learning]] — 世界模型需要通过持续学习更新。
- [[Tool-Use-Architecture]] — 工具调用为世界模型提供外部观测和校验。
- [[Scientific-Discovery-AI]] — 科学发现场景需要模型理解实验和理论之间的状态转移。
