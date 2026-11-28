---
type: source-summary
title: "AgentJudgeBench: A Multi-Difficulty Benchmark for Evaluating LLM Judges on Agentic Tool-Calling"
source_raw:
  - "[[20260827-agentjudgebench]]"
canonical_url: "https://arxiv.org/abs/2608.26623"
raw_state: full
source_locator:
  - "3,808 instances / six DAG topologies / three difficulty tiers"
  - "paired with-ground-truth vs without-ground-truth conditions across five generators and six judges"
  - "difficulty degradation, hard no-GT 77–82% band, over-anchoring cases and rubric mitigation"
created: 2026-09-19
updated: 2026-11-28
tags:
  - source-summary
  - verification
  - agent-evaluation
evidence_level: high
claim_type: mixed
---

# AgentJudgeBench: A Multi-Difficulty Benchmark for Evaluating LLM Judges on Agentic Tool-Calling

## 编译摘要

### 1. 浓缩

- **核心结论 1：reference availability 本身是 judge 行为变量，而不是天然“越多越好”。**
  - 关键证据：benchmark 对同一类 judge 做 paired with/without-ground-truth 对照；总体上无 ground truth 时随难度退化更快，但部分 frontier judge 暴露 ground truth 后 alignment 反而下降。
- **核心结论 2：特定 hard/no-GT 条件下观察到 judge alignment 窄带，非规模无关上限。**
  - 关键证据：作者在§4.1 Finding 1报告四个generator的hard/no-GT约77–82%窄带；回读v1 Table 2发现第五个SmolLM3-3B的hard/no-GT为69.0–73.3%，Llama-3.3-70B为83.3–84.6%，作者概括亦有口径差；表内数值优先，不视为规模上限或规模因果效应。
- **核心结论 3：judge quality 依赖“拿什么当 reference”。**
  - 关键证据：有 ground truth 时某模型最匹配 programmatic reference，而 human validation 又由另一 judge 最贴近人工判断，说明“最佳 judge”依赖评测锚点。

### 2. 质疑

- 历史原文与代码核查见 [[20260906--reference-integrity-success-provenance--research]]：C3 操纵 judge 所见 Rj，程序评分 Rs 不变；同一 PDF 表1/2 的同名 GT 分数未对齐，需作者 run manifest；120条人审为单标注且可见程序评分，非盲多标注共识。第三十五轮未重开PDF；第三十六轮回核 [arXiv v1 HTML](https://arxiv.org/html/2608.26623v1) §4.2/Table 1–2/Appendix G/J，确认3,808基础记录、C3和120条人审同版存在，hard/GT行Gemini 78.9 vs 82.2、QwQ 84.6 vs 87.5的差异仍在；120条×4指标=480裁决，445/480一致，单标注且有意过采非满分案例，非总体无偏或盲多标注。未取得作者运行清单，不猜测两表差异原因，不拼表；未重跑代码或论文全量数据。

- programmatic reference 本身不是不可错的绝对真值；这正是 EX-004 要继续区分 reference truth 与 judge alignment 的原因。
- 77–82% band 是特定 DAG/tool-calling 构造中的结果，不应外推为所有 Agent judge 的普遍上限。
- ground-truth exposure 同时改变可用信息与 anchoring 行为，不能仅凭总 alignment 判断哪一种条件更“真实”。

### 3. 对标

- 对 EX-004：首次在当前证据簇中提供明确的 **reference condition paired intervention**，证明 reference availability 会直接改变 judge 行为。
- 对 EX-001：即使使用多个不同规模 judge，也可能在困难条件下收敛到相近误差区间；但这不等价于独立性因果检验。
- 对 [[Evaluator-Miscalibration]]：judge 对 programmatic reference 与 human judgment 的最佳匹配者不同，说明 evaluator calibration 必须绑定目标定义。

## 关联概念

- [[Verifiable-Agent-Engineering]]
- [[LLM-as-a-Judge]]
- [[Evaluator-Miscalibration]]
- [[Agent-Verification]]
