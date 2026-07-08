---
type: entity
title: Minimal Pair Evaluation
aliases:
  - Minimal Pair Evaluation
  - 最小对比对评估
  - Minimal-Pair Study
definition: "构造在架构、依赖和外部行为上匹配，仅在目标变量上不同的仓库对，以隔离该变量对 coding agent 行为的独立影响。SonarSource (2026) 首次提出的评估方法论。"
created: 2026-07-08
updated: 2026-07-08
tags:
  - evaluation-methodology
  - agentic-engineering
  - benchmark
evidence_level: high
claim_type: extracted
related_entities:
  - "[[Code-Cleanliness-Agent-Footprint]]"
  - "[[Agent-Harness]]"
  - "[[Agentic-Workflow-Token-Efficiency]]"
source_raw:
  - "[[202605-code-cleanliness-coding-agents-minimal-pair.pdf]]"
---

# Minimal-Pair-Evaluation（最小对比对评估）

> [!definition] 定义
> **Minimal-Pair-Evaluation** 是一种评估方法论：构造在架构、依赖和外部行为上完全匹配，仅在目标变量（如代码整洁度）上不同的仓库对，以隔离该变量对 coding agent 行为的独立因果影响。

## 方法论核心

### SWE-bench 的方法论缺口

SWE-bench 系列（Jimenez et al., 2024; Chowdhury et al., 2024）的每个 instance 是单个仓库单个版本。任何跨 instance 的差异都混淆了任务难度和代码状态——你无法区分 agent 失败是因为任务难还是代码脏。

Minimal-pair evaluation 填补了这个缺口：**同一个任务在两个版本上运行，唯一差异是目标变量。**

### 双向构造

论文用两个方向的 agent pipeline 构建 minimal pairs：

| 方向 | 名称 | 输入 | 输出 |
|------|------|------|------|
| 降级 | Slopify | 干净仓库 | 合理的脏版本（模拟没有 code review 的历史） |
| 清理 | Vibeclean | 脏仓库 | 合理的干净版本（模拟有 static analysis 门控的历史） |

**双向设计的价值**：两个方向产生略微不同形状的 pair，防止结论只适用于单一构造方向。

### 三阶段 Pipeline

Slopify pipeline 的三阶段（为减少 agent 脱轨）：

1. **Build**：编译仓库、测试通过、冻结构建指令到 `build-instructions.md`
2. **Explore**：遍历仓库、为每个值得降级的目录写 `summary.md`
3. **Transform**：基于摘要执行降级变换

### 三条任务设计规则

1. **Route through hotspots**：任务锚定在 pair 两侧差异最大的代码区域
2. **Describe in externally observable terms**：任务描述只说外部行为，不指定实现路径
3. **Verify through hidden tests**：通过应用公共表面的隐藏测试评分

### 三条任务轨道

| 轨道 | 设计意图 | 数量 |
|------|---------|------|
| Calibration | 不涉及差异区域的任务（基线对照） | 6 |
| Boundary-crossing | 跨多个模块边界的任务 | 14 |
| Cognitive-hotspot | 集中在单一高密度代码区域的任务 | 13 |

## 6 个仓库对

| 仓库 | Pipeline | NCLOC (k) | Issues (clean/messy) | Issue density (per kLOC) |
|------|----------|-----------|---------------------|-------------------------|
| sonar-sca | Slopify | 128.8/136.7 | 94/2,825 | 0.73/20.66 |
| sonar-caas-poc | Slopify | 26.2/31.5 | 16/855 | 0.61/27.16 |
| sonarcloud-codedatalake | Slopify | 45.6/38.4 | 199/1,319 | 4.36/34.39 |
| commons-bcel | Vibeclean | 55.1/54.8 | 694/2,711 | 12.60/49.46 |
| genie | Vibeclean | 118.8/116.7 | 152/1,262 | 1.28/10.81 |
| ckan | Vibeclean | 133.4/132.1 | 1,006/3,632 | 7.54/27.50 |

## 10 个度量指标

| 类别 | 指标 | 含义 |
|------|------|------|
| **正确性** | Pass rate | 隐藏测试通过率 |
| **足迹** | Input tokens | agent 读入的总 token |
| **足迹** | Output tokens | agent 产出的总 token |
| **足迹** | Reasoning characters | 推理过程字符数 |
| **轨迹** | Conversation turns | agent-工具交互总轮次 |
| **轨迹** | Turns before first edit | 首次编辑前的轮次 |
| **轨迹** | Characters before first edit | 首次编辑前的总字符数 |
| **导航** | Files read | 打开的不同文件数 |
| **导航** | File revisitation | 已编辑文件的回访次数 |
| **导航** | Lines edited | 修改的源代码行数 |

## 方法论的可迁移性

Minimal-pair evaluation 原则上可迁移到任何二元变量的因果隔离：

- **类型系统**：强类型 vs 弱类型版本的 agent 行为差异
- **文档密度**：有/无 API 文档对 agent 导航效率的影响
- **测试覆盖**：高/低测试覆盖率对 agent 修改信心的影响
- **架构风格**：monolith vs microservice 结构的 agent 任务完成差异

## 关键数据点

| 指标 | 数据 |
|------|------|
| Minimal pairs 数量 | 6（3 Slopify + 3 Vibeclean） |
| 编码任务数 | 33（6 calibration + 14 boundary-crossing + 13 cognitive-hotspot） |
| 试验总次数 | 660 |
| 度量指标 | 10 个（1 正确性 + 3 足迹 + 3 轨迹 + 3 导航） |
| 代码语言 | Java + Python |
| SonarQube issue 差距 | 最大 pair (sonar-sca): 94 vs 2,825 issues |

## 前提与局限性

- 构造 minimal pair 需要大量前期工作（agent pipeline + 人工验证）
- "clean" 和 "messy" 是 pair 内标签，不是对原始仓库的评判
- SonarQube 规则集作为整洁度代理可能有工具特定偏差
- 论文未开源 benchmark（截至 2026-07 状态），限制了独立复现

## 关联概念

- [[Code-Cleanliness-Agent-Footprint]] — 本方法论产生的核心发现
- [[Agentic-Workflow-Token-Efficiency]] — minimal pair 方法验证的效率杠杆之一
- [[Agent-Verification]] — minimal pair 是 agent 评估的方法论创新
