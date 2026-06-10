---
type: entity
title: Ralph Loops
aliases:
  - Ralph 循环
definition: "一种实现长程任务（Long-horizon execution）的 Harness 技术：通过 Hook 拦截 Agent 的退出尝试，将原始提示重新注入新鲜上下文窗口，强制 Agent 持续向目标推进。"
created: 2026-06-10
updated: 2026-06-10
tags:
  - Agent-Loops
  - long-horizon
related_entities:
  - "[[Agent-Harness]]"
  - "[[Agent-Loops]]"
  - "[[Harness-Engineering]]"
source_raw:
  - "[[20260419-agent-harness-engineering]]"
---

# Ralph Loops

> [!definition] 定义
> **Ralph Loops** 是一种用于驱动 Agent 处理超长任务的循环技术。它不依赖于单个会话的持久性，而是通过拦截 Agent 的“退出（Exit）”信号并重置环境，将单会话 Agent 转化为能够跨多个会话持续工作的实体。

## 关键数据点
- 应用领域: 涉及数百个文件重构的大型编码任务、数小时的自动化探索。

## 前提与局限性
- **前提**: 必须有可靠的 Hook 拦截机制和磁盘状态持久化方案（如进度文件）。
- **局限**: 跨会话可能导致某些短期上下文丢失，需要极高质量的“状态移交文件”。

## 关联概念
- [[Agent-Harness]]
- [[Agent-Loops]]
- [[Harness-Engineering]]
- [[Context-Rot]]
