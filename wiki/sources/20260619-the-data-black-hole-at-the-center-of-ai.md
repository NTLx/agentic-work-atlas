---
type: source-summary
title: "The data black hole at the center of AI"
source_raw:
  - "[[20260619-the-data-black-hole-at-the-center-of-ai]]"
created: 2026-06-20
updated: 2026-11-28
tags:
  - source-summary
  - AI-scaling
  - economy
evidence_level: medium
claim_type: mixed
---

# The data black hole at the center of AI

## 编译摘要

### 1. 浓缩与证据身份

Patel（2026-06-19）提出三项相互关联的观点：人类与模型的样本效率可能不同、数据及计算可能是能力增长的重要杠杆、训练资产可跨服务复用。原文是分析文章，不是同任务对照试验、实验室训练数据审计或利润研究。

- **样本效率**：原文假设人类成年前约2亿语言token、前沿训练10T–100T token，算术比5万–50万；感官数据、先验、任务目标、重复及胜任阈值不同，不能定为普适样本效率差。驾驶小时与车队里程、基因组字节与参数数目不可直接比较。
- **缩放拟合**：[Hoffmann 2022](https://arxiv.org/html/2203.15556) §3.3 Eq.2允许对给定目标loss求数据需求的条件极限；比例依赖起始参数、目标loss和拟合参数，不支持10倍普适上限。详见 [[Sample-Efficiency]]。
- **开放权重差距**：[Epoch 2026-05-29](https://epoch.ai/data-insights/open-closed-eci-gap) 2026-01-01至05-28的ECI平均差4个月；严格点估计超过则6个月，8分（90% CI 7–11）。作者推测API蒸馏解释追赶，不是该研究的因果结果；不得认定实验室实际训练来源或低至1%的成本。详见 [[API-Distillation-Catch-Up]]。
- **摊销**：原文论证前置学习成本可跨数十亿会话分摊；未测单任务推理零成本、无限并发或必然净利润。区分权重复制、训练、推理、容量、复核与失败开销，见 [[Amortized-Intelligence]]。

### 2. 质疑

数据、算法、架构、训练规模、后训练、推理预算与评测均可能影响进步。不能由公开分数逆推训练贡献。领域泛化、长尾与成本分摊需独立验证；人类知识也可通过教学及知识产品复用，不等同可直接复制个体。服务条款及许可要按产品与用途核验。

### 3. 对标

这些问题分别属于样本效率、蒸馏、模型经济及企业采购；原文对就业与AGI的预测保留为历史作者观点，不晋升为事实。撤回百万倍、10倍、零边际成本及由追赶推唯一主因等旧强论断。外部原始分析仅作本次校准，正式晋升走既有Weekly门。

### 关联概念

- [[Sample-Efficiency]]
- [[Amortized-Intelligence]]
- [[API-Distillation-Catch-Up]]
- [[World-Model]]
- [[AI-Era-Economy-Shift]]
- [[Allocation-Economy]]
- [[AI-Labor-Bottleneck-Shift]]
- [[Enterprise-AI-Model-Sourcing]]
