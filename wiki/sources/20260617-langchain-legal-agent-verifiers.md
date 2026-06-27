---
type: source-summary
title: "Designing Efficient Verifiers for Legal Agents"
source_raw:
  - "[[20260617-langchain-legal-agent-verifiers]]"
created: 2026-06-17
updated: 2026-06-17
tags:
  - source-summary
  - agentic-engineering
  - verification
  - evaluation
evidence_level: high
claim_type: mixed
---

# Designing Efficient Verifiers for Legal Agents

## 编译摘要

### 1. 浓缩
- **核心结论1**: 验证器成本是 agent 评估和 RL 后训练的瓶颈；批处理验证和开源模型可降低一个数量级成本
  - 关键证据: 40 个 LAB 法律任务、2348 个标准验证；批处理比逐条验证便宜一个数量级（节省重复输入 token）；DeepSeek 比前沿模型便宜 3 个数量级
- **核心结论2**: 前沿模型之间也存在分歧（Opus 与 GPT-5.5 仅 95.7% 一致），100% 匹配率不现实
  - 关键证据: Opus/GPT-5.5/Sonnet 之间约 4-5% 标签不一致；Haiku 误通过率 48.4%（逐条）/34.7%（批处理），法律验证中属于错误失败模式
- **核心结论3**: 针对性提示调优可进一步优化验证器行为；开源模型允许微调定制验证器
  - 关键证据: DeepSeek 通过提示调优将误通过率从 10.7%→9.5%（逐条）、15.6%→14.2%（批处理）；trace 挖掘和行为蒸馏是有效策略

### 2. 质疑
- **关于"以 Opus 为基准"的质疑**: 以 Opus per-criterion 作为 ground truth 基准，但 Opus 本身与 GPT-5.5 仅 95.7% 一致；基准本身的不确定性会影响结论可靠性
- **关于"法律领域可推广性"的质疑**: 实验在 40 个法律任务上进行，法律验证的严格性是否适用于其他高风险领域（医疗、金融）尚不确定
- **关于"成本外推"的质疑**: 60-1000x 成本节约是外推估计，实际 RL 后训练中的验证成本受 rollout 数量、任务复杂度等因素影响

### 3. 对标
- **Verifiable-Agent-Engineering**: 本文为 [[Verifiable-Agent-Engineering]] 提供具体工程实践——验证器设计是可验证 agent 系统的核心组件
- **Dominator-Analysis**: 批处理 vs 逐条验证的权衡类似于 [[Dominator-Analysis]] 中验证粒度与成本的平衡
- **Evaluation-Set**: 法律 LAB benchmark 是 [[Evaluation-Set]] 概念在垂直领域的实例化
- **Open-Source-Operational-AI-Framework**: 开源模型作为验证器的策略与 [[Open-Source-Operational-AI-Framework]] 中开源运营部署框架一致

### 关联概念
- [[Verifiable-Agent-Engineering]]
- [[Dominator-Analysis]]
- [[Evaluation-Set]]
- [[Open-Source-Operational-AI-Framework]]
