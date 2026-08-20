---
type: entity
title: Decoupled Grader Architecture
aliases:
  - Decoupled Grader Architecture
  - Decoupled Grader
  - Solver-Grader Split
  - Solver-Grader Decoupling
definition: "在 AI eval 系统中把 solver（被测 agent）与 grader（评分模型）拆解为不同模型的架构模式——grader 选用成本/能力匹配的模型，rubric 设计偏向 strict-binary + 程序化 reduction 以最大化评分一致性，并允许 grader 配额与 solver 配额独立管理"
created: 2026-08-19
updated: 2026-08-19
tags:
  - evals
  - verification
  - architecture
  - rubric-design
  - grading
evidence_level: medium
claim_type: mixed
related_entities:
  - "[[LLM-as-a-Judge]]"
  - "[[Rubric-Based-Evaluation]]"
  - "[[Evaluator-Miscalibration]]"
  - "[[Skills-as-Products]]"
source_raw:
  - "[[20260819-google-ai-evals-inspect-skill]]"
---

# Decoupled Grader Architecture

> [!definition] 定义
> **Decoupled Grader Architecture** 是 AI eval 系统中把 solver（被测 agent 与其在 sandbox 中的执行）和 grader（对执行结果评分的模型）拆分为不同模型的架构模式：solver 配额按被测能力选择，grader 配额按评分精度与成本独立选择；grader 的 rubric 设计偏向 strict-binary + 程序化 reduction，以在低成本模型上获得 robust 评分，并允许生产系统替换为更强 grader 收窄置信区间。

## 三条原则

1. **职责拆分**：solver 产生 trace / 答案，grader 只读 + 评分。grader 不参与工具调用，不接触 sandbox 噪声
2. **代差换成本**：demo 阶段用上一代/小模型做 grader（如 Gemini 3.1 flash-lite），生产阶段用同期/更强模型收窄置信区间
3. **rubric 形态适配评分模型能力**：便宜模型偏 strict-binary + 程序化 reduction（确定性），强模型可承担连续分级评分

## strict-binary rubric 的代价

| 维度 | strict-binary | 分级锚点 |
|------|--------------|----------|
| grader 模型要求 | 低（任何 chat 模型） | 高（需准确理解多档描述） |
| 评分一致性 | 高（binary 判断） | 中（受 rubric 措辞影响大） |
| 诊断信息 | 低（只知对错） | 高（看分数梯度） |
| 适用规模 | 大规模粗筛 | 关键样本精评 |
| 防止 game | 中（"几乎对"也算错） | 取决于锚点设计 |

## 关键参数

| 参数 | 选择 | 理由 |
|------|------|------|
| solver 模型 | 3 个 gemini flash 变种 | 测模型 × skill 矩阵 |
| grader 模型 | gemini-3.1-flash-lite | 上一代、低成本 |
| 时间限制 | 300s/task | 防止 reasoning loops 失控 |
| epoch 数 | 2 | 多次采样取统计均值 |
| max-tasks | 4 | 4-way parallel sweep |
| 工具配置 | `web_access=false` | 最小化 token 消耗、控制变量 |
| rubric 形态 | strict-binary per fact | cheap grader 适配 |
| 评分聚合 | mean → mean² 二次方 curving | 让最优答案立即突出 |

## 配套机制

- **外部配置分离**：questions.json 与 thrifty_system_prompt.txt 独立于 eval script 维护；好处是 rubric 变化不需要改 solver
- **rate-limiting 防御**：solver 版本固定（version="0.51.0" pinning）防止上游 SDK 变更导致对照失效
- **grader 配额解耦**：grader 与 solver 配额独立计费——可分别为 grader 增加更贵模型而不影响 solver 设计
- **CLI 参数 reference**：所有 `inspect eval` 参数显式传入，便于跨 run 复现

## 关键数据点

- 4-way parallel sweep across models × skill conditions
- 300s timeout + 2 epochs + max-tasks 4
- grader 用 Gemini 3.1 flash-lite（上一代），生产建议用更新模型
- 5/6 fact 评分 0.8333 → quadratic curving 后 0.65

## 前提与局限性

- **binary rubric 的诊断力有限**——当分数贴近边界（5/6 vs 6/6）时，binary 评分看不出"差在哪一个 fact"
- **cheaper grader 减少 quota 消耗但置信区间更宽**——demo 可接受，生产需换贵 grader 收窄
- **decoupled 假设 solver 与 grader 互不影响**——若 solver 输出含 grader 模型见过的相同训练数据，仍存在同质性监督失效（参见 [[LLM-as-a-Judge]] 的同质性段落）
- **strict-binary 在主观题上失效**——情感质量、推理深度等连续属性 binary 评分会丢失信息
- **依赖外部 sandbox 隔离**——若 solver 的 sandbox 噪声未隔离（timeouts/missing binaries），grader 会把环境问题当答案问题

## 关联概念

- [[LLM-as-a-Judge]] — decoupled grader 是 LLM-as-a-Judge 在多 agent eval 中的具体架构
- [[Rubric-Based-Evaluation]] — strict-binary 是 rubric 形态的一种选择
- Atomic Fact Rubric — fact-by-fact binary rubric 是 multi_scorer + custom_reducer 的实现细节
- [[Evaluator-Miscalibration]] — strict-binary 抗校准错误的 robustness 来自其 binary 形态
- [[Skills-as-Products]] — on-submit eval 可采用 decoupled grader 做初始筛选
- [[Evals-as-PRD]] — eval 作为需求文档的循环起点