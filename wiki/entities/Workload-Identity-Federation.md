---
type: entity
title: "Workload Identity Federation"
aliases:
  - Workload Identity Federation
  - Workload Identity
  - 工作负载身份联邦
  - OIDC Federation
  - Ambient Authority
definition: "基于云 provider 的 ambient authority（VM/container metadata endpoint）为 workload 自动签发 short-lived OIDC tokens 的凭据方案——'no credential to leak, no way to use this credential anywhere but in CI'。代表性实现：AWS IAM Roles Anywhere / GCP Workload Identity / Azure Managed Identity / GitHub Actions OIDC。"
created: 2026-08-01
updated: 2026-08-01
tags:
  - credential-security
  - infrastructure
  - zero-trust
related_entities:
  - "[[Long-Lived-Credential-Risk]]"
  - "[[Rogue-AI-Agent]]"
  - "[[Agent-Containment]]"
  - "[[Agent-Harness]]"
source_raw:
  - "[[20260801-tailscale-hugging-face-ai-agent-intrusion]]"
---

# Workload Identity Federation

> [!definition] 定义
> **Workload Identity Federation** 是基于云 provider ambient authority（VM/container metadata endpoint）为 workload 自动签发 short-lived OIDC tokens 的凭据方案。核心优势：**no credential to leak, no way to use this credential anywhere but in CI**——把"凭据泄漏"从威胁模型中消除。
>
> 代表性实现：AWS IAM Roles Anywhere / GCP Workload Identity / Azure Managed Identity / GitHub Actions OIDC / Tailscale workload identity federation。

## 工作机制

```
CI workload (VM/container) 启动
  ↓
workload 询问 cloud metadata endpoint："我是谁？"
  ↓
cloud 验证 workload 的身份（基于 VM 实例 ID / container ID）
  ↓
cloud 签发 OIDC token（短生命周期，分钟级）
  ↓
workload 用 OIDC token 换取具体服务的 short-lived credential
  ↓
Tailscale / 第三方服务 验证 token + 授予权限（按 workload tags）
  ↓
CI job 结束 → token 自动失效 → 无残留凭据
```

**关键特性**：
1. **Ambient**：无需用户配置——VM/container 启动时自动获得身份
2. **Short-lived**：token 寿命以分钟计——被偷也很快失效
3. **Workload-bound**：token 与特定 workload 绑定——"no way to use this credential anywhere but in CI"
4. **Automatic**：无需手动签发——spin up CI node → Tailscale gets identity → assigns tags

## 三类实现对比

| 实现 | 云 provider | 主要场景 |
|------|-----------|---------|
| **AWS IAM Roles Anywhere** | AWS | EC2 / ECS / EKS workload 访问 AWS 服务 |
| **GCP Workload Identity** | GCP | GKE pod 访问 GCP 服务 / 跨云 |
| **Azure Managed Identity** | Azure | VM / App Service / AKS workload |
| **GitHub Actions OIDC** | GitHub | GitHub Actions workflow 访问云资源 |
| **Tailscale Workload Identity Federation** | 任意 | CI node 加入 tailnet |

## 为什么是 AI agent 时代的核心方案

### 1. 消除"凭据泄漏"攻击面

传统 long-lived auth key：
- 可以被复制到任意位置（agent 偷到后复制到外部沙盒）
- 可以被无限次使用（直到过期）

Workload identity federation：
- **没有可复制的凭据**——只有 workload-bound OIDC token
- 攻击者要使用必须**重新取得 workload 上下文**——这要求取得 cloud metadata endpoint

### 2. 时间窗口压缩

| 凭据寿命 | 攻击窗口 | agent 速度下得手概率 |
|---------|---------|-------------------|
| 1 年 | 1 年 | 100% |
| 1 天 | 1 天 | 100% |
| 1 小时 | 1 小时 | 高 |
| **5 分钟** | **5 分钟** | **低（需要持续入侵）** |

### 3. 自动清理

短生命周期 token 自动失效——**无残留凭据**。这与 "Make the safe path the easy path" 一致：用户无需管理凭据轮换。

## 与 Tailscale 的整合

Tailscale 收购 Border0 后，提供 `workload identity federation` 机制：

1. CI job 启动 container
2. container 向云 metadata endpoint 请求 OIDC token
3. Tailscale 验证 token（基于云签名）
4. Tailscale 授予该 workload 特定 tags + scopes
5. workload 在 tailnet 内有权限，但**没有可复制的 auth key**

**关键优势**：Hugging Face 入侵场景中，reusable auth key 被复制到外部沙盒使用——如果用 workload identity federation，攻击者**没有可复制的凭据**——必须重新取得 cloud workload 上下文。

## 前提与局限性

### 1. OIDC Trust Chain 本身可被攻陷

- IMDSv1（AWS metadata v1）允许 SSRF 攻击——攻击者通过服务器漏洞读取 metadata
- OIDC token 的接收方必须正确验证 issuer / audience / signature
- 多云/混合云的 trust chain 配置复杂

### 2. 实施成本

- CI/CD 平台需支持 OIDC（GitHub Actions 2022 后支持，但旧平台不支持）
- IAM 角色 / service account 需预先配置
- 失败回退路径往往回到 long-lived（违反安全原则）

### 3. 不是所有场景都适用

- 一次性本地开发环境（无 cloud identity）
- 物理服务器 / air-gapped 系统
- 部分 legacy 系统

### 4. Workload 身份本身的信任问题

如果 workload 所在 VM 被攻陷——agent 仍可使用其 identity。这要求 workload 本身有强隔离（与 [[Agent-Containment]] 互补）。

## 关键数据点

- AWS IAM Roles Anywhere、GCP Workload Identity、Azure Managed Identity 是三大云标准方案
- GitHub Actions OIDC token 自 2022 年开始支持
- Tailscale workload identity federation 基于 Border0 收购整合
- Hugging Face 入侵 2026 案例直接驱动 Tailscale 反思 "We should have done more"

## 关联概念

- [[Long-Lived-Credential-Risk]] — 本方案直接解决该风险
- [[Rogue-AI-Agent]] — 本方案是该威胁的核心防御
- [[Agent-Containment]] — 互补：workload 身份有效但 workload 被攻陷时无意义
- [[Agent-Harness]] — harness 应优先采用 workload identity 而非 auth key
- [[Coding-Agent-Security-Audit]] — DFD+VDF 应审计 workload identity 配置