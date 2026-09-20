---
type: source-summary
title: "Role of Human-AI Interaction in Selective Prediction"
source_raw:
  - "[[20211213-human-ai-interaction-selective-prediction]]"
canonical_url: "https://arxiv.org/abs/2112.06751"
raw_state: full
source_locator:
  - "fixed-receiver human experiment"
  - "factorial manipulation: show deferral status / show AI prediction"
  - "human judgement accuracy changes with handoff message"
created: 2026-09-19
updated: 2026-09-19
tags:
  - source-summary
  - governance
  - verification
evidence_level: high
claim_type: mixed
---

# Role of Human-AI Interaction in Selective Prediction

## 编译摘要

### 1. 浓缩

- **核心结论 1：handoff 不是透明传输；消息本身会改变接收者。**
  - 关键证据：实验直接操纵“告诉人系统选择了 defer”与“展示 AI prediction”两个因素，人类判断准确率随之变化。
- **核心结论 2：更多模型信息不一定更好。**
  - 关键证据：研究中展示错误模型预测会把人带偏；最佳条件是传达 deferral status 而不展示 AI prediction。
- **核心结论 3：不能用离线 human/model accuracy 直接估计 human-AI team accuracy。**
  - 关键证据：人类行为会因为自己处于 AI 协作/deferral 场景而改变。

### 2. 质疑

- 固定 receiver，无法回答“交给谁”。
- 分类消息不是长程 investigation handoff packet。
- 不含 queue、waiting time、tool trace 或 receiver workload。

### 3. 对标

- 对 EX-003：这是当前证据簇中最直接的 **packet/message 因果操纵**。
- 对 [[Escalation-Based-Human-Oversight]]：升级事件至少要记录向人展示了什么；“已升级”不是充分审计字段。
- 对 [[Human-Governor-Agent-Operator]]：Governor 的独立判断可能被 Agent conclusion anchoring 污染，因此 handoff packet 应区分 evidence 与 model recommendation。

## 关联概念

- [[Escalation-Based-Human-Oversight]]
- [[Human-Governor-Agent-Operator]]
- [[Human-Signal]]
