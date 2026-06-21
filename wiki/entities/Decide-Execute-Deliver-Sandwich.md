---
type: entity
title: Decide-Execute-Deliver Sandwich
aliases:
  - Decide-Execute-Deliver 三明治
  - 三明治模型
  - DED 三明治
definition: "将知识工作（特别是软件工程）分解为三个层次的分析框架：Decide（决定做什么）、Execute（执行）、Deliver（交付验证），AI 主要压缩中间的 Execute 层，但两端的 Decide 和 Deliver 层仍然需要人类"
created: 2026-06-22
updated: 2026-06-22
tags:
  - ai-coding
  - knowledge-work
  - productivity
  - labor-market
  - framework
evidence_level: medium
claim_type: extracted
related_entities:
  - "[[Vibe-Coding]]"
  - "[[Agentic-Engineering]]"
  - "[[Jevons-Paradox-for-Knowledge-Work]]"
  - "[[AI-Era-Career-Skills]]"
source_raw:
  - "[[20260615-normaltech-ai-hasnt-replaced-software-engineers]]"
---

# Decide-Execute-Deliver Sandwich

> [!definition] 定义
> 将知识工作（特别是软件工程）分解为三个层次的分析框架：Decide（决定做什么）、Execute（执行）、Deliver（交付验证）。AI 主要压缩中间的 Execute 层，但两端的 Decide 和 Deliver 层仍然需要人类。

## 为什么重要

这个框架解释了为什么 AI 编码能力快速提升，但软件工程师就业没有大幅下降。核心洞察：**代码生成不是瓶颈——决定做什么和验证交付才是**。

## 框架结构

```
┌─────────────────────────────────────┐
│         Decide（决定做什么）         │
│  用户需求、市场信号、组织优先级       │
│  → 需要人类判断，AI 难以替代         │
├─────────────────────────────────────┤
│         Execute（执行）              │
│  写代码、调试、测试                   │
│  → AI 已大幅压缩这一层               │
├─────────────────────────────────────┤
│         Deliver（交付验证）          │
│  验证、测试、问责                     │
│  → 需要人类监督，当前最真实的瓶颈     │
└─────────────────────────────────────┘
  前提：Deep understanding（对系统、业务、环境的理解）
  贯穿三层，是所有工作的基础
```

## 关键证据

- **GitHub 10 万开发者研究**：AI 让代码行数增加 8 倍，但发布量只增加 30%——说明 Execute 层不是瓶颈
- **SWE-chat 数据**：只有 44% 的 AI 生成代码存活到用户提交；vibe-coded 提交引入漏洞的概率是人工的 9 倍
- **Simon Willison 实证**：监督 AI Agent 比自己写代码更累，到上午 11 点就精疲力尽

## 与 Vibe Coding 的关系

NormalTech 区分了两种实践：
- **Vibe Coding**：用户告诉 Agent 做什么，不监督、不审查、不评估——只有 Execute 层
- **Agentic Engineering**：人类保持控制和问责，AI 是工具——完整的三明治

Vibe Coding 的问题不是 AI 能力不足，而是跳过了 Decide 和 Deliver 层。

## Jevons' 悖论

当代码生成成本降低时，人们会写更多软件（价格弹性高）。历史上，程序员就业从 1950 年代的接近零增长到今天的数百万。AI 可能加速这一趋势。

## 前提与局限性

- **行业限制**：框架主要基于软件工程，其他知识工作的适用性需要验证
- **时间限制**：AI 能力仍在快速提升，瓶颈可能会移动
- **假设前提**：假设人类仍然需要对交付负责——如果责任机制改变，框架可能需要调整

## 关联概念

- [[Vibe-Coding]]：跳过 Decide 和 Deliver 层的编码方式
- [[Agentic-Engineering]]：AI 是工具，人类保持控制和问责
- [[Jevons-Paradox-for-Knowledge-Work]]：成本降低导致需求增加
- [[AI-Era-Career-Skills]]：AI 时代需要的新技能
