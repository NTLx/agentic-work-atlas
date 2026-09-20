---
type: source-summary
title: "Cited but Not Verified: Parsing and Evaluating Source Attribution in LLM Deep Research Agents"
source_raw:
  - "[[20260507-cited-but-not-verified]]"
canonical_url: "https://arxiv.org/abs/2605.06635"
raw_state: full
source_locator:
  - "three citation dimensions: Link Works / Relevant Content / Fact Check"
  - "14-model benchmark with human-calibrated rubric evaluators"
  - "2→150 tool-call depth ablation and approximately 42% average Fact Check decline"
created: 2026-09-19
updated: 2026-09-19
tags:
  - source-summary
  - verification
  - agent-evaluation
evidence_level: high
claim_type: mixed
---

# Cited but Not Verified: Parsing and Evaluating Source Attribution in LLM Deep Research Agents

## 编译摘要

### 1. 浓缩

- **核心结论 1：引用存在、引用相关、引用真的支持该事实，是三个不同验证对象。**
  - 关键证据：框架分别评分 Link Works、Relevant Content 与 Fact Check；强模型可以同时拥有很高的链接有效性/相关性，却只有明显更低的事实支持率。
- **核心结论 2：更多检索深度不自动转化为更高事实可靠性。**
  - 关键证据：在两种 frontier model 的 2→150 tool-call ablation 中，Fact Check accuracy 平均下降约 42%，而 link/relevance 指标保持较强。
- **核心结论 3：验证 evidence coverage 时还必须考虑 synthesis capacity。**
  - 关键证据：系统可以“找到更多且相关的来源”，但最终 claim-to-source 对齐反而恶化，说明 coverage 与 interpretation/synthesis 不是同一个门。

### 2. 质疑

- tool calls 增加同时改变信息量、轨迹长度、任务时间和潜在上下文压力，不能把下降唯一归因于“attention dilution”。
- Fact Check 使用经人工校准的 LLM judge，而不是完全独立的事实 oracle；judge calibration 本身仍属于测量链的一部分。
- 深度研究报告与 tool-using environment agent 的状态验证不同，不能直接把 42% 变化外推到所有 Agent。

### 3. 对标

- 对 EX-002：补出 **evidence-synthesis interference**——coverage 增加后，interpretation/synthesis 可能恶化。
- 对 EX-004：citation link/relevance 是 provenance 的表面条件，真正的 reference integrity 还要求 claim 与 source content 对齐。
- 对 [[Sufficient-Context]]：充分上下文不是“越多越好”；超过模型可稳定整合的范围后，额外 evidence 可能降低事实忠实度。

## 关联概念

- [[Verifiable-Agent-Engineering]]
- [[Sufficient-Context]]
- [[Corrective-RAG]]
- [[LLM-as-a-Judge]]
