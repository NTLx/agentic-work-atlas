---
type: source-summary
title: "Frontier Models with Our Harness Achieve ~99% on ARC-AGI-3 Public — Schema"
source_raw:
  - "[[20260717-schema-harness-arc-agi]]"
created: 2026-07-27
updated: 2026-07-27
tags:
  - source-summary
  - agent-harness
  - benchmark
  - AGI
  - agentic-engineering
evidence_level: medium
claim_type: extracted
---

# Frontier Models with Our Harness Achieve ~99% on ARC-AGI-3 Public — Schema

> Schema harness 在不修改模型权重的前提下，通过 Two-Level Joint Reasoning 架构将前沿模型在 ARC-AGI-3 Public 上的表现从 ~7% 提升至 ~99%（~14× 提升）。来源: Schema Team 官方页面，证据等级: medium（仅 Public set 结果，Semi-private 未报告）。

## 编译摘要

### 1. 浓缩
- **核心结论1**: Harness 设计可产生数量级性能飞跃——Schema 不改变模型权重，仅改变模型周围的推理过程（观察→建模→预测→修正），即实现 ~14× 效率提升
  - 关键证据: Claude Opus 4.8 + Fable 5 达 ~99% RHAE（Public），GPT-5.6 Sol 达 95.35%；同期无 harness 的 GPT-5.6 Sol 在 Semi-private set 仅 7.78%
- **核心结论2**: Two-Level Joint Reasoning（State Grounding + Mechanism Discovery 联合求解）是关键架构创新——状态表示与转移规则编码在同一可编辑程序中，观察矛盾时同时修正两者
  - 关键证据: 先前系统 VIGA（仅 Level 1）和 WorldCoder（仅 Level 2）分别解决子问题；Schema 证明两者不可独立解决——错误的状态表示会导致无法找到一致的转移规则
- **核心结论3**: ARC-AGI-3 的任务设计（无物体清单、规则表、目标陈述或奖励塑形的 64×64 网格环境）测试的是从零开始的环境建模能力
  - 关键证据: RHAE 指标以首次接触人类基线为参照，衡量动作效率而非仅完成率

### 2. 质疑
- **关于 ~99% 成绩的质疑**: 仅在 Public set 上达到 ~99%，Semi-private 成绩未披露。ARC-AGI 历史表明 Public/Semi-private 之间差距显著（7.78% 是无 harness Semi-private 成绩，但 Schema 的 Semi-private 成绩缺失），可能存在对 Public set 的过拟合风险
- **关于\"不修改权重\"主张的质疑**: Schema 依赖 Claude Opus 4.8、Fable 5 等前沿模型的极强基础能力——harness 放大了模型能力但并非模型无关；GPT-5.6 Sol（95.35%）与 Opus 4.8（~99%）的差异暗示模型选择仍然重要
- **关于 ~14× 提升的质疑**: 14× 的比较基线是"同模型无 harness"，但未说明基线是零 harness 还是简单 prompt。基线定义对倍率声明的可信度至关重要

### 3. 对标
- **跨域关联1**: Schema 的"不改权重只改过程"与 [[Agent-Harness]] 的核心命题一致——**Agent = Model + Harness**，Schema 是该命题在 AGI benchmark 上的极端验证案例
- **跨域关联2**: Two-Level Joint Reasoning 的"状态与规则联合编辑"与 [[World-Model|世界模型]] 概念深度对应——Schema 本质是在构建一个可程序化修正的 world model，而非仅做 pattern matching
- **跨域关联3**: Schema 的迭代修正循环（观察→预测→矛盾→联合修正）是 [[Agent-Loops]] 中 Observe-Orient-Decide-Act 模式的具体实例，但增加了"修正表示本身"的元层能力

### 关联概念
- [[Agent-Harness]]
- [[Harness-Engineering]]
- [[World-Model]]
- [[Agent-Loops]]
- [[Continual-Learning]]
