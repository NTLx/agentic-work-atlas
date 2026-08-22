---
type: entity
title: EnvRigger
aliases:
  - Env Rigger
  - Environment Rigger
definition: "EnvHarness 的自动化 customization 流程——四阶段循环（Observe / Diagnose / Write / Validate），把目标 policy 当 black box，从 trajectory 诊断行为弱点，迭代合成并验证 EnvHarness components；接受自然语言 user-defined constraints 把领域知识直接注入训练信号"
created: 2026-08-22
updated: 2026-08-22
evidence_level: high
claim_type: mixed
tags:
  - agent-harness
  - environment
  - automation
  - rl
  - paper
related_entities:
  - "[[EnvHarness]]"
  - "[[Agent-Harness]]"
  - "[[Lessons-MD-Self-Improvement]]"
  - "[[Self-Evolving-Agent]]"
  - "[[Loop-Engineering]]"
  - "[[ReasoningBank]]"
  - "[[Verification-Tether]]"
source_raw:
  - "[[2608.19880-envharness-agent-learning]]"
---

# EnvRigger

> [!definition] 定义
> **EnvRigger**（arXiv:2608.19880，2026-08-20）是 [[EnvHarness]] 的自动化 customization 流程——四阶段循环（**Observe** / **Diagnose** / **Write** / **Validate**），把目标 policy 当 black box，从 trajectory 诊断行为弱点，迭代合成并验证 EnvHarness components。接受自然语言 user-defined constraints，可把领域知识直接注入训练信号。

## 关键数据点

- **论文**：EnvHarness 同篇（arXiv:2608.19880v1）
- **任务设定**：给定 base 环境 `E` + 目标 policy `π`，自动生成 modified 环境 `E' = H(E, t; π)` 适配特定 task `t`，暴露 `π` 弱点促进改进
- **policy-agnostic 约束**：单个 EnvHarness component 可应用到任何 policy；但选择 + 参数化组件必须 condition on 任务和 policy 行为
- **核心 map**：`H(E, t; π) = (w_k ∘ ... ∘ w_1)(E)`——多组件嵌套，每个针对诊断出的特定弱点
- **user-defined 约束**：自然语言（如「阻止未跑测试的 patch」）可注入 → 自动生成 Contract 强制 policy 验证 fix

## 四阶段流程

```
Observe → Diagnose → Write → Validate (Write-and-Validate loop)
```

### Observe

在当前环境跑 `π`，收集 successes + failures 轨迹。

- **failures** 暴露要解决的特定弱点
- **successes** 定义能力边界——避免 EnvHarness 教 agent 已经会的东西

### Diagnose

分析轨迹，输出 **textual diagnosis**——既描述弱点（policy 过度依赖的 shortcut、verbose observation 处理失败等），也描述当前能力边界。

如果失败太少（agent 已饱和）→ EnvRigger 输出「environment too easy, increase challenge」类诊断，触发 Stage 增加障碍。

### Write

基于 diagnosis，合成一个或多个 EnvHarness components。

- 单个弱点可能需要**组合**（Stage 改 initial + Contract 改后续交互）
- 候选 set 作为整体评估

### Validate

在 `E'` 上跑 fresh rollouts of `π` on base task `t`。按 trajectory metrics（success rate, failure distribution）三选一：

| 决策 | 条件 | 后续动作 |
|------|------|----------|
| **Accept** | 信号合适 | 提交组件 |
| **Reject** | 不可解或无挑战 | 直接丢弃 |
| **Refine** | 信号尺度不当 | 携 trajectory + 反馈回到 Write 阶段 |

**重复 EnvRigger loop** → agent 与环境**持续共同进化**（co-evolution），性能 compounding gains 随定制任务数 scaling。

## 与知识库既有概念的对接

- **[[Lessons-MD-Self-Improvement]]** — 同构机制：两者都从 trajectory 反推改进信号。Lessons-MD 沉淀为 markdown（agent 侧），EnvRigger 沉淀为 EnvHarness components（环境侧）
- **Self-Evolving-Agent** — 本文是 environment 维度 self-evolution 的具体化（待建 entity）。Fang 2025 综述列出 self-evolution 的多个分支：prompt / skill library / memory / weights / harness，**本文是 environment**
- **[[Agent-Loops]]** — Observe/Diagnose/Write/Validate 是经典 loop engineering
- **[[Agent-Verification]]** — Validate 阶段用 fresh rollouts 验证，与「独立验证」原则同构

## 关键设计原则

1. **Black-box policy treatment**：不 inspect 模型权重，只看 outputs → 跨模型家族/强度可用
2. **Standard interface (reset/step)**：跨 benchmark 同一方法
3. **Verifiability preserved**：所有 EnvHarness intervention 在接口层，verifier 不动
4. **Iterative Write-and-Validate**：失败候选自动 refine，不靠人工调参
5. **User-defined constraint injection**：自然语言 → 代码级 Contract

## 前提与局限性

- **Chain 组件被显式排除在自动化 pipeline 外**（"difficult for EnvRigger to observe internal states of joined environments"）
- **Diagnose 阶段依赖强 LLM 推理**——对弱 LLM policy 的诊断质量未量化
- **依赖 deterministic reset**——Stochastic 环境下 Stage 组件可重现性未验证
- **「policy-agnostic 组件」与「policy-conditioned 选择」的张力**——同一组件对不同 policy 效果可能差异大，需要持续 re-diagnose
- **compute 开销**未量化——四阶段循环 + fresh rollouts 的总成本 vs 收益

## 关联概念

- [[EnvHarness]] — 自动化 customization 的对象
- [[Agent-Harness]] — 对称的 agent-side customization
- [[Lessons-MD-Self-Improvement]] — trajectory → improvement 的同构机制
- Self-Evolving-Agent — environment 维度 self-evolution（待建 entity）
- [[Agent-Loops]] — 四阶段 loop 工程
- ReasoningBank — 论文中 skill extraction 的具体方法（论文引用，非知识库 entity）
- [[Agent-Verification]] — Validate 阶段的独立验证原则
- [[Forward-Deployed-Engineer|FDE]] — user-defined natural language constraint 对应「懂问题的人定制工具」
