---
type: entity
title: "Skill 内化"
aliases:
  - Skill Internalization
  - 内化 Skill
  - 技能内化
definition: "理解外部技能的机制与适用条件，并选择直接复用或按本地规则适配，经验证后沉淀为可维护技能的工程实践；非必然优于安装。"
created: 2026-05-29
updated: 2026-11-28
evidence_level: medium
claim_type: mixed
tags:
  - skill-engineering
  - knowledge-management
  - claude-code
related_entities:
  - "[[Knowledge-Compilation]]"
  - "[[Compound-Engineering]]"
  - "[[Three-Layer-Agent-Memory]]"
  - "[[Agent-Harness]]"
source_raw:
  - "[[20260526-obsidian-claude-code-brain]]"
  - "[[Every Agentic Engineering Hack I Know (June 2026)]]"
---

# Skill 内化

> [!definition] 定义
> 将外部技能的设计思想、可用工作流与适用边界转化为本地可复用能力。个人实践称为“内化”，并非必须重写外部技能，也不改变原有许可和来源责任。

## 直接复用与适配

| 选择 | 适用情境 | 风险 |
|---|---|---|
| 直接安装或复用 | 接口、依赖、规则及授权兼容，可信来源与更新路径明确 | 隐藏依赖、权限扩张、规则冲突 |
| 局部适配 | 有明确环境、流程或风格差异 | 维护分叉、回归遗漏、上游修复不同步 |
| 自建 | 现有方案无法满足实质目标 | 额外设计与长期维护成本 |

## 内化与晋升合同（本库综合）

先阅读来源、许可、接口及实际工作流；对照已有能力、规则与权限，尽量复用最小必要部分。将可复用经验与一次性上下文分开，记录适用条件、版本、失败边界及成功判据。用代表性任务及必要负向测试验证，确认净收益与维护责任，再批准晋升。后续变化时复核、升级或撤销。成功次数只是候选发现信号，不能代替证据独立性或风险验收。

## 关键数据点

- [[20260526-obsidian-claude-code-brain]] §04：作者选择完整阅读外部Skill、提炼设计思想、结合本地语料再组织；SKILL.md不超过200行并按需加载references/scripts是其个人约定，不是通用硬限制。原Raw未包含旧实体中卡兹克五级质检、100+手改稿、30%故事占比及几十个技能等具体案例，撤出未核实细节，历史仍可查。
- [[Every Agentic Engineering Hack I Know (June 2026)]] Raw L304–316：Matt Van Horn描述工作重复超过两次时考虑制作skill，引用成熟Skill结构搭建新能力。属于作者启发式，不是经济收益或永久有效保证。

## 前提与局限性

重写可能丢失有效语义、依赖、边界和测试；外部Skill指令不自动取得更高权限。优先简单复用，适配前后检验行为与实际结果，必要时保留原版或可回滚版本。许可、隐私、供应链与数据范围分别判断。2026-11-28回读个人Vault原文及Matt相关Raw段落，未复现技能效果或完整核查Matt全部文章。本轮仅修订知识页。

## 关联概念

- [[Knowledge-Compilation]]、[[Compound-Engineering]] — 经验提炼、复用与净收益。
- [[Three-Layer-Agent-Memory]]、[[Shared-Memory-Contamination]] — 晋升与纠错边界。
- [[Agent-Harness]]、[[Capability-Map]] — 发现、执行和验收。
