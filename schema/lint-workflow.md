---
title: "Lint 工作流（知识审计）"
type: schema-subdoc
---

> 本文档是 Agentic Work Atlas Schema 子文档，由 README.md 路由表按需加载。

# Lint 工作流（知识审计）

`tools/wiki-lint.py` 是仓库门禁脚本：存在 blocking issue 时退出码为 1，CI 门禁（`.github/workflows/deploy.yml`）失败。`--fix-index --write-report` 是本地 audit / 维护命令：同步版本化的 `index.md` 计数，并生成 `wiki/lint-report.md`（派生审计产物，不参与 Git commit 一致性门禁）。**本档只描述该脚本实际实现的能力**；脚本未实现的检查见第三节，交给人工审计或独立工具。

## 1. 自动化阻断检查（Blocking）

任一失败即门禁失败（exit code 1，CI 失败）：

| 类别 | 检查内容 |
|------|---------|
| `frontmatter` | YAML 解析失败；双引号标量内疑似未转义双引号 |
| `date` | `published/created/updated/date/validated_at` 必须为 `YYYY-MM-DD` |
| `hidden-char` | 页面正文含零宽字符（raw 原文除外） |
| `mathjax` | 裸露 `$` 会触发 Obsidian MathJax，需反引号包裹或反斜杠转义（raw 原文除外） |
| `wikilink` | wikilink 指向不存在的目标（代码块内占位符不算） |
| `relations` | 仅 `type: entity` 页面可用；predicate 必须属于六种白名单；target 必须指向 `wiki/entities/` 下的实体 |
| `source_raw` | 目标必须存在；`raw_state: removed` 的 Evidence 不可继续引用 |
| `entity` | 必填字段（title / aliases / definition / source_raw）；概念 Entity 的标准三章节；作者 Entity 的验证字段 |
| `comparison` | 必须含 `updated` 字段 |
| `index` | 概览计数与文件系统一致（`--fix-index` 维护；CI 只读校验计数同步） |
| `registry-consistency` | raw 缺 registry 记录、生命周期状态漂移、需重编译候选（含摘要覆盖缺失） |

## 2. 自动化警告检查（Warning）

不阻断门禁，仅记入 `wiki/lint-report.md`：

| 类别 | 检查内容 |
|------|---------|
| `tag` | tags 超过 5 个、非 kebab-case、一次性 tag |
| `low-evidence` | `evidence_level: low` 的页面只能作为补 source 或探索线索 |
| `stale-core` | 入链较多且超过 90 天未更新的核心页 |

## 3. 人工审计 / 独立工具（Manual & Separate）

以下检查**不由 `wiki-lint.py` 承担**，不得据其报告声称已覆盖：

| 项 | 承担方 |
|----|--------|
| 定义冲突（同一概念在不同 Entity 中的定义是否冲突） | 人工审计；lint 不实现跨页语义比对 |
| 孤岛 / 连接度 / 碎片化（图拓扑口径） | `tools/entity-audit.py`；口径定义见 `schema/fragmentation-metrics.md` |
| 重复概念候选（标题/aliases/token 高度重叠） | `tools/entity-audit.py` 复核队列；不自动合并 |
| Raw backlog 提醒（逾期未编译） | 人工触发 compile；lint 只在报告列出"待编译 Raw" |
| Entity 价值 / 主题覆盖 / 幂律结构 | `tools/entity-audit.py` |
| Agent Skill 安装、lock、目录哈希与 Claude 兼容入口漂移 | `tools/skill-audit.py`；只读报告，不参与 Skill 路由 |

## 运行方式

**CI 门禁（只读）**——存在 blocking issue 即失败（exit 1），以 commit 提交日期为 as-of，保证同一 commit 结果恒定：

```bash
AS_OF=$(git show -s --format=%cs HEAD)
uv run python tools/wiki-lint.py --as-of "$AS_OF"
```

CI 不生成、不提交、不比对 `wiki/lint-report.md`；`index.md` 的计数一致性仍由 blocking 的 `index` 检查守护。

**本地 audit / 维护（写模式）**——用于查看完整健康状态：

```bash
uv run python tools/wiki-lint.py --fix-index --write-report
```

`--fix-index` 同步版本化的 `index.md` 计数；`--write-report` 生成 `wiki/lint-report.md` 供本地查看审计详情，该文件被 `.gitignore` 忽略，不要求随 commit 提交。知识变更（compile/recompile 等）只需通过只读校验即可提交，无需强制生成报告。

Skill 供应链审计是独立的只读检查：

```bash
uv run python tools/skill-audit.py
```

它扫描当前 Runtime 的 `SKILL.md`、`skills-lock.json` 和 `.claude/skills/` 软链接，报告 frontmatter、安装/锁定差异、目录哈希漂移及兼容入口问题；不会删除、更新或修复任何 Skill、lock 条目或软链接。发现错误时退出码为 1；警告本身不阻断命令。

## Recompile Guard（只读约束）

定时 Claim Recompile 使用只读检查，避免无知识变化时改写生成文件：

```bash
uv run python tools/wiki-lint.py
python3 tools/recompile-guard.py --base "$BASELINE" --log-date "$RUN_DATE" --max-stable 0
```

Recompile guard 默认只允许本次 Research 日志和 `research-agenda.md`，稳定页上限为 0；只有人工显式传入参数时才可开放既有稳定页或 `index.md`。它同时阻断 raw 变更、新建稳定页、transcript、无关路径、过长日志，以及超过 300 行 / 60 KB / 单行 600 字符的 agenda。完整 index 刷新留给 audit 任务；`wiki/lint-report.md` 为派生审计产物，本地 audit 生成即可，与 recompile 无耦合。

## Entity 章节规范

**概念 Entity**（tags 不含 person）必须包含以下三个标准章节：
1. `## 关键数据点` — 从 raw 源提取的关键数据、统计、事实
2. `## 前提与局限性` — 概念成立的前提条件和适用边界
3. `## 关联概念` — 与其他概念的关系（统一标题，非"相关概念"/"外部链接"等变体）

**作者 Entity**（tags 含 person）不需要以上三章，但必须有 `validated_source` + `validated_at` frontmatter 字段。

## Lint 执行注意事项

- **Agent 结果必须用 grep 二次验证**（文件系统是真相，agent 可能基于过期缓存）
- 失效链接检查中，代码块内的 `[[wikilink]]` 占位符（如教程示例）不算真实断裂
- 修复 CI 时只关注第 1 节阻断项；警告项可暂缓，但应进入维护队列
