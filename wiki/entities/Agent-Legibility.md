---
type: entity
title: Agent-Legibility
aliases:
  - Agent Legibility
  - Agent 可读性
  - Agent 可理解性
definition: "设计代码、文档及工具，使 Agent 能在授权范围内获得、定位和验证完成任务所需的信息；仓库内版本化知识是实现之一，不是唯一知识来源"
created: 2026-06-11
updated: 2026-11-28
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
> **Agent Legibility** 是一种设计原则：OpenAI 的特定工程实验以 Codex 为主要读者；未进入可用上下文的组织事实难以可靠利用，但具有获授权连接器或检索工具的 Agent 可以读取外部资料，模型先验也不等于组织事实。

## 关键数据点

- **OpenAI 实验（2026）**：5 个月、0 行手写代码、百万行代码、1500 PR，3 名工程师人均 3.5 PR/天
- **AGENTS.md 重定义**：从"规则手册"（60 行）变为"目录"（约 100 行），指向 docs/ 中的结构化知识库
- **知识库结构**：设计文档（含验证状态）、架构文档（域和包分层）、质量文档（各领域分级）、执行计划（进度和决策日志）、技术债务
- **机械验证**：专用 linter + CI 验证知识库时效性、交叉链接和结构正确性
- **Doc-gardening agent**：自动扫描过时文档，开修复 PR
- **单次 Agent 运行**：原文称其团队经常见到单任务运行约6小时或更长（有时在人类睡觉时）；未提供时长分布或成功率统计，不外推其他环境。
- **架构约束**：每个业务域固定分层（Types→Config→Repo→Service→Runtime→UI），自定义 linter 机械执行

## 为什么重要

当 agent 成为主力代码生产者时，代码库的"读者"发生了根本变化。传统代码库为人类工程师设计可读性（命名、注释、目录结构）；agent-first 代码库需要为 agent 设计可读性。

OpenAI 团队的核心洞察：**human legibility 和 agent legibility 不是同一件事**。人类可以问同事、翻 Slack、看会议记录；该案例的 Agent 以仓库及运行工具为主要可见面。原则是给任务提供受控、可追溯、可验证的知识入口；无需把所有外部权威资料、秘密或实时业务状态复制入仓库。

## 核心原则

### 1. 仓库可作为项目工程知识的权威记录

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
- 单体手册可能迅速失效，agent 无法判断哪些规则仍然有效
- 单一文件难以做机械检查（覆盖度、新鲜度、所有权、交叉链接）

### 3. 渐进式披露

Agent 从一个小的、稳定的入口点开始，被教导下一步看哪里，而不是一开始就被淹没。这与 Progressive-Disclosure 原则一致。

### 4. "无聊"技术更利于 agent

Agent 更容易理解和使用组合性好、API 稳定、训练数据中广泛存在的技术。该案例认为有时可采用可理解的本地实现；应比较依赖维护、安全、测试与重写成本，不将重造轮子设为默认。

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
- **Agent legibility ≠ Human legibility**: 应按真实任务和审查需求验证两者；不能仅以 Agent 通过率判断人类可维护性。

## 关联概念

- [[Agent-Harness]] — Agent legibility 是 harness 设计的核心目标之一
- [[Context-Engineering]] — 结构化上下文优于堆积上下文
- [[AGENTS-md]] — OpenAI 将 AGENTS.md 从"规则手册"重定义为"目录"
- [[Progressive-Disclosure]] — 仓库知识库的分层加载策略
- [[Constraint-Driven-Engineering]] — 架构约束作为 agent 可读性的机械保障
- [[Verifiable-Agent-Engineering]] — linter 和结构测试让知识库可验证
- [[Harness-Engineering]] — 从"包装 LLM"扩展到"设计整个开发环境"
