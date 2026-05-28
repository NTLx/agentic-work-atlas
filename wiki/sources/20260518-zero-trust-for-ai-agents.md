---
type: source-summary
title: "Zero Trust for AI Agents"
source_raw:
  - "[[20260518-zero-trust-for-ai-agents]]"
created: 2026-05-28
updated: 2026-05-28
tags:
  - source-summary
  - agent-security
  - zero-trust
  - enterprise
---

# Zero Trust for AI Agents

## 编译摘要

### 1. 浓缩
- **核心结论1**: Agent 安全需要 Zero Trust 原则——"永不信任、始终验证、假设已被攻破"。传统 perimeter 防御无法应对 AI 加速的攻击（漏洞到利用从数月压缩到数小时）。
  - 关键证据: 美国要求所有联邦机构在 2027 年前采纳 Zero Trust；NIST SP 800-207（2020）和 NSA ZIGs（2026）已将 Zero Trust 标准化。
- **核心结论2**: OWASP 识别的 Agent 五大威胁向量——Prompt 注入（直接/间接）、工具和资源滥用（含 MCP tool poisoning 和 tool chaining）、身份与权限滥用（unscoped privilege inheritance）、内存与上下文投毒（RAG poisoning、shared context poisoning）、供应链风险（模型后门、MCP 恶意服务器）。
  - 关键证据: 间接 prompt 注入中，Microsoft Research 确认 LLM 无法可靠区分信息性上下文与可执行指令；250 篇恶意文档即可后门化 600M-13B 参数模型，且后门在 SFT 和 RLHF 后仍存在。
- **核心结论3**: "Impossible, not tedious" 设计测试——控制措施必须让攻击在结构上不可能，而非仅仅繁琐。摩擦性控制（rate limits、SMS MFA、非标准端口）在 Agent 攻击者面前退化严重（无限耐心 + 接近零的边际成本）。
  - 关键证据: 三层能力框架：Foundation（最小可行安全，但基线已提升——摩擦性控制不再合格）→ Enterprise（大多数组织目标）→ Advanced（高风险/强监管基线）。

### 2. 质疑
- **关于"三层框架落地可行性"的质疑**: Foundation 层已经要求 cryptographic identity + short-lived tokens，这对中小团队是显著的基础设施门槛。大多数部署 Agent 的组织可能不具备专业安全工程能力。
- **关于"Advanced 层硬件隔离的可达性"的质疑**: AMD SEV、Intel TDX、confidential computing enclaves 在大多数云环境中仍是前沿能力，文中列为 Advanced 但实际部署门槛极高。
- **关于"OWASP 威胁模型的完整性"的质疑**: 威胁清单侧重技术攻击面，但 Agent 在组织中的社会工程风险（如 Agent 作为内部人的信任关系被利用）讨论较少。

### 3. 对标
- **跨域关联1**: Zero Trust 的"假设已被攻破"原则与 [[Agent-Containment|Agent Containment]] 的确定性边界兜底策略完全一致——都假设概率性防御会失败，需要硬边界。
- **跨域关联2**: Least Agency（OWASP 新概念）扩展了 Least Privilege，不仅限制访问什么，还限制 Agent 工具能做什么、做多少次、在哪里做。这与 [[Agent-Harness|Agent Harness]] 中的权限管理直接对接。
- **跨域关联3**: MCP tool poisoning 和 rug pull 攻击，与 [[Model-Context-Protocol-MCP|MCP]] 生态治理问题呼应——MCP Registry 作为治理中心可以部分缓解工具供应链风险。

### 关联概念
- [[Agent-Containment]]
- [[Least-Agency]]
- [[Agent-Harness]]
- [[Model-Context-Protocol-MCP]]
- [[Agentic-Engineering]]
- [[Verifiable-Agent-Engineering]]
