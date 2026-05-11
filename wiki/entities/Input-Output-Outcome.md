---
type: entity
title: Input-Output-Outcome
aliases:
  - Input Output Outcome
definition: "区分代码（输入）、功能（输出）、用户付费（结果）的商业分析框架——AI 大幅提升输入但未必提升结果"
created: 2026-05-11
updated: 2026-05-11
tags:
  - business
  - ai-labor
  - framework
related_entities:
  - "[[Knowledge-Work]]"
  - "[[Allocation-Economy]]"
  - "[[AI-Capability-Gap]]"
source_raw:
  - "[[The layoffs will continue till we learn to use AI]]"
---

# Input-Output-Outcome（输入-输出-结果）

> [!definition] 定义
> 区分代码（输入）、功能（输出）、用户付费（结果）的商业分析框架。AI 大幅提升了输入速度，但输出和结果未必同比例增长。

## 三层模型

| 层级 | 含义 | AI 影响 |
|------|------|--------|
| **Input（输入）** | 代码、PR、diff | AI 直接放大 2-5 倍 |
| **Output（输出）** | 功能、产品变化 | 增幅远低于输入 |
| **Outcome（结果）** | 用户付费、收入 | 几乎未见同比例增长 |

## 核心洞察

AI 工具（如 Claude Code）按 token 计费，本质上是为**输入**付费，而非为**结果**付费。这导致：

- 代码生成量 5 倍增长 → AI 支出 5 倍增长
- 但用户感知的产品几乎未变
- 资产负债表失衡：输入成本增加，收入未增长

## SaaS 定价启示

> [!example] 对比
> 如果销售工具能 "关闭速度快 36%"，可以按销售额的 5% 收费——因为它直接影响 Outcome。但 AI 编码工具按 token 收费——因为它只影响 Input。

## 前提与局限性

- **前提**: 该框架假设代码是输入而非产出本身——在某些组织中，代码本身就是可交付物（如开源项目）
- **前提**: 框架假设存在清晰的因果链（输入→输出→结果），但现实中因果关系更复杂
- **边界条件**: 适用于软件产品公司，不适用于咨询、内容创作等领域
- **局限性**: 框架过于简化——某些 AI 提升的输入确实带来了显著的结果（如 GitHub Copilot 的代码补全减少错误率）

## 关联概念

- [[Knowledge-Work]] - 传统知识工作以"输入"（知识量）衡量价值
- [[Allocation-Economy]] - 从知识经济到分配经济的转型
- [[AI-Capability-Gap]] - AI 提升了输入能力但结果差距仍然存在
