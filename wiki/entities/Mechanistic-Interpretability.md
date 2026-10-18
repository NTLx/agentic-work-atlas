---
type: entity
title: Mechanistic Interpretability
aliases:
  - 机制可解释性
  - Mechanistic Interpretability
  - Mech Interp
definition: "通过测量、解码并因果干预模型内部激活与计算结构，解释模型为何产生某类行为的研究方法"
created: 2026-10-18
updated: 2026-10-18
evidence_level: high
claim_type: mixed
tags:
  - interpretability
  - ai-safety
  - llm
related_entities:
  - "[[Model-Introspection]]"
  - "[[Agent-Verification]]"
  - "[[World-Model]]"
source_raw:
  - "[[20261018-lenny-emmanuel-ameisen-interpretability]]"
  - "[[20260923-latentspace-eric-biosecurity]]"
  - "[[20261010-latentspace-biohub-deepmind-protein-folding]]"
---

# Mechanistic Interpretability（机制可解释性）

> [!definition] 定义
> **Mechanistic Interpretability** 不是让模型“解释自己”，而是直接研究模型内部计算：记录中间激活、寻找稳定表征或 circuit 候选，再通过干预内部状态观察行为是否按预测改变，从而逐步建立可检验的机制解释。

## 关键数据点

- Ameisen 描述的标准路径是：在大量输入上记录 intermediate activations → 找稳定 representation / circuit 候选 → 直接修改内部状态 → 检查行为是否按预测变化。
- Claude 的内部表征可以跨文本、图像、语言或不同上下文复用同一概念方向；访谈以地理概念和“eye”概念为例。
- 模型可以在未显式输出的中间状态中提前编码后续目标；诗歌押韵实验显示后续 token 会反复利用这一内部计划。
- Golden Gate Claude 是可解释性因果干预的直观案例：持续增强特定概念特征后，模型行为系统性偏向该概念。
- “36”异常案例显示，内部测量可以定位一个在实际计算前就已出现的强偏置，并帮助追溯到错误奖励数据。

## 核心方法

最小实验闭环可以概括为：

~~~text
controlled inputs
      ↓
record activations / intermediate states
      ↓
identify representation or circuit candidates
      ↓
intervene on the internal state
      ↓
measure behavioral consequence
      ↓
refine the mechanism hypothesis
~~~

Ameisen 在 2026-10 的访谈中给出两个关键层次：首先在大量文本上记录中间数值，寻找只在特定语言、对象或语义概念出现时稳定激活的模式；随后直接修改这些激活，检查模型行为是否发生预期变化。Golden Gate Claude 是这种因果干预思路的直观案例：研究者找到与 Golden Gate Bridge 相关的内部特征后持续增强它，模型行为随之系统性偏向该概念。

**判断**：机制可解释性的证据强度来自“相关表征 + 因果干预”的组合，而不是给某组 activation 起了一个容易理解的名字。

- **证据**：[[20261018-lenny-emmanuel-ameisen-interpretability]]。
- **边界**：当前方法只能覆盖部分内部机制；被成功解码的 feature 不等于模型的完整内部算法，也不能把“未检测到异常”当成安全证明。

## 与 Model Introspection 的区别

[[Model-Introspection|Model Introspection]] 是产品与 debugging 层的方法：让模型生成“为什么刚才会这样做”的自我解释。它成本低、可快速暴露 harness、prompt 或行为模式问题，但输出可能是 post-hoc rationalization。

Mechanistic Interpretability 则绕过模型生成的自我叙述，直接观察和干预内部计算状态：

| 维度 | Model Introspection | Mechanistic Interpretability |
|------|---------------------|-----------------------------|
| 观察对象 | 模型生成的自我解释 | 内部 activation / representation / circuit |
| 主要证据 | 语言自述与行为模式 | 内部测量 + 因果干预 |
| 成本 | 低，可产品化 | 高，通常需要研究级工具 |
| 主要风险 | 后验合理化、幻觉 | 解码不完整、feature 误标、覆盖不足 |
| 最适合 | debugging / failure triage | 机制研究 / alignment investigation |

**判断**：两者可以串联，而不应混用。Model Introspection 适合提出“可能哪里不对”的假设；Mechanistic Interpretability 可以在部分场景进一步检验内部机制是否真的支持该假设。

## 与 Agent Verification 的关系

[[Agent-Verification|Agent Verification]] 主要回答“系统做出来的结果是否满足 contract、oracle 或 policy”；Mechanistic Interpretability 试图回答“模型内部哪些机制或表征导致了这种行为”。

Ameisen 对 alignment 的描述给出一个很清楚的 defense-in-depth 结构：

~~~text
behavior / transcript monitoring
        ↓
what did the model do?

mechanistic interpretability
        ↓
what internal state may have driven it?
~~~

在“36”训练污染案例中，模型能算出正确答案 12，却被训练压力反复拉向 36；内部激活显示它在真正开始计算之前就异常强烈地表征了 36。这个案例说明：仅看最终推理文本可以看到异常行为，但内部测量能进一步定位异常偏置出现的时间和可能来源。

**判断**：对高自主 Agent，external verification 与 internal interpretability 是互补证据层。前者仍是生产正确性的主要门禁；后者更适合解释稳定失败模式、异常倾向和 alignment 风险，而不是替代可执行 oracle。

- **边界**：现实部署中，大多数 Agent 任务仍缺少足够成熟的 mechanistic monitoring；因此不能把它假设为当前通用 production control。

## 跨领域使用边界

本库已有两类相邻证据：

- [[20260923-latentspace-eric-biosecurity]] 讨论 biological mechanistic interpretability，即从 embeddings / activations 中寻找 biological structure；这说明“解释内部 representation”可以跨到科学模型，但当时仍处早期阶段。
- [[20261010-latentspace-biohub-deepmind-protein-folding]] 强调对 scientific AI 来说，mechanistic interpretability 不能替代 capability boundary、calibrated uncertainty、known failure modes 和 external validation。

因此本实体的使用边界是：**mechanistic understanding 是可信系统的一层证据，不是可信系统的全部合同。** 在科学、软件 Agent 或高风险决策中，最终仍要回到外部可验证结果、已知失效模式和真实环境验证。

## 前提与局限性

- **可解码不等于完全可解释**：某个稳定方向与概念相关，不意味着整个模型以离散、人类可读概念运行。
- **干预可能有副作用**：内部 feature 往往不是完全局部模块；改变一个方向可能同时影响多个行为。
- **覆盖问题仍然存在**：只能研究被工具发现和测量的机制；未知 circuit 不会因为没被看到就不存在。
- **术语需要功能化理解**：研究者说模型“有概念”“会规划”时，应理解为内部表征与行为功能，而不是自动推导出人类式主观体验。

## 关联概念

- [[Model-Introspection|Model Introspection]]
- [[Agent-Verification|Agent Verification]]
- [[World-Model|World Model]]
