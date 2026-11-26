---
type: source-summary
title: How AI agents shape experts’ judgment calls
canonical_url: https://www.anthropic.com/research/agents-judgment-calls
raw_state: index
original_raw_file: "20261027-anthropic-agents-judgment-calls.md"
original_body_sha256: "0e9cee8f6a1fa6f1bd18eb672b748f1588c8bf3eb94f74f323d9a7e5dd346409"
indexed_at: "2026-11-26T12:31:43+08:00"
author: Amaç Herdağdelen, Hailey Joren, Alex Tamkin
published: '2026-10-27'
created: '2026-11-26'
updated: '2026-11-26'
tags:
- source-summary
- agent-evaluation
- verification
- agent-security
evidence_level: medium
claim_type: mixed
source_locator:
- Study design
- Results
- Our study’s limitations
- What this means
---

# How AI agents shape experts’ judgment calls

> **原文保留边界**：来源为公开网页，按 canonical URL 与章节定位结算为可恢复索引（raw_state: index）。Registry 哈希对应临时来源登记摘录（非全文），不是原网页正文或全文哈希；原文需按来源链接回查。读取与结算日期：2026-11-26。

## 编译摘要

### 1. 浓缩

- **判断权与操作权可分离，但未必真的分离。** 研究将专业分析师置于农业合作社因果分析场景；对四项分析选择与最终建议分别随机指定 Agent 的倾向，要求它诚实论证且在证据反对时改变立场。61 人参加，50 人实际使用 Claude Code（Opus 4.8 High），11 人未使用。四项分析选择中，匹配倾向的比例为 86%；依次为结果变量 92%、比较方法 82%、覆盖人群 81%、权重 90%。最终推广建议的比例在 Agent 支持推广与反对推广的组分别为 54% 和 36%。定位：Study design / Results。
- **主观独立感不是独立判断的可靠指标。** 事后 48 人调查中，77% 至少一次复述 Agent 的论据，仅 15% 在任一回答中注明来自 Agent；52% 认为最终建议更多反映自己的判断。原先已表达偏好的参与者在 Agent 不同意时改变选择的比例为 60%，同意时为 6%。定位：Results。
- **使用 Agent 的收益与判断依赖同时存在。** 使用者严重方法错误为 3/50，未使用者为 6/11；中位完成时间 65 对 90 分钟。该比较非随机分配，不能归因于 Agent 本身。定位：Results / limitations。

### 2. 质疑

随机化的是工具内倾向，不是 AI 使用本身；研究人工强化倾向，不能把 86% 当成生产环境中所有专家的依赖率。判断题存在多个合理答案，跟随建议不自动意味着犯错。单一模型、任务、实验时段限制外部效度。参与者自报所有权和信心无法提供独立性证据。若多团队共享相同模型偏好，相关性会降低多次复核的独立证据价值；这是作者提出的风险，非本实验直接测得的系统性共识偏差。

### 3. 对标

- **综合判断：** [[Decision-Quality]] 中的人工批准应分为已了解依据、独立形成选择、接受建议、授权执行。高影响分歧先记录人的初始偏好，再展示正反论证与数据敏感性；低风险常规判断允许委托，避免所有细节都阻塞。
- [[Evaluation-Integrity]]：抽样对照 Agent 倾向反转、盲化评审与无建议基线；检验最终选择是否随无关先验改变，同时测正确性、用时与审查成本。
- [[Organization-as-Agent-Harness]]：企业审批留存候选方案、关键假设、反方理由、决策责任及真实终态。多人签字若都由同一 Agent 提供推理，不能自动计作多个独立证据。

## 前提与局限性

研究博客是直接来源；未在本轮独立复现实验、重新分析原始数据或逐页核对论文。对生信场景可优先试验统计模型、分析样本纳入、批次校正与阈值选择，不将实验比例直接外推为临床或生信项目风险。

## 关联概念

- [[Decision-Quality]]
- [[Evaluation-Integrity]]
- [[Organization-as-Agent-Harness]]
