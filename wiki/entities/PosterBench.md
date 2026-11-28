---
type: entity
title: PosterBench
aliases:
  - PosterBench
  - PosterBench-Main-Track
  - PosterBench-mini
definition: "AutoDesign 发布的 paper-to-poster 评估基准——100 篇五学科 Main Track + 10 篇 PosterBench-mini 固定子集，七维评估协议（Faithfulness / Coverage / Density / Visual Evidence / Layout / Readability / Aesthetics），另有11名志愿者提供933次有效盲评比较，用Bradley-Terry估计偏好；不是客观ground truth。本页描述作者发布的评估协议，非全行业排名"
created: 2026-08-16
updated: 2026-11-28
tags:
  - benchmark
  - agent-evaluation
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
> **PosterBench** 是 AutoDesign (Luo et al., 2026) 发布的 paper-to-poster 评估基准，包含 PosterBench Main Track（100 篇五学科论文）+ PosterBench-mini（10 篇固定子集，受控对照用）+ 933 次人类盲评对（Bradley-Terry 估计）+ 七维评估协议（Faithfulness / Coverage / Density / Visual Evidence / Layout / Readability / Aesthetics）。本页描述作者发布的评估协议，非全行业排名。

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

**冻结的PosterBench评分（式7–8）**：七维0–10分，权重(10,10,15,10,20,25,10)，逐海报加权后应用layout/viability/failure/gate中最严格的分数上限，再平均。标准P0上限40；不可直接从各维平均反推总体分。R_meta是优化期评估器，不是同一冻结协议。

**关键设计**：optimization-time evaluator 与 frozen PosterBench 协议**分离**——前者参与 harness 优化，后者只在最终系统比较时使用，避免"评估器被同向优化"。

### 主要结果

**Main Track 完整系统比较（100 papers, 5 学科）**

| 系统 | PosterBench Score |
|------|------------------|
| **AutoDesign** | **78.32** |
| Claude Design（商业） | 70.87 |
| Claude Code（coding agent） | 70.01 |
| OpenDesign（Claude Code + Claude 4.8） | 69.45 |

→ AutoDesign 超 Claude Design **+7.45 分**（商业系统对比）

**人类盲评（n=933 pairwise）**

| 系统 | BT 偏好估计 |
|------|------------|
| AutoDesign | 64.0%（95% CI: 55.2-77.8%）|
| Claude Code | 本轮未复核图中估计 |
| OpenDesign | 本轮未复核图中估计 |
| Claude Design | — |

- AutoDesign 对 Claude Design 胜率 67.6%
- 评估-人类偏好相关性：Pearson r=0.34（CI [0.22, 0.44]）

### 关键实验发现

**Harness-Attachment Ablation 普遍正增益**

PosterBench-mini 10篇、7个已完成配置平均54.99→67.39（+12.40分，非相对+12.4%）；DeepSeek V4 Pro最大+19.56，Claude 4.8最小+5.01；GPT-5.5 +5.59。上限效应为候选解释。详见 [[Meta-Harness-Optimization]] 数据表。

**评估器 vs 人类偏好的一致性**

| 评估分差区间 | 人类一致率 |
|------------|----------|
| 0-3 | 52%（近随机）|
| 3-6 | 未复核图中数值 |
| 6-10 | 未复核图中数值 |
| 10-20 | 未复核图中数值 |
| 20+ | **74.4%** |

→ 在919个非同分有效比较中，0–3分差一致率51.9%，≥20分差74.4%。分差提供该样本内的判断强度信息，不证明系统排名必然可靠，也不是通用发布阈值。未核对图像中的中间分段值及其余系统BT点估计，暂不作数值引用；历史记录仍在Git。

## 前提与局限性

- **Pearson r=0.34 不算高**——评估协议能区分系统但不能很好预测人类盲评；分差 ≤3 分时人类一致率近随机
- **100 papers 是适度规模**——5 学科覆盖但不是 paper-to-poster 全领域（缺 ACL/ICCV 最佳海报、设计领域海报等）
- **11 评审偏少**——Bradley-Terry 估计区间宽（55.2-77.8%），评审数与评审间一致性未充分披露
- **optimization-time evaluator 与 frozen 协议分离的设计聪明但有 trade-off**——R_meta用于评价候选Harness的训练与开发集表现，而非被外环同时优化；冻结PosterBench独立评分。多次使用Ddev门禁仍可能适应开发集反馈。
- **paper-to-poster 单任务基准**——slide/webpage/video 是 pilot，**未经 controlled benchmark 验证**

## 评估协议 vs 其它基准

| 维度 | PosterBench | CORE-Bench | ITBench | SWE-Bench |
|------|------------|-----------|---------|-----------|
| 任务 | paper-to-poster | 科学计算复现 | IT 运维 | 软件问题解决 |
| 协议 | 七维 rubric | 指定计算结果复现 | 按具体 ITBench 版本 | 补丁与测试结果 |
| 参考证据 | 933 pairwise 人类偏好记录 | 论文相关计算结果 | 按具体版本 | issue 与测试；Verified 含工程师复核 |

不同基准衡量不同任务及目标；未采用统一任务集、成本与评分协议，不能据这些维度宣称 PosterBench 整体领先。2026-11-28核对[AutoDesign v1 HTML](https://arxiv.org/html/2608.13560v1) §5、式7–8及表1–4、§5.3；未复跑实验、未复核其他基准版本或原始盲评记录。

## 关联概念

- [[Meta-Harness-Optimization]] — PosterBench 是学术海报任务的作者自建benchmark
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
| Controlled tracks | 三个受控track（Design Harness/Coding Harness/Model），另有Main Track、mini及attachment ablation |
| 人类盲评 | 933 pairwise, 11 评审, 4 系统 |
| BT 估计 | AutoDesign 64.0% (CI 55.2-77.8%) |
| 评估-人类 Pearson r | 0.34 (CI [0.22, 0.44]) |
| AutoDesign Main Track | 78.32 |
| vs Claude Design | +7.45 |