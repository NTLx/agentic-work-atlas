---
type: source-summary
title: "Using LLMs to Secure Source Code"
source_raw:
  - "[[Using LLMs to secure source code]]"
created: 2026-05-28
updated: 2026-05-28
tags:
  - source-summary
  - security
  - agentic-engineering
  - llm-workflow
---

# Using LLMs to Secure Source Code

## 编译摘要

### 1. 浓缩
- **核心结论1**: LLM 辅助安全扫描的瓶颈已从发现（discovery）转移到验证、分类和修补——发现可并行化，但后续步骤仍是人工密集型。
  - 关键证据: Anthropic 截至 2026-05-22 已披露 1,596 个漏洞，仅 97 个被修补（6.1%）。发现能力远超修补能力，形成显著的"验证瓶颈"。
- **核心结论2**: Find-and-fix 六步循环——Threat Model → Sandbox → Discover → Verify → Triage → Patch。每步都有对应的 Claude skill 和参考 harness 实现。
  - 关键证据: Threat model 决定什么算漏洞（避免 false positive 噪音）；sandbox 隔离 Agent 并验证 exploit；discovery 使用 autonomous harness 并行扫描；verify 通过构建 PoC 确认可利用性；triage 按严重性排序；patch 生成修复代码。
- **核心结论3**: Agent 安全扫描的"沙箱验证"环节是关键——必须在隔离环境中证明漏洞可被实际利用，而非仅靠 LLM 判断代码有潜在风险。
  - 关键证据: 配套仓库 `defending-code-reference-harness` 提供 interactive skills（手动工作流）和 autonomous scanning harness（自动扫描），形成可复用的安全扫描基础设施。

### 2. 质疑
- **关于"6.1% 修补率"的质疑**: 1,596 个披露中仅 97 个被修补——这可能反映开源维护者的响应能力问题，而非 LLM 扫描本身的问题。但如果修补率持续低迷，发现的价值会被质疑。
- **关于"threat model 前置"的质疑**: 文章强调先决定什么算漏洞再扫描，这隐含假设团队有能力定义完整的威胁模型。对于缺乏安全专业知识的团队，这一步可能成为新的瓶颈。
- **关于"并行化 discover 的成本"的质疑**: 大规模并行扫描的 token 成本未披露。如果扫描数百万行代码，成本可能很高，需要考虑 ROI。

### 3. 对标
- **跨域关联1**: 与 [[Verifiable-Agent-Engineering|可验证 Agent 工程]] 的验证管道概念一致——安全扫描的 "discover → verify → patch" 流水线，本质上是把 LLM 的非确定性判断（这个代码有风险）转化为确定性验证（构建 PoC 证明可利用）。
- **跨域关联2**: Sandbox 隔离思路与 [[Agent-Containment|Agent Containment]] 的环境层隔离策略同源——安全扫描 Agent 本身也需要被隔离，因为它可能执行恶意代码来验证漏洞。
- **跨域关联3**: 与 [[20260518-zero-trust-for-ai-agents|Zero Trust for AI Agents]] 中的 Zero Trust 原则形成互补——LLM 安全扫描是 Zero Trust 中"持续验证"能力的具体实现手段。

### 关联概念
- [[Agentic-Engineering]]
- [[Agent-Containment]]
- [[Verifiable-Agent-Engineering]]
- [[Verifiability]]
- [[Code-Execution]]
