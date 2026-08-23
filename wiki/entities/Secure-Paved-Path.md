---
type: entity
title: Secure-Paved-Path
aliases:
  - Secure Paved Path
  - 安全铺装路径
  - Paved Path Security
definition: "把安全控制嵌入默认开发路径的平台策略：让安全的方式成为最容易的方式，开发者无需主动选择即获得签名、隔离与 provenance，绕过比遵守更难"
created: 2026-07-30
updated: 2026-08-24
tags:
  - software-engineering
  - security
evidence_level: medium
claim_type: mixed
related_entities:
  - "[[Operational-Responsibility]]"
  - "[[Agent-Verification]]"
  - "[[Constraint-Infrastructure]]"
source_raw:
  - "[[20260730-palantir-secure-rapid-software-development-sscs]]"
---

# Secure-Paved-Path（安全铺装路径）

> [!definition] 定义
> **Secure Paved Path** 是把安全控制嵌入默认开发路径的平台策略——在所有仓库与构建上保证安全控制默认在场（guard rails on paved paths），使安全的方式成为最容易的方式。它来自 Palantir 的 SSCS（Software Supply Chain Security）实践：威胁模型先行量化风险，再用 paved path 把高影响控制变成默认值而非可选项。

## 方法论序列：威胁模型先行

SSCS 项目的启动顺序不是"买工具"或"过合规"，而是：

1. **描绘代码流的 ground truth**：从开发者 → 源码控制 → 构建系统 → 打包 → 生产的完整流动图。难点不在绘图，而在组织考古——多年高速发展留下多套重复的开发路径（Palantir 10K repos 的 GitHub Enterprise 实例即此规模）。
2. **按区块定义风险**：五个核心区块——Source Control & Software Design / Third-Party Dependencies / Builds & Artifact Publishing / Artifact Storage / Artifact Deployment。
3. **按风险分配资源**：安全资源有限，威胁模型决定投向何处。
4. **共享所有权**：邀请跨业务工程师参与威胁模型评审，使安全目标成为开发组织的共同财产而非中心团队的审计清单（与 [[Operational-Responsibility]] 的 "editing, not authoring" 同构）。

威胁假设取最高档：APT（零日、社工、人力招募、近距离渗透、供应链攻击）+ assume breach（所有设备视为可能已被攻陷）。

## 关键机制

- **Hermetic builds**：构建仅依赖显式声明的输入——把隐式依赖转为显式 provenance。与 agent 安全中"tool 调用依赖显式 authorization grants"同构。
- **端到端 provenance**：每个 artifact 可追溯到代码 + 构建环境 + 构建者；commit 加密签名保证真实性、完整性、不可否认性；安全敏感操作硬件加密签名。
- **最小权限覆盖全环境**：源码控制、构建、部署系统一体适用。
- **临时构建节点**：每次构建使用全新环境（ephemeral CircleCI nodes），消除构建环境的状态污染。

## Config-as-Code 双刃剑

> [!warning] 规模化传播是风险放大器
> 10K repos 用中央 config-as-code 仓库管理：一行 YAML 改动即可批量推送仓库配置（含安全控制开关）。这既是 paved path 的分发机制，也是最大的单点风险——"Security was not a primary consideration in the development of most of these tools because they were built to reduce friction at all costs"。内部效率工具的安全债往往是 SSCS 项目的主要清理对象。**推论：规模化传播安全控制的工具，本身需要最高等级的变更治理（多人 review + 金丝雀推送 + 回滚审计）。**

## 防御形态学定位：活墙实例（08-24 圆桌，synthesized/medium）

> 开放域防御定价定理（[[research-agenda]] 97 行）的形态学二分：墙 = 遗骸形态（便宜可展示可表演）、市场 = 活体形态（定价/限责/要求对手方结算）。本实体按该框架定位 **paved path = 工具链默认值形态的"墙"**，但 **08-24 形态学二分破产裁决修正此定位**——墙不必然死，真变量 = 结算通道开放度 × 重构密度。

- **paved path 是"墙"而非"市场"的证据**：防护价值内嵌默认路径（开发者无选择即获得），非由外部对手方定价结算——采用成本零（工具链默认值），展示性强（安全报告可视）。
- **它是活墙的证据（重构密度高）**：SSCS 的存活因素正是"被击打且击打被记录"——威胁模型先行（按区块量化风险并随组织考古重绘 ground truth）+ 威胁假设取最高档（APT + assume breach）意味着墙持续在被真实威胁重新审视；Hermetic builds / provenance 每次构建都被显式校验。这不是墙不被质疑，是墙每轮构建都在接受挑战。
- **墙的失效面 = 漂移对象（接三对象修正）**：paved path 防的是"决策对象"（开发者走错路）；它的漂移对象是**安全松弛的正常化**——成本压力下把 guardrail 调松一档、把"临时豁免"变成常态；形状对象是 **config-as-code 本身被攻破** → 一行 YAML 批量下发 = 攻击者借墙放大伤害（与 Config-as-Code 双刃剑节直接衔接）。
- **推论**：paved path 要长期存活，处方 = 保持重构密度（威胁模型定期重绘 + 金丝雀推送 + 变更治理）+ 对 config-as-code 这一单点用最高等级变更治理（见上节警告）——这正是"活墙"的组织形态。

来源：08-24 圆桌（[[research-agenda]] 新判断行「开放域防御三对象 + 锚对手无关性」）。

## 关键数据点

- Palantir 规模：10K repos / GitHub Enterprise 实例
- 五大风险区块：Source Control & Software Design / Third-Party Dependencies / Builds & Artifact Publishing / Artifact Storage / Artifact Deployment
- 威胁假设取最高档：APT（零日、社工、人力招募、近距离渗透、供应链攻击）+ assume breach
- Hermetic builds：构建仅依赖显式声明的输入；commit 加密签名
- Config-as-code 双刃剑：一行 YAML 改动可批量推送仓库配置

## 前提与局限性

- **资源预设**：Palantir 方案含"拒 SaaS + 全自托管 + FedRAMP/IL5/IL6"，预设军工级工程资源与合规要求；对多数组织，云厂商安全投入高于自建，"自托管更安全"不成立。
- **总纲局限**：原始文献为系列第一篇，8 条程序目标均为应然清单，实现细节在后续篇目。
- **适用域**：paved path 的价值随仓库/团队规模上升；小规模组织中默认路径可由文化维持，不需要平台化。

## 关联概念

- [[Operational-Responsibility]] — 安全共享所有权与生产共享所有权同构
- [[Constraint-Infrastructure]] — paved path 是约束基建在人类开发流程中的形态
- [[Agent-Verification]] — hermetic/provenance 原则迁移到 agent 产物验证
