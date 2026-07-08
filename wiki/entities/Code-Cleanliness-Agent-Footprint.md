---
type: entity
title: Code Cleanliness Agent Footprint
aliases:
  - Code Cleanliness Agent Footprint
  - 代码整洁度对 Agent 足迹效应
  - Code Cleanliness Effect
definition: "代码整洁度不影响 coding agent 的任务通过率，但显著降低其操作足迹（token −7-8%、file revisitation −34%）的实证现象。来自 SonarSource 2026 年 minimal-pair 研究。"
created: 2026-07-08
updated: 2026-07-08
tags:
  - Agentic-Engineering
  - code-quality
  - token-efficiency
evidence_level: high
claim_type: extracted
related_entities:
  - "[[Agentic-Workflow-Token-Efficiency]]"
  - "[[Agent-Harness]]"
  - "[[Minimal-Pair-Evaluation]]"
  - "[[Agentic-Engineering]]"
  - "[[Agent-Ergonomics]]"
  - "[[Context-Engineering]]"
source_raw:
  - "[[202605-code-cleanliness-coding-agents-minimal-pair.pdf]]"
---

# Code-Cleanliness-Agent-Footprint（代码整洁度的 Agent 足迹效应）

> [!definition] 定义
> **Code-Cleanliness-Agent-Footprint** 是指代码整洁度不影响 coding agent 能否完成任务，但显著改变其操作成本结构的实证现象：整洁代码使 agent 使用更少 token（−7-8%）并大幅减少文件回访（−34%）。

## 核心发现

### 通过率不变，足迹收缩

SonarSource 的 minimal-pair 实验（660 次试验，Claude Sonnet 4.6 + Claude Code）发现：

| 指标 | 变化幅度 | 解读 |
|------|----------|------|
| 任务通过率 | −0.9pp（不显著） | agent 都能做对，与代码质量无关 |
| Input tokens | −7.1% | agent 拉入更少的代码到上下文 |
| Output tokens | −8.5% | 产出（工具调用+代码+推理）更少 |
| Reasoning chars | −11.1% | 推理过程更精简 |
| File revisitation | **−34%** | 最大效应：不再反复回去验证 |
| Conversation turns | −7.0% | 对话更短 |

### File Revisitation：最大单一效应

> [!important] 核心机制
> Agent 在脏代码上的典型行为是 `read → edit → read again`——反复回去确认之前的修改是否正确。在干净代码上是 `read → edit → move on`——读一次就定稿。

这个 34% 的差距在所有 6 个仓库对上都成立（−7% 到 −69%），是最稳健的信号。

**类比**：在一个标识清晰的网格城市里，你去过的地方不需要再回去确认；在一个没有路标的有机生长区域里，你不断折返验证"刚才走对了没有"。

### 任务拓扑的调节效应

论文按任务类型拆分为三条轨道：

| 轨道 | Token 效应 | 行为差异 |
|------|-----------|---------|
| Calibration（简单） | 接近零 | 基线 |
| Boundary-crossing（跨模块） | −11.0% input | 受益最大——跨模块导航时整洁度价值更高 |
| Cognitive-hotspot（高密度区域） | ~0% input | token 不变但读更多文件——重构把复杂度分散到了更多 helper |

**张力**：boundary-crossing 和 cognitive-hotspot 两个轨道拉扯方向相反。Clean 版本在热点任务上把逻辑分散到更多文件（helper extraction），导致 agent 需要读更多文件但每次编辑更少。聚合后 −7.1% 是两种行为平均后的净效应。

### Per-task 方差极大

- 同一任务同一侧 10 次试验，最贵的通常是 2.5 倍最便宜的
- 27 个真实任务中，16 个在 clean 侧更便宜，11 个在 messy 侧更便宜（60/40 而非聚合数字暗示的压倒性优势）
- 极端案例：ckan/organization-list-exclude-empty 的 10 次 clean 试验跨度 1.4M–10.6M input tokens

**实践含义**：单个任务的 ~10% delta 可能是 agent 噪声；只有聚合数百次试验才能提取信号。

## 评论混淆实验

论文做了关键控制：归一化两侧评论行数后发现——

| 仓库对 | 原始 input tok ∆ | 归一化后 ∆ |
|--------|-----------------|-----------|
| sonar-caas-poc | +1.2% | −18.0% |
| sonar-sca | +1.3% | −8.5% |
| sonarcloud-codedatalake | −29.0% | −30.6% |
| genie | +5.2% | +3.0% |

sonar-caas-poc 归一化后方向翻转，说明原始效应中确实有评论量贡献；但 sonar-sca 和 sonarcloud-codedatalake 的效应保持或增强，说明代码结构本身的贡献是真实的。

## 对 Agentic Engineering 的启示

### 代码质量是第四类 Token 效率杠杆

在 [[Agentic-Workflow-Token-Efficiency]] 已识别的三类杠杆（模型选择 9x、工具裁剪、上下文管理）之外，本文新增第四类：

| 杠杆 | 典型幅度 | 改动成本 |
|------|----------|---------|
| 模型选择 | ~9x | 切换 API |
| 工具裁剪 | −8-12KB 上下文 | 修改 MCP 配置 |
| 上下文管理 | −26-54% | 重构 harness |
| **代码整洁度** | **−7-8%** | **持续代码治理** |

幅度最小但不需要改 harness——它是唯一"不需要碰 agent 基础设施"的杠杆。

### 投资回报率翻转

AI 时代代码质量投资的 ROI 论证应新增一行：

> "整洁代码不仅降低人类维护成本，还降低 agent 运营成本——每次 agent 交互都少用 7-8% 的 token，在高频率 agent 工作流中年化效果显著。"

## 关键数据点

| 指标 | 数据 |
|------|------|
| 试验总次数 | 660 (6 pair × 33 tasks × 10 trials) |
| 通过率 (cleaner) | 0.913 |
| 通过率 (messier) | 0.921 (差距 −0.9pp) |
| Input tokens ∆ | −7.1% |
| Output tokens ∆ | −8.5% |
| Reasoning chars ∆ | −11.1% |
| File revisitation ∆ | **−34%** (最大效应) |
| Conversation turns ∆ | −7.0% |
| 最贵/最便宜试验比 | ~2.5x (trial-to-trial variance) |
| Per-task input token delta 范围 | −47% to +44% |
| 模型 | Claude Sonnet 4.6 + Claude Code |

## 前提与局限性

- 仅 Claude Sonnet 4.6 + Claude Code，未测试其他模型或 harness
- Haiku 4.5 试验噪声过大无法提取信号
- 仓库和任务由作者策划，可能存在选择偏差
- 只检测 hidden test，不检查是否破坏了既有测试
- 未检测 agent 输出代码的整洁度——整洁度是否自我强化或自我侵蚀未知
- 效应仅在短程任务（单任务）上测量，长程累积效应未验证

## 关联概念

- [[Minimal-Pair-Evaluation]] — 产生这一发现的方法论
- [[Agentic-Workflow-Token-Efficiency]] — 代码质量作为第四类 token 效率杠杆
- [[Agent-Harness]] — harness 运行的"地形复杂度"维度
- [[Context-Engineering]] — 整洁代码减少 agent 需要处理的上下文量
- [[Agent-Ergonomics]] — agent 工作环境的质量影响其操作效率
