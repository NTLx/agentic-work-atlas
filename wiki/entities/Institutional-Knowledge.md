---
title: "Institutional Knowledge"
created: 2026-06-27
updated: 2026-06-27
tags:
aliases:
  - 制度性知识
  - 组织知识
  - Tacit Knowledge
definition: "Organizational knowledge accumulated over long-term operations, embedded in people's experience and team processes—difficult to document, difficult to automate, and lost when personnel leave."
source_raw:
  - "[[20260625-ford-ai-quality-jd-power]]"
evidence_level: medium
claim_type: mixed
---

# Institutional Knowledge

组织在长期运营中积累的、嵌入人员和流程中的隐性知识——难以文档化、难以自动化、人员流失即知识流失。

## 核心特征

1. **嵌入性**: 知识存在于工程师的经验判断、团队的协作模式、组织的决策惯例中，而非文档或数据库中
2. **不可完全转移**: 文字化、系统化只能捕获一部分；剩余部分依赖人际传递（师徒制、轮岗、复盘）
3. **AI 放大器效应**: AI 系统的有效性取决于训练数据质量，而训练数据质量取决于制度性知识的完整性

## AI 时代的制度性知识困境

> "Mistakenly, we thought that by just introducing artificial intelligence and adjusting the design requirements that we had, that that would produce a high-quality product."
> — Charles Poon, Ford VP of vehicle hardware engineering

Ford 案例（→ [[20260625-ford-ai-quality-jd-power]]）揭示了一个递归困境：
- AI 需要制度性知识来训练
- 制度性知识在专家离职前未完成转移
- AI 系统因此产生质量缺陷
- 修复缺陷需要找回已离职的专家

这与软件工程的 "Bus Factor" 问题同构——关键知识集中在少数人手中，人员流失导致系统不可维护。

## 关键数据点

- **Ford AI 质量案例** (2026): JD Power 报告显示搭载 AI 辅助设计工具的 Ford 新车在品质排名上显著下滑，直接触发 VP Charles Poon 公开承认"错误地认为引入 AI 即可保证产品质量"
- **Bus Factor 同构性**: 与软件工程中的 Bus Factor 问题同构——当关键知识仅存于少数人的经验判断中时，任何一人离职都会导致系统性风险
- **递归困境**: AI 需要制度性知识来训练 → 制度性知识在专家离职前未完成转移 → AI 系统产生质量缺陷 → 修复缺陷需要找回已离职的专家

## 前提与局限性

- **可迁移性假设有限**: 该概念假设部分制度性知识可以通过师徒制、轮岗、复盘等方式转移，但转移效率高度依赖于组织文化和时间投入
- **AI 并非万能解药**: 引入 AI 本身不能解决制度性知识丢失问题——AI 只是制度性知识的放大器，其输出质量受限于输入数据的完整性
- **不适用于所有知识类型**: 该概念聚焦隐性、情境化的知识，显性事实性知识（如操作手册、API 文档）不在此列
- **规模边界**: 小团队中制度性知识可通过面对面交流自然共享；随着组织规模扩大，隐性知识碎片化加速，管理成本呈指数增长

## 关联概念

- [[AI-Capability-Gap]] — AI 的能力边界部分取决于制度性知识的完整性；制度性知识缺失会导致 AI 能力 gap 扩大
- [[Judgment]] — 制度性知识的核心是判断力，难以编码为规则或模型
- [[Wisdom-Work]] — 制度性知识是 Wisdom Work 的组织层面表现，两者都涉及人类独有的价值判断和情境理解
- [[Knowledge-Compilation]] — 将制度性知识编译为 AI 可用格式的挑战，是 bridging institutional knowledge and AI 的关键环节
- [[AI-Ready-Organization]] — 组织需要为 AI 部署重新设计知识管理流程，主动捕获和管理制度性知识
