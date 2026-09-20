---
type: source-summary
title: "How KTern.AI built agentic AI for SAP on Amazon Bedrock AgentCore"
source_raw:
  - "[[20260710-aws-ktern-agentcore-sap]]"
canonical_url: "https://aws.amazon.com/blogs/machine-learning/how-ktern-ai-built-agentic-ai-for-sap-on-amazon-bedrock-agentcore/"
raw_state: full
source_locator:
  - "20+ production agents / 50+ configurations"
  - "per-agent least privilege + session isolation + private network path"
  - "persistent AgentCore Memory across 12–18 month SAP projects"
created: 2026-09-19
updated: 2026-09-19
tags:
  - source-summary
  - agent-security
  - privacy
evidence_level: medium
claim_type: mixed
---

# How KTern.AI built agentic AI for SAP on Amazon Bedrock AgentCore

## 编译摘要

### 1. 浓缩

- **核心结论 1：生产 multi-agent 系统可以实行 per-agent least privilege 与 tenant/session isolation。**
  - 关键证据：20+ production agents，AgentCore Identity 按 agent/tool 约束访问，Runtime 隔离客户 session，网络走 VPC/PrivateLink。
- **核心结论 2：least privilege 与 data retention 完全可以朝不同方向变化。**
  - 关键证据：同一架构明确使用 persistent memory 保存 process decisions、code patterns 和 accumulated insights，项目周期长达 12–18 个月。
- **核心结论 3：审计 trace 也不等于数据最小化。**
  - 关键证据：所有 tool/model activity 可观测，但页面没有 read-volume、context minimization、TTL/deletion 指标。

### 2. 质疑

- 厂商客户案例，自报架构与效果。
- 长期 memory 可能是业务必要状态，不能因为“保留久”直接判定为过度收集。
- 页面没有给出 retention policy、selective forgetting 或项目结束后的删除语义。

### 3. 对标

- 对 CR-002：这是最清楚的“权限安全 ≠ 数据最小化”案例。
- 对 [[Agent-Data-Minimization]]：要求把 authorization、actual reads、retention/deletion 分开度量。
- 对 [[Least-Agency]]：least agency 解决动作能力边界，但不自动决定 memory 生命周期。

## 关联概念

- [[Agent-Data-Minimization]]
- [[Least-Agency]]
- [[Agent-Security]]
