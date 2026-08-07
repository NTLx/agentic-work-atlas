---
type: entity
title: Evaluator Miscalibration
aliases:
  - Evaluator Miscalibration
  - 评估器校准错误
  - 校准陷阱
  - Calibration Trap
definition: "评估器测量的不是你真正关心的行为：rubric 标准互相冲突或锚点奖励了错误的东西，使聚合分数与真实质量背离——校准错误的评估比没有评估更糟，因为它递给你虚假的信心"
created: 2026-07-30
updated: 2026-08-07
tags:
  - evaluation
  - agentic-engineering
related_entities:
  - "[[LLM-as-a-Judge]]"
  - "[[Rubric-Based-Evaluation]]"
  - "[[Goodharts-Law]]"
  - "[[Over-Inference]]"
source_raw:
  - "[[20260729-similarweb-langsmith-agent-report-evaluation]]"
  - "[[20260805-personalization-mirage-llm-over-inference]]"
evidence_level: medium
claim_type: mixed
---

# Evaluator Miscalibration（评估器校准错误）

> [!definition] 定义
> **Evaluator Miscalibration（评估器校准错误）** 是评估器与真实质量脱节的状态：rubric 标准之间互相冲突，或锚点设计奖励了错误的东西，使聚合分数背离团队实际关心的行为。其危险性不在于"分数不准"，而在于**虚假信心**——团队会信任数字、压倒自己的阅读，于是校准错误的评估比没有评估更糟。

## 机制

1. **标准冲突**：两个标准奖励相反的方向（如"来源广度"奖励数量、"归因质量"惩罚模糊来源），聚合分数把冲突平均掉，任何单维度改善都可能表现为总分回归。
2. **激励错位**：锚点措辞即激励结构。奖励" reaching outside the platform"（伸出平台外）的锚点，立即被"九个模糊引用"游戏化——这是 [[Goodharts-Law]] 在评估层的直接形态：度量一旦成为目标就不再是好度量。
3. **聚合掩盖**：总分是唯一被看的量时，逐标准评语里的诊断信息（"广度不错，但归因薄弱"）被丢弃——评语早就知道答案，分数假装不知道。

## 关键数据点

- SimilarWeb Data Studio（LangChain Blog, 2026-07-29）：一次完全没问题的 prompt 更新被误判为回归，反复回滚浪费近一周；根因是 source breadth 与 attribution 两个标准拉扯，聚合分数掩盖冲突。
- 修复方式：把 `source_integration` 锚点从奖励数量改为奖励"命名、可验证、 tied to 具体论断的来源"；同一份"九个模糊引用"的报告分数从 0.7 落到 0.3——数字终于与评语一致。
- 诊断信号结构：每个标准返回 score + gap + detail 三件套；低分永远附带可检查的理由，使"哪个标准被校准错了"可定位。

## 诊断与修复

- 怀疑校准时，**打开逐标准评语**而不是盯总分——冲突通常写在评语里。
- 检查锚点的激励方向：这个锚点被游戏化时，最省力的刷分行为是什么？那个行为是否是你真正想要的？
- 对标准做正交性审查：一版输出能否在 A 标准上升的同时在 B 标准下降？若能且两者都重要，聚合分数不可单独决策。
- 评估器本身进入验证循环：rubric 改动也要用小规模评估 + trace 检查验证，而不是只凭直觉重写。

## 自评反转：校准错误的极端形态（08-07 补充）

当**模型自身充当评估器**（self-audit）时，校准错误达到系统性反转程度。MirageBench（arXiv 2608.04570, 2026-08，来源 [[20260805-personalization-mirage-llm-over-inference]]）给出最极端的实证：

- **跨模型自评与实测负相关**：12 模型自评 OI 与独立 judge 实测 OI 的 Spearman ρ = −0.60（p=0.044，**exploratory**，CI [−0.90,+0.06]）。自报 OI 最低的 Qwen3-8B（13.0%）实测最高（48.7%）——**自评最安全的模型实测最危险**。
- **机制 = differential self-labeling strictness（差分自标严格度）**：宽松自标者（GPT-4o-mini/Qwen3-8B）把几乎所有自己的推断标为"reasonable"，不产生校准信号；严格自标者（Claude/GLM/Kimi）愿把推断标为有问题。自评分数反映的是"标注严格度"而非"实际行为"——这正是本 Entity 讲的锚点激励错位在自评层的形态：**自评的"锚点"由模型自身的自我标签倾向决定，跨模型不可比**。
- **与 Goodharts-Law 同构**：自报 OI 一旦成为选型指标就失效——选"自评最安全"的模型恰恰选中最危险的。
- **作用域分裂**：自评绝对水平不可作跨模型安全比较器；模型内相对排序仍可用（AUROC 0.58–0.83）。诊断时应问：这是跨模型比较（→ 必须外部 judge）还是模型内排序（→ 自评可用）？

与本 Entity 前文的差异：前文讲**外部评估器**标准设计错误（SimilarWeb 案例）；本条讲**模型自评**作为评估器时，其"校准锚点"（自我标签倾向）本身是模型属性，无法标准化。两层叠加意味着"让模型评估自己"比"让评估器评估模型"更不可靠。

## 前提与局限性

- **证据层级**：主要来自单一团队自述（SimilarWeb），机制一般但量化细节是自报；跨团队系统性研究缺乏。
- **不意味着分数无用**：命题是"聚合分数不可单独决策"，不是"不要分数"；分数 + 评语 + trace 三位一体时，评估仍是人类判断的放大器。
- **与裁判偏差是两层问题**：本条处理标准层失效（锚点/冲突设计错误）；[[LLM-as-a-Judge]] 的同质性监督失效处理价值观层——两层叠加时（标准错 + 裁判偏），可检查性也只能部分补救。
- **基线陷阱未覆盖**：A/B 基线是"已接受的历史版本"，校准修复若只校准新输出而从不重校基线，偏差会以基线形式固化。

## 关联概念

- [[Goodharts-Law]] — 校准错误是古德哈特定律在评估器设计层的直接形态。
- [[Rubric-Based-Evaluation]] — 锚点设计是校准的主战场；分级锚点（score + gap + detail）是诊断基础设施。
- [[LLM-as-a-Judge]] — 裁判方法论；可检查的评语 + trace 是校准错误的探测手段。
