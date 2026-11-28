---
type: entity
title: API Distillation Catch-up
aliases:
  - API Distillation Catch-up
  - API 蒸馏追赶效应
  - API Distillation
  - 蒸馏追赶
definition: "经授权利用教师模型输出训练学生模型，可能帮助特定任务追赶；开放权重与闭源前沿的测得差距不能识别该机制的因果贡献。"
created: 2026-06-20
updated: 2026-11-28
tags:
  - concept
  - AI-scaling
evidence_level: medium
claim_type: mixed
related_entities:
  - "[[Sample-Efficiency]]"
  - "[[Specialized-Small-Models]]"
  - "[[Recursive-Self-Improvement]]"
  - "[[Enterprise-AI-Model-Sourcing]]"
source_raw:
  - "[[20260619-the-data-black-hole-at-the-center-of-ai]]"
---

# API-Distillation-Catch-up（API 蒸馏追赶效应）

> [!definition] 定义
> 教师模型输出可作为学生模型的训练数据，可能降低部分任务的标注或训练成本；公开API可访问不等于有训练许可。Patel 的“蒸馏解释追赶”是因果假设，非实证归因。

## 核心机制与证据

- [Epoch AI 2025-10-30](https://epoch.ai/data-insights/open-weights-vs-closed-weights-models)：历史ECI横向平均3.5个月（90% CI 1.1–5.3）、纵向7分。与[2026-05-29](https://epoch.ai/data-insights/open-closed-eci-gap) 的2026-01-01至05-28逐日估计并非完全同方法。新版平均4个月（bootstrap至少5%样本超过历史SOTA），严格点估计超过则6个月；8 ECI分（90% CI 7–11）。公开基准优化、未公开模型和评测覆盖限制，不能推出11月现况或固定代差。
- [DeepSeek-R1 官方模型卡](https://huggingface.co/deepseek-ai/DeepSeek-R1) 的同项目教师输出蒸馏是可见的任务级证据；不是所有开放模型依靠闭源API追赶的证明。数据、架构、算法、算力、后训练、推理预算和发布节奏可能共同作用。
- 蒸馏学生可在某些任务接近或超过某些基线；是否超过教师取决于任务、额外数据、优化及评测。不存在由蒸馏定义推出的全局性能上界。

## 关键数据点

- 4/6个月是同一历史窗口不同判据，非未来规律。原“蒸馏成本只有从头训练1%甚至更低”没有统一任务、规模及成本口径，撤回稳定数值。
- 开放权重不等同OSI开源AI；见 [[Closed-Frontier-Models-vs-Open-Model-Economy]]。

## 前提与局限性

- [OpenAI Services Agreement](https://openai.com/policies/services-agreement/) 对用输出开发竞争模型有限制及Permitted Exception；具体产品、合同与例外需逐项核验。不能以API可用推定许可，也不从行业传闻认定特定供应商违规。
- 蒸馏效果需要独立评测、数据权利、训练与运行成本验证。开放权重、发布透明性、训练数据可得性及商业许可分别记录。
- 未重算ECI或验证各实验室训练数据，新增资料仅用于纠正既有论断，正式来源晋升仍走Weekly。

## 关联概念

- [[Sample-Efficiency]] — 数据效率、数据质量与教师监督是不同测量对象。
- [[Specialized-Small-Models]] — API 蒸馏通常被用来训练更小、更专注于特定领域的高性价比专业模型。
- [[Recursive-Self-Improvement]] — API 蒸馏主要是一种外部反馈，而自我迭代则指望利用模型自身在私有验证器下的 RL 演化。
- [[Enterprise-AI-Model-Sourcing]] — 用合法许可、任务实测及总成本评价模型，而非推定其追赶方式。
