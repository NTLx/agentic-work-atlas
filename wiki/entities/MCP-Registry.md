---
type: entity
title: MCP Registry (MCP 注册表)
aliases:
  - MCP 注册表
  - MCP Registry
definition: "MCP server 元数据的注册与发现服务；公共目录、下游聚合及企业内部准入可采用不同治理策略，注册或发布者身份验证不等于运行时工具授权或安全证明。"
created: 2026-05-13
updated: 2026-11-28
evidence_level: medium
claim_type: mixed
tags:
  - AI-Agent
  - governance
  - infrastructure
related_entities:
  - "[[Model-Context-Protocol-MCP]]"
  - "[[Pinterest-Engineering]]"
  - "[[Harness-Engineering]]"
  - "[[Context-Engineering]]"
source_raw:
  - "[[Building an MCP Ecosystem at Pinterest]]"
  - "[[20260617-huggingface-agentic-resource-discovery]]"
---

# MCP Registry

> [!definition] 定义
> 注册表负责 MCP server 元数据的登记、发现和分发。企业可以在其上增加准入、权限查询、运营和审查机制；这些不是所有 MCP Registry 自动具备的能力。

## 三种对象，不混用信任边界

| 对象 | 职责 | 不代表 |
|---|---|---|
| 官方公共 Registry | 发布者命名空间验证、server.json 元数据及发现 API | 代码经过完整安全审查，或企业批准使用 |
| 下游目录 / 企业 Registry | 聚合、筛选、组织准入、owner、状态与策略元数据（按实现） | 所有请求经过中介，或每次动作已获得授权 |
| Runtime 授权与执行点 | 认证主体、资源/工具范围、实际策略判定与效果记录 | 注册成功或工具发现成功即可授权 |

2026-11-28 实际回核 [官方 Registry About](https://github.com/modelcontextprotocol/registry/blob/main/docs/modelcontextprotocol-io/about.mdx)、[2025-09-08 发布公告](https://blog.modelcontextprotocol.io/posts/2025-09-08-mcp-registry-preview/) 和 [Registry Authorization](https://github.com/modelcontextprotocol/registry/blob/main/docs/reference/api/registry-authorization.md)：官方服务承载公共元数据，支持下游及私有兼容目录；实际 server 代码的安全扫描主要由包仓库与下游承担。Registry read/write scope 约束目录资源访问/修改，不授权 server 工具调用。官方公共目录可公开读取，发布使用独立认证机制。主分支文档仍有 preview 表述，本轮未验证部署版本或 API conformance，不据此断言所有实现的成熟度。以上 URL 为既有概念纠错依据，未作为新 Source 晋升。

## Pinterest 内部 Registry：组织治理案例

原始文章 [[Building an MCP Ecosystem at Pinterest]] 记录其内部云托管 MCP、多个领域 server、中心注册表及统一部署管线。

- 注册表 Web UI / API 提供 server、owner、support channel、安全姿态、在线状态与可见 tools。
- 生产使用的非实验 server 绑定 owning team，经 Security、Legal/Privacy 及适用时 GenAI review。内部服务可查询用户是否允许使用指定 server。
- 实际运行时由 Envoy 验证 end-user JWT 和粗粒度策略，server 内 policy decorator 处理工具细粒度权限；敏感数据还有业务组限制。低风险无人在场的只读路径可使用 SPIFFE mesh identity；身份验证不等于资源授权。
- 敏感或高成本操作由其工作流要求人工确认。批准入库与具体动作授权、执行和事后验证不同。

这些是 Pinterest 自报的组织级治理设计，而非 MCP 公共 Registry 的必备行为，也未证明无旁路或所有调用安全。文章报告的调用数及节省时间为历史统计和 owner 估算，不是独立的生产力因果评估。

## 发现与动态搜索

[[20260617-huggingface-agentic-resource-discovery]] 描述 ARD draft（当时版本）通过静态 manifest 和动态搜索发现 skills、MCP servers 与 agents。发现与执行分离；排序结果、发布者 metadata、运行状态不能代替风险评审和实际授权。采用程度及最新规范未本轮复核。

## 治理与可替换性

2026-07-22 历史推演中的“宪法级权力”收窄为条件性分析：若客户端或组织默认依赖单一目录，准入、排名、元数据更新、撤下规则及迁移成本可能影响选择。公开规范和兼容目录为替代设计提供可能，但不证明迁移成本为零；也不能断言 fork 信任锚不可行、退出威胁必然不可信或控制者可单方修改全部生态规则。

实际评估：目录切换时逐项验证元数据兼容性、私有 server 可见性、主体/权限映射、策略与审计连续性、缓存失效及业务恢复。若固定任务和授权后，多个目录或静态配置能实现等价发现和治理，不强制引入中心目录。

## 关键数据点

- Pinterest 文章报告截至 2025 年 1 月约 66,000 次月调用、844 月活用户，以及按 owner 单次节省估计计算的约 7,000 小时/月；三个数字均为该企业历史披露，不外推至官方公共目录。
- 官方公共目录、企业准入目录、执行授权三种对象的接口职责见上表；没有跨实现安全效果或迁移成本的可比量化数据。

## 前提与局限性

- evidence_level: medium；企业案例为自报，ARD 为历史草案，公共 Registry 文档说明设计职责而非部署效果。
- 目录是可选架构组件，不能以其存在推断完整中介。若依赖中心服务，评估可用性、缓存一致性和审批瓶颈；可采用多目录、直接配置等适合场景的方案。
- 注册、发布者身份、代码完整性、组织准入、运行时权限、真实效果是不同检查对象。安全检查由合适的执行点落实，不能把目录发现等同信任或授权。

## 关联概念

- [[Model-Context-Protocol-MCP]] — 协议与发现/治理边界
- [[Pinterest-Engineering]] — 企业内部 Registry 案例
- [[Harness-Engineering]] — 运行时策略与验收
- [[Context-Engineering]] — 按任务发现工具与上下文预算
