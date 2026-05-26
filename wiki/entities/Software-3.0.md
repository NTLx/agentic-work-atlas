---
type: entity
title: Software 3.0
aliases:
  - Software 3.0
definition: "编程范式第三阶段：上下文窗口是内存，提示词是程序语言，LLM 是解释器，编程从写代码变为设计给 agent 的指令文本"
created: 2026-05-08
updated: 2026-05-26
tags:
  - programming-paradigm
  - AI
  - LLM
related_entities:
  - "[[Software-2.0]]"
  - "[[Agentic-Engineering]]"
  - "[[Vibe-Coding]]"
  - "[[Agent-Native]]"
  - "[[Andrej-Karpathy]]"
  - "[[Latent-Space-vs-Deterministic]]"
  - "[[CLAUDE-md]]"
source_raw:
  - "[[Andrej Karpathy: From Vibe Coding to Agentic Engineering]]"
  - "[[OpenClaw + 6 个 Agent 运转半个月，从聊天到干活的完整工程实践]]"
---

# Software 3.0

> [!definition] 定义
> **Software 3.0** 是 Andrej Karpathy 在 Software 2.0（2017）的基础上提出的编程范式第三阶段。Software 1.0 = 人写代码规则；Software 2.0 = 人通过准备数据集和优化目标来训练神经网络；Software 3.0 = 人通过提示词和上下文窗口编程，LLM 成为新的"计算机"——上下文窗口是内存，提示词是程序语言，模型是解释器。

## 关键数据点

- **OpenClaw 安装案例**：传统方式需要应对多平台的复杂 shell 脚本（Software 1.0）；Software 3.0 方式是"复制粘贴一段文本给 agent"——agent 自带智能，能感知目标环境、调试循环，远比确定性脚本强大
- **MenuGen 案例**：Karpathy 用 Software 1.0+2.0 方式写了 OCR+图像生成的完整 app；但 Software 3.0 版本只用 Gemini + NanoBanana 一句话，LLM 直接在像素层渲染结果——"app 不应存在"
- **与 Software 2.0 的关系**：Software 2.0 是训练专用模型执行特定任务；Software 3.0 是用通用 LLM 通过提示词执行任意信息处理任务
- **CPU 角色翻转**：Karpathy 预测未来神经网络成为"主机进程"，CPU 退化为"协处理器"——翻转为当前虚拟化架构的镜像

## 前提与局限性

- Software 3.0 的"app 不应存在论"倾向激进——忽略了隐私、离线、定制化等真实需求。
- LLM 作为解释器的可靠性远不如传统 CPU——输出不稳定、不可完全预测。这正是 [[Latent-Space-vs-Deterministic|潜在空间与确定性分工]] 要解决的问题。
- 当前仍处于过渡期——多数产品是 Software 1.0/2.0/3.0 的混合体。
- 需要全新的工具链和最佳实践，整个行业仍在摸索。

## 三个范式的本质区别

| 维度 | Software 1.0 | Software 2.0 | Software 3.0 |
|------|-------------|-------------|-------------|
| 编程对象 | 代码 | 数据集和损失函数 | 提示词和上下文 |
| 执行器 | CPU | 神经网络 | LLM |
| 程序存储 | 源代码文件 | 模型权重 | 上下文窗口 |
| 调试方式 | 断点和日志 | 训练曲线和验证集 | 提示词工程和模型自省 |
| 核心技能 | 编程语言 | 机器学习 | 自然语言 + 系统设计 |
| 可靠性 | 确定性 | 统计性 | 生成性（不可完全预测） |

Software 1.0 到 2.0 的迁移是"从写规则到训练规则"。Software 2.0 到 3.0 的迁移是"从训练专用模型到使用通用模型"。每次迁移都降低了"让计算机做事"的门槛，但也引入了新的不可控性：Software 1.0 的 bug 可复现，Software 2.0 的泛化失败可度量，Software 3.0 的输出不可完全预测。

## 工程含义：CLAUDE.md 是 Software 3.0 的"程序"

如果 Software 3.0 的"程序"是提示词和上下文，那么 [[CLAUDE-md|CLAUDE.md]] 就是这种程序的典型形态。它不是传统意义上的文档，而是给 agent 的运行时指令——定义了 agent 的工作边界、质量标准和决策框架。

这个类比揭示了 Software 3.0 的核心工程挑战：如何把隐性的团队知识、业务约束和质量标准显式化到上下文中，让 agent 在没有人类实时监督的情况下做出正确决策。[[Agentic-Engineering|Agentic Engineering]] 就是在这种新范式下发展出的工程实践。

## 关联概念

- [[Software-2.0]] — 前序范式，从写代码到训练网络。
- [[Agentic-Engineering]] — Software 3.0 时代的工程实践。
- [[Vibe-Coding]] — Software 3.0 的普及化表达。
- [[Agent-Native]] — Software 3.0 要求的基础设施范式。
- [[Latent-Space-vs-Deterministic]] — Software 3.0 的核心张力：LLM 作为解释器不可靠，需要与传统确定性系统分工。
- [[CLAUDE-md]] — Software 3.0 的"程序"形态：给 agent 的运行时指令。
