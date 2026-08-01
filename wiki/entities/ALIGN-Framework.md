---
type: entity
title: "ALIGN Framework"
aliases:
  - ALIGN
  - ALIGN Framework
  - Auto-Aligned Interface Generation
  - 自动对齐接口生成
  - ALIGN-generated interface
definition: "清华 NLP (THUNLP-MT) 提出的自动生成 agent-environment 对齐接口的框架。由 Analyzer（从失败轨迹诊断错位）与 Optimizer（合成 Python 函数形式的接口）迭代协作，输出 INFERRULES（前置暴露静态规则）+ WRAPSTEP（动态增强观察）两个模块的 Python wrapper，**不改 agent 逻辑或环境代码**。在 4 个 benchmark（ALFWorld / ScienceWorld / WebShop / M3ToolEval）上一致提升 6-46%，接口 plug-and-play 跨 5 种 agent 架构和多种 LLM backbone。"
created: 2026-08-01
updated: 2026-08-01
tags:
  - AI-Agent
  - harness
  - interface
  - llm-agent
related_entities:
  - "[[Agent-Environment-Misalignment]]"
  - "[[Agent-Harness]]"
  - "[[ACI-Agent-Computer-Interface]]"
  - "[[Agent-Verification]]"
  - "[[Building-Effective-Agents]]"
source_raw:
  - "[[20260801-align-agent-environment-interface.pdf]]"
  - "[[20260801-openbmb-align-tweet.md]]"
---

# ALIGN Framework

> [!definition] 定义
> **ALIGN**（Auto-Aligned Interface Generation）是清华 NLP (THUNLP-MT) 提出的**自动生成 agent-environment 对齐接口**的框架。它通过 Analyzer（从失败轨迹诊断错位）与 Optimizer（合成 Python 函数形式的接口）迭代协作，输出两个模块 `INFERRULES`（前置暴露静态规则）+ `WRAPSTEP`（动态增强观察）作为 Python wrapper，**不改 agent 逻辑或环境代码**。

## 框架核心：`Φ = {INFERRULES, WRAPSTEP}`

```python
# ALIGN 接口 = 两个 Python 函数
Φ = {
    INFERRULES: (task, o₀) → Ĩ,      # 静态规则暴露
    WRAPSTEP:   (F, sₜ, aₜ) → õₜ,    # 动态观察增强
}

# 包装后的环境：Ẽ = (S, A, T, F̃, I ∪ Ĩ)
# 其中 F̃(sₜ, aₜ) := WRAPSTEP(F, sₜ, aₜ)
```

| 模块 | 输入 | 输出 | 作用 |
|------|------|------|------|
| **INFERRULES** | 任务描述 + 初始观察 `o₀` | 增强的静态信息 `Ĩ` | 暴露前置依赖、动作顺序、环境规则 |
| **WRAPSTEP** | 原始观察函数 `F`、状态 `sₜ`、动作 `aₜ` | 增强的观察 `õₜ` | 附加成功/失败条件、推断的前置条件 |

**形态**：轻量 Python wrapper，部署在 agent 和 environment 之间，不修改任何一方代码。

## 三阶段迭代（Algorithm 1）

```
Stage 1: Misalignment Analysis
  Analyzer 从上一轮的失败轨迹 τ_fail^{(i-1)} 诊断新的错位集 M^{(i)}

Stage 2: Interface Generation
  Optimizer 基于 M^{(i)} 和上一轮接口 Φ^{(i-1)} 生成新接口 Φ^{(i)}
  ⊕ 实验验证：Optimizer 真的与环境交互，确认错位存在且新接口能解决

Stage 3: Execution with Interface
  Agent 用 Φ^{(i)} 与 Ẽ^{(i)} 交互
  失败轨迹 τ_fail^{(i)} 反馈给下一轮 Analyzer

终止条件：训练集无失败 / 无新错位 / 达到最大迭代次数 K
```

## Analyzer：错位诊断器

LLM-based 模块，输入：
- 上一轮的失败轨迹 `τ_fail^{(i-1)}`
- 当前已识别的错位集 `M`
- 上一轮接口 `Φ^{(i-1)}`

输出：结构化的错位描述（三元组）：
```
{
  "Agent High-Level Reasoning Intent": "...",  // agent 对动作的预期
  "Environment Rule": "...",                    // 环境的隐式规则
  "Sufficient Observation": "...",              // 环境应提供的反馈
}
```

**关键创新**：错位被**结构化为文本**而非自由生成——便于 Optimizer 处理和迭代。

## Optimizer：接口合成器

LLM-based 模块，输入：
- 新错位集 `M^{(i)}`
- 上一轮接口 `Φ^{(i-1)}`

输出：新的 Python 函数 `INFERRULES` 和 `WRAPSTEP`。

**核心机制——实验验证对抗幻觉**：

```
Optimizer 生成新接口 Φ^{(i)}
  ↓
真的在环境中执行（用工具封装的环境）
  ↓
能否解决 M^{(i)}？
  ├─ Yes → 输出 Φ^{(i)}
  └─ No  → 提供 refine_strategy → 重新生成
```

消融显示：无实验验证时，T=0.5 下 4 轮迭代后准确率从 23.88% → 0.75%，**完全崩塌**（Table 5）。

## 主实验结果（Table 1）

5 个 agent 方法 × 4 个 benchmark，全部正收益：

| Agent | ALFWorld | ScienceWorld | WebShop | M3ToolEval |
|-------|----------|--------------|---------|------------|
| Vanilla | +47.02 | +12.75 | +7.13 | +9.72 |
| ReAct | +44.03 | +8.94 | +5.73 | +8.34 |
| Self-Consistency | **+57.46** | +11.34 | +4.87 | +5.56 |
| Self-Refine | +36.57 | +8.12 | +7.50 | +1.39 |
| Planning | +43.29 | +9.21 | +7.72 | +6.95 |
| **平均** | **+45.67** | **+10.07** | **+6.59** | **+6.39** |

> **平均提升 = 45.67% 成功率**（ALFWorld）

## 关键能力一：减少连续无效动作（Table 2）

| Agent | ALFWorld 降幅 | ScienceWorld 降幅 |
|-------|--------------|-------------------|
| Vanilla | -66% | -50% |
| ReAct | -53% | -36% |
| Self-Consistency | -81% | -38% |
| Self-Refine | -49% | -49% |
| Planning | -74% | -70% |
| **平均** | **-65%** | **-49%** |

连续无效动作的减少直接证明：ALIGN 让 agent 对"前置条件"更敏感，能从孤立错误中恢复。

## 关键能力二：Plug-and-Play 泛化（Table 3）

**(a) 跨 agent 架构**：用 Vanilla 生成的接口应用于其他 agent：
- ALFWorld +41.61（平均）、ScienceWorld +12.84、WebShop +5.08、M3ToolEval +7.29

**(b) 跨 LLM backbone**：用 Qwen2.5-7B 生成的接口应用于其他模型：

| Target LLM | ALFWorld | ScienceWorld | WebShop | M3ToolEval |
|------------|----------|--------------|---------|------------|
| Qwen2.5-14B-Instruct | +17.46 | +4.61 | +4.66 | +6.11 |
| Llama3.1-8B-Instruct | +5.97 | +10.27 | +0.33 | +0.83 |
| Llama3.3-70B-Instruct | +5.82 | +3.99 | +5.68 | +1.67 |

**结论**：ALIGN 捕获的是**真实的环境约束**，不是针对特定 agent 的过拟合。

## 组件消融（Table 4）

去掉任一组件都导致性能下降，去掉 WRAPSTEP 下降更显著：

| 组件 | ALFWorld 降幅 | ScienceWorld 降幅 |
|------|--------------|-------------------|
| w/o INFERRULES | -6.72（平均） | -2.05（平均） |
| w/o WRAPSTEP | **-31.79**（平均） | -7.84（平均） |

> **WRAPSTEP 是关键**——细粒度的观察增强比静态规则暴露更重要。

## 关键数据点

- ALFWorld 上 Qwen2.5-7B-Instruct：13.4% → 31.3%（仅改写反馈）→ 60.45%（完整 ALIGN Vanilla）→ 69.40%（ALIGN + Self-Consistency）
- 5 agent × 4 benchmark 平均提升：ALFWorld +45.67%、ScienceWorld +10.07、WebShop +6.59、M3ToolEval +6.39
- 连续无效动作平均下降：ALFWorld -65%、ScienceWorld -49%
- 跨 backbone 泛化：Qwen2.5-14B +17.46（ALFWorld）、Llama3.3-70B +5.82（方向一致）
- 实验验证消融：无验证时 T=0.5 下准确率 23.88% → 0.75%
- 组件消融：去 INFERRULES -6.72，去 WRAPSTEP -31.79

## 实现细节

- **Base model**：所有 agent 默认用 Qwen2.5-7B-Instruct
- **Optimizer**：interface generation 用 Gemini 2.5 Pro
- **Analyzer + 其他步骤**：用 GPT-4.1
- **代码**：https://github.com/THUNLP-MT/ALIGN
- **论文**：arXiv:2505.21055（2025-05-27）

## 与 ACI 的关系

[[ACI-Agent-Computer-Interface|ACI]]（SWE-agent 提出）是**人工设计的 agent-computer 接口**——人类为 Agent 设计最佳工具描述、参数 schema、错误反馈。

| 维度 | ACI | ALIGN |
|------|-----|-------|
| 设计方式 | 人类手工 handcraft | LLM 自动生成 |
| 适用环境 | 单一环境 | 跨环境通用 |
| 优化机制 | 一次性 | 迭代（从失败学习） |
| 成本 | 高（需人工调优） | 中（多轮 LLM 调用） |
| 维护 | 改环境需重新设计 | 自动更新 |

ALIGN 可以视为 **ACI 的工业化、自动化版本**。

## 前提与局限性

- **方向性单向**：用强模型生成接口给弱模型，反向未验证
- **环境覆盖**：实验集中在文本环境，多模态环境（OSWorld、GAIA）未测
- **成本未报告**：迭代生成接口的 API 成本 vs 性能提升的 trade-off 未量化
- **统计方差**：Table 1 没有报告方差或置信区间，小幅提升的统计显著性未知
- **LLM-as-Analyzer 边界**：真正隐式的环境规则（如模拟器物理约束），LLM 不一定能识别
- **"无验证崩塌"**：依赖 LLM-as-Optimizer 链路的健康度，失败时无 fallback

## 关联概念

- [[Agent-Environment-Misalignment]] — ALIGN 解决的问题
- [[Agent-Harness]] — ALIGN 是 harness 内部接口层的自动化实现
- [[ACI-Agent-Computer-Interface]] — ALIGN 是 ACI 的工业化版本
- [[Building-Effective-Agents]] — "Well-crafted ACI"原则的算法化
- [[Agent-Verification]] — ALIGN 的实验验证步骤是 verification 循环的强化版
- *（ALIGN 抽象出的"自动接口生成"作为机制类暂未单独建 entity，与 [[ACI-Agent-Computer-Interface]] 对照阅读即可）*