---
type: entity
title: Tool Latency Bottleneck
aliases:
  - Tool Latency Bottleneck
  - 工具延迟瓶颈
  - Tools Too Slow
definition: "Agent 速度提升后，外部工具为人类设计的延迟成为整个系统的新瓶颈"
created: 2026-05-30
updated: 2026-05-30
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
---

# Tool Latency Bottleneck（工具延迟瓶颈）

> [!definition] 定义
> **Tool Latency Bottleneck** 是指当 AI 模型的推理速度提升后，系统整体速度不再由模型决定，而是由外部工具的响应延迟决定。这些工具——API、数据库、文件系统、浏览器、CI/CD 管线——是为人类的秒级交互节奏设计的，无法匹配 Agent 的毫秒级操作频率。

## 为什么重要

Noam Shazeer 的一句话精确描述了这个瓶颈：**"30 天里有 29.5 天是在等待。"**

Jeff Dean 进一步阐述："If you make the model infinitely fast, you are going to limit how much you can actually speed up real work because often they involve interactions with tools that are designed for kind of human latency."

这意味着：

1. **加速模型不等于加速工作**：模型从 2 秒降到 0.2 秒，但如果后续的 API 调用需要 5 秒，总时间只节省了 1.8 秒
2. **工具生态需要重新设计**：为人类设计的工具假设"用户会等"——页面加载 1-3 秒、数据库查询 100ms、CI 跑 5 分钟。Agent 不等待
3. **频率比延迟更关键**：Koray 补充说"the frequency of working"同样重要——Agent 每秒可以发起 10 次工具调用，人类每分钟 1 次

## 关键数据点

- **Jeff Dean 预测**（2026-05）："agents are going to stress that all of our tools are too slow"——这将是 IO 2027 前的核心问题
- **30 天 Agent 的全栈需求**：要实现自主运行 30 天的 Agent，需要 memory systems + continual learning + 更好的硬件（"a zillion tokens"）+ 低延迟硬件
- **"29.5 天等待"**：Noam 指出当前 Agent 的绝大多数时间花在等待外部工具响应上
- **频率约束**：Koray 强调"the frequency of working"——工具不仅延迟高，吞吐量也为人类频率设计
- **对标 Integration Wall**：工具延迟瓶颈是 [[Integration-Wall|集成之墙]] 的微观版本——AI 从 demo 进入生产遇到 legacy system；Agent 从快速对话进入长期自主遇到为人类设计的工具

## 典型场景

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
- **解决方案需要全栈**：Jeff 强调"it takes the full stack"——模型加速、工具重设计、硬件改进、网络优化缺一不可
- **不总是需要低延迟**：有些工具操作本身就需要时间（如编译大型项目、跑完整测试套件），低延迟不是唯一解法，异步调度和并行执行同样重要

## 关联概念

- [[Agentic-Engineering]] — 工具延迟是 Agent 系统设计中必须考虑的基础约束
- [[Tool-Use-Architecture]] — 工具使用架构需要为 Agent 频率而非人类频率优化
- [[Integration-Wall]] — 工具延迟是微观版集成之墙
- [[Code-Execution]] — Agent 代码执行依赖的沙箱、CI/CD 是延迟瓶颈的核心来源
- [[ACI-Agent-Computer-Interface]] — Agent-Computer Interface 的设计需要考虑延迟和吞吐量
