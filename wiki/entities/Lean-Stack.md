---
type: entity
title: Lean-Stack
aliases:
  - Lean Stack
definition: "按产品实际约束降低持续技术与运营成本的最小充分技术栈；SQLite+Go+单机 VPS 是个人实践案例，不是固定定义"
created: 2026-04-15
updated: 2026-11-28
evidence_level: medium
claim_type: mixed
tags:
  - software-engineering
  - bootstrap
  - indie-developer
related_entities:
  - '[[Steve-Hanov]]'
  - '[[Specialized-Small-Models]]'
  - '[[Token-Supply-Chain]]'

source_raw:
  - '[[How I run multiple USD10K MRR companies on a USD20month tech stack]]'
  - '[[20260606-the-minimill-of-ai]]'
---

# Lean-Stack（精益技术栈）

## 定义

**Lean-Stack** 是一种在满足功能、可靠性与维护约束下减少不必要持续开销的技术架构选择。低净现金消耗可以延长有限现金跑道；仅基础设施费用低不等于完整经营成本低或无限跑道。

## Steve Hanov 的历史案例配置（非标准模板）

| 组件 | Lean-Stack 选择 | 传统选择 |
|------|---------------|---------|
| 服务器 | Linode/DigitalOcean `$5/月` (1GB RAM) | AWS/GCP `$50-500/月` |
| 数据库 | SQLite + WAL | PostgreSQL/MySQL |
| 语言 | Go (静态二进制, `scp` 部署) | Python/Node.js/Java |
| 认证 | 自写 OAuth2 (30 行) | Auth0/Clerk |
| AI 批量推理 | RTX 3090 + VLLM (一次性 `$900`) | OpenAI API 按 token 付费 |
| AI API 网关 | OpenRouter (按量付费 + 自动回退) | 直接对接各厂商 API |
| AI 开发（历史） | GitHub Copilot 旧请求制 | 需按当前实际计费与任务成本比较 |
| 部署 | systemd service | Docker + K8s |

## 关键数据点

### SQLite vs PostgreSQL 性能对比

[Hacker News 讨论](https://news.ycombinator.com/item?id=47736555) 中 eurleif 评论的 10 万次 `SELECT 1` 微基准（非 Steve Hanov 原文，2026-11-28 核验）：
- PostgreSQL (localhost TCP): 2.77 秒
- PostgreSQL (Unix socket): 1.93 秒（后续另一轮测试，不能与首轮视为同次测量）
- SQLite (内存): 0.07 秒 — **差距近 40 倍**

SQLite + WAL 的写入仍需序列化。该微基准是内存 SQLite 与 PostgreSQL 本地 TCP/socket 的简单查询比较，不证明业务读写、持久化或并发吞吐普遍快 40 倍。

### 内存效率

- Python gunicorn 4 workers: 基线 500MB
- Go 静态二进制: 几 MB
- Go 交叉编译为单一静态二进制文件，`scp` 上传到 `$5` VPS 即运行，无 `pip install` 依赖地狱

### AI 成本三层层级

| 层级 | 方案 | 成本 | 适用场景 |
|------|------|------|---------|
| 本地批量 | RTX 3090 (24GB) + VLLM PagedAttention | 一次性 `$900` | 大批量分类/摘要/研究 |
| API 网关 | OpenRouter 统一接口 + 自动回退 | 按量 | 前沿模型、低延迟用户交互 |
| 开发辅助（历史案例） | GitHub Copilot 旧请求制 | 历史自报 | 不作为当前价格或长任务成本保证 |

**本地 AI 升级路径**: Ollama (快速实验) → VLLM (生产并发) → Transformer Lab (微调)

## Agentic 扩展：本地优先，云端升级

Tomasz Tunguz 的 “minimill” 案例把 Lean-Stack 从低成本软件栈扩到了低成本 agent 栈：先用本地小模型把任务分流，复杂任务再升级到云端。结果是 78% 的 AI 工作留在本地处理，平均任务时长从 47 秒降到 19 秒，queue age 从 73 秒降到 4。

这里的关键不是“全部本地化”，而是先路由，再决定是否动用昂贵算力。对 Lean-Stack 来说，这意味着 AI 成本优化不只是在 API 账单层做减法，而是在任务入口处做结构化分层。

## 前提与局限性

- **适用场景**：部署拓扑简单、负载与写并发在实际容量内、恢复与可靠性满足目标的产品；月活人数不是数据库选型阈值。
- **不适用场景**: 需要多区域部署、PB 级数据、复杂分布式事务
- **关键前提**: WAL 模式下单写者限制，高并发写入场景需要额外设计；参见 [SQLite 官方选型指南](https://www.sqlite.org/whentouse.html)。
- **新增前提**: 本地优先的 agent 栈依赖任务分流质量；若 easy / hard 误判过多，性能收益会被回退和升级开销吃掉
- **认知偏差**: 部分选择依赖 Steve Hanov 个人经验，不同产品可能需要不同方案。旧计费、报价与硬件价格是时点事实；GitHub 已于 2026-06-01 切换 Copilot 计费，部分旧年付计划过渡例外，详见 [[Lean-Indie-Engineering]] 的核验记录。

## 关联概念

- Anti-Enterprise-Mindset — 不买"万一"的账
- Runway-Math — 低成本的数学逻辑
- [[Constraint-Driven-Engineering]] — 约束决定技术选择
- [[Steve-Hanov]] — 实践者
