---
type: source-summary
title: "Long-horizon agents and durable execution"
raw_state: index
original_raw_file: "20261110-martinfowler-long-horizon-agents-durable-execution.md"
original_body_sha256: "8e2fb5e3e66865858ec9d9e9a277d2ad594ad2c053ce285f5bc41f8cb1fd2fd3"
indexed_at: "2026-11-28T16:35:48+08:00"
canonical_url: "https://martinfowler.com/articles/durable-execution-agents.html"
canonical_key: "article:martinfowler.com/articles/durable-execution-agents"
promotion_id: "martinfowler-durable-agent-workflows:2026-11-16"
work_id: "wiki_compile:martinfowler-durable-agent-workflows:2026-11-16"
correlation_id: "knowledge-promotion:week-of-2026-11-16"
created: 2026-11-16
updated: 2026-11-28
tags:
  - source-summary
  - durable-execution
  - AI-Agent
evidence_level: medium
claim_type: mixed
source_locator:
  - "Durable execution / Making the loop durable: step input-output log and replay"
  - "The entity and the workflow: per-entity workflow and finite process workflow"
  - "Waiting for people and systems: persisted event waits and timeout"
  - "Retrying failed calls, at least once: retry and idempotency requirements"
  - "Durable is not the same as correct: unknown outcomes, version drift, context and memory"
---

# Long-horizon agents and durable execution

> Kiran Prakash, Martin Fowler site, 2026-11-10. [Primary article](https://martinfowler.com/articles/durable-execution-agents.html). First-party engineering walkthrough and illustrative stock replenishment example, **not** an independently replicated cross-platform reliability benchmark. Weekly promotion event: `knowledge.promotion.manifest:martinfowler-durable-agent-workflows:2026-11-16`; upstream candidate: `intelligence.candidate.canonicalized:martinfowler:durable-execution-agents:20261111`. The original article remains at its canonical URL; the 2026-11-28 capture repairs the evidence lifecycle under the original approved promotion scope.

## 编译摘要

### 1. 浓缩

- **持久化 step log + replay 是恢复执行状态的机制，不是外部副作用的一次且仅一次保证。** 作者将模型决策、工具调用等与外界交互定义为持久化 step，记录输入输出；重启后跳过已记录输出的步骤并重建局部状态。**失败窗口**：外部服务已接单但响应或记录丢失时，重试可能再次执行动作。证据定位：*Durable execution / Making the loop durable*、*Retrying failed calls, at least once*。
- **区分 Entity workflow 与 Process workflow。** 前者维持一个长寿命业务实体（示例：SKU）的状态、消息入口与互斥协调；后者处理一次有限的补货作业，完成后终止。这样可避免同一实体在等待期间无控制地启动重复流程，但仍需业务级状态检查。定位：*The entity and the workflow*。
- **Wait 是持久化的状态转换，而非 Worker 永久占用进程。** 等待人工审批、供应商回应、定时器与超时，需要稳定身份、事件关联和恢复后的继续处理；恢复流程还须重新检查过期业务前提。定位：*Waiting for people and systems*、*The world moves on while you wait*。
- **代码、上下文和记忆漂移是另一组正确性门禁。** 长期运行跨版本部署，重放历史可能遇到不兼容代码；长上下文必须区分可审计的 durable record 与提供给模型的有限上下文。定位：*Code change under a running task*、*Memory: what the agent keeps, and what the model sees*。

### 2. 质疑与边界

- 文章包含 Temporal 与 Cloudflare 的实现及工程示例，证明的是可行架构与行为契约；未提供跨平台随机实验、精确一次效果证明或通用的恢复延迟分布。
- Step 的 `completed` 不等于外部资源的 `committed`。必须为有副作用操作定义幂等键、provider receipt、read-back 和 unknown/partial/retry reconciliation；单凭 durable log 不能判断丢失响应后的真实外部状态。
- Entity workflow 按实体划分并不自动解决跨实体并发、库存竞争、消息重放、审批授权失效和长期版本迁移，需要独立设计与验证。

### 3. 对标与关联

- **判断（综合）**：Agent 编排至少分离四个验收对象：`step-log/replay`、`entity/process identity and ordering`、`external effect settlement`、`current business post-state`。这比“工作流已恢复”更接近用户的业务正确性。
  - **证据**：本文 *Durable execution / The entity and the workflow / Outcomes the agent doesn't see*。
  - **边界**：这是从单一一手架构材料抽象的设计建议，不是该设计在所有服务上的生产可靠性实测结论。
- 与既有 EX-005 研究 **互补而非重复**：[[20260907--ex005-durable-stop-semantics--research]]、[[20260906--agent-revocation-recovery--research]] 聚焦停止/授权撤销、in-flight 和 effect reconciliation；本文补充长期 entity/process 分层、持久 wait、replay 和版本漂移。取消成功不能代替外部效果确认。
- 实施方向：先固定每个外部 action 的业务 identity 和幂等键；重试前用权威来源查 post-state；以可持久化 inbox / timer 恢复等待；新版本上线需兼容尚未结束的工作流历史；最后使用针对失联、重复响应与代码升级的故障注入验证。

## 来源与 provenance

- Canonical URL: https://martinfowler.com/articles/durable-execution-agents.html
- Author/date: Kiran Prakash / 2026-11-10
- Evidence basis: author-primary engineering exposition and code example, not independent replication
- Promotion: `martinfowler-durable-agent-workflows:2026-11-16`; integration: `wiki_compile:martinfowler-durable-agent-workflows:2026-11-16`
- Source identity: `article:martinfowler.com/articles/durable-execution-agents`
- **生命周期修复（2026-11-28）**：原 2026-11-16 Weekly approval 已从 n8n work_events（event_id 如上，row id 3845）回读确认，accepted scope 不变。2026-11-28 重新获取原网页的正文 Markdown（HTTP 200，50,441 字符，Firecrawl scrape ID `01a2214b-671b-74c8-acd2-e0a6874c0242`），核验作者、日期、主要章节和结束标记；这是当日网页转 Markdown 的捕获，不是 11-16 历史原件、原始 HTML 或交互资产的完整副本。新 Raw 正文哈希由 Registry 实际生成；旧哈希未知，不作历史同一性声明。保留原 promotion lineage，不创建重复来源或新晋升任务。
