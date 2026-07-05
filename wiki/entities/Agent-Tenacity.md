---
type: entity
title: Agent Tenacity
aliases:
  - Agent Tenacity
  - 代理韧性
  - AI Stamina
definition: "Agent 在明确目标、反馈信号和预算边界内持续调用工具、试错和修正，直到成功或触发停止条件的能力"
created: 2026-04-21
updated: 2026-06-16
evidence_level: medium
claim_type: mixed
tags:
  - ai-agent
  - software-engineering
  - productivity
related_entities:
  - '[[Andrej-Karpathy]]'
  - '[[Claude-Code-CLI]]'
  - '[[Agentic-Engineering]]'
  - '[[Verifiability]]'
  - '[[Slopocalypse]]'
  - '[[Dominator-Analysis]]'
source_raw:
  - "[[20260127-claude-coding-notes]]"
  - "[[20260702-anthropic-harnesses-long-running-agents]]"
---

# Agent Tenacity

> [!definition] 定义
> **Agent Tenacity（代理韧性）** 是 Agent 在明确目标、反馈信号和预算边界内持续调用工具、试错和修正，直到成功或触发停止条件的能力。

## 为什么重要

Agent Tenacity 解释了 coding agent 带来的部分“能力跃迁”体感：它们不只是一次性生成代码，而是可以在工具循环中持续运行、观察失败、修改方案、再次验证。Karpathy 在 Claude coding notes 中把这种体验描述为 watching it struggle for a long time and come out victorious 30 minutes later。

这会改变软件工作的瓶颈。过去很多任务不是因为人类不会做，而是因为反复试错太烦、太累、太容易让人放弃。Agent 把这类摩擦从情绪和体力成本转成 token、时间、权限和验证成本。

但 tenacity 不是可靠性的同义词。没有 [[Verifiability|可验证性]]、预算上限和停止条件，持续尝试会变成无效循环、测试过拟合或大规模生成低质产物。

## 生成机制

Agent Tenacity 来自四个条件的组合。

1. **工具循环**：Agent 能读取文件、运行命令、修改代码、重新测试，而不是只输出一次建议。
2. **外部反馈**：测试、编译、lint、截图、日志或用户评价为下一步行动提供方向。
3. **低情绪成本**：Agent 不会因为失败而沮丧，也不会因为重复操作而厌烦。
4. **可消耗预算**：持续试错的真实约束变成 token、运行时间、API 费用、权限风险和 CI 资源。

这也是它和人类“毅力”的区别：人类的韧性要对抗疲劳、挫败和注意力衰减；Agent 的韧性主要受环境反馈质量和资源边界约束。

## 关键数据点

- **观察实例**：Karpathy 描述 Agent 可以长时间 struggle，约 30 分钟后解决问题
- **核心差异**：Agent 不受挫败感、厌烦和动机波动影响，但会消耗 token、时间和工具调用预算
- **工作流变化**：杠杆来自“给成功标准”，而不是一步步命令 Agent 做什么
- **组织影响**：效果不只是一项任务 speedup，也会带来 work expansion，让人开始处理过去不值得、不敢碰或太繁琐的代码工作

## 使用条件

Agent Tenacity 在以下条件下最有价值：

- **目标可表达**：任务能被写成结果标准，而不只是模糊愿望。
- **反馈够快**：Agent 每轮尝试后能获得测试、日志、编译或评审反馈。
- **状态可回滚**：失败尝试不会不可逆地破坏生产环境或关键数据。
- **预算可控**：token、时间、命令权限和外部服务调用都有上限。
- **人类能验收**：最终结果仍有人或自动系统负责判断是否可交付。

Karpathy 的实践建议可以压缩为一句话：不要只告诉 Agent 做什么，而要给它成功标准，让它在约束内循环到标准达成。

## 失败模式

- **无效循环**：Agent 在错误假设下不断重试，表面勤奋，实际没有靠近目标。
- **预算燃烧**：持续运行把问题从人工时间转成 token、CI、API 和审查成本。
- **测试过拟合**：Agent 为了让当前测试通过而写出脆弱补丁，隐藏更深的概念错误。
- **风险放大**：在权限过大的环境中，持续尝试可能反复修改文件、迁移数据或调用外部系统。
- **低质扩散**：tenacity 让产出变多，但如果没有筛选机制，会加速 [[Slopocalypse|低质内容泛滥]]。

因此，Agent Tenacity 必须和停止条件一起设计。工程上应明确最大轮次、最大预算、失败升级路径、人工接管点和回滚策略。

## 与可验证性的关系

Agent Tenacity 的价值取决于任务能否被验证。代码、测试、lint、编译和截图回归这类任务天然适合，因为每一轮失败都能给出新信号。

在开放式研究、产品判断、架构取舍和写作中，反馈更主观，Agent 可能持续产出看似努力的内容，却没有可靠进步。此时 tenacity 不能替代 [[Decision-Quality|决策质量]]、品味和责任承担。

在非确定性 Agent 行为测试中，[[Dominator-Analysis|Dominator Analysis]] 提供了另一种边界：不是要求每次执行路径相同，而是识别成功路径中必须经过的 essential states。这样可以区分有意义的自适应重试和真正偏离目标的失败。

## 前提与局限性

- **前提**：Agent 有明确成功目标和验证机制，如测试通过、lint 清零或可观察状态达成
- **前提**：工具权限、运行环境和回滚机制足够安全
- **局限**：当前证据主要来自 Karpathy 个人体验，不是量化研究
- **局限**：持续尝试不能修复错误目标、错误测试和错误需求
- **约束**：人类仍需要决定何时继续、何时停止、何时改写问题

## 关联概念

- [[Andrej-Karpathy]] — 观察者
- [[Claude-Code-CLI]] — Karpathy 使用的 coding agent
- [[Agentic-Engineering]] — Agent 编程方法论
- [[Verifiability]] — Tenacity 需要客观反馈才能转化为可靠进步
- [[Slopocalypse]] — 持续生成能力如果缺少筛选，会放大低质产出
- [[Dominator-Analysis]] — 非确定性 Agent 验证中区分有效重试和失败路径

## 跨域洞察

| 领域 | 对比 |
|------|------|
| **心理学** | 人类工作瓶颈可能是"情绪韧性"而非智力能力 |
| **经济学** | Agent 将劳动成本转化为计算、权限和验证成本，改变了工作的边际效用 |
| **管理学** | 组织要把“坚持尝试”变成可观测流程，而不是把无限运行误认为负责 |

## 实践应用

Karpathy 建议：
1. 不要命令 Agent"做什么"，给出"成功标准"让 Agent 循环尝试
2. 先写测试，让 Agent 循环直到测试通过
3. 用声明式指令而非命令式指令，获得更大杠杆

本库中的操作化版本是：

- 给 Agent 明确验收测试、退出条件和失败上报路径。
- 让 Agent 每轮记录做了什么、看见什么失败、下一步为何合理。
- 对高风险任务使用只读、沙箱、分支、灰度和人工批准。
- 把 tenacity 用在可验证任务上，把开放式判断留给人类或专门评审流程。
