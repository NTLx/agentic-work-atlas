---
type: source-summary
title: "开源权重模型如何改变 AI 版图"
source_raw:
  - "[[20260617-bytebytego-open-weight-models]]"
created: 2026-06-22
updated: 2026-06-22
tags:
  - source-summary
  - open-weight
  - MoE
  - model-architecture
  - ai-ecosystem
evidence_level: medium
claim_type: extracted
---

# 开源权重模型如何改变 AI 版图

## 编译摘要

### 1. 浓缩

- **核心结论1**: 开源模型通过"Borrow-and-Build"模式快速追赶——每个团队学习前人创新并贡献新创新
  - 关键证据: DeepSeek V3 → Moonshot Kimi K2 → Zhipu GLM-5 演进链；每家公司基于前一家的公开权重和技术报告进行创新
- **核心结论2**: 架构正在收敛（MoE），差异在训练方法——注意力策略、专家数量、后训练方法
  - 关键证据: 所有主要开源 LLM（DeepSeek、Kimi、Qwen、Llama、GLM）都使用 MoE 架构；差异在 GQA/MLA/Sparse Attention、16-384 专家数量、RL/蒸馏/合成数据
- **核心结论3**: "活跃参数"比"总参数"更重要——决定推理成本的是每词激活的参数量
  - 关键证据: DeepSeek V3（671B 总/37B 活跃）、Kimi K2（1T 总/32B 活跃）、Qwen3（235B 总/22B 活跃）——活跃参数相近时成本相近

### 2. 质疑

- **关于"Borrow-and-Build 模式"的质疑**: 开源团队学习前人创新，但闭源团队的创新是私有的。这意味着开源模型只能追赶已公开的创新，而闭源模型可能已经在下一轮创新上领先
- **关于"架构收敛"的质疑**: 架构收敛可能意味着创新空间缩小——当所有人都用 MoE 时，差异化只能来自训练方法和数据质量。这可能导致"数据战争"而不是"架构战争"
- **关于"活跃参数"的质疑**: 活跃参数决定推理成本，但总参数决定知识容量。对于需要大量知识的任务（如法律、医疗），总参数可能更重要

### 3. 对标

- **跨域关联1**: 与 [[Closed-Frontier-Models-vs-Open-Model-Economy]] 的关联——开源模型的追赶速度可能改变对比结论
- **跨域关联2**: 与 [[Agentic-Engineering]] 的关联——开源模型的企业部署需要考虑工具生态、安全框架和运维能力
- **跨域关联3**: 与 [[AI-Ready-Organization]] 的关联——企业选择开源模型需要组织具备相应的技术能力和运维能力

### 关联概念

- [[Closed-Frontier-Models-vs-Open-Model-Economy]]
- [[Agentic-Engineering]]
- [[AI-Ready-Organization]]
- [[Enterprise-AI-Model-Sourcing]]
