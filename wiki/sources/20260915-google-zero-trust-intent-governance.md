---
type: source-summary
title: "Build zero-trust AI agents that judge intent, not just syntax"
source_raw:
  - "[[20260915-google-zero-trust-intent-governance]]"
canonical_url: "https://developers.googleblog.com/build-zero-trust-ai-agents-that-judge-intent-not-just-syntax/"
raw_state: full
created: 2026-09-18
updated: 2026-09-18
tags:
  - source-summary
  - agent-security
  - zero-trust
  - agentic-engineering
evidence_level: medium
claim_type: mixed
---

# Build zero-trust AI agents that judge intent, not just syntax

> 来源：Google Developers Blog，Eric Dong、Shubham Saboo，2026-09-15。本文是 Gemini Enterprise Agent Platform 的产品化技术说明，并附开源 companion demo；机制可提取，产品效果和示例阈值仍需独立验证。

## 编译摘要

### 1. 浓缩

- **核心结论 1：只在构建期检查语法和固定模式，无法识别语义上合法但意图恶意的动作。**
  - 关键证据：文章用退款 Agent 说明，SQL 参数、金额和输入格式都可以合法，但“数字商品退款”仍可能违反业务政策；单轮检查也看不到跨轮次的累计盗取。
- **核心结论 2：运行时治理被拆成三个互补控制面。**
  - 关键证据：Model Armor 在入口/出口筛查 prompt injection、jailbreak、恶意 URL 和敏感信息；Semantic Governance Policies 在工具执行前根据用户意图、会话历史、工具参数和自然语言规则给出 Allow/Deny；Agent Anomaly Detection 跨会话遥测发现重复工具调用、写入速度和累计金额异常。
- **核心结论 3：检测可以进入闭环，让管理员在不重部署 Agent 的情况下补充策略。**
  - 关键证据：示例中每次 `$20` 退款单独低于阈值，但累计超过订单的 `$149`；异常被发现后，管理员创建针对同一订单重复退款的语义策略，下一次工具调用由 Agent Gateway 拦截。

### 2. 质疑

- **关于“判断意图”的质疑**：语义策略本身仍是 LLM 判断，可能误放行、误阻断或被上下文操纵；文章没有给出 precision、recall、延迟、成本和跨模型稳定性。
- **关于覆盖面的质疑**：平台控制只有在所有相关工具、API、MCP server、网络和副作用都经过 Agent Gateway 时才成立；文章的 refund demo 不能证明真实企业 action surface 已完整中介。
- **关于异常检测的质疑**：文中的 detector 名称、confidence 和 finding shape 明确标注为 illustrative；真实多租户环境中的基线、误报和对抗适应没有呈现。
- **关于闭环治理的质疑**：动态加策略提高响应速度，也带来策略冲突、过期策略、责任归属、失败关闭和审计版本管理问题；没有部署级恢复指标。
- **关于职责迁移的质疑**：治理从 Agent 开发者移到平台/安全管理员是重要组织变化，但需要清楚的 policy owner、执行点和撤销权，否则只是把责任换了名字。

### 3. 对标

- **与治理策略即代码对标**：[[Policy-as-Code-for-Agent-Governance]] 已把权限和升级规则放在模型外；Google 示例补充了自然语言策略在工具执行点的运行时裁决和动态更新。
- **与 Agent Logic 对标**：[[Agent-Logic]] 负责把确定性、可验证的企业规则放进 harness；语义治理适合处理难以穷举的上下文规则，但不能替代确定性权限和账务约束。
- **与观测和遏制对标**：[[Agent-Observability]] 提供跨会话证据，[[Agent-Containment]] 限制失败后的 blast radius；三者共同构成“看见—判定—拦截/恢复”链。
- **跨域迁移**：零信任 Agent 的最小闭环不是“模型拒绝危险请求”，而是“入口筛查 + 工具前授权 + 跨状态异常 + 独立执行点 + 策略回流”；这是一条综合判断，不能由本文单独证明。

## 前提与局限性

文章是 Google 平台的官方产品技术说明，包含开源 demo 但不是独立安全评测。它能支持运行时控制的架构模式和威胁示例，不足以支持“语义策略已经可靠判断真实意图”或“闭环路由已在生产中普遍有效”。

## 关联概念

- [[Agent-Security]]
- [[Policy-as-Code-for-Agent-Governance]]
- [[Agent-Logic]]
- [[Agent-Observability]]
- [[Agent-Containment]]

