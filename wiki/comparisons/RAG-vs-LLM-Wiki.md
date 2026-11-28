---
type: comparison
title: RAG vs LLM Wiki
created: 2026-04-09
updated: 2026-11-28
evidence_level: medium
claim_type: mixed
tags:
  - comparison
  - knowledge-management
  - llm-wiki
related_entities:
  - '[[Context-Engineering]]'
  - '[[Multi-Layer-Memory]]'
  - '[[Andrej-Karpathy]]'
  - '[[Knowledge-Compilation]]'
  - '[[Memex]]'
source_raw:
  - '[[20260413-llm-wiki]]'
  - '[[一篇文章卖了20万，开源CC+Obsidian打造的LLM Wiki 内容创作3.0系统]]'
  - '[[深度解析LLM Wiki  Obsidian-Wiki  GBrain：Agent时代知识的“自组织”与“自进化”]]'
---

# RAG vs LLM Wiki

> [!summary] 对比概述（2026-11-28 校准）
> 本比较保留“运行时检索与预先知识编译”的有用区分，**退役“RAG 天生无积累、Wiki 天生更正确”的二元命题**。RAG 是查询时引入外部知识的生成机制；LLM Wiki 是持续维护、可审查的知识资产及生命周期。两者不是同层互斥技术。

## 三个独立维度

| 维度 | 基础运行时 RAG | LLM Wiki 的目标 | 组合方式 |
|------|-----------------|----------------|----------|
| 知识持久性 | 原始库及索引可持久；基础检索不自动保存跨源判断 | 持久维护 Entity、Topic、Comparison、Source Summary | RAG 检索 Wiki 与 Raw |
| 综合时机 | 查询时组织相关证据 | 摄取/审查时预编译，查询时仍可综合 | 预计算摘要与查询时综合并存 |
| 治理 | 按实际系统实现版本、来源、更新、权限与评价 | 显式维护知识身份、证据边界、反例和退役 | 检索与知识治理分别验收 |

## 知识累积与代价

基础 chunk RAG 通常需要在每次查询时重新解释相关片段；这不意味着检索索引、缓存、历史回答、记忆或预计算语义结构必须被丢弃。[[GraphRAG]] 的图索引与预生成社区报告，以及 [[GBrain]] 的向量粗筛加文件精读，已提供本库内的反例。GraphRAG 的预计算聚合与 Wiki 的持续知识治理也不等价。

Wiki 的编译有可能降低重复综合成本、帮助发现矛盾与复用判断，却可能引入错误抽象、陈旧前提、重复内容和维护成本。Lint、链接密度、文件完整读取或内部一致性都不能单独证明知识准确。必须以可回溯来源、适用边界、实际查询效用和退役机制检验。

## 查询与维护

| 问题 | 主要策略 | 验收 |
|------|----------|------|
| 最新或低频原始事实 | 检索权威当前来源 | 时效、来源、引用与访问权限 |
| 反复出现的跨来源决策问题 | 编译并维护稳定知识 | 证据独立性、边界、反例与复用 |
| 既需历史综合又需实时事实 | 先定位 Wiki 的判断，再检索原始或最新证据 | 区分当时结论与当前事实 |
| 数据量增长 | 按需选择文本、向量、图或混合索引 | 真实问题集上的召回、质量、延迟、维护及成本 |

## 证据与历史边界

- [[20260413-llm-wiki]] 是 Karpathy 对常见文档检索使用方式的批评及其持久 Wiki 设计；不是所有 RAG 架构的定义或基准实验。
- [[一篇文章卖了20万，开源CC+Obsidian打造的LLM Wiki 内容创作3.0系统]] 是个人创作场景自报；不证明一般查询质量或知识积累速度。
- [[深度解析LLM Wiki  Obsidian-Wiki  GBrain：Agent时代知识的“自组织”与“自进化”]] 提供混合架构与历史测试数字；原页的 P@5、固定规模上限和精度高低排序缺少可比较的任务/数据/成本条件，不再作为普遍选型结论。具体基准回到源材料复核。
- [[Memex]] 是持久关联知识的历史思想先驱。LLM 可以辅助维护，不保证自动解决知识可信度或长期维护成本。

## 相关概念

- [[Context-Engineering]] — 任务上下文的选择与组织。
- [[Multi-Layer-Memory]] — 记忆层次和生命周期。
- [[Knowledge-Compilation]] — 预编译、校准与持久知识治理。
- [[GraphRAG]]、[[GBrain]] — 检索与预计算的组合方案。
- [[Andrej-Karpathy]] — LLM Wiki 设计思想。
