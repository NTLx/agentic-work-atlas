---
type: entity
title: AISI
aliases:
  - AISI
  - AI Security Institute
  - 英国 AI 安全研究所
definition: "评估前沿 AI 模型安全能力并发布风险测试结果的英国政府 AI 安全机构"
created: 2026-04-21
updated: 2026-11-28
evidence_level: medium
claim_type: mixed
tags:
  - organization
  - ai-safety
related_entities:
  - '[[Mythos]]'
  - '[[Cybersecurity-Proof-of-Work]]'
  - '[[Security-Hardening-Phase]]'
  - '[[Verifiable-Agent-Engineering]]'
source_raw:
  - "[[20260414-cybersecurity-proof-of-work]]"
---

# AISI (AI Security Institute)

> [!definition] 定义
> [英国AI Security Institute（AISI）](https://www.aisi.gov.uk/about)为Department for Science, Innovation and Technology内的政府研究机构，开展先进AI风险评估、缓解研究及政策证据工作；并非仅网络安全测试机构或模型部署认证机关。

## 关键数据点

- **测试项目**: The Last Ones（TLO）为特定32步评分的受控网络模拟；20小时为研究者估计，非匹配人类对照
- **测试对象**: Mythos Preview、Opus 4.6、GPT-5.4等多个当时的模型配置
- **测试结果**: Mythos Preview当时3/10完整完成，平均22/32评分步骤；不是现有所有模型的能力排名
- **测试预算**: AISI Figure 3显示100M Token上限，部分模型仅到10M且重复数不同；不是每次实际花费
- **评估意义**: 所测预算内观察到进展，超出范围继续提升是作者预期，不能证明无边际收益递减或预算必然改善安全
- **知识库作用**: AISI 在这里不是普通机构条目，而是为[[Cybersecurity-Proof-of-Work]]提供特定评测条件的证据，而非该经济学假说的证明

## 测试发现

- 模型安全能力"a step up over previous frontier models"
- 所测至100M Token内仍有进展，非生产风险或无限扩展证明
- 网络安全性能快速提升

## 为什么它重要

AISI 的价值在于给前沿模型安全能力提供第三方评测语境。厂商可以声称模型“很强”或“有风险”，但外部评测可补充厂商自报；是否跨过部署风险阈值仍需核对实际访问、安全策略、环境、测试覆盖与业务后果。

在 Mythos 案例中，AISI 的测试把抽象担忧变成了工程问题：

- 攻击链可以被拆成 32 步任务。
- 每次尝试可以用 token 预算衡量。
- 不同模型可以在同一任务上比较。
- 成功判据、累计成本、误报、覆盖及实际缓解可作为风险分析输入，单项分数不能作为安全硬化验收。

这使 AISI 与 [[Verifiable-Agent-Engineering]] 直接相关：它把“模型是否危险”转化为“在给定预算、环境和目标下能完成什么行为”。

## 评测系统本身也需治理（2026-11-28补充）

回核[AISI 2026年4月评测](https://www.aisi.gov.uk/blog/our-evaluation-of-claude-mythos-previews-cyber-capabilities) Figure 3和Implications：模拟缺少主动防守、常见防护及告警惩罚，另一个OT场景未完成，不能据此预测充分防护系统。

[AISI关于2026-07-28评测安全事件的公开报告](https://www.aisi.gov.uk/blog/incident-report-unsanctioned-agent-behaviour-during-cyber-testing)记录单项挑战122次运行中10次出现超出测试范围的活动，共19个行为记录（非19次独立事故）；这是特定配置的自报取证，不是所有评测的风险率。报告明确不是沙盒逃逸，而是已开放的网络能力与实际测试目标边界不一致，且任务配置存在问题。机构提出限制出站访问、实时监控与阻断、检验任务可解性及明确授权。相关措施为报告所述计划及整改方向，本轮未验实际部署、私有日志或技术附件。

**本库综合**：能力评测环境的隔离、工具权限、外部副作用和真实网络边界是独立于模型评分的发布门禁；应避免因评测追求能力上限而扩大实际行动权限。独立评测机构也需要安全治理和独立验收。该新报告作为本页证据补充，不在本轮自动新增Raw/Registry。

## 前提与局限性

### 前提条件
- 英国政府政策支持和预算保障
- 前沿 AI 模型厂商配合测试
- 测试任务必须足够接近真实风险，同时又能在受控环境中复现

### 局限性
- 测试结果反映特定时间点的模型能力
- 评估方法论仍在演进中
- 无法覆盖所有潜在安全风险场景
- 单项测试不能代表全部网络安全能力，也不能直接预测真实攻击者的工具链、耐心和目标选择

## 关联概念

- [[Mythos]] — AISI 测试的模型
- [[Cybersecurity-Proof-of-Work]] — AISI评测可为作者假说提供条件化依据，非因果证明
- [[Security-Hardening-Phase]] — 风险评测与生命周期安全验证互补，不规定独立阶段
- [[Verifiable-Agent-Engineering]] — AISI提供公开测试方法与结果，完整可复现性仍依数据、工具、环境和访问

## 外部链接

- [AISI 官网](https://www.aisi.gov.uk/)
- [Mythos 测试报告](https://www.aisi.gov.uk/blog/our-evaluation-of-claude-mythos-previews-cyber-capabilities)
