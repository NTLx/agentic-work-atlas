---
type: comparison
title: "Vibe-Coding vs Software-2.0"
entity_a: "[[Vibe-Coding]]"
entity_b: "[[Software-2.0]]"
created: 2026-05-01
updated: 2026-05-22
tags:
  - comparison
  - analysis
source_raw:
  - "[[20260413-llm-wiki]]"
  - "[[What is agentic engineering? - Agentic Engineering Patterns]]"
  - "[[Andrej Karpathy: From Vibe Coding to Agentic Engineering]]"
---

# Vibe-Coding vs Software-2.0

## 定义对比

| 维度 | [[Vibe-Coding]] | [[Software-2.0]] |
|------|----------------|----------------|
| **定义** | Andrej Karpathy 提出的概念，指未经审查、原型质量的 LLM 生成代码 | Andrej Karpathy 提出的概念，指明软件开发范式的转变：从程序员编写代码（Software 1.0）转向程序员编写目标、神经网络通过数据编程（Software 2.0）。 |

## 核心差异

### 1. 本质区别

- **Vibe-Coding**: Software 3.0 时代的用户实践。人通过自然语言、运行反馈和复制粘贴驱动 LLM 生成软件，重点是快速原型和“忘记代码存在”。
- **Software-2.0**: 深度学习时代的编程范式。人定义目标、提供数据和损失函数，神经网络权重成为程序，重点是训练出的模型行为。

### 2. 应用场景

| 场景 | 更适合 |
|------|--------|
| 非程序员快速做原型、内部工具、一次性脚本 | Vibe-Coding |
| 视觉识别、语音识别、推荐系统、自动驾驶感知 | Software-2.0 |
| 通过 prompt 与 agent 交互生成应用代码 | Vibe-Coding |
| 通过数据集和优化器训练模型能力 | Software-2.0 |
| 生产级软件工程治理 | Agentic Engineering，而不是二者本身 |

### 3. 优缺点

**Vibe-Coding**
- ✅ 优点: 抬高软件创造的能力底线，让非专业开发者也能快速把想法变成可运行原型。
- ❌ 局限: 默认原型质量、缺少审查和验证；进入团队或生产场景时容易制造技术债和责任空洞。

**Software-2.0**
- ✅ 优点: 能解决传统规则编程难以手写的感知、语言和推荐问题，把数据和目标函数转化为可执行能力。
- ❌ 局限: 依赖数据质量、训练成本和评估集；在确定性、安全敏感和可解释要求高的领域仍需 Software 1.0 框架约束。

## 关联关系

- [[Software-2.0]] → [[Software-3.0]]: Software 2.0 把“程序”从手写代码扩展到神经网络权重；Software 3.0 进一步把 LLM 变成可提示、可交互的计算机。
- [[Vibe-Coding]] → [[Software-3.0]]: Vibe Coding 是 Software 3.0 的大众化实践，不是 Software 2.0 的同义词。
- [[Agentic-Engineering]] → [[Vibe-Coding]]: Agentic Engineering 保留 Vibe Coding 的速度，但加上测试、review、harness 和 ownership。

## 选择指南

何时选择 **Vibe-Coding**:
- 目标是探索想法、验证界面、写个人脚本或低风险原型。
- 失败成本低，且你可以接受后续重写或工程化。

何时选择 **Software-2.0**:
- 目标行为无法靠显式规则稳定手写，但可以用大量数据和目标函数训练。
- 你需要构建模型能力本身，而不是让模型帮你生成普通软件。

## 相关概念

- [[Vibe-Coding]]
- [[Software-2.0]]
