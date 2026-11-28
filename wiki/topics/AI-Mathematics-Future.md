---
type: topic
title: AI Mathematics Future
aliases:
  - AI数学未来
  - 数学AI进展
definition: "数学AI的竞赛求解、开放研究、证明与独立验证，以及搜索成本、概念形成和研究贡献的评价边界"
created: 2026-07-01
updated: 2026-11-28
evidence_level: medium
claim_type: mixed
tags:
  - AI-capabilities
  - mathematics
related_entities:
  - '[[AI-in-Mathematics]]'
  - '[[Conceptual-Breakthroughs]]'
  - '[[Grindability-vs-Verifiability]]'
  - '[[Autoregressive-Generation]]'
  - '[[Human-Curation]]'
  - '[[Theory-of-Mind]]'
source_raw:
  - '[[20260701-grant-sanderson-ai-math-future]]'
---

# AI Mathematics Future

> [!definition] 定义
> 数学是检验部分推理、搜索和证明能力的重要场景，不是已证明的AGI充分指标或其他职业自动化的预测器。区分竞赛、已知命题重推导、未知真假开放问题、概念形成与共同体理解。

## 证据与能力边界（2026-11-28）

- [AlphaProof 原论文](https://www.nature.com/articles/s41586-025-09833-y) 与 [2024 IMO 官方报告](https://deepmind.google/blog/ai-solves-imo-problems-at-silver-medal-level/)：合计28/42，银牌水平；AlphaGeometry 2在收到形式化P4后19秒求解，非端到端；两道组合题未解是该次实验，不是长期领域能力边界。
- [2025 IMO 官方报告](https://deepmind.google/blog/advanced-version-of-gemini-with-deep-think-officially-achieves-gold-medal-standard-at-the-international-mathematical-olympiad/)：高级Gemini Deep Think自然语言端到端、4.5小时内35/42，五题满分。协议变化，不把分数变化当同测量条件或AGI。
- [OpenAI 2026-05-20](https://openai.com/index/model-disproves-discrete-geometry-conjecture/) 内部模型给出Erdős单位距离猜想 n^(1+o(1)) 上界的反证，借用代数数论，外部数学家检查并写伴随论文；不等于确定u(n)的精确渐近阶。跨领域连接的反例不能忽略，也不证明任意概念突破能力。
- Meta合作论文、KLS人机搜索及O’Neill局部改进的既有证据见 [[AI-in-Mathematics]]；分别记录实际命题、提示、模型/计算资源、人工贡献、prior art、证明与复核。形式检查依赖形式化是否匹配命题及可信计算基。
- 外部候选 [Huang, PNAS 2026](https://pmc.ncbi.nlm.nih.gov/articles/PMC13732072/) Methods/Table1：GPT-5.5 Pro 2026-04-23快照，关闭工具与网页，8次正确或基本正确，平均106.7k reasoning tokens。但system/first prompt明确已知定理被证明并给出反证方向；是已知目标重推导，不是盲态原创或8/8开放问题成功率。未复跑、未独立审八份证明；待正式晋升。

## 科研工作设计

| 维度 | 需要验证 |
|---|---|
| 搜索与可磨性 | 可重置环境、并行成本、分支多样性、路线可达性、预算和停止规则 |
| 正确性 | 明确命题、独立证明/检查器、假设、形式化对应及实现可信性 |
| 原创性 | 研究前可见信息、目标是否已知、prior art、独立/同时发现、人工提示 |
| 科学价值 | 是否增加解释、统一或新预测，是否可理解与复用；不是仅靠证明通过 |
| 自主性 | 谁选择问题、设定目标、指导分支、执行、检查及承担责任 |

[[Grindability-vs-Verifiability]] 两轴互补，不比较普适重要性；并行采样不能保证独立错误或跳出固定路线。[[Conceptual-Breakthroughs]] 区分数学有效性、传播与长期影响；Galois的历史并非统一百年验证期。[[Autoregressive-Generation]] 是生成因子分解，不推出不能跨领域连接；增加探索需与预算、质量及相关性对照。[[Human-Curation]] 与 [[Theory-of-Mind]] 是候选工作维度，不作为永久人类独占能力。历史1–3/3–10/10年以上的预测缺估计或可检验依据，撤回稳定身份。原访谈的未来愿景保留为作者观点。

## 关联概念

- [[AI-in-Mathematics]] — AI在数学中的应用与进展
- [[Conceptual-Breakthroughs]] — 概念突破的本质与验证
- [[Grindability-vs-Verifiability]] — 可磨性与可验证性的区别
- [[Autoregressive-Generation]] — 自回归生成的局限性
- [[Human-Curation]] — 人类策展的核心价值
- [[Theory-of-Mind]] — 心智理论在沟通和教学中的作用

## 来源

- [[20260701-grant-sanderson-ai-math-future]] — Grant Sanderson与Dwarkesh Patel的播客访谈