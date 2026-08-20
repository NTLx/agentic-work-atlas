---
type: entity
title: Show and Tell Adoption
aliases:
  - Show-and-Tell Adoption
  - Show and Tell
  - Self-Organized Adoption
  - 演示式自组织采纳
definition: "AI 工具内部推广的自组织模式——通过公开演示（write-up canvas、show-and-tell channel）让 adoption 自然传播，而非 mandate 或强制；前提是'felt value' > 'mandate'"
created: 2026-08-20
updated: 2026-08-20
tags:
  - organization
  - adoption
  - culture
  - change-management
evidence_level: medium
claim_type: mixed
related_entities:
  - "[[Human-Agent-Teams]]"
  - "[[Conversation-as-Knowledge-Base]]"
  - "[[AI-Adoption-Barbell]]"
  - "[[Slop-Proxy]]"
  - [[Capability-Overhang]]
source_raw:
  - "[[20260820-slack-human-agent-teams]]"
---

# Show and Tell Adoption（演示式自组织采纳）

> [!definition] 定义
> **Show and Tell Adoption** 是 Slack 通过公开演示让 AI 工具 adoption 自组织传播的内部推广模式——典型做法是 PM 写 canvas 分享"我怎么用 Claude"，其他 PM 复制格式，team 自己组织 workshop 并建 git repos；与 Salesforce "How I Slackbot" channel (thousands of members) 同构。**核心机制：felt value > mandate**——员工看到同事的工作产出后自愿采纳，而非被强制。

## 核心机制

```
1 个先行者用 AI 完成显著成果
    ↓
写 public write-up（"what I did and how I did it"）
    ↓
公开在 show-and-tell channel
    ↓
其他 team 复制格式
    ↓
自组织 workshops + git repos
    ↓
adoption 在多个 function 间传播
```

## 案例（Slack + Salesforce）

| 案例 | 机制 | 结果 |
|------|------|------|
| **Slack "How I Slackbot"** | 公开 channel 分享 Slackbot 技巧 | thousands of members |
| **Slack PM 用 Claude** | DevEx lead 帮 PM 设置 → PM 写 canvas 分享 | 其他 PM 复制 |
| **Slack workshops** | team 自组织 | 自建 git repos 沉淀模板 |

Jaime 描述："most self-organized thing you could possibly imagine"

## 原则

1. **Show, don't mandate**: 不强制所有人用新工具，让 adoption 自然发生
2. **Write-ups others can copy**: 一份 "what I did and how" 文档比 training session 更有传播力
3. **Public by default**: 在公开 channel 演示，maximize surface area
4. **Cross-function pollination**: "a trick from a sales process can end up reshaping an engineering process" — 跨职能方法借鉴

## 与传统 change management 对比

| 传统推广 | Show and Tell |
|----------|---------------|
| Top-down mandate | Bottom-up organic |
| Training sessions | Write-ups others copy |
| Required usage | Voluntary adoption |
| Adoption metrics | Felt value |

## 为什么有效

- **Felt value > mandate**: 员工看到同事成果后产生 "I want this too" 内驱
- **Lower barrier to try**: write-up 比 training 更容易上手
- **Cross-pollination**: 不同 function 的方法可借鉴
- **Self-reinforcing**: 越多 write-up → 越多 adoption → 越多 write-up

## 与 [[AI-Adoption-Barbell]] 的关系

- Adoption Barbell 现象：5-10% power users / 70% 几乎不用 / 20% 中间
- Show and Tell 推广**针对中间层**：让 20% 中间层向 5-10% power user 看齐
- 不会消除 Barbell（power user vs 不用 仍存在），但可扩大采用层

## 与 [[Slop-Proxy]] 的边界

- **Show and Tell** 是真实 value 的演示（write-up 含具体经验、可复制）
- **Slop Proxy** 是 false value 的伪装（写 AI 长文但无独立判断）
- **边界**: 演示是否含真实经验？write-up 是否可被独立验证？

## 关键数据点

- 案例来源: Slack CPO Jaime DeLanghe 2026-08 Anthropic blog
- Salesforce "How I Slackbot"：thousands of members
- Slack 内 PM 推 Claude adoption：self-organized

## 前提与局限性

- **前提 1**: 有 willing 先行者（demo or champion）
- **前提 2**: 组织有 psychological safety 接受不完美 demo
- **前提 3**: 有公开分享的渠道（channel / wiki）
- **selection bias**: 案例都是成功的 attempt；失败案例未讨论
- **不适用 mandate 场景**: 合规、safety-critical 流程必须强制（不能 show-and-tell）
- **依赖工具可演示性**: AI 工具的成果需可被展示（不易量化的 workflow 难推广）

## 实施建议

1. **Stand up show-and-tell channel**: 公司范围或 team 范围
2. **鼓励 write-ups**: 模板 "what I did and how I did it"
3. **Cross-function exposure**: 不同 function 的 channel 互通
4. **Avoid show-and-tell mandates**: 不要强制所有人做 write-up（自组织）

## 关联概念

- [[Human-Agent-Teams]] — show-and-tell 是 adoption 的关键路径
- [[Conversation-as-Knowledge-Base]] — show-and-tell channel 是公开 KB 的一部分
- [[AI-Adoption-Barbell]] — show-and-tell 推动中间层向 power user 看齐
- [[Slop-Proxy]] — 演示与 proxy 的边界
- [[Capability-Overhang]] — show-and-tell 让其他员工看到 capability 的实际用法
- [[Excellence-as-Operating-System]] — 高 talent density 文化更易自组织推广