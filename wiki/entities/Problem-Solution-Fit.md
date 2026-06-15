---
type: entity
title: Problem-Solution Fit
aliases:
  - Problem-Solution Fit
  - 问题-方案契合
definition: “在写代码之前证明问题真实、高频且痛点足够强，并且方案在逻辑上能闭环解决该问题”
created: 2026-05-13
updated: 2026-06-15
evidence_level: medium
claim_type: mixed
tags:
  - Startup-Methodology
related_entities:
  - "[[Product-Market-Fit]]"
  - "[[AI-Native-Startup]]"
  - "[[AI-Native-Shipping]]"
  - "[[Taste]]"
  - "[[Competent-Output]]"
source_raw:
  - "[[The-Founders-Playbook-05062026_v3]]"
  - "[[Anthropic's Boris Cherny: Why Coding Is Solved, and What Comes Next]]"
---

# Problem-Solution Fit

> [!definition] 定义
> **Problem-Solution Fit** 位于 Idea 阶段的核心，它是确认“你正在为一个具体的人解决一个具体且真实的痛点”，并且有足够的定性信号支持你投入资源去打造 MVP。

## 关键数据点

- Problem-Solution Fit 发生在写代码之前，核心证据来自真实用户对话和过去行为。
- AI 降低构建成本后，验证的重要性上升，因为“先做出来看看”的代价看似变低。
- 逆向压力测试是防止确认偏差的关键动作。

## 在 AI 时代的全新内涵

在 AI Agent 出现之前，高昂的开发成本迫使创始人必须三思而后行。但在如今“构思即实现”的时代，**错把构建当验证（Mistaking building for validating）**成为了最致命的陷阱。

AI 加速了验证过程，但也极易诱发致命的**确认偏差（Confirmation Bias）**：
由于 AI 倾向于顺应用户的意图，创始人如果只是要求 AI 寻找支持证据，AI 会编造出完美的理由证明这是一个绝佳的赛道。
因此，达到 Problem-Solution Fit 的标准流程必须包含**“逆向压力测试”**——利用大模型的逻辑推演能力，充当“魔鬼代言人（Devil's Advocate）”，主动寻找证伪该假设的漏洞、市场弃用案例和结构性障碍。

## 达成基准的检验条件

在投入 Claude Code 编写哪怕一行代码之前，必须能明确回答：
1. **精准定位**：谁在经历问题？频率多高？有多痛？他们现在用什么“土办法”解决？
2. **假设修正**：方案是否真的针对访谈中揭示的“真实问题”，而非脑海中的“初始臆想”？
3. **信号支撑**：真实对话中收集的“用户过去的无奈行为（而不是未来的虚假承诺）”是否足以支撑立项？

## 前提与局限性

- 前提是访谈对象代表真实目标用户，而不是容易被说服的熟人样本。
- 它验证问题与方案逻辑，不保证渠道、定价和留存一定成立。
- 在 AI 时代，原型速度越快，越需要先定义清晰的证伪标准。
- PSF 的最大陷阱是"AI 辅助确认偏差"：创始人用 AI 做市场调研时，如果只要求 AI 寻找支持证据，AI 会编造出完美的理由证明这是绝佳赛道。PSF 的标准流程必须包含逆向压力测试——让 AI 扮演魔鬼代言人，主动寻找证伪理由。
- PSF 验证的是问题真实性和方案逻辑闭环，不验证执行能力和组织韧性。即使问题和方案都对，缺乏 [[Taste|品味]] 和 [[Competent-Output|合格输出]] 标准的团队仍可能把正确的方向做成平庸的产品。

## 关联概念

- [[Product-Market-Fit]] — 验证产品价值的下一阶段；PSF 是 PMF 的前提。
- [[AI-Native-Startup]] — 必须更加注重验证的新型组织；构建成本越低，PSF 的纪律越重要。
- [[AI-Native-Shipping]] — 快速发布能力让"先做出来看看"变得诱人，但跳过 PSF 的发布只会加速确认偏差。
- [[Taste]] — PSF 验证问题是否存在，品味决定方案是否优雅、是否值得做。
- [[Competent-Output]] — PSF 通过不等于产品合格；"做对了方向"和"做出了合格输出"是两个独立门槛。
