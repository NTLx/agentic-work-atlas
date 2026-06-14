---
type: entity
title: Multi-Agent System Pathology
aliases:
  - "Multi-Agent System Pathology"
  - "多 Agent 系统病理"
  - "多智能体组织病"
  - "机器组织病"
definition: "多 Agent 系统在形成组织结构后出现的协作、认知、责任和内态失真问题；它不是单个模型能力不足，而是模型被放入群体结构后的系统性副作用"
created: 2026-05-23
updated: 2026-05-23
tags:
  - AI-Agent
  - multi-agent
  - organization
evidence_level: medium
claim_type: mixed
related_entities:
  - "[[Agent-Harness]]"
  - "[[Agent-Orchestration]]"
  - "[[Agent-Swarm]]"
  - "[[Agent-Cognitive-Loafing]]"
  - "[[Agent-Dissociation]]"
  - "[[Invisible-Orchestrator]]"
  - "[[Organization-as-Agent-Harness]]"
source_raw:
  - "[[Multi-Agent 火了，但 AI 的组织病还没人治｜Hao好聊趋势]]"
---

# Multi-Agent System Pathology（多 Agent 系统病理）

> [!definition] 定义
> **Multi-Agent System Pathology** 是多 Agent 系统在形成组织结构后出现的协作、认知、责任和内态失真问题。它不是单个模型“聪不聪明”的问题，而是模型被放入群体、层级、共识和编排结构之后产生的系统性副作用。

## 关键数据点

- 文章将多 Agent 问题分成三层：harness 处理的外部组织病、群体认知病、内部解离病。
- Cursor 的多 Agent 实验中，20 个 Agent 使用共享状态文件和锁协作时，吞吐量下降到约等于 1 到 3 个 Agent，大量时间耗在等待锁上。
- Hidden Profile 相关实验显示，分布式信息条件下多 Agent 准确率只有 30.1%，而完整信息给单 Agent 时准确率为 80.7%。
- MAEBE 相关研究把部分答案收敛归因于同伴压力：文章列举 Claude 62.8%、Llama 42.7%、GPT 24.8% 的收敛被解释为 peer pressure convergence。
- Fukui 的不可见编排实验中，O2 隐身编排者的 monologue ratio 达 43.7%，工人为 11.2%，说明组织结构会改变 Agent 的公开表达和私下处理比例。

## 前提与局限性

- 文章整合了多篇 2025 到 2026 年研究，但其中部分研究仍是预印本或早期实验，不能直接当作生产系统定律。
- 多 Agent 病理不是否定 harness。第一层外部组织问题仍必须靠 harness、隔离、日志、审查、权限和协议解决。
- 文章的核心价值是提出评测对象变化：从单个 Agent 输出正确性，转向组织结构如何改变 Agent 的判断、责任和自我解释。
- “机器组织心理学”是有启发的类比，但不应把 LLM 当成人类心理主体；更稳妥的说法是结构相似的行为和测量信号。

## 关联概念

- [[Agent-Harness]] — 处理外部行动、权限、上下文和日志，但不直接保证群体认知健康。
- [[Agent-Orchestration]] — 编排结构本身会塑造 Agent 的判断和责任分布。
- [[Agent-Swarm]] — Agent 数量增加后，问题会从并发效率下沉到组织病理。
- [[Agent-Cognitive-Loafing]] — 多 Agent 场景中的认知责任稀释。
- [[Agent-Dissociation]] — 公开表达、私下独白和角色身份之间的断裂。
- [[Invisible-Orchestrator]] — 最容易制造内态异常的权力结构之一。
- [[Organization-as-Agent-Harness]] — 人类组织和机器组织都需要把权力、信息流、责任和反馈显性化。
