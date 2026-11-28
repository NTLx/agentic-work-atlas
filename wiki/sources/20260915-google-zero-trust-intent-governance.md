---
type: source-summary
title: "Build zero-trust AI agents that judge intent, not just syntax"
source_raw:
  - "[[20260915-google-zero-trust-intent-governance]]"
canonical_url: "https://developers.googleblog.com/build-zero-trust-ai-agents-that-judge-intent-not-just-syntax/"
raw_state: full
created: 2026-09-18
updated: 2026-11-28
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

- **核心结论 1：只检查语法和固定模式可能遗漏业务语义及跨状态违规；确定性业务状态、产品类别及授权规则仍可覆盖许多具体风险。**
  - 关键证据：文章用退款 Agent 说明，SQL 参数、金额和输入格式都可以合法，但“数字商品退款”仍可能违反业务政策；仅依据单次请求、未读取权威累计状态的检查会遗漏累计违规；单次执行门禁仍可查询并原子检查跨轮次状态。
- **核心结论 2：运行时治理被拆成三个互补控制面。**
  - 关键证据：Model Armor 在入口/出口筛查 prompt injection、jailbreak、恶意 URL 和敏感信息；Semantic Governance Policies 在工具执行前根据用户意图、会话历史、工具参数和自然语言规则给出 Allow/Deny；Agent Anomaly Detection据厂商描述使用统计模型和LLM分析会话及Agent fleet遥测；示例detector、confidence和finding形状为illustrative，本地代码是stand-in。
- **核心结论 3：检测可以进入闭环，让管理员在不重部署 Agent 的情况下补充策略。**
  - 关键证据：示例中每次 `$20` 退款单独低于阈值，但累计超过订单的 `$149`；异常示例已发生累计超额退款，管理员可新增同一会话订单重复退款策略并拦截后续调用；不撤销既有副作用，且不证明跨会话、并发与重放路径均受阻。

### 2. 质疑

- **关于“判断意图”的质疑**：语义策略本身仍是 LLM 判断，可能误放行、误阻断或被上下文操纵；文章没有给出 precision、recall、延迟、成本和跨模型稳定性。
- **关于覆盖面的质疑**：平台控制只有在所有相关工具、API、MCP server、网络和副作用都经过 Agent Gateway 时才成立；文章的 refund demo 不能证明真实企业 action surface 已完整中介。
- **关于异常检测的质疑**：文中的 detector 名称、confidence 和 finding shape 明确标注为 illustrative；真实多租户环境中的基线、误报和对抗适应没有呈现。
- **关于闭环治理的质疑**：动态加策略提高响应速度，也带来策略冲突、过期策略、责任归属、失败关闭和审计版本管理问题；没有部署级恢复指标。
- **关于职责迁移的质疑**：治理从 Agent 开发者移到平台/安全管理员是重要组织变化，但需要清楚的 policy owner、执行点和撤销权，否则只是把责任换了名字。

### 3. 对标

- **与治理策略即代码对标**：[[Policy-as-Code-for-Agent-Governance]] 已把权限和升级规则放在模型外；Google 示例补充了自然语言策略在工具执行点的运行时裁决和动态更新。
- **与 Agent Logic 对标**：[[Agent-Logic]] 负责把确定性、可验证的企业规则放进 harness；语义治理适合提出风险判定，不能替代确定性权限和账务约束。**综合判断**：在提交事务内检查订单剩余可退余额、幂等键、请求身份/授权及并发一致性；产品分类如已有权威字段，优先使用结构化规则。检测、拒绝后续动作与补偿已提交动作是不同能力。
- **与观测和遏制对标**：[[Agent-Observability]] 提供跨会话证据，[[Agent-Containment]] 限制失败后的 blast radius；三者共同构成“看见—判定—拦截/恢复”链。
- **跨域迁移**：零信任 Agent 的最小闭环不是“模型拒绝危险请求”，而是“入口筛查 + 工具前授权 + 跨状态异常 + 独立执行点 + 策略回流”；这是一条综合判断，不能由本文单独证明。

## 前提与局限性

2026-11-28回读本地Raw全295行。文章是Google平台技术说明；伴随demo用本地Python函数和模拟器，未复跑、未审核实际托管Gateway或生产安全覆盖。它能支持运行时控制的架构模式和威胁示例，不足以支持“语义策略已经可靠判断真实意图”或“闭环路由已在生产中普遍有效”。

## 关联概念

- [[Agent-Security]]
- [[Policy-as-Code-for-Agent-Governance]]
- [[Agent-Logic]]
- [[Agent-Observability]]
- [[Agent-Containment]]

