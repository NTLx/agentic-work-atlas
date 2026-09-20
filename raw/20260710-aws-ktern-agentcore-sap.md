---
type: raw
title: "How KTern.AI built agentic AI for SAP on Amazon Bedrock AgentCore"
source: "https://aws.amazon.com/blogs/machine-learning/how-ktern-ai-built-agentic-ai-for-sap-on-amazon-bedrock-agentcore/"
author:
  - "Vijayaraghavan C P"
  - "Prabhu G"
published: "2026-07-10"
created: "2026-09-19"
description: "AWS/KTern.AI 客户案例：20+ production agents、per-agent least privilege、session isolation、VPC 私网访问与完整 tool audit；同时用 AgentCore Memory 保留 12–18 个月项目上下文，显示权限最小化不等于保留最小化。"
tags:
  - clippings
  - agent-security
  - privacy
---

# How KTern.AI built agentic AI for SAP on Amazon Bedrock AgentCore

> Canonical source: https://aws.amazon.com/blogs/machine-learning/how-ktern-ai-built-agentic-ai-for-sap-on-amazon-bedrock-agentcore/

## Source locator

- KTern.AI reports 20+ specialized agents in production and 50+ agent configurations.
- Agents access SAP APIs, customer ERP systems, process-mining sources and KTern repositories through AgentCore Gateway / MCP.
- Runtime provides session isolation across customer environments.
- Agents connect privately over VPC interface endpoints / AWS PrivateLink.
- AgentCore Identity enforces authentication and least-privilege access per agent and tool.
- Tool actions and model responses are logged/traced through AgentCore observability and CloudWatch.
- AgentCore Memory stores persistent project context, including process decisions, code patterns and accumulated insights across sessions.
- SAP transformation projects are described as lasting 12–18 months; the system intentionally carries project history across that period.
- Reported operational metrics include 99.8% agent uptime and 82% first-pass success rate for evaluation cycles.

## Evidence boundary

This is an AWS customer/solution case, not independent privacy research. It provides a production example of per-agent least privilege and tenant/session isolation. It does not report data-volume minimization, retention TTL, selective forgetting or deletion metrics. In fact, its persistent project memory is an explicit counterexample to equating least privilege with minimum retention: long-lived context can be intentional and useful while still creating a separate governance obligation.
