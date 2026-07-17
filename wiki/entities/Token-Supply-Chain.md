---
type: entity
title: "Token 供应链"
aliases:
  - Token Supply Chain
  - token 供应链管理
definition: "将 token 像电力、物流和数据库一样编排的生产基础设施层，覆盖推理调度、KV cache 管理、成本路由、可观测性和治理，使 token 从聊天消耗品变成可控生产资料"
created: 2026-05-29
updated: 2026-06-15
evidence_level: medium
claim_type: mixed
tags:
  - agentic-ai
  - token-economics
related_entities:
  - "[[Agent-Infra]]"
  - "[[Agentic-Workflow-Token-Efficiency]]"
  - "[[Specialized-Small-Models]]"
  - "[[Dual-Tier-LLM-Architecture]]"
  - "[[Token-Maxing]]"
  - "[[Enterprise-AI-Rationing]]"
source_raw:
  - "[[20260528-agentic-ai-2026-landscape]]"
  - "[[20260528-corporate-america-ai-rationing]]"
  - "[[20260606-the-minimill-of-ai]]"
---

> [!definition] 定义
> 将 token 像电力、物流和数据库一样编排的生产基础设施层，覆盖推理调度、KV cache 管理、成本路由、可观测性和治理，使 token 从聊天消耗品变成可控生产资料。

Token 供应链是 [[Agent-Infra]] 和 Model 层之间的中间基础设施层。当 Agent 从"回答一句话"扩展到"连续读代码、查资料、调用工具、等待反馈再继续执行"，token 就从聊天消耗变成了生产资料，需要被稳定、便宜、可观测、可治理地供应。

## 核心分工

推理层出现四种分工：

| 分工 | 代表项目 | 职责 |
|------|---------|------|
| 高吞吐引擎 | vLLM、SGLang | 把模型更快、更稳、更便宜地跑起来 |
| 边缘/本地推理 | llama.cpp | 把模型带到个人电脑、私有环境和端侧设备 |
| 数据中心级调度 | Dynamo、Ray Serve | 多模型、多租户、多 GPU、多地域运行 |
| 网关和代理 | LiteLLM、OpenRouter | 模型路由、降级、统一接口、成本追踪和审计 |

## 关键数据点

- SGLang issue #21846 路线图命名为 "Distributed KVCache System For Agentic Workload"，明确写入 agentic workloads 导致 KV cache storage 与 transfer volumes 快速增长
- Dynamo issue #5506 的 H1'26 roadmap 聚焦请求调度、KV cache 复用、worker 扩缩容和多节点高可用
- LiteLLM 仓库中 cost/budget/spend 相关 issue/PR 合计 154 条（cost based routing 23、lowest cost 18、budget routing 37、spend tracking 76）
- RouteLLM（ICLR 2025）实现接近强模型质量时超过 2 倍成本节省
- IPR（EMNLP Industry 2025）在 Claude 系列间做 prompt routing，成本降低 43.9%

## 关键洞察

**Agent 改变了 token 的消费结构。** 传统推理是一个请求、一次生成；Agent 推理是连续多轮、工具调用、长上下文、等待反馈再继续。这对 KV cache、PD 分离、健康检查和路由提出了全新要求。

**工业场景真正痛的是稳定性。** SGLang issue #20252 记录了一个典型 cascading failure：qwen3-32b-fp8 在 90 prefill + 30 decode 的 H20 集群上，部分节点重启后 decode 重试、健康检查失败、router 移除 worker、流量压到剩余节点，最终 503。模型能跑起来只是第一步，一台节点的波动可能沿路由和健康检查放大成全局故障。

## 从数据中心延伸到端侧路由

Token 供应链不只发生在数据中心。Tomasz Tunguz 的本地/云双通道实践说明，终端设备本身也可以成为供应链节点：先在本地完成简单任务，只有复杂任务才升级到云端。

这意味着 token 编排开始出现“边缘 minimill”形态：

- 本地小模型吸收高频、短任务负载。
- 云端强模型保留给长尾、复杂和高不确定任务。
- 吞吐、等待时间和成本一起受到路由策略影响，而不只是受到单次 token 单价影响。

## 类比云计算演化

Model Infra 正在走云计算早期的路径：从"能不能把服务跑起来"到调度、弹性、观测、成本、SLA、供应链和开发者体验的系统工程竞争。

## 前提与局限性

- Token 供应链优化主要适用于大规模部署场景；个人开发者或小团队可能直接从 API 获取 token 更经济
- 成本路由（RouteLLM、IPR）依赖问题难度判断的准确性；误判会导致质量下降
- 文章数据来自蚂蚁 OpenDigger 体系，可能存在分类偏差

## Token FinOps 演化路径（07-17 扩展）

Token 供应链的 FinOps 层面临品类分化（roundtable 4人×2轮）：

### 品类分化

| 子类 | 功能 | 演化路径 | 时间 |
|------|------|---------|------|
| **Token 优化** | 成本可见性、用量追踪、预算告警 | → 被平台收编（模型厂商/可观测/云） | ≈2027 |
| **Token 智能** | 跨平台路由、模型选择、prompt 优化、安全合规 | → 可能独立（需创造独立入口） | ≈2028-2030 |

### 独立窗口关闭三信号

1. 模型厂商内建：Anthropic Console/OpenAI dashboard 已有基础 token 用量
2. 可观测扩展：Datadog 2026 Q1 LLM Observability beta
3. 融资下降：Token FinOps 工具 A 轮估值 2026 < 2025

### 买家优先级

- 模型厂商（Anthropic/OpenAI/Google）：最可能——token 在其基础设施上跑，能提供隐私安全的分析
- 可观测性（Datadog/New Relic）：已在加 token 维度——一维 token vs 多维关联
- 云厂商（AWS/Azure/GCP）：如果企业 AI 入口 = Bedrock 式托管

### 中国差异

中国企业 AI 部署单模型为主（无多模型策略需求）+ 监管压制消费级 Agent → TAM 不足以支撑独立 Token FinOps 品类。缺失 = 结构性非临时性。

## 多模型定价透明性（07-18 扩展）

Tokenizer 差异导致隐性成本偏差 20-40%/prompt（roundtable 4人×2轮）。GPT(tiktoken)、Claude(自定义BPE)、Gemini(SentencePiece)的 token 定义不同→双重变量($/token × token数)同时变化→模型间成本比较=苹果比橙子。

**解决路径**：标准化"每单位工作成本"非"每token成本"。MLPerf for LLM Pricing——10标准任务，每任务token消耗+延迟+质量分数。

**行业联盟路径**（O'Reilly+Thompson）：MLCommons模式→12-18月出v1.0→企业采购RFP纳入→事实标准→成熟后转正。关键障碍=Google（Gemini tokenizer效率较低→暴露隐性高成本）。

**Tokenizer非竞争差异化**（Willison）：差异=历史偶然（GPT-2→tiktoken，Claude=BPE，Gemini=T5传统→SentencePiece）。标准化不压缩有意义竞争维度。

## 关联概念

- [[Agentic-Workflow-Token-Efficiency]] — token 效率优化的方法论层面
- [[Specialized-Small-Models]] — 专门化小模型是 token 供应链的下游消费者
- [[Dual-Tier-LLM-Architecture]] — 按复杂度路由的分层架构是 token 供应链的一种实现
- [[Agent-Infra]] — token 供应链服务的上层
- [[Layered-AI-Sourcing]] — 企业级模型采购是 token 供应链的组织侧映射
