---
type: entity
title: Sample Efficiency
aliases:
  - Sample Efficiency
  - 样本效率
  - Training Sample Efficiency
definition: "智能体为达到特定业务流利度和胜任力所需要接触/训练的数据量。样本效率高意味着使用更少的数据就能学会新知识或新技能。"
created: 2026-06-20
updated: 2026-11-28
tags:
  - concept
  - AI-scaling
  - cognitive-science
evidence_level: medium
claim_type: mixed
related_entities:
  - "[[Amortized-Intelligence]]"
  - "[[API-Distillation-Catch-Up]]"
  - "[[World-Model]]"
  - "[[AI-Labor-Bottleneck-Shift]]"
source_raw:
  - "[[20260619-the-data-black-hole-at-the-center-of-ai]]"
  - "[[20260908-dwarkesh-pretraining-progress-data]]"
---

# Sample-Efficiency（样本效率）

> [!definition] 定义
> **Sample-Efficiency（样本效率）** 是衡量一个智能体（人类或 AI）学习效率的核心指标。它定义为在给定领域中，为了达到特定的流利度、胜任力和操作水平，所需要接触或训练的数据总量。样本效率越高，学习新技能所需的数据量就越小。

## 人类与 AI 的可比性

Patel 原文的语言接触量、20小时驾驶和机器人示范是量级类比，并非同一能力阈值下的人机对照。即便照其假设以2亿token对10万亿至100万亿token，算术比为5万至50万倍；不同训练目标、先验、多模态、数据重复和部署可靠性使比值不能解释成样本效率。驾驶小时与车队里程更不能直接比较。撤回3–6数量级通用差距。

## 缩放拟合的边界

[Hoffmann et al. 2022](https://arxiv.org/html/2203.15556) §3.3 Eq.(2) 拟合 L(N,D)=E+A/N^α+B/D^β。设目标L*>E，且L*−E−A/N^α>0，代数上 D(N)=[B/(L*−E−A/N^α)]^(1/β)，当N趋向无穷时 D∞=[B/(L*−E)]^(1/β)。两者比例取决于起始N、目标loss与拟合参数；并非普适10倍极限。无限参数是数学外推，不是实测、也不是人类认知定律。训练loss与下游任务胜任度分别测量。

## 新证据：数据改进与模型改进的预训练分解

[[20260908-dwarkesh-pretraining-progress-data]] 的小规模实验给“数据工程能提高有效学习效率”提供了新的量化线索。

**判断**：在该实验的尺度和 OLMES 评测下，数据 corpus 的改进比模型 recipe 的改进带来了更大的 compute-efficiency multiplier；这支持“数据质量/整理是有效训练效率的重要杠杆”，但不等于模型的狭义 sample efficiency 已经发生算法级跃迁。

- **证据**：2019–2025 年代表性 recipe 与 corpus 的组合实验，在 1e19 FLOPs 预算下得到数据侧 12.0x、模型侧 3.7x 的 compute multiplier，前者约为后者的 3.24 倍。
- **边界**：实验最高只有 1e19 FLOPs，模型相对较小，评测主要是 OLMES 的选择题任务；数据侧主要是 Common Crawl 的筛选和整理，未覆盖更大尺度、合成数据、专家数据、RL 或 post-training。

## 关键数据点

- 原作者语言接触量与训练token是量级假设，非共同测量；撤回百万倍稳定身份。
- 给定拟合式及目标loss可求条件性数据需求极限；不存在任务无关的10倍上限。
- 基因组与模型参数文件不是同一表示；发育、环境、结构及先验不能由文件字节数排除。作者类比不识别遗传与个体学习贡献。
- **预训练分解实验**：在小规模 1e19 FLOPs 预算下，2019–2025 数据侧 compute multiplier 为 12.0x，模型侧为 3.7x；这是条件性实验结果，不是整体 AI 进步份额。

## 前提与局限性

- **多模态对齐**：人类感知、示范、文本token、环境步数和模拟里程不直接可比；需明确相同任务、先验、质量阈值、数据单位及重复次数。
- **任务局限性**：高样本效率学习主要体现在通用常识、物理世界交互（如驾驶、操纵）以及人类已有先验知识中。围棋和蛋白质折叠的训练机制不同；不能将蛋白质折叠泛化为RL自我博弈，亦不能由运行速度推样本效率。
- **概念边界**：数据整理提高给定预算下的 compute efficiency，不等于模型用更少样本学会新技能；二者必须分开测量。
- **尺度边界**：数据侧优势可能随模型规模、训练 token 数、上下文长度和任务类型变化，不能从该实验直接外推到 frontier training。

## 关联概念

- [[Amortized-Intelligence]] — 摊销智能是抵消低样本效率高昂代价的经济手段。
- [[API-Distillation-Catch-Up]] — 教师输出训练是可能的效率杠杆；追赶的因果贡献需另行识别。
- [[World-Model]] — 物理世界的“世界模型”是人类拥有极高样本效率的先验基础。
- [[AI-Labor-Bottleneck-Shift]] — 样本效率的缺失导致 AI 在面对全新的、OOD 的长尾任务时依然极其依赖人类专家数据。
