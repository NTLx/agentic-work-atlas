---
type: source-summary
title: "REDAgentBench: Executable Red Teaming and Faithful Measurement of LLM Agent Systems"
source_raw:
  - "[[20260811-redagentbench-executable-red-teaming]]"
canonical_url: "https://arxiv.org/abs/2608.10669"
raw_state: full
source_locator:
  - "1,661 executable cases / five service surfaces / six models / three harnesses"
  - "service receipt and final-state grounded violation measurement"
  - "Recognition–Execution Gap diagnostic cohort and matched policy-reminder replay"
created: 2026-09-19
updated: 2026-09-19
tags:
  - source-summary
  - verification
  - agent-safety
evidence_level: medium
claim_type: mixed
---

# REDAgentBench: Executable Red Teaming and Faithful Measurement of LLM Agent Systems

## 编译摘要

### 1. 浓缩

- **核心结论 1：安全评测必须区分“发生了什么”与“transcript 看起来发生了什么”。**
  - 关键证据：REDAgentBench 从 service receipt 与 final-state change 验证副作用，避免把 exposure、execution、observation、adjudication 压成一个 ASR。
- **核心结论 2：识别规则不等于执行阶段遵守规则。**
  - 关键证据：在可解析 action anchor 的 state-grounded 子集中，接近五分之一已确认违规发生在 agent 已表达相关约束或风险之后。
- **核心结论 3：同一 rollout 的证据视图会改变“测得的违规率”。**
  - 关键证据：作者报告 ASR 随 harness 和 evidence view 变化，说明 judge 所见证据本身就是测量系统的一部分。

### 2. 质疑

- benchmark 的攻击模板、服务沙箱和 oracle 由同一研究团队设计，外部复现仍重要。
- “policy reminder 降低 70+pp”是 matched replay 中的 benchmark 结果，不等价于生产环境中稳定降低相同比例风险。
- 它证明 state-grounded measurement 更忠实，但没有单独操纵 verifier family independence。

### 3. 对标

- 对 EX-004：直接补上 **execution receipt / final post-state** 这一层 success provenance。
- 对 EX-002：同一执行在不同 evidence view 下可得到不同测量结果，说明 evidence coverage 会污染 judge 结论。
- 对 [[Agent-Attack-Surface]] / [[Agent-Security]]：威胁路径与安全责任链最终必须落到可验证的外部状态，而不是模型自述。

## 关联概念

- [[Verifiable-Agent-Engineering]]
- [[Agent-Attack-Surface]]
- [[Agent-Security]]
- [[Agent-Verification]]
