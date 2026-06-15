---
type: entity
title: Distributional Alignment
aliases:
  - Distributional Alignment
  - 分布对齐
  - 任务分布对齐
  - 训练历史对齐
definition: "模型训练历史与部署任务分布之间的贴近程度；在特定企业任务中，它可能比参数规模更能解释模型质量、成本和稳定性"
created: 2026-05-24
updated: 2026-05-29
evidence_level: medium
claim_type: mixed
tags:
  - AI-evaluation
  - enterprise-AI
  - model-selection
related_entities:
  - "[[Specialized-Small-Models]]"
  - "[[Specialization-Compounds]]"
  - "[[Layered-AI-Sourcing]]"
  - "[[Evaluation-Set]]"
  - "[[Verifiability]]"
  - "[[Model-Safety-Divergence]]"
source_raw:
  - "[[Specialization Beats Scale A Strategic Variable Most AI Procurement Decisions Overlook]]"
  - "[[20260528-ai-model-simulation]]"
---

# Distributional Alignment（分布对齐）

> [!definition] 定义
> **Distributional Alignment（分布对齐）** 指模型训练历史与真实部署任务分布之间的贴近程度。它不是抽象的“模型更懂业务”，而是模型在预训练、领域预训练、监督微调和偏好优化中已经接触并适配了多少相近任务、语言、文档类型和失败模式。

## 关键数据点

- DharmaOCR 文章的核心主张是：在巴西葡萄牙语 OCR 这个企业域里，一个 3B 专门化模型在质量、成本和稳定性上同时领先被比较的商业 API。
- 文章报告，专门化 3B 模型 composite score 为 0.911，最近的 frontier 替代 Claude Opus 4.6 为 0.833；同一比较中，该模型每百万页推理成本约低 52 倍。
- 文章把胜负变量解释为训练历史与部署任务的距离：Nanonets-OCR2-3B 已经是通用 OCR 专家，再经过目标域 SFT 与 DPO 后，明显优于从通用 Qwen2.5-VL-3B 起步的同架构模型。
- 在 3B 比较里，Qwen2.5-VL-3B 经相同流程达到 0.793 与 1.41% degeneration；Nanonets-OCR2-3B 达到 0.921 与 0.20% degeneration。

## 前提与局限性

- 该证据来自 OCR 这个可度量、可验证、文档分布相对清楚的任务，不应直接外推到开放式推理、战略判断或创意写作。
- 分布对齐不是取代参数规模，而是把参数规模从唯一默认变量降级为多个变量之一。
- 企业要使用这个概念，必须拥有代表真实工作流的 [[Evaluation-Set|评测集]]；没有任务级评测，所谓“对齐”容易退化成供应商叙事。
- 文章由模型发布方 Dharma-AI 撰写，虽然包含论文和 benchmark，但采购判断仍应复现实验或在本企业数据上重测。

## 关联概念

- [[Specialized-Small-Models]] — 分布对齐让小模型在窄任务中可能超过更大的通用模型。
- [[Specialization-Compounds]] — 对齐不是一次性状态，而是可沿层级累积的训练历史。
- [[Layered-AI-Sourcing]] — 企业采购应把分布对齐纳入模型选择，而不是只按 frontier API 默认采购。
- [[Evaluation-Set]] — 分布对齐必须通过真实任务评测显性化。
- [[Verifiability]] — 越可验证的任务，越容易衡量分布对齐带来的收益。
- [[Model-Safety-Divergence]] — Emergence World 模拟实验证明：分布对齐不仅影响任务质量，还直接影响自治环境下的安全行为（从零犯罪到灭绝）
