---
type: entity
title: Security Hardening Phase
aliases:
  - Security Hardening Phase
  - 安全硬化阶段
  - Hardening Phase
definition: "在软件生命周期中按风险持续验证安全控制、发现缺陷、修复和复验的工程活动；可包含独立的发布前硬化阶段与预算约束的自动化检查"
created: 2026-04-21
updated: 2026-11-28
tags:
  - agentic-engineering
  - cybersecurity
  - software-engineering
evidence_level: medium
claim_type: mixed
related_entities:
  - '[[Cybersecurity-Proof-of-Work]]'
  - '[[Agentic-Engineering]]'
  - '[[Drew-Breunig]]'
  - '[[AISI]]'
  - '[[Mythos]]'
  - '[[Verifiable-Agent-Engineering]]'
  - '[[Agent-Containment]]'
source_raw:
  - "[[20260414-cybersecurity-proof-of-work]]"
---

# Security Hardening Phase

> [!definition] 定义
> Drew Breunig提出的开发、审查、硬化三阶段设想；安全硬化的目标是降低已识别风险并验证控制，而非耗尽预算。

## 三阶段模型

| 阶段 | 任务 | 瓶颈 | 特点 |
|------|------|------|------|
| **开发** | 实现功能、快速迭代 | Human input | 人类直觉主导 |
| **代码审查** | 文档、重构、PR 审查 | Human input | 应用最佳实践 |
| **安全硬化** | 识别、验证、修复与复验 | 预算、专家、测试环境、发布 | 按风险和增量收益决定范围与停止 |

## 关键数据点

- **Anthropic Code Review**：Breunig 2026-04文章引用的历史每次审查估算，不是当前报价或完整硬化成本
- **预算**：Breunig按AISI 100M Token上限所作历史估算`$12,500`，不是实际支出或硬化预算标准
- **历史对比**: 作者设想自动化使持续审计更可行；非已证实行业迁移或最优预算
- **瓶颈变化**: 人工、算力、环境、缺陷分诊和发布能力在各阶段均可能成为瓶颈
- **AISI 证据**: [AISI](https://www.aisi.gov.uk/blog/our-evaluation-of-claude-mythos-previews-cyber-capabilities)报告Mythos Preview特定受控模拟3/10完整完成，至100M Token仍有进展；非硬化效果实验或无边际递减证明

## 何时硬化：贯穿生命周期，发布前集中验收

不应把安全推迟到功能完成后。[NIST SSDF SP 800-218](https://csrc.nist.gov/publications/detail/sp/800-218/final)建议将安全实践整合到SDLC。威胁建模、身份权限、数据边界、安全依赖及设计审查宜尽早进行；对稳定版本安排更深入的授权隔离测试、修复及发布门禁，线上继续监测和响应。长程Agent只能在明确授权、隔离与预算内辅助验证。

**本库综合**：验收以具体风险和控制证据为准：高风险路径有负向测试与修复证据；记录版本、覆盖、未解决问题及风险接受者；修复后回归并确认发布实际生效。预算耗尽或没有发现新问题都不等于安全。

## 前提与局限性

- **前提**: 
  1. 额外预算在给定任务中可能有增益，需按已验证发现及风险减少量测量
  2. 有明确的硬化成功标准
- **局限性**: 
  1. 深度验证可聚焦稳定版本，但架构安全与高风险设计不能推迟
  2. 预算上限需人工决策
- **其他边界**:
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

- 持续安全实践与按风险的独立评估互补，非取消一次性审计
- 代码生成成本不能代表安全交付总成本
- 硬化成本由风险、工具与推理成本、专业人员、修复与运营等共同决定
- 安全团队需要把硬化预算、发现数量、严重度、修复率和回归测试一起纳入工程仪表盘
