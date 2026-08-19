---
type: source-summary
title: "Designing AI Evals: Clarity Now and Visualization Next"
source_raw:
  - "[[20260819-google-ai-evals-inspect-skill]]"
created: 2026-08-19
updated: 2026-08-19
tags:
  - source-summary
  - evals
  - verification
  - inspect-ai
  - agent-skills
evidence_level: medium
claim_type: mixed
---

# Designing AI Evals: Clarity Now and Visualization Next

## 编译摘要

### 1. 浓缩

- **核心结论1**: Decoupled grader 架构是 agent skill eval 的关键成本控制——把 solver（被测 agent，用 Gemini 3.5/3.6 flash）和 grader（评分模型，用更便宜的 Gemini 3.1 flash-lite）拆开，grader 用 strict-binary rubric + 程序化 reduction 在不消耗 solver quota 的前提下做 robust 评分；生产系统应换成更贵的 grader 收窄置信区间
  - 关键证据: "intentionally offloaded grading for this demo to a previous-generation model... by changing rubric criteria to strict binary decisions and applying a reduction programmatically, it delivers sufficiently robust evaluations without burning through solver quota"; "For a *production* evaluation system, consider investigating using newer and more capable models as graders"
- **核心结论2**: 多事实 rubric + 二次方 curving 让"接近正确"与"几乎正确"可区分——`multi_scorer` 对每个 fact 做 binary model_graded_qa，custom_reducer 取算术平均，再应用 mean² curving；5/6 fact ≈ 0.8333 被压到 0.65，让最优答案立即突出
  - 关键证据: "applies quadratic score curving (mean²) to ensure that the further from correct the mean of the supplied answers are, the lower the score is pulled"; 0.8333 → 0.65 实测映射
- **核心结论3**: Skill vs baseline 评估有 5 种诊断结果（high-efficiency capability lift 等），按 "skill 是否带来 accuracy/cost 双改善"区分——评估者用这套 mental models 决定下一步追查方向，避免仅看总分掩盖真相
  - 关键证据: "five distinct diagnostic outcomes—ranging from High-Efficiency Capability Lift (best) to Context Overload & Skill Regression (worst)"; 5 种 outcomes 分别对应不同 audit 行动

### 2. 质疑

- **关于 "decoupled cheap grader" 的鲁棒性**: 严格 binary rubric 减少了 grader 偏误，但代价是丢失连续分数的诊断信息。当一个 answer 多数 fact 对、少数 fact 错时，binary 评分看不出"哪里接近对了"——这是 [[Rubric-Based-Evaluation]] 中分级锚点存在的理由
- **关于 quadratic curving 的数学假设**: mean² curving 假设评分分布对称，但实际 multi-fact 评分可能在 (0.0, 0.5) 或 (0.9, 1.0) 附近聚集——curving 在两端区分度不足；作者也承认公式需按数据调
- **关于 5 种 mental models 的完备性**: 这是 Google DevRel 的内部经验分类，未公开 5 种模型各自的样本比例和典型 case。可能存在第 6 种"skill 既无 lift 也无 cost 增加"的无效模式，或遗漏"skill 改变 skill 激活模式"这种元层影响
- **关于"在所有 case skill 提升或打平 accuracy"**: 但所有 case **都**增加了 duration——这意味着 skill 的 cost 副作用一致存在，但被 score-improving 掩盖；按 5 种 mental models 维度评估时，这是"efficiency regression"信号需要单独计分
- **关于 gcloud skill 在 3.5→3.6 时 accuracy 略降**: 文中未给原因——可能是 skill description 在 3.6 上不被 activate，可能是 skill 内容过时，可能是更复杂的交互。这种"模型升级反而 skill 倒退"是 [[Skills-as-Products]] 的腐烂风险实证

### 3. 对标与旁逸

- **跨域关联1**: *strict-binary grader + 程序化 reduction* 与 [[LLM-as-a-Judge]] 的同质性监督失效同向，但解法不同。LLM-as-a-Judge 强调 rubric 设计解决同质监督问题，本文强调 rubric 形态（binary vs continuous）+ 评分模型代差——互补而非替代
- **跨域关联2**: *quadratic curving* 在传统机器学习中有先例（如 focal loss 的 γ 参数、Huber loss 在 L2/L1 之间的过渡），但用在 multi-fact 聚合上是新方法——更接近"评分函数作为评估设计的一部分"，可视为 evaluation-as-design-pattern
- **跨域关联3**: *5 种 mental models* 与 [[Evaluator-Miscalibration]] 的诊断模式同源——都是"总分掩盖真相，必须看逐维诊断"。差异：Evaluator-Miscalibration 讲 rubric 标准冲突，本文讲 skill 与 baseline 的相对结果；两层叠加构成完整 eval 诊断矩阵
- **跨域关联4**: *skill activation check*（transcript tab 确认 skill 是否真的被 agent 激活）是 eval 设计的 hidden layer——很多"skill eval"实际测的是 baseline model 知识，不是 skill 效用。这个洞察对 [[Skills-as-Products]] 的"on-submit eval"环节有直接含义：rubric 必须先验证 skill 激活，否则评的是 baseline

## 关联概念

- [[Decoupled-Grader-Architecture]]（新建）— solver/grader 拆分 + strict-binary rubric + cheap grader 节省 quota 的架构模式
- [[Five-Diagnostic-Outcomes-Skill-Eval]]（新建）— skill vs baseline 5 种诊断结果分类
- [[LLM-as-a-Judge]] — grader 是 LLM-as-a-Judge 的工程实例
- [[Rubric-Based-Evaluation]] — strict-binary 是 rubric 设计的一个具体形态
- [[Evaluator-Miscalibration]] — 5 种 mental models 应对的是校准错误的不同子形态
- [[Skills-as-Products]] — skill activation check 是 product-level eval 的前置条件
- [[Goodharts-Law]] — quadratic curving 是抗 game 的反向激励设计
- [[Evals-as-PRD]] — 评测驱动改进的循环
- [[Agent-Verification]] — eval 与 verification 在 agent 工程域的重叠