---
type: entity
title: Agentic Analytics
aliases:
  - Agentic Analytics
  - Agentic Data Analytics
  - 代理式数据分析
definition: "用 LLM/Agent 承担自助数据分析入口，但可靠性来自 canonical datasets、semantic layer、domain skills、评测、provenance 和 correction harvesting 的系统"
created: 2026-06-05
updated: 2026-06-05
tags:
  - data-analytics
  - enterprise-ai
  - context-engineering
related_entities:
  - "[[Context-Engineering]]"
  - "[[Enterprise-AI-Learning-Gap]]"
  - "[[Machine-Readable-Processes]]"
  - "[[Knowledge-Compilation]]"
  - "[[Thin-Harness-Fat-Skills]]"
source_raw:
  - "[[20260603-anthropic-self-service-data-analytics]]"
---

# Agentic Analytics（代理式数据分析）

> [!definition] 定义
> **Agentic Analytics** 是用 LLM/Agent 承担自助数据分析入口的工作系统。它的可靠性不来自“会写 SQL”，而来自 canonical datasets、semantic layer、domain skills、评测、provenance、telemetry 和 correction harvesting 共同组成的分析 harness。

## 核心问题

传统 self-service analytics 常在两个坏选择之间摇摆：

- 做宽表和 dashboard，让更多人能查，但不同团队容易得出不一致口径。
- 把分析环境圈起来，保证质量，但覆盖不了长尾问题，最后 dashboard 泛滥。

Anthropic 的关键判断是：把 Claude 直接接入 data warehouse 会制造“精确错觉”。Analytics 不是普通代码任务，很多问题只有一个正确答案，且无法靠编译器或测试天然证明。真正难点是把自然语言问题映射到正确实体、指标、表、时间窗口、权限和业务语义。

## 系统组件

| 组件 | 作用 | 失败时会发生什么 |
|------|------|------------------|
| Canonical datasets | 降低口径分裂，提供可信入口 | 同一指标多种版本，答案看似精确但实际错 |
| Semantic layer | 让业务指标和数据表有稳定映射 | Agent 自己猜 join、filter 和 metric 定义 |
| Domain skills | 保存过程性业务知识和使用规则 | 模型会写 SQL，但不知道该查什么 |
| Evals | 离线验证 domain 能否上线 | 只能靠主观试用判断可靠性 |
| Provenance footer | 暴露来源、假设和查询证据 | 用户难以发现 silent failure |
| Correction harvesting | 把用户纠错变成 PR 和技能更新 | 系统无法跨过 learning gap |

## 关键数据点

- Anthropic 称 95% business analytics queries 已通过 Claude 自动化，aggregate accuracy 约 95%。
- 没有 skills 时准确率不超过 21%；有 skills 后整体超过 95%，部分 domain 接近 99%。
- 给 agent 访问数千个历史 SQL 文件只带来不到 1 个百分点提升；80% 错误答案的答案已经在 corpus 中，但 agent 没有正确使用。
- Skills 如果不维护，准确率可在一个月内从约 95% 掉到约 65%。
- 约 90% 数据模型 PR 包含 skill 变更，因为 skill markdown 与 transformation 代码 colocate，并由 code-review hook 约束同步更新。
- Adversarial review 可带来约 6% accuracy 提升，但增加 32% token 和 72% latency。

## 与 Context Engineering 的关系

Agentic Analytics 说明 [[Context-Engineering]] 不是“把更多资料塞进上下文”。历史 SQL、文档和仓库访问都可能在上下文里，但如果没有结构化语义、技能路由和评测，它们只是噪声。

更准确的表述是：Context Engineering 要把正确知识放在正确抽象层。

- 原始 SQL corpus 是证据库，不是运行时指导。
- Semantic layer 是指标和实体的稳定入口。
- Skill 是 domain-specific 操作手册。
- Eval 是判断 skill 是否仍然可信的回归测试。

## 前提与局限性

- Anthropic 的做法依赖强数据工程基础，普通企业最容易低估 canonical datasets 和 semantic layer 的建设成本。
- Aggregate accuracy 不能覆盖所有风险，高管指标、财务口径和低频长尾问题仍需更强审查。
- Provenance footer 能降低沉默失败风险，但不能消灭沉默失败。
- Skills 是资产也是负债，必须进入 PR、CI 和 owner 机制，否则会快速腐烂。

## 关联概念

- [[Context-Engineering]] — Agentic Analytics 的核心不是更长上下文，而是结构化上下文。
- [[Enterprise-AI-Learning-Gap]] — Correction harvesting 和 skill PR 是跨过学习鸿沟的机制。
- [[Machine-Readable-Processes]] — 数据定义、指标口径和分析流程必须机器可读。
- [[Knowledge-Compilation]] — Query corpus 需要被蒸馏为 skills，而不是原样丢给 agent。
- [[Thin-Harness-Fat-Skills]] — 分析 domain 的厚知识应沉淀在 skill 层。
