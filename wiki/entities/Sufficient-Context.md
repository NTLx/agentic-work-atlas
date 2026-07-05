---
type: entity
title: Sufficient Context
aliases:
  - Sufficient Context
  - 上下文充分性
  - Sufficient Context Agent
definition: "在生成答案前判断当前证据是否足以完整回答原问题，并在不足时明确缺口、继续检索或拒答的运行时验证机制"
created: 2026-06-06
updated: 2026-06-16
evidence_level: medium
claim_type: mixed
tags:
  - RAG
  - verification
  - context-engineering
related_entities:
  - "[[Corrective-RAG]]"
  - "[[Verifiable-Agent-Engineering]]"
  - "[[Agent-Harness]]"
  - "[[Context-Engineering]]"
  - "[[Reflexion]]"
source_raw:
  - "[[20260606-google-agentic-rag]]"
  - "[[20260630-loop-engineering-andrew-ng]]"
---

# Sufficient Context（上下文充分性）

> [!definition] 定义
> **Sufficient Context** 是一种运行时验证机制：系统不只检查“检索到了什么”，而是检查“这些材料是否已经足够回答原问题”。如果不够，它必须指出缺口、继续搜索，或返回拒答，而不是让模型凭不完整证据硬答。

## 关键数据点

- Google 的 agentic RAG 在 planner、query rewriter 和 search fanout 之后，引入专门的 sufficient context agent 审查 retrieved snippets、intermediate draft 和 missing pieces analysis。
- 该机制要求系统输出明确的 `Reason` 与 `Feedback`，把“为什么不够”结构化为下一轮检索输入。
- 在 FramesQA 上，文中报告相对 standard RAG 的 factuality 最高提升 34%；在 4 个语料库的 cross-corpus 设置中准确率 90.1%，延迟与 single-corpus 版本接近。

## 为什么重要

传统 RAG 默认“有相关文档”就足以生成答案。Sufficient Context 改写了这个假设：相关不等于充分，命中文档不等于答案闭环。对于企业知识系统，真正常见的失败不是完全找不到，而是找到第一段线索后就过早停止。

因此它把 RAG 的成功条件从“检索命中”推进到“证据闭环”：

1. 找到候选线索。
2. 判断这些线索是否覆盖原问题所需的所有关键字段。
3. 明确缺口是什么。
4. 继续检索、改写查询，或安全拒答。

## 与相邻概念的边界

| 概念 | 它解决什么 | 与 Sufficient Context 的区别 |
|------|------------|------------------------------|
| [[Corrective-RAG|Corrective RAG]] | 检索结果是否相关 | Sufficient Context 进一步问“即使相关，是否已经够回答” |
| [[Context-Engineering|Context Engineering]] | 如何组织输入材料 | Sufficient Context 是运行时闸门，不是静态上下文打包策略 |
| [[Reflexion]] | 生成后如何自我修正 | Sufficient Context 发生在最终回答前，重点是证据是否充足 |
| [[Verifiability|Verifiability]] | 输出是否可判断对错 | Sufficient Context 把可验证性前移到证据层 |

## 失败模式

- **过早满足**: 系统拿到部分证据就误判“足够”，输出貌似完整但关键字段缺失的答案。
- **缺口描述含糊**: 知道不够，但不能把缺什么结构化为下一轮可执行查询。
- **无限检索循环**: 一直判断不够，却没有清晰的停机或拒答条件。
- **证据过量**: 为了追求“充分”，把大量无关材料塞进上下文，反而稀释关键信号。

## 前提与局限性

- 需要系统能枚举“完整回答”所需的关键槽位或子问题；否则“充分”很容易退化成主观判断。
- 充分性审查本身也可能幻觉化，因此最好与 schema、字段检查、来源约束或人工门控结合。
- 对开放式创作任务，“充分上下文”往往没有清晰边界，这个概念更适合事实性、检索性、流程性任务。

## 关联概念

- [[Corrective-RAG]] — 先纠正相关性，再判断充分性
- [[Verifiable-Agent-Engineering]] — 把验证前移到上下文层
- [[Agent-Harness]] — 需要运行时协调继续检索、重写或拒答
- [[Context-Engineering]] — 为充分性检查提供可读、可评估的上下文结构
