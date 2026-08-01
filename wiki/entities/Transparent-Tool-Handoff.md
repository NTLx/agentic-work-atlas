---
type: entity
title: Transparent-Tool-Handoff
aliases:
  - Transparent Tool Handoff
  - 透明工具交接
  - Transparent Handoff
definition: "将复杂任务从不可解释的 LLM 交接给可解释工具（业务逻辑/决策树/回归模型/自定义函数）执行，LLM 只做编排——以系统级可解释性替代模型级可解释性的架构模式"
created: 2026-07-30
updated: 2026-07-30
tags:
  - agentic-engineering
  - explainability
evidence_level: medium
claim_type: mixed
related_entities:
  - "[[Model-Introspection]]"
  - "[[Agent-Observability]]"
  - "[[Decision-Centric-Architecture]]"
  - "[[Evaluation-Set]]"
  - "[[Agent-Verification]]"
source_raw:
  - "[[20260730-palantir-responsible-ai-black-box-explainability]]"
  - "[[20260730-palantir-responsible-ai-evals-prototype-to-production]]"
---

# Transparent-Tool-Handoff（透明工具交接）

> [!definition] 定义
> **透明工具交接**是一种以系统级可解释性替代模型级可解释性的架构模式：把复杂任务中可形式化的步骤从不可解释的 LLM handoff 给可解释工具（业务逻辑、决策树、线性回归、计算器、自定义函数），LLM 充当 orchestrator。它不解释 LLM 内部如何工作，但使 AI **系统**的行为可追踪、可诊断。

## 理论基础：CoT ≠ 解释

Chain-of-Thought 输出不是模型的解释——模型不在推理，而在**模仿**推理。CoT "thought" 是统计 token 预测的产物，结构上像推理，但与模型实际预测路径**无因果关系**（Anthropic 研究显示 CoT "reasoning" 可与真正的预测原因完全无关；另见 Miller 2018、Lipton《Mythos of Model Explainability》）。

由此推出两个实践结论：

1. 把 CoT 生成文本当作"模型为何如此输出"的忠实反映，是系统性误用。
2. CoT 的真正价值在于它使能了结构化的工具调用序列——可解释性的落点从"模型的自述"转移到"工具调用的记录"。

## 系统级 vs 模型级可解释性

| 维度 | 模型级可解释性 | 系统级可解释性 |
|------|--------------|--------------|
| 问题 | 为何此预测 | 组件如何交互 |
| 状态 | 未解问题（可能永远无满意解） | 今天可工程化实现 |
| 手段 | 反事实分析、归因、统计方法 | 工具交接 + 执行日志 + 工具源码检查 |
| 载体 | 模型内部 | 系统架构 |

## LLM Debugger 模式

code debugger 的 LLM 版本：输入数据到 LLM 驱动函数 → 观察每一步 tool invocation 的 input/output/execution log → 导航 tool call 序列 → 在工具逻辑层面诊断失败（"if our AI system begins to exhibit unexpected behaviors due to the use of a tool, we can examine the specific logic and steps of those tools"）。

Debugger 暴露 **how**（系统做了什么），工具源码检查给出 **why**（为何此逻辑产生此结果）。在 evals 迭代循环中，同一模式用于失败案例 drill-down：如产品召回系统将数学计算失败定位后 handoff 给 Calculator tool（准确率 41.3% → 93.3% → tool 修复）。

## 关键数据点

- CoT "reasoning" 可与真正的预测原因完全无关（Anthropic 研究 / Miller 2018 / Lipton《Mythos of Model Explainability》）
- LLM Debugger 模式：输入数据 → 观察 tool invocation 的 input/output/execution log → 导航 tool call 序列
- 产品召回案例：数学计算失败从 LLM 41.3% → Calculator tool handoff 后 93.3%
- 黑盒转移：tool invocation 日志解释"系统做了什么"，不解释"LLM 为何选择调用这个工具"——黑盒从整个系统缩小到 LLM 的选择，未被消除

## 前提与局限性

- **能力天花板**：能 handoff 给可解释工具的任务本身是确定性、可形式化的；最需要解释的高风险模糊判断恰恰无法 handoff。
- **orchestration 仍是黑盒**：tool invocation 日志只解释"系统做了什么"，不解释"LLM 为何选择调用这个工具"——黑盒从整个系统缩小到 LLM 的选择，未被消除。
- **时效边界**：CoT 忠实度研究主要针对提示诱导的 CoT；对训练出来的推理链（reasoning models），"CoT 与真实推理无因果关系"的强度需打折。

## 与模型自省的对立统一

> [!warning] 冲突标记
> 本实体与 [[Model-Introspection]] 表面矛盾：模型自省主张"问模型 why did you do this"能获得人类独立分析达不到的洞察；本实体主张模型自述的推理不可信。调和方式：**自省用于调试 harness**（发现 system prompt 误导、子 agent 委托失败等编排层错误），**tool-handoff 检查用于调试任务执行**（发现工具逻辑与数据错误）。两者作用于不同层次，不可互相替代；但自省结论必须经工具层证据交叉验证，不可单独采信。

## 关联概念

- [[Model-Introspection]] — 互补的 harness 层调试方法（见上方冲突标记）
- [[Agent-Observability]] — 工具调用日志是 agent 可观测性的核心数据源
- [[Decision-Centric-Architecture]] — logic binding 的工具化是本模式的架构前提
- [[Evaluation-Set]] — evals 迭代的 drill-down 环节依赖 tool-handoff 做定点修复
- [[Agent-Verification]] — 可解释的工具序列使 agent 自主验证成为可能
