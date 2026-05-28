---
type: source-summary
title: "ITBench-AA: Frontier Models Score Below 50% on Agentic Enterprise IT Tasks"
source_raw:
  - "[[ITBench-AA Frontier Models Score Below 50% on the First Benchmark for Agentic Enterprise IT Tasks — by Artificial Analysis and IBM]]"
created: 2026-05-28
updated: 2026-05-28
tags:
  - source-summary
  - agent-evaluation
  - agentic-engineering
---

# ITBench-AA: Frontier Models Score Below 50% on Agentic Enterprise IT Tasks

## 编译摘要

### 1. 浓缩
- **核心结论1**: 前沿模型在企业 IT Agent 任务上表现远低于预期——最佳模型 Claude Opus 4.7 在 SRE（站点可靠性工程）任务上仅达 47%，所有模型均低于 50%。
  - 关键证据: 59 个 SRE 任务（40 个公开 + 19 个新增 held-out），覆盖 Kubernetes 事件响应（alerts、events、traces、metrics、logs、topology），模型需识别最小根因 Kubernetes 实体集。
- **核心结论2**: 更多调查轮次不等于更高准确率——过度调查的模型倾向于把上游故障注入机制或共现症状误报为根因，产生 false positive。
  - 关键证据: GPT-5.5（xhigh）平均 31 轮得 46%；Gemini 3.1 Pro Preview 平均 83 轮仅得 30%。评分使用 recall-gated precision：漏掉任何真实根因得 0 分，多报则降低 precision。
- **核心结论3**: 开源权重模型处于成本前沿——Gemma 4 31B（Reasoning）以 `$0.14`/task 获得 37%，同时击败更昂贵的闭源模型。
  - 关键证据: Gemma 4 31B（37%, `$0.14`）> Gemini 3.1 Pro（30%, `$2.23`），分数和成本双胜；GLM-5.1（40%, `$1.23`）追平 Gemini 3.5 Flash（40%, `$1.70`）但成本更低。

### 2. 质疑
- **关于"59 个任务通用性"的质疑**: SRE 只是企业 IT 的一个子领域，59 个任务的多样性和覆盖度有限。模型在其他 IT 任务（FinOps、CISO）上的表现可能完全不同。
- **关于"recall-gated precision"的质疑**: 这种评分方式对 false positive 极度惩罚（漏一个根因 = 0 分），可能高估了模型在真实生产环境中的实际效用——在真实 SRE 中，给出 3 个候选根因让人类筛选，好过只给 1 个但遗漏。
- **关于"成本数据可比性"的质疑**: 各模型的推理模式不同（Adaptive Reasoning vs xhigh vs Reasoning）， effort level 的设置直接影响轮次和成本，不同 effort level 下的比较可能不公平。

### 3. 对标
- **跨域关联1**: 类似 [[Verifiable-Agent-Engineering|可验证 Agent 工程]] 中的非确定性验证问题——ITBench 的 recall-gated precision 是一种"结果可验证性"的极端形式，验证维度从"输出格式"上移到"领域知识正确性"。
- **跨域关联2**: 与 [[Agent-Harness|Agent Harness]] 中的 Stirrup 参考 harness 直接关联——harness 固定才能做 apples-to-apples 的模型对比，证明了 harness 标准化对 Agent 评测的决定性作用。
- **跨域关联3**: "更多轮次 ≠ 更好结果"的发现，类似 [[Agentic-Workflow-Token-Efficiency|Agentic Workflow Token Efficiency]] 中 token 效率问题——Agent 的"调查深度"需要工程约束，否则会无限制膨胀。

### 关联概念
- [[ITBench]]
- [[Agentic-Engineering]]
- [[Agent-Harness]]
- [[Verifiability]]
- [[Agentic-Workflow-Token-Efficiency]]
