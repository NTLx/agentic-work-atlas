---
type: entity
title: Research Preview
aliases:
  - Research Preview
  - 研究预览
definition: "将发布从重型承诺降维为轻量试探的产品策略——功能以\"早期实验版本\"上线，收集反馈，不保证长期支持"
created: 2026-05-08
updated: 2026-05-26
tags:
  - product-management
  - AI
related_entities:
  - "[[Cat-Wu]]"
  - "[[AI-Native-Shipping]]"
  - "[[Product-Overhang]]"
  - "[[PM-in-AI-Era]]"
  - "[[Model-Introspection]]"
source_raw:
  - "[[How Anthropic’s product team moves faster than anyone else - Cat Wu (Head of Product, Claude Code)]]"
  - "[[Anthropic's Boris Cherny: Why Coding Is Solved, and What Comes Next]]"
---

# Research Preview（研究预览）

> [!definition] 定义
> **Research Preview（研究预览）** 是一种产品发布策略：几乎每个新功能都先以"Research Preview"标签上线，明确告诉用户该功能是早期版本、正在收集反馈、可能不被长期支持。这种策略通过降低发布的承诺成本，将发布从需要市场/法务/销售多部门协同的重型事件变为轻量试探。

## 关键数据点

- **心理门槛效应**：Research Preview 消除了团队对"完美发布"的心理枷锁——不完美的版本也可以 ship
- **覆盖范围广泛**：Anthropic "绝大多数功能"都采用此方式——这是系统性策略而非例外
- **用户期望管理**：标签本身即沟通——不需要每次额外解释"这不是最终版本"
- **反馈闭环加速**：早发布→早反馈→早迭代，形成 compounding speed advantage
- **与 Product Overhang 协同**：当模型能力溢出（有潜力但未完全成熟），Research Preview 允许产品先"预占位置"

## 前提与局限性

- 依赖用户群对不确定性的容忍——developer tools 用户天然更能接受"不保证支持"。
- 如果滥用（每个功能永远停留在预览阶段），用户信任会消退。
- 安全敏感功能需要更审慎——Research Preview 不适用于可能造成实质性损害的场景。

## 从承诺到探针：发布的本质转变

传统发布的本质是**承诺**："这个功能稳定、会被长期支持、出了 bug 我们负责"。这要求市场、法务、文档、支持等多部门协同，让每次发布成为重型事件。

Research Preview 把发布变成了**探针**："这个能力我们正在测试，想让你试试，可能随时调整或撤回"。这带来三层组织效应：

| 效应 | 机制 | 结果 |
|------|------|------|
| 降低心理门槛 | 不需要"完美才发布" | 不完美的功能也能 ship |
| 加速反馈循环 | 早发布 → 早反馈 → 早迭代 | compounding speed advantage |
| 预留产品位置 | 为模型能力溢出"占位" | 模型追上来时产品已就绪 |

这个策略与 [[Product-Overhang|产品能力溢出]] 形成协同：当模型已具备某能力但产品界面尚未成熟时，Research Preview 允许团队先释放一个"学习接口"，用真实用户反馈来决定是否需要加固。

## 可复制性边界

Research Preview 的可复制性取决于三个条件：

1. **用户群容忍度**：developer tools 用户天然更能接受"不保证长期支持"；面向 enterprise 或消费者市场时，需要更强的期望管理。
2. **撤回纪律**：如果每个功能永远停留在预览阶段，标签就从"学习信号"退化为"推卸责任的挡箭牌"。
3. **升级路径清晰**：用户需要知道什么条件下 Research Preview 会变成 GA（General Availability），否则信任会持续流失。

## 关联概念

- [[AI-Native-Shipping]] — Research Preview 是极速发布的引擎。
- [[Product-Overhang]] — 为还没完全成熟的模型能力提前预留产品接口。
- [[PM-in-AI-Era]] — Research Preview 是 PM 高速公路的"低摩擦出口"。
- [[Model-Introspection]] — 发布后的模型自省可以帮助判断 Research Preview 是否值得加固。
