---
type: entity
title: "ALIGN Framework"
aliases:
  - ALIGN
  - ALIGN Framework
  - Auto-Aligned Interface Generation
  - 自动对齐接口生成
  - ALIGN-generated interface
definition: "清华 NLP (THUNLP-MT) 提出的自动生成 agent-environment 对齐接口的框架。由 Analyzer（从失败轨迹诊断错位）与 Optimizer（合成 Python 函数形式的接口）迭代协作，输出 INFERRULES（前置暴露静态规则）+ WRAPSTEP（动态增强观察）两个模块的 Python wrapper，**不改 agent 逻辑或环境代码**。在4个文本基准的已测组合上平均增益为6.39–45.67（分或百分点，依指标而定），同环境内测试了跨Agent方法及模型迁移；不是跨任意环境通用。"
created: 2026-08-01
updated: 2026-11-28
evidence_level: medium
claim_type: mixed
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

**形态**：生成Python wrapper，不修改原始Agent逻辑或环境代码。v3 §3.1另定义Action Transducer，实际方法将其限定为identity的任务语义；Appendix D.6审计87个env.step调用点，65原样、17增加只读探查或导航子步骤、5表层规范化、0语义重映射。不能将“不改原代码”误作完全无新增环境动作。

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

ALFWorld Vanilla无实验验证消融：T=.5从Iter0 13.43%→23.88%→1.49%→0.75%，T=.2为13.43%→22.39%→0→0（v1 Table 5/v3 Table 6）；仅为该流程实证。

## 主实验结果（Table 1）

5个Agent方法×4基准的主实验组合均为正增益（ALFWorld/M3ToolEval为百分点，ScienceWorld/WebShop为分）：

| Agent | ALFWorld | ScienceWorld | WebShop | M3ToolEval |
|-------|----------|--------------|---------|------------|
| Vanilla | +47.02 | +12.75 | +7.13 | +9.72 |
| ReAct | +44.03 | +8.94 | +5.73 | +8.34 |
| Self-Consistency | **+57.46** | +11.34 | +4.87 | +5.56 |
| Self-Refine | +36.57 | +8.12 | +7.50 | +1.39 |
| Planning | +43.29 | +9.21 | +7.72 | +6.95 |
| **平均** | **+45.67** | **+10.07** | **+6.59** | **+6.39** |

> ALFWorld五种Agent平均绝对增益为45.67个百分点，不是相对增长率。

## 关键能力一：减少连续无效动作（Table 2）

| Agent | ALFWorld 降幅 | ScienceWorld 降幅 |
|-------|--------------|-------------------|
| Vanilla | -66% | -50% |
| ReAct | -53% | -36% |
| Self-Consistency | -81% | -38% |
| Self-Refine | -49% | -49% |
| Planning | -74% | -70% |
| **平均** | **-65%** | **-49%** |

Table 2报告连续无效动作比例的相对下降；支持行为改善，但不单独证明唯一机制或因果归因。

## 关键能力二：Plug-and-Play 泛化（Table 3）

**(a) 跨 agent 架构**：用 Vanilla 生成的接口应用于其他 agent：
- ALFWorld +41.61（平均）、ScienceWorld +12.84、WebShop +5.08、M3ToolEval +7.29

**(b) 跨 LLM backbone**：用 Qwen2.5-7B 生成的接口应用于其他模型：

| Target LLM | ALFWorld | ScienceWorld | WebShop | M3ToolEval |
|------------|----------|--------------|---------|------------|
| Qwen2.5-14B-Instruct | +17.46 | +4.61 | +4.66 | +6.11 |
| Llama3.1-8B-Instruct | +5.97 | +10.27 | +0.33 | +0.83 |
| Llama3.3-70B-Instruct | +5.82 | +3.99 | +5.68 | +1.67 |

**证据边界**：这些结果支持 ALIGN 生成接口在论文测试范围内可跨若干 agent 架构与 LLM backbone 复用；它降低了“只对单一 agent 过拟合”的解释可能性，但不能证明跨任意环境/模态都捕获同一类真实约束。

## 组件消融（v1 Table 4 / v3 Table 5）

ALFWorld及ScienceWorld的平均消融均下降，WRAPSTEP降幅较大；v3 Appendix C.5/Table 15也有去掉WrapStep后ReAct在WebShop +4.67分、M3ToolEval +1.38个百分点的反例，不外推必然正收益。

| 组件 | ALFWorld 降幅 | ScienceWorld 降幅 |
|------|--------------|-------------------|
| w/o INFERRULES | -6.72（平均） | -2.05（平均） |
| w/o WRAPSTEP | **-31.79**（平均） | -7.84（平均） |

> 该两基准中WrapStep的平均条件贡献更大；组件相对价值依任务和实现。v3修正Self-Consistency去WrapStep的ALFWorld降幅为-46.27（v1表为-37.27、与均值不符）。

## 关键数据点

- ALFWorld 上 Qwen2.5-7B-Instruct：13.4% → 31.3%（仅改写反馈）→ 60.45%（完整 ALIGN Vanilla）→ 69.40%（ALIGN + Self-Consistency）
- 5 agent × 4 benchmark 平均提升：ALFWorld +45.67个百分点、ScienceWorld +10.07分、WebShop +6.59分、M3ToolEval +6.39个百分点
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

[[ACI-Agent-Computer-Interface|ACI]]（SWE-agent 提出）是广义的Agent-Computer Interface设计概念，SWE-agent实例采用人工设计——人类为 Agent 设计最佳工具描述、参数 schema、错误反馈。

| 维度 | ACI | ALIGN |
|------|-----|-------|
| 设计方式 | 人类手工 handcraft | LLM 自动生成 |
| 适用环境 | 可为多环境设计 | 各环境分别生成；已测同环境跨Agent/模型复用 |
| 优化机制 | 人工或自动迭代 | 从失败轨迹生成候选并实验验证 |
| 成本 | 依设计/测试/维护而定 | 有离线生成成本及后续维护成本 |
| 维护 | 可迭代更新 | 测试时冻结接口，环境变化后重验 |

ALIGN是自动化接口设计的研究实例，不代表工业化成熟度或取代所有人工设计。

## 前提与局限性

- **生成器能力门槛**：v3 D.5/Table18中GPT-4.1-mini分析/验证+Gemini 2.5 Pro代码合成可以生成有效接口（ALFWorld Qwen2.5-7B 13.43→64.93）；全7B栈在32k/65k/131k三次运行未完成验证（290假说/0验证）。目标模型泛化与生成器能力是两件事。
- **环境覆盖**：实验集中在文本环境，多模态环境（OSWorld、GAIA）未测
- **成本**：v3 Appendix E/Table 20–21：ALFWorld接口生成8轮、每轮约0.55M Token，按当时标价约9.4美元；四环境约30美元。作者报告复用时单任务输入Token为基线58%、LLM调用为43%，估计付费API场景约120次任务摊回生成费；并非生产TCO或未来环境无需维护。
- **统计方差**：Table 1 没有报告方差或置信区间，小幅提升的统计显著性未知
- **LLM-as-Analyzer 边界**：真正隐式的环境规则（如模拟器物理约束），LLM 不一定能识别
- **验证失败**：作者v3说明无法确认的假说会被丢弃、接口保持不变；仍需生产回滚、版本隔离与安全门禁，不能以任务分数替代代码审查。

## v3新增证据与工程边界

本轮回核[ALIGN v3（2026-10-22）](https://arxiv.org/html/2505.21055v3) §4、Appendix C–F；保留主实验条件，不把版本更新当独立复现。

- v3 Appendix D.3审计20个接口的312条注入文本：279条机制级、12条边界级、21条任务相关；后者集中在ScienceWorld（2）与M3ToolEval（19）。作者新增task-agnosticism约束，但已评估接口生成于加约束之前，未报告修订后对应主实验。机制透明、任务提示和答案泄漏需区别验收。
- Table 4：GPT-4.1-mini 28.36→64.93%、GPT-4.1 73.88→93.28%、GiGPO领域模型原训练配置89.55→92.54%。Table7中AutoManual与ALIGN组合在两种被测模型得分最高，但Qwen3-8B单独ALIGN低于AutoManual（47.76 vs52.24），表明两者可互补但相对价值依模型。
- 接口只从训练任务生成、测试冻结。Appendix F.1记录各任务划分，ALFWorld测试使用OOD分区（E.1指出134任务）；ScienceWorld每任务类型最多前5例、WebShop固定50个测试任务、M3ToolEval每类2例训练余下测试。不是独立多次复现或GUI验证。
- **综合判断**：不必所有在线执行都用强模型；可比较离线接口生成、人工实现、Agent-side规则与在线教师的质量/成本/维护开销。论文未做预算匹配的在线教师对照；生成wrapper需审计额外动作、授权、状态语义、隐私和过度引导。

## 关联概念

- [[Agent-Environment-Misalignment]] — ALIGN 解决的问题
- [[Agent-Harness]] — ALIGN 是 harness 内部接口层的自动化实现
- [[ACI-Agent-Computer-Interface]] — ALIGN是ACI自动优化实例
- [[Building-Effective-Agents]] — "Well-crafted ACI"原则的算法化
- [[Agent-Verification]] — ALIGN 的实验验证步骤是 verification 循环的强化版
- *（ALIGN 抽象出的"自动接口生成"作为机制类暂未单独建 entity，与 [[ACI-Agent-Computer-Interface]] 对照阅读即可）*