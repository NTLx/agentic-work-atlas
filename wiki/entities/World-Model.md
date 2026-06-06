---
type: entity
title: World Model
aliases:
  - World Model
  - 世界模型
definition: "AI 系统对环境状态、因果结构和行动后果的内部表示，使 Agent 能在长期任务中预测、规划并随经验修正策略"
created: 2026-05-18
updated: 2026-06-06
tags:
  - AI
  - AGI
  - cognitive-architecture
related_entities:
  - "[[Continual-Learning]]"
  - "[[Tool-Use-Architecture]]"
  - "[[Scientific-Discovery-AI]]"
  - "[[Agent-Knowledge-Management]]"
  - "[[Jagged-Intelligence]]"
  - "[[Unified-Model-Strategy]]"
  - "[[Model-Distillation]]"
source_raw:
  - "[[Demis Hassabis: Agents, AGI & The Next Big Scientific Breakthrough]]"
  - "[[20260529-gemini-co-leads-origins]]"
  - "[[20260606-fei-fei-world-model-taxonomy]]"
---

# World Model（世界模型）

> [!definition] 定义
> **World Model** 是 AI 系统对外部环境、状态转移、因果关系和行动后果的内部表示。它让 Agent 不只是响应当前输入，而是能预测“如果我这么做，会发生什么”，并在长期任务中用新经验修正策略。

## 为什么重要

没有世界模型的 Agent 更像强大的反应器：它能根据当前上下文生成下一步，但很难稳定理解环境如何变化、哪些变量会造成后果、哪些经验应该迁移到未来任务。

持续学习需要世界模型作为承载对象。系统不是把每段历史原样存下来，而是要把经验压缩成对环境有预测力的结构：哪些行动有效，哪些约束稳定，哪些假设被实验推翻，哪些工具输出可信。

## 关键数据点

- Hassabis 认为当前 AGI 路线仍缺持续学习、长期推理和记忆；这些能力都依赖系统能形成可更新的世界模型。
- 更长上下文不等于世界模型。上下文是材料集合，世界模型是对材料背后因果结构的压缩。
- **Gemini Omni 联合训练**（Koray Kavukcuoglu, 2026-05）：Gemini Omni 被定位为"真正的世界模型"——不是文本到视频的单向生成（如 Veo），而是联合训练理解物理、视觉、文本等多模态。过去复杂视频场景的前向一致性需要手动设计，现在"just by training at scale and mixing all the data, we're seeing these capabilities emerge"。
- **功能分类补充**（Fei-Fei Li, 2026-06）：world model 至少可拆成三种输出职责：renderer 输出 observation、simulator 输出 state、planner 输出 action；其中 simulator 是连接 render 和 plan 的结构中枢。
- 对 coding agent 来说，世界模型包括代码库结构、测试反馈、用户目标、部署环境和长期约束。
- 对科学发现 Agent 来说，世界模型包括实验结果、假设空间、目标函数、模拟器状态和工具可靠性。
- 世界模型必须与 [[Tool-Use-Architecture|工具使用架构]]结合：模型通过工具获得观测、执行实验、校验预测，而不是只在文本里想象。

## 功能分类：renderer / simulator / planner

Fei-Fei Li 的分类让“世界模型”从一个过载热词变成可分析结构：

| 类型 | 主要输出 | 成功标准 |
|------|----------|----------|
| renderer | observation | 视觉保真、像不像人眼看到的世界 |
| simulator | state | 几何、物理、动力学是否结构正确 |
| planner | action | 给定观察与目标后，下一步行动是否合理 |

这组分类的价值在于，它把“会生成视频”“会模拟物理”“会规划动作”切回同一个 perception-action loop 中。不同系统可能共享底层知识，但对外暴露的契约并不相同。

其中最重要的判断是：**simulator 是三者的桥**。如果语言是对世界的抽象、像素是对世界的投影，那么几何、物理和动力学更接近世界的结构骨架。render 和 plan 最终都要依赖这层骨架。

## 与相邻概念的边界

| 概念 | 区别 |
|------|------|
| 上下文窗口 | 当前可见材料；不自动形成稳定因果结构 |
| 记忆系统 | 保存过去经验；不保证经验能预测未来 |
| [[Continual-Learning]] | 更新机制；World Model 是被更新的内部结构之一 |
| [[Scientific-Discovery-AI]] | 应用场景；World Model 让科学 Agent 能连接实验、理论和工具结果 |

## 失败模式

- **原始记录堆积**：系统保存了大量历史，但没有形成可预测的抽象。
- **错误模型固化**：早期错误假设被长期记忆反复调用，导致后续决策持续偏斜。
- **局部世界过拟合**：Agent 在一个项目或实验环境学到的规则，被错误迁移到另一种环境。
- **缺少外部校验**：内部模型看似连贯，但没有用工具、实验、测试或现实反馈更新。

## 前提与局限性

- 开放世界任务中的世界模型只能是局部、可修正的近似，不能被当作完整真相。
- 世界模型质量取决于反馈质量；静态文本通常不足以学习可靠因果关系。
- unified world model 虽然是合理终点，但 3D/物理数据稀缺、sim-to-real gap 和生成几何错误仍是硬瓶颈。
- 强世界模型也可能带来风险：系统越会预测和规划，越需要权限、目标和安全边界。

## 关联概念

- [[Continual-Learning]] - 世界模型需要通过持续学习更新
- [[Tool-Use-Architecture]] - 工具调用为世界模型提供外部观测和校验
- [[Scientific-Discovery-AI]] - 科学发现场景需要连接实验、理论和状态转移
- [[Agent-Knowledge-Management]] - 外部知识层可作为世界模型的材料来源
- [[Unified-Model-Strategy]] - 统一模型战略为联合多模态训练提供组织基础
- [[Model-Distillation]] - 蒸馏能否传递世界模型（vs 只传递统计模式）是开放问题
