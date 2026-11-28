---
type: entity
title: GBrain
aliases:
  - GBrain
definition: "Garry Tan 构建的 Agent 知识管理系统——混合检索（向量粗筛 + 文件精读）+ 基于规则的图谱实体关系，以 Thin Harness, Fat Skills 为设计哲学"
created: 2026-05-13
updated: 2026-11-28
tags:
  - knowledge-management
  - AI
  - agent
evidence_level: medium
claim_type: mixed
related_entities:
  - "[[LLM-Wiki]]"
  - "[[Obsidian-Wiki]]"
  - "[[Progressive-Disclosure]]"
  - "[[Thin-Harness-Fat-Skills]]"
  - "[[Latent-Space-vs-Deterministic]]"
  - "[[Harness-Engineering]]"
source_raw:
  - "[[深度解析LLM Wiki  Obsidian-Wiki  GBrain：Agent时代知识的“自组织”与“自进化”]]"
---

# GBrain

> [!definition] 定义
> **GBrain** 是由 Y Combinator 总裁兼 CEO Garry Tan 构建的 Agent 知识管理系统。它在 LLM Wiki 的核心思想（文件系统存储 + 渐进式披露）基础上，引入混合检索架构（向量粗筛 + 文件精读）和基于规则的图谱实体关系管理，旨在缓解纯文件检索的规模与关系查询问题；实际收益取决于任务、数据、版本和成本，不能宣称已普遍解决。

## 关键数据点

- **历史基准退役（2026-11-28）**：原页的 49.1% P@5 / 97.9% R@5 及相对 17.7% 的产品优势不再作为有效产品成绩。项目方 [勘误](https://github.com/garrytan/gbrain-evals/blob/main/docs/corrections.md)（Relationships and calibration）确认四种问题模板的正则解析器产生了原表的 49.1% 行，现名 graph-oracle-parse，不是产品评分。原 240 页语料及数字仅用于历史溯源，不能用于产品选型。
- **设计哲学**: Thin Harness, Fat Skills——Harness 做薄，主要精力在丰富 Skills 上
- **核心分工**: 让 LLM 决定"做什么"（Latent Space），让代码保证"在哪里"和"如何做"（Deterministic）
- **架构组成**: 混合搜索（Hybrid Search）+ 分层喂给模型（Layered Feeding）+ 图谱反向链接强制化（Backlink Enforcement）

## 前提与局限性

- 引入向量数据库增加了运维复杂度，背离 LLM Wiki "纯 Markdown" 的极简哲学
- 项目方维护的评测需要检查修订记录、实际被测版本、数据泄漏、分母与对照条件。旧 relationship 结果已有正式勘误，不能仅以样本小解释其有效性问题。
- 图谱提取方式及覆盖随版本变化；旧二手描述不足以确定当前实现。
- 分层读取可能增加往返，也可能减少上下文处理成本；需按同任务的实际端到端时延及质量比较。

## 关联概念

- [[LLM-Wiki]] — GBrain 的思想源头，保留了渐进式披露的核心理念
- [[Obsidian-Wiki]] — 与 GBrain 并行的 LLM Wiki 工程化实现，侧重 Agent 历史摄入
- [[Progressive-Disclosure]] — GBrain 检索流程核心："Chunk 确认 → 整页加载 → 分层呈现"
- [[Thin-Harness-Fat-Skills]] — GBrain 的架构哲学
- [[Latent-Space-vs-Deterministic]] — GBrain 的核心设计洞察
- [[Harness-Engineering]] — 主流把重点放在 Harness Engineering 上，GBrain 反其道而行
- [[RAG-vs-LLM-Wiki]] — GBrain 的混合检索是 RAG 与 LLM Wiki 的折衷方案
