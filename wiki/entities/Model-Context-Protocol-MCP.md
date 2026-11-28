---
type: entity
title: Model Context Protocol (MCP)
aliases:
  - MCP
  - Model Context Protocol
definition: "让 AI client 通过统一客户端-服务器协议连接工具和数据源的开放标准，用来替代模型与工具之间的一对一硬编码集成"
created: 2026-05-13
updated: 2026-11-28
tags:
  - AI-Agent
  - tool-use
evidence_level: medium
claim_type: mixed
related_entities:
  - "[[MCP-Registry]]"
  - "[[Pinterest-Engineering]]"
  - "[[Harness-Engineering]]"
  - "[[Context-Engineering]]"
  - "[[Tool-Use-Architecture]]"
source_raw:
  - "[[20261110-latentspace-resend-designing-for-agents]]"
  - "[[Building an MCP Ecosystem at Pinterest]]"
  - "[[20260718-bytebytego-mcp-vs-a2a-vs-acp]]"
  - "[[20260805-how-we-use-ai-cloudflare-os]]"
  - "[[20260925-databricks-spglobal-genie-mcp]]"
---

# Model Context Protocol (MCP)

## Resend Remote MCP：工具列表规模背后的 API、OAuth/RBAC 与产品责任（2026-11）

[[20261110-latentspace-resend-designing-for-agents]]（**37:55–46:29**）记录 Resend 从投资者相关人员构建的本地开源 MCP，演进为官方 Remote MCP 的实际前提：为所有资源补齐 OAuth、RBAC、授权、审计可观测，并争取客户端官方入口。Resend 曾让 Dashboard 的私有 API 与公开 API 分叉维护，访谈认为共享 headless backend 是长期较好的结构；访谈时 80+ 命名工具试图覆盖 usage、billing、invite、provision 等长尾行为，但 Contacts 结果过大暴露了独立于工具数量的上下文问题。主持人与 Cloudflare Code Mode 的少量 search/execute 工具作对比，**不是性能测评**。

- **判断（综合）**：MCP 是产品 API 和用户权限的投影层；先定义唯一业务契约和不同用户的真实资源权限，再提供 CLI/UI/MCP。可操作性与可授权性必须分开：删除、账单、管理员动作另设角色/确认和持久审计。工具数量、schema 成本、返回负载、成功率与模型版本在任务级测试中联合衡量。
- **证据**：[[20261110-latentspace-resend-designing-for-agents]]（40:11–46:29）。
- **边界**：访谈强调官方供应商维护更可信，但不意味着所有第三方 MCP 都不可信；80+ tools 有增长也不证明其比 Code Mode 设计更高效。



> **核心洞察**：MCP 是 AI 时代的“USB 接口”，它标准化了工具与模型之间的连接方式。

> [!definition] 定义
> Model Context Protocol (MCP) 是让 AI client 通过统一客户端-服务器协议连接工具和数据源的开放标准，用来替代模型与工具之间的一对一硬编码集成。

## 为什么重要

MCP 的核心价值不是“多一个 API 标准”，而是把 agent tool use 从临时集成变成可治理基础设施。没有标准协议，每个模型、IDE、chat surface 和内部系统都要写一套连接逻辑；有了 MCP，工具提供方可以通过 server 暴露能力，消费方可以通过 client 发现、连接和调用。

但 Pinterest 案例也说明，协议只解决连接问题，不自动解决生产问题。进入企业后，应按风险落实身份、授权、安全审查与可观测性；[[MCP-Registry]]、人工确认和领域特定 server 是可选的实现路径，不是协议或所有部署的必要条件。

## Pinterest 的实践模式

[[Pinterest-Engineering]] 在其生产环境中应用了 MCP，并总结了以下关键架构选择：

1. **云端托管 (Cloud-hosted)**：不同于本地 stdio 模式，Pinterest 把生产路径优化为内部云托管 MCP servers，以便实施集中路由、安全审计、身份校验、部署和负载管理。
2. **领域特定服务器 (Domain-specific Servers)**：不使用单一巨型服务器，而是为 Presto、Spark、Airflow、Knowledge 等领域建立独立小型 server。
3. **中心注册表 (Registry)**：把 server approval、tool discovery、安全姿态、live status 和用户授权放到同一个治理层。
4. **接入日常 surface**：MCP 不只在实验环境中运行，而是进入内部 Web Chat、IDE integration 和内部聊天机器人，让 agent 在员工实际工作场景中调用工具。

这些选择说明：企业 MCP 的重点不是连接数量，而是最小权限、上下文清洁度和工具 owner 责任。

## Cloudflare 的治理强化案例（08-06 补充）

Cloudflare Cloudflare OS（CIO Sam Rhea, 2026-08-05，来源 [[20260805-how-we-use-ai-cloudflare-os]]）用 MCP 连接内部系统记录，但强调**自建以控权限**：

1. **自建 MCP server 即使有原生版**："In most cases, we build and deploy our own implementation of an MCP server for each system of record, even when the system of record provides a native version." 理由：可加额外控制层，如按角色/地区限流（rate limits by role or region）。Cloudflare Workers 提供 serverless 部署，维护负担近零。
2. **MCP Portal 做会话权限映射**：MCP 标准只定义"连接"，权限语义由 Portal 落地——用户会话在 Cloudflare OS 的访问 scoped 到其在系统记录里的既有权限集（follow our rule around permissions）。
3. **与 Pinterest 的互补**：Pinterest 强调中心化 [[MCP-Registry]]（哪些 server 被批准、谁能访问）；Cloudflare 强调"自建 MCP server 加权限控制层"——在连接层就落地最小权限，而非依赖单个系统记录的原生实现。

**可迁移内核**：区分能力发现与实际授权/执行。注册表及自建控制层是两家企业选择的实现方式；若原生服务或网关已满足同等权限、限流与审计要求，不必重复自建。

## MCP 作为组合层：窄语义服务，宽业务入口（2026-09）

S&P Global Energy 的 Databricks/Genie 架构（[[20260925-databricks-spglobal-genie-mcp]]）给 MCP 增加了一个此前 Pinterest / Cloudflare 案例较弱的角色：**composition contract**。

底层不是一个巨型 MCP server，而是多个 dataset-group 级 Genie Agent，每个 Agent 保持窄业务语义；上层 FastMCP proxy 用 namespace 把多个 server 组合成 commodity 或跨 commodity endpoint。消费者只需要连接较少的复合入口，而 LLM 在工具层做 route / fan-out。

**判断**：MCP 的企业价值可以分成三层：

1. **连接标准**：client 不必为每个数据服务重新实现协议；
2. **治理投射**：MCP endpoint 继承已有 auth / permission / audit；
3. **组合边界**：在不合并底层语义模型的前提下，把多个窄服务组成更宽业务能力。

第三层尤其重要：**协议组合可以扩大可达面，而不要求先把所有 domain ontology 合并成一个大 Agent。** 这与 Pinterest 的 domain-specific server 原则形成互证。

- **证据**：[[20260925-databricks-spglobal-genie-mcp]]；每个 Genie Agent 暴露为 managed MCP server，上层 FastMCP proxy 组合 namespaced tools。
- **边界**：组合降低客户端配置复杂度，但不会自动解决跨域 routing error、语义冲突和 tool explosion；这些仍需 eval 与 observability。

## 核心组件

- **MCP Client**：集成 LLM 的应用（如 Pinterest 内部的 AI 聊天平台）。
- **MCP Server**：暴露具体工具能力的后端服务（如 Presto 查询、日志读取）。
- **MCP Registry（可选）**：元数据发现目录；企业可增加治理和准入能力，不替代运行时授权。
- **AuthN / AuthZ 层**：身份与资源权限的执行机制；JWT、mesh identity、Envoy 和 policy decorator 是 Pinterest 案例中的选择。
- **Human-in-the-loop（按风险配置）**：必要时确认敏感或高成本动作；确认不替代执行权限与效果验证。

---

## 关键数据点

- Pinterest 在 2025 年 1 月时已达到每月 **66,000 次** MCP 调用。
- 覆盖了 844 名月活用户。
- 作者按工具 owner 提供的单次节省时间乘调用数估算每月约 **7,000 小时**，不是独立实测净生产力。
- Pinterest 以多个领域特定 MCP server 替代单一巨型 server，以降低权限耦合和上下文噪声。
- 非实验 server 需要 owning team、registry entry 和 Security、Legal/Privacy、GenAI review。

## 前提与局限性

- **前提**：需要工具提供方（Server）和消费方（Client）都遵循同一套协议规范。
- **局限性**：虽然标准化了连接，但“如何教导 Agent 正确使用工具”这一 Prompt 难题依然存在。
- **安全风险**：统一的接口意味着如果鉴权失效，Agent 可能会获得极大的系统操作权限，因此必须配合严格的 [[Harness-Engineering|驾驭工程]]。
- **上下文风险**：工具太多会污染模型上下文。MCP server 设计必须考虑工具描述长度、领域边界和按需加载策略。
- **治理风险**：协议本身不定义企业内谁能批准 server、谁承担 owner、如何审计调用、如何废弃低质量工具；这些必须由组织 harness 补齐。

## 治理结构与可替换性（07-22 历史推演，2026-11-28 复核）

可按协议规范、注册与发现、客户端默认配置、运行时授权四个对象分析控制权。它们可能由不同参与方掌握，不是一个必然集中或单方控制的治理层。

官方公共 Registry 提供元数据目录与命名空间认证；下游聚合及企业私有目录可增加准入、审查和过滤。官方 [About](https://github.com/modelcontextprotocol/registry/blob/main/docs/modelcontextprotocol-io/about.mdx) 与 [2025-09-08 发布公告](https://blog.modelcontextprotocol.io/posts/2025-09-08-mcp-registry-preview/) 明确支持兼容目录，且实际 server 代码安全扫描主要由包仓库及下游承担。[[MCP-Registry]] 中 Pinterest 的内部准入机制不是协议必备组件。目录身份与运行时资源授权不可互替。

历史“宪法级权力”“Anthropic 单方控制”“标准战争已结束”“分层垄断不可退出”“W3C 最后窗口”等判断未有充分比较、市场份额或规则控制证据；撤回稳定结论身份，保留 [[2026-07-22]] 推演原文。MCP 与 A2A 的主要接口对象不同，互补关系不证明二者永久不会竞争或替代。协议客户端-服务器形态也不等于所有部署集中于单一中心。

可验证方向：固定业务能力与权限，比较静态配置、兼容目录和聚合层切换后的发现质量、接口兼容、迁移成本、授权、审计及恢复；存在等价实现则不以目录或自建服务作为必要条件。未重新核验 MCP 当前传输版本、SDK、市场份额或 A2A 实现，不能使用本节历史资料直接指导当前接口迁移。

## 关联概念

- [[MCP-Registry]] - 治理核心
- [[Pinterest-Engineering]] - MCP 进入企业生产环境的案例
- [[Harness-Engineering]] - Pinterest 将 MCP 视为其 Agent 基础设施（Harness）的底座
- [[Context-Engineering]] - 通过分领域服务器管理 Agent 的上下文空间
- [[Agent-Native]] - MCP 是 Agent 原生基础设施的典型代表
