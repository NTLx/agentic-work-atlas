---
type: entity
title: Mythos
aliases:
  - Mythos
  - Claude Mythos
  - Anthropic Mythos
definition: "Anthropic 面向网络安全任务的受限访问模型，用于高强度漏洞发现与安全评测"
created: 2026-04-21
updated: 2026-05-25
tags:
  - ai-model
  - cybersecurity
  - anthropic
related_entities:
  - '[[Cybersecurity-Proof-of-Work]]'
  - '[[Cybersecurity-Openness]]'
  - '[[Drew-Breunig]]'
  - '[[AISI]]'
  - '[[Security-Hardening-Phase]]'
  - '[[Verifiable-Agent-Engineering]]'
source_raw:
  - "[[20260414-cybersecurity-proof-of-work]]"
  - "[[AI and the Future of Cybersecurity Why Openness Matters]]"
---

# Mythos

> [!definition] 定义
> Anthropic (2026) 的安全专用 LLM 模型，在网络安全任务上表现卓越。

## 关键数据点

- **发布**: 2026 年 4 月（preview）
- **访问限制**: 仅向关键软件制造商提供（Glasswing 项目）
- **安全能力**: AISI 测试中完成 32 步企业网络攻击模拟（人类需 20 小时）
- **成本**: 100M tokens per attempt = `$12,500`
- **成功率**: 10 次尝试中成功 3 次（唯一完成任务的模型）
- **能力特征**: 不是一次短回答，而是能在长程任务中持续探索、利用工具、推进攻击链
- **风险含义**: 如果防御者能购买类似能力，攻击者也可能用 token 预算购买漏洞发现能力

## 系统级理解

Mythos 的真正意义不在单一模型名称，而在一个系统级配方：

- 安全专门化模型。
- 漏洞探测脚手架。
- 足够长的自主运行预算。
- 可衡量的攻击任务和成功标准。
- 受限访问与关键软件制造商优先硬化窗口。

这组要素共同说明，网络安全中的 Agent 能力不是只由模型参数决定，也由 harness、工具、预算和评测环境决定。Mythos 因此应和 [[Cybersecurity-Proof-of-Work]]、[[Security-Hardening-Phase]] 一起理解。

## 前提与局限性

- **前提**: Anthropic 判断模型安全能力过高，公开风险大于收益
- **局限性**: 
  1. 测试结果来自 AISI，需更多独立验证
  2. 真实攻击场景可能比测试更复杂
  3. 模型仍未显示边际收益递减，意味着持续投入 tokens 可能持续发现漏洞
- **局限性**:
  1. 受限访问意味着外部社区难以复现实验细节
  2. 该模型是否代表未来通用模型能力，仍需继续观察
  3. 防御收益取决于厂商是否把发现转化为实际补丁和硬化流程

## 关联概念

- [[Cybersecurity-Proof-of-Work]] — 模型能力支撑的概念
- [[AISI]] — 测试机构（英国 AI 安全研究所）
- [[Drew-Breunig]] — 分析者
- [[Security-Hardening-Phase]] — Mythos 代表安全硬化阶段的高预算 Agent
- [[Verifiable-Agent-Engineering]] — Mythos 的风险需要通过受控评测和行为证据理解

## Anthropic Glasswing 项目

Anthropic 为 Mythos 创建的访问控制机制：
- 仅"critical software makers"可获得访问
- 提供时间窗口进行安全硬化
- 体现 Anthropic 对 AI 安全的谨慎态度
