---
type: entity
title: AISI
aliases:
  - AISI
  - AI Security Institute
  - 英国 AI 安全研究所
definition: "评估前沿 AI 模型安全能力并发布风险测试结果的英国政府 AI 安全机构"
created: 2026-04-21
updated: 2026-05-25
tags:
  - organization
  - ai-safety
related_entities:
  - '[[Mythos]]'
  - '[[Cybersecurity-Proof-of-Work]]'
  - '[[Security-Hardening-Phase]]'
  - '[[Verifiable-Agent-Engineering]]'
source_raw:
  - "[[20260414-cybersecurity-proof-of-work]]"
---

# AISI (AI Security Institute)

> [!definition] 定义
> 英国政府设立的 AI 安全研究机构，负责评估前沿 AI 模型的安全能力。

## 关键数据点

- **测试项目**: "The Last Ones" — 32 步企业网络攻击模拟（人类需 20 小时）
- **测试对象**: Mythos, Opus 4.6, GPT-5.4
- **测试结果**: Mythos 唯一完成任务（3/10 成功率）
- **测试预算**: 每次尝试 100M tokens
- **评估意义**: 100M tokens 预算没有出现明显边际收益递减，说明更长、更贵的 agentic security runs 可能继续发现漏洞
- **知识库作用**: AISI 在这里不是普通机构条目，而是支撑 [[Cybersecurity-Proof-of-Work]] 的独立评测节点

## 测试发现

- 模型安全能力"a step up over previous frontier models"
- 100M tokens 预算未显示边际收益递减
- 网络安全性能快速提升

## 为什么它重要

AISI 的价值在于给前沿模型安全能力提供第三方评测语境。厂商可以声称模型“很强”或“有风险”，但安全能力是否已经跨过部署边界，需要外部机构用可复现任务、预算上限和对照模型给出证据。

在 Mythos 案例中，AISI 的测试把抽象担忧变成了工程问题：

- 攻击链可以被拆成 32 步任务。
- 每次尝试可以用 token 预算衡量。
- 不同模型可以在同一任务上比较。
- 成功率、边际收益和任务成本可以进入安全硬化决策。

这使 AISI 与 [[Verifiable-Agent-Engineering]] 直接相关：它把“模型是否危险”转化为“在给定预算、环境和目标下能完成什么行为”。

## 前提与局限性

### 前提条件
- 英国政府政策支持和预算保障
- 前沿 AI 模型厂商配合测试
- 测试任务必须足够接近真实风险，同时又能在受控环境中复现

### 局限性
- 测试结果反映特定时间点的模型能力
- 评估方法论仍在演进中
- 无法覆盖所有潜在安全风险场景
- 单项测试不能代表全部网络安全能力，也不能直接预测真实攻击者的工具链、耐心和目标选择

## 关联概念

- [[Mythos]] — AISI 测试的模型
- [[Cybersecurity-Proof-of-Work]] — AISI 测试支撑的概念
- [[Security-Hardening-Phase]] — AISI 的 token 预算测试提示安全硬化会成为独立阶段
- [[Verifiable-Agent-Engineering]] — AISI 提供可比较、可审计的模型行为证据

## 外部链接

- [AISI 官网](https://www.aisi.gov.uk/)
- [Mythos 测试报告](https://www.aisi.gov.uk/blog/our-evaluation-of-claude-mythos-previews-cyber-capabilities)
