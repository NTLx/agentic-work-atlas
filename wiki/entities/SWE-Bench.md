---
type: entity
title: SWE-Bench
aliases:
  - SWE-Bench
  - SWE-bench
  - Software Engineering Benchmark
definition: "给定真实 GitHub issue 及对应代码库，评估模型或 Agent 提交的补丁能否通过指定测试并解决问题的一组软件工程基准；主要指标是解决率而非修复耗时。"
created: 2026-06-06
updated: 2026-11-28
evidence_level: medium
claim_type: mixed
tags:
  - benchmark
  - software-engineering
  - AI-evaluation
related_entities:
  - "[[CORE-Bench]]"
  - "[[Task-Horizon]]"
  - "[[Coding-Agents]]"
  - "[[Agentic-Engineering]]"
  - "[[Evaluation-Integrity]]"
source_raw:
  - "[[20260604-anthropic-recursive-self-improvement]]"
  - "[[20260708-openai-swe-bench-pro-audit]]"
---

# SWE-Bench

> [!definition] 定义
> SWE-bench 评估根据真实软件 issue 生成能够解决问题的代码补丁的能力。官方 FAQ 描述在仓库环境应用补丁并运行测试，统计已解决任务；不是以修复速度为核心的基准。

## 关键数据点

### 版本与测量合同

- [官方 FAQ](https://www.swebench.com/SWE-bench/faq/) 列出原始集合2294项、Lite 300项、Verified 500项，另有 Multimodal、Multilingual。定义勘误依据，待正式晋升为一手来源记录。
- 不同版本、任务子集、harness、模型版本、工具权限、预算与重复次数不能混用。报告解决率时说明分母与无效运行处理。测试通过也不保证真实 issue 的所有隐含要求、代码可维护性和生产可部署性。
- 2026-06 Anthropic 报告概括约两年从低个位数到饱和，未在本页确认具体可比序列和饱和阈值。撤回“饱和=独立完成任意 issue”及“CORE-Bench 饱和更快证明推理进步更快”的推论。

## 前提与局限性

### 已有反证与评估治理

- [[20260708-openai-swe-bench-pro-audit]]：Pro 审计先从731题中筛出286题，agent/human 分别报告200/249项 breaking tasks；人审和机器审计不等价，审计针对筛选后的子集，不是未见全部题目的无偏估计。Pro 的问题不能直接当作 Verified 的统计结果。
- OpenAI 对 Verified 的[独立文章](https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/) 提出测试缺陷与污染风险；本轮仅作证据定位和复核候选，未重跑评测或将审计子集比例推广到全库。
- 选择基准应考虑真实任务代表性、污染、评分合同与误差；与 [[Task-Horizon]] 的关系是互补，不是同一测量。

## 关联概念

- [[CORE-Bench]] — 科学计算复现基准
- [[Task-Horizon]] — 任务视野估计
- [[Evaluation-Integrity]] — 基准本身的证据质量
- [[Coding-Agents]] — 评测对象
- [[Agentic-Engineering]] — 软件交付与验证
