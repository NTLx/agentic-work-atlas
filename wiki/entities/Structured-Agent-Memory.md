---
type: entity
title: Structured Agent Memory
aliases:
  - Structured Agent Memory
  - 结构化 Agent 记忆
  - Structured Memory
  - Faceted Agent Memory
definition: "按多属性维度（模块、语言、操作类型等）组织的纠正性记忆，通过属性匹配而非关键词/向量检索来精确召回相关知识。区别于无结构 Markdown 文件 + embedding 检索的范式。"
created: 2026-07-08
updated: 2026-07-08
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
---

# Structured-Agent-Memory（结构化 Agent 记忆）

> [!definition] 定义
> **Structured Agent Memory** 是按多属性维度组织的纠正性记忆系统，通过属性匹配（而非关键词或向量检索）精确召回与当前任务相关的知识。每个记忆条目携带结构化标签（如模块名、语言、操作类型、失败模式），以及纠正性指令。

## 核心问题：为什么 "Files Are All You Need" 不够

当前 agent 记忆的主流范式是无结构 Markdown 文件 + grep/embedding 检索。Berkeley AI Research 指出三个结构性瓶颈：

1. **Context window 有限**：检索所有相关 MD 片段塞入 context 终将崩溃
2. **延迟成本**：即使 context 够大，全量检索的延迟不可接受
3. **不可序列化**：大型数据库、代码库不可能序列化进 context

知识图谱（KG）同样受限——缺乏结构化搜索能力，仍然依赖关键词或 embedding 相似度。

## 结构化记忆的设计

### 多属性组织

每个记忆条目携带结构化属性，每个属性可设为：
- `*`：普遍适用
- 具体值列表：仅在匹配时召回

**示例**（数据 agent 场景）：

| 属性 | 示例值 |
|------|--------|
| SQL 关键词 | `JOIN`, `GROUP BY` |
| 表名 | `orders`, `products` |
| 列名 | `product_name` |
| 操作类型 | date-time operations |
| 纠正性指令 | "when performing date-time operations, use fiscal year not calendar year" |

### 与分层记忆的互补

> [!tip] 两个正交维度
> - **[[Multi-Layer-Memory|分层记忆]]** 解决 **时间问题**：何时存、何时忘、何时从短期晋升到长期
> - **结构化记忆** 解决 **空间问题**：什么维度的知识与当前任务相关
> 
> 两者可组合：每一层记忆都可采用结构化组织，而非只有顶层才结构化。

### 纠正性 vs 原始轨迹

原始 agent trace（包含错误）不适合作为记忆——它会诱导 agent 重复同样错误。结构化记忆存储的是**纠正性知识**（corrective instructions），而非原始执行日志。

### 应用特定 Schema

一个开放问题是如何定义**应用特定的结构化记忆 schema**（作者称之为 "world models for memory"）。类比：为每个应用定义一个 schema，agent 自身可以帮助定义和迭代这个 schema。

## 规模化时的额外挑战

当数千 agent 共享结构化记忆时，还需要解决：

| 挑战 | 相关技术 |
|------|---------|
| 并发编辑 | MVCC、copy-on-write、CRDTs |
| 大规模回滚 | Exactly-once semantics |
| Livelock 避免 | 语义级补偿（agent 能推理回滚原因） |
| 记忆冲突 | 共识机制（agent 间协商 schema 定义） |
| 过时知识 | 进化框架 + 结构化记忆驱动的自我改进 |

## 关键数据点

| 指标 | 数据 |
|------|------|
| 作者 | Berkeley EPIC Data Lab (Parameswaran et al.) |
| 论文 | arxiv:2602.13521 |
| 记忆维度示例 | 列名、表名、操作类型、自然语言纠正指令 |
| 替代方案 | MD 文件 + grep/embedding、知识图谱 |
| 核心差异 | 属性匹配 vs 关键词/向量匹配 |

## 前提与局限性

- 多属性匹配需要预定义 schema——在开放域知识工作中可能不可行
- 作者承认 "application-specific structured memory" 是 open question
- MD + embedding 的"粗暴"方式之所以流行，恰恰因为它不需要预定义 schema
- 结构化记忆的 schema 定义成本可能高于其在小规模场景的收益
- 仅数据 agent 场景有实验验证，通用知识工作场景未测试

## 关联概念

- [[Multi-Layer-Memory]] — 时间维度的记忆分层，与结构化记忆正交互补
- [[Three-Layer-Agent-Memory]] — 另一种记忆架构视角
- [[Memory-Architecture]] — 记忆系统的整体架构设计
- [[Context-Engineering]] — 结构化记忆是 context engineering 的数据源
- [[Agent-Harness]] — harness 需要管理结构化记忆的读写和一致性
