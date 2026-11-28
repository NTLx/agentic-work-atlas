---
type: source-summary
title: "ITBench-AA: Frontier Models Score Below 50% on Agentic Enterprise IT Tasks"
source_raw:
  - "[[ITBench-AA Frontier Models Score Below 50% on the First Benchmark for Agentic Enterprise IT Tasks — by Artificial Analysis and IBM]]"
created: 2026-05-28
updated: 2026-11-28
tags:
  - source-summary
  - agent-evaluation
  - agentic-engineering
---

# ITBench-AA: Frontier Models Score Below 50% on Agentic Enterprise IT Tasks

## 编译摘要

### 1. 浓缩
- **核心结论1**: 2026-05-27 AA发布时，所测配置在ITBench-AA SRE的满召回条件precision均值最高47%（Claude Opus 4.7），均低于50%；不是所有企业IT任务成功率，也不是当前排名。
  - 关键证据: 59个离线Kubernetes事故快照根因诊断任务（40公开+19私有held-out），覆盖事故观测（alerts、events、traces、metrics、logs、topology），模型需识别最小根因 Kubernetes 实体集。
- **核心结论2**: 在当时的不同配置间，更多轮次未必对应更高分；作者观察额外上游/共现实体误报，但不证明同一模型缩短调查一定有益。
  - 关键证据: GPT-5.5（xhigh）平均 31 轮得 46%；Gemini 3.1 Pro Preview 平均 83 轮仅得 30%。评分使用 recall-gated precision：漏掉任何真实根因得 0 分，多报则降低 precision。
- **核心结论3**: 开源权重模型处于成本前沿——Gemma 4 31B（Reasoning）以 `$0.14`/task 获得 37%，同时击败更昂贵的闭源模型。
  - 关键证据: Gemma 4 31B（37%, `$0.14`）> Gemini 3.1 Pro（30%, `$2.23`），分数和成本双胜；GLM-5.1（40%, `$1.23`）追平 Gemini 3.5 Flash（40%, `$1.70`）但成本更低。

### 2. 质疑
- **关于"59 个任务通用性"的质疑**: SRE 只是企业 IT 的一个子领域，59 个任务的多样性和覆盖度有限。模型在其他 IT 任务（FinOps、CISO）上的表现可能完全不同。
- **关于"recall-gated precision"的质疑**: 漏任一真实根因组为零；全召回后按precision扣额外预测。漏报和误报惩罚非对称，可能低估可供人类筛选的不完整诊断效用，也可能高估真实恢复能力；两种目标需分别评估。
- **关于"成本数据可比性"的质疑**: 各模型的推理模式不同（Adaptive Reasoning vs xhigh vs Reasoning）， effort level 的设置直接影响轮次和成本，不同 effort level 下的比较可能不公平。

### 3. 对标
- **跨域关联1**: 类似 [[Verifiable-Agent-Engineering|可验证 Agent 工程]] 中的非确定性验证问题——ITBench 的 recall-gated precision 是一种"结果可验证性"的极端形式，验证维度从"输出格式"上移到"领域知识正确性"。
- **跨域关联2**: 与 [[Agent-Harness|Agent Harness]] 中的 Stirrup 参考 harness 直接关联——固定Stirrup控制部分变量，仍须记录effort、模型调用接口、资源预算及评估器；不能保证完全公平或因果分离。
- **跨域关联3**: "更多轮次 ≠ 更好结果"的发现，类似 [[Agentic-Workflow-Token-Efficiency|Agentic Workflow Token Efficiency]] 中 token 效率问题——Agent 的"调查深度"需要工程约束，否则会无限制膨胀。

### 证据边界

2026-11-28回读本地Raw全文（42行），并核对[AA发布文章](https://artificialanalysis.ai/articles/itbench-aa-launch)、[AA方法文档](https://artificialanalysis.ai/methodology/intelligence-benchmarking)的ITBench-AA节。IBM原始[ITBench（ICML 2025）](https://proceedings.mlr.press/v267/jha25a.html)覆盖SRE、CISO及FinOps，与2026年的AA离线实现非同一评分实验。AA方法在当前版本用GPT-5.5 medium answer matcher映射canonical entities/alias groups并去重，再以满召回precision计分；并非纯确定性oracle。当前[AA榜单](https://artificialanalysis.ai/evaluations/itbench-aa)已出现高于50%的配置，因此标题保留历史发布语境，不用作当前判断。原文成本为历史评测每任务估计，非生产任务成本。未重跑评测或检查私有数据。

## 关联概念
- [[ITBench]]
- [[Agentic-Engineering]]
- [[Agent-Harness]]
- [[Verifiability]]
- [[Agentic-Workflow-Token-Efficiency]]
