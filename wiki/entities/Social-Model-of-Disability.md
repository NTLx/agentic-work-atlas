---
type: entity
title: Social-Model-of-Disability
aliases:
  - Social Model of Disability
  - 障碍的社会模型
definition: "把障碍理解为环境设计造成的访问壁垒，而不是个人能力缺陷的无障碍思想模型"
created: 2026-05-18
updated: 2026-05-25
tags:
  - accessibility
  - philosophy
related_entities:
  - "[[Accessibility-Agent]]"
  - "[[Accessibility-Complexity-Evaluation]]"
  - "[[Accessibility-High-Risk-Patterns]]"
  - "[[Verifiable-Agent-Engineering]]"
  - "[[Bias-to-Action-LLM]]"
source_raw:
  - "[[Building a general-purpose accessibility agent—and what we learned in the process]]"
---

# Social-Model-of-Disability

> [!definition] 定义
> **障碍的社会模型（Social Model of Disability）** 认为：障碍（disability）和损伤（impairment）并非源于人本身，而是环境被设计的方式所创造的。应用到数字领域：无障碍问题不是用户的问题，而是我们构建用户界面方式的问题。

## 在无障碍 Agent 中的应用

GitHub 的 Accessibility Agent 基于这一哲学：

- **不试图"解决"无障碍问题**：无障碍不是 Agent 能独立完成的孤立任务
- **而是增强人工努力**：Agent 的目的是帮助工程师移除因构建方式而产生的障碍
- **明确不是银弹**：承认 Agent 不能自动解决所有场景，这反而加速了实验推出

> "The social model of disability teaches us that access barriers—and consequently impairment—can be created because of how an environment is built."

## 关键数据点

- 社会模型区分"损伤"（impairment）与"障碍"（disability）：前者是身体状态，后者是社会建构
- 数字无障碍领域：一个界面是否"无障碍"取决于设计决策，而非用户能力
- GitHub Accessibility Agent 的起点不是“让 AI 替用户适应界面”，而是让工程系统更早发现并移除访问壁垒
- 该哲学解释了为什么 Agent 必须内置“不行动”：如果自动修改会制造新的访问壁垒，拒绝和人工升级比生成代码更符合无障碍目标

## 对 Agent 设计的影响

社会模型会把 Agent 的目标从“修 bug”改成“减少环境制造的障碍”。这不是修辞差异，而会改变工程边界：

- Agent 不应把用户能力当作问题源头，而应检查界面结构、交互状态、焦点顺序和辅助技术反馈。
- Agent 不能只追求自动化率，因为错误自动化会把访问壁垒固化进代码。
- Agent 需要引用组织历史审计、WCAG 解读和真实修复 PR，而不是只靠通用训练语料。
- Agent 应把复杂模式升级给人类专家，因为高风险交互往往需要设计、产品和工程共同判断。

因此，社会模型是 [[Accessibility-Agent]] 的价值边界：AI 的任务不是替代残障用户表达需求，而是帮助工程团队承担原本就属于系统设计的责任。

## 前提与局限性

- 社会模型不否认损伤的存在，而是重新定义"问题在哪里"——这是视角转变，而非医学论断
- 在商业语境中，社会模型意味着无障碍投入应归于产品设计和开发团队，而非"特殊需求部门"
- 在 Agent 语境中，社会模型不等于“所有访问问题都能由代码修复”。有些障碍来自产品假设、信息架构、流程设计或组织优先级
- 如果团队只把社会模型当作价值宣言，而没有复杂度门控、人工升级和真实用户测试，它不会自动提升无障碍质量

## 关联概念

- [[Accessibility-Agent]] — 基于社会模型哲学构建的无障碍 Agent
- [[Accessibility-Complexity-Evaluation]] — 将“是否应自动修改”变成工程门控
- [[Accessibility-High-Risk-Patterns]] — 标记可能制造新访问壁垒的交互模式
- [[Verifiable-Agent-Engineering]] — 社会模型要求 Agent 不只生成修复，还要知道何时停止和升级
- [[Bias-to-Action-LLM]] — 模型的行动偏差可能与无障碍责任冲突
