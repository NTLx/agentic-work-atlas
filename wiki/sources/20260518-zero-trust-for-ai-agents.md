---
type: source-summary
title: "Zero Trust for AI Agents"
source_raw:
  - "[[20260518-zero-trust-for-ai-agents]]"
created: 2026-05-28
updated: 2026-11-28
tags:
  - source-summary
  - agent-security
  - zero-trust
  - enterprise
---

# Zero Trust for AI Agents

## 编译摘要

### 1. 浓缩
- **核心结论1**: Agent 安全需要 Zero Trust 原则——"永不信任、始终验证、假设已被攻破"。外围防御不足以单独处理内部权限滥用及AI加速威胁；数月到数小时是指南中的趋势叙述，未提供普适实测分布。
  - 关键证据: 历史政策勘误：2022-01-26 [OMB M-22-09](https://www.whitehouse.gov/wp-content/uploads/2022/01/M-22-09.pdf?enkwrd=canon)第1页文本要求适用机构在FY2024末实现指定目标；[DoD官方说明](https://dodcio.defense.gov/In-the-News/Article/3267555/dod-releases-path-to-cyber-security-through-zero-trust-architecture/)所述FY2027是国防部门目标，不能泛称全部联邦机构统一2027截止。此处非最新法律适用性审查。NIST SP 800-207为架构指南；不把Anthropic三层设计视为强制标准。
- **核心结论2**: Anthropic指南整理的五类Agent威胁向量（非OWASP Top10完整分类）——Prompt 注入（直接/间接）、工具和资源滥用（含 MCP tool poisoning 和 tool chaining）、身份与权限滥用（unscoped privilege inheritance）、内存与上下文投毒（RAG poisoning、shared context poisoning）、供应链风险（模型后门、MCP 恶意服务器）。
  - 关键证据: 间接 prompt 注入中，Microsoft Research 确认 LLM 无法可靠区分信息性上下文与可执行指令；指南转述特定训练数据投毒实验；未重新核对其原始研究、模型及训练条件，不保留固定样本数作为普遍阈值。
- **核心结论3**: "Impossible, not tedious" 设计测试——优先移除不必要的攻击能力，而非仅依赖增加摩擦；具体凭据、隔离和时限只约束其覆盖的路径。限速、审批及预算仍可限制吞吐、累计副作用与损失；不将攻击者耐心或边际成本视为无限或零。
  - 关键证据: 三层能力框架：Foundation（最小可行安全，但基线已提升——不能仅依赖摩擦性控制）→ Enterprise（大多数组织目标）→ Advanced（高风险/强监管基线）。

### 2. 质疑
- **关于"三层框架落地可行性"的质疑**: Foundation 层已经要求 cryptographic identity + short-lived tokens，这对中小团队是显著的基础设施门槛。大多数部署 Agent 的组织可能不具备专业安全工程能力。
- **关于"Advanced 层硬件隔离的可达性"的质疑**: AMD SEV、Intel TDX、confidential computing enclaves 在大多数云环境中仍是前沿能力，文中列为 Advanced 但实际部署门槛极高。
- **关于"OWASP 威胁模型的完整性"的质疑**: 威胁清单侧重技术攻击面，但 Agent 在组织中的社会工程风险（如 Agent 作为内部人的信任关系被利用）讨论较少。

### 3. 对标
- **跨域关联1**: Zero Trust 的"假设已被攻破"原则与 [[Agent-Containment|Agent Containment]] 的确定性边界兜底策略完全一致——都假设概率性防御会失败，需要硬边界。
- **跨域关联2**: Least Agency与动态Least Privilege互补；[OWASP ASI02](https://genai.owasp.org/agentic-applications-2026/asi02-tool-misuse-and-exploitation/)和[LLM03:2026](https://genai.owasp.org/llm2026/llm032026-excessive-agency/)明确最小工具功能、授权、完整中介、用户上下文和高影响审批；不主张词源首创，不仅限制访问什么，还限制 Agent 工具能做什么、做多少次、在哪里做。这与 [[Agent-Harness|Agent Harness]] 中的权限管理直接对接。
- **跨域关联3**: MCP tool poisoning 和 rug pull 攻击，与 [[Model-Context-Protocol-MCP|MCP]] 生态治理问题呼应——MCP Registry 作为治理中心可以部分缓解工具供应链风险。

### 证据边界

2026-11-28定向复核本地Raw导言及Impossible not tedious、Least Agency/privilege scoping、rate limits等定位；未逐页复验整本电子书、未核对原投毒研究。M-22-09文本可访问但页面截图返回cache miss；仅用公开正文文本和DoD官方HTML区分历史目标，不将其当作当前全部法规要求。OWASP建议并非部署安全证明。

## 关联概念
- [[Agent-Containment]]
- [[Least-Agency]]
- [[Agent-Harness]]
- [[Model-Context-Protocol-MCP]]
- [[Agentic-Engineering]]
- [[Verifiable-Agent-Engineering]]
