---
title: "Compile 操作注意事项"
type: schema-subdoc
---

> 本文档是 Agentic Work Atlas Schema 子文档，由 README.md 路由表按需加载。

# Compile 操作与 Raw 生命周期

本文件是 Raw 收录、编译后去留和周期性压缩审计的唯一规则源。

## 收录门

收到附件或 URL 时先判题，再选择一个结果：

- **不收录**：主题外、重复转载、低信息密度或已有更好一手来源；仓库不写入。
- **Source 需求**：方向相关但当前不值得保存全文；只登记到 research agenda。
- **全文剪藏**：包含独特证据、来源脆弱、用户私有，或需要离线编译；写入 `raw/` 并注册为 `pending`。

全文剪藏不承诺永久保留。材料完成编译后必须结算 Raw 生命周期。

## 两个正交状态

Registry 的 `status` 表示编译状态：`pending / compiled / skipped`。

Registry 的 `raw_state` 表示证据保留状态：

| 状态 | 工作树 | 使用条件 |
|------|--------|----------|
| `full` | 原始全文存在于 `raw/` | 来源不可可靠恢复、仍被活跃 Claim 使用，或包含尚未迁移的独特证据 |
| `index` | 原始全文不在工作树 | 已编译，有同名 source summary、稳定一手地址、正文摘要哈希和证据定位 |
| `removed` | 原始全文不在工作树 | 主题外、重复、低质量或已被更好一手来源替代；保留删除墓碑 |

历史 Registry 条目没有 `raw_state` 时按 `full` 解释。

## 去留判定

按以下顺序裁决：

1. 主题外、重复转载或低质量且无独特证据 → `removed`。
2. 活跃 Claim 正在直接使用，或来源私有、脆弱、无法恢复 → `full`。
3. 可以从 canonical URL、DOI、arXiv 或官方仓库恢复，且 source summary 已记录关键证据定位 → `index`。
4. 无法确认恢复能力 → 保持 `full`，登记缺失信息，不猜测。

“已经编译”只是进入判定的前提，不等于可以删除。source summary 是证据地图，不是独立 Evidence。

## 状态变更纪律

- `full` 正文不可改；frontmatter 仅做阻断性最小修复。
- 降级必须在同一个 commit 中更新 source summary、Registry、引用和原文件。
- `index` 必须保留原 `body_sha256`、`summary_path`、`canonical_url` 和 `indexed_at`。
- `removed` 必须保留 `retired_at` 与 `retire_reason`；是否保留 source summary 取决于它是否仍承担导航或历史说明。
- `set-raw-state` 只修改 Registry，不删除文件；调用者显式处理文件并运行 lint。
- 不在本仓库创建 `archive/` 存放全文。需要离线副本时使用仓库外冷存储，并可在 Registry 记录 `archive_uri`。

生命周期命令以 `tools/compile_registry.py --help` 为准。典型顺序：先完成 source summary 与恢复信息，再移除原文件、设置状态、运行 lint。

## 编译写入边界

- 新编译写入 `wiki/sources/`，不向 raw 正文追加摘要。
- 优先更新已有 Entity/Topic；新 Entity 必须满足 `schema/entity-spec.md` 的准入门槛。
- 单篇材料暴露的新问题进入 `explore`，不由 compile 自动触发圆桌、盲区扫描或第二个研究主题。
- git 只显式暂存本轮文件；从仓库根目录运行命令。
- X/Twitter 作者已有 Entity 时使用 `[[Author-Name]]`，否则使用纯文本。
