---
type: entity
title: N-Hour
aliases:
  - N-Hour
  - N 小时
  - N-Hour Paradigm
definition: "补丁发布后数小时内即被 AI 构建利用代码的新网络安全现实，取代传统 N-Day 概念"
created: 2026-06-12
updated: 2026-06-12
tags:
  - cybersecurity
  - AI-capability
  - paradigm-shift
related_entities:
  - "[[Mythos]]"
  - "[[Cybersecurity-Proof-of-Work]]"
  - "[[Security-Hardening-Phase]]"
  - "[[Collingridge-Dilemma]]"
source_raw:
  - "[[20260610-anthropic-ai-exploits-security-patches]]"
---

# N-Hour

> [!definition] 定义
> Anthropic (2026) 提出的概念：随着 AI 模型能在数小时内从安全补丁构建完整利用代码，传统衡量补丁与利用之间时间差的"N-Day"术语已过时，"N-Hour"更准确描述新现实。

## 关键数据点

- **Firefox SpiderMonkey**: Mythos Preview 在补丁发布后 12 分钟内获得第一个崩溃证明，1 小时内完成第一个完整利用
- **Windows 内核**: 21 个漏洞中 18 个在 6 小时内被发现，8 个完整提权链在约 12 小时内构建完成
- **成本**: 平均每个利用 `$2,000`，8 个利用链总成本 `$15,700`
- **Microsoft 评级失效**: 14/21 漏洞被评为"不太可能被利用"，Mythos Preview 破解了其中 13 个
- **补丁窗口期**: Windows Autopatch 需 7 天覆盖 90% 设备，所有利用在自动更新前已完成
- **对比基准**: Mandiant 2020 年分析显示 25 个漏洞中 16 个需一个月或更长时间被利用

## 前提与局限性

- **前提**:
  1. 前沿 AI 模型持续发现和利用漏洞的能力随 tokens 增加
  2. 安全补丁的代码差异提供了足够的漏洞定位信息
  3. 模型能理解复杂的二进制代码和系统架构
- **局限性**:
  1. 真实攻击还需要目标侦察、投递、检测规避等额外步骤
  2. Mythos Preview 是受限访问模型，不代表所有公开可用模型的能力
  3. 防御方可能开发 AI 驱动的检测和响应系统
  4. 内存安全语言和硬件级保护可能长期改变攻防均衡

## 关联概念

- [[Mythos]] — 构建 N-Hour 范式的模型
- [[Cybersecurity-Proof-of-Work]] — N-Hour 加速了 token 成本博弈
- [[Security-Hardening-Phase]] — N-Hour 要求持续而非一次性的安全硬化
- [[Collingridge-Dilemma]] — N-Hour 是技术影响难以预见直到难以管理的经典案例
