---
type: entity
title: Agent Logic
aliases:
  - Agent Logic
  - agent logic
  - Agent 逻辑
definition: "运行在 Agent harness 内、模型之外的工作流专用逻辑层，用知识图谱、程序分析、算法、策略执行和验证结构缩小 LLM 的推理空间"
created: 2026-06-02
updated: 2026-06-15
evidence_level: medium
claim_type: mixed
tags:
  - AI-Agent
  - enterprise-ai
  - agent-harness
  - architecture
related_entities:
  - "[[Agent-Harness]]"
  - "[[Local-Bounded-Reasoning]]"
  - "[[Policy-as-Code-for-Agent-Governance]]"
  - "[[Graph-Guided-Agent-Investigation]]"
  - "[[Verifiable-Agent-Engineering]]"
  - "[[Enterprise-AI-Factory]]"
source_raw:
  - "[[20260602-ibm-agent-logic-scalable-ai-adoption]]"
---

# Agent Logic

> [!definition] 定义
> **Agent Logic** 是运行在 [[Agent-Harness|Agent harness]] 内、模型之外的工作流专用逻辑层。它用知识图谱、程序分析、算法、策略执行、图遍历、自适应规划和验证循环，为 LLM 缩小上下文空间并约束行动路径。

## 核心问题

企业 Agent 不只是回答问题，而是要进入长周期、多系统、强权限、强合规的真实工作流。单纯扩大上下文窗口会把问题推给 LLM：更多 token、更高成本、更大幻觉空间，也更难审计。

Agent logic 的判断相反：稳定结构不该反复作为自然语言上下文塞给模型，而应该变成 harness 内的可执行原语。

```text
企业工作流
  -> 结构化约束
  -> agent logic
  -> LLM 在更小空间内推理
  -> 工具调用 / 验证 / 升级
```

## 它包括什么

| 类型 | 作用 | 典型场景 |
|------|------|----------|
| 程序分析 | 从代码和系统依赖中提取确定性结构 | 主机代码理解、测试生成、bug repair |
| 知识图谱 | 把服务、指标、事件和依赖关系组织成可遍历结构 | IT incident investigation |
| 策略执行 | 把权限、披露、合规和升级路径变成运行时规则 | 医疗客服、合规自动化 |
| 图结构与 DAG | 把证据链和检查流程固定下来 | 工业资产维护 |
| 自适应规划 | 根据任务状态动态分解和调整路径 | IT compliance modernization |

## 与 Prompt Engineering 的区别

Prompt engineering 把约束写进模型输入；agent logic 把约束写进系统运行时。

这一区别很关键。Prompt 里的规则容易被上下文稀释、被冲突指令覆盖，也难以被独立审计。Agent logic 则可以被测试、版本化、复用和权限控制。

## 价值

- **降低上下文成本**: 让模型只看当前必要证据，而不是吞下整个企业环境。
- **提高正确率**: 用图谱、程序分析和规则引擎减少无约束推理。
- **增强可审计性**: 决策路径可以追溯到规则、图边、证据节点或验证结果。
- **沉淀组织能力**: 一次部署中的流程知识可以回流为下次部署的 harness 资产。

## 关键数据点

- IBM watsonx Code Assistant for Z / App Insights 在最高 1M 行代码、1K 程序任务中，相比 frontier LLM-only baseline 保持略高性能，同时 token 消耗低约 30 倍。
- Aster 测试生成在 75+ 个 IBM CIO Java 应用预生产运行中，将 line / branch / method coverage 从约 20% 提升到约 45%，相对某些 coding agent token 消耗低至约 15 倍。
- Instana I3 在 ITBench 上相对 ReAct agent with GPT-5.1 最高提升 4 倍。
- Maximo Condition Insights 内部 pilot 将资产分析时间从 15-20 分钟降到 15-30 秒，资产覆盖率从约 1% 提升到约 30%。

## 前提与局限性

Agent logic 不等于把所有业务规则写死。过重的逻辑会让系统退回传统自动化，失去 LLM 处理模糊输入、跨域解释和灵活组合的优势。

更准确的原则是：把稳定、可验证、低熵的部分做成逻辑；把开放、语义、跨上下文的部分留给模型。

这些指标主要来自 IBM Research 文章中的 IBM 产品、benchmark 或内部 pilot，适合证明 agent logic 路线的机制价值，但不能直接外推为所有企业、所有工作流的通用收益。

## 关联概念

- [[Agent-Harness]] — Agent logic 的运行位置。
- [[Local-Bounded-Reasoning]] — Agent logic 的推理效果：缩小局部搜索空间。
- [[Policy-as-Code-for-Agent-Governance]] — Agent logic 在治理与合规中的形态。
- [[Graph-Guided-Agent-Investigation]] — Agent logic 在 IT 调查中的形态。
- [[Verifiable-Agent-Engineering]] — Agent logic 的工程质量目标。
