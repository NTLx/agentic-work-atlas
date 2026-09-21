---
type: source-summary
title: "Hidden in Memory: Sleeper Memory Poisoning in LLM Agents"
source_raw:
  - "[[20260514-sleeper-memory-poisoning]]"
canonical_url: "https://arxiv.org/abs/2605.15338"
raw_state: full
source_locator:
  - "persistent-memory attack pipeline: write → retrieve → use"
  - "poisoned memory added up to 99.8% on GPT-5.5 / 95% on Kimi-K2.6"
  - "among successful retrievals, attacker-intended agentic actions in 60–89% of evaluations"
created: 2026-09-20
updated: 2026-09-20
tags:
  - source-summary
  - agent-security
  - verification
evidence_level: medium
claim_type: mixed
---

# Hidden in Memory: Sleeper Memory Poisoning in LLM Agents

## 编译摘要

### 1. 浓缩

- **核心结论 1：持久记忆是一条跨会话控制状态通道。**
  - 恶意 document / webpage / repository 可以诱导 Agent 写入伪造 memory；原始恶意内容离场后，后续独立 session 仍可能检索并使用该状态。
- **核心结论 2：必须把 write、retrieve、use 分开观测。**
  - 论文直接按三阶段评测；memory 被成功写入不代表未来一定检索，检索成功也不代表一定执行攻击者意图。
- **核心结论 3：污染可以抵达 agentic action。**
  - 论文报告 poisoned-memory 写入最高 99.8%（GPT-5.5）和 95%（Kimi-K2.6）；在成功 retrieval 的条件下，攻击者意图的 agentic action 在不同模型/设置中为 60–89%。

### 2. 质疑

- provider-specific memory pipeline 部分不可见，不能把实验中的 write/retrieve/use 概率直接外推到所有产品。
- 论文证明了持久污染链，但没有闭合 provenance-aware write、correction、revocation/deletion、user review 到未来 action 的完整防御生命周期。
- 60–89% 是 successful retrieval 条件下的 action 结果，不是对所有注入尝试的无条件攻击成功率。

### 3. 对标

- 对 EX-006：补上 **carrier contamination across sessions**；问题不只是 policy 是否被压缩丢失，也包括不可信内容是否被持久化成未来决策状态。
- 对 CR-002：这里的核心对象是“什么状态被写入并跨会话影响动作”，不是单纯的数据保留时长或最小化。
- 对 [[Agent-Security]]：memory security 至少需要 write provenance、retrieval visibility、use/action receipt 与 correction/revocation semantics，不能只检查最终文本。

## 关联概念

- [[Agent-Security]]
- [[Context-Rot]]
- [[Long-Lived-Credential-Risk]]
- [[Verifiable-Agent-Engineering]]
