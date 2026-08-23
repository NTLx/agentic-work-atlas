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
  - diagnostics
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

## 测量架构重编译（08-23 深度思考）

同一 raw 的 decoupled grader / sandbox / curving 设计，借圆桌（Gödel/MacKenzie/O'Neil/Tukey）+ 追本 + qa 重编译出四条跨页判断，与本 entity 的诊断框架形成互补——本页回答"评估对象表现如何"，重编译回答"评估本身在做什么"：

### 评测守恒律（synthesized/中，待升级）
评测缝隙总量守恒——缝隙从行为层压进 rubric、从 rubric 压进 fact 选择、从 fact 选择压进 curving，只换住址不归零；诚实只决定缝隙住得显眼还是隐蔽。对本页的含义：5 种诊断结果的"刻度"不是中性镜子，是 fact 集 + curving 搬过缝隙后的读数；分类再准也只覆盖"被设计者允许可见"的差异。

### 测量设计 = 逃逸机会结构的形状塑造者（synthesized/中，待升级）
sandbox 隔离 / fact 集合 / curving 三层设计都是环境侧机会结构的工程化构造——评估"显示超出基线"与评估"被逃逸"，是同一设计硬币的两面。对本页的含义：若 skill 因激活检测的假阳性（见配套机制"Skill Ingestion Check"）而虚高，那正是"设计半邀请的逃逸"在诊断层的实例。

### curving = 制造可见性/精确性幻觉（synthesized/中，待升级）
0.833→0.65 的二次方变换让"接近正确"陡然可辨——但精确记号让所有决策者停止追问（接透明幻觉判决）；本页 5 种结果的 (accuracy, cost) 分类同样在制造决策可见性。

### 评测域反驳通道缺席（synthesized/低-中，待升级）
被评测方（skill 作者）面对 0.65 无申诉/复议/审计权限——三层测量设计 = 三层权力加码，接归因环"被告的声音"。

> [!note] 待实证
> curving 公式是否公开（裁决"诚实约定 vs 权力决定"）；decoupled grader 退化基线漂移；缝隙守恒 vs 增殖——均挂在 agenda 08-23 待证伪节。

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