---
type: entity
title: Continual Learning
aliases:
  - Continual Learning
  - 持续学习
  - 连续学习
definition: "让 AI 系统在新情境中吸收经验、更新知识和保持旧能力，而不是每次会话都从静态权重和临时上下文重新开始的能力"
created: 2026-05-08
updated: 2026-05-30
tags:
  - AI
  - AGI
  - machine-learning
related_entities:
  - "[[Demis-Hassabis]]"
  - "[[Jagged-Intelligence]]"
  - "[[World-Model]]"
  - "[[Multi-Layer-Memory]]"
  - "[[Agent-Knowledge-Management]]"
  - "[[Scientific-Discovery-AI]]"
  - "[[Model-Distillation]]"
  - "[[Unified-Model-Strategy]]"
source_raw:
  - "[[Demis Hassabis: Agents, AGI & The Next Big Scientific Breakthrough]]"
  - "[[20260529-gemini-co-leads-origins]]"
---

# Continual Learning（持续学习）

> [!definition] 定义
> **Continual Learning** 是 AI 系统在运行中吸收新经验、整合进已有知识、并保持旧能力的能力。它要解决的不是“能不能记住更多文本”，而是系统能否随着环境变化稳定更新自己，同时避免灾难性遗忘和上下文污染。

## 为什么重要

当前大模型大多是 stateless 的：模型权重不会因为某个项目、某个用户、某个实验失败而自然更新。工程上常见的补丁是把更多内容塞进上下文窗口，或把经验写进外部 memory、wiki、skills、数据库，再在需要时检索。

这些方法能缓解问题，但还不等于持续学习。更长上下文只是更大的工作记忆；它会把重要信息、错误信息、过时信息和噪声一起带入推理。真正困难的是：什么时候该学、学到哪里、如何检索、如何验证、如何忘记，以及新经验是否会破坏旧能力。

## 关键数据点

- Hassabis 把持续学习、长期推理、记忆和一致性列为当前 AGI 路线的关键短板。
- 他用海马体和睡眠回放解释生物智能如何整合经验：大脑在睡眠，尤其是 REM 阶段回放重要情景，把新经验融入已有知识结构。
- DeepMind 的早期 DQN 从神经科学借鉴了 experience replay，通过反复回放成功轨迹来学习 Atari 策略。
- 单纯扩大上下文窗口不足以解决问题。实时视频会迅速消耗百万 token；更大的问题是检索相关经验的成本，而不是能不能存下所有内容。
- **架构有机性缺失**（Koray Kavukcuoglu, 2026-05）：当前模型架构（如 MoE 专家混合）结构过于统一——"lots of experts, they're all very similar structure"。Koray 认为需要"更有机的（organic）"、更灵活的架构来实现真正的持续学习，但"we are not doing that yet"。
- **Self-learning 预测**（Koray, 2026-05）：预测 IO 2027 前后，模型将在实验层面参与改进自身的部分——"rely on the models to improve different parts of Gemini"。Jeff 补充这将是在人类指导下的自我改进（"under the guidance of researchers"）。
- 缺乏持续学习会限制 Agent 的 `fire and forget` 能力：Agent 可以完成任务片段，但很难长期适应一个具体组织、项目或科学问题空间。

## 与工程补丁的边界

| 机制 | 能解决什么 | 仍缺什么 |
|------|------------|----------|
| 长上下文窗口 | 把更多当前材料放进工作记忆 | 不会自动区分重要、错误、过期和噪声 |
| RAG / 向量检索 | 运行时找回相关材料 | 检索结果不等于知识整合 |
| [[Multi-Layer-Memory]] | 跨会话保存经验和规则 | 仍需人工或 harness 设计晋升、清理和验证机制 |
| [[LLM-Wiki]] | 把原始材料编译为稳定知识层 | 主要是外部知识系统，不是模型权重级学习 |
| Continual Learning | 系统随经验更新内部能力 | 仍是开放研究问题，可能需要架构突破 |

## 与 Agent 知识管理的关系

[[Agent-Knowledge-Management|Agent 知识管理]]是持续学习的工程近似：用 raw、wiki、memory、skills、lint 和人类策展模拟“长期学习”。它的价值在于让 Agent 不必把所有知识塞进当前上下文，而是通过可版本化、可审查的外部层积累经验。

但这仍是外部化的持续学习。真正的 Continual Learning 要求系统能在长期任务中更新 [[World-Model|世界模型]]、保留有用经验、删除错误假设，并在新情境中迁移旧知识。

## 前提与局限性

- 持续学习可能只需要现有范式继续 scale 和增量创新，也可能需要新的架构突破；当前证据不足以确定。
- 生物启发提供了方向，但机器系统不必照搬海马体或睡眠机制。
- 持续学习必须处理污染问题：错误经验被长期保存，比一次性幻觉更危险。
- 对企业 Agent 来说，持续学习还涉及权限和治理：哪些经验可以进入长期记忆，谁批准，谁能删除，谁承担后果。

## 关联概念

- [[World-Model]] - 持续学习更新的是系统对环境和因果结构的内部表示
- [[Multi-Layer-Memory]] - 外部记忆系统是持续学习的工程替代层
- [[Agent-Knowledge-Management]] - 用 Wiki、skills 和检索组织长期知识
- [[Jagged-Intelligence]] - 缺乏稳定学习会让模型能力表现更加锯齿化
- [[Scientific-Discovery-AI]] - 科学发现需要把多轮实验结果累计为可行动的知识
- [[Model-Distillation]] - 蒸馏传递训练时快照，不替代运行时持续学习
- [[Unified-Model-Strategy]] - 统一模型为持续学习提供一致的能力基础
