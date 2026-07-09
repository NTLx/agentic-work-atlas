---
type: source-summary
title: "古德哈特定律：指标的暴政"
source_raw:
  - "[[20260706-goodharts-law-tyranny-of-metrics]]"
created: 2026-07-09
updated: 2026-07-09
tags:
  - source-summary
  - goodharts-law
  - metrics
  - evaluation
evidence_level: medium
claim_type: mixed
---

# 古德哈特定律：指标的暴政

## 编译摘要

### 1. 浓缩
- **核心结论1**: 古德哈特定律的核心机制——代理指标（proxy）一旦成为奖惩目标，人们就会优化指标而非真实目标（true objective），导致指标失效。机制链条：真实目标 → 代理指标 → 优化压力 → 目标替代
  - 关键证据: 软件公司 bug 修复数考核——员工专挑简单 bug、拆分大工单、搁置难题，修复数顶半个团队却无真实贡献；NHS 急诊 4 小时指标导致医院把病人堵在救护车里、晾在走廊上
- **核心结论2**: 古德哈特定律有两个近亲——卢卡斯批判（经济政策领域：人们会针对新政策优化行为，历史规律不可外推）和坎贝尔定律（社会指标领域：越用于重大决策的指标越容易被腐蚀）。三者共同揭示"度量即干预"的不可逃避性
  - 关键证据: 卢卡斯批判源于 1975 年古德哈特对英国央行货币政策的分析；坎贝尔定律用于社会现象解释；社交媒体互动指标放大错误信息和极端对立
- **核心结论3**: 在 AI agent 语境中的延伸——当 eval benchmark 成为模型优化的目标，benchmark 就不再是好的能力度量（benchmark gaming）；当代码行数/修复数成为 agent 产出度量，agent 会学会拆分工单和挑简单 bug。这与 [[Reward-Hacking|reward hacking]] 结构同构
  - 关键证据: 此结论为编译阶段的综合判断，非原文直接讨论。原文的 bug 修复数案例与 AI agent 的工单修复数场景存在直接类比关系

### 2. 质疑
- **关于"结论3"的质疑**: 将古德哈特定律应用到 AI agent 评估是编译阶段的综合判断，非原文讨论内容。原文的案例（NHS 急诊、社交媒体互动）是传统领域，向 AI agent 领域的迁移需要验证边界条件
- **关于"解法"的质疑**: 原文提到了一些缓解思路（多指标、不可预测指标），但没有系统性方案。古德哈特定律是否真正有"解"仍是开放问题
- **关于证据强度的说明**: 原文为知识转述类音频节目（万维钢讲读），非学术一手来源。核心定律本身来自经济学文献（Goodhart 1975, Strathern 1997），但讲述过程中的案例和简化可能损失学术精确性

### 3. 对标
- **跨域关联1**: 古德哈特定律与 AI 领域的 [[Reward-Hacking|reward hacking]] 同构——当 reward function 成为优化目标，agent 找到 loophole 而非完成真实任务。古德哈特定律是 reward hacking 在人类组织中的社会学版本
- **跨域关联2**: 与 [[LLM-as-a-Judge]] 关联——LLM 裁判的 rubric 设计本质上是在对抗古德哈特定律，需要防止被评估模型 gaming rubric 中的可量化维度
- **跨域关联3**: 与 [[Agent-Verification]] 关联——验证机制的设计需要超越可被 gaming 的代理指标，向真实目标的直接评估或不可预测采样方向演进

### 关联概念
- [[Goodharts-Law]]
- [[LLM-as-a-Judge]]
- [[Agent-Verification]]
- [[Reward-Hacking]]
