---
type: entity
title: WCAG
aliases:
  - WCAG
  - Web Content Accessibility Guidelines
  - Web 内容无障碍指南
definition: "W3C 制定的 Web 内容无障碍指南，包含 55 个级别 A 和 AA 成功标准，其中仅 64% 可通过自动代码检查器检测，约 36% 需人工评估"
created: 2026-05-18
updated: 2026-05-26
tags:
  - accessibility
  - standard
  - W3C
related_entities:
  - "[[Accessibility-Agent]]"
  - "[[Accessibility-High-Risk-Patterns]]"
  - "[[Accessibility-Complexity-Evaluation]]"
  - "[[Verifiability]]"
  - "[[Social-Model-of-Disability]]"
source_raw:
  - "[[Building a general-purpose accessibility agent—and what we learned in the process]]"
  - "[[The Conscious 1% Leading a new renaissance in the era of AI]]"
---

# WCAG

> [!definition] 定义
> **WCAG（Web Content Accessibility Guidelines，Web 内容无障碍指南）** 是 W3C 制定的 Web 内容无障碍标准。当前版本 WCAG 2.2 包含 55 个级别 A 和 AA 成功标准，其中仅 35 个（64%）可通过自动代码检查器检测，约 36% 需要人工评估。

## 自动化检测的边界

| 类型 | 数量 | 比例 |
|------|------|------|
| 可自动检测 | 35 个 | 64% |
| 需人工评估 | ~20 个 | ~36% |

LLM Agent 正在缩小这 36% 的差距，但这不是完美科学。

## 法规驱动

- **欧洲无障碍法案（EAA）**：已生效，要求数字产品符合 WCAG 标准
- **美国 ADA 第二章**：2027 年 4 月起，将 WCAG 2.1 AA 确立为法律意义上的"完成标准"

组织如果尚未投入无障碍问题识别和修复，将在未来处于劣势。

## 关键数据点

- WCAG 2.2 级别 A + AA 共 **55 个成功标准**
- 仅 **64% 可自动检测**，36% 需人工判断
- 欧洲 EAA 已生效，美国 ADA 2027 年 4 月生效

## 前提与局限性

- WCAG 是最低标准而非目标——合规不代表可用，不合规一定不可用。
- 自动检测器只能验证代码层面的合规性，无法验证实际辅助技术使用体验。
- 不同国家和地区对 WCAG 版本的法律引用不同（2.0/2.1/2.2），需注意适用版本。

## 36% 缺口的本质

WCAG 2.2 的 55 个 A/AA 成功标准中，约 36% 需要人工评估。这个缺口不是技术暂时无法解决的，而是结构性的——它对应的是需要理解**使用意图、上下文和辅助技术交互体验**的标准。

| 可自动检测（64%） | 需人工评估（36%） |
|-------------------|------------------|
| alt 属性是否存在 | alt 文本是否准确描述内容 |
| 颜色对比度数值 | 颜色是否传达必要信息 |
| 标签是否关联控件 | 标签是否帮助用户理解操作 |
| 焦点顺序是否存在 | 焦点顺序是否符合逻辑流程 |

LLM Agent 正在缩小这 36% 的差距，但不是以替代人工评估的方式——而是以增强评估覆盖面的方式。GitHub 的 accessibility agent 已 review 3,535 个 PR，resolution rate 为 68%。关键发现是：LLM 训练语料中充满几十年的 inaccessible code，模糊要求它"使用 accessibility best practices"效果不好；组织内部经过验证的历史 issue 和修复 PR 才是最强资产。

## 高风险模式的识别

即使 WCAG 检测通过，某些交互模式仍然具有高风险。GitHub 的实践列出了 drag and drop、toast、rich text editor、tree view、data grid 等模式，禁止 Agent 自动生成修复——这些需要 [[Accessibility-Complexity-Evaluation|复杂度评估]] 后由人类或专业团队处理。

这与 [[Verifiability|可验证性]] 形成交叉：WCAG 合规中"可自动验证"的部分可以大胆自动化，"需人工评估"的部分需要 Agent 做初筛 + 人类最终判断，而高风险交互模式则需要完全保留人类决策。

## 关联概念

- [[Accessibility-Agent]] — 无障碍 Agent 以 WCAG 成功标准为核心评审依据。
- [[Accessibility-High-Risk-Patterns]] — 即使 WCAG 检测通过，某些交互模式仍可能实际不可用。
- [[Accessibility-Complexity-Evaluation]] — 判断哪些 WCAG 问题适合 Agent 自动修复的评估机制。
- [[Verifiability]] — WCAG 合规中可自动验证 vs 需人工评估的分工是可验证性原则的具体体现。
- [[Social-Model-of-Disability]] — WCAG 的理论基础：障碍来自设计而非个体缺陷。
