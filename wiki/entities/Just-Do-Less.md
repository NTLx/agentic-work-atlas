---
type: entity
title: Just Do Less
aliases:
  - Just Do Less
  - just do less
  - Do Less
definition: "OpenAI 设计负责人 Ian Silber 提出的反直觉 AI 产品设计原则：在 AI 时代优先复用现有 system 组件、扩展已有功能，而非发明新功能或新组件；背后假设是产品快速变化 → 减少重设计风险"
created: "2026-08-17"
updated: "2026-08-17"
tags:
  - design
  - ai-era
  - method
  - openai
related_entities:
  - "[[Ian-Silber]]"
  - "[[OpenAI-Design-Team]]"
  - "[[Systems-Thinking]]"
  - "[[Capability-Overhang]]"
source_raw:
  - "[[20260816-openai-head-of-design-best-time]]"
---

# Just Do Less（少做）

> [!definition] 定义
> **Just Do Less** 是 OpenAI Head of Design Ian Silber 在 AI 产品设计中的反直觉原则——面对模型快速演化、产品形态每天都在变的环境，主动克制"发明新组件/新功能"的冲动，优先复用现有 system primitives 或扩展已有功能。这与 [[Build-First-Business-Ontology]] 中"ontology 优先于 UI"的论证同构。

## 核心命题

```
如果产品每 30 天都在变：
  → 任何"重设计"的高成本投入都是浪费
  → 复用 > 新建
  → 扩展 > 创造
  → 设计 effort 应集中在"durable"且"model-stable"的事物上
```

## Ian 的原话

> "Just do less. Don't design it if you don't have to, maybe there's already an existing system or component or something that we can build on top of, or maybe we don't even need this feature. We actually just need to extend an existing feature."

> "Pick your battles... focus the design effort on the things that will be durable and not change."

## 与 Instagram "do the simple thing first" 的关系

Ian 自陈从 Instagram 带到 OpenAI 的方法论迁移：

| 公司 | 原则 | 速度假设 | 适用场景 |
|------|------|----------|----------|
| Instagram | "do the simple thing first" | 8 年成熟产品，慢节奏 | stable 产品功能 |
| OpenAI | "Just do less" | 模型每月变化，产品每日变化 | research lab 节奏 |

两者本质同构——"复用 > 发明"——但适用场景取决于产品 stability。

## 适用边界（来自 Ian 自己）

- **依赖前提**：产品已存在可复用的 system primitives（零起步产品不适用）
- **依赖前提**：团队 velocity 极高、产品快速演化（slow-moving 产品不适用）
- **Ian 自己说**："it depends on what stage you're at in the process... there are certain features for ChatGPT where we really obsess... and other things we really embrace building in public"
- **没给出判别标准**：Ian 没明说"哪些 feature 走 sweat the details，哪些走 ship in 4 hours"

## 反例与质疑

- **stable enterprise 产品不适用**：在银行、医疗、政府软件等"模型不变、业务不变"的场景下，"Just do less" 可能退化为"功能不够"
- **早期产品不适用**：从 0 到 1 的产品没有 primitives 可复用
- **风险**：过度"do less"可能导致产品缺乏差异化（被 capability overhang 压缩）

## 与相关概念的关系

- [[Systems-Thinking]]：Just do less 是 systems thinking 在设计领域的具体应用——优先复用 system primitives
- [[Capability-Overhang]]：当 capability overhang 严重时（多数人只用 5% 功能），"do less" 是合理策略
- [[Build-First-Business-Ontology]]：ontology 优先于 UI 的原则与"Just do less"同构
- [[Vibe-Coding]]：vibe coder 滥用"Just do less"会产出不可维护代码——边界要靠 taste 把握

## 关键数据点

- Ian Silber 2026-08 Lenny 访谈原文："Just do less. Don't design it if you don't have to"
- Ian 自陈从 Instagram "do the simple thing first" 口号带到 OpenAI
- 两档设计 effort：某些 feature "sweat the details"（100 try 99 throw out），某些 "ship in 4 hours"
- 反例条件：stable enterprise 产品 / 早期产品 / 0→1 阶段不适用
- OpenAI 模型每月变化、产品每日变化——research lab 节奏决定"Just do less"成立

## 前提与局限性

- 依赖前提：产品已存在可复用的 system primitives（零起步产品不适用）
- 依赖前提：团队 velocity 极高、产品快速演化（slow-moving 产品不适用）
- Ian 自己承认："it depends on what stage you're at in the process"——判别标准未明说
- 风险：过度 do less 可能导致产品缺乏差异化，被 capability overhang 压缩
- 在银行/医疗等稳定业务中"Just do less" 可能退化为"功能不够"

## 关联概念

- [[Ian-Silber]] — 原则提出者
- [[Systems-Thinking]] — Just do less 是 systems thinking 在设计领域的应用
- [[Capability-Overhang]] — Overhang 严重时 do less 是合理策略
- [[OpenAI-Design-Team]] — 团队层面的实践
- [[Build-First-Business-Ontology]] — ontology 优先于 UI 与 Just do less 同构
- [[Vibe-Coding]] — vibe coder 滥用 Just do less 的边界要靠 taste
- [[Taste]] — Just do less 的边界判断靠 taste 把握