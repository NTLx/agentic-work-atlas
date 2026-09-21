---
type: entity
title: AI-Autonomy
aliases:
  - AI 自主性
definition: "本库对 AI 在任务执行中自主决策程度的工作性概念；Anthropic 的 1–5 任务/产物量表与 Berkeley 的 SDLC 责任转移分级是互补框架，不能合并成单一自治分数"
created: 2026-06-30
updated: 2026-07-28
evidence_level: medium
claim_type: mixed
tags:
  - ai-labor
related_entities:
  - "[[AI-Use-Rhythm]]"
  - "[[AI-Artifact-Classification]]"
  - "[[Software-Development-Autonomy-Levels]]"
source_raw:
  - "[[20260626-anthropic-economic-index-june-2026-report]]"
  - "[[20260726-berkeley-auto-software-dev]]"
---

# AI-Autonomy

> [!warning] 证据身份与边界
> Anthropic Economic Index 提供 Claude 使用遥测中的任务/产物自主性比较；Berkeley 来源提供 position paper 的 Code/Pipeline/Demand autonomy 框架。前者测观察到的产品使用模式，后者讨论 SDLC 责任如何转移；二者不能互相当作同一量表，也不能从中推出所有 AI 产品的自治能力。

## 定义

AI 在任务执行中自主决策的程度，使用1-5级量表测量，从“无”（如简单翻译）到“极端”（如创建应用和网站）。

## 关键数据点

- **在 Anthropic 样本中**，Claude Code 比 Chat/Cowork 具有更高自主性：31 种产物中的 26 种上显示更高自主性（平均高 0.37 点）。这是产品/任务分布结果，不是模型本体的通用自治排名。
- **自主性与计算成本正相关**：高自主性任务消耗更多 token。
- **产品配置可能重要**：Source Summary 将相同模型下的 Claude Code 差异归因于产品/工作流配置；该观察不能单独证明“产品比模型更重要”。

## 高自主性任务

- 创建应用和网站
- 游戏开发
- 演示文稿设计
- 需要持续判断的任务

## 低自主性任务

- 数学计算
- 翻译
- 问答

## 前提与局限性

- 自主性量表是主观的，可能受任务复杂度影响。
- 数据仅基于 Claude，其他 AI 工具可能不同。
- 自主性与价值的关系需要进一步研究。

## 关联概念

- [[AI-Artifact-Classification]]：自主性水平与产物类型相关。
- [[AI-Use-Rhythm]]：非工作时间的任务可能具有更高自主性。
- [[Labor-Market-Impact]]：自主性可能影响劳动力市场结构。
- [[Software-Development-Autonomy-Levels]]：框架互补——本实体测任务类型的自主分布（1-5 量表），后者分 SDLC 阶段的责任转移（三级自治）。
