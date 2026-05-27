---
type: entity
title: Verifiability
aliases:
  - Verifiability
  - 可验证性
definition: "决定 LLM 自动化能力的关键维度——能客观验证输出质量的领域可通过 RLVR 训练持续提升，不能验证的领域模型进步受限"
created: 2026-05-08
updated: 2026-05-26
tags:
  - AI
  - LLM
  - RL
  - training
related_entities:
  - "[[Jagged-Intelligence]]"
  - "[[Ghost-Intelligence]]"
  - "[[Agentic-Engineering]]"
  - "[[Andrej-Karpathy]]"
  - "[[Specialization-Compounds]]"
  - "[[Evaluation-Set]]"
  - "[[Taste]]"
  - "[[Agent-Containment]]"
source_raw:
  - "[[Andrej Karpathy: From Vibe Coding to Agentic Engineering]]"
  - "[[Specialization Beats Scale A Strategic Variable Most AI Procurement Decisions Overlook]]"
---

# Verifiability（可验证性）

> [!definition] 定义
> **Verifiability（可验证性）** 指一个任务或领域的输出能否被客观、自动地验证。这是 RLVR（基于可验证奖励的强化学习）训练的核心前提——只有可验证的领域，模型才能通过大规模 RL 持续进步。可验证性是解释 LLM 能力分布不均匀的关键变量。

## 关键数据点

- **RLVR 机制**：数学题的答案可自动判断对错、代码可通过测试验证——因此模型在这些领域能力爆炸性增长
- **模型能力的经济学**：代码领域创造了最大的经济价值和最多的 RL 环境，因此 labs 投入最多，能力进步最快
- **非对称分布**：传统计算机能自动化的是"你可以在代码中精确指定"的任务；LLM 能自动化的是"你可以验证"的任务——后者范围大得多
- **可验证 ≠ 自动进步**：即使一个领域客观可验证，如果 labs 不投入（没经济价值），模型也不会自动变好

## 前提与局限性

- 当前框架下，"可验证"主要指有客观自动化验证方式（测试、数学证明、eval 分数）。
- 写作、设计等主观领域可通过 LLM 评审团等方式逼近可验证性，但精度下降。
- Karpathy 认为长期看"几乎一切都可以被做成可验证的"，区别只是难度。
- 对创业者而言，在未被 labs 覆盖的可验证领域建立 RL 环境，是结构性机会。

## RLVR 经济学：为什么可验证性决定能力分布

可验证性不只是技术属性，它驱动了 labs 的资源分配决策。其经济学链条是：

1. **可验证 → 可建 RL 环境**：数学有标准答案，代码有测试用例——这些领域可以低成本生成大量验证信号。
2. **RL 环境 → 训练数据飞轮**：有了验证信号，模型可以通过 RLVR 自我改进，不需要持续的人工标注。
3. **飞轮 → labs 投入**：labs 把资源投向 RL 环境最成熟的领域，因为这些领域的 ROI 最高。
4. **投入 → 能力差距**：代码领域创造了最大经济价值和最多 RL 环境，因此 labs 投入最多，能力进步最快。

这导致了一个反直觉的结果：LLM 在可验证领域（代码、数学）极强，在不可验证领域（写作、设计、战略判断）相对弱。[[Jagged-Intelligence|锯齿状智能]] 的根源就在这里。

## 可验证性的企业含义

对企业 AI 采购和部署而言，可验证性是一个被低估的战略变量：

| 场景特征 | 可验证性 | 适合的策略 |
|----------|---------|-----------|
| 输出可通过测试/规则验证 | 高 | 大胆用 Agent 自动化，依赖 [[Evaluation-Set|评测集]] 监控质量 |
| 输出有专业标准但需人类判断 | 中 | Agent 辅助 + 人类审核，逐步扩展自动化边界 |
| 输出质量高度主观 | 低 | Agent 做初稿或辅助，核心决策保留人类 |

可验证性还与 [[Specialization-Compounds|专门化复利]] 形成交叉：只有可验证的任务才能通过评测暴露专门化小模型的收益。如果一个任务不可验证，企业就无法判断专门化模型是否真的比通用模型好——专门化复利的飞轮也就无法启动。

## 关联概念

- [[Jagged-Intelligence]] — 可验证性是锯齿状分布的根本原因。
- [[Ghost-Intelligence]] — LLM 没有内在动机，完全依赖外部验证信号。
- [[Agentic-Engineering]] — 可验证性使 Agent 能迭代出可工作的软件。
- [[Taste]] — 在不可验证领域的判断力，目前仍是人类护城河。
- [[Specialization-Compounds]] — 只有可验证任务才能暴露专门化模型的收益。
- [[Evaluation-Set]] — 评测集是企业层面的可验证性基础设施。
