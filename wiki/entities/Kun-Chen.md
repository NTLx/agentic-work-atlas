---
type: entity
title: Kun Chen
aliases:
  - Kun Chen
  - kunchenguid
definition: "前 Meta/Microsoft/Atlassian L8 Principal Engineer，构建 Bing 搜索引擎、Windows、Facebook Games 等大规模系统。近年在 Atlassian 构建前沿 coding agents，日常 ship 40-50 production commits/天。开源了 AXI、Lavish、No Mistakes、gnhf、Treehouse、First Mate 等 agentic engineering 工具链。"
validated_source: "https://www.youtube.com/watch?v=iQyg-KypKAA"
validated_at: "2026-06-22"
created: 2026-06-22
updated: 2026-06-22
tags:
  - person
  - agentic-engineering
  - tool-builder
related_entities:
  - "[[Agentic-Engineering]]"
  - "[[Agent-Ergonomics]]"
  - "[[Validation-Pipeline]]"
  - "[[Captain-Mindset]]"
  - "[[Agent-Orchestration]]"
source_raw:
  - "[[20260620-l8-principal-agentic-workflow]]"
---

> [!definition] 定义
> Kun Chen 是一位从大规模系统工程转向 agentic engineering 工具链构建的工程师，以"船长模型"（Captain Mindset）和 AXI（Agent-first 工具设计标准）为核心贡献。

## 职业时间线

| 年份 | 角色 | 贡献 |
|------|------|------|
| 早期 | Microsoft 工程师 | Bing 搜索引擎、Windows |
| 中期 | Meta L8 Principal Engineer | Facebook Games 大规模系统 |
| 近年 | Atlassian | 构建前沿 coding agents，帮助工程团队有效使用 |
| 2026 | 独立工具构建者 | 开源 agentic engineering 工具链 |

## 核心贡献

### 工具链

| 工具 | 定位 | 解决什么问题 |
|------|------|-------------|
| AXI | Agent-first 工具设计标准 | 工具对 Agent 的 token 效率和延迟优化 |
| Lavish | 交互式 HTML artifact 规划 | 替代 text wall 的可视化需求讨论 |
| No Mistakes | 验证管线 | 自动化 adversarial review + e2e + PR babysitting |
| gnhf | 长时运行任务循环 | Agent 自主运行直到停止条件 |
| Treehouse | Worktree 生命周期管理 | 消除手动 worktree 管理的认知负担 |
| First Mate | Meta-orchestrator | 管理多 Agent session 的切换和编排 |

### 思想贡献

- **Captain Mindset**: 人从 sailor（写代码）到 captain（指挥 Agent 团队）的角色转型
- **Agent Ergonomics**: 工具应以 Agent 为第一公民设计，AXI 十原则
- **Validation over Review**: 不审 diff，看管线生成的证据
- **Memory + Skills 渐进式架构**: global memory（极简偏好）→ project memory（集体学习）→ skills（按需加载）

## 关键数据点

- 日常 ship 40-50 production commits（非 demo，是 well-tested production code）
- 所有工具免费开源
- GitHub: kunchenguid
- Linktree: https://linktr.ee/kunchenguid

## 关联概念

- [[Agentic-Engineering]] — 整体实践框架
- [[Agent-Ergonomics]] — AXI 工具设计原则
- [[Validation-Pipeline]] — No Mistakes 验证管线
- [[Captain-Mindset]] — 角色转型理念
- [[Agent-Orchestration]] — First Mate 编排模式
