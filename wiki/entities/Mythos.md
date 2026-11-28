---
type: entity
title: Mythos
aliases:
  - Mythos
  - Claude Mythos
  - Anthropic Mythos
definition: "Anthropic的受限前沿模型家族：2026-04的Mythos Preview是通用前沿模型，后续版本面向网络安全与生命科学等高能力任务；须区分底层模型、访问政策、安全限制和评测配置"
created: 2026-04-21
updated: 2026-11-28
tags:
  - cybersecurity
  - anthropic
evidence_level: high
claim_type: mixed
related_entities:
  - '[[Cybersecurity-Proof-of-Work]]'
  - '[[Cybersecurity-Openness]]'
  - '[[Drew-Breunig]]'
  - '[[AISI]]'
  - '[[Security-Hardening-Phase]]'
  - '[[Verifiable-Agent-Engineering]]'
  - '[[N-Hour]]'
  - '[[AI-Policy-Framework]]'
source_raw:
  - "[[20260414-cybersecurity-proof-of-work]]"
  - "[[AI and the Future of Cybersecurity Why Openness Matters]]"
  - "[[20260610-anthropic-ai-exploits-security-patches]]"
  - "[[20260610-ai-exponential-policy]]"
---

# Mythos

> [!definition] 定义
> Anthropic前沿模型家族。Mythos Preview并非仅用于网络安全的专用模型，而是具有较强编码、推理与Agent能力的通用前沿模型；初始用途与访问受限。后续Mythos版本不能与Preview实验直接混用。

## 关键数据点

- **发布**: 2026-04-07（Preview，Project Glasswing）
- **访问限制**: 初期经Glasswing向选定伙伴开放防御用途；后续开放政策、资格与可用版本见下方版本记录
- **安全能力**: AISI在特定受控网络模拟中报告结果；20小时为研究者对人类完成时间的估计，并非匹配的人类对照
- **成本**: 100M Token为AISI模拟预算上限；`$12,500`为Breunig历史估算，不是实付成本或当前定价
- **成功率**: Preview在当时TLO评测中3/10完整完成，平均22/32评分步骤；不能外推当前模型排名或充分防护系统的成功率
- **能力特征**: 不是一次短回答，而是能在长程任务中持续探索、利用工具、推进攻击链
- **风险含义**: 如果防御者能购买类似能力，攻击者也可能用 token 预算购买漏洞发现能力

### 2026-06 受控安全研究（Preview）

[Anthropic原文](https://www.anthropic.com/research/n-days)比较已知补丁样本上的PoC触发与完整验证结果；两者不是同一指标。实验耗时、预算与软件更新节奏对照提示缩短防御窗口，但不代表现实入侵、通用零日发现能力或真实攻击成本。详见[[N-Hour]]和已校准源摘要。

## 系统级理解

Mythos 的真正意义不在单一模型名称，而在一个系统级配方：

- 具有较强任务相关能力的模型；不假定为安全专门化训练。
- 漏洞探测脚手架。
- 足够长的自主运行预算。
- 可衡量的攻击任务和成功标准。
- 受限访问与关键软件制造商优先硬化窗口。

这组要素共同说明，网络安全中的 Agent 能力不是只由模型参数决定，也由 harness、工具、预算和评测环境决定。Mythos 因此应和 [[Cybersecurity-Proof-of-Work]]、[[Security-Hardening-Phase]] 一起理解。

## 前提与局限性

- **证据身份**：Anthropic将双用途风险作为受限发布的依据，这是厂商风险判断与访问策略，不是唯一可能的治理路径
- **局限性**: 
  1. AISI为独立政府研究机构；模拟缺少主动防守和部分真实防护，另一个OT场景未完整完成。仍需按真实风险验证
  2. 真实攻击场景可能比测试更复杂
  3. 在所测预算内仍有进展，不证明无限扩展或无边际递减
- **其他边界**:
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

Glasswing是初期受限防御合作计划，而非所有后续Mythos版本的唯一访问机制或安全效果证明。2026-11-28核对[官方模型页面](https://www.anthropic.com/claude/mythos)与[Preview发布研究](https://www.anthropic.com/research/mythos-preview)：

| 日期 | 版本或计划 | 证据边界 |
|---|---|---|
| 2026-04-07 | Mythos Preview / Glasswing | 通用前沿模型，初期选定防御伙伴 |
| 2026-06-09 | Mythos 5 | 后续版本；6月12日暂停，7月1日恢复部分美国组织访问（官方历史记录） |
| 2026-09-01 | Mythos 5.1 | 受限于经审核组织 |
| 2026-11-09 | Mythos 5.2 | 官方记录为网络安全及生命科学研究，经验证计划向合格组织开放 |

官方说明Fable 5.2与Mythos 5.2共享底层模型，安全限制不同，部分评测差异反映限制介入；不能把产品可用能力等同底层能力。安全评测与访问政策须注明版本和日期。未独立运行模型、审核当前访问资格或验证厂商全部榜单。
