---
type: entity
title: Capability Overhang
aliases:
  - Capability Overhang
  - capability overhang
  - Capability overhang
definition: "OpenAI 设计团队观察到的现象——模型能力远超大多数用户的实际使用，多数人只用到模型能力的一小部分（vast majority getting a sliver of the true value）；为这一 overhang 设计意味着默认体验要极简，把 cutting edge 留给 care 的用户"
created: "2026-08-17"
updated: "2026-08-17"
tags:
  - design
  - ai-era
  - openai
  - product-philosophy
related_entities:
  - "[[Ian-Silber]]"
  - "[[OpenAI-Design-Team]]"
  - "Broad-Spectrum-User（forward reference，单源待建）"
  - "[[Just-Do-Less]]"
source_raw:
  - "[[20260816-openai-head-of-design-best-time]]"
---

# Capability Overhang（能力悬垂）

> [!definition] 定义
> **Capability Overhang** 是 OpenAI Head of Design Ian Silber 描述的产品现象——AI 模型的实际能力远超典型用户的实际使用，多数人只用到模型能力的一小部分（a sliver of the true value）。产品设计需要承认这个 overhang：默认体验保持极简，把 cutting edge 留给"care"的用户；让 capability 增长到被自动发现，而非强迫用户面对。

## 核心命题

```
模型能力 >> 典型用户使用
  → 把 cutting edge 暴露给 100% 用户会 overwhelm
  → 把 cutting edge 藏起来又会浪费 overhang
  → 解决：分层默认体验
     - 默认 = 极简、streamlined、任何人都能用
     - cutting edge = 桌面 app / Codex / ChatGPT Work（给高级用户）
     - 终极目标：distill 到主体验，让用户"don't have to think about a switch or a mode"
```

## Ian 的原话

> "We believe in this idea of this is sort of capability overhang where the product, vast majority of the people are getting a sliver of the true value that they could out of the model. That's not necessarily a bad thing. They're still getting tons of value."

> "We focus on creating an extremely simple, streamlined experience for many, many people. And then we put all of the cutting edge stuff... we also make sure to give that and make sure that's really accessible for the people that care."

> "Eventually... things will truly become for billions of users when they don't have to think about a switch or a mode or anything like that."

## 跨域同构

- **Excel 95% 用户只用 5% 功能** —— 同样的 capability overhang 现象
- **AutoCAD 多数项目只用基础建模** —— 同上
- **Vibe-Coding 中的 vibe coder** —— 用 5% 框架完成 80% 工作（[[Vibe-Coding]]）
- **iPhone 早期 vs 后期** —— 早期能力被开发给开发者，后期能力被 distill 给大众

## 与 Broad Spectrum User 的关系

Capability overhang 是 broad spectrum user 现象的**结构原因**：

```
Capability overhang（能力远大于使用）
  + Broad spectrum user（用户能力分布广）
  → ChatGPT 同时服务"问疹子"和"建 Salesforce"两类用户
```

## 设计推论

- **极简默认**：与 [[Just-Do-Less]] 直接关联——overhang 越大，越要克制
- **Adaptive interface**：根据用户上下文（novice / power user）给不同 affordances
- **Layered exposure**：desktop app / Codex / ChatGPT Work 是 cutting edge 入口
- **Distill 方向**：overhang 最终要被 distill 到主体验，不留 mode 切换

## 前提与局限性

- **前提**：产品确实 capability overhang（如果模型/工具只解决具体问题，overhang 概念不适用）
- **前提**：用户分层（如果全是 power user，overhang 概念不需要）
- **Ian 的限制**：capability overhang 是 OpenAI/ChatGPT 特有现象，不一定适用于其他 AI 产品（如 Notion、Cursor 用户分层较窄）
- **演化问题**：当 capability 被 distill 后，overhang 转化为 "默认体验的丰富度"——但 distill 需要时间

## 反例

- **窄用户产品**：Notion、Cursor、Figma 主要服务一类用户，overhang 不是关键设计挑战
- **early-stage 产品**：capability 不足，没有 overhang 问题
- **B2B 嵌入式产品**：用户被 role 限定，不需要面对 broad spectrum