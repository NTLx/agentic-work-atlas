---
type: entity
title: Auto Mode
aliases:
  - 自动模式
  - Claude Code Auto Mode
definition: "Claude Code 的一种自动化权限判定模式，利用模型分类减少逐条人工审批；实际安全性取决于版本、策略、执行边界和评测，不由模式名称保证。"
created: 2026-06-12
updated: 2026-11-28
evidence_level: medium
claim_type: mixed
tags:
  - claude-code
  - agentic-engineering
  - security
related_entities:
  - "[[Claude-Code-CLI]]"
  - "[[Agent-Verification]]"
  - "[[Agent-Loops]]"
source_raw:
  - "[[20260608-reflecting-on-year-of-claude-code]]"
---

> [!definition] 定义
> Auto Mode 是 Claude Code 的自动执行模式。2026-06-08 团队访谈描述将权限请求交给分类器判定并保留拒绝/人工允许路径；本页不是当前版本权限规则的完整说明。

## 关键数据点

- 安全机制: 受访者报告收集数千条完整轨迹与权限请求进行安全分类，未披露样本构成、训练/测试划分或准确率。
- 红队测试: 受访者报告红队与内部攻击测试被用于构造 eval 并改善分类；未说明红队独立性或普遍阻断保证。
- 内部验证: Anthropic 内部团队尝试攻击 auto mode → 持续改进
- Boris 描述个人从 plan mode 转向 auto mode；规划需要和权限判定是不同维度。
- 受访者认为减少重复审批可缓解注意力疲劳；99% 是访谈中的表达，不是对照事故率。

## 前提与局限性

- **依赖模型对齐**: 需要模型足够 aligned 才能判断安全边界
- **自我评估偏差**: Anthropic 自己训练分类器评估自己的产品，存在 self-serving bias
- **无独立审计**: 来源没有提供可核实的独立第三方对照审计结果；不能由此断言从未有外部评估。
- **模型版本依赖**: 不同模型版本（Opus 4 vs 4.7）的 auto mode 行为可能不同

## 关联概念

- [[Claude-Code-CLI]] — Auto mode 是 Claude Code 的核心功能
- [[Agent-Verification]] — 自动权限判定可减少等待，但不提供独立验证保证
- [[Agent-Loops]] — 自动判定可支持某些循环，不是持续执行的充分必要条件
