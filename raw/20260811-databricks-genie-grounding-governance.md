---
type: raw
source: "https://www.databricks.com/blog/how-ground-genie-agents-both-structured-data-and-documents-without-losing-governance"
author:
  - "Doyoung Jung"
  - "Databricks"
published: "2026-08-10"
created: "2026-08-11"
description: "Databricks 官方博客，阐述 Genie Agents 如何同时 grounding 结构化数据与文档，治理契约通过 Unity Catalog 继承到 agent 而非堆在模型层。"
tags:
  - "clippings"
  - "agentic-engineering"
  - "agent-governance"
  - "databricks"
  - "unity-catalog"
  - "abac"
  - "row-filter"
  - "column-mask"
  - "structured-data"
  - "unstructured-data"
  - "enterprise-ai"
---

# How to ground Genie Agents in both structured data and documents without losing governance

> 类别: Best Practices | 发布: 2026-08-10 | 作者: Doyoung Jung (Databricks)
> 一句话核心: **Genie Agents run with the end user's credentials** — 治理在 catalog 层,不在模型层。

## Summary (官方)

- 将 Genie Agents grounding 在结构化数据 (Managed Tables / External Tables / Foreign Tables / Views / Metric Views / Materialized Views) 与非结构化文件 (Unity Catalog Volumes) 上,让单一 agent 跨全部数据作答。
- **Agent 治理位于 catalog 层而非模型层**。治理随 agent 一起扩展,不会失控。
- 借助 Automatic Identity Management (AIM)、Object Privileges、ABAC、Row Filters、Column Masks,Genie Agents 以用户身份运行,每个答案都按该用户的权限过滤。

## 核心论点:治理契约 (The Governance Contract)

**Genie Agents run with the end user's credentials**。Unity Catalog 默认强制治理,确保对表和 Volume 的访问直接绑定到最终用户既有身份与权限。

反对的常见反模式:**许多自研系统给 agent 宽泛访问,然后依赖 prompt 工程在模型层过滤结果**。这实际上把 LLM 变成安全边界——一个危险赌注,因为模型可被操纵或绕过。向审计员解释"我加了句指令说不许显示受限数据"不是可辩护的治理控制。

正确路径:**Unity Catalog,不是模型,是安全边界**。Genie 决定 _如何_ 查询数据,但它无法返回该用户无权看到的记录——每个答案在离开 Lakehouse 之前已在数据层被过滤。

## Step 0 — Identity: AIM + JIT 供应

治理可靠性只与身份评估的可靠性相当。

- **Automatic Identity Management (AIM)** (Microsoft Entra ID、Okta): 用户、组、组成员、服务主体自动同步进 Databricks,**无需 SCIM 应用**。
- **Just-in-Time 供应**: 用户首次登录即被供应,自动携带其既有的组成员关系。
- **四步流程**:
  1. IdP 是事实源 (某人加入 APAC sales org → IdP 把它放进 `brickstore_apac` 组)。
  2. AIM 同步进 Databricks,JIT 在用户首次打开 Genie One 时供应。
  3. Unity Catalog 策略基于这些组评估:object privileges、ABAC、row filters、column masks 都在查询时按组评估。
  4. 用户问 Genie Agent 问题,答案严格按组权限塑形,不多不少。

**收益是治理连续性而非快照**:员工从 APAC 转岗到 AMER,IdP 移动组,AIM 同步,他们下一个 Genie 问题返回的就是 AMER 视图——无需工单、无需改 Genie Agent。员工离职,IdP 停用,他们对所有 Genie Agent 的访问立即被移除。

## Step 1 — Grounding 结构化数据 + 四层访问控制

Genie Agent 可访问任何 Unity Catalog 数据资产:tables、views、materialized views、metric views、streaming tables、甚至 federated foreign tables。

### 四层访问控制

| Layer | 回答的问题 | 机制 |
|-------|------------|------|
| **Object Privileges** | 谁对什么资源有什么级别访问 | `GRANT SELECT` on catalog/schema/table |
| **ABAC** | 哪条策略应用到哪 | 由 governed tag 驱动,挂一次全局传播 (例:任何带 `pii` 标签的列只对某些组可见) |
| **Row filters** | 用户能访问哪些 _行_ | SQL UDF,查询时逐行评估 |
| **Column masks** | 哪些 _列_ 应被掩码及如何掩码 | SQL UDF,接收列值返回原值或掩码版 |

**关键观察**:行级与列级控制复用既有 grant 的组 (`is_account_group_member('brickstore_apac')`)。ABAC 不替代这些,而是**用策略而不是逐表**来附加同样的过滤与掩码。

### ABAC:定义一次,自动传播

老办法:每个表单独写 row filter / column mask,百张表即百次配置,易漏。

ABAC (GA in Unity Catalog,与 governed tags、自动数据分类配合): 给敏感数据打 governed tag (账号级、ACL 控制的 k/v,如 `pii:email`),写**一条策略**声明"凡此 tag 处皆应用此保护"。新表一旦打标即继承保护。

**保护整个 catalog 的所有 email 列 (mask + ABAC)**:

```sql
-- Masking UDF
CREATE FUNCTION brickstore.sales.mask_email(email STRING) RETURNS STRING
RETURN CASE
  WHEN is_account_group_member('brickstore_global') THEN email
  ELSE regexp_replace(email, '(^.).*(@.*$)', '$1***$2')
END;

-- ABAC Policy
CREATE POLICY mask_customer_email
ON CATALOG brickstore
COLUMN MASK brickstore.sales.mask_email
TO `account users`
FOR TABLES
MATCH COLUMNS has_tag_value('pii', 'email') AS email
ON COLUMN email;
```

**按区域 row filter + ABAC Policy**:

```sql
-- Row filter UDF
CREATE FUNCTION brickstore.sales.region_filter(req_region STRING) RETURNS BOOLEAN
  RETURN is_account_group_member('brickstore_global')
    OR (is_account_group_member('brickstore_apac') AND req_region = 'APAC')
    OR (is_account_group_member('brickstore_amer') AND req_region = 'AMER');

-- ABAC policy
CREATE POLICY restrict_by_region
ON SCHEMA brickstore.sales
ROW FILTER brickstore.sales.region_filter
TO `account users`
FOR TABLES
MATCH COLUMNS has_tag_value('geo', 'region') AS region
USING COLUMNS (region);
```

结果:APAC manager 查 orders → 只返 APAC 行 + 邮件掩码。AMER manager 查同一表 → 只返 AMER 行。

## Step 2 — 把同样治理延伸到文档

历史难题:文档往往在独立存储系统、由独立 ACL 管理,与结构化数据割裂。

**修复**:把文件放进同一个治理平面 — **Unity Catalog Volumes**。它们与表一样是 securable,可 `GRANT READ VOLUME`:

```sql
GRANT READ VOLUME ON VOLUME brickstore.sales.market_reports TO `brickstore_apac`;
GRANT READ VOLUME ON VOLUME brickstore.sales.market_reports TO `brickstore_amer`;
```

### Volume 的两个非显然行为

1. **附加的 Volume 是"必需源" (required source)**:agent 加载时会校验对每个附加源的访问,缺失 READ VOLUME 的用户根本无法使用该 agent。Volume 授权是使用 agent 的**前置条件**,所以要把每个 agent 的文档源 scope 到目标用户群。若两个用户群需要不同文档,可能需要给它们不同的 Genie Agents (各自挂载它们能读的 Volume)。
2. **Volume 是最小 securable 单位**:权限作用于整个 volume 而非单个文件,不能挑文件分享——要么整个 volume,要么没有。

### 支持的文档格式 (Volumes)

- PDF
- 图像 (JPG, JPEG, PNG, TIFF, TIF)
- Office (DOC, DOCX, PPT, PPTX)
- 纯文本、Markdown

实战含义:扫描的合同、PPT、spec 都能用,不只是干净的 PDF。

### Volume 配置的最佳实践

- **加清晰的描述**:不要用泛指占位符。比如不要写"regional files",而是写"APAC market report — demand drivers, trends, and watch items for the APAC region"。Genie 依赖描述来选对 volume。
- **避免重复内容**:多个 volume 包含重叠信息会让检索变难。volume 内的文件也适用。
- **避免无关文件**:只放与 agent 领域相关的文件,无关文件会迷惑 agent。
- **用清晰的文件名**:让 agent 能区分文件。

## Step 3 — 生产中的 Genie Agents:同样问题,不同答案

两个 manager 都问同样的问题:
> "Which product is our top seller this quarter and what's driving that demand? Also list the top customers behind those sales and their emails."

两人同属不同组 (`brickstore_apac` vs `brickstore_amer`)。基于同一份资产 (`orders` 表、`products` catalog、`market_report` Volume) 启动并发的 Genie Agent 会话。

### 值得指出的三件事

1. **数字不同,两都正确**。"top-selling bricks" 都从同一张表拉数据,差异纯粹是各有权访问的行——不是指标计算口径不同。
2. **零 per-user prompt engineering**。没人写"if user is APAC, hide other regions"。agent 的指令对所有人一致,Unity Catalog 在查询时做行级 + 列级过滤。邮件列被自动掩码保护 PII。
3. **结构化数据由非结构化知识增强**。没有区域文档,Genie 能答 "what",但难以解释"什么在驱动需求"。加上非结构化数据,Genie 拥有完整业务上下文。

## Patterns to Watch for

- **先 tag,后 policy。不要逐表掩码**。本能是给眼前三张表加保护——克制它。定义 governed tags 和 ABAC policies,让数据治理面向未来。
- **每个 volume 一个受众**。因为 volume 是最小授权单位,在 volume 边界决定文档访问。如果两个文档需要不同读者,它们需要不同 volume 和不同 Genie Agents——前置规划布局。
- **通过 MCP/API 对外暴露 Genie One 或 Genie Agents 时,小心处理身份**。与 UI 内运行不同,你并不总能获得 end-user 身份 (例:使用 Service Principal 鉴权)。Databricks 在 [Access Genie everywhere](https://www.databricks.com/blog/access-genie-everywhere) 中详述 U2M、M2M、OBO 配置。
- **通过 impersonation 测试,不是通过 inspection 测试**。不要读策略说服自己它对——以每个组成员身份问同一问题并对比响应。把它做成回归测试,策略或分组变化时跑一遍。

## The Takeaway

构建 agent 可以很容易,但治理需要真正的设计工作。在 Databricks:

- 企业身份从 IdP 同步
- object privileges 把守访问
- ABAC 和 governed tags 规模化应用保护
- row filters 和 column masks 控制返回内容
- 文档与数据在同一系统

此设置下,Genie Agents **零额外配置**继承所有治理。

## 参考链接

- [Genie documentation](https://docs.databricks.com/aws/en/genie/)
- [ABAC policies documentation](https://docs.databricks.com/aws/en/data-governance/unity-catalog/abac/)
- [Automatic Identity Management](https://docs.databricks.com/aws/en/admin/users-groups/automatic-identity-management/)
- [Genie Agents volumes documentation](https://docs.databricks.com/aws/en/genie-agents/volumes)
- [ABAC launch blog](https://www.databricks.com/blog/abac-row-filtering-and-column-masking-policies-governed-tags-and-data-classification-are-now)
- [Access Genie everywhere (身份与外部暴露)](https://www.databricks.com/blog/access-genie-everywhere)