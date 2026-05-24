---
type: source-summary
title: "Cybersecurity Looks Like Proof of Work Now"
source_raw:
  - "[[20260414-cybersecurity-proof-of-work]]"
created: 2026-05-24
updated: 2026-05-24
tags:
  - source-summary
---

# Cybersecurity Looks Like Proof of Work Now

## 编译摘要

### 1. 浓缩

- **核心结论1**: 网络安全正在变成”Proof of Work”博弈——防御者需要花费比攻击者更多的 tokens 发现漏洞，而非依靠技术巧思
  - 关键证据: “You don’t get points for being clever. You win by paying more... to harden a system you need to spend more tokens discovering exploits than attackers will spend exploiting them”

- **核心结论2**: Anthropic Mythos 模型在 AISI 测试中完成 32 步企业网络攻击模拟（人类需 20 小时），100M tokens 预算（`$12,500`）仍未显示边际收益递减
  - 关键证据: “Mythos was the only model to complete the task, in 3 out of its 10 attempts... none of the models given a 100M budget showed signs of diminishing returns”

- **核心结论3**: Agentic Coding 将进入三阶段循环：开发 → 代码审查 → 安全硬化（human input vs money 分别是瓶颈）
  - 关键证据: “I suspect we’ll see a three phase cycle: development, review, and hardening”

### 2. 质疑

- **关于”结论1”的质疑**: Proof of Work 模型假设 tokens 成本不变；若推理成本下降（如推理优化），安全预算是否持续有效？
- **关于”结论2”的质疑**: Mythos 测试结果来自 AISI（英国 AI 安全研究所），是否独立验证？Anthropic 自称”strikingly capable”可能有营销成分
- **关于数据可靠性的质疑**: 100M tokens 预算未显示边际收益递减，但测试范围有限；真实攻击场景可能更复杂

### 3. 对标

- **跨域关联1**: Proof of Work 类似加密货币挖矿——成功概率与算力投入成正比，而非技术优势
- **跨域关联2**: Linus’s law 扩展（”eyeballs + tokens”）类似开源软件历史：平台依赖 → 社区审计 → 企业投入 tokens 审计

### 概念更新建议

- **新增 Entity**: [[Cybersecurity-Proof-of-Work]]（安全即 token 成本博弈）
- **新增 Entity**: [[Drew-Breunig]]（作者）
- **新增 Entity**: [[Mythos]]（Anthropic 安全专用模型）
- **新增 Entity**: [[Security-Hardening-Phase]]（agentic coding 第三阶段）
- **更新 [[Agentic-Engineering]]**: 补充三阶段模型（开发/审查/硬化）

## 关联概念

- [[Drew-Breunig]]
- [[Cybersecurity-Proof-of-Work]]
- [[Mythos]]
- [[Security-Hardening-Phase]]
- [[Agentic-Engineering]]
- [[Andrej-Karpathy]]
