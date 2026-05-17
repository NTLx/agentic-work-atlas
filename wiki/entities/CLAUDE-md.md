---
type: entity
title: CLAUDE.md
aliases:
  - CLAUDE.md
  - 架构上下文文档
definition: "AI 原生初创公司的“系统记忆与防御屏障”：用于显式记录架构决策、业务规范和边界约束的 Markdown 文件，是防止 Agent 在无摩擦开发中发生“架构漂移”的核心机制。"
created: 2026-05-13
updated: 2026-05-13
tags:
  - AI-Agent
  - Documentation
  - Software-Engineering
related_entities:
  - "[[Claude-Code-CLI]]"
  - "[[Agentic-Engineering]]"
  - "[[AI-Native-Startup]]"
source_raw:
  - "[[The-Founders-Playbook-05062026_v3]]"
---

# CLAUDE.md

> [!definition] 定义
> **CLAUDE.md** 不仅仅是一个 Prompt 文件，它是 AI Agent（如 Claude Code）的“长期记忆基底”。在 Agentic Engineering 中，它负责承载项目的全局上下文，确保高速自动化的代码生成始终处于受控的系统结构内。

## 核心价值：对抗 AI 熵增

在传统的软件工程中，架构知识可以通过高级工程师的评审（Code Review）和团队口耳相传进行约束。但在 AI 原生组织中，构建速度被无限放大，若缺乏持久化的规则：
1. **架构漂移（Architectural Drift）**：AI 会在每一次新会话中根据当前零散的指令重新推导基础决策，导致各个功能模块逻辑互斥。
2. **复利型技术债**：Agent 产出的代码虽然“能运行”，但在系统层面毫无连贯性，最终导致项目无法扩展和维护。

## 最佳实践规范

- **会话前同步（Pre-flight Context）**：开启新会话时，Agent SDK（如 Claude Code）会自动读取目录下的 CLAUDE.md，以此作为行动边界。
- **记录“Why”而非仅仅是“What”**：不只是记录使用的框架，更要记录放弃了什么方案，以及权衡（Trade-offs）的逻辑。
- **模块化分布**：在庞大的系统里，不应只有一个巨大的 CLAUDE.md，而是要在特定的子目录放置特定的规范，提供精细化的局部上下文。
- **动态更新（Living Document）**：每次会话产生了新的重要架构决策或引入了新的基础模式，应立即写回 CLAUDE.md，使其与代码库共同进化。

## 战略意义

对于 AI 原生创始人而言，编写和维护 CLAUDE.md 是最重要的“编排”工作之一。它是创始人将自身领域专知（Domain Expertise）转化为代码护城河的最直接载体。

## 关联概念

- [[Claude-Code-CLI]] - 主要读取者与执行者
- [[Agentic-Engineering]] - 理论框架
- [[AI-Native-Startup]] - 组织基础设施
