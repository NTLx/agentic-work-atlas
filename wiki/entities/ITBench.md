---
type: entity
title: "ITBench"
aliases:
  - ITBench-AA
  - ITBench-AA SRE
definition: "IBM ITBench 是企业IT自动化评测框架（ICML 2025），覆盖SRE、CISO、FinOps；ITBench-AA是Artificial Analysis基于IBM数据合作推出的独立评测实现，首发为Kubernetes离线事故快照根因识别。任务、运行环境和评分口径不可混用。"
created: 2026-05-28
updated: 2026-11-28
evidence_level: medium
claim_type: mixed
tags:
  - agent-evaluation
  - agentic-engineering
  - benchmark
related_entities:
  - "[[Agentic-Engineering]]"
  - "[[Agent-Harness]]"
  - "[[Verifiability]]"
  - "[[Agentic-Workflow-Token-Efficiency]]"
source_raw:
  - "[[ITBench-AA Frontier Models Score Below 50% on the First Benchmark for Agentic Enterprise IT Tasks — by Artificial Analysis and IBM]]"
---

# ITBench

> [!definition] 定义
> IBM ITBench 原始框架发表于[ICML 2025](https://proceedings.mlr.press/v267/jha25a.html)，初始覆盖SRE、CISO、FinOps。Artificial Analysis与IBM于2026-05-27发布[ITBench-AA](https://artificialanalysis.ai/articles/itbench-aa-launch)，基于IBM任务的独立实现，先覆盖SRE。AA在离线Kubernetes事故快照中要求最小独立根因实体集；评分为满召回条件下的precision均值，并非整体修复成功率。

## 关键数据点

- ITBench-AA首发59个SRE任务（40公开+19私有held-out），Stirrup参考Harness，100轮上限，每任务3次，共177次试验/配置。
- 2026-05 排行榜：Claude Opus 4.7（Adaptive Reasoning, Max Effort）47% 领先，GPT-5.5（xhigh）46%，Qwen3.7 Max 42%
- 2026-05-27发布时所评模型均低于50%，属于AA当时较不饱和的Agent基准之一；这是历史快照而非当前榜单。
- 轮次差异近 3×：GPT-5.5 平均 31 轮得 46%，Gemini 3.1 Pro Preview 83 轮得 30%
- 开源权重成本前沿：Gemma 4 31B（37%, `$0.14`/task）同时击败 Gemini 3.1 Pro（30%, `$2.23`）的分数和成本
- GLM-5.1（Reasoning）40% 为开源最高，追平 Gemini 3.5 Flash（high）40% 但成本更低（`$1.23` vs `$1.70`）

## 前提与局限性

- **范围**：ITBench-AA首发仅SRE且截至本轮[AA方法文档](https://artificialanalysis.ai/methodology/intelligence-benchmarking)仍描述59离线根因任务；原始IBM ITBench已涵盖三个领域。不得把诊断分数外推到真实修复、FinOps或CISO。
- **评分非对称**：缺任何真实根因组为0，否则TP/(TP+FP)；漏报与额外候选不同惩罚。2026-11-28核对AA方法：GPT-5.5 medium answer matcher先将预测归一化到canonical/alias group；等价实体去重，再确定性计分。因此并非全确定性oracle。人类筛查候选与最小独立根因识别属于不同任务目标。
- **Effort level 不可比**: 不同模型的推理模式（Adaptive Reasoning / xhigh / Reasoning）设置不同，跨模型 effort level 比较存在公平性问题
- **Harness 依赖**: 固定Stirrup控制部分变量；仍有模型接口、effort、预算、输出归一化等差异，不能宣称完全公平。IBM I3/EoG/Praxis的研究结果不可直接与AA分数相比。

## 关联概念

- [[Agentic-Engineering]] — ITBench 为 agentic engineering 提供企业级能力基线
- [[Agent-Harness]] — 固定参考Harness提高配置间可比性而非消除全部混杂
- [[Verifiability]] — 满召回条件precision是一种任务特定评分，包含语义匹配步骤
- [[Agentic-Workflow-Token-Efficiency]] — 历史配置间轮次与分数无简单正相关；不证明对同一模型强行减少轮次必然改善
