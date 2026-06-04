---
type: entity
title: Compound Engineering
aliases:
  - Compound Engineering
definition: "持续把有效计划、指令、工具和重复工作沉淀为可复用资产，让每次 Agent 工作为下一次降低成本"
created: 2026-04-10
updated: 2026-06-04
tags:
  - AI-Agent
  - coding-agents
  - best-practices
related_entities:
  - '[[Agentic-Engineering]]'
  - '[[Coding-Agents]]'
  - "[[Plan-as-Agent-Checkpoint]]"
  - "[[Human-Signal]]"
  - "[[Skill-Internalization]]"
source_raw:
  - '[[20260410-better-code]]'
  - "[[Every Agentic Engineering Hack I Know (June 2026)]]"
---

# Compound Engineering（复合工程）

> **核心理念**：每个编码项目以回顾结束，记录有效内容用于未来的 Agent 运行

## 定义

**Compound Engineering** 是 Every (Dan Shipper & Kieran Klaassen) 提出的模式，描述与编码助手持续改进的工作方式：

```
项目完成 → Compound Step（回顾）→ 记录有效做法 → 未来运行使用
```

## 核心循环

### 1. 执行项目

使用编码助手完成开发任务。

### 2. Compound Step

项目结束时的回顾环节：

- 什么做法有效？
- 什么指令帮助最大？
- 遇到什么问题？
- 如何避免未来问题？

### 3. 记录沉淀

将学习内容记录到：

- CLAUDE.md 或类似配置文件
- 自定义指令
- 工具文档

### 4. 未来复用

下次运行时，Agent 可以访问这些积累的知识。

## 从复盘循环扩展为工作系统

Matt Van Horn 的个人工作流把 Compound Engineering 从“项目后复盘”扩展成一条更连续的复利链：

```text
最新研究与原始上下文
  -> [[Plan-as-Agent-Checkpoint|结构化计划]]
  -> 多 Agent 执行
  -> [[Human-Signal|人类反馈与重定向]]
  -> 重复工作固化为 Skill
  -> 下一次计划读取已有知识和 Skill
```

这里的关键不是安装更多工具，而是让一次工作的高价值部分留下来。计划保存任务状态，笔记和历史方案保存判断，Skill 保存程序性做法。只有这些资产能被未来 Agent 直接读取和执行，复利才真正发生。

## 关键洞察

> [!tip] 复合效应
> 小改进会复合。曾经耗时的质量增强现在成本已降至没有借口不投资质量。
> 
> **编码助手意味着我们终于可以两者兼得**：新功能 + 高质量。

## 与传统开发的区别

| 维度 | 传统开发 | Compound Engineering |
|------|---------|---------------------|
| 学习沉淀 | 个人经验 | 可复用指令 |
| 知识传递 | 文档/培训 | Agent 配置 |
| 迭代速度 | 手动改进 | 自动应用 |
| 知识累积 | 线性 | 复合增长 |

## 实践建议

1. **每个 PR 后**：记录什么提示有效
2. **遇到问题时**：更新指令避免重复
3. **成功模式**：标准化为可复用模板
4. **工具文档**：持续优化 Agent-Computer Interface

## 关键数据点

- 由 Dan Shipper 和 Kieran Klaassen (Every) 提出
- 每个编码项目以回顾结束，称为"compound step"
- 小改进会复合，曾经耗时的质量增强现在成本已降至没有借口不投资
- 编码助手意味着可以两者兼得：新功能 + 高质量

## 前提与局限性

- 依赖前提：编码助手能够理解并遵循积累的指令和配置
- 适用边界：适用于使用 AI 编码助手的软件开发流程
- 局限性：指令迭代可能有天花板，过度定制可能丧失通用性
- 需要人类主动记录：Agent 不会自动学习，需要人类刻意更新指令
- 知识沉淀依赖团队纪律性：需要每个项目后坚持做 compound step
- 沉淀速度过快也会积累错误做法；计划、Skill 和规则需要版本控制、验证和淘汰机制
- “重复两次就做成 Skill”是启发式，不适合变化快、风险高或尚未理解清楚的工作

---

> **来源**：Simon Willison, "AI should help us produce better code" (Agentic Engineering Patterns, 2026)

## 关联概念

- [[Agentic-Engineering]] - 基础工程范式
- [[ACI-Agent-Computer-Interface]] - 工具接口设计
- [[Technical-Debt-Avoidance]] - 复合工程帮助避免技术债务
- [[Plan-as-Agent-Checkpoint]] - 把任务状态和验收标准持久化
- [[Human-Signal]] - 为高吞吐 Agent 执行提供方向和判断
- [[Skill-Internalization]] - 把重复经验和外部设计编译为可复用 Skill
