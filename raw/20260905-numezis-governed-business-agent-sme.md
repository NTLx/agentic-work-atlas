---
type: raw
title: "A governed business agent, in production at a Swiss services SME"
source: "https://advisory.numezis.com/en/work/business-agent-platform-sme"
author:
  - "Numezis Advisory & Engineering"
created: "2026-09-19"
description: "匿名瑞士服务型 SME 的 6 个月生产案例：按法人/客户文件隔离检索、逐工具权限、不可变审计、前三个月全量人工审批、模型调用无保留且不以客户数据训练。"
tags:
  - clippings
  - privacy
  - agent-governance
---

# A governed business agent, in production at a Swiss services SME

> Canonical source: https://advisory.numezis.com/en/work/business-agent-platform-sme
> Accessed: 2026-09-19.

## Source locator

- Anonymised representative case drawn from real Numezis engagements.
- Swiss fiduciary / administrative services SME:
  - about 35 employees;
  - 3 legal entities;
  - about 450 active client files.
- Engagement duration: 6 months during 2025–2026.
- Agent layer reads incoming email, documents and accounting entries, prepares actions, and executes within explicit controls.
- Document retrieval is segregated by legal entity and client file.
- MCP connectors expose controlled access to accounting software, DMS and mailbox, with tool-specific permissions.
- Every read, proposal and decision is logged.
- First 3 months: no outbound action without human approval.
- Later low-risk actions move to sample-based approval.
- Model calls are configured with no retention and no training on client data.
- Immutable audit log is reviewed with the external audit firm.
- Reported operational comparison uses the 90 days before pilot vs last 90 days of engagement.

## Evidence boundary

This is an anonymised consultant-authored case study, not an independently audited research paper. It demonstrates that an agentic workflow can be designed with file/entity segregation, tool-level permissions and model-side no-retention/no-training controls. It does not report actual bytes/records read per task, end-to-end context retention outside the model provider, deletion/TTL metrics, or a long multi-year longitudinal privacy outcome.
