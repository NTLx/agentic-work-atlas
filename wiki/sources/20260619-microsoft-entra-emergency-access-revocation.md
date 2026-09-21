---
type: source-summary
title: "Revoke user access in an emergency in Microsoft Entra ID"
source_raw:
  - "[[20260619-microsoft-entra-emergency-access-revocation]]"
canonical_url: "https://learn.microsoft.com/en-us/entra/identity/users/users-revoke-access"
raw_state: full
source_locator:
  - "disable account + revoke refresh tokens + disable devices"
  - "existing access token may remain valid until expiry; default ≈1 hour"
  - "application-issued sessions require application-side revocation/synchronization"
created: 2026-09-20
updated: 2026-09-20
tags:
  - source-summary
  - agent-security
  - verification
evidence_level: high
claim_type: extracted
---

# Revoke user access in an emergency in Microsoft Entra ID

## 编译摘要

### 1. 浓缩

- **核心结论 1：identity revoke 不等于所有 session 立即死亡。**
  - Entra 可以阻止新登录并撤销 refresh token，但现有 access token 可能持续到过期；默认生命周期约 1 小时。
- **核心结论 2：应用 session 有自己的 owner。**
  - 应用自己签发的 session token 需要应用自身终止；若依赖同步 disabled state，结束时间取决于应用配置与同步机制。
- **核心结论 3：撤销状态具有层级和所有权。**
  - account、refresh token、access token、device 与 application session 是不同对象，不能把其中一个变成 inactive 当作全链完成。

### 2. 质疑

- 这是用户/身份平台文档，不是 Agent 工具调用的 revoke-after-send 实测。
- 默认 access-token 生命周期不是所有应用和 Conditional Access 场景的固定值。
- 即使 session 被终止，也不代表已经提交的 API/业务 effect 被撤销。

### 3. 对标

- 对 EX-005：补强 authority owner / session owner 分离；permission stop 自身就可能跨多个时钟和系统。
- 对 [[Agent-Security]]：至少要记录 account disable、refresh-token revoke、access-token expiry/CAE、application-session revoke 四类状态，而不是单一 revoked。
- 对 CR-004：需要能把 identity event 继续 join 到应用 session 与目标系统 action receipt，才可判断真实阻断时间。

## 关联概念

- [[Agent-Security]]
- [[Long-Lived-Credential-Risk]]
- [[Distinct-Principal-Identity]]
- [[Agent-Observability]]
