---
type: source-summary
title: "From Data to Dialogue: How S&P Global Energy Made Its Structured Data Estate Conversational with Databricks Genie Agents and MCP"
canonical_url: "https://www.databricks.com/blog/data-dialogue-how-sp-global-energy-made-its-structured-data-estate-conversational-databricks"
raw_state: index
original_raw_file: "20260925-databricks-spglobal-genie-mcp.md"
original_body_sha256: "1097ae46d403d1aa54452c52fef255b28b42dc3eb34cf2c1d5679a48719ca751"
indexed_at: "2026-09-28T16:34:39+08:00"
created: 2026-09-28
updated: 2026-09-28
tags:
  - source-summary
  - agentic-analytics
  - mcp
  - semantic-layer
  - enterprise-data
evidence_level: high
claim_type: mixed
source_locator:
  - "The challenge: Structured data is easy to store, hard to converse with"
  - "The architecture: Genie Agents as the semantic layer, MCP as the contract"
  - "Layer 1: SMEs curate one Genie Agent per dataset group"
  - "Layer 2: Every Genie Agent is automatically an MCP server"
  - "Layer 3: Composing group Genie Agents into commodity bundles with a FastMCP proxy"
  - "What changed for the business"
  - "Lessons learned and best practices"
---

# From Data to Dialogue

## 1. 浓缩

- **核心结论 1：企业 Agentic Analytics 的语义层应该由 domain expert 直接拥有，而不是通过工程 backlog 间接维护。**
  - S&P Global Energy 让 SMEs 按 dataset group 建立窄范围 Genie Agent，并直接维护表/列说明、business definition、trusted examples。
  - **判断**：semantic layer 不只是数据平台资产，也是组织 ownership 设计；最懂业务定义的人应该能直接发布机器可消费的语义。
- **核心结论 2：MCP 在该架构中的价值不是“让 Agent 会查 SQL”，而是成为统一、受治理的 access contract。**
  - 每个 Genie Agent 直接暴露为 managed MCP server，并继承 Unity Catalog 的 auth/permission/audit；没有再建一套平行安全层。
  - **判断**：MCP 最有价值的企业形态是把既有 governance 投射到 Agent access，而不是绕过治理建立新的 AI 数据通道。
- **核心结论 3：窄 Agent + MCP composition 优于巨型全域 Agent。**
  - dataset-group Agent 保持语义聚焦，高层用 FastMCP proxy 组合成 commodity/cross-domain endpoint。
  - **判断**：应该在语义层保持局部边界，在协议层组合广度。这样既降低单 Agent 的 context/ontology 复杂度，又避免消费者配置大量 server。
- **核心结论 4：质量闭环应由 SME benchmark 驱动，而不是只看 latency。**
  - SMEs 定义代表真实问法的测试问题和 verified answer，修改 instructions/data/business logic 后可重复跑 benchmark。
  - **判断**：Agentic Analytics 的“信任”可以部分操作化为 domain owner agreement + regression eval，而不是依赖 demo impression。

## 2. 质疑

- 这是 Databricks/S&P 客户案例，time-to-market 和质量收益没有独立 benchmark。
- “一 agent 一 dataset group”是该数据域的经验，不应机械推广成固定粒度。
- Unity Catalog inherited governance 依赖数据权限模型本身已经正确；MCP 不会修复错误或过宽的数据授权。
- FastMCP composition 减少客户端复杂度，但上层路由错误、跨域语义冲突和 tool explosion 仍需要 eval/observability。

## 3. 对标与约束

- **与 [[Agentic-Analytics]]**：Anthropic/LangChain 已表明 semantic layer + domain skills + evals 是可靠分析入口；本案例补上第三个独立组织，并把 domain owner 从“维护文档”推进到“直接发布 conversational endpoint”。
- **与 [[Model-Context-Protocol-MCP]]**：Pinterest/Cloudflare 证明 MCP 需要领域 server + governance；S&P 进一步证明 MCP 可作为**组合层**，把多个 narrow semantic agents 暴露为一个稳定业务 endpoint。
- **与 [[Context-Engineering]]**：答案质量不是靠更大 context，而是把 business semantics 放进小而清晰的 domain surface。
- **与 [[Machine-Readable-Processes]]**：业务定义、trusted query 和 benchmark 被编码为 agent 可执行/可验证的资产。

## 证据边界

- 第一方客户案例；技术架构证据强于业务收益幅度。
- Raw 为公开页面 evidence snapshot；canonical 页面可恢复。

## 关联概念

- [[Agentic-Analytics]]
- [[Model-Context-Protocol-MCP]]
- [[Context-Engineering]]
- [[Machine-Readable-Processes]]
