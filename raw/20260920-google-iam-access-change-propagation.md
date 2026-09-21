---
type: raw
title: "Access change propagation in Google Cloud IAM"
source: "https://docs.cloud.google.com/iam/docs/access-change-propagation"
author:
  - "Google Cloud"
created: "2026-09-20"
description: "Google Cloud IAM 官方说明：权限变更是 eventual consistency；policy 变更通常约 2 分钟、可能 7 分钟以上，group membership 变更可能更久，因此 revoke request 与 deny-effective 不是同一时间点。"
tags:
  - clippings
  - agent-security
  - verification
---

# Access change propagation in Google Cloud IAM

> Canonical source: https://docs.cloud.google.com/iam/docs/access-change-propagation
> Accessed: 2026-09-20.

## Source locator

- IAM access changes are eventually consistent; recent grants or revocations might not be effective everywhere immediately.
- Direct allow/deny policy changes typically propagate in about 2 minutes and can take 7 minutes or longer.
- Group membership changes typically take several minutes and can take hours or longer; nested-group changes can also take hours or longer.
- Removing a principal from a group generally propagates more slowly than adding one.

## Evidence boundary

These are platform propagation estimates, not Agent-specific revoke measurements and not hard upper bounds. They measure when authorization state becomes effective across IAM, not whether already-sent requests, existing connections, queued work or committed external effects have stopped or been reversed.
