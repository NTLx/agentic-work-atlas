---
type: raw
source: "https://blog.palantir.com/how-palantir-enables-a-secure-rapid-software-development-environment-2f918b021568"
title: "How Palantir Enables a Secure, Rapid Software Development Environment (Software Supply Chain Security, #1)"
author:
  - "Palantir"
published: 2024-11-12
created: 2026-07-30
description: "Palantir 官方博客（2024-11-12，6 分钟阅读，Software Supply Chain Security 系列第一篇）。⚠️ Vendor 立场：Palantir 是 SSCS 实践者 + SSCS 工具（Apollo）供应商，但本篇内容以威胁建模方法论为主，机制层可独立验证；产品叙事（'natively supported by our very own products'）需打折。核心机制：SolarWinds 2020 攻击后启动 SSCS 项目，从 'move fast and break things' 转向 'move fast and secure things'。威胁模型假设 APT（含零日、社会工程、人力招募、近距离渗透、供应链攻击），并假设网络已被渗透（'assume all devices are potentially hostile or compromised'）。基础设施三原则：(1) 拒 SaaS——自行托管以避免上游 SaaS 厂商被攻陷；(2) 合规——FedRamp/IL5/IL6 自托管确保 SDLC 安全合规；(3) 监控——内部基础设施可全面埋点零信任技术。核心组件栈：GitHub Enterprise（源码）+ CircleCI 临时节点（构建）+ Artifactory（制品）+ Apollo（部署）。规模化工程：10K repos 的 GitHub Enterprise 实例用 config-as-code 中央仓库管理，一行 YAML 改动即可批量推送仓库配置（含安全控制开关），速度快但 risk surface 也大。SSCS 威胁模型 5 个核心区块：(1) Source Control & Software Design；(2) Third-Party Dependencies；(3) Builds & Artifact Publishing；(4) Artifact Storage；(5) Artifact Deployment。SSCS 程序目标 8 条：(a) 多层防御恶意代码注入；(b) review 所有软件的安全架构；(c) 所有 commit 加密签名（真实性+完整性+不可否认性）；(d) 安全敏感操作硬件加密签名（git commit / SSO 登录）；(e) 'paved paths' 默认安全控制（即平台默认安全，开发不能轻易绕过）；(f) 最小权限原则覆盖所有环境；(g) 构建环境充分硬化 + 隔离，目标是 hermetic builds（构建仅依赖显式声明的输入）；(h) 端到端 provenance（每个 artifact 可追溯到代码+构建环境+构建者）。结论：先建威胁模型量化风险→再决定资源分配→团队共享所有权是规模化 SSCS 的关键。"
tags:
  - clippings
  - palantir
  - supply-chain-security
  - sscs
  - devsecops
  - zero-trust
  - software-engineering
---

# How Palantir Enables a Secure, Rapid Software Development Environment (Software Supply Chain Security, #1)

*Palantir · Palantir Blog (Medium) · 2024-11-12 · 约 6 分钟阅读 · Software Supply Chain Security 系列 #1*

---

*Editor's Note: This is the first post in a series that shares insights from our journey to enhance our software supply chain security story at Palantir. This post provides background on why and how we initiated our Software Supply Chain Security (SSCS) program, and focuses on the threat model behind our security controls and posture.*

## Introduction

Palantir's competitive advantage has always been its ability to rapidly adapt and build software solutions for complex, impactful, real-world problems. This requires a development culture that moves fast and can pivot rapidly. However, moving quickly comes with risks. At Palantir, given our mission, scope of work, and set of customers, we are acutely aware of this. The most advanced and persistent adversaries in the world target us.

So, how do we enable developers to be effective and secure?

In this blog post series we'll break down how we transitioned from the well-known motto of "move fast and break things" to "move fast and secure things." We'll explore how we evolved from a nascent understanding of our software supply chain to building out a cutting-edge Software Supply Chain Security (SSCS) program that is natively supported by our very own products.

## Threat Environment

Palantir operates in a challenging threat environment that requires security-by-design at the core of every major initiative. We are routinely targeted by sophisticated and persistent adversaries who are highly motivated to attack western democracies, financial systems, and other critical infrastructure.

As a company known for handling the sensitive data of many Western nations, including intelligence and military organizations, we must threat model against advanced persistent threats (APTs). This includes well known nation-state actors as well as criminal groups. As part of our threat model, we assume an attacker would leverage advanced tactics, techniques, and procedures (TTPs), including zero-day exploitation, social engineering, human asset recruitment, close access, supply chain attacks, and other sophisticated methods.

Like many organizations, some of the greatest risks we face are software supply chain attacks. These may target software providers, upstream libraries we rely on, or us directly as a nexus point to reach our customers. Given the frequency and severity of supply chain-based attacks, our threat environment has necessitated we implement solutions that are at the bleeding edge.

## Our Infrastructure

Palantir has embraced zero-trust, defense-in-depth, and assume breach mentalities. We strongly believe in hardened, well-defined network boundaries that constrain adversaries' ability to operate. From a network access perspective, we do not allow connectivity to the vast majority of our corporate resources from the general Internet. Instead, we require our devices to first connect to our network via a full-tunnel virtual private network (VPN) authenticated via our SSO passwordless login. We also believe that our adversaries will find beachheads into these networks, and therefore design our security controls to assume all devices are potentially hostile or compromised.

To enhance our monitoring abilities, enforce security controls, and build forward-looking security solutions unavailable in the current market, Palantir relies on internally hosted infrastructure for our secure software deployment lifecycle. This approach offers three major benefits:

1. **Reduced Breach Likelihood via Upstream Vendor Compromise**: We are not reliant on software-as-a-service (SAAS) platforms, making us more resilient to their potential compromise.
2. **Security and Compliance Requirements**: Running our own FedRamp/IL5/IL6 accredited environments ensures our secure software development lifecycle meets all security and compliance requirements.
3. **Enhanced Security Monitoring and Zero-Trust Technologies**: We can instrument all our infrastructure with advanced security monitoring and zero-trust technologies.

### Key Components

Palantir's software supply chain infrastructure includes several key components. Our **source code** repositories are stored on GitHub Enterprise (GHE). **Software builds** are conducted on ephemeral CircleCI nodes, ensuring a fresh environment for each build. The resulting **software artifacts** are stored in Artifactory, providing a secure and organized repository for all our build outputs. Finally, Palantir Apollo is used for **continuous deployment** and application management, enabling seamless and secure deployment of our software.

### Threat Modeling the Software Supply Chain

Before modern software supply chain frameworks like SLSA, S2C2F, or P-SSCRM, there was the 2020 SolarWinds hack. Palantir's CISO moved quickly to establish the ground truth of our development process and existing security controls. To identify the right controls, we needed to understand where we held risk. Unfortunately, many years of high-speed development, intense growth, and ever-expanding product scope left us with a disparate set of approved development paths supported by various teams duplicating maintenance, infrastructure, security controls, and processes.

Getting the ground truth involved numerous meetings, interviews, document revisions, and diagram updates, which left us with a still flawed understanding of what our development teams were doing.

We started by creating a threat model diagram illustrating the flow of code from a developer, to source control, to the build system, packaging, and finally to production. This seemingly simple concept was complicated by reality: we had built our own development tools to optimize for internal workflows and our internal advanced deployment system. Understanding these tools and systems, and how they were used in practice versus their original intended use, was a significant undertaking.

For example, with 10,000 repositories in our GitHub enterprise instance, our developer tools team built out a solution to apply repository configurations at scale from a central configuration-as-code repository. Instead of manually configuring each repo via the GitHub UI to enable a required status check on protected branches, we could make a one-line YAML file change in our central repository, and that change would propagate across any desired set of repositories. This tool is incredibly powerful and enables us to move quickly, but it also introduces significant risks, such as the potential to disable a security control at scale. Security was not a primary consideration in the development of most of these tools because they were built to reduce friction at all costs.

Figuring out the reality of how these tools were used and what the secure version should be was an iterative process. The threat model focused on five core areas of our software supply chain:

1. Source Control & Software Design
2. Third-Party Dependencies
3. Builds & Artifact Publishing
4. Artifact Storage
5. Artifact Deployment

We defined risks and proposed mitigating controls for each area, aiming to prevent a SolarWinds-type breach. Once the software supply chain diagram was created, we invited partners from across the business to share risks and possible security solutions based on their view of the world. This process was immensely helpful for two reasons. First, it created buy-in by establishing a shared understanding of the need to increase security in our supply chain. Second, it brought in engineers from across the business who had ground-truth insights into development activities and could share ownership of possible solutions. We uncovered many inconsistencies and challenges, helping us focus on high-impact security controls. These controls serve as the foundation for our SSCS program, enabling us to build software securely by default.

### SSCS Program Objectives

Based on our software supply chain threat model, we defined the following objectives for our SSCS program:

* Provide multiple layers of defense against the injection of malicious code into our supply chain.
* Review the security architecture of all software we produce to ensure secure-by-design principles.
* Ensure all source control commits are cryptographically signed guaranteeing authenticity, integrity, and non-repudiation of our source control.
* Use hardware-backed cryptographic signing for security-sensitive operations (e.g., git commit signing, SSO login).
* Implement guard rails on paved paths to guarantee security control presence for all development source control repositories and builds.
* Apply the principle of least privilege to all environments, including source control, build, and deployment systems.
* Sufficiently harden and isolate all build environments with an aim of achieving hermetic builds.
* Require end-to-end provenance for all software artifacts produced to guarantee the authenticity and integrity of our software supply chain.

In upcoming posts in this series, we'll break down some of these objectives and the security solutions we implemented to achieve them.

## Conclusion

Given that security resources are limited, it is crucial to prioritize high-impact, high-conviction projects. Beginning with a threat model to quantify risk and gain a comprehensive understanding of the software supply chain is essential for appropriately resourcing the weak areas in your software development lifecycle (SDLC). As software supply chain attacks become more prevalent and complex, having a robust foundation to build upon is critical. Additionally, fostering a development organization that shares ownership in achieving security goals ensures that everyone is aligned and committed to maintaining a secure environment.