---
type: source-summary
title: "OpenAI LifeSciBench: 750 任务生命科学 Benchmark"
source_raw:
  - "[[20260617-openai-lifescibench]]"
created: 2026-06-18
updated: 2026-06-18
tags:
  - source-summary
  - benchmark
  - evaluation
evidence_level: high
claim_type: mixed
---

# OpenAI LifeSciBench: 750 任务生命科学 Benchmark

## 编译摘要

### 1. 浓缩
- **核心结论1**: LifeSciBench 是首个基于真实生命科学研究工作流的 benchmark——750 任务、7 工作流、7 生物领域、19020 个评分标准
  - 关键证据: 173 名 PhD 科学家编写；79% 任务需要多步推理（平均 4 步）；1062 个附件；453 名评审一致性超 96%
- **核心结论2**: GPT-Rosalind 以 36.1% 通过率领先，但远未饱和——22.8% 的任务无模型通过，34.8% 的任务最佳通过率低于 20%
  - 关键证据: Scientific Communication 71.1%、Translation 57.7% 表现最强；Design 30.7%、Analysis 30.3% 仍困难；artifact 使用是瓶颈（45.1%→28.1%）
- **核心结论3**: 精确输出（序列/结构/数值）是最大短板——GPT-Rosalind 数值任务仅 14.8%，序列/结构仅 24.0%
  - 关键证据: 14% 的任务获得部分分数但未通过 70% 阈值；模型常"走到一半"但缺少关键约束或计算

### 2. 质疑
- **关于"GPT-Rosalind 领先"**: OpenAI 自建 benchmark 且评估自家模型，独立性存疑；但 453 名外部评审的一致性（96%+）提供了部分制衡
- **关于"远未饱和"的解读**: 750 任务可能不代表所有生命科学领域；benchmark 的领域覆盖偏差可能影响"饱和度"判断
- **关于 artifact 使用瓶颈**: 模型在处理复杂图形、大型序列文件时的失败可能反映的是多模态能力不足而非科学推理不足

### 3. 对标
- **Evaluation-Set**: LifeSciBench 是 [[Evaluation-Set]] 概念在生命科学领域的实例——专家编写的标准比自动生成更可靠
- **Research-Taste**: "79% 任务需要多步推理"与 [[Research-Taste]] 中研究判断能力的评估方向一致，但 LifeSciBench 更侧重领域知识而非方向选择
- **Scientific-Discovery-AI**: LifeSciBench 评估的是 [[Scientific-Discovery-AI]] 的下游工具能力——模型能否辅助而非替代科学家
- **Dominator-Analysis**: 验证器设计（19020 标准、70% 通过阈值）与 LangChain Legal Verifiers 中的验证策略形成跨领域对照

### 关联概念
- [[Evaluation-Set]]
- [[Research-Taste]]
- [[Scientific-Discovery-AI]]
- [[Dominator-Analysis]]
