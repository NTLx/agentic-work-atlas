---
type: source-summary
title: "Human-AI Teaming Through the Lens of Calibration"
source_raw:
  - "[[20260609-human-ai-teaming-calibration]]"
canonical_url: "https://arxiv.org/abs/2606.10906"
raw_state: full
source_locator:
  - "rejector calibration burden under delegation"
  - "human hidden-feature / unobservable-information excess-risk condition"
  - "ImageNet-16H and HAM10000 empirical evaluation"
created: 2026-09-19
updated: 2026-09-19
tags:
  - source-summary
  - governance
  - verification
evidence_level: high
claim_type: mixed
---

# Human-AI Teaming Through the Lens of Calibration

## 编译摘要

### 1. 浓缩

- **核心结论 1：把 case 升级给人不会消除判断问题，而是把问题转移给 rejector。**
  - 关键证据：delegation 框架要求一个 meta-model 判断由人还是模型负责预测。
- **核心结论 2：路由质量取决于 rejector 能否观察决定“谁更擅长”的特征。**
  - 关键证据：当人类使用系统不可见的额外信息时，论文给出不可约 excess-risk 条件。
- **核心结论 3：专家越异质，粗粒度 confidence threshold 越不够。**
  - 关键证据：rejector 必须更细地刻画 feature space 中 human/model relative advantage。

### 2. 质疑

- 研究对象是 prediction delegation，不是长程 Agent handoff；没有 queue、handoff packet、等待和接管工作流。
- “human-only information” 是信息可辨识性边界，不等于所有人类都有隐藏优势。
- 理论限制不能直接给出生产中的最佳升级率。

### 3. 对标

- 对 EX-003：为 **trigger / receiver selection** 提供理论边界——facilitator 不可能仅靠自己看得见的状态完美估计人类隐藏优势。
- 对 [[Escalation-Based-Human-Oversight]]：升级条件不能只写成单一 confidence threshold；还要记录路由器可见信息与专家私有信息。
- 对 [[Human-Governor-Agent-Operator]]：Governor 的价值有一部分来自系统外信息，但这也意味着路由器无法完全自证何时该调用 Governor。

## 关联概念

- [[Escalation-Based-Human-Oversight]]
- [[Human-Governor-Agent-Operator]]
- [[Verifiable-Agent-Engineering]]
