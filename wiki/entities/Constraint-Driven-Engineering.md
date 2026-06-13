---
type: entity
title: Constraint-Driven Engineering
aliases:
  - 约束驱动工程
  - 约束闭环控制
definition: "一种 Agentic Engineering 范式，主张通过分阶段注入机器可校验的硬约束和分层验收机制，将 Agent 的交付过程从“随机生成”转变为“确定性收敛”的控制系统。"
created: 2026-06-10
updated: 2026-06-11
tags:
  - Agentic-Engineering
  - methodology
related_entities:
  - "[[Agentic-Engineering]]"
  - "[[Verifiable-Agent-Engineering]]"
  - "[[Automated-Criteria]]"
  - "[[Long-Horizon-Execution]]"
  - "[[Pixel-Facts]]"
source_raw:
  - "[[20260610-qwen-constraint-driven-engineering-experiment]]"
  - "[[20260611-openai-harness-engineering]]"
  - "[[20260613-aliyun-agent-infra-constraint-infrastructure]]"
---

# Constraint-Driven Engineering（约束驱动工程）

> [!definition] 定义
> **Constraint-Driven Engineering** 是由通义实验室（2026）提出的工程方法论。它认为 Agent 的输出质量不应依赖于模型的某种“神启”式一次性生成，而应通过一套严密的约束闭环系统，在漫长的决策链条中不断过滤无效路径，最终使系统状态收敛到预定义的达标线。

## 核心支柱

### 1. 分阶段注入约束 (Progressive Constraint Injection)
约束不是一次性丢进 System Prompt 的，而是随任务阶段逐层加码：
- **规划阶段**: 约束目标边界（页面清单、功能范围）。
- **架构阶段**: 约束技术栈与数据建模事实。
- **编码阶段**: 注入具体的实现规则与自查项。

### 2. 像素事实 (Pixel Facts)
解决模糊需求与精准执行之间的矛盾。将 UI 需求从有损的文字描述（“两列网格”）转化为无损的像素坐标约束（Bounds）。坐标是机器能逐条核对的事实，是消除 Agent “脑补”错误的关键。

### 3. 带错纠正与收敛 (Error-Prone Correction)
Harness 不仅是一个调度器，更是一个偏差收集器。失败时的报错原文被完整保留并注入下一轮上下文，确保重试不是从头再来，而是基于残局的持续逼近。

## 关键洞察
- **“质量是收敛出来的”**: 在长程任务中，错误会随时间指数级放大，必须在每个环节设置“当场截断”的硬信号。
- **约束减法原则**: 约束要做减法，只保留能被机器字面匹配、明确验证的规则。模糊的提醒（如“风格要一致”）反而会诱导模型通过“哄骗校验”来产生伪交付。

## 关键数据点
- 通义实验室实验显示：凭一份 15 万字文档，Agent 在 4 小时内全自动交付双端（移动+Web）应用。
- 采用该范式后，长程交付的成功率显著高于仅提供编辑器的 Agent 环境。

## 前提与局限性
- **前提**: 模型必须具备极高的指令遵循稳定性和长上下文处理能力（如 Qwen3.7-Max）。
- **局限**: 构建整套约束闭环需要极高的人期前置投入（SOP 编写、坐标抓取程序开发）。
- **局限**: 适用于结构化程度高的工程任务，对于艺术创作等弱约束领域效用不明。

## 关联概念
- [[Agentic-Engineering]] - 该范式的母体
- [[Verifiable-Agent-Engineering]] - 强调可验证性，约束工程是其具体实现路径之一
- [[Automated-Criteria]] - 约束工程的“眼睛”，没有自动化判据则闭环不成立
- [[Task-Horizon\|Long-Horizon Execution]] - 约束工程解决的核心问题场景
- [[Pixel-Facts]] - 约束工程在 UI 还原领域的特定技术
- [[Constraint-Infrastructure]] - 约束驱动工程的平台层实现，将方法论转化为可编程的基础设施能力
