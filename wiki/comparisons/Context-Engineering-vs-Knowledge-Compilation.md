---
type: comparison
title: "Context Engineering vs Knowledge Compilation"
entity_a: "[[Context-Engineering]]"
entity_b: "[[Knowledge-Compilation]]"
created: 2026-05-24
updated: 2026-05-24
tags:
  - comparison
  - context-engineering
  - llm-wiki
related_entities:
  - "[[Context-Engineering]]"
  - "[[Knowledge-Compilation]]"
  - "[[LLM-Wiki]]"
  - "[[Agent-Knowledge-Management]]"
  - "[[Progressive-Disclosure]]"
  - "[[Multi-Layer-Memory]]"
  - "[[RAG-vs-LLM-Wiki]]"
source_raw:
  - "[[20260413-llm-wiki]]"
  - "[[一篇文章卖了20万，开源CC+Obsidian打造的LLM Wiki 内容创作3.0系统]]"
  - "[[深度解析LLM Wiki  Obsidian-Wiki  GBrain：Agent时代知识的“自组织”与“自进化”]]"
---

# Context Engineering vs Knowledge Compilation

> [!summary] 对比概述
> Context Engineering 解决“这一次任务应该让模型看到什么”；Knowledge Compilation 解决“原始材料如何被转化为以后可复用的知识中间层”。前者是运行时输入工程，后者是摄取时知识工程。

## 核心维度对比

| 维度 | Context Engineering | Knowledge Compilation |
|------|---------------------|-----------------------|
| 核心问题 | 当次推理需要哪些上下文 | 原始材料如何沉淀为稳定知识 |
| 发生时机 | 运行时、任务执行中 | 摄取时、整理时、审计时 |
| 输入 | 当前任务、用户问题、检索片段、工具结果 | raw source、笔记、文章、论文、输出反馈 |
| 输出 | 模型上下文窗口中的有效材料 | entity、topic、comparison、source summary |
| 优化目标 | 降低噪声、避免遗漏、提高当次回答质量 | 避免重复理解、积累概念边界、支持未来复用 |
| 失败形态 | 上下文太多、太少、过期或不相关 | 总结化、孤立化、无证据、概念边界不清 |
| 典型机制 | 检索、压缩、懒加载、工具调用、prompt 组织 | 编译摘要、概念抽取、对比页、回填检查、lint |

## 本质区别

Context Engineering 把重点放在**模型这一轮看见什么**。它的目标是让模型在有限上下文窗口里拿到最相关、最少噪声、最适合当前任务的材料。

Knowledge Compilation 把重点放在**知识以后如何复用**。它不是把 source 摘短，而是把 source 转化为可查询、可链接、可审计、可继续演化的知识结构。

简单说：

- Context Engineering 是给模型配餐。
- Knowledge Compilation 是建设厨房、菜谱和食材库。

## 与 RAG 和 LLM Wiki 的关系

[[RAG-vs-LLM-Wiki]] 已经说明：RAG 通常在查询时临时取回材料，LLM Wiki 则在摄取时提前编译知识。

Context Engineering 与 RAG 更接近，因为它关注运行时材料选择。但好的 LLM Wiki 也需要 Context Engineering：当用户提问时，系统仍要决定加载哪些 entity、topic、comparison 和 raw source。

Knowledge Compilation 与 LLM Wiki 更接近，因为它关注 raw 到 wiki 的结构转化。没有这一层，系统每次都要重新读原文、重新抽概念、重新判断边界。

## 两者如何配合

```text
raw source
  -> Knowledge Compilation
  -> entity / topic / comparison
  -> Context Engineering
  -> 当前回答、output 或决策 memo
  -> 回填检查
  -> 继续编译或修正 wiki
```

Knowledge Compilation 降低未来理解成本；Context Engineering 降低当次推理成本。一个负责长期复利，一个负责即时表现。

## 反模式

### 用更长上下文替代知识编译

上下文窗口变长不等于知识结构变好。如果每次都把原文塞给模型，系统仍然没有积累概念边界、冲突标记和可复用判断。

### 把知识编译写成普通摘要

编译不是摘要。摘要只压缩内容，编译要抽出概念、前提、局限、关系和可复用判断。一个好的 entity 页面应让以后回答问题时不用重读原文。

### 只做 Wiki 不做上下文选择

Wiki 页多了以后，仍然需要选择机制。否则模型会在过多页面之间迷失，或者把弱相关概念混在一起。

## 选择指南

优先投入 Context Engineering，当：

- Agent 当次任务经常遗漏关键信息。
- 检索结果噪声大，模型容易被无关材料带偏。
- 工具调用、文件加载、上下文压缩成为主要瓶颈。

优先投入 Knowledge Compilation，当：

- 同一批 source 被反复重读。
- 概念边界反复混淆。
- 输出中新判断无法回链。
- raw source 很多，但 entity、topic、comparison 层无法支撑回答。

成熟知识系统需要两层同时存在：编译层负责长期记忆，上下文层负责即时调度。

## 相关概念

- [[Context-Engineering]] — 管理模型当前可见材料的工程实践。
- [[Knowledge-Compilation]] — 把 raw source 转为可复用 Wiki 知识的过程。
- [[LLM-Wiki]] — 用 LLM 维护和演化的结构化知识库。
- [[Agent-Knowledge-Management]] — Agent 知识自组织与自进化主题。
- [[Progressive-Disclosure]] — 根据任务动态加载知识的策略。
- [[Multi-Layer-Memory]] — Agent 记忆系统的多层结构。

