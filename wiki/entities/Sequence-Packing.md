---
type: entity
title: Sequence Packing
aliases:
  - 序列打包
definition: "一种 LLM 训练优化技术，将多条短序列拼接成单个固定长度序列，消除填充开销，大幅减少前向传播次数，提升 GPU 利用率和训练吞吐量。"
created: 2026-05-10
updated: 2026-05-10
tags:
  - LLM-Training
  - Performance-Optimization
  - AMD
related_entities:
  - "[[Dual-Tier-LLM-Architecture]]"
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

## 前提与局限性

- **前提**: 需要训练框架支持（SFTConfig 的 packing 参数）
- **前提**: 样本长度差异较大时效果更显著；等长样本的收益较小
- **局限性**: 打包后不同样本之间可能存在注意力泄漏（attention leakage），需要框架正确处理
- **局限性**: 与 QLoRA 等其他优化技术配合时需要调试兼容性

## 关联概念

- [[Dual-Tier-LLM-Architecture]] — 序列打包使双层模型的快速微调成为可能
