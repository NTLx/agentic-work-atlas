---
type: source-summary
title: "building-effective-agents"
source_raw:
  - "[[building-effective-agents]]"
created: 2026-05-24
updated: 2026-05-24
tags:
  - source-summary
  - AI-Agent
  - LLM
  - agentic-systems
  - workflows
  - tool-use
  - Claude
---

# building-effective-agents

## 编译摘要

### 1. 浓缩
- **核心结论1**: 最简单的方案往往最好——最成功的实现使用简单、可组合的模式，而非复杂框架
  - 关键证据: 应该先用简单的 prompt + retrieval + in-context examples，只有在明确证明能提升效果时才增加复杂度
- **核心结论2**: Workflows vs Agents 选择——预定义工作流适合可预测任务，自主决策适合需要灵活性的复杂任务
  - 关键证据: Coding agents 和 customer support 是两个最有前景的应用场景
- **核心结论3**: Agent-Computer Interface (ACI) 很重要——工具定义和文档应该和 prompt 一样精心设计
  - 关键证据: Anthropic 在 SWE-bench 上花在优化工具的时间比优化 prompt 更多

### 2. 质疑
- **关于"简单"的质疑**: 简单方案是否总是最优？复杂框架是否有存在的必要？
- **关于"自主性"的质疑**: 完全自主的 agents 是否适合生产环境？需要多少人类监督？
- **关于 ACI 的质疑**: 是否存在通用工具设计模式，还是每个工具都需要单独设计？

### 3. 对标
- **跨域关联1**: 类似软件工程中的"过度设计"反模式——YAGNI 原则在 LLM 领域的体现
- **跨域关联2**: 类似自动驾驶分级——从 rules-based 到 end-to-end，agents 是 LLM 的"完全自动驾驶"
- **可迁移场景**: 任何需要 AI 辅助决策和执行的复杂任务——研究代理、自动化运维、多步骤内容创作

### 关联概念
- [[Agentic-Engineering]] - Agent 工程范式
- [[Agent-Workflow-Patterns]] - Agent 工作流模式
- [[ACI-Agent-Computer-Interface]] - Agent 计算机接口
- [[Code-Execution]] - AI 代码执行能力
- [[Context-Engineering]] - Agent 上下文工程
