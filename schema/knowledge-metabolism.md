---
title: "每周知识代谢与知识晋升"
type: schema-subdoc
---

> 本文档是 Agentic Work Atlas Schema 子文档，由 README.md 路由表按需加载。

# 每周知识代谢与知识晋升

本协议定义外部 intelligence 如何进入现有 `clip → compile`、Research 与维护工作；它不是新知识生命周期、第五个日常环节或独立状态系统。

## 角色与执行边界

固定编排链为：`Daily Evidence Discovery → work_events(canonical candidate lineage) → ai_work_queue(worker=weekly, kind=knowledge_promotion_review) → ChatGPT Weekly Promotion / Research Decision → work_events(promotion manifest) + ai_work_queue(worker=hourly, kind=wiki_compile) → ChatGPT Hourly Integration → VPS ServerFS MCP（直接仓库操作） → 本仓库稳定知识 → ChatGPT Monthly Knowledge Governance`。

- **Daily** 执行 intelligence discovery、verification 与 canonicalization；完整报告以 Markdown 交付，机器可消费的候选语义与 lineage 通过 `work_events` 的 canonical candidate Event 持久化。Daily 不直接决定耐久知识保留，也不生成 sidecar / Daily GitHub artifact 作为知识代谢接口。
- **Weekly** 是唯一 Promotion Gate 与 Promotion 前 evidence-gap resolution 层：审阅 canonicalized 候选、检查现有 Wiki coverage、由当前 ChatGPT 直接完成必要的有界补研，最终决定 `promote`、`research_needed` 或 `ignore`。只有 `promote` 才创建 `worker=hourly, kind=wiki_compile`；完整 promotion manifest 持久化为 `work_events` Event，并由 queue 的 `source_event_id` 引用。Weekly 不创建 `wiki_research` 或 `wiki_maintenance`。
- **Hourly** 是可恢复 Integration Gate，正常只执行 Weekly 已批准且边界冻结的 `wiki_compile`。clip、compile、lint、registry 与必要 Git 操作由 ChatGPT 本身通过直接非 Agent 工具完成；跨运行恢复依赖 `work_id` / `correlation_id`、`source_event_id` 指向的 promotion manifest、队列状态、仓库当前状态与已有 commit，而不是服务器侧 Agent task。Hourly 不承担 Promotion、开放式研究或既有知识治理。
- **ServerFS MCP / 本仓库** 是 repository-local Integration / Governance 的直接工具通道：ChatGPT 使用 ServerFS MCP 当前直接暴露的文件、Repo Actions 与核心 repository/Git 能力读取、创建、修改仓库内容。ServerFS 不作为二次 AI Agent 编排层，也不替 ChatGPT 再调用服务器上的 AI Agent；如果某个必要步骤没有直接暴露的非 Agent 能力，应显式返回 `blocked` 或保留待完成步骤，而不是把任务静默委派给服务器 AI Agent。
- **Monthly** 是 Knowledge Governance Layer：直接评估并治理已经存在于本仓库的稳定知识，包括 utility、merge、supersede、stale/orphan、alias、relationship/structure、provenance continuity 与 knowledge debt。Monthly 不把 `wiki_maintenance` 派给 Hourly；若治理暴露出新的来源、事实或稳定知识命题，则创建窄范围 `worker=weekly` evidence / promotion work，重新进入 Weekly Gate。

`work_events`、queue 与 work recovery 是外部运行状态。本仓库不复制其状态，不新增运行表、注册表或周度运行账本。Daily 通过 `work_events` 提供已验证、已 canonicalize 的候选语义；Weekly 通过 `work_events` 提供 promotion decision 与完整 integration manifest；`ai_work_queue` 只承载 worker 路由和运行状态。ServerFS MCP 只提供 ChatGPT 当前可直接调用的仓库操作能力，不开展广泛新闻发现，也不自动启动服务器 AI Agent。

## 来源身份与候选归并（第一阶段增量契约）

`canonical_key` 表示“待判断的知识候选/命题”的语义身份，不等于来源 URL 身份；`evidence_version` 表示该候选的证据版本。为了避免同一来源跨日产生不同 `canonical_key` 而被误认成独立证据，新的 Daily candidate Event 在现有字段之外可写 `source_identity`，Weekly 必须兼容无此字段的历史 Event：

- GitHub 官方仓库统一为 `github:<owner>/<repo>`（owner/repo 小写，以实际确认的官方仓库身份为准），例如 `github:nvidia/auto-ontology`。
- 普通网页优先用实际验证的一手 `canonical_url` 作为身份依据；移除 fragment、已证实无语义的追踪参数，保留可能改变资源/版本的查询参数。不得只凭标题相似、域名相同或推测重定向合并来源。
- 同一个 `source_identity` + 同一个核心事实/技术命题跨日再出现：先查已有 candidate Event，复用先前 `canonical_key`，以新的 `evidence_version` 记录真正增量；没有增量则不生成重复候选。若同一来源确实支持**不同的独立命题**，可以拥有不同 `canonical_key`，但必须在 Event 中说明 `claim_scope` 与差异。
- Weekly 归并时至少交叉核验 `source_identity`（有则用）、canonical/source URL、原始仓库或论文身份、命题范围、现有 Wiki 覆盖。历史 `canonical_key` 不一致不是两份独立 Evidence；合并时保留所有原 Event ID 与旧 key 的 lineage，不能删除或重写历史事件。

本阶段只增加向后兼容的元数据及归并规则，不批量改写历史 Event、Raw Registry 或 Stable Wiki 页面，也不将新的字段设为全库 lint 阻断项。现有 n8n `Record work event` 仍按 `event_id` 幂等，而非按 `canonical_key` 或 URL 全局唯一；因此 Weekly 的跨 Event 归并目前仍是必要的语义质量门。

## RSS 逐条证据记录与可恢复结算（第一阶段增量契约）

RSS `rss_intelligence_items` 中的 `status=processing` 和 `digest_id` 是 n8n 运行层的权威状态。Delivery Receipt 只证明报告送达；`rss.digest.completed` 只在处理完成后产生。**不能因为已发送 Discord、时间已过或有部分 verified 文章就封账整批。**

为避免历史 `processing` 每日重复从零核验而缺少逐条进度，Daily 在实际复核某条已认领 Item 后，通过现有 `Record work event` 写入或更新一条 `work_events`：

- `event_id = rss.article.evidence_checked:<digest_id>:<item_key>`，其中 `digest_id` 和 `item_key` 均原样取自实际 n8n 行；不要生成新的 Item ID。
- `category = rss.article.evidence_checked`；`project = tech-intelligence`；`correlation_id = <digest_id>`；`url = <该 Item 的原始 URL>`；`source = chatgpt:daily`（现行执行器标识）；`occurred_at` 为本次实际检查时间。
- `metadata` 至少包含 `digest_id`、`item_key`、`source_url`、`disposition`（`verified` / `excluded` / `source_gap`）、`source_read_status`（`verified` / `partial` / `blocked` / `not_applicable`）、`checked_at`、`evidence_summary`；对 `verified` 还需原文可定位片段/章节或等效 `source_locator`；对 `excluded` 必须有具体 `reason`（表示不进入正式知识候选，不冒充已读正文）；对 `source_gap` 记录缺失证据/受限原因。
- 重试先按 exact `event_id` 回读已持久化检查结果；只有真的复核才更新其 `checked_at` / disposition。禁止重复制造来源，也禁止把旧 `source_gap` 仅凭时间改成 `verified`。
- 即使已有 `verified` 条目，同一 digest 仍存在 `source_gap` 或没有可信终态记录时，仍保留整批 `processing`，按 `rss.digest.recovery_pending:YYYY-MM-DD` 记录缺口。已有 Discord A 消息不重发；新补证只追加带 lineage 的补充 Event/必要通知。

逐条 Receipt 是**处理进度可观测性**，不是仅凭字段值自动证明模型确实阅读了原文。当前 n8n Complete 工作流仍主要验证持久化 Discord A 回执与批次数量，尚未强制检查每条 Receipt；在该确定性门禁单独完成测试并上线前，Daily 必须自行逐条核验后才可调用 Complete。不得以此文档声称 n8n 已具备逐条强制验收。

## 外部 work manifest

Hourly `wiki_compile` manifest 应由 Weekly 在 `work_events.metadata_object` 中持久化，并由 queue 的 `source_event_id` 引用。至少携带 `canonical_key`、`promotion_id`、parent `work_id` / `correlation_id`、canonical/source URLs、`decision=promote`、evidence summary/strength、accepted scope、expected knowledge delta、existing Wiki coverage、相关既有 Wiki paths（如有）、provenance / lineage、success criteria 与 `execution_policy=chatgpt_direct_only`。Hourly work 的恢复身份由 `work_id` / `correlation_id`、`source_event_id`、队列状态与仓库事实维护，不依赖 ServerFS Agent `task_id`。关键 manifest 缺失到无法可靠执行 Integration Gate 时返回 `blocked(manifest_incomplete)`，不自行重新 Promotion 或扩大研究输入。

## Integration Gate 与结果

Integration Gate 先校验 manifest 的 operation、目标和 lineage，再检查 `raw/`、`state/raw-registry.json`、`wiki/sources/`、entities、topics 与 comparisons 的现有覆盖。按 `canonical_key`、canonical/source URL、Registry 条目、source summary 和已有页面交叉去重；同一 URL 或转载不自动成为增量。重复来源若有实质证据增量，保留原始来源链并解释差异；不得覆盖不可变 Raw。

本地结果是每个 work item 的执行结果，不是新状态机或长期登记：

- `compiled`：按既有 compile 生命周期完成有证据支持的知识写入。
- `no_delta`：任务已检查，现有知识充分，无需改动。
- `duplicate`：manifest 对应已有相同来源/知识，无实质增量。
- `source_gap`：所需证据不可得或缺失；按 research manifest 规则只更新既有 Research agenda/log。
- `blocked`：manifest 不完整、冲突无法裁决、权限/材料不可用，或现有门禁阻止安全执行。

不得将 `promote_compile`、`source_need`、`ignore` 当作本地 Integration Gate 决策。它们不属于仓库执行结果。Integration Gate 对已晋升任务执行正常 compile；对已选 research gap 执行 Research 写入；对 maintenance 执行有界修复。主题宪法仍约束所有写入，不能以外部晋升绕过证据、Raw、provenance、实体准入、lint、index 或 git 规则。

## `wiki_compile`

Hourly 执行 Weekly 已晋升的材料。将 canonical/source URL 作为既定输入，按 `schema/compile-operations.md`、`schema/compile-workflow.md`、`schema/three-step-method.md`、source-summary、frontmatter 与 provenance 规则完成现有 `clip → compile`。继续检查 raw、Registry、source summaries、entities、topics、comparisons 覆盖；重复且无增量返回 `duplicate`，确有证据增量才编译。每次输入无法执行时返回 `blocked` 或 `source_gap`，不得改判 promotion 或转而发现其他候选。

## Weekly evidence-gap resolution

`research_needed` 是 Weekly Promotion Gate 的结论状态，不是 Hourly operation。候选证据初步不足时，Weekly ChatGPT 在当前运行内按有界问题直接检索、核验与比较可靠来源，并重新判断 `promote` / `research_needed` / `ignore`。本轮合理补研后仍缺关键 Evidence 时，将 missing evidence、checked sources、uncertainty、future trigger 与 lineage 记录在外部 `work_events`；不得创建 `wiki_research` work，也不得借研究状态写入稳定 Entity、Topic、Comparison 或 Source Summary。若后续取得并验证 Evidence，需要稳定知识增量时重新进入 Weekly Promotion，再由 `wiki_compile` 集成。

## Monthly Knowledge Governance

Monthly 直接对既有稳定知识执行有界治理，可处理 utility review、合并/取代重复页、stale 或 orphan 页面、aliases、关系与 bounded structure、provenance continuity 与 knowledge debt。按 `schema/lint-workflow.md`、`schema/entity-spec.md`、`schema/fragmentation-metrics.md`、`schema/knowledge-utility-eval.md` 及 git 规范审查；治理对象、问题、证据、成功标准和影响范围必须明确。不得借治理引入未经过 Weekly Promotion 的新来源或新稳定主张；若发现新的 evidence / source / knowledge claim，创建窄范围 `worker=weekly` work 或记录 research gap，由 Weekly 重新进入 Promotion Gate。Monthly 不创建或派发 `wiki_maintenance` 给 Hourly。

## Lineage 传播

使用现有 provenance、frontmatter、Registry、Research 记录、外部 `work_events` 与 Git history 连接：Daily canonical object → Weekly promotion → Hourly work → source/raw → stable pages → commit → later reuse。字段按其归属保存，不在本仓库重复建立 runtime 状态：

| 字段 | 外部运行层 | 本仓库持久化 |
|------|------------|---------------|
| `canonical_key` | Daily canonical object、Weekly manifest 与 work item | 编译来源的 source summary frontmatter；若没有 source summary，则写入现有 Research log 对应任务记录 |
| `promotion_id` | Weekly 决策及后续 work manifest | 有晋升来源的 source summary frontmatter；仅适用时记录 |
| `work_id`, `correlation_id` | queue / `work_events` / Hourly task | source summary frontmatter 或对应 Research log，便于从提交文件回查；不写入单独账本 |
| `result_ref` | queue / `work_events`，用于记录 commit、PR 或确有必要的外部执行标识 | 不要求复制为仓库状态；仓库以 Git commit 与实际路径为权威结果 |
| canonical/source URL | Daily canonical object 与 work manifest | Raw 的 `source`、source summary 的 `canonical_url`、Research 中的 source need；保留原始来源身份 |
| operation/kind | queue / `work_events` manifest | Hourly 稳定集成只使用 `wiki_compile`；Weekly research 状态与 Monthly governance action 保留在各自 Event / work lineage 中，不增加仓库运行状态字段 |
| resulting commit / wiki paths | Hourly 回报及外部 `work_events` | Git commit 与实际文件路径本身为权威记录；外部记录回填其 commit SHA / paths |

Source summary 可选记录以下可追溯 frontmatter 字段：`canonical_key`、`promotion_id`、`work_id`、`correlation_id`。它们是 provenance 元数据，不是新状态字段；缺少 lineage 值时不猜造。Research task 在既有 agenda/log 中以紧凑文本记录适用字段。稳定页继续通过 `source_raw` / wikilink 回到 source summary 或 Research 依据，不复制整套运行元数据。后续 Monthly Reuse 可从外部 promotion/work 记录和 Git commit 定位最近样本，并检查稳定页是否进入后续回答或持久化 Output。

## 完成契约

Hourly `wiki_compile` 逐项回报 `work_id`、canonical/promotion/correlation 标识、`source_event_id`、结果、去重/证据依据、实际 wiki paths、resulting commit（如已提交）与验证结果。`compiled` 必须通过现有 compile 门与 wiki lint。Monthly Governance 变更按其适用 lint/audit/utility/git 门验证，并在外部 Event 中记录治理 action 与 before/after evidence。只有实际仓库变更才按 README 和 `schema/git-commit-spec.md` 显式暂存、提交、推送。`no_delta` / `duplicate` 不制造空知识提交；`source_gap` / `blocked` 说明缺口与恢复条件。不要生成 digest、文章或额外运行报告，不新增仓库内运行账本。
