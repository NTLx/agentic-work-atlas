---
type: entity
title: Constraint-Driven Engineering
aliases:
  - 约束驱动工程
  - 约束闭环控制
definition: "一种 Agentic Engineering 方法：通过机器可检查的约束、环境包装、分层验收和失败反馈，减少长程任务中的无效路径，并把概率性生成嵌入可重复的验证闭环；目标是提高收敛性，而不是把 Agent 变成确定性系统。"
created: 2026-06-10
updated: 2026-09-19
tags:
  - Agentic-Engineering
  - methodology
evidence_level: high
claim_type: mixed
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
  - "[[2608.19880-envharness-agent-learning]]"
---

# Constraint-Driven Engineering（约束驱动工程）

> [!definition] 定义
> **Constraint-Driven Engineering** 是本库对一类 Agent 工程实践的归纳：不用单轮模型输出承担全部质量责任，而是把目标、环境、工具调用和验收条件显式化，并通过失败反馈持续排除无效路径。Qwen 的 2026 实验是一个代表案例；OpenAI harness engineering 与 EnvHarness 则分别补充了运行时控制和环境包装视角。它提高可控性，但不把概率性模型变成确定性程序。

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
- **“质量由闭环收敛”是工程主张，不是定律**：长程任务会累积状态与误差，因此越靠近关键边界，越需要可检查的中间条件、失败信号和回放能力。
- **约束优先机器可验**：能被脚本、schema、测试、状态检查或真实环境验证的条件，比模糊提醒更适合作为硬门；审美、产品判断等不可完全自动化的条件仍需人工或独立评审。
- **环境也可以成为约束层**：EnvHarness 的 Stage / Contract 说明，不必只在 prompt 中写规则；可以改变初始状态、交互契约或环境包装，同时保留原 verifier，从而把部分约束移到模型外。

## 关键数据点
- Qwen 实验报告：Agent 在约 4 小时内通过分阶段约束完成移动端与 Web 端交付；该案例证明方法可行，但不能单案推出普遍收益。
- EnvHarness 在 5 个 benchmark / 4 个领域中报告平均提升，并在 SWE-bench Verified 上同时提高成功率、减少平均步数；它提供了“环境约束也能改善 Agent 学习/执行”的独立证据。
- 两类结果都依赖具体模型、环境、verifier 与预算，不能据此把“约束更多”简单等同于“质量更高”。

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
