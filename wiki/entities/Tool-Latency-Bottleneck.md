---
type: entity
title: Tool Latency Bottleneck
aliases:
  - Tool Latency Bottleneck
  - 工具延迟瓶颈
  - Tools Too Slow
definition: "模型、工具和工作流延迟共同决定端到端耗时；模型提速后工具、外部等待或调度可能成为约束，须按关键路径实测"
created: 2026-05-30
updated: 2026-11-28
evidence_level: medium
claim_type: mixed
tags:
  - AI-Agent
  - agentic-engineering
  - infrastructure
related_entities:
  - "[[Agentic-Engineering]]"
  - "[[Tool-Use-Architecture]]"
  - "[[Integration-Wall]]"
  - "[[Code-Execution]]"
  - "[[ACI-Agent-Computer-Interface]]"
source_raw:
  - "[[20260529-gemini-co-leads-origins]]"
  - "[[20260930-latentspace-devday-2026]]"
  - "[[20260921-linear-ci-bottleneck-reworked]]"
---

# Tool Latency Bottleneck（工具延迟瓶颈）

> [!definition] 定义
> **Tool Latency Bottleneck** 指特定工作流的端到端完成时间主要受工具调用、排队、外部事件等待或反馈链制约的情形。不是所有 API、数据库或 CI 都为人类节奏设计，也不能假定 Agent 操作普遍达到毫秒级。

## 为什么重要

Noam Shazeer 在讨论未来 30 天自主 Agent 的假设场景时用“29 and a half days”描述等待。原始 Transcript L418–428 没有测量样本、trace、计算方法或实际 30 天运行，属预测性/夸张表述，不能作为实测占比。

Jeff Dean 进一步阐述："If you make the model infinitely fast, you are going to limit how much you can actually speed up real work because often they involve interactions with tools that are designed for kind of human latency."

这意味着：

1. **加速模型不等于加速工作**：模型从 2 秒降到 0.2 秒，但如果后续的 API 调用需要 5 秒，总时间只节省了 1.8 秒
2. **按关键路径优化**：区分实际外部处理、轮询、排队、固定等待与可并行部分；不以降低延迟为由绕过必要的验证或授权。
3. **频率与延迟分别测量**：Koray 补充工作频率；原文没有每秒10次或每分钟1次的对照数据。高并发还受吞吐、限流、负载和排队制约。

## 关键数据点

- **Jeff Dean 预测**（2026-05）："agents are going to stress that all of our tools are too slow"——这将是 IO 2027 前的核心问题
- **30 天 Agent 的全栈需求**：要实现自主运行 30 天的 Agent，需要 memory systems + continual learning + 更好的硬件（"a zillion tokens"）+ 低延迟硬件
- **"29.5 天等待"**：未来场景的口头估计，不是当前 Agent 的总体实测。既有 [[20260930-latentspace-devday-2026]]（00:12:32–00:19:06）访谈也描述网页和外部响应时延及事件驱动方案；仍属产品方观察。[[20260921-linear-ci-bottleneck-reworked]] 则给出团队内部 CI 关键路径和 setup 优化实例；不把两个不同场景合并为统一延迟比例。
- **频率约束**：Koray 强调"the frequency of working"——工具不仅延迟高，吞吐量也为人类频率设计
- **对标 Integration Wall**：工具延迟瓶颈是 [[Integration-Wall|集成之墙]] 的微观版本——AI 从 demo 进入生产遇到 legacy system；Agent 从快速对话进入长期自主遇到为人类设计的工具

## 典型场景（原有数字仅为示意，非实测基准）

| 场景 | 模型耗时 | 工具耗时 | 瓶颈 |
|------|----------|----------|------|
| Agent 查 API 获取数据 | 0.1s | 2-5s | API 延迟 |
| Agent 跑测试验证代码 | 0.05s | 30s-5min | CI/CD 管线 |
| Agent 搜索代码库 | 0.2s | 1-10s | 索引/检索延迟 |
| Agent 调用浏览器操作 | 0.1s | 3-15s | 页面加载+渲染 |
| Agent 写入数据库 | 0.05s | 0.5-2s | 事务锁+网络 |

## 前提与局限性

- **前提：Agent 能力已经足够强**：只有当模型本身不再是瓶颈时，工具延迟才成为瓶颈。当前很多场景中模型推理仍是主要耗时
- **前提：工具调用频繁**：如果 Agent 只做少量工具调用，总延迟影响有限。瓶颈在长期自主运行的 Agent 中最显著
- **方案需按真实瓶颈选择**：模型提速、异步事件、缓存、批处理、并行、硬件及网络优化为候选措施；不必所有层同时重构。
- **不总是需要低延迟**：有些工具操作本身就需要时间（如编译大型项目、跑完整测试套件），低延迟不是唯一解法，异步调度和并行执行同样重要

## 关联概念

- [[Agentic-Engineering]] — 工具延迟是 Agent 系统设计中必须考虑的基础约束
- [[Tool-Use-Architecture]] — 工具使用架构需要为 Agent 频率而非人类频率优化
- [[Integration-Wall]] — 工具延迟是微观版集成之墙
- [[Code-Execution]] — Agent 代码执行依赖的沙箱、CI/CD 是延迟瓶颈的核心来源
- [[ACI-Agent-Computer-Interface]] — Agent-Computer Interface 的设计需要考虑延迟和吞吐量
