---
type: topic
title: Verifiable Agent Engineering
description: "可验证 Agent 工程：把 LLM 的非确定性推理关进可观察、可拒绝、可复现的工程系统"
created: 2026-05-18
updated: 2026-05-20
tags:
  - AI-Agent
  - verification
  - engineering
related_entities:
  - "[[Verifiability]]"
  - "[[Dominator-Analysis]]"
  - "[[Agentic-Engineering]]"
  - "[[Agent-Harness]]"
  - "[[Agent-PR-Review]]"
  - "[[Accessibility-Agent]]"
  - "[[Bias-to-Action-LLM]]"
  - "[[Accessibility-Complexity-Evaluation]]"
  - "[[Accessibility-High-Risk-Patterns]]"
  - "[[Corrective-RAG]]"
  - "[[Reflexion]]"
  - "[[MachinaCheck]]"
  - "[[Hardware-Sovereignty]]"
source_raw:
  - "[[Andrej Karpathy: From Vibe Coding to Agentic Engineering]]"
  - "[[Validating agentic behavior when “correct” isn’t deterministic]]"
  - "[[Agent pull requests are everywhere. Here's how to review them.]]"
  - "[[Building a general-purpose accessibility agent—and what we learned in the process]]"
  - "[[MachinaCheck Building a Multi-Agent CNC Manufacturability System on AMD MI300X]]"
  - "[[OncoAgent A Dual-Tier Multi-Agent Framework for Privacy-Preserving Oncology Clinical Decision Support]]"
  - "[[Maintainability sensors for coding agents]]"
---

# Verifiable Agent Engineering（可验证 Agent 工程）

> [!summary] 核心洞察
> Agent 的能力上限不由“模型愿意做多少事”决定，而由“系统能验证多少事”决定。真正可规模化的 Agent 工程，不是放大自主性，而是扩大可验证边界。

## 为什么这是一个独立 Topic

现有 Agent 讨论容易把问题落在“模型更强”“工具更多”“循环更长”上。但 wiki 中多条线索指向同一个底层结构：

- [[Verifiability|可验证性]]解释了为什么代码、数学、测试驱动任务进步最快。
- [[Dominator-Analysis|支配者分析]]说明非确定性行为也能被提取出必经骨架。
- [[Accessibility-Agent|无障碍 Agent]]显示真实生产系统需要知道何时不动手。
- [[MachinaCheck]]说明领域 Agent 不应把确定性工作交给 LLM。
- [[Corrective-RAG]]和[[Reflexion]]把“生成”变成可拒绝、可重试、可审计的管线。

这些不是零散技巧，而是同一件事：给非确定性智能修一条确定性轨道。

## 三个生成器

| 生成器 | 它解决什么 | 典型实体 |
|--------|------------|----------|
| 可验证边界 | 哪些输出能自动判断对错 | [[Verifiability]], [[Agent-PR-Review]], [[WCAG]] |
| 确定性骨架 | 哪些步骤必须由代码、规则、图结构保证 | [[Dominator-Analysis]], [[MachinaCheck]], [[Corrective-RAG]] |
| 拒绝机制 | 什么时候停止生成、转人工、返回安全拒绝 | [[Bias-to-Action-LLM]], [[Accessibility-High-Risk-Patterns]], [[Reflexion]] |

缺第一根，Agent 只是在表演努力。缺第二根，系统会把所有复杂性都倒给 LLM。缺第三根，Agent 的“行动偏差”会把边界条件变成事故。

## 从“让 Agent 做”到“让 Agent 被验证”

传统自动化的核心问题是：能不能把流程写成规则。

Agentic 自动化的核心问题变了：能不能把结果、路径或中间状态变成可验证对象。

```
任务目标
  ↓
可观察状态   ← 日志 / 截图 / 代码快照 / 结构化输出
  ↓
验证骨架     ← 测试 / dominator / schema / 距离门控 / 规则引擎
  ↓
动作边界     ← 自动修复 / 重试 / 拒绝 / 人工接管
```

这解释了为什么“可验证性”比“智能程度”更接近工程第一性原理。模型可以更聪明，但系统必须知道什么时候相信它。

## 生产级 Agent 的反直觉

越接近生产，越不应该让 LLM 覆盖整个流程。

[[MachinaCheck]] 的价值不在“用了多个 Agent”，而在它只在需要制造推理和报告组织的环节使用 LLM。STEP 文件解析和工具匹配由确定性代码完成，因为这些环节不需要想象力，只需要正确性。

[[Accessibility-Agent|无障碍 Agent]] 的价值也不在“自动改所有问题”，而在识别复杂度、高风险交互和人工介入点。一个能拒绝的 Agent，比一个永远动手的 Agent 更接近生产可用。

## 可验证性不是测试覆盖率

测试只是可验证性的一种形式。更完整的可验证工程至少包含四层：

| 层级 | 验证对象 | 示例 |
|------|----------|------|
| 输出验证 | 最终结果是否满足要求 | 单元测试、格式校验、WCAG 检查 |
| 路径验证 | 是否经过成功所需的必经状态 | [[Dominator-Analysis]] |
| 上下文验证 | 检索材料是否真的相关 | [[Corrective-RAG]] |
| 行为验证 | 系统是否在该停止时停止 | 高风险模式转人工、安全拒绝 |

真正的 Agent harness 是这四层的组合，而不是一个更长的 prompt。

## 传感器层：把内部质量也纳入可验证边界

Birgitta Böckeler 对这个 Topic 的补充在于：Agent 的可验证性不应只盯着“功能有没有做对”，还要盯着“代码库是否仍然值得继续让 Agent 修改”。一旦小改动开始牵连越来越多文件，或者改一个地方更容易把旧功能带坏，系统虽然还在产出代码，但它的可维护性边界已经在塌。

这篇文章把传感器明确铺成三层：会话内即时反馈、CI 复验、周期性漂移审查。type checker、ESLint、Semgrep、dependency-cruiser、测试覆盖、增量 mutation testing 和 GitLeaks 负责在开发过程中不断收缩错误空间；安全审查、数据处理审查、依赖新鲜度和模块耦合审查则负责发现慢变量上的退化。这样被验证的不只是输出结果，还包括结构、依赖和安全约束。

更关键的是，传感器不是纯报警器。作者把 lint message 改写成带工程判断的自我纠正提示，让 agent 学会什么时候该补类型、什么时候只压制 warning、什么时候阈值调整只能作为例外。这说明生产级 verification loop 不只是“有检查”，还要把检查包装成 agent 可消费的修正语言；否则反馈很快会退化成噪声，甚至把系统推向过度重构。

## 与现有 Topic 的关系

- [[Agentic-Engineering-Patterns]]回答“如何用 Agent 做软件工程”。
- [[Building-Effective-Agents]]回答“Agent 工作流有哪些架构模式”。
- 本 Topic 回答“这些模式怎样跨过 demo 与生产之间的断层”。

## 结论

Agent 工程的下一步不是更像人，而是更像实验室：输入可控，状态可观测，失败可复现，边界可拒绝。

当系统能验证一个 Agent，它才真正拥有这个 Agent。
