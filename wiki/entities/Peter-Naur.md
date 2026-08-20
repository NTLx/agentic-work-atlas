---
type: entity
title: Peter Naur
aliases:
  - Peter Naur
  - Naur
  - Peter Naur 1985
definition: "丹麦计算机科学家（1928-2016），1985 年论文《Programming as Theory Building》提出「代码是软件开发的输入而非输出」的核心论断；这一论断在 LLM 时代被多个 skeptic 重新引用，挑战「代码行 = 生产力」的主流叙事"
validated_source: "https://pablo.rauzy.name/dev/naur1985programming.pdf"
validated_at: "2026-08-19"
created: "2026-08-19"
updated: "2026-08-19"
tags:
  - author
  - software-philosophy
  - classical-theory
related_entities:
  - "[[Joshua-Barretto]]"
  - "[[Horn]]"
  - "[[Taste]]"
  - "[[Judgment]]"
source_raw:
  - "[[20260814-i-remain-a-skeptic]]"
---

# Peter Naur（1928-2016）

丹麦计算机科学家，图灵奖获得者（2005，与 Ole-Johan Dahl 共获）。其 1985 年论文《Programming as Theory Building》是软件工程哲学的奠基性论述之一。

## 核心命题：代码是输入不是输出

> "code is an input to the software development process and not an output"

Naur 在 1985 年提出：软件开发的产出不是代码，而是开发者对系统的**理论理解**——程序是理论的具体化（artifact），不是结果。代码本身可以被替换，但理论不能——这就是为什么软件维护的核心是维护对系统的理解，而非修改代码。

## LLM 时代的回归

Naur 1985 在 40 年后被多个 AI 时代 skeptic 重新引用：

- [[Joshua-Barretto]]："Peter Naur remains undefeated"——即使在 LLM 让代码生成自动化，Naur 的论断更凸显
- 与 [[Horn]] 的"agentic orchestration = program management"同源——程序的"理论"维度不能被 AI 替代

## 与库中概念的对标

- 与 [[Taste]] 的"ability-taste flip"同构：AI 让 code ability 普遍化，theory/taste 反而稀缺
- 与 [[Judgment]] 同构：判断力是"理论"在 AI 时代的最直接表现
- 与 Ian Silber 在 [[20260816-openai-head-of-design-best-time]] 中"设计是 judgment loop"的论断同构

## 可验证链接

- 原文: https://pablo.rauzy.name/dev/naur1985programming.pdf
- Wikipedia: https://en.wikipedia.org/wiki/Peter_Naur
- Turing Award: https://amturing.acm.org/award_winners/naur_1477614.cfm

## 关键数据点

- Peter Naur 生卒 1928-2016
- 1985 年论文《Programming as Theory Building》
- 2005 年图灵奖（与 Ole-Johan Dahl 共获）
- 核心命题原文："code is an input to the software development process and not an output"
- 软件维护的核心是维护对系统的理解，而非修改代码——程序是理论的具体化
- 40 年后被多个 AI 时代 skeptic 重新引用：jsbarretto "Peter Naur remains undefeated"
- 与 Horn "agentic orchestration = program management" 同源——理论的维度不能被 AI 替代

## 前提与局限性

- 1985 年观点基于传统软件工程，AI 时代代码生成自动化后理论维度的体现可能改变形式
- "理论不可被 AI 替代" 取决于对"理论"的定义——若理论包括代码生成中的隐式判断，AI 已部分承担
- jsbarretto 等引用者以 Naur 论断作为 AI 怀疑论的核心，但 Naur 本人未必同意这种重新解读
- Naur 的命题偏抽象，工程实践中的可测量指标（如维护成本）未充分对应
- 经典理论在新范式下的适用边界需要 cross-check，不能简单外推

## 关联概念

- [[Joshua-Barretto]] — 重新引用 Naur 最多的作者
- [[Horn]] — 同引用者，agentic orchestration = program management
- [[Taste]] — AI 让 code ability 普遍化，theory/taste 反而稀缺
- [[Judgment]] — 判断力是 "theory" 在 AI 时代的最直接表现
- [[Mythical-Man-Month]] — 与 Naur 并称的软件工程哲学经典
- [[Theory-of-Mind]] — 理解他人心智是理论构建能力
- [[Software-Development-Autonomy-Levels]] — 不同自治级别下理论的角色不同