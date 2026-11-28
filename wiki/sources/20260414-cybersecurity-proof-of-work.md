---
type: source-summary
title: "Cybersecurity Looks Like Proof of Work Now"
source_raw:
  - "[[20260414-cybersecurity-proof-of-work]]"
created: 2026-05-24
updated: 2026-11-28
tags:
  - source-summary
---

# Cybersecurity Looks Like Proof of Work Now

## 编译摘要

### 1. 浓缩

- **核心结论1**: 作者以Proof of Work类比安全搜索，提出防御预算可能更重要；这是经济学推演而非必要充分条件，风险还受攻击面、隔离、缺陷类别、工具、质量及修复影响
  - 关键证据: “You don’t get points for being clever. You win by paying more... to harden a system you need to spend more tokens discovering exploits than attackers will spend exploiting them”

- **核心结论2**: Anthropic Mythos 模型在 AISI 测试中完成 32 步企业网络攻击模拟（人类需 20 小时），AISI报告在所测至100M Token预算范围内仍观察到进展；不能推出边际收益不递减或无限投入必然发现更多缺陷，美元为作者历史估算
  - 关键证据: “Mythos was the only model to complete the task, in 3 out of its 10 attempts... none of the models given a 100M budget showed signs of diminishing returns”

- **核心结论3**: 作者设想Agentic Coding可采用三阶段循环：开发 → 代码审查 → 安全硬化（human input vs money 分别是瓶颈）
  - 关键证据: “I suspect we’ll see a three phase cycle: development, review, and hardening”

### 2. 质疑

- **关于”结论1”的质疑**: 安全搜索不等于同质独立随机试验；成本变化、缺陷发现概率、架构消除漏洞类别、修复成本和攻击者目标均可改变预算关系。
- **关于”结论2”的质疑**: AISI是英国政府研究机构的独立评测来源，而非Anthropic自测；该模拟环境无主动防守、缺少真实安全工具且不惩罚告警，不能证明能攻破充分防护系统。
- **关于数据可靠性的质疑**: 所测预算内观察到进展，不等于验证无边际收益递减；真实攻击场景可能更复杂

### 3. 对标

- **跨域关联1**: Proof of Work 类似加密货币挖矿——计算投入可能提高搜索机会，但两类问题均不应简化为线性概率定律，漏洞搜索还依方法和目标
- **跨域关联2**: Linus’s law 扩展（”eyeballs + tokens”）类似开源软件历史：平台依赖 → 社区审计 → 企业投入 tokens 审计

### 概念更新建议

- **新增 Entity**: [[Cybersecurity-Proof-of-Work]]（安全搜索预算的经济学类比，待实证）
- **新增 Entity**: [[Drew-Breunig]]（作者）
- **新增 Entity**: [[Mythos]]（Anthropic 安全专用模型）
- **新增 Entity**: [[Security-Hardening-Phase]]（agentic coding 第三阶段）
- **更新 [[Agentic-Engineering]]**: 补充三阶段模型（开发/审查/硬化）

### 证据边界

2026-11-28回读作者Raw全文（58行）及[AISI评测原文](https://www.aisi.gov.uk/blog/our-evaluation-of-claude-mythos-previews-cyber-capabilities)。AISI明确3/10完整完成、平均完成22/32步骤，20小时为人类估计非匹配对照；预算范围内有进展，OT场景未完整完成。原文强调弱防护环境和现实差异；作者关于比攻击者投入更多Token的结论不是实证规律。防御侧按风险、缺陷类别、修复验证和剩余风险设计安全硬化预算，避免只以Token用量度量安全；未复跑实验。

## 关联概念

- [[Drew-Breunig]]
- [[Cybersecurity-Proof-of-Work]]
- [[Mythos]]
- [[Security-Hardening-Phase]]
- [[Agentic-Engineering]]
- [[Andrej-Karpathy]]
