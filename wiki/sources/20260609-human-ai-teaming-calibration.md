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
updated: 2026-11-28
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
  - 关键证据：当人类使用系统不可见的额外信息、且人机相对优势随隐藏特征跨越最优路由阈值时，在论文的校准假设下可能出现相对可见该信息的 oracle 的不可约 excess risk；隐藏信息本身并不充分。
- **核心结论 3：当异质性改变最优分派区域时，粗粒度 confidence threshold 可能不足。**
  - 关键证据：rejector 必须更细地刻画 feature space 中 human/model relative advantage。

### 2. 质疑

- 研究对象是 prediction delegation，不是长程 Agent handoff；没有 queue、handoff packet、等待和接管工作流。
- “human-only information” 是信息可辨识性边界，不等于所有人类都有隐藏优势。
- 理论限制不能直接给出生产中的最佳升级率。

### 3. 对标

- 对 EX-003：为 **trigger / receiver selection** 提供理论边界——facilitator 仅凭可见信息可能无法识别由隐藏特征改变的最优分派区域。
- 对 [[Escalation-Based-Human-Oversight]]：升级条件不能只写成单一 confidence threshold；还要记录路由器可见信息与专家私有信息。
- 对 [[Human-Governor-Agent-Operator]]：系统外信息可能改变人类与模型的相对优势；是否需要 Governor 仍取决于任务、信息获取成本和授权边界。

## 关联概念

- [[Escalation-Based-Human-Oversight]]
- [[Human-Governor-Agent-Operator]]
- [[Verifiable-Agent-Engineering]]
