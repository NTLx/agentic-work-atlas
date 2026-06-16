---
type: entity
title: Agent-Legibility
aliases:
  - Agent Legibility
  - Agent 可读性
  - Agent 可理解性
definition: "设计代码库、文档和工具链时以 agent 为首要消费者的原则——任何 agent 运行时无法在上下文中访问的知识，对 agent 来说等于不存在"
created: 2026-06-11
updated: 2026-06-16
evidence_level: medium
claim_type: mixed
tags:
  - Agentic-Engineering
  - Context-Engineering
  - design-principle
related_entities:
  - "[[Agent-Harness]]"
  - "[[Context-Engineering]]"
  - "[[AGENTS-md]]"
  - "[[Progressive-Disclosure]]"
  - "[[Constraint-Driven-Engineering]]"
  - "[[Verifiable-Agent-Engineering]]"
  - "[[Harness-Engineering]]"
source_raw:
  - "[[20260611-openai-harness-engineering]]"
---

# Agent Legibility（Agent 可读性）

> [!definition] 定义
> **Agent Legibility** 是一种设计原则：代码库、文档和工具链应以 agent 为首要消费者进行组织。从 agent 的视角看，运行时无法在上下文中访问的知识等于不存在——Google Docs、Slack 讨论、人脑中的共识对 agent 来说都是不可见的。

## 关键数据点

- **OpenAI 实验（2026）**：5 个月、0 行手写代码、百万行代码、1500 PR，3 名工程师人均 3.5 PR/天
- **AGENTS.md 重定义**：从"规则手册"（60 行）变为"目录"（约 100 行），指向 docs/ 中的结构化知识库
- **知识库结构**：设计文档（含验证状态）、架构文档（域和包分层）、质量文档（各领域分级）、执行计划（进度和决策日志）、技术债务
- **机械验证**：专用 linter + CI 验证知识库时效性、交叉链接和结构正确性
- **Doc-gardening agent**：自动扫描过时文档，开修复 PR
- **单次 agent 运行**：常见持续 6 小时以上（常在人类睡觉时运行）
- **架构约束**：每个业务域固定分层（Types→Config→Repo→Service→Runtime→UI），自定义 linter 机械执行

## 为什么重要

当 agent 成为主力代码生产者时，代码库的"读者"发生了根本变化。传统代码库为人类工程师设计可读性（命名、注释、目录结构）；agent-first 代码库需要为 agent 设计可读性。

OpenAI 团队的核心洞察：**human legibility 和 agent legibility 不是同一件事**。人类可以问同事、翻 Slack、看会议记录；agent 只能看到仓库中的版本化文件。因此，所有对决策有影响的知识都必须被推入仓库。

## 核心原则

### 1. 仓库是唯一的知识源

| 对人类可读 | 对 agent 可读 |
|-----------|-------------|
| Google Docs | docs/ 目录中的 markdown |
| Slack 讨论 | 执行计划和决策日志 |
| 人脑中的约定 | AGENTS.md 和架构文档 |
| 会议共识 | 设计文档中的 core beliefs |
| 口头传承 | linter 规则和错误信息 |

### 2. AGENTS.md 是目录而非百科

OpenAI 的做法：AGENTS.md 约 100 行，作为 map 指向 docs/ 中的深层知识。原因：
- 上下文是稀缺资源，巨型指令文件会挤占任务、代码和相关文档
- 过多指导变成"非指导"——当一切都"重要"时， nothing is
- 单体手册会立即腐烂，agent 无法判断哪些规则仍然有效
- 单一文件难以做机械检查（覆盖度、新鲜度、所有权、交叉链接）

### 3. 渐进式披露

Agent 从一个小的、稳定的入口点开始，被教导下一步看哪里，而不是一开始就被淹没。这与 Progressive-Disclosure 原则一致。

### 4. "无聊"技术更利于 agent

Agent 更容易理解和使用组合性好、API 稳定、训练数据中广泛存在的技术。有时让 agent 重新实现子功能比处理不透明的第三方库行为更便宜。

## 工程实践

| 实践 | 作用 |
|------|------|
| 结构化 docs/ 目录 | 知识库作为 system of record |
| 自定义 linter | 验证知识库时效性、交叉链接、结构正确性 |
| doc-gardening agent | 扫描过时文档，自动开修复 PR |
| 执行计划版本化 | 活跃计划、完成计划、技术债务共置 |
| 质量分级文档 | 追踪各领域和架构层的质量差距 |
| linter 错误信息注入修复指令 | 将 remediation 直接放入 agent 上下文 |

## 前提与局限性

- **投入前提**: 需要大量前期投入（结构化 docs、linter、CI、doc-gardening agent），小团队可能负担不起
- **泛化边界**: OpenAI 明确说此行为"depends heavily on the specific structure and tooling"，不应假定无需类似投入即可复现
- **腐烂缓解但未消除**: doc-gardening agent 能发现过时文档，但定义"什么是过时"仍需人类判断
- **人类知识外化成本**: 将 Slack 共识、会议决策推入仓库需要持续纪律，可能增加流程负担
- **Agent legibility ≠ Human legibility**: 为 agent 优化的代码结构可能不符合人类风格偏好，文章认为"that's okay"

## 前提与局限性

- **投入前提**: 需要大量前期投入（结构化 docs、linter、CI、doc-gardening agent），小团队可能负担不起
- **泛化边界**: OpenAI 明确说此行为"depends heavily on the specific structure and tooling"，不应假定无需类似投入即可复现
- **腐烂缓解但未消除**: doc-gardening agent 能发现过时文档，但定义"什么是过时"仍需人类判断
- **人类知识外化成本**: 将 Slack 共识、会议决策推入仓库需要持续纪律，可能增加流程负担
- **Agent legibility ≠ Human legibility**: 为 agent 优化的代码结构可能不符合人类风格偏好，文章认为"that's okay"

## 关联概念

- [[Agent-Harness]] — Agent legibility 是 harness 设计的核心目标之一
- [[Context-Engineering]] — 结构化上下文优于堆积上下文
- [[AGENTS-md]] — OpenAI 将 AGENTS.md 从"规则手册"重定义为"目录"
- [[Progressive-Disclosure]] — 仓库知识库的分层加载策略
- [[Constraint-Driven-Engineering]] — 架构约束作为 agent 可读性的机械保障
- [[Verifiable-Agent-Engineering]] — linter 和结构测试让知识库可验证
- [[Harness-Engineering]] — 从"包装 LLM"扩展到"设计整个开发环境"
