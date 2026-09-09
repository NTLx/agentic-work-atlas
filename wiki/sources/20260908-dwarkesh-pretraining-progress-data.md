---
type: source-summary
title: "Pretraining progress is mostly coming from data"
canonical_url: "https://www.dwarkesh.com/p/pretraining-progress-is-mostly-data"
raw_state: index
original_raw_file: "20260908-dwarkesh-pretraining-progress-data.md"
original_body_sha256: "fa27a1ac0db6c5ac3f466ac1ee23cf3b425907bdfc89751732f8285628df20ef"
indexed_at: "2026-09-09T18:28:43+08:00"
created: "2026-09-09"
updated: "2026-09-09"
tags:
  - source-summary
  - ai-scaling
  - pretraining
  - data-engineering
evidence_level: medium
claim_type: mixed
---

# Pretraining progress is mostly coming from data

> Dwarkesh Patel（2026-09-08）发布的一项小规模预训练分解实验。文章的实证价值在于把 2019–2025 年代表性模型 recipe 与数据 corpus 交叉组合并测量 compute multiplier；结论只覆盖预训练、有限算力和 OLMES 这类下游评测，不能直接代表前沿模型或全部 AI 进步。

## 编译摘要

### 1. 浓缩

- **核心结论 1：在这项小规模实验里，数据侧改进带来的预训练计算效率增益大于模型侧改进**
  - 关键证据：在 1e19 FLOPs 预算下，从 2019 到 2025，数据改进的 compute multiplier 为 12.0x，模型改进为 3.7x；两者相除约为 3.24x。
  - 关键证据：对比的是 GPT-2 + OpenWebText 基线与 OLMo-2 + UltraFineWeb 端点，并组合测试 2019–2025 年代表性 recipe 和 corpus。

- **核心结论 2：数据和模型改进在该实验中大体可加，复杂交互不是主要解释**
  - 关键证据：在 3.16e18 FLOPs 的组合网格上，OLMES 分数的线性模型中，模型效应与数据效应的加性项解释了约 88% 的方差。
  - 关键证据：作者报告的年同比 compute-efficiency gain 为模型侧 1.24x、数据侧 1.51x、联合 1.57x；这不是更大尺度前沿训练的直接估计。

- **核心结论 3：模型研究的主要价值可能更多在于打开规模上限，数据工程则直接提高有限预算下的有效训练**
  - 关键证据：作者指出 MoE、稀疏注意力、稳定性、内存/带宽和 kernel 优化等模型/系统工作，常常是在移除“训练更大模型会崩溃或不可行”的约束，而非只体现为相同能力所需 FLOPs 下降。
  - 关键证据：作者把数据改进的未来问题归结为数据墙和合成数据：本实验尚未测量合成数据能否在不伤害性能的情况下扩展有效语料。

### 2. 质疑

- **关于尺度外推的质疑**：实验最高只有 1e19 FLOPs，使用的是相对较小的模型；数据质量的收益可能随模型容量和过度训练比例变化，不能直接外推到 frontier scale。
- **关于评测的质疑**：OLMES 汇总 10 个相对容易、以选择题为主的 benchmark。为了跨 corpus 比较，作者测的是下游能力而不是固定数据集上的 cross-entropy loss，这会增加噪声；不同代码、数学或长程推理评测可能得出不同排序。
- **关于实验设计的质疑**：每年只选择一个“代表性”模型 recipe 和 corpus，并非穷尽当年最优方法；3.16e18 FLOPs 的 7×7 组合网格每格只有一个 seed，超参数搜索也有限。
- **关于“数据进步”的口径质疑**：被测数据大多是 Common Crawl 的不同过滤、抽取和整理版本，未覆盖新增高质量来源、专家数据、合成数据或 post-training/RL 数据；12.0x 反映的是该实验定义下的有效 corpus 改进，不等于数据供给已经解决。
- **关于“模型价值”的质疑**：模型改进使更大参数量、更长上下文和更长运行时间变得可行，这是合理机制解释，但本文的 multiplier 实验主要测 compute efficiency，不能单独证明这些 scaling-enabling 贡献的全部价值。
- **关于样本效率的质疑**：数据改进带来的 compute efficiency 不等于模型学会新技能所需样本量发生了算法级下降；它更接近在给定预算下，数据筛选和组织使训练更有效。

### 3. 对标

- **与 [[Sample-Efficiency]] 对标**：本文为“更好的数据工程可能提高有效学习效率”提供了新的量化线索，但应与“算法/架构让模型用更少样本学会技能”区分；前者是 corpus 质量和训练效率，后者才是狭义 sample efficiency。
- **与 [[AI-Era-Economy-Shift]] 对标**：AI 的前置成本不只有算力和模型研究，也包含抽取、过滤、去重和数据质量评估；如果数据侧收益在更大尺度仍成立，数据工程会成为训练经济中的核心生产资料。
- **与 [[Amortized-Intelligence]] 对标**：数据优化发生在高成本训练端，模型权重的低边际复制发生在部署端；两端共同决定智能资产能否被摊销。
- **与 [[Agentic-Engineering]] 对标**：作者提到数据进步中的许多 ablation 可以由自动化研究者反复实测；这暗示 Agent 可能先自动化“数据实验—评测—筛选”闭环，而不是直接替代高层研究判断。
- **跨域联想（综合判断）**：模型改进像把船造得更大、更稳，数据工程像选择和装载货物；前者决定能否承载规模，后者决定有限航程里装载什么。两者不是“谁更重要”的永久二选一，而是受尺度和任务定义约束的两种效率。

## 证据定位

- 结果段：给出 2019–2025 的数据侧 12.0x、模型侧 3.7x 与 3.24x 比值。
- Discussion：解释数据从 OpenWebText 到 UltraFineWeb 的过滤/规模变化，以及模型从 GPT-2 到 OLMo-2 的架构、优化器和稳定性变化。
- Future research：明确提出更大尺度、边际高质量数据、合成数据与实验室数据投入等待研究问题。
- Appendix/Methodology：说明 compute 预算、C = 6ND 记账、compute-optimal 配置、共享 tokenizer/context，以及 seed、超参数和评测噪声限制。

## 前提与局限性

- 这是研究者在公开文章中自述的小规模实验，页面未提供同行评审或独立复现实验作为证据。
- 结果依赖代表性 recipe/corpus 的选择、OLMES 任务构成、超参数调优和 compute multiplier 的外推方式。
- 本文研究的是 pretraining 的计算效率，不是 RL、SFT、推理效率、tokenizer 或整体 AI capability 的完整进步分解。
- 合成数据是否能越过数据墙仍是未决问题；本文只指出其重要性，没有给出效果结论。
- “数据侧更重要”是该尺度和该评测下的条件性结论；在更大的模型、更长上下文、不同任务或包含 post-training 的系统里，结论可能改变。

## 与既有知识的关系

本文与 [[20260619-the-data-black-hole-at-the-center-of-ai]] 的“进步主要来自更大、更好的数据分布”判断方向一致，但新增了一个可检验的分解：在有限尺度的预训练实验中，数据侧 compute multiplier 高于模型侧。它同时收窄了原判断的适用范围：数据收益不等于 sample efficiency 已经改善，也不削弱模型研究对可扩展训练的基础作用。

## 关联概念

- [[Sample-Efficiency]]
- [[Amortized-Intelligence]]
- [[AI-Era-Economy-Shift]]
- [[AI-Labor-Bottleneck-Shift]]
- [[Agentic-Engineering]]
- [[20260619-the-data-black-hole-at-the-center-of-ai]]
