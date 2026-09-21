---
type: raw
title: "Revoke user access in an emergency in Microsoft Entra ID"
source: "https://learn.microsoft.com/en-us/entra/identity/users/users-revoke-access"
author:
  - "Microsoft"
created: "2026-09-20"
description: "Microsoft Entra 官方撤销文档：阻止新登录与撤销 refresh token 不会瞬间终止所有现有 access/session；默认 access token 生命周期约 1 小时，应用自有 session 的结束依赖应用或同步机制。"
tags:
  - clippings
  - agent-security
  - verification
---

# Revoke user access in an emergency in Microsoft Entra ID

> Canonical source: https://learn.microsoft.com/en-us/entra/identity/users/users-revoke-access
> Source last updated: 2026-06-19.
> Accessed: 2026-09-20.

## Source locator

- Administrators can disable the account, revoke refresh tokens and disable registered devices.
- Existing access tokens are not necessarily invalidated immediately; default Microsoft Entra access-token lifetime is about one hour.
- For applications using session tokens, existing sessions end when the token expires unless the application is configured to synchronize disabled state and revoke its sessions.
- Applications that issue their own session tokens are responsible for revoking those application sessions.

## Evidence boundary

This is identity-platform guidance, not an Agent incident experiment. It demonstrates that identity authority, access-token validity and application-session validity can have different owners and clocks. It does not describe whether an already-dispatched Agent action is cancelled, whether a business transaction commits, or how external effects are compensated.
