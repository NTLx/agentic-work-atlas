---
type: entity
title: YAGNI
aliases:
  - YAGNI
  - You Aren't Gonna Need It
  - 你不需要它
definition: "敏捷软件开发中的克制原则，要求不要提前实现当前尚未被真实需求证明需要的功能"
created: 2026-04-21
updated: 2026-05-26
tags:
  - agile
  - software-engineering
  - design-principle
related_entities:
  - '[[Laziness-Virtue]]'
  - '[[Martin-Fowler]]'
  - '[[Agentic-Engineering]]'
  - '[[AI-Lacks-Laziness]]'
  - '[[Technical-Debt-Avoidance]]'
  - '[[AI-Restraint]]'
source_raw:
  - "[[20260414-martin-fowler-fragments]]"
---

# YAGNI

> [!definition] 定义
> 敏捷软件开发中的克制原则，要求不要提前实现当前尚未被真实需求证明需要的功能

## 为什么重要

YAGNI 是 AI 时代尤其重要的反生成原则。coding agent 让"多写一点"的即时成本下降，但未来维护成本仍然由人类团队和后续 Agent 承担。

Martin Fowler 的 playlist generator 例子说明，人在动手时可能重新发现问题其实更简单；如果直接让 LLM 实现最初设想，它可能快速完成一个过度复杂的方案。YAGNI 要求先问：这个功能、抽象、配置、扩展点，现在真的被需要了吗？

这与 [[Laziness-Virtue]] 相连。人类时间有限，所以会倾向少写、晚写、删除和简化。[[AI-Lacks-Laziness]] 的风险在于模型没有这种未来痛感，容易把系统做大而不是做好。

## 起源与 AI 迁移

- **提出脉络**：Extreme Programming 社群中的敏捷原则。
- **经典表达**：You Aren't Gonna Need It。
- **Fowler 迁移**：Fowler 在 AI 相关 fragments 中用 YAGNI 反思 LLM 是否会过度复杂化个人工具。
- **Agentic 迁移**：在 [[Agentic-Engineering]] 中，YAGNI 应成为 Agent review 标准：生成更快不代表应该生成更多。

## 关键数据点

- YAGNI 要求把未验证的未来需求留到未来，而不是提前把抽象成本加入系统。
- AI 生成能力降低了实现成本，却没有消除阅读、理解、测试、部署、回滚和维护成本。
- [[20260414-martin-fowler-fragments]] 将 YAGNI 与 AI 缺乏懒惰、TDD-for-agents 和 AI 克制放在同一组工程判断中。
- 对 coding agent 的约束不是"不许写代码"，而是"没有当前证据时不要增加结构性复杂度"。

## 在 Agent Review 中怎么用

- 检查是否新增了当前需求没有使用的扩展点、配置项、抽象层或泛化接口。
- 检查 Agent 是否为一个单一场景生成了框架化方案。
- 检查删除代码是否比新增代码更能解决问题。
- 检查测试是否覆盖真实需求，而不是覆盖过度设计后的实现细节。
- 检查 prompt 是否鼓励"完整、可扩展、生产级"而没有说明范围边界。

## 前提与局限性

- **需求前提**：未来需求不确定，提前实现很可能错配真实变化。
- **成本前提**：未实现的功能不产生维护成本，已实现的功能会持续占用理解和测试预算。
- **判断边界**：YAGNI 不反对所有前置设计。安全、数据迁移、公共 API、领域边界和不可逆架构决策可能需要提前规划。
- **误用风险**：把 YAGNI 当成拒绝抽象的借口，会导致复制粘贴、短视设计和未来重构困难。
- **AI 风险**：Agent 可能默认选择泛化实现；团队需要在指令、review 和测试中明确范围约束。

## 关联概念

- [[Laziness-Virtue]] — YAGNI 是懒惰美德的具体实践
- [[Martin-Fowler]] — 推广者，2026 年文章中再次强调
- [[Agentic-Engineering]] — AI 编程需要 YAGNI 约束
- [[AI-Lacks-Laziness]] — AI 缺少少做和简化的自然压力
- [[Technical-Debt-Avoidance]] — 避免因提前泛化制造债务
- [[AI-Restraint]] — 高风险系统需要知道何时不行动

## Martin Fowler 的个人体验 (2026)

Fowler 描述修改 playlist generator 的经历：
- 开始添加新功能 → 发现复杂度增加 → 气馁
- 想起 YAGNI → 删除未需要的部分 → 简化为 24 行代码
- 反思：如果用 LLM，是否会过度复杂化？是否会 LGTM 接受？

> "If I had used an LLM for this, it may well have done the task much more quickly, but would it have made a similar over-complication?"
