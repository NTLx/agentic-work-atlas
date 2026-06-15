---
type: entity
title: Custom Policy Guardrails
aliases:
  - Custom Policy Guardrails
  - custom policy guardrails
  - 自定义策略护栏
definition: "在推理时注入组织自定义安全策略，让模型按该策略解释多模态输入并输出可审计 verdict 的安全控制模式"
created: 2026-06-07
updated: 2026-06-16
evidence_level: medium
claim_type: mixed
tags:
  - ai-safety
  - enterprise-ai
  - guardrails
related_entities:
  - "[[Policy-as-Code-for-Agent-Governance]]"
  - "[[Verifiable-Agent-Engineering]]"
  - "[[Model-Safety-Divergence]]"
  - "[[Agent-Containment]]"
  - "[[Cybersecurity-Openness]]"
source_raw:
  - "[[Nemotron 3.5 Content Safety: Customizable Multimodal Safety for Global Enterprise AI]]"
---

# Custom-Policy-Guardrails（自定义策略护栏）

> [!definition] 定义
> **Custom Policy Guardrails** 是一种安全控制模式：在模型推理时直接注入组织、行业或产品自定义政策，让模型按该政策解释文本、图像和回复上下文，并输出带理由的安全 verdict。

## 它解决什么问题

通用 safety taxonomy 适合做基线，但生产部署很少只有一套普适规则。医疗、金融、儿童教育、开发者工具和企业搜索对风险的容忍度都不同。

Custom policy guardrails 的意义在于，不必为每个产品域都重新训练一整套安全分类器，而是让模型在推理时读入该组织的政策语言，再给出具体判断。

## 关键机制

### 1. 联合判定输入

不是单看 prompt，也不是单看图片或回复，而是把三者放在一起判断：

- user prompt
- optional image
- optional assistant response

这样能覆盖“单独看都不违规，但组合起来违规”的多模态场景。

### 2. 自定义政策注入

模型不只输出“是否安全”，还要根据传入的组织策略解释“为什么不安全、违反哪类规则”。

### 3. 可审计 trace

可选 reasoning mode 会输出简短 reasoning trace，再给出 `safe` / `unsafe` 结论与 category。它不等于法律证明，但足以让人工复核、策略迭代和抽样审计更具体。

## 与治理策略即代码的边界

| 维度 | [[Custom-Policy-Guardrails|Custom Policy Guardrails]] | [[Policy-as-Code-for-Agent-Governance|治理策略即代码]] |
|------|------------------------------|------------------------------|
| 主要层级 | 模型内语义解释 | 模型外运行时执行 |
| 适合处理 | 语义边界、语境判断、多模态含义 | 权限、升级路径、硬性合规规则 |
| 优点 | 灵活、能处理灰度语义 | 可测试、可拒绝、可审计 |
| 风险 | 仍是概率式解释 | 规则表达成本高、边界不灵活 |

两者不是替代关系，而是互补关系。前者负责解释复杂语义，后者负责执行不可妥协的边界。

## 关键数据点

- Nemotron 3.5 使用 Gemma 3 4B IT + LoRA，支持 128K context。
- 显式训练覆盖 12 种语言，并继承约 140 种语言的零样本泛化能力。
- 支持三种输出模式：binary verdict、verdict + categories、reasoning + verdict。
- 文中报告多模态 benchmark 延迟相对另一模型约 3x 更低，reasoning mode 下输出 token 最多可减少约 50%。

## 为什么对本库重要

这类 guardrail 说明企业 AI 的安全边界不再只是“加一个审核 API”，而是开始形成独立的、可部署的策略解释层。它让“组织的风险语言”进入模型调用本身，成为工作系统的一部分。

## 前提与局限性

- 自定义 policy 仍以自然语言输入，不能替代外部可执行策略。
- reasoning trace 有助于审计，但可能是压缩后的解释，而非真实决策因果链。
- benchmark 结果不自动代表企业场景中的误杀率、漏报率或合规责任充足性。
- 如果组织自身没有稳定、清楚的政策语言，模型也无法稳定解释这些规则。

## 关联概念

- [[Policy-as-Code-for-Agent-Governance]] — 把不可妥协的边界移到模型外执行
- [[Verifiable-Agent-Engineering]] — 让安全 verdict 成为可抽查证据
- [[Model-Safety-Divergence]] — 同一策略在不同模型上的行为差异值得独立评测
- [[Agent-Containment]] — policy verdict 仍需与环境权限边界配合
