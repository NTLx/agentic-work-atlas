---
type: topic
title: AI-Era Career Skills
created: 2026-04-09
updated: 2026-05-23
tags:
  - AI-Agent
  - productivity
  - career
related_entities:
  - '[[Judgment]]'
  - '[[Model-Introspection]]'
  - '[[Taste]]'
  - '[[Forward-Deployed-Engineer]]'
  - '[[Claude-Code-CLI]]'
  - '[[Agent-Tenacity]]'
source_raw:
  - '[[20260127-claude-coding-notes]]'
  - '[[Forward deployed engineering at OpenAI]]'
  - '[[Forward Deployed Engineer (FDE) - NYC]]'
  - '[[OpenAI launches the OpenAI Deployment Company to help businesses build around intelligence]]'
  - '[[A Day in the Life of a Palantir Forward Deployed Software Engineer]]'
---

# AI-Era Career Skills

> [!info] 主题概述
> 本主题探讨 AI 时代职业技能的演化——从 Prompt 到 Skill，从知识积累到智慧工作，以及如何利用 AI 工具重构工作流程。

## 核心概念

### 1. 从手动执行到调度 Agent

Karpathy 的 Claude coding notes 显示，AI 编程技能的核心变化不是“会不会写 prompt”，而是工作方式从手写细节转向用自然语言调度大粒度 code actions。

他把自己的工作流变化描述为：从 2025 年 11 月的约 `80%` 手动编码、`20%` agent 辅助，迅速转成 2025 年 12 月的约 `80%` agent 编码、`20%` 人工编辑和修补。这是个人经验，不是行业统计，但它说明一个方向：职业技能正在从“亲手生成”转向“设定目标、约束边界、审查结果”。

### 2. 杠杆来自成功标准，而不是命令清单

Agent 最擅长的是在明确目标下循环尝试。Karpathy 的方法建议是：

- 先写测试，再让 agent 通过测试。
- 给出成功标准，而不是一步步命令。
- 先写朴素但更可能正确的算法，再在保持正确性的前提下优化。
- 把 browser MCP、测试、运行反馈放进闭环。

这意味着 AI 时代的职业技能更接近“设计可验证任务环境”：把目标、约束、反馈和验收标准组织好，让 agent 可以长时间自主推进。

### 3. 判断力比生成力更稀缺

模型的错误不再主要是语法错误，而是概念性错误：替用户补前提、不主动澄清、不暴露矛盾、过度复杂化、顺手改掉无关代码。

因此，人的关键能力不是“生成更多”，而是：

- 看出 agent 什么时候在错误前提上继续前进。
- 要求它暴露困惑、权衡和边界条件。
- 把臃肿实现压回更简单的方案。
- 在代码可运行之外审查概念是否正确。

## 关键洞察

### Model Introspection：把错误变成技能

AI 时代的高阶技能不只是会写 prompt，还包括让模型解释自己的错误路径。[[Model-Introspection|模型自省]] 能把一次失败转化为可复用的调试规则：为什么模型会误判、它默认补了什么前提、下次应该给什么约束。

这类能力属于判断力训练，而不是工具熟练度训练。

### FDE：把模型接进真实工作流的人

**Forward Deployed Engineer（FDE，前线部署工程师）** 不是“又一种 prompt 工程师”，而是把模型能力翻译成组织结果的部署角色。

OpenAI 官方职位页把这个岗位写成一条完整闭环：从 `discovery`、`technical scoping` 到 `system design`、`build`、`production rollout`，并用 `production adoption`、`workflow impact`、`eval-driven feedback` 衡量成功。

Palantir 的官方解释补了一条更结构性的对照：传统软件工程更像“为很多客户做一个能力”，FDSE 更像“为一个客户启用很多能力”。这说明 FDE 的核心不是抽象封装，而是把既有模型、平台和约束条件拼成能跑起来的系统。

**一手材料能确认的行业信号**:
- OpenAI 已为此建立独立部署实体，并明确把 deployment 到 product 的循环写成 `build, prove, generalize`。
- Palantir 证明这种角色不是 AI 热潮临时产物，而是一种长期存在的部署形态。

这标志着 AI 行业的竞争重点继续从“谁会做模型”往“谁能把模型接进真实流程”移动。

## 相关概念

- [[Judgment]] - Skill 放大判断力，不替代思考
- [[Taste]] - 优质 Skill 需品味设计工作流程
- [[Model-Introspection]] - 从模型错误中提炼可复用调试经验
- [[Wisdom-Work]] - 知识工作正在向智慧工作转变
- [[Forward-Deployed-Engineer]] - AI 时代新岗位：驻扎客户现场，用代码而非 PPT 交付 AI 集成
