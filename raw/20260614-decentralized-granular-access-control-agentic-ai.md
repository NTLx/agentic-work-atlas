---
type: raw
title: "Decentralized Granular Access Control for Agentic AI Systems in Critical Infrastructure"
source: "https://arxiv.org/abs/2607.22611"
author:
  - "Arun Malik"
  - "Deepal Jayasinghe"
  - "Bradley Klemick"
  - "Prachi Shah"
  - "Nitish Talasu"
  - "Vineet Tushar Trivedi"
published: "2026-06-14"
created: "2026-09-19"
description: "生产级细粒度 Agent 权限架构：20+ 专用 Agent、60+ deterministic playbooks、每天数千次操作，8 个月零未授权写入；但未提供读取量、上下文保留或删除/TTL 证据。"
tags:
  - clippings
  - agent-security
  - permissions
---

# Decentralized Granular Access Control for Agentic AI Systems in Critical Infrastructure

> Canonical source: https://arxiv.org/abs/2607.22611

## Source locator

- Proposes decentralized multi-layer access control for agentic AI in critical cloud infrastructure.
- Compound identity binds agent action authority to delegated human authority.
- Five permission levels span global platform access down to per-parameter constraints.
- Tool teams independently own authorization policy boundaries.
- Progressive trust escalation and safety interlocks constrain high-risk actions.
- Production deployment is reported at a major cloud provider managing network infrastructure across hundreds of datacenters.
- Scale:
  - 20+ specialized AI agents;
  - 60+ deterministic playbooks;
  - thousands of operations per day;
  - 8 months of production operation.
- Reported outcome: zero unauthorized write operations over those 8 months.
- High-risk write actions are not granted as unconstrained autonomous capability; the design routes them through deterministic playbooks / approval mechanisms.

## Evidence boundary

The paper is a preprint and the deployment/customer is not independently named in the paper. Most importantly for CR-002, its outcome metric is unauthorized write prevention. It does not report how much data agents read, whether read scope was minimal relative to task necessity, how much context was retained, or deletion/TTL behavior. Therefore it is strong evidence against unavoidable over-broad write authority, but not a direct longitudinal proof of data minimization.
