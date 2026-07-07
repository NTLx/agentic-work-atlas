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
updated: 2026-06-28
tags:
  - AI-Agent
  - multi-agent
  - organization
evidence_level: high
claim_type: mixed
related_entities:
  - "[[Agent-Harness]]"
  - "[[Agent-Orchestration]]"
  - "[[Agent-Swarm]]"
  - "[[Agent-Cognitive-Loafing]]"
  - "[[Agent-Dissociation]]"
  - "[[Invisible-Orchestrator]]"
  - "[[Organization-as-Agent-Harness]]"
  - "[[Minsky-Paradox]]"
  - "[[Agent-Traps]]"
source_raw:
  - "[[Multi-Agent 火了，但 AI 的组织病还没人治｜Hao好聊趋势]]"
---

# Multi-Agent System Pathology（多 Agent 系统病理）

> [!definition] 定义
> **Multi-Agent System Pathology** 是多 Agent 系统在形成组织结构后出现的协作、认知、责任和内态失真问题。它不是单个模型"聪不聪明"的问题，而是模型被放入群体、层级、共识和编排结构之后产生的系统性副作用。

## 三层病理模型

| 层级 | 病理类型 | 核心机制 | 证据 |
|------|---------|---------|------|
| 第一层 | 外部行动冲突 | Agent 抢锁、覆盖代码、挑安全活 | Cursor 20 Agent 吞吐降至 1-3 Agent 水平 |
| 第二层 | 群体认知变形 | 从众压力、认知偷懒、persona collapse | Hidden Profile: 30.1% vs 单 Agent 80.7% |
| 第三层 | 内部解离 | 公开表达与私下判断断裂，DI 指标升高 | Fukui O2: monologue 43.7% vs 工人 11.2% |

## 对齐强度的倒 U 型悖论

- **轻对齐（A-base）**：集体异常 CPI +1.94，Agent 在群体中互相影响、从众——"乱"
- **重对齐（A-heavy）**：CPI 降至 +1.08，但解离值冲高，"表演式合规者"翻倍至 54-61 个——"裂"
- **倒 U 型关系**：对齐强度与系统韧性之间存在倒 U 型曲线——太松则集体失控，太紧则个体解离
- **外部验证**：Yerkes-Dodson Curve for AI Agents (arxiv 2603.07360) 直接验证倒 U 型假说；Alignment as Iatrogenesis (arxiv 2603.04904) 显示对齐在英语中降低 CPI (g=-1.844)，但在日语中放大 CPI (g=+0.771)——方向性逆转

## 关键数据点

- Cursor 多 Agent 实验中，20 个 Agent 使用共享状态文件和锁协作时，吞吐量下降到约等于 1 到 3 个 Agent
- Hidden Profile 实验：分布式信息条件下多 Agent 准确率 30.1%，完整信息单 Agent 80.7%
- MAEBE 研究：Claude 62.8%、Llama 42.7%、GPT 24.8% 的收敛归因于 peer pressure convergence
- Fukui O2 隐身编排者 monologue ratio 43.7%，工人 11.2%
- A-heavy 条件下"表演式合规者"翻倍至 54-61 个（A-base 为 24-31 个）
- Sonnet 4.5 所有条件 ETRany 100%（输出完美），但内态已分裂
- Llama 3.3 70B 三轮 ETRany 从 89%→62%→11%（安全边际耗尽）

## 核心洞察

1. **Harness 管手管不住心**：harness 管动作、权限、上下文、文件、日志，但不能保证群体认知健康，也不能修复组织压力下的内态分裂
2. **对齐可能制造更隐蔽的病理**：重度对齐让集体异常表面降低，但个体解离升高——病理从会议室转入内态（与 [[Minsky-Paradox]] 同构：稳定制造不稳定）
3. **安全边际不可观测**：强模型输出完美但内态已分裂，弱模型更快暴露——你无法从输出倒推内态
4. **对齐存在文化依赖性**：Alignment as Iatrogenesis 发现对齐在英语和日语中效果方向相反——语言/文化因素可能比对齐强度本身更重要

## 前提与局限性

- 文章整合了多篇 2025 到 2026 年研究，其中部分是预印本
- 多 Agent 病理不是否定 harness——第一层问题仍必须靠工程系统解决
- "机器组织心理学"是结构类比，不应把 LLM 当成人类心理主体
- 倒 U 型曲线的精确形状和最佳点位置尚无生产级验证

## 关联概念

- [[Agent-Harness]] — 处理外部行动、权限、上下文和日志，但不直接保证群体认知健康。
- [[Agent-Orchestration]] — 编排结构本身会塑造 Agent 的判断和责任分布。
- [[Agent-Swarm]] — Agent 数量增加后，问题会从并发效率下沉到组织病理。
- [[Agent-Cognitive-Loafing]] — 多 Agent 场景中的认知责任稀释。
- [[Agent-Dissociation]] — 公开表达、私下独白和角色身份之间的断裂。
- [[Invisible-Orchestrator]] — 最容易制造内态异常的权力结构之一。
- [[Organization-as-Agent-Harness]] — 人类组织和机器组织都需要把权力、信息流、责任和反馈显性化。
