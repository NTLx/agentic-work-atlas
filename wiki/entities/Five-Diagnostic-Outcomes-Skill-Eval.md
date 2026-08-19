---
type: entity
title: Five Diagnostic Outcomes for Skill Eval
aliases:
  - Five Diagnostic Outcomes for Skill Eval
  - Skill vs Baseline Mental Models
  - 5 Skill Eval Outcomes
  - High-Efficiency Capability Lift
definition: "Skill vs baseline agent eval 的 5 种诊断结果分类——按 (accuracy 改善/打平/退化) × (cost 改善/持平/退化) 区分，从 High-Efficiency Capability Lift（最好）到 Context Overload & Skill Regression（最差），每种对应不同 audit 行动"
created: 2026-08-19
updated: 2026-08-19
tags:
  - evals
  - skill-evaluation
  - agent-skills
  - mental-models
evidence_level: medium
claim_type: mixed
related_entities:
  - "[[Skills-as-Products]]"
  - "[[LLM-as-a-Judge]]"
  - "[[Rubric-Based-Evaluation]]"
  - "[[Evaluator-Miscalibration]]"
  - "[[Agent-Skill]]"
source_raw:
  - "[[20260819-google-ai-evals-inspect-skill]]"
---

# Five Diagnostic Outcomes for Skill Eval

> [!definition] 定义
> **Five Diagnostic Outcomes for Skill Eval** 是 Google DevRel 提出的 skill vs baseline agent eval 诊断框架：当评估"加入 skill 后 agent 表现是否改善"时，结果不能只看总分，应按 (accuracy 方向) × (cost 方向) 分类为 5 种结果，从 **High-Efficiency Capability Lift**（skill 同时改善 accuracy 和 cost，最理想）到 **Context Overload & Skill Regression**（skill 拖慢且表现错，最失败），每种对应不同的下一步 audit 行动。

## 5 种结果（按 outcomes 优劣排序）

| # | 结果 | accuracy | cost | 含义 | 下一步 |
|---|------|----------|------|------|--------|
| 1 | **High-Efficiency Capability Lift** | ↑ | ↓ | skill 同时提升 accuracy 和降低 cost | promote skill 进入 product skill set |
| 2 | **Capability Lift（cost-neutral）** | ↑ | → | skill 提升 accuracy 但成本不变 | audit skill 内容是否真生效 |
| 3 | **Cost-Only Lift** | → | ↓ | skill 不改善 accuracy 但显著降成本 | 视场景决定——若业务关键 accuracy 则无价值 |
| 4 | **Cost Bloat** | → | ↑ | skill 不改善 accuracy 但显著增成本 | 删除或重写 skill 描述 |
| 5 | **Context Overload & Skill Regression** | ↓ | ↑ | skill 退化 accuracy 且增加 cost | 删除并调查 skill 描述是否误导 agent |

## 评估者使用流程

```
跑 skill vs baseline eval
    ↓
获得 (accuracy_delta, cost_delta) 二元组
    ↓
映射到 5 种结果之一
    ↓
按结果执行对应 audit / promote / delete 行动
```

## 与 Inspect AI 的具体映射

| 评估层 | 数据源 | 决策项 |
|--------|--------|--------|
| Macro view | `inspect view` GUI | 按 model 分组观察 accuracy 与 token/duration |
| Sample-level | Transcript tab | skill 是否被 activate；reasoning loops vs 环境噪声 |
| Scoring tab | multi_scorer 输出 | 哪些 fact 错、是否系统错还是边界错 |

## 与 Evaluator Miscalibration 的关系

[[Evaluator-Miscalibration]] 关注**评估器本身**的校准错误（rubric 冲突、锚点 game）；本文关注**评估对象**（skill 表现）的诊断分类。两层互补：先校准评估器（避免看错），再看诊断分类（避免做错决定）。

## 关键数据点

- Google DevRel 在 Gemini 3.5 vs 3.6-flash × skill 4-way sweep 中观察到多种结果
- 所有 case 都改善或打平 accuracy，但**也**全部增加 duration——意味着 skill 的 cost 副作用一致存在，被 score-improving 掩盖
- gcloud skill 在 3.5→3.6-flash 时 accuracy 略降——属于 Context Overload 或 Skill Regression 的轻量版本

## 前提与局限性

- **5 种分类未覆盖完备性**：可能遗漏"skill 改变 skill activation 模式"等元层影响；可能存在"完全无效"（accuracy 与 cost 都无变化）的第 6 种
- **依赖 decoupled grader 准确**：5 种结果的前提是 grader 评分与 ground truth 接近；rubric 不准则分类错
- **样本量与统计 confidence**：单次 sweep 不足以稳健分类；置信区间宽时需重跑扩大样本
- **skill activation 先决条件**：若 skill 未被 agent 激活，eval 实际测的是 baseline——5 种结果应在 activation verified 后才有意义
- **未量化各 case 比例**：5 种结果在大型 skill library 中的分布未公开；无法判断哪种是常见情况

## 配套机制

- **Skill Ingestion Check**：transcript tab 验证 agent 是否真的激活了 skill（否则 eval 测的是 baseline 知识）
- **Sample-level diagnostics**：从 high-level 总分下钻到单 sample 看 transcript + scoring
- **Sandbox noise vs model reasoning**：区分推理 loop（agent 责任）和环境噪声（沙箱责任）

## 关联概念

- [[Skills-as-Products]] — 5 种结果是 skill product 治理的 decision matrix
- [[LLM-as-a-Judge]] — 评分机制；5 种结果依赖 robust judge
- [[Rubric-Based-Evaluation]] — rubric 设计影响分类的稳定性
- [[Evaluator-Miscalibration]] — 先校准评估器再看结果分类
- Agent Skill — skill 是被评估对象；其设计与 5 种结果直接相关
- [[Evals-as-PRD]] — eval 驱动改进的具体决策模型