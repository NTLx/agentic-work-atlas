---
title: "每周知识代谢与知识晋升"
type: schema-subdoc
---

> 本文档是 Agentic Work Atlas Schema 子文档，由 README.md 路由表按需加载。

# 每周知识代谢与知识晋升

本协议定义外部 intelligence 如何进入现有 `clip → compile`、Research 与维护工作；它不是新知识生命周期、第五个日常环节或独立状态系统。

## 角色与执行边界

固定编排链为：`n8n → ai_work_queue(worker=weekly, kind=knowledge_promotion_review) → ChatGPT Weekly Promotion Gate → ai_work_queue(worker=hourly, kind=wiki_compile | wiki_research | wiki_maintenance) → ChatGPT Hourly → VPS ServerFS MCP（直接仓库操作） → 本仓库`。

- **Daily** 执行 intelligence discovery、verification 与 canonicalization，输出候选和证据缺口；不直接决定耐久知识保留。
- **Weekly** 是唯一 Promotion Gate：审阅 canonicalized 候选，决定晋升、转成可行动 evidence gap、或不保留，并为已选工作创建有界 Hourly work。Weekly 不执行跨运行的长任务。
- **Hourly** 是可恢复执行 worker，负责一个有界 work item。剪藏、研究、编译、知识维护、lint 与必要 Git 操作由 ChatGPT 本身完成；跨运行恢复依赖 `work_id` / `correlation_id`、队列状态、仓库当前状态与已有 commit，而不是服务器侧 Agent task。Weekly / Monthly 不持有跨运行执行状态。
- **ServerFS MCP / 本仓库** 是 repository-local Integration Gate 的直接工具通道：ChatGPT 使用 ServerFS MCP 当前直接暴露的文件与其他确定性能力读取、创建、修改仓库内容。ServerFS 不作为二次 AI Agent 编排层，也不替 ChatGPT 再调用服务器上的 AI Agent；如果某个必要步骤没有直接暴露的非 Agent 能力，应显式返回 `blocked` 或保留待完成步骤，而不是把任务静默委派给服务器 AI Agent。
- **Monthly** 执行知识效用与长期质量复核；可提出 `wiki_maintenance` 或 evidence-gap manifest，由 Weekly/外部调度转交 Hourly 执行。Monthly 不拥有跨运行长任务。

`work_events`、queue 与 work recovery 是外部运行状态。本仓库不复制其状态，不新增运行表、注册表或周度运行账本。Daily 仅向本流程提供已验证、已 canonicalize 的候选清单；ServerFS MCP 只提供 ChatGPT 当前可直接调用的仓库操作能力，不开展广泛新闻发现，也不自动启动服务器 AI Agent。

## 外部 work manifest

每个 manifest 应携带可用的 lineage 字段：`canonical_key`（Daily canonical object 的稳定标识）、`promotion_id`（Weekly 晋升时）、`work_id`、`correlation_id`、canonical/source URL、`operation` / `kind`，以及已有的来源事实和目标。Hourly work 的恢复身份由 `work_id` / `correlation_id` 与队列状态维护，不依赖 ServerFS Agent `task_id`。`wiki_compile` manifest 表示 Weekly 已决定晋升；`wiki_research` 表示 Weekly 已选择一个 actionable evidence gap；`wiki_maintenance` 表示 Monthly/审计已提出有界的既有知识修复。缺少足以识别 work 或来源的字段时返回 `blocked`，不自行扩大输入。

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

## `wiki_research`

Hourly 将外部已选择的 actionable evidence gap 转为现有 `wiki/research/research-agenda.md` 条目，必要时按 `schema/research-module.md` 写入 research log。合并到最接近的既有 CR/EX 或 Source 需求；只在现有 Research 规则允许时创建条目。记录可执行的 source goal、Evidence gap、canonical/source URL 和 lineage。Research 是未验证问题的操作层：没有取得并验证 Evidence 前，不创建或更新稳定 Entity、Topic、Comparison 或 Source Summary。已有 Evidence 需编译时应另建/排入 `wiki_compile` 工作，不在 research work 中暗中编译。

## `wiki_maintenance`

Hourly 对 manifest 指定范围执行有界的既有知识修复，可处理合并/取代重复页、stale 或 orphan 页面、aliases、关系与结构问题。按 `schema/lint-workflow.md`、`schema/entity-spec.md`、`schema/fragmentation-metrics.md` 及 git 规范审查；使用现有 lint、entity-audit、Research、provenance 与稳定页规则。不得借维护任务引入新来源、新主张或扩展成 compile；发现证据缺口时只写入既有 Research agenda/log，并报告 `source_gap`。维护范围必须来自 manifest 或本地审计发现，按其边界最小修复。

## Lineage 传播

使用现有 provenance、frontmatter、Registry、Research 记录、外部 `work_events` 与 Git history 连接：Daily canonical object → Weekly promotion → Hourly work → source/raw → stable pages → commit → later reuse。字段按其归属保存，不在本仓库重复建立 runtime 状态：

| 字段 | 外部运行层 | 本仓库持久化 |
|------|------------|---------------|
| `canonical_key` | Daily canonical object、Weekly manifest 与 work item | 编译来源的 source summary frontmatter；若没有 source summary，则写入现有 Research log 对应任务记录 |
| `promotion_id` | Weekly 决策及后续 work manifest | 有晋升来源的 source summary frontmatter；仅适用时记录 |
| `work_id`, `correlation_id` | queue / `work_events` / Hourly task | source summary frontmatter 或对应 Research log，便于从提交文件回查；不写入单独账本 |
| `result_ref` | queue / `work_events`，用于记录 commit、PR 或确有必要的外部执行标识 | 不要求复制为仓库状态；仓库以 Git commit 与实际路径为权威结果 |
| canonical/source URL | Daily canonical object 与 work manifest | Raw 的 `source`、source summary 的 `canonical_url`、Research 中的 source need；保留原始来源身份 |
| operation/kind | queue / work manifest | 通过既有工作产物与结构化 commit type/scope 表达；不增加独立状态字段 |
| resulting commit / wiki paths | Hourly 回报及外部 `work_events` | Git commit 与实际文件路径本身为权威记录；外部记录回填其 commit SHA / paths |

Source summary 可选记录以下可追溯 frontmatter 字段：`canonical_key`、`promotion_id`、`work_id`、`correlation_id`。它们是 provenance 元数据，不是新状态字段；缺少 lineage 值时不猜造。Research task 在既有 agenda/log 中以紧凑文本记录适用字段。稳定页继续通过 `source_raw` / wikilink 回到 source summary 或 Research 依据，不复制整套运行元数据。后续 Monthly Reuse 可从外部 promotion/work 记录和 Git commit 定位最近样本，并检查稳定页是否进入后续回答或持久化 Output。

## 完成契约

逐项回报 `work_id`、operation/kind、适用的 canonical/promotion/correlation 标识、结果、去重/证据依据、实际 wiki paths、resulting commit（如已提交）与验证结果。`compiled` 必须通过现有 compile 门与 wiki lint；Research 与 maintenance 按各自 lint/audit/git 门验证。只有实际仓库变更才按 README 和 `schema/git-commit-spec.md` 显式暂存、提交、推送。`no_delta` / `duplicate` 不制造空知识提交；`source_gap` / `blocked` 说明缺口与恢复条件。不要生成 digest、文章或额外运行报告，不新增仓库内运行账本。
