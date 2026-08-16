---
type: entity
title: PosterBench
aliases:
  - PosterBench
  - PosterBench-Main-Track
  - PosterBench-mini
definition: "AutoDesign 发布的 paper-to-poster 评估基准——100 篇五学科 Main Track + 10 篇 PosterBench-mini 固定子集，七维评估协议（Faithfulness / Coverage / Density / Visual Evidence / Layout / Readability / Aesthetics），同时包含 933 次人类盲评对（Bradley-Terry 估计）的 ground truth。是当前 paper-to-poster 任务最完整的工业级 benchmark"
created: 2026-08-16
updated: 2026-08-16
tags:
  - benchmark
  - multimodal-evaluation
  - paper-to-poster
  - agent-evaluation
  - rubric-evaluation
evidence_level: medium
claim_type: extracted
related_entities:
  - "[[Meta-Harness-Optimization]]"
  - "[[Rubric-Based-Evaluation]]"
  - "[[LLM-as-a-Judge]]"
  - "[[Evaluator-Miscalibration]]"
source_raw:
  - "[[20260815-autodesign-meta-harness-optimization]]"
---

# PosterBench

> [!definition] 定义
> **PosterBench** 是 AutoDesign (Luo et al., 2026) 发布的 paper-to-poster 评估基准，包含 PosterBench Main Track（100 篇五学科论文）+ PosterBench-mini（10 篇固定子集，受控对照用）+ 933 次人类盲评对（Bradley-Terry 估计）+ 七维评估协议（Faithfulness / Coverage / Density / Visual Evidence / Layout / Readability / Aesthetics）。是当前 paper-to-poster 任务最完整的工业级 benchmark。

## 关键数据点

### 协议结构

| Track | Papers | 用途 | 控制的变量 |
|-------|--------|------|-----------|
| PosterBench Main Track | 100 | 完整系统比较 | Source paper + source assets + output contract + frozen protocol；变 system configuration |
| PosterBench-mini Main Track | 10 | 共享子集 | 共享 10 paper + output contract + frozen protocol；变 system configuration |
| Design Harness Track | 10 | 隔离 design harness 贡献 | Claude Code + Claude 4.8 固定；变 design harness |
| Coding Harness Track | 10 | 隔离 coding harness 贡献 | AutoDesign + GLM 5.2 固定；变 coding harness |
| Model Track | 10 | 隔离模型贡献 | AutoDesign + Claude Code 固定；变 model |
| Harness-Attachment Ablation | 10 | harness 装/卸对照 | 模型 + code agent 固定；变有无 DesignHarness |

### 七维评估协议

| 维度 | 含义 | 典型评分要点 |
|------|------|-------------|
| **Faithfulness** | 内容保真 | 数字、引用、作者、机构、方法名不能幻觉 |
| **Coverage** | 内容覆盖 | 是否覆盖论文关键 section（动机、方法、数据、结果、消融、限制） |
| **Density** | 信息密度 | 单位面积信息含量，避免大数字表 + 空泛填词 |
| **Visual Evidence** | 视觉证据 | 是否引用源 figures / tables（原文 crops），而不是 native 重建 |
| **Layout** | 布局 | 三栏平衡、7-10 sections、header 三行（title/authors/institutions）严格 |
| **Readability** | 可读性 | Times New Roman 类学术衬线字体；body weight 400；inline emphasis 仅用于 lead phrases |
| **Aesthetics** | 美学 | VLM-as-judge 综合视觉品质 |

**评估器 R_meta 实现**：由 coding agent 用人类标注的 reference artifacts 实现，结合**规则检查**（直接可测属性，如 header 三行约束、3-column 布局）+ **VLM 判断**（感知属性，如美学）。

**关键设计**：optimization-time evaluator 与 frozen PosterBench 协议**分离**——前者参与 harness 优化，后者只在最终系统比较时使用，避免"评估器被同向优化"。

### 主要结果

**Main Track 完整系统比较（100 papers, 5 学科）**

| 系统 | PosterBench Score |
|------|------------------|
| **AutoDesign** | **78.32** |
| Claude Design（商业） | 70.87 |
| Claude Code（coding agent） | 70.01 |
| OpenDesign | — |

→ AutoDesign 超 Claude Design **+7.45 分**（商业系统对比）

**人类盲评（n=933 pairwise）**

| 系统 | BT 偏好估计 |
|------|------------|
| AutoDesign | 64.0%（95% CI: 55.2-77.8%）|
| Claude Code | 51.7% |
| OpenDesign | 43.4% |
| Claude Design | — |

- AutoDesign 对 Claude Design 胜率 67.6%
- 评估-人类偏好相关性：Pearson r=0.34（CI [0.22, 0.44]）

### 关键实验发现

**Harness-Attachment Ablation 普遍正增益**

n=7 配置平均 +12.4%；DeepSeek V4 Pro 提升最大 +19.56；GPT-5.5 提升最小 +5.59（上限效应）。详见 [[Meta-Harness-Optimization]] 数据表。

**评估器 vs 人类偏好的一致性**

| 评估分差区间 | 人类一致率 |
|------------|----------|
| 0-3 | 52%（近随机）|
| 3-6 | 57% |
| 6-10 | 58% |
| 10-20 | 60% |
| 20+ | **74.4%** |

→ PosterBench 适合**系统排名**，不适合**个体海报排序**——做产品落地时按分差分段使用。

## 前提与局限性

- **Pearson r=0.34 不算高**——评估协议能区分系统但不能很好预测人类盲评；分差 ≤3 分时人类一致率近随机
- **100 papers 是适度规模**——5 学科覆盖但不是 paper-to-poster 全领域（缺 ACL/ICCV 最佳海报、设计领域海报等）
- **11 评审偏少**——Bradley-Terry 估计区间宽（55.2-77.8%），评审数与评审间一致性未充分披露
- **optimization-time evaluator 与 frozen 协议分离的设计聪明但有 trade-off**——R_meta 在 Dtrain 上被优化，可能学到了 Ddev 之外未见过的 pattern；评估器固定只用于 gate 而不是 reward，但 gate 的 J_dev 已经包含它的判断
- **paper-to-poster 单任务基准**——slide/webpage/video 是 pilot，**未经 controlled benchmark 验证**

## 评估协议 vs 其它基准

| 维度 | PosterBench | CORE-Bench | ITBench | SWE-Bench |
|------|------------|-----------|---------|-----------|
| 任务 | paper-to-poster | 通用 agent | IT 运维 | 代码修复 |
| 协议 | 七维 rubric | 时间相关任务 | 故障注入 | pass/fail 测试 |
| 人类 ground truth | 933 pairwise | 无 | 无 | 无 |
| 多模型对照 | 7 配置 + 4 系统 | 弱 | 弱 | 强 |
| 工业级 controlled matrix | 6 track | 无 | 无 | 弱 |

→ PosterBench 在**多系统对照 + 人类 ground truth + controlled factor 隔离**三维度上明显领先同类基准。

## 关联概念

- [[Meta-Harness-Optimization]] — PosterBench 是 Meta-Harness 优化的工业级 benchmark
- Bradley-Terry 人类偏好估计 — 933 pairwise 评审的统计建模方法
- [[Rubric-Based-Evaluation]] — 七维评分是 rubric 评估的扩展形式
- [[LLM-as-a-Judge]] — Aesthetics 等感知维度的 VLM 判断
- [[Evaluator-Miscalibration]] — Pearson r=0.34 是评估器校准的实际案例
- Evaluation-Driven Development — R_meta 评估器驱动的 harness 优化循环
- Long-Horizon Agentic Design — PosterBench 评测的范式

## 数据卡片

| 维度 | 数值 |
|------|------|
| Main Track 规模 | 100 papers, 5 学科 |
| PosterBench-mini | 10 papers |
| 七维 | Faithfulness / Coverage / Density / Visual Evidence / Layout / Readability / Aesthetics |
| Controlled track | 6（含 Harness-Attachment Ablation）|
| 人类盲评 | 933 pairwise, 11 评审, 4 系统 |
| BT 估计 | AutoDesign 64.0% (CI 55.2-77.8%) |
| 评估-人类 Pearson r | 0.34 (CI [0.22, 0.44]) |
| AutoDesign Main Track | 78.32 |
| vs Claude Design | +7.45 |