---
type: source-summary
title: "An Empirical Analysis of Calibration and Selective Prediction in Multimodal Clinical Condition Classification"
source_raw:
  - "[[20260629-selective-prediction-clinical-calibration]]"
canonical_url: "https://proceedings.mlr.press/v333/lopez26a.html"
raw_state: full
source_locator:
  - "PMLR 333 / CHIL 2026 multimodal ICU selective-prediction study"
  - "class-dependent miscalibration and aggregate-metric masking"
  - "uncertainty-based deferral can degrade task performance"
created: 2026-09-19
updated: 2026-09-19
tags:
  - source-summary
  - governance
  - verification
evidence_level: high
claim_type: extracted
---

# An Empirical Analysis of Calibration and Selective Prediction in Multimodal Clinical Condition Classification

## 编译摘要

### 1. 浓缩

- **核心结论 1：整体 calibration 好，不代表每类 case 的升级策略都可靠。**
  - 关键证据：论文发现严重 class-dependent miscalibration，聚合指标会遮蔽局部失败。
- **核心结论 2：uncertainty-based selective prediction 可能把错误 case 留给模型、把正确 case 交给专家。**
  - 关键证据：某些类别中 uncertainty 与 correctness 的对应关系发生反转或明显失真。
- **核心结论 3：升级策略必须同时看 coverage 与被升级 case 的组成。**
  - 关键证据：只看总体 accuracy / calibration 无法判断 deferral 是否把专家容量花在最需要的地方。

### 2. 质疑

- 这是 ICU 多标签分类，不能直接外推到客服、SRE 或开放式 Agent。
- 论文没有真实专家队列和人工接管成本。
- 结果说明 threshold routing 的风险，不证明复杂 facilitator 一定更好。

### 3. 对标

- 对 EX-003：补出 **trigger calibration 不能只用 aggregate confidence**；需要 per-class / risk-stratified routing audit。
- 对 [[Escalation-Based-Human-Oversight]]：例外升级的“例外”必须被按失败类型校准，而不是只设全局阈值。
- 对 [[Human-Governor-Agent-Operator]]：专家容量是稀缺资源，错误 deferral 会把人力浪费在不需要接管的 case 上。

## 关联概念

- [[Escalation-Based-Human-Oversight]]
- [[Human-Governor-Agent-Operator]]
- [[Evaluator-Miscalibration]]
