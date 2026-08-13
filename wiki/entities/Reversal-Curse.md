---
type: entity
title: Reversal-Curse
aliases:
  - 反转诅咒
  - Reversal Curse
  - 逆向问题失败
definition: "LLM 训练中见过'A 是 B'（如 Oasis 在 Boardwalk 首演）却答不出'什么是 B'（谁在 Boardwalk 首演）的现象——曾被归因于自回归目标/双向编码缺失，知识画像研究将其再框架为 recall（取用）不对称而非知识缺失"
created: 2026-08-13
updated: 2026-08-13
evidence_level: high
claim_type: mixed
tags:
  - llm-memory
  - factuality
  - evaluation
related_entities:
  - "[[Knowledge-Profiling]]"
  - "[[Verifiability]]"
  - "[[Memory-Architecture]]"
source_raw:
  - "[[20260215-recall-bottleneck-parametric-factuality]]"
  - "[[20260812-google-recall-bottleneck-factuality]]"
---

# Reversal Curse（反转诅咒）

> [!definition] 定义
> **Reversal Curse（反转诅咒）** 指 LLM 记住了 "A 是 B"（ordered pair）却答不出反向问题 "B 是什么" 的现象（Berglund et al., 2024）。它暴露了模型表达知识时的方向不对称：知识以被见到的方式存储，查询方向偏离训练时的关系顺序时取用失败。

## 再框架：从"学习失败"到"取用失败"

既有解释集中于 pre-training 侧：自回归目标（factorization curse）、训练动态、数据不对称，解法多为 pre-training 修改或架构改动。知识画像研究（ICML 2026）给出新证据，主张它本质上是 recall 问题：

- **识别-生成分离**：在 open-ended generation（recall）中反向问题显著更难；在 multiple-choice verification（recognition）中反向问题不再更难、甚至更易。能识别（distractor 中认出正确答案）却生成不出 → 双向知识并非缺失，而是查询方向偏离训练呈现时取用失败。
- **thinking 可缓解**：thinking 对反向问题的收益大于直接问题——为不依赖 pre-training 解法提供新路径。

## 含义

- 对评测：准确率把 encoding 与 recall 混为一谈，reversal curse 是这一混淆的典型样本。
- 对 RAG/Agent：reversal 类查询不可简单归因于"模型没学"，用检索或改写补取用成本更低（综合判断）。

## 关键数据点

- 概念首提：Berglund et al. (2024)
- 识别-生成分离：多选识别中反向问题不再更难（甚至更易），开放生成中反向显著更难
- thinking 对反向问题的收益大于直接问题

## 前提与局限性

- 识别-生成分离基于 WikiProfile（Wikipedia 单跳事实）；复杂多跳场景未验证。
- "recall 而非双向编码缺失"是对既有机制（factorization curse 等）的重解释，非严格证伪——两者可在不同条件中共存。
- 单一研究来源，等待独立复现（尤其跨语言）。

## 关联概念

- [[Knowledge-Profiling]] — 提供分离 encoding/recall 的诊断框架
- [[Verifiability]] — 识别（可验证、多选）vs 生成（开放 recall）的能力分层
- [[Memory-Architecture]] — 存储与取用分离是记忆系统设计的基础区分
- [[Structured-Agent-Memory]] — 结构化匹配解决"取用"维度，与"存储"正交