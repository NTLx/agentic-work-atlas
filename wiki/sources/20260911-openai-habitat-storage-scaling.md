---
type: source-summary
title: "Rapidly scaling online storage to serve over 1 billion ChatGPT users"
source_raw:
  - "[[20260911-openai-habitat-storage-scaling]]"
canonical_url: "https://openai.com/index/scaling-storage-one-billion-users-part-one/"
source_locator:
  - "What is Habitat? / Build a service：从客户端库到独立服务，减少跨服务发布扇出并集中安全控制"
  - "Running Habitat at scale：asyncio/GIL、Statsig 配置抖动、LIFO 连接池反馈回路与 Envoy"
  - "Why Habitat does less：受限 NoSQL object/edge API、常量工作量与 CDC→Rockset 复杂查询逃生舱"
  - "Migrate from Python to Rust：Q2 2026 两名工程师、Codex 与 GPT-5.5，Rust 承担 95% 生产请求"
raw_state: full
created: "2026-09-13"
updated: "2026-09-13"
tags:
  - source-summary
  - agentic-engineering
  - agent-infrastructure
  - platform-engineering
  - distributed-systems
evidence_level: high
claim_type: mixed
---

# Rapidly scaling online storage to serve over 1 billion ChatGPT users

> OpenAI 官方工程文章（Jon Lee、Chaomin Yu、Ben Ries，2026-09-11），介绍在线存储平台 Habitat 如何从 DevDay 2023 的 Python 客户端库演化为全球服务层。文章是系列第一部分，数据和经验主要来自 OpenAI 自述。

## 编译摘要

### 1. 浓缩

- **核心结论 1：当共享客户端的变更扇出、运维脆弱性和安全边界超过可接受范围时，基础设施应从库升级为集中服务。**
  - 关键证据：Habitat 最初是连接 Azure Cosmos DB 的 Python client library；随着产品和服务数量增加，协议变更要协调几十个服务，发布变得脆弱，于是迁移为独立 service。
  - 关键证据：服务化提供单一控制点，用于统一部署、可观测性、访问控制、审计日志、数据安全与隐私，并限制外部、内部及 Agent 访问底层存储。
  - 规模背景：文章报告 Habitat 每秒处理超过 7,000 万请求，支持每周超过 10 亿用户使用的产品，覆盖近 40 个地域并服务超过 500 PB 数据；这些是 OpenAI 的自报运行数据。
- **核心结论 2：规模化可靠性来自把接口能力约束在可预测的成本边界内，同时用测量发现运行时反馈回路。**
  - 关键证据：Habitat 不允许客户端任意构造可能触发大表扫描或复杂 join 的 SQL，而是提供 client-defined object/edge 的受限 NoSQL API；复杂查询通过 CDC 流入各团队隔离的 Rockset 视图，避免在线热路径承担不可控工作。
  - 关键证据：文章通过 asyncio loop delay、CPU profiling 和线上实验定位了 Statsig 巨型配置的同步解析、LIFO 连接复用造成的“慢实例获得更多流量”等问题，并以 targeted config/jitter、FIFO 和 Envoy/Istio 等方式拆除反馈回路。
- **核心结论 3：先用熟悉但有技术债的栈快速形成平台，再用 Agent 降低迁移成本；这不等于 Agent 取代架构和运维判断。**
  - 关键证据：Python 是必要的快速交付选择，但在 CPU-heavy 工作、尾延迟和多进程/连接管理上暴露瓶颈；Q2 2026 两名工程师配合 Codex 与 GPT-5.5 重写 Rust，文章报告 Rust 已承载 95% 生产请求，CPU 效率约 6 倍、内存效率约 15 倍。
  - 关键证据：迁移前仍需要明确服务边界、接口约束、验证指标、流量切换与回滚顺序；模型降低的是实现和迁移成本，不会自动决定哪些查询应被禁止或哪些 SLO 足够。

### 2. 质疑

- **关于规模数据的质疑**：70M+ requests/s、1B+ weekly users、500 PB、近 40 个地域以及 Rust 的 6x/15x 对比均来自 OpenAI 工程团队自述；文章未给出完整 workload mix、SLO、置信区间、成本分布或独立复现。
- **关于服务化的质疑**：集中服务减少客户端发布扇出，也形成控制面单点和组织依赖；它是否优于库，取决于部署频率、团队边界、故障隔离能力和平台团队成熟度，不能普遍化为“总是服务化”。
- **关于受限 API 的质疑**：NoSQL object/edge API 以牺牲表达力换取成本可预测性；CDC→Rockset 把复杂度转移给各产品团队，并引入近实时延迟、数据一致性和额外资源管理问题。文章只展示了该权衡，没有比较其他分片、查询治理或数据库方案。
- **关于 Rust 重写的质疑**：95% 流量、6x CPU 和 15x 内存是迁移结果，但“2 engineers + Codex + GPT-5.5”对结果的因果贡献无法从单篇自述中分离；剩余 Python 流量、回归范围、上线事故与长期维护成本尚未公开。
- **关于证据版本的质疑**：这是 Habitat 系列第一部分，数据库层和 500 PB/70M+ 请求如何落地在后续 Part II；本摘要不把未公开的数据库细节补成结论。

### 3. 对标

- **与 [[Agent-Harness]] 对标**：Habitat 把模型或产品不应重复处理的路由、权限、审计、尾延迟和回滚控制收进平台边界；它展示了“确定性控制面包住开放式调用者”的 Harness 形态。
- **与 [[Agent-Infra]] 对标**：从 client library 到 service 是 Agent 基础设施从组件到组织级平台的跃迁：产品团队使用简单接口，平台统一承载安全、可观测性、容量和演进。
- **与 [[Secure-Paved-Path]] 对标**：受限 API 把安全和成本约束嵌入默认路径，令高代价查询必须显式走逃生舱；这比事后审查每个调用更接近 paved path。
- **与 [[Technical-Debt-Avoidance]] 对标**：先用 Python 解决产品和可靠性问题、再以可验证指标推动 Rust 迁移，是“技术债务作为有意序列化选择”的案例；关键不在避免所有债，而在知道何时偿还、用什么证据验收。
- **跨域关联（综合判断）**：Agent 系统的工具接口也应优先暴露常量工作量、可审计、可回滚的原语，把复杂查询、跨系统写入或高风险动作移到隔离且有明确责任人的路径中。

## 证据定位

- **开头规模摘要 / What is Habitat?**：平台规模、DevDay 2023 起点、client library 的职责和服务化动因。
- **Build a service**：发布扇出、集中访问控制、审计日志、数据安全与隐私边界。
- **Running Habitat at scale**：尾延迟、asyncio/GIL、多进程、Statsig 同步配置解析、LIFO/FIFO 连接池和 Envoy/Istio。
- **Why Habitat does less**：受限 NoSQL API、避免无界查询、复杂查询的 CDC→Rockset 路径。
- **Migrate from Python to Rust**：Q2 2026 的迁移组织方式、95% 生产请求、6x CPU、15x 内存及 Part II 边界。

## 前提与局限性

- 这是 OpenAI 的第一方工程复盘，不能单独证明同一架构适用于不同规模、不同一致性要求或不同数据库团队。
- 文章强调关键决策和结果，但没有完整披露故障率、延迟分位数、成本、数据一致性指标、权限实现和 Rust 迁移的测试矩阵。
- “受限接口提高可靠性”是有条件的工程判断：如果复杂查询是核心产品能力，隔离的二级视图、缓存或专用查询服务的成本必须纳入比较。
- 本篇是两部分系列的第一部分；关于底层存储层的结论应等待后续材料，不从摘要外推。

## 关联概念

- [[Agent-Harness]]
- [[Agent-Infra]]
- [[Secure-Paved-Path]]
- [[Technical-Debt-Avoidance]]
- [[Agent-Verification]]
