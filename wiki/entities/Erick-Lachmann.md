---
type: entity
title: Erick Lachmann
aliases:
  - Erick Lachmann
definition: "Dharma-AI 研究员，专门化小模型与企业 AI 采购变量的研究者"
validated_source: "https://huggingface.co/blog/Dharma-AI/specialization-beats-scale"
validated_at: 2026-05-24
created: 2026-05-24
updated: 2026-05-27
tags:
  - person
  - AI
  - enterprise-AI
related_entities:
  - "[[Specialized-Small-Models]]"
  - "[[Distributional-Alignment]]"
  - "[[Specialization-Compounds]]"
  - "[[Enterprise-AI-Model-Sourcing]]"
  - "[[Layered-AI-Sourcing]]"
source_raw:
  - "[[Specialization Beats Scale A Strategic Variable Most AI Procurement Decisions Overlook]]"
---

# Erick Lachmann

> [!definition] 定义
> **Erick Lachmann** 是 Dharma-AI 研究员，专注于专门化小模型与企业 AI 采购变量的研究，提出"训练历史与任务分布必须成为采购变量"的核心洞察

## 可验证履历

| 时间 | 角色 | 组织 |
|------|------|------|
| 2024-至今 | 研究员 | Dharma-AI（专注企业 OCR 与文档理解） |
| 2026-05 | 一作发表 | "Specialization Beats Scale" HuggingFace 博客 |

**研究领域**：专门化小模型、分布对齐、企业 AI 采购策略
**验证来源**：[HuggingFace 博客](https://huggingface.co/blog/Dharma-AI/specialization-beats-scale)

## 核心观点

### 专门化胜过规模

Lachmann 在 [[Specialization Beats Scale A Strategic Variable Most AI Procurement Decisions Overlook]] 中提出，企业 AI 采购的核心变量不是参数规模，而是训练历史与部署任务之间的 [[Distributional-Alignment|分布对齐]]：

- **实验证据**：专门化 3B 模型在巴西葡萄牙语 OCR benchmark 中 composite score 为 0.911，高于 Claude Opus 4.6 的 0.833，且每百万页推理成本约低 52 倍
- **关键机制**：同样训练流程下，已具备 OCR 专门化起点的 Nanonets-OCR2-3B 达到 0.921 与 0.20% degeneration；通用 Qwen2.5-VL-3B 仅达到 0.793 与 1.41% degeneration
- **层级累积**：专门化是层级式累积过程，从 generalist 到 general-domain specialist 再到 domain-specific specialist

### 采购范式转变

Lachmann 的研究改变了企业 AI 采购的核心问题：

| 旧范式 | 新范式 |
|--------|--------|
| "买最大模型" | "按任务组合模型来源" |
| benchmark leadership 代表企业场景 | 真实工作负载上的分布对齐测试 |
| 参数规模是唯一变量 | 训练历史与任务分布是关键变量 |

### 专门化复利

如果企业把真实任务数据、评测集和失败模式持续回流，[[Specialization-Compounds|专门化]] 可以成为内部版 [[Deployment-Product-Flywheel|部署产品飞轮]]。反之，若评测集留在供应商手中，企业只是在为别人的专门化飞轮供料。

## 关联概念
| 本库主题 | Lachmann 的贡献 |
|---------|----------------|
| [[Specialized-Small-Models]] | 提供专门化小模型胜过大型 API 的实验证据 |
| [[Distributional-Alignment]] | 把分布对齐定义为企业 AI 采购的核心变量 |
| [[Specialization-Compounds]] | 展示专门化如何通过层级累积产生复利 |
| [[Enterprise-AI-Model-Sourcing]] | 改变企业模型采购的核心问题 |
| [[Layered-AI-Sourcing]] | 支撑分层采购策略的实证基础 |
| [[Evaluation-Set]] | 强调评测集产权对专门化复利的关键作用 |
| [[Verifiability]] | OCR 任务因可验证才能暴露专门化收益 |
| [[Hardware-Sovereignty]] | 专门化小模型降低本地部署门槛 |

## 研究边界

Lachmann 明确限定其结论只覆盖：
- OCR 任务
- 葡萄牙语文档
- 论文 benchmark

**不能直接外推**到：开放式推理、创意任务、复杂战略判断。

## 外部链接

- [HuggingFace 博客](https://huggingface.co/blog/Dharma-AI/specialization-beats-scale)
