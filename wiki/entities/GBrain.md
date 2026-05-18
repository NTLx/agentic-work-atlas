---
type: entity
title: GBrain
aliases:
  - GBrain
definition: "Garry Tan 构建的 Agent 知识管理系统——混合检索（向量粗筛 + 文件精读）+ 基于规则的图谱实体关系，以 Thin Harness, Fat Skills 为设计哲学"
created: 2026-05-13
updated: 2026-05-13
tags:
  - knowledge-management
  - AI
  - agent
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
> **GBrain** 是由 Y Combinator 总裁兼 CEO Garry Tan 构建的 Agent 知识管理系统。它在 LLM Wiki 的核心思想（文件系统存储 + 渐进式披露）基础上，引入混合检索架构（向量粗筛 + 文件精读）和基于规则的图谱实体关系管理，解决了纯 Markdown Wiki 在规模膨胀后的检索性能瓶颈。

## 关键数据点

- **P@5 提升**: 带图谱的 GBrain P@5 达 49.1%，仅混合搜索（无图谱）为 17.7%，差距 +31.4pp；R@5 达 97.9%
- **Benchmark 规模**: 240 页富文本语料库测试
- **设计哲学**: Thin Harness, Fat Skills——Harness 做薄，主要精力在丰富 Skills 上
- **核心分工**: 让 LLM 决定"做什么"（Latent Space），让代码保证"在哪里"和"如何做"（Deterministic）
- **架构组成**: 混合搜索（Hybrid Search）+ 分层喂给模型（Layered Feeding）+ 图谱反向链接强制化（Backlink Enforcement）

## 前提与局限性

- 引入向量数据库增加了运维复杂度，背离 LLM Wiki "纯 Markdown" 的极简哲学
- Benchmark 数据来自项目自身，240 页规模与实际企业场景差距较大，可能存在选择性报告偏差
- 图谱构建依赖正则和关键词模式匹配而非 NER，在非结构化文本中的召回率有限
- 渐进式披露增加了工具调用和文档读取的时间开销，响应速度比 RAG 慢

## 关联概念

- [[LLM-Wiki]] — GBrain 的思想源头，保留了渐进式披露的核心理念
- [[Obsidian-Wiki]] — 与 GBrain 并行的 LLM Wiki 工程化实现，侧重 Agent 历史摄入
- [[Progressive-Disclosure]] — GBrain 检索流程核心："Chunk 确认 → 整页加载 → 分层呈现"
- [[Thin-Harness-Fat-Skills]] — GBrain 的架构哲学
- [[Latent-Space-vs-Deterministic]] — GBrain 的核心设计洞察
- [[Harness-Engineering]] — 主流把重点放在 Harness Engineering 上，GBrain 反其道而行
- [[RAG-vs-LLM-Wiki]] — GBrain 的混合检索是 RAG 与 LLM Wiki 的折衷方案
