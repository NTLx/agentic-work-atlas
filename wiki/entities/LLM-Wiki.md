---
type: entity
title: LLM Wiki
aliases:
  - LLM Wiki
  - LLM 知识库
definition: "用 LLM 将文档集合编译为结构化 Wiki 的知识管理范式——三层架构（Raw → Wiki → Schema），LLM 持久维护知识体，人类负责策展与提问"
created: 2026-05-08
updated: 2026-11-28
tags:
  - knowledge-management
  - AI
evidence_level: high
claim_type: mixed
related_entities:
  - "[[Knowledge-Compilation]]"
  - "[[Knowledge-Graph]]"
  - "[[Memex]]"
  - "[[Software-3.0]]"
  - "[[Andrej-Karpathy]]"
  - "[[Obsidian-Wiki]]"
  - "[[GBrain]]"
  - "[[Progressive-Disclosure]]"
source_raw:
  - "[[Andrej Karpathy: From Vibe Coding to Agentic Engineering]]"
  - "[[20260413-llm-wiki]]"
  - "[[深度解析LLM Wiki  Obsidian-Wiki  GBrain：Agent时代知识的“自组织”与“自进化”]]"
---

# LLM Wiki

> [!definition] 定义
> **LLM Wiki** 是 Andrej Karpathy 描述的一种新型知识管理范式：用 LLM 对固定文档集合进行多次"重编译"（recompile）和"重排列"（reorder），每次产生新的信息投影（projection），让人从中获得洞察。其重点是重组并持久维护知识；RAG 则是检索增强生成机制，二者可组合。

## 关键数据点

- **新增能力与历史边界**：LLM 可辅助跨文档综合和维护自然语言知识结构。不能据此否定 LLM 出现前的自动知识抽取、索引、模板及 Wiki 生成方法。
- **Synthetic Data Generation 类比**：Karpathy 将 LLM Wiki 视为对固定数据的"合成数据生成"——不同的投影产生不同的理解
- **人与 LLM 的分工**：LLM 做信息的填充和重排（像 interns 填充细节），人做顶层分类、设计决策和最终理解
- **与 RAG 的关系**：检索增强生成与持久知识编译是可组合的设计维度，见 [[RAG-vs-LLM-Wiki]]。
- **"Outsource thinking, not understanding"**：Karpathy 引用的一条推文——LLM Wiki 帮你思考，但不能替代你的理解

## 前提与局限性

- 需要高质量的源文档集合作为输入
- LLM 输出的重组结构需要人工验证和筛选——LLM 可能产生虚假关联
- 信息的"投影"质量依赖 prompt 设计和编译策略
- 动态知识需要明确时效、有效时间及更新/失效策略；最新权威状态应按需回查，Wiki 不替代实时业务系统。
- Karpathy 原设计以约100来源、数百页面作为 index 可用的经验示例，并建议按需求引入搜索；不是经过规模实验确定的 Markdown 上限。本库已采用 search-first，实际规模能力以真实查询、覆盖、成本和延迟评价。
- 原始设计文档不规定调度器；本库采用独立自动化编排。知识结构与运行时调度是不同职责。

## 工程化演进

LLM Wiki 的理念催生了两个重要的工程化实现：

- **[[Obsidian-Wiki]]**：基于 Skill 的多 Agent 框架，Agent 无关（9+ 种）、Skill 驱动、Obsidian 原生。核心增强包括 Delta 追踪（SHA-256 哈希）、来源可信度边界、溯源标记系统（extracted/inferred/ambiguous）、Agent History Ingest Skills
- **[[GBrain]]**：Y Combinator CEO Garry Tan 构建，引入混合检索（向量粗筛 + 文件精读）旨在缓解检索规模问题，通过基于规则的图谱实体关系管理实现结构化知识图谱。设计哲学为 [[Thin-Harness-Fat-Skills]] 和 [[Latent-Space-vs-Deterministic]]

## 检索 vs 重走：四动作的再巩固性质（07-22 自反投影）

LLM Wiki 作为语义关联架构（wikilink + 语义组织），其 produce 环节有一个结构性风险（synthesized/medium，07-22 圆桌+追本，来源：[[2026-07-22]] 研究日志）：

- **compile 是"走"，链接是足迹**：agent 读 raw、判断、提取、关联，产出的 entity/wikilink 是判断的**有损压缩**——压掉的是判断过程本身（压力、排除项、怀疑）。足迹记得路，不记得走路的力气。
- **检索 ≠ 重走**：produce 若只检索足迹（语义相似页面）而不重走（重读、重判、保留"可否证旧足迹"的权力），因果停止再生——问题不是"检索找相似"，是**检索替代了重走**。
- **因果在干预时刻进入**：只有关联型操作（摘要/链接）的编译只产相似足迹；audit/证伪/冲突标记可检验和撤回因果主张，但审查文本不等于对研究对象实施因果干预（Pearl 因果阶梯：关联是一层，干预是二层，检索不自动爬梯）。
- **produce = 记忆再巩固**：输出回填可能改善解释，也可能传播失真；记忆再巩固仅为类比，不是对 Wiki 因果机制的实证。这解释了 output 的建构性价值（非消费），也解释了失真累积风险。
- **重走者遴选 = 知识级制造共识**：produce 按 agenda 焦点表重走 → 重走 ⊂ agenda 已承认的因果 → agenda 之外的问题可能长期得不到复核，形成选择偏差；不是因果关系不存在（Lippmann "脑中之图"的知识库版本）。对策胚胎：盲区扫描（偶然重走）+ 冲突标记（多图冲突驯服因果循环）。

## 关联概念

- [[Knowledge-Compilation]] — LLM Wiki 的核心操作：编译
- [[Knowledge-Graph]] — LLM Wiki 的结构化表示
- [[Memex]] — Vannevar Bush 1945 年提出的信息关联愿景，LLM Wiki 是其 AI 增强版
- [[Software-3.0]] — LLM Wiki 是 Software 3.0 在知识管理中的应用
- [[RAG-vs-LLM-Wiki]] — 检索增强与知识治理的互补关系
- [[Obsidian-Wiki]] — LLM Wiki 的工程化实现（Agent 历史摄入 + Skill 系统）
- [[GBrain]] — LLM Wiki 的工程化实现（混合检索 + 图谱关系）
- [[Progressive-Disclosure]] — LLM Wiki 的核心知识组织机制
