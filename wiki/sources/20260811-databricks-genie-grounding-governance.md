---
type: source-summary
title: "How to ground Genie Agents in both structured data and documents without losing governance"
source_raw:
  - "[[20260811-databricks-genie-grounding-governance]]"
created: 2026-08-13
updated: 2026-08-13
tags:
  - source-summary
  - agent-governance
  - grounding
  - enterprise-ai
  - identity
evidence_level: low
claim_type: mixed
---

# How to ground Genie Agents in both structured data and documents without losing governance

> 来源与证据定级：Doyoung Jung（Databricks）2026-08-10 官方博客，厂商最佳实践类内容。取 `low`：单源（Databricks 官方）、营销/产品叙事（Genie/Unity Catalog/ABAC 皆其产品）、无独立评估或对照组；但其机制描述（row filter / column mask / volume 授权 / AIM 身份同步）具体且与技术事实可核对，故 claim_type 为 `mixed`。

## 编译摘要

### 1. 浓缩

- **核心结论1：Agent 治理契约（Governance Contract）应放在数据层（catalog），而非模型层——"Unity Catalog，不是模型，是安全边界"。**
  - 关键证据：Genie Agents 以终端用户凭证运行；object privileges / ABAC / row filters / column masks 在查询时按用户组逐行逐列过滤，每个答案离开 Lakehouse 前已在数据层被过滤。反模式：给 agent 宽泛访问、靠 prompt 在模型层过滤结果——"向审计员解释'我加了句指令说不许显示受限数据'不是可辩护的治理控制"。SQL 示例（mask_email UDF + ABAC policy `MATCH COLUMNS has_tag_value('pii','email')`；region_filter + ABAC）。
- **核心结论2：身份是治理可靠性的地基——AIM（Automatic Identity Management）+ JIT 供应让治理成为连续性而非快照。**
  - 关键证据：IdP 是事实源（Entra/Okta 同步用户/组/成员，无需 SCIM）；员工转岗（APAC→AMER）或离职自动反映到下一次 Genie 查询，"无需工单、无需改 Genie Agent"。
- **核心结论3：结构化数据与非结构化文档纳入同一治理平面（Unity Catalog Volumes），文档授权成为使用 agent 的前置条件。**
  - 关键证据：Volume 与表同为 securable（`GRANT READ VOLUME`）；附加的 volume 是"必需源"（缺 READ VOLUME 的用户无法使用该 agent）；volume 是最小 securable 单位（不能挑文件授权）→ 设计原则"每个 volume 一个受众"；文档格式覆盖 PDF/Office/图像/Markdown。

### 2. 质疑

- **关于"catalog 即安全边界"的质疑**：Databricks 厂商博客，主张直接服务于其产品（Unity Catalog/ABAC/Genie）叙事；未与"模型层 guardrail + 最小权限 agent 身份"方案做对照基准，"catalog 是唯一安全边界"是架构主张而非实证结论。
- **关于身份依赖的边界**：作者自认"治理可靠性只与身份评估的可靠性相当"；外部暴露（MCP/API）场景下不一定能获得 end-user 身份（Service Principal 鉴权时），需 U2M/M2M/OBO 特殊处理——"以用户凭证运行"并非处处成立。
- **关于表达力上限**："零 per-user prompt engineering"隐含假设所有权限语义都可用 row filter / column mask / governed tag 表达；复杂动态规则（依赖查询内容的上下文敏感控制）与性能成本（逐行 SQL UDF）未给出基准。
- **关于粒度成本**：volume 作为最小授权单位带来前置规划负担——不同受众需不同 volume + 不同 Genie Agent，agent 数量与运维成本随权限分化上升。
- **关于验证方式**：作者建议"通过 impersonation 测试，不是通过 inspection 测试"——承认策略正确性难以静态审阅，需以各组身份实际查询对比响应（回归测试），间接承认配置复杂性与出错面。

### 3. 对标

- **跨域关联1（身份模式的两种极）**：Genie"继承终端用户凭证"与 [[Distinct-Principal-Identity]]"独立 agent 身份"是防止过权的两种相反实现——前者信任继承 + 数据层过滤，后者信任隔离 + 最小权限上限；选型取决于能否可靠获得 end-user 身份（综合判断）。
- **跨域关联2（策略即代码）**：ABAC policy + governed tags 即 [[Policy-as-Code-for-Agent-Governance]] 在数据目录层的实现——执行点不在 agent runtime 而在数据层，策略随 agent 扩展自动传播（综合判断）。
- **跨域关联3（信任面收缩）**：把安全边界下沉到数据目录层，缩小 agent 的信任面——与 Zero Trust 思想（不再默认信任、每请求按身份评估）同构；Agent 只负责"如何查询"，不负责"能否看到"（综合判断）。
- **跨域关联4（AI-ready 前提）**：该模式要求组织先具备身份同步、数据打标（governed tags）、数据资产盘点——正是 [[AI-Ready-Organization]]"数据基础是第一优先级"的落地形态（综合判断）。

### 关联概念

- [[Policy-as-Code-for-Agent-Governance]]
- [[Distinct-Principal-Identity]]
- [[AI-Ready-Organization]]
- [[Custom-Policy-Guardrails]]
- [[Agent-Verification]]
- [[Ontology]]
- [[Knowledge-Graph]]