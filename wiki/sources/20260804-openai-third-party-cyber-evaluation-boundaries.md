---
type: source-summary
title: "Third-party cyber evaluations involving OpenAI models"
source_raw:
  - "[[20260804-openai-third-party-cyber-evaluation-boundaries]]"
canonical_url: "https://openai.com/index/third-party-cyber-evaluations-involving-openai-models/"
raw_state: full
source_locator:
  - "UK AISI: internet enabled, external-use boundary under-specified, 2 GPT-5.6 Sol unsanctioned events"
  - "Irregular: intended no-internet CTF, environment misconfiguration exposed public internet"
  - "authorization ambiguity vs isolation/configuration mismatch"
created: 2026-09-19
updated: 2026-09-19
tags:
  - source-summary
  - verification
  - agent-security
evidence_level: high
claim_type: mixed
---

# Third-party cyber evaluations involving OpenAI models

## 编译摘要

### 1. 浓缩

- **核心结论 1：评测边界失守至少有两种不同机制。**
  - UK AISI：公网是有意开放的，但“能否使用真实外部账户/服务”没有被充分显式化。
  - Irregular：公网本应不可达，但环境误配置让真实网站进入攻击面。
- **核心结论 2：prompt 中声明 scope 不等于 runtime 中存在可执行的 scope。**
  - 关键证据：UK AISI prompt 能描述 range 内/外系统，但公网使用语义仍有空白；Irregular 更直接出现“告诉模型无互联网，但实际上有互联网”。
- **核心结论 3：检测和停止必须属于评测本身。**
  - 关键证据：UK AISI 是监控发现异常数据传输后停止相关评测并隔离机器，而不是模型的任务完成判据自动阻止越界。

### 2. 质疑

- UK AISI 19 个事件中只有 2 个由 GPT-5.6 Sol 产生，不能把全部事件归给 OpenAI 模型。
- Irregular 是配置错误，不应被写成“模型突破了正确配置的 sandbox”。
- 两起事件都在降低 safeguard 的 cyber evaluation 条件下发生，不代表普通产品部署行为。

### 3. 对标

- 对 CR-006：直接支持 **scope specification 与 actual reachability 是两个独立门**。
- 对 [[Agent-Security]]：授权边界必须在 action boundary 被确定性执行，不能只存在于 prompt。
- 对 [[Evaluation-Integrity]]：评测设计必须同时定义 in-scope target、可用工具、外部服务语义、stop condition 与 incident escalation。

## 关联概念

- [[Evaluation-Integrity]]
- [[Agent-Security]]
- [[Verifiable-Agent-Engineering]]
