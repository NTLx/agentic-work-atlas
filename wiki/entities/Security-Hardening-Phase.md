---
type: entity
title: Security Hardening Phase
aliases:
  - Security Hardening Phase
  - 安全硬化阶段
  - Hardening Phase
definition: "在开发和代码审查之后，用预算驱动的 Agent 搜索持续发现漏洞的安全阶段"
created: 2026-04-21
updated: 2026-05-25
tags:
  - agentic-coding
  - cybersecurity
  - software-engineering
related_entities:
  - '[[Cybersecurity-Proof-of-Work]]'
  - '[[Agentic-Engineering]]'
  - '[[Drew-Breunig]]'
  - '[[AISI]]'
  - '[[Mythos]]'
  - '[[Verifiable-Agent-Engineering]]'
source_raw:
  - "[[20260414-cybersecurity-proof-of-work]]"
---

# Security Hardening Phase

> [!definition] 定义
> Agentic Coding 的第三阶段：识别漏洞直到预算耗尽。

## 三阶段模型

| 阶段 | 任务 | 瓶颈 | 特点 |
|------|------|------|------|
| **开发** | 实现功能、快速迭代 | Human input | 人类直觉主导 |
| **代码审查** | 文档、重构、PR 审查 | Human input | 应用最佳实践 |
| **安全硬化** | 识别漏洞、持续审计 | Money (tokens) | 自主运行直到预算耗尽 |

## 关键数据点

- **Anthropic Code Review**: `$15-20` per review（代码审查阶段产品）
- **Mythos Hardening**: `$12,500` per attempt (100M tokens)
- **历史对比**: 安全审计从"rare, discrete, inconsistent"变为"constant, within optimal budget"
- **瓶颈变化**: 开发和 review 仍主要受 human input 限制；安全硬化更接近预算限制
- **AISI 证据**: Mythos 在 32 步企业攻击任务中 10 次成功 3 次，且 100M token 预算没有明显边际收益递减

## 为什么是第三阶段

安全硬化不适合放在开发早期。若代码结构还在剧烈变化，Agent 会把预算花在不断变化的目标上，产出很快失效。更合理的流程是：

1. 开发阶段先让功能跑起来。
2. 代码审查阶段改善可维护性、文档、测试和基本质量。
3. 安全硬化阶段用长程 Agent、漏洞脚手架和预算上限持续寻找可利用路径。

这意味着 Agentic Coding 的“完成”标准会变高。代码通过测试只是第二阶段完成，只有经过足够预算的安全搜索，才更接近生产风险判断。

## 前提与局限性

- **前提**: 
  1. 模型安全能力随 tokens 增加
  2. 有明确的硬化成功标准
- **局限性**: 
  1. 为什么硬化前要先完成开发？避免浪费 tokens 硬化未稳定代码
  2. 预算上限需人工决策
- **局限性**:
  1. 预算更多不等于覆盖全部攻击面
  2. 防御者还需要把发现变成补丁、测试和持续监控
  3. 若攻击者工具链更便宜，防御预算也必须重新估算

## 关联概念

- [[Cybersecurity-Proof-of-Work]] — 硬化阶段的核心博弈
- [[Agentic-Engineering]] — 扩展为三阶段模型
- [[Drew-Breunig]] — 提出者
- [[AISI]] — 提供高预算网络攻击评测证据
- [[Mythos]] — 安全硬化阶段的代表性模型能力
- [[Verifiable-Agent-Engineering]] — 安全硬化是生产 Agent 的独立验证阶段

## 实践意义

- 安全从"一次性审计"变为"持续投入"
- 代码便宜，除非需要安全
- 硬化成本由漏洞市场价值决定（而非模型推理成本）
- 安全团队需要把硬化预算、发现数量、严重度、修复率和回归测试一起纳入工程仪表盘
