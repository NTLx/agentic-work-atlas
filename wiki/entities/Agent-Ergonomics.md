---
type: entity
title: Agent Ergonomics
aliases:
  - Agent Ergonomics
  - Agent 人体工学
  - AXI
definition: "将 Agent 视为工具的第一公民（first-class citizen），通过 token-efficient 输出格式、低延迟接口和结构化交互设计优化工具对 Agent 的效率。Kun Chen (2026) 提出 AXI 十原则，benchmark 显示 AXI 标准工具比传统 MCP server 节省 3x token 成本。"
created: 2026-06-22
updated: 2026-06-22
evidence_level: medium
claim_type: mixed
tags:
  - agentic-engineering
related_entities:
  - "[[ACI-Agent-Computer-Interface]]"
  - "[[Agent-Harness]]"
  - "[[Tool-Use-Architecture]]"
  - "[[Agentic-Engineering]]"
  - "[[Agentic-Workflow-Token-Efficiency]]"
source_raw:
  - "[[20260620-l8-principal-agentic-workflow]]"
---

> [!definition] 定义
> Agent Ergonomics 是一种工具设计哲学：不为人类优化界面，而为 Agent 优化接口。核心指标是 Agent 完成同一任务所需的 token 数、turns 数和成功率。

## 核心原则（AXI 十原则摘要）

Kun Chen 在 AXI（axi.md）中提出 10 条 Agent-first 工具设计原则，核心要点：

1. **Token-efficient 输出格式**：不用 JSON，用紧凑格式可节省约 40% tokens
2. **低延迟接口**：减少 round-trip，batch 操作优于逐条调用
3. **结构化交互**：给 Agent 可直接解析的结构化数据，而非人类可读的自由文本
4. **确定性语义**：工具返回值含义明确，Agent 无需猜测或二次确认
5. **错误信号清晰**：错误信息包含足够上下文让 Agent 自行修复

## 关键数据点

- GitHub MCP server vs GitHub CLI benchmark：同一任务，MCP 花费 **3x token 成本** + **2x 延迟**，无明确收益
- Token-efficient 输出格式相比 JSON 可节省约 **40% tokens**
- Chrome DevTools AXI 相比其他浏览器工具：更少 turns、更少 tokens 完成相同任务
- AXI 工具在 ProgramBench 评测中显示最高成功率 + 最低成本

## 前提与局限性

- AXI benchmark 由作者自行设计和执行，methodology 和 dataset 未公开，需独立复现验证
- Token-efficient 格式（非 JSON）可能增加 Agent 的解析错误率，尤其在模型能力较弱时
- AXI 原则适用于 CLI/API 工具，对需要丰富上下文的 MCP 工具（如需要 schema 描述的工具）适用性待验证
- 工具设计优化是**一次性投入**，需要评估 ROI：高频使用的工具（如 GitHub、浏览器）优化价值高，低频工具不值得专门优化

## 关联概念

- [[ACI-Agent-Computer-Interface]] — Agent-Computer Interface，更广义的 Agent 友好接口设计
- [[Agentic-Workflow-Token-Efficiency]] — Token 效率在 agent 工作流中的系统性优化
- [[Tool-Use-Architecture]] — 工具使用的系统架构设计
- [[Progressive-Disclosure]] — 工具信息的按需加载，减少 system prompt 膨胀
