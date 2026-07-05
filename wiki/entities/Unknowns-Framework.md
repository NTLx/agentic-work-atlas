---
type: entity
title: Unknowns Framework
aliases:
  - Unknowns Framework
  - 未知物框架
  - Rumsfeld Matrix for Agentic Coding
definition: "Thariq Shihipar (2026) 将 Rumsfeld 的 Known/Unknown 矩阵应用于 Agentic Coding：将工作分解为 Known Knowns（prompt 中已写明）、Known Unknowns（知道自己不知道）、Unknown Knowns（太显然不会写下来但看到就认得出）、Unknown Unknowns（完全未考虑的维度）。Fable 5 是第一个让工作质量瓶颈从模型能力转移到用户澄清未知物能力的模型"
created: 2026-07-05
updated: 2026-07-05
tags:
  - agentic-engineering
  - AI-Agent
  - human-skill
evidence_level: medium
claim_type: extracted
related_entities:
  - "[[Agentic-Engineering]]"
  - "[[Captain-Mindset]]"
  - "[[Context-Engineering]]"
  - "[[Skill-Chains]]"
  - "[[Tacit-Knowledge-Lock-In]]"
source_raw:
  - "[[20260703-fable-field-guide-finding-unknowns]]"
---

# Unknowns Framework（未知物框架）

> [!definition] 定义
> **Unknowns Framework** 是 Thariq Shihipar（2026-07-03）将 Rumsfeld 的 Known/Unknown 认知矩阵应用于 Agentic Coding 的实践框架。核心理念：**Agentic Coding 的核心技能不是 prompt engineering，而是发现和管理未知物的能力**——地图（prompt/skills/context）与领土（代码库/真实约束）之间的差距就是"未知物"。

## 四象限

| 象限 | 定义 | 例子 | 应对技术 |
|------|------|------|---------|
| **Known Knowns** | Prompt 中已写明的内容 | "我要加一个 auth provider" | 直接实现 |
| **Known Unknowns** | 知道自己还没想清楚 | "我知道需要处理 rate limiting，但不知道具体策略" | Interview、Implementation Plan |
| **Unknown Knowns** | 太显然不会写下来，但看到就认得出 | "这个按钮位置不对"——在脑子里有标准但没说出来 | Brainstorm、Prototype |
| **Unknown Unknowns** | 完全未考虑的维度 | 不知道 color grading 是什么但需要调色视频 | Blind Spot Pass、Reference |

## 全周期技术矩阵

### 实现前
- **Blind Spot Pass**：直接问 Claude "帮我找出我的 Unknown Unknowns"——让 Agent 主动搜索代码库和互联网帮你发现盲区
- **Brainstorm + Prototype**：针对 Unknown Knowns——通过快速原型把"看到才认得出"的标准显性化
- **Interview**：让 Claude 逐个提问，优先问"答案会改变架构"的模糊点
- **Reference**：当无法用语言描述时，指向源码/设计/文档作为参考
- **Implementation Plan**：让 Claude 写出计划，但把"最可能被修改的决策"（数据模型、类型接口、UX 流程）放在前面

### 实现中
- **Implementation Notes**：在临时文件中记录偏差，选择保守方案并继续——供下次尝试学习

### 实现后
- **Pitch + Explainer**：打包原型、spec、实现笔记为单一文档，加速审查者理解（他们从你同样的未知物开始）
- **Quiz**：Claude 生成变更报告 + 测验，只有通过测验后才 merge——同时是知识转移和质量门禁

## 核心洞察

1. **Fable 5 是第一个瓶颈转移的模型**：之前模型能力是瓶颈，Fable 5 让"用户澄清未知物的能力"成为瓶颈
2. **最好的 Agentic Coder 相对未知物很少**：他们与代码库和模型行为深度同步，但即使他们也假设未知物存在
3. **减少和规划未知物是可以练习的技能**：每次 brainstorm、interview、prototype、reference 都是"在修复变贵之前发现你不知道的东西"
4. **指令颗粒度的平衡**：过细→Agent 无法在必要时转向；过粗→Agent 按行业惯例做不适合的假设

## 关键数据点

- Thariq Shihipar 用 Fable 5 + Claude Code 完全编辑了 Fable 发布视频，从零学习视频编辑、转录、调色（2026-07-03）
- 作者引用 Boris Cherny（Claude Code 作者）和 Jarred Sumner 作为"未知物极少"的标杆
- 盲点扫描（Blind Spot Pass）使用字面词 "blindspot pass" 和 "unknown unknowns" 触发

## 前提与局限性

- **框架普适性**：Rumsfeld 矩阵是认知框架而非工程方法，映射到 Agentic Coding 是创造性应用。四象限之间的边界在实践中可能模糊
- **Quiz 验证局限**：测验可能无法覆盖深层逻辑错误或跨模块副作用
- **Fable 5 特殊性**：作者称 Fable 5 是"第一个"转移瓶颈的模型，但未对比其他模型——可能受近期体验偏差影响
- **单源**：目前仅来自 Thariq Shihipar 一篇文章，需要更多来源验证框架的普适性

## 关联概念

- [[Agentic-Engineering]] — Unknowns Framework 是 Agentic Coding 的核心技能框架
- [[Captain-Mindset]] — 船长思维要求人类在规划和质量层面投入，Unknowns Framework 给出了具体操作技术
- [[Context-Engineering]] — 未知物本质上是"context 的缺口"——Context Engineering 的目标是系统性填补这些缺口
- [[Skill-Chains]] — Interview/Quiz/Blind Spot Pass 等技术可以沉淀为可复用的 Skill
- [[Tacit-Knowledge-Lock-In]] — "Unknown Knowns"（太显然不写下来）直接对应隐性知识——框架的核心贡献是让隐性知识显性化可操作