---
type: entity
title: Scientific Discovery AI
aliases:
  - Scientific Discovery AI
  - 科学发现 AI
definition: "把巨大组合搜索空间、明确目标函数、数据或模拟器和工具调用结合起来，用 AI 寻找科学突破方案的系统形态"
created: 2026-05-08
updated: 2026-05-25
tags:
  - AI
  - science
  - deepmind
related_entities:
  - "[[Demis-Hassabis]]"
  - "[[Einstein-Test]]"
  - "[[Continual-Learning]]"
  - "[[World-Model]]"
  - "[[Tool-Use-Architecture]]"
source_raw:
  - "[[Demis Hassabis: Agents, AGI & The Next Big Scientific Breakthrough]]"
---

# Scientific Discovery AI（科学发现 AI）

> [!definition] 定义
> **Scientific Discovery AI** 是用 AI 在科学问题空间中寻找突破的系统形态。它通常需要四个条件：巨大组合搜索空间、明确目标函数、足够数据或模拟器，以及能通过工具调用和实验反馈不断校验假设。

## 为什么重要

科学发现是检验 AI 是否能超越文本生成的重要场景。它要求系统不只是复述论文或给出方案，而是在庞大搜索空间中找到人类难以穷举的结构，并把结果变成可验证的理论、实验或工具。

Hassabis 从 AlphaGo 和 AlphaFold 总结出一个模式：当问题可以被描述为海量组合搜索，并且有可优化目标函数时，AI 能找到 needle in a haystack 式的解。围棋中的惊人落子和蛋白质折叠中的结构预测，都是这个模式的不同实例。

## 关键数据点

- AlphaFold 被全球数百万研究者使用，说明科学发现 AI 的价值不只是论文指标，而是能成为科研基础设施。
- Hassabis 提出的通用条件是：组合搜索空间足够大、目标函数清晰、有足够数据或模拟器生成分布内数据。
- 药物发现可被表述为搜索问题：如果物理规律允许某种化合物存在，难点就是如何高效找到它。
- 虚拟细胞路线需要更强的观测和模拟能力，可能依赖无损活细胞纳米级成像，也可能依赖更好的学习型模拟器。
- 通用模型不应把所有专业科学知识塞进一个巨大脑袋；更可行的是通过 [[Tool-Use-Architecture|工具使用架构]] 调用 AlphaFold 这类专用系统。

## 两种层级

| 层级 | 任务 | 代表问题 |
|------|------|----------|
| 搜索型发现 | 在已有规则和目标函数下找到极优解 | 围棋走法、蛋白质折叠、候选分子搜索 |
| 框架型发现 | 提出新的问题、理论或解释结构 | [[Einstein-Test|Einstein Test]] 所关心的新理论生成 |

当前方法在第一层更有把握。第二层需要更强的类比推理、世界模型、持续学习和对“什么问题重要”的判断。

## 与 Agent 架构的关系

科学发现 AI 很可能不是一个单体模型，而是一个 agentic tool-use system：

- 通用模型负责拆问题、规划实验、调用工具和整合结果。
- 专用模型负责蛋白质、材料、药物、数学或模拟器中的特定能力。
- [[World-Model]] 负责把实验结果和理论假设连接起来。
- [[Continual-Learning]] 负责让多轮实验经验不被遗忘，也不被错误经验污染。

这与企业 Agent 的结构类似：通用 orchestrator 不替代所有专家系统，而是协调专用工具、检索、验证和人类判断。

## 前提与局限性

- 清晰目标函数不是所有科学领域都有；“什么是好猜想”比“怎样赢棋”更难定义。
- 数据和模拟器可能是瓶颈，尤其是生命科学中无法直接观测的动态过程。
- 搜索型突破不等于真正原创；系统可能会解已有问题，却不会提出新问题。
- 科学发现结果必须经过实验或形式化验证，不能只靠语言说服。

## 关联概念

- [[Einstein-Test]] - 检验系统能否提出新问题和新理论
- [[Continual-Learning]] - 多轮实验需要累积经验并避免遗忘
- [[World-Model]] - 科学探索需要可更新的环境和理论表示
- [[Tool-Use-Architecture]] - 通用模型应协调专用科学工具
- [[Demis-Hassabis]] - AlphaGo / AlphaFold 路线背后的关键人物
