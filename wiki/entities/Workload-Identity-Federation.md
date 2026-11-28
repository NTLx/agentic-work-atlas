---
type: entity
title: "Workload Identity Federation"
aliases:
  - Workload Identity Federation
  - Workload Identity
  - 工作负载身份联邦
  - OIDC Federation
definition: "通过预配置的信任关系将工作负载身份换取目标服务的受限凭据；OIDC 是常见实现，可减少静态长期密钥依赖，但不等于消除短期凭据泄漏风险。"
created: 2026-08-01
updated: 2026-11-28
evidence_level: medium
claim_type: mixed
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
> **Workload Identity Federation** 通过预配置的跨信任域身份关系，将工作负载的可信身份换取目标服务的受限凭据。OIDC 是常见实现，而非唯一身份机制。减少长期静态密钥不等于消除可复制凭据、重放或工作负载失陷风险。

## 工作机制（OIDC 型）

1. 管理者配置可信 issuer、audience、subject/claim 匹配及目标权限。
2. 工作负载从自己的身份提供方取得签名身份 token（获取机制依平台而异，不一定经过 metadata endpoint）。
3. 目标服务验证签名、issuer、audience、有效期及身份匹配规则，签发受限的短期 access token。
4. 资源侧持续执行授权；分别管理原身份、交换所得 token、续期及已建立会话/节点的生命周期。

## 实现辨析

- GitHub Actions OIDC：workflow job 获取身份 JWT，向支持 OIDC 的云服务换取短期凭据。
- Tailscale WIF：身份 JWT 换取配置了 scope 的 API token；可以用于加入或管理 tailnet，权限与节点生命周期须分别核查。
- GCP Workload Identity、Azure Managed Identity：相关的工作负载身份机制，具体凭据交换与身份映射依部署而异。
- AWS IAM Roles Anywhere：相关但非同一 OIDC 流程；使用受信 CA 签发的 X.509 证书获取临时 AWS 凭据，主要面向 AWS 外部工作负载。

技术勘误依据（2026-11-28 核对产品文档）：[Tailscale WIF](https://tailscale.com/docs/features/workload-identity-federation)、[GitHub Actions OIDC](https://docs.github.com/en/actions/concepts/security/openid-connect)、[AWS IAM Roles Anywhere](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/introduction.html)。文档是机制说明，不是攻击防御有效性的独立实证。

## 风险收益与剩余风险

- 减少静态密钥的分发、存储和长期重用；可限制身份来源、权限和凭据有效期。
- 签名 JWT 的身份声明不等于持有者绑定。若使用 bearer 凭据，泄露后仍可能在有效期及目标服务约束允许的范围内被重放；sender-constrained 或硬件绑定需要额外机制。
- 短时效缩小单次凭据的有效窗口，不提供固定得手概率，也不自动限制已造成的效果；可持续续期、已建立会话、已注册节点可能具有不同生命周期。
- Tailscale 厂商反思中的 reusable auth key 可被复用是具体暴露路径。WIF 可移除对该静态 key 的依赖，但不能从反事实推断该入侵必然被阻止。

## 前提与局限性

### 1. OIDC Trust Chain 本身可被攻陷

- IMDSv1（AWS metadata v1）允许 SSRF 攻击——攻击者通过服务器漏洞读取 metadata
- OIDC token 的接收方必须正确验证 issuer / audience / signature
- 多云/混合云的 trust chain 配置复杂

### 2. 实施成本

- 需要受信身份提供方、交换端与权限配置；旧系统可能缺少相应支持
- IAM 角色 / service account 需预先配置
- 失败回退路径往往回到 long-lived（违反安全原则）

### 3. 不是所有场景都适用

- 一次性本地开发环境（无 cloud identity）
- 物理服务器或隔离网络可能需要本地 PKI/身份服务；不能仅因部署不在公有云就排除联邦
- 部分 legacy 系统

### 4. Workload 身份本身的信任问题

如果 workload 所在 VM 被攻陷，且攻击者取得相应身份调用能力，则仍可能使用其 identity。这要求 workload 本身有强隔离（与 [[Agent-Containment]] 互补）。

## 关键数据点

- 上述平台是编译时的技术对标，并非 Tailscale 事故反思正文逐项列举；不同机制不可混为一种协议。
- Tailscale 原文称其 workload identity federation 使用云端 ambient authority；具体 issuer、audience、签名验证和权限映射仍须按部署配置核实。
- Hugging Face 入侵是 Tailscale 反思的案例背景；它支持“可复制长期凭据扩大暴露面”的案例判断，不证明 workload identity federation 能阻止所有同类入侵。

## 关联概念

- [[Long-Lived-Credential-Risk]] — 本方案可降低静态凭据暴露风险
- [[Rogue-AI-Agent]] — 本方案是凭据层的候选防御
- [[Agent-Containment]] — 互补：工作负载被攻陷时仍需限制可达权限、续期与影响范围
- [[Agent-Harness]] — harness 应优先采用 workload identity 而非 auth key
- [[Coding-Agent-Security-Audit]] — DFD+VDF 应审计 workload identity 配置
