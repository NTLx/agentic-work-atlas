---
type: entity
title: OpenClaw
aliases:
  - Open Claw
  - OpenClaw Agent
  - OpenClaw 项目
definition: "由 Peter Steinberger 在 2025 年 11 月开源、本地优先的个人 Agent 运行时——以'养龙虾'隐喻让用户迭代 Agent 学习自己的数字足迹，被广泛视为 Agent 元年的标志事件"
created: 2026-08-21
updated: 2026-08-21
tags:
  - agent
  - agent-infra
  - personal-agent
  - open-source
  - local-first
related_entities:
  - "[[Agent-Harness]]"
  - "[[Agent-Harness-Engineering]]"
  - "[[Agent-Native]]"
  - "[[Agentic-Memory-Dosage]]"
  - "[[Agent-Loops]]"
source_raw:
  - "[[20260819-valley101-e249-token-economic-pivot]]"
  - "[[20260528-agentic-ai-2026-landscape]]"
  - "[[20260409-ai-capability-gap-ai-psychosis]]"
  - "[[20260630-loop-engineering-andrew-ng]]"
  - "[[20260617-langchain-art-of-loop-engineering]]"
  - "[[20260613-qoder-human-bottleneck]]"
  - "[[20260611-loss-function-development]]"
  - "[[20260811-vasuman-ai-adoption-is-a-myth]]"
  - "[[20260713-agentic-misalignment-summer-2026]]"
  - "[[20260618-cio-conference-ai-practices]]"
evidence_level: medium
claim_type: mixed
---

# OpenClaw

> [!definition] 定义
> **OpenClaw** 是 Peter Steinberger 于 2025 年 11 月开源、本地优先的个人 Agent 运行时与生态——用户通过「养龙虾」隐喻（heartbeat 循环、主动 spawn 任务）迭代 Agent 学习自己的数字足迹。它被多位行业观察者视为「Agent 元年」的标志事件：从研究 → 工程、从模型 → Agent 的转折点。

## 关键数据点

- **作者**：Peter Steinberger（工程师/架构师，非 ML 研究员）
- **发布时间**：2025 年 11 月
- **爆发节奏**：从上线到 GitHub 20 万关注用 84 天（对比 React 用了近十年）（来源：20260528-agentic-ai-2026-landscape）
- **架构特征**：开源 + 本地优先 + heartbeats 循环 + 极客扩圈（类 Linux 传播路径）
- **当前状态**（2026 年中后期）：Peter 已加入 OpenAI，项目由基金会运营；OpenAI 战略重心转向 Codex
- **同期同类**：Hermes（Nous Research）、Claude Code（Boris Cherny）、Codex（OpenAI）、Qoder（Coding Agent）
- **峰值使用案例**：钱宇超 Raft（Slock）峰值 ~1B Tokens/天、账单 `$300-400`/天（同类 Agent 通信平台）
- **Peter 工作密度**：单日提交 627 次代码（约 2.3 分钟一次）—— AI 时代开发者工作密度的极端案例

## 为什么「标志 Agent 元年」

OpenClaw 的历史地位不是技术突破，而是**范式信号**——证明 Agent 不再是研究玩具，而是工程师一周可以搭出、普通人可以用起来的工程产物（来源：20260819-valley101-e249-token-economic-pivot）：

> 「最近有人跟我说，OpenClaw 之所以会引发那么大的反响，是因为这是第一次有一大批非技术背景的人，真正体验到了最新的 agentic 模型。对他们来说，之前对 AI 的理解，基本就停留在『ChatGPT 这个网站』上。」——Karpathy 补充

## 关键技术贡献

### Heartbeat 循环
OpenClaw 把 Agent 从「被动响应」转为「主动 spawn 任务」——例如：
- Zoe Agent 每天扫描 error log，发现新错误就 spawn Codex → 自动开 PR
- 哨兵 Agent 扫描 GitHub Trending / arXiv，按重要性排序推送技术情报

这是 [[Agent-Loops|Agent 循环]] 的代表性实践：把 Agent 嵌入 always-on 的反馈循环（来源：20260617-langchain-art-of-loop-engineering、20260630-loop-engineering-andrew-ng）。

### 「养龙虾」隐喻
迭代 Agent 学习用户的数字足迹——东旭把它定位为「信息过滤」而非「决策代理」（来源：20260819-valley101-e249-token-economic-pivot）。这是 [[Agent-Containment|Agent 收容]] 的一种隐式实践。

### 工程师密度信号
Peter 在 OpenClaw 开发期间曾单日提交 627 次代码（约 2.3 分钟一次），这是 AI 时代开发者工作密度的极端案例（来源：20260613-qoder-human-bottleneck）。

## 已知局限

- **质量未打磨**：大规模部署有 config / 稳定性问题
- **记忆是持续痛点**：压缩而非存储 → 回滚、Token 浪费（来源：20260819-valley101-e249-token-economic-pivot）→ 与 [[Agentic-Memory-Dosage|Agentic 记忆剂量]] 问题同源
- **企业级缺失**：本地优先的设计在企业场景下面临合规、协作、审计挑战

## 与同类产品的位置

| 维度 | OpenClaw | Hermes（Nous Research） | Claude Code |
|------|----------|------------------------|-------------|
| 形态 | 本地优先 Agent 运行时 | 本地 Agent 框架 + Skills 蒸馏 | 终端编码 Agent |
| 记忆策略 | 压缩（不持久） | 蒸馏为 Skills | 项目级上下文 |
| 作者背景 | 工程师/架构师 | 研究型团队 | Anthropic 内部 |
| 商业模式 | 开源 + 基金会 | 与模型厂商谈渠道折扣 | 闭源 + 订阅 |

（来源：20260819-valley101-e249-token-economic-pivot）

## 前提与局限性

- **社区叙事偏差**：OpenClaw 在华人开发者圈传播速度远高于英语圈，部分原因是 Peter 与华人开发者社群（东旭为代表）关系密切；评价需考虑这一来源偏差
- **「标志 Agent 元年」是回顾性叙事**：当时（2025 年 11 月）多数人未意识到其历史地位；事后建构的解释可能高估其范式意义
- **当前项目已转向基金会运营**：核心维护力量变化，未来发展路径有不确定性

## 关联概念

- [[Agent-Harness]] / [[Agent-Harness-Engineering]] — OpenClaw 是 Harness 层的代表性工程实践
- [[Agent-Native]] — OpenClaw 推动 Agent-Native 概念从理论走向产品
- [[Agent-Loops]] — heartbeat 是 Agent 循环的早期示范
- [[Agentic-Memory-Dosage]] — OpenClaw 暴露的 memory 痛点对应此概念
- Peter Steinberger — 作者，后加入 OpenAI
- [[Token-Maxing-vs-Token-Efficient]] — OpenClaw 是 Token Maxing 阶段的代表性产物，其工程纪律性预示 Token Efficient 阶段
