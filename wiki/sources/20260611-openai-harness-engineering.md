---
type: source-summary
title: "Harness engineering: leveraging Codex in an agent-first world"
source_raw:
  - "[[20260611-openai-harness-engineering]]"
created: 2026-06-11
updated: 2026-06-11
tags:
  - source-summary
  - agentic-engineering
  - codex
  - openai
---

# Harness engineering: leveraging Codex in an agent-first world

## 编译摘要

### 1. 浓缩

- **核心结论1**: 工程师角色从"写代码"变为"设计环境"——当 agent 成为主力执行者，人类的核心工作是设计工具、抽象、反馈循环和架构约束，让 agent 能可靠工作。失败时的修复不是"try harder"，而是"what capability is missing, and how do we make it legible and enforceable for the agent?"
  - 关键证据: 3 名工程师用 Codex 5 个月产出百万行代码、1500 个 PR，人均 3.5 PR/天；人类 0 行手写代码
- **核心结论2**: 仓库知识必须对 agent 可读（Agent Legibility）——AGENTS.md 作为目录而非百科全书，docs/ 结构化知识库支持渐进式披露，所有知识必须仓库本地化，因为 agent 看不到 Google Docs、Slack 或人脑中的知识
  - 关键证据: AGENTS.md 约 100 行作为 map；docs/ 包含设计文档、架构文档、质量分级、执行计划；doc-gardening agent 自动扫描过时文档
- **核心结论3**: 架构约束是速度的前提而非障碍——严格分层依赖方向、自定义 linter、结构测试让 agent 在不牺牲一致性的前提下高速产出；约束编码后自动全局生效，"once encoded, they apply everywhere at once"
  - 关键证据: 每个业务域固定分层（Types→Config→Repo→Service→Runtime→UI）；自定义 linter 错误信息注入修复指令到 agent 上下文；golden principles + 后台 Codex 任务持续清理

### 2. 质疑

- **关于"0 行手写代码"的质疑**: 这是极端约束实验，使用 OpenAI 自家 Codex + GPT-5，环境高度优化。其他团队用不同模型/工具能否复现存疑。人类直接写某些关键代码（如架构约束本身）可能更高效。
- **关于"3.5 PR/天"的质疑**: 数据来自 OpenAI 内部，产品有内部用户但非外部公开产品。PR 质量和复杂度未公开比较。吞吐量增长可能部分来自 agent 对已有模式的复制（文章承认 entropy 问题）。
- **关于"docs/ 作为 system of record"的质疑**: 需要大量前期投入（结构化 docs、linter、CI、doc-gardening agent）。小团队可能负担不起。文档腐烂问题通过 agent 自动化缓解但未完全解决。
- **关于"架构约束早期必要性"的质疑**: 文章承认"这是通常推迟到数百人才做的架构"，但在 agent 场景下变成早期前提。这个判断可能过度乐观——快速原型阶段严格约束可能抑制探索。
- **关于泛化性的质疑**: 文章明确说"This behavior depends heavily on the specific structure and tooling of this repository and should not be assumed to generalize without similar investment"。

### 3. 对标

- **Harness Engineering**: 本文是 Harness Engineering 的一手实践案例，直接验证了 Osmani 的 "Agent = Model + Harness" 公式，且将 harness 概念从"包装 LLM"扩展到"设计整个开发环境"
- **Context Engineering**: "give Codex a map, not a manual" 直接呼应 Context Engineering 的核心原则——结构化上下文优于堆积上下文
- **Verifiable Agent Engineering**: 自定义 linter + 结构测试 + 质量分级是可验证 Agent 工程的实例
- **Progressive Disclosure**: 仓库知识库的渐进式披露（AGENTS.md 作为 map → docs/ 按需深入）是 Progressive Disclosure 在工程侧的大规模实践
- **Constraint-Driven-Engineering**: 严格架构约束 + 机械执行 + golden principles 是约束驱动工程的实例
- **Compound-Engineering**: agent-to-agent review、执行计划版本化、知识持续沉淀是 Compound Engineering 的高级形态

### 关联概念

- [[Agent-Harness]]
- [[Harness-Engineering]]
- [[AGENTS-md]]
- [[Context-Engineering]]
- [[Compound-Engineering]]
- [[Constraint-Driven-Engineering]]
- [[Progressive-Disclosure]]
- [[Verifiable-Agent-Engineering]]
- [[Agentic-Engineering]]
