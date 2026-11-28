---
type: entity
title: Structured Agent Memory
aliases:
  - Structured Agent Memory
  - 结构化 Agent 记忆
  - Structured Memory
  - Faceted Agent Memory
definition: "以可检查的属性、适用条件、来源及状态组织Agent记忆，并按实际任务选择相关知识；可与关键词、语义检索和文件存储组合。"
created: 2026-07-08
updated: 2026-11-28
tags:
  - agentic-engineering
  - memory
  - data-systems
evidence_level: medium
claim_type: mixed
related_entities:
  - "[[Multi-Layer-Memory]]"
  - "[[Three-Layer-Agent-Memory]]"
  - "[[Memory-Architecture]]"
  - "[[Context-Engineering]]"
  - "[[Agent-Harness]]"
source_raw:
  - "[[20260707-intelligence-is-free-data-systems-for-of-by-agents]]"
  - "[[20260819-ibm-altk-evolve-memory-dosage]]"
---

# Structured-Agent-Memory（结构化 Agent 记忆）

> [!definition] 定义
> 以属性、适用条件、来源、版本及状态组织记忆，通过结构化约束与其他检索方式选出适用知识。Berkeley的Tk-Boost研究是面向NL2SQL纠正性知识的实例，而非所有结构化记忆的唯一定义。

## 核心问题

原始轨迹、文档与经验可能包含重复、误判或过时信息；将所有内容放入活动上下文有成本及注意力限制。BAIR 2026-07-07观点文章主张面向任务属性选择记忆。文件可包含frontmatter/结构化索引，知识图谱也可执行结构查询，不能将两者统称为不具结构化搜索能力。数据存储与组织、检索算法和知识内容是不同维度。

## Tk-Boost：适用条件与局部纠正

[Agarwal等，Arming Data Agents with Tribal Knowledge（v2，2026-02-17）](https://arxiv.org/html/2602.13521v2) §3–5：

- 从训练查询的错误中提炼纠正陈述及可复用知识，生成适用条件；测试查询独立。
- 四类匹配字段为SQL关键词、表、列及数据类型。每维可设通配或值集合，按各维是否有交集筛选候选，再由LLM结合实际SQL过滤相关性；不是纯确定性召回。
- 初稿形成后提供纠正反馈，可按CTE局部检索与修订；最终SQL需执行并核验正确结果。结构化条件不等于语义正确性或执行授权。
- 原始轨迹仍是核验与重新学习的证据，不应作为无条件操作指令；纠正知识也需适用范围、来源及回归。

## 关键数据点

v2 §6 Table 2–6：各数据集训练/测试分别SQLite 34/101、BigQuery 50/155、Snowflake 29/179、BIRD 72/211；独立经验集，指标取两轮平均。作者概述约25%训练比例，但Snowflake表中为29/208，不能把全部数据集都精确写成25%。

| Spider 2 SQLite / GPT-4.1 | 执行准确率 |
|---|---:|
| 无知识 | 27.7% |
| 全量知识（Table 6a） | 35.6% |
| NL相似度、生成前应用（Table 5） | 31.7% |
| SQL特征匹配、全SQL修订（Table 5） | 39.7% |
| 按CTE检索并修订（Table 5） | 44.6% |

该配置净增16.9个百分点；平均调用12.0→15.9，延迟29.6→37.0秒（Table 3）。论文报告修正及回退的比例，但该段对分母措辞不一致，本轮不将18.1%/1.2%解释为条件成功率。Table 6b经验集大小变化也改变测试集，不作严格同一测试集的剂量因果比较。其他模型/数据集有不同收益，未独立复跑。

## 与其他记忆设计的互补

- [[Multi-Layer-Memory]]、[[Three-Layer-Agent-Memory]]：信息类型、持久性与按需加载可以与属性组织组合，不是严格正交的数学维度。
- [[20260819-ibm-altk-evolve-memory-dosage]]：前轮已校准的AppWorld厂商实验显示知识剂量随模型和任务而变，不保证选择性总是最好。
- 共享状态需明确并发写入、版本、幂等、实际事务与恢复；MVCC、CRDT、共识或补偿是候选工具，不自动提供exactly-once或语义正确性。按规模选择最小机制。

## 前提与局限性

Tk-Boost实证限NL2SQL与其评价协议；适用条件生成、解析、LLM过滤及纠正可能失败。结构化Schema需要维护，开放任务可能需混合检索；多维匹配不保证召回或跨域迁移。2026-11-28回核BAIR本地Raw及论文v2关键章节；不复跑、不新增系统、未完整复核IBM实验。Wiki可使用既有frontmatter、来源定位与适用条件；不因论文结果要求迁移数据库或自动创建新Schema。

## 关联概念

- [[Memory-Architecture]] — 生命周期、组织与评估。
- [[Multi-Layer-Memory]]、[[Three-Layer-Agent-Memory]] — 分层组织。
- [[Context-Engineering]]、[[Agent-Harness]] — 知识按需应用及任务验收。
- [[Shared-Memory-Contamination]] — 写入授权、来源及冲突处理。
