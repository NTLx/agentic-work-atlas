---
type: entity
title: Agent Harness Engineering
aliases:
  - Agent Harness Engineering
  - Harness Engineering
  - agent harness
definition: "围绕 Agent 模型的脚手架工程——提示词、工具、沙箱、反馈环等环绕结构的设计；与 Agent Harness 的关系是：Harness Engineering 是工程方法论，Agent Harness 是产出物"
created: "2026-08-17"
updated: "2026-08-17"
tags:
  - entity
  - agentic-engineering
  - harness
related_entities:
  - "[[Context-Engineering]]"
  - "[[Agent-Harness]]"
source_raw:
  - "[[20260419-agent-harness-engineering]]"
  - "[[20260611-openai-harness-engineering]]"
  - "[[20260613-NLAH-natural-language-agent-harnesses]]"
  - "[[20260623-ibm-cuga-agent-harness]]"
  - "[[20260702-qwen-agent-harness-practice]]"
---

# Agent Harness Engineering

> [!definition] 定义
> **Agent Harness Engineering** 是围绕 Agent 模型设计脚手架（提示词、工具、沙箱、反馈环）的工程方法论。核心命题：**Agent = Model + Harness**，脚手架的设计往往比模型选择更能决定最终性能。

## 核心要点（跨源综合）

### 模型 vs Harness 的相对重要性

- 模型处于平台期时，Harness 是核心变量
- Claude Opus 4.6 在自定义 Harness 下 Terminal Bench 2.0 评分远高于默认 Harness
- Viv Trivedy 团队仅通过优化 Harness 将 Agent 排名从前 30 提升至前 5

### 棘轮（Ratchet）纪律

- 每当 Agent 犯错，通过工程化手段（更新 `AGENTS.md`、增加 Hook、拆分 Planner/Executor）确保错误不再发生
- 类型检查（Typecheck）作为背压信号接入循环
- 风险：过度约束导致僵化、`AGENTS.md` 长度爆炸加剧 context rot

### Context Rot 处理

- 长程任务主要瓶颈是上下文腐烂
- Harness 承担上下文压缩（Compaction）、工具调用卸载、定时重置（Context Reset）
- Anthropic 团队使用完整上下文重置 + 结构化"移交文件（Hand-off file）"

## 跨域同构

- **Just do less ↔ Harness 复用 primitives**：Ian Silber 的"Just do less"在 Agent 侧的等价物是"复用 harness primitives 而非新建"
- **Systems thinking ↔ Harness 架构**：Lenny 在 5 期 podcast 中提到 systems thinking——Harness 是把"systems thinking"工程化到 Agent 周边
- **Build-First-Business-Ontology ↔ Harness Schema 优先**：ontology 优先于 UI 在 Agent 侧对应 harness schema 优先于 prompt

## 立场偏见提醒

- "Harness 是核心变量" 在模型平台期成立，但若 GPT-5+ 模型原生支持长程规划和自省，复杂 harness 可能成为技术债务
- 通用 Harness 模式可能扼杀垂直领域（生物、医药）对高度定制化 Harness 的需求

## Source

- [[20260419-agent-harness-engineering]] — 核心 raw
- [[20260611-openai-harness-engineering]]
- [[20260613-NLAH-natural-language-agent-harnesses]]
- [[20260623-ibm-cuga-agent-harness]]
- [[20260702-qwen-agent-harness-practice]]

## 关键数据点

- Anthropic 内部 Terminal Bench 2.0 排名：仅优化 Harness（不换模型权重）从前 30 跃升至前 5
- Claude Opus 4.6 自定义 Harness 下评分远高于默认 Harness——单一变更即可改变 Top 30 → Top 5
- 每 1 步 Agent 操作 99% 成功率 → 10 步流程端到端仅 ~90.4%——错误复合效应
- Anthropic 长周期 Agent 拆分为 Initializer Agent + Coding Agent，Coding Agent 每次只做一个 feature 并强制 git commit

## 前提与局限性

- "Harness 是核心变量" 的命题在模型平台期成立；模型快速跃升期（如 GPT-5+ 引入原生长程规划）时部分 Harness 形态会变成技术债
- 通用 Harness 模式可能压低垂直领域（生物、医药）对高度定制 Harness 的需求
- 棘轮纪律过度收紧会导致 `AGENTS.md` 长度爆炸，加剧 context rot；过度宽松则失去工程化收益
- Harness 有效性高度依赖具体模型——harness 优化可能仅对特定 benchmark 优化，未必泛化

## 关联概念

- [[Agent-Harness]] — Agent Harness Engineering 的产出物
- [[Context-Engineering]] — Harness 内部管理模型看到什么的子学科
- [[Harness-Engineering]] — 同义别名
- [[Just-Do-Less]] — Harness 复用 primitives 与"Just do less"方法论同源
- [[Systems-Thinking]] — Harness 工程是 systems thinking 在 Agent 周边的工程化
- [[Build-First-Business-Ontology]] — Harness schema 优先与 ontology 优先于 UI 同构
- [[Mythical-Man-Month]] — Brooks 沟通开销二次方定律在 multi-agent Harness 上重现