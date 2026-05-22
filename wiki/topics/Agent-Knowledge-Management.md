---
type: topic
title: "Agent 知识管理与自进化"
created: 2026-05-13
updated: 2026-05-23
tags:
  - knowledge-management
  - AI
  - agent
  - topic
related_entities:
  - "[[LLM-Wiki]]"
  - "[[GBrain]]"
  - "[[Obsidian-Wiki]]"
  - "[[Progressive-Disclosure]]"
  - "[[Thin-Harness-Fat-Skills]]"
  - "[[Latent-Space-vs-Deterministic]]"
  - "[[Harness-Engineering]]"
  - "[[Knowledge-Compilation]]"
  - "[[Memex]]"
source_raw:
  - "[[深度解析LLM Wiki  Obsidian-Wiki  GBrain：Agent时代知识的“自组织”与“自进化”]]"
  - "[[Demis Hassabis: Agents, AGI & The Next Big Scientific Breakthrough]]"
---

# Agent 知识管理与自进化

> [!summary] 主题概述
> Agent 知识管理正从 RAG 的"每次查询从头检索"向 LLM Wiki 的"编译一次、持续更新"范式转变。LLM Wiki、Obsidian-Wiki、GBrain 代表了三种知识自组织与自进化的技术路径——从极简的纯 Markdown 方案到工程化的混合检索架构。

## 从 RAG 到 LLM Wiki：范式转变

传统 RAG 是"带着书本进考场"——每次查询临时检索、生成、丢弃，知识无累积。LLM Wiki 则是"把书读透并记成整理后的笔记"——知识在摄入阶段就被编译为结构化 Wiki，交叉引用已建立、矛盾已标记、综合分析已反映所有读过内容。

参见 [[RAG-vs-LLM-Wiki]]

## LLM Wiki 的三层架构

1. **Raw Sources（原始资料层）**：只读存档区，LLM 读取但永不修改
2. **Wiki 层**：按主题/人物/概念组织的结构化知识页面，LLM 全权维护
3. **Schema（规则层）**：定义系统运行规则和约定的元指令文件

核心操作闭环：**Ingest（摄入）→ Query（查询）→ Lint（维护）**

## 三种工程化实现

### LLM Wiki（Karpathy）
- 纯 Markdown 文件 + Schema 指导
- 极简哲学，零依赖
- 适合个人/小团队、规模可控的知识场景
- 参见 [[LLM-Wiki]]

### Obsidian-Wiki
- 基于 Skill 的多 Agent 框架
- Agent 无关（9+ 种 Agent 支持）
- 核心创新：Agent History Ingest（自动扫描历史记录）、Delta 追踪、溯源标记
- 参见 [[Obsidian-Wiki]]

### GBrain（Garry Tan）
- 混合检索架构：向量粗筛 + 文件精读
- 基于规则的图谱实体关系管理
- 设计哲学：[[Thin-Harness-Fat-Skills]]、[[Latent-Space-vs-Deterministic]]
- 适合中大规模场景
- 参见 [[GBrain]]

## 知识自进化的路径

### 轻量级路径：Skillify / 渐进式披露
- 通过 Skill 机制实现 Agent 自进化
- 将非结构化知识转化为可被 Agent 高效调用的结构化资产
- 代价：响应速度比 RAG 慢
- 参见 [[Progressive-Disclosure]]

### 重量级路径：RL 训练
- 通过强化学习深度训练模型
- 门槛和成本高，面向研究人员和特定 Benchmark 优化

### 最佳实践：混合架构
- 向量检索/关键词索引解决"找得快"
- 大模型渐进式披露解决"答得准"和"记得牢"
- 离线自我迭代保持知识新鲜度

## 长期记忆仍是 Agent 的硬缺口

Demis Hassabis 的 AGI 访谈从另一个方向支持了这个 Topic：当前模型仍缺持续学习、长期推理和一致性。把所有内容塞进百万 token context window 不是长期记忆，只是更大的工作记忆；它会把不重要、错误或过时的信息也一起塞进去，检索和判断成本仍然存在。

因此，Agent 知识管理不能只追求更长上下文。更稳的方向是把 raw source、编译后的 wiki、检索索引、专用工具和人类策展分层组织起来。Hassabis 提到的 [[Tool-Use-Architecture|Tool-Use Architecture]] 也指向同一结构：通用模型不应把所有专业知识塞进一个巨大脑袋，而应成为专用系统和知识工具的协调者。

## 人类角色的转变

在 LLM Wiki 范式下，人类的角色从"知识维护者"转变为"知识策展人"：

- **策展来源**：选择有价值的信息源
- **引导分析**：提出好问题，指导 LLM 的编译方向
- **最终理解**：LLM 负责信息填充和重排，人负责顶层判断

> [!quote] Karpathy
> Obsidian is the IDE; the LLM is the programmer; the wiki is the codebase.

## 思想渊源

- [[Memex]] — Vannevar Bush 1945 年的个人知识存储愿景，LLM Wiki 的思想先驱
- Bush 未能解决"谁来维护"的问题——LLM 解决了

---

*本主题页面整合自飞樰《深度解析 LLM Wiki / Obsidian-Wiki / GBrain》一文，由 LLM Wiki 编译流程生成。*
