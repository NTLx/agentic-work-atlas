---
type: entity
title: Sequence Packing
aliases:
  - 序列打包
definition: "把多条短训练样本拼接进固定长度上下文以减少 padding 浪费的 LLM 训练优化技术"
created: 2026-05-10
updated: 2026-06-16
evidence_level: medium
claim_type: mixed
tags:
  - training
  - AMD
related_entities:
  - "[[Dual-Tier-LLM-Architecture]]"
  - "[[Hardware-Sovereignty]]"
  - "[[Specialized-Small-Models]]"
  - "[[Enterprise-AI-Model-Sourcing]]"
  - "[[Verifiable-Agent-Engineering]]"
source_raw:
  - "[[OncoAgent A Dual-Tier Multi-Agent Framework for Privacy-Preserving Oncology Clinical Decision Support]]"
---

> [!definition] 定义
> 序列打包是 LLM 监督微调中的训练优化技术：通过 `packing=True` 配置将多条短训练样本拼接成单个固定长度序列（如 2048 tokens），消除传统填充（padding）带来的计算浪费，大幅减少前向传播次数，显著提升 GPU 利用率和训练吞吐量。

## 关键数据点

- **OncoAgent 实践**: 在 AMD MI300X 上实现 266,854 样本全量微调约 50 分钟（原预估 5 小时），约 6 倍训练时间压缩
- **GPU 利用率**: 峰值 ~70%，稳定吞吐量 ~11.3 s/iteration
- **配置**: `SFTConfig(packing=True, max_seq_length=2048)`
- **合成数据加速**: 从 ~120 cases/hr 提升至 ~6,800 cases/hr（56 倍）
- **VRAM 使用**: Unsloth 优化后 ~64 GB / 192 GB（约 60% 峰值 VRAM 降低）
- **适用训练**: 常见于 SFT、instruction tuning、领域微调和小模型专门化训练
- **工程位置**: 属于训练管线优化，不直接提升模型能力，但显著降低获得专门化模型的时间和硬件成本

## 为什么它值得保留为 Entity

Sequence Packing 看起来像局部训练参数，但在本库主题下有更大的结构意义：它降低了“企业自己训练或微调专门模型”的门槛。

在 OncoAgent 案例中，真正的部署能力不是单一模型，而是本地硬件、双层模型、RAG、隐私前置和安全验证组成的系统。Sequence Packing 与 Unsloth、QLoRA、MI300X 一起，让 266,854 个肿瘤病例训练不再是遥远的大厂工程，而变成单卡可执行的本地实验。

这直接连接两条主线：

- 对 [[Hardware-Sovereignty]] 来说，它降低本地训练的成本和等待时间。
- 对 [[Enterprise-AI-Model-Sourcing]] 来说，它让企业更有机会测试专门化小模型，而不是默认采购 frontier API。
- 对 [[Dual-Tier-LLM-Architecture]] 来说，它使多个层级的模型可以更快迭代和重训。

## 前提与局限性

- **前提**: 需要训练框架支持（SFTConfig 的 packing 参数）
- **前提**: 样本长度差异较大时效果更显著；等长样本的收益较小
- **局限性**: 打包后不同样本之间可能存在注意力泄漏（attention leakage），需要框架正确处理
- **局限性**: 与 QLoRA 等其他优化技术配合时需要调试兼容性
- **局限性**: 它优化的是吞吐和显存，不会弥补训练数据质量、标签噪声、评测缺失或任务定义错误
- **局限性**: 如果框架没有正确隔离样本边界，模型可能学习到跨样本伪关联，反而损害微调质量
- **局限性**: 训练速度提升可能诱导团队过度依赖合成数据扩张，而忽视临床或业务专家验证

## 关联概念

- [[Dual-Tier-LLM-Architecture]] — 序列打包使双层模型的快速微调成为可能
- [[Hardware-Sovereignty]] — 本地训练可行性依赖吞吐、显存和成本优化
- [[Specialized-Small-Models]] — 专门化小模型需要低成本、可重复的微调流程
- [[Enterprise-AI-Model-Sourcing]] — 企业模型采购应考虑内部微调和部署能力
- [[Verifiable-Agent-Engineering]] — 训练优化必须和评测集、验证闭环一起看，不能只看速度
