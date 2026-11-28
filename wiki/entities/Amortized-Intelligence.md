---
type: entity
title: Amortized Intelligence
aliases:
  - Amortized Intelligence
  - 分摊智能
  - 摊销智能
definition: "将可复用模型的前置训练、适配和固定成本在实际服务量上分摊；推理、运维、验证与错误处理仍有成本，商业净收益取决于收入和全成本。"
created: 2026-06-20
updated: 2026-11-28
tags:
  - concept
  - economy
evidence_level: medium
claim_type: mixed
related_entities:
  - "[[Sample-Efficiency]]"
  - "[[Allocation-Economy]]"
  - "[[Always-On-Economy]]"
  - "[[Enterprise-AI-Factory]]"
source_raw:
  - "[[20260619-the-data-black-hole-at-the-center-of-ai]]"
---

# Amortized-Intelligence（摊销智能 / 分摊智能）

> [!definition] 定义
> Patel 提出的摊销机制强调前置投资可在多次服务中复用。复制权重的边际开销与运行推理的边际成本不是同一变量；后者受硬件容量、功耗、内存、网络、并发、上下文、工具及重试影响。

## 成本边界与计量

对一个固定期间和同一可验证任务口径，单位完成成本 =（归属本期的训练/适配/固定容量及运维成本 + 实际全部请求、工具、人工复核、返工及失败处理成本）÷ 验收成功任务数。失败、超时与升级成本计入分子；零成功时不可报有限单位成本。固定成本分摊受利用率、模型更新及资产寿命影响，不等同于边际成本或API标价。企业采购方和训练供应商的成本边界不同，避免把已包含于API价的训练费用重复计入。

## 关键数据点

- [Epoch AI 2026-02支出估计](https://epoch.ai/data-insights/company-spending-breakdown) 依据MiniMax/Z.ai上市文件及Anthropic媒体数据估算：MiniMax 2025前三季推理算力3800万美元/收入5300万、Z.ai 2025上半年900万/2700万。口径和时期不同，属于二次归类的会计估算，不是单任务边际成本；Anthropic来自媒体预测，不作审计数据。本轮未直接复核上市文件。
- 旧“微秒级摊销成本”（时间与货币混用）、“6–9数量级边际差”、无限并发及必然高利润均退役；尚无共同任务和全成本分母。
- 人类教育、教材、示范、流程与知识产品也能复用和分摊，个人身体与模型权重的可复制性有差异，但不推出人类知识完全不可摊销。

## 前提与局限性

高频且稳定质量可能帮助固定投入分摊；长尾、低利用率、频繁换代、资源拥塞和高复核成本可能抵消优势。单位平均成本下降不保证增量成本下降、盈利或全社会资源消耗下降。参见 [[Enterprise-AI-Model-Sourcing]]、[[Jevons-Paradox-for-Knowledge-Work]]。不将作者商业预测当事实。

## 关联概念

- [[Sample-Efficiency]] — 样本效率影响训练投入，但与单位服务成本不同。
- [[Allocation-Economy]] — 分摊可能改变资源配置的相对成本，不证明经济结构必然迁移。
- [[Always-On-Economy]] — 连续服务需容量、可靠性、运维和实际需求，不由摊销自动保证。
- [[Enterprise-AI-Factory]] — 智能工厂是生产和持续优化这种可分摊权重资产的物理机构。
