---
type: entity
title: Jagged Intelligence
aliases:
  - Jagged Intelligence
  - 锯齿状智能
definition: "LLM 能力在不同任务和领域之间高度不均匀分布的现象，强项和弱项会像锯齿边缘一样并存"
created: 2026-05-08
updated: 2026-05-26
tags:
  - AI
  - LLM
  - cognitive-science
evidence_level: medium
claim_type: mixed
related_entities:
  - "[[Verifiability]]"
  - "[[Ghost-Intelligence]]"
  - "[[AI-Capability-Gap]]"
  - "[[AI-Psychosis]]"
  - "[[Andrej-Karpathy]]"
  - "[[AI-Restraint]]"
source_raw:
  - "[[Andrej Karpathy: From Vibe Coding to Agentic Engineering]]"
---

# Jagged Intelligence（锯齿状智能）

> [!definition] 定义
> LLM 能力在不同任务和领域之间高度不均匀分布的现象，强项和弱项会像锯齿边缘一样并存

## 为什么重要

Jagged Intelligence 是理解 AI 能力争论的核心概念。它说明"AI 很强"和"AI 很蠢"可以同时成立，因为模型能力不是均匀铺开的。

在可验证、训练投入高、经济价值大的领域，例如代码、数学、漏洞复现和测试驱动任务，模型可能表现极强。在常识、实体状态、社会语境、责任判断和训练回路外任务中，它仍可能犯低级错误。

这直接影响 Agent 设计。不能因为模型在代码任务上很强，就默认它在产品判断、权限决策、社会后果和常识推理上同样稳健。每个任务都要重新问：它是否在模型的高峰区域，是否有外部验证，失败代价是什么。

## 关键数据点

- **洗车案例**：Opus 4.7 能重构 10 万行代码库、发现零日漏洞，却建议你"走路去 50 米外的洗车店"——忽略了车不能走路这一基本常识
- **草莓问题**：LLM 长期无法正确回答"strawberry 中有几个 r"，后被针对性修补
- **象棋跃迁**：GPT-3.5 → GPT-4 期间象棋能力大幅提升，不是因为模型全面变强，而是因为有人把大量棋谱数据加入了预训练集
- **RL 回路效应**：如果你在 RL 训练回路中，你飞；如果你在回路之外，你挣扎
- **经济投入效应**：实验室会优先优化高价值、可验证、可规模化评测的领域，能力分布因此更不均匀。

## 使用原则

- 不按模型整体名声判断任务风险，而按具体任务是否可验证判断。
- 对高峰领域仍保留测试和 review，因为强项也可能在边界处断裂。
- 对低谷领域提供更多上下文、工具、人工确认或拒绝机制。
- 对跨领域任务拆分处理，避免让模型把代码能力外推到业务、法律、医疗或组织判断。

## 前提与局限性

- 锯齿状的分布取决于训练数据分布和 RL 环境覆盖范围，不是模型的内在固定属性
- 随着新模型发布，旧的"锯齿缺口"可能被修补（如草莓问题），新的缺口可能产生
- 理解锯齿状的形态对具体应用场景至关重要——不能说"AI 很强"或"AI 很弱"，要看具体在哪个回路里
- 这个概念不等于悲观判断。它要求更精确地匹配任务、验证方式和权限边界。

## 关联概念

- [[Verifiability]] — 锯齿状的根源：RLVR 只在可验证的领域有效
- [[Ghost-Intelligence]] — 幽灵比喻：LLM 不是全能的动物智能
- [[AI-Capability-Gap]] — 不同用户群体因体验不同而产生的认知鸿沟
- [[AI-Psychosis]] — 深度使用前沿 agentic 模型的用户因看到锯齿状高峰而产生的震撼感
- [[AI-Restraint]] — 任务落在低谷或不可验证区域时，需要停手、求证或转人工
