---
type: source-summary
title: "I remain a skeptic"
source_raw:
  - "[[20260814-i-remain-a-skeptic]]"
created: "2026-08-19"
updated: "2026-08-19"
tags:
  - source-summary
  - ai-skepticism
  - labor-politics
  - software-philosophy
  - evidence-gap
evidence_level: medium
claim_type: mixed
---

# I remain a skeptic — Joshua Barretto (2026-08-14)

## 编译摘要

### 1. 浓缩

- **核心结论 1**：**4 年的 LLM "革命"在顶级生产力层面无显著证据支撑**——`$1.5T` 投资后，独立研究要么聚焦细枝末节（代码行、PR 数、feature 数），要么样本过小；支持 AI 的研究也只显示边际甚至负面生产力收益。
  - 关键证据：作者作为开源项目维护者，4 年来没看到行业在质量/速度/成本/安全性上显著改善。
  - 关键证据："we still have almost no independent studies that can attest to top-level productivity improvements associated with AI"。
  - 关键证据："Even then, those studies that do exist and suggest some amount of academic rigour point to only marginal or even negative productivity gains"。

- **核心结论 2**：**代码不是软件开发的输出，而是输入**——Peter Naur 1985 年的论断被 LLM 时代再次证实；行业仍把代码行作为生产力指标，无论代码来自机器还是被激励扭曲的人类，都通向 unmaintainable slop。
  - 关键证据：作者明确引用 Peter Naur 1985 论文（"code is an input to the software development process and not an output"）。
  - 关键证据："even the most forward-looking organisations still tacitly treat lines of code as a productivity metric"。

- **核心结论 3**：**LLM 革命的隐藏目标是劳动力同质化（fungible）**——当智力劳动可互换，工人议价能力被削弱；软件开发曾是最后的"行会领域"，现在正被工业化。
  - 关键证据："The not-so-quiet goal of the LLM push by big tech was to homogenise intellectual labour such that it can be made fungible"。
  - 关键证据：作者选择不依赖 LLM 来专注更窄的技能集，工作保障反而增强——"By not leaning into LLMs I've given myself the room to specialise in a smaller set of skills"。

### 2. 质疑

- **关于"无显著证据"的质疑**：
  - **selection bias**：作者从开源维护者角度观测，主动用 LLM 给他提 PR 的人可能本身就更糟——这不是 LLM 平均水平的样本。
  - **顶级生产力度量本身困难**："top-level productivity" 没有公认的客观度量；作者批评"代码行/PR 数/feature 数"是细枝末节，但他也没给替代度量。
  - **反例**：库中已存的 [[20260626-anthropic-economic-index-june-2026-report]] 显示 OpenAI 内部使用量 27-56 倍增长；存在企业内部真实采用证据。
  - **反例**：Ian Silber 在 [[20260816-openai-head-of-design-best-time]] 中观察工程师"10x–100x 产出"——这与作者观测矛盾，需并列。

- **关于"代码不是输出"的质疑**：
  - 这是 50 年前的真理，但 LLM 时代有质变：code review 和 design review 的成本急剧下降，使得"先写代码看输出"成为可行工作流——"输入迭代"成本结构改变。
  - 作者引用 Naur 是对的，但 Naur 时代没有"快速生成多个候选输入"的可能性——AI 把"尝试多个输入"成本降到接近零，可能改变了整体生产函数。

- **关于"劳动力 fungible"的质疑**：
  - **证据薄弱**：作者没提供明确证据，主要是推测。
  - **反例**：与 Ian Silber 论述一致——AI 反而让"judgment-heavy"工作更稀缺（设计/工程师剪刀差，judgment 是不可 fungible 的）。
  - **反例**：AI 也创造了新 specialty（prompt engineering、AI safety、AI red teaming）。
  - **边界**：fungible labor 论断可能在某些层级（初级编码、客服）成立，但在 specialty 层级反向。

- **关于"个人未落后"的质疑**：
  - **selection bias 严重**：作者是顶级开源维护者，技能资本本来就是稀缺的——这不是 LLM 不影响普通人的证据。
  - **反例**：Lenny workforce survey（被 [[20260816-openai-head-of-design-best-time]] 引用）显示 Junior 工程师被 AI 替代或难以进入。

### 3. 对标与旁逸

#### 3a. 跨域类比

- **"代码是输入不是输出" ↔ Naur 1985**：作者引用同源——[[Peter-Naur]]（若库中无 entity，需考虑新建）。
- **"`$1.5T` 投资无独立证据" ↔ [[Generation-Verification-Asymmetry]]**：与库中已存的生成-验证不对称定理同构——投资产生的是 generation 能力，verification 滞后。但 jsbarretto 暗示 verification 完全失败，与 GVA 的"剪刀存在但可管理"判断存在张力。
- **"劳动力 fungible" ↔ [[Jevons-Paradox-for-Knowledge-Work]] 反向**：Jevons 说 AI 加速产出导致更多知识工作消费；jsbarretto 说 AI 加速产出但没解决 top-level 生产力问题——两者矛盾，需并列。
- **"个人 specialty 反脆弱" ↔ [[Taste]] / [[Specificity]]**：与库中 Taste 的 "ability-taste flip" 同构——AI 让 ability 普遍化，taste/specificity 反而稀缺。
- **"Industry 表演性叙事" ↔ AI-Confidence-Theater（forward reference，Elena Verna 概念，无独立 raw）**。

#### 3b. 旁逸

- **"Peter Naur remains undefeated"**——作者隐含的论断是"AI 时代的所有权-专利-Naur 模型"：当 AI 让代码生成自动化，Naur 模型更凸显——代码本身不重要，理解和判断才重要。这与 Ian Silber 的"设计师护城河是 judgment"同构。

#### 3c. 约束分析

- **结论 1 成立的硬约束**：
  - 顶级生产力度量的困难（"top-level productivity" 无公认度量）。
  - 软约束：行业研究的 selection bias（多数是 vendor 资助）。
  - 自设约束：作者从"自己不在意 LLM"的立场出发，可能更倾向看到负面证据。

- **结论 2 成立的硬约束**：
  - 软件工程 50 年来的实证支持（Naur 1985）。
  - 软约束：AI 改变"输入迭代"成本结构，但没改变"代码≠输出"的本质。

- **结论 3 成立的软约束**：
  - 大科技确实在 push LLM，但"隐藏目标"是 speculation，需观察 AI 时代工人议价能力的实际数据。
  - 自设约束：作者是开源维护者（高 specialty），论断对其个人验证 ≠ 对行业普适。

### 关联概念

- [[Joshua-Barretto]]
- [[Peter-Naur]]（forward reference，跨源被多次引用）
- [[Generation-Verification-Asymmetry]]
- [[Jevons-Paradox-for-Knowledge-Work]]
- [[Taste]]
- [[Specificity]]
- AI-Confidence-Theater（forward reference，Elena Verna 概念）
- [[20260816-openai-head-of-design-best-time]]（OpenAI 视角对照）
- [[20260815-engineers-history-reinvention]]（同向反方对照）

### 待解问题

1. 顶级生产力（top-level productivity）的客观度量是否存在？
2. "代码是输入不是输出"在 LLM 时代是否仍是真理，还是已成为部分过时？
3. AI 时代工人议价能力的实际数据是什么？（与"fungible labor" 论断对照）
4. Junior 工程师的真实处境——被 AI 替代还是被 AI 增强？
5. Peter Naur 模型与 AI 时代 judgment 价值的精确关系？