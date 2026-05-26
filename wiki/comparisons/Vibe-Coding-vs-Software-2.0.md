---
type: comparison
title: "Vibe-Coding vs Software-2.0"
entity_a: "[[Vibe-Coding]]"
entity_b: "[[Software-2.0]]"
created: 2026-05-01
updated: 2026-05-26
tags:
  - comparison
  - analysis
source_raw:
  - "[[20260413-llm-wiki]]"
  - "[[What is agentic engineering? - Agentic Engineering Patterns]]"
  - "[[Andrej Karpathy: From Vibe Coding to Agentic Engineering]]"
  - "[[What Is Code?]]"
  - "[[20260409-ai-capability-gap-ai-psychosis]]"
---

# Vibe-Coding vs Software-2.0

> [!summary] 对比概述
> Vibe Coding 和 Software 2.0 都由 [[Andrej-Karpathy|Andrej Karpathy]] 提出，但分属不同范式阶段。Software 2.0（2017）把"程序"从手写代码扩展到神经网络权重；Vibe Coding（2025）是 Software 3.0 的普及化实践——人通过自然语言和运行反馈驱动 LLM 生成软件。两者共享"人不直接写实现"的方向，但在接口、验证、所有权和工程治理上分歧显著。

## 定义对比

| 维度 | [[Vibe-Coding]] | [[Software-2.0]] |
|------|----------------|------------------|
| **定义** | 人通过自然语言、运行反馈和复制粘贴驱动 LLM 生成软件，重点是快速原型和"忘记代码存在" | 人定义目标和损失函数、提供数据集，神经网络权重成为程序 |
| **提出年份** | 2025 年 2 月 | 2017 年 11 月 |
| **所属范式** | [[Software-3.0]] 的大众化实践 | 深度学习时代的编程范式 |
| **主要接口** | 提示词、上下文窗口、运行反馈 | 数据集、目标函数、优化器 |
| **"程序"形态** | LLM 在上下文中解释并生成的代码文本 | 训练后的神经网络权重矩阵 |
| **"编译"过程** | 对话、运行和复制粘贴 | 训练过程（SGD/Adam 优化） |

## 演进脉络：Software 1.0 → 2.0 → 3.0

两个概念不是同层对比，而是跨代对比。理解这条演进链才能看清各自位置：

| 阶段 | 程序员的工作 | 程序的来源 | 代表技术 |
|------|-------------|-----------|---------|
| **Software 1.0** | 编写明确的代码逻辑 | 人类编写的源代码 | C++, Python, Java |
| **Software 2.0** | 编写目标和约束，准备数据集 | 神经网络通过数据学习生成 | PyTorch, TensorFlow |
| **Software 3.0** | 设计提示词和上下文，审查输出 | LLM 在上下文中解释并生成 | Claude, GPT, Gemini |

Vibe Coding 是 Software 3.0 的**用户侧实践**——人不再直接写大量实现代码，而是"see things, say things, run things, and copy paste things"。Software 2.0 是**模型侧构建**——人定义训练目标和数据，让神经网络自己学会执行任务。

## 核心差异

### 1. 工程治理维度

这是两者最关键的分歧，也是实践中最容易被忽略的：

| 治理维度 | Vibe Coding | Software 2.0 |
|----------|-------------|--------------|
| **验证方式** | 凭感觉、肉眼看运行结果 | 验证集评估、交叉验证、A/B 测试 |
| **质量标准** | 原型质量——"mostly works" | 生产质量——精度、召回率、F1 |
| **可复现性** | 低——每次对话上下文不同 | 高——相同数据和超参数可复现 |
| **回归检测** | 无系统机制 | 持续评估流水线 |
| **所有权归属** | 模糊——人说不清代码为什么这样写 | 明确——数据集和模型版本可追溯 |
| **团队协作** | 困难——每个人的 vibe 不同 | 可标准化——数据管道和模型注册表 |

美团的 31 万行 AI Coding 实践揭示了 Vibe Coding 在团队场景下的系统性风险：当 90%+ 代码由 AI 生成且缺乏统一规范时，不同背景成员各自 vibe，系统会加速腐化而非收敛复杂度。

### 2. 适用场景

| 场景 | 更适合 |
|------|--------|
| 非程序员快速做原型、内部工具、一次性脚本 | Vibe Coding |
| 视觉识别、语音识别、推荐系统、自动驾驶感知 | Software 2.0 |
| 通过 prompt 与 agent 交互生成应用代码 | Vibe Coding |
| 通过数据集和优化器训练模型能力 | Software 2.0 |
| 需要确定性保证的安全关键系统 | 两者都不适合——需要 Software 1.0 |
| 生产级软件工程治理 | [[Agentic-Engineering]]，而不是二者本身 |

### 3. 失败模式

**Vibe Coding 的失败模式**：
- **技术债加速**：LLM 倾向过度复杂化代码、膨胀抽象层、不清理死代码。Karpathy 自己观察到模型会"实现冗余、脆弱的 1000 行方案，经提示后可压缩为 100 行"。
- **所有权空洞**：当代码由 AI 生成、人不审查细节时，出了生产事故没有人能解释系统为什么这样工作。
- **品味退化**：长期暴露在 AI 平均产出中，人对"好代码"的判别力可能下降。

**Software 2.0 的失败模式**：
- **数据依赖**：模型行为由数据集决定，数据清洗、标注和偏差控制成本常被低估。
- **不可解释性**：权重矩阵不可读，安全敏感和可解释要求高的领域仍需 Software 1.0 框架约束。
- **领域局限**：只适合目标函数可定义的感知类任务，不适合需要显式逻辑推理和确定性保证的场景。

### 4. 优缺点

**Vibe Coding**
- 优点: 抬高软件创造的能力底线，让非专业开发者也能快速把想法变成可运行原型。继承了 Software 2.0 "程序由神经网络产生" 的方向，但操作界面从数据集和训练目标变成了上下文窗口与自然语言。
- 局限: 默认原型质量、缺少审查和验证；进入团队或生产场景时容易制造技术债和责任空洞。

**Software 2.0**
- 优点: 能解决传统规则编程难以手写的感知、语言和推荐问题，把数据和目标函数转化为可执行能力。
- 局限: 依赖数据质量、训练成本和评估集；在确定性、安全敏感和可解释要求高的领域仍需 Software 1.0 框架约束。

## 关联关系

- [[Software-2.0]] → [[Software-3.0]]: Software 2.0 把"程序"从手写代码扩展到神经网络权重；Software 3.0 进一步把 LLM 变成可提示、可交互的计算机。
- [[Vibe-Coding]] → [[Software-3.0]]: Vibe Coding 是 Software 3.0 的大众化实践，不是 Software 2.0 的同义词。
- [[Agentic-Engineering]] → [[Vibe-Coding]]: Agentic Engineering 保留 Vibe Coding 的速度，但加上测试、review、harness 和 ownership——本质上是在 Software 3.0 中补回 Software 2.0 已有的工程纪律（验证集、评估流水线、版本管理）。
- [[Jagged-Intelligence]]: Vibe Coding 暴露了 LLM 的锯齿状能力——在代码生成上极强，在常识推理上脆弱。Software 2.0 的锯齿则体现在训练域内极强、域外脆弱。

## 选择指南

何时选择 **Vibe Coding**:
- 目标是探索想法、验证界面、写个人脚本或低风险原型。
- 失败成本低，且你可以接受后续重写或工程化。
- 你需要的是快速把想法变成可运行的东西，而不是构建可维护系统。

何时选择 **Software 2.0**:
- 目标行为无法靠显式规则稳定手写，但可以用大量数据和目标函数训练。
- 你需要构建模型能力本身，而不是让模型帮你生成普通软件。
- 你有数据管道、评估体系和模型版本管理的基础设施。

何时 **两者都不应选**:
- 你需要确定性保证（银行系统、编译器、加密算法）。
- 你需要可解释性（监管合规、安全审计）。
- 你需要长期可维护性且团队规模大于 1 人——此时应升级为 [[Agentic-Engineering]]。

## 相关概念

- [[Vibe-Coding]]
- [[Software-2.0]]
- [[Software-3.0]]
- [[Agentic-Engineering]]
- [[Andrej-Karpathy]]
- [[Jagged-Intelligence]]
- [[Verifiability]]
- [[Harness-Engineering]]
