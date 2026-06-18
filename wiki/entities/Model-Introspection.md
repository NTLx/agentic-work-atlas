---
type: entity
title: Model Introspection
aliases:
  - Model Introspection
  - 模型自省
definition: "让模型分析自己为什么会犯某个错误，从其推理链路中提取人类独立分析难以获得的洞察"
created: 2026-05-08
updated: 2026-06-15
evidence_level: medium
claim_type: mixed
tags:
  - AI
related_entities:
  - "[[Cat-Wu]]"
  - "[[Jagged-Intelligence]]"
  - "[[AI-Psychosis]]"
  - "[[Product-Overhang]]"
  - "[[Research-Preview]]"
  - "[[Competent-Output]]"
source_raw:
  - "[[How Anthropic’s product team moves faster than anyone else - Cat Wu (Head of Product, Claude Code)]]"
  - "[[Anthropic's Boris Cherny: Why Coding Is Solved, and What Comes Next]]"
  - "[[20260617-huggingface-agentic-resource-discovery]]"
---

# Model Introspection（模型自省）

> [!definition] 定义
> **Model Introspection（模型自省）** 是一种 AI 使用技能：当模型犯错时，不只修复错误，而是追问模型"分析你刚才为什么犯这个错"。模型对自身错误的分析能产生远超人类独立分析的洞察，因为它能访问推理链路中隐含的模式和假设。

## 关键数据点

- **Cat 的实际用法**：经常让 Claude "分析你刚犯的错误，告诉我你为什么会犯"——将此视为 debugging workflow 的标准步骤
- **洞察深度**：模型的自省经常揭示其推理路径中的系统性偏差——不仅仅是"我算错了"，而是"我在做类似 X 的判断时倾向于假设 Y"
- **与其他 debugging 方法的关系**：比传统 rubber duck debugging 更强——你不是在跟一个无响应的对象说话，你是在问那个犯了错的 entity
- **隐性知识提取**：模型对自身行为的解释可能揭示其训练数据分布或 RL 回路中的规律——这构成了反馈到 fine-tuning 的闭环

## 前提与局限性

- 模型自省本质上仍是 pattern prediction——它不是真正的元认知（metacognition），而是对"什么样的解释看起来合理"的预测
- 模型对错误原因的解释可能是幻觉——"我是因为 X 犯的错"可能只是听起来合理，实际上真正原因是完全不同的模式偏差
- 过度依赖自省可能产生"自我强化偏差"——模型在自省中发现的模式可能进一步固化其偏见
- 区分真正有用的自省和 post-hoc rationalization 需要人类 [[Judgment|判断力]]

## 作为产品研究方法的模型自省

Cat Wu 在 Anthropic 产品团队将模型自省从 debugging 技巧升级为产品研究方法。其逻辑是：模型解释自己为什么犯某个错误时，不仅暴露了单次失误，还揭示了它在某类任务上的系统性行为模式。

这对产品团队有三层价值：

1. **能力边界测绘**：模型的自省解释暴露了它在什么类型的上下文中稳定失误、什么条件下突然变强——这比人工测试更高效地绘制了 [[Product-Overhang|产品能力溢出]] 的边界。
2. **发布决策支撑**：通过观察模型的自省质量，产品团队可以判断某个能力是接近可用（自省能定位问题且有改进路径），还是根本不可靠（自省输出本身就是幻觉）。这直接支撑 [[Research-Preview|Research Preview]] 的发布时机决策。
3. **评测集补充**：模型自省揭示的失败模式可以被转化为新的评测用例，补充到 [[Evaluation-Set|评测集]] 中，形成"自省 → 评测 → 训练 → 自省"的闭环。

## 与人类 debugging 的结构对比

| 维度 | Rubber Duck Debugging | Model Introspection |
|------|----------------------|---------------------|
| 对话对象 | 无响应的物体 | 犯了错的实体 |
| 信息来源 | 人类自己的推理 | 模型的推理链路 |
| 洞察深度 | 受限于人类视角 | 可揭示训练分布中的系统性偏差 |
| 风险 | 无 | 自省可能是后验合理化 |

传统 debugging 的核心瓶颈是人类看不到模型内部的决策路径。模型自省的价值不是"模型知道自己为什么错"（它可能不知道），而是"模型的解释能揭示人类看不到的模式"——即使解释本身不完全准确，它指向的方向仍然有价值。

## 关联概念

- [[Jagged-Intelligence]] — 模型自省揭示了锯齿状的内部结构。
- [[Taste]] — 判断模型自省的质量需要品味——区分真洞察和合理美化。
- [[Judgment]] — 辨别模型自省中的信号与噪音。
- [[Product-Overhang]] — 模型自省帮助产品团队发现模型已具备但尚未产品化的能力。
- [[Competent-Output]] — 自省是判断输出是否合格的辅助手段：模型能解释自己的输出为什么合格，比"看起来合格"更可靠。
