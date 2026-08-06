---
type: lint-report
title: "Agentic Work Atlas Lint 报告"
date: "2026-08-06"
score: 100
status: "PASS"
tags:
  - lint-report
  - wiki-maintenance
---

# Agentic Work Atlas Lint 报告 - 2026-08-06

> [!summary] 状态
> 门禁: **PASS**
> 分数: **100/100**
> 阻断问题: **0**

## 统计

| 类别 | 数量 |
|------|------|
| Raw 来源 | 244 |
| Raw 已编译 | 236 |
| Raw 待编译 | 8 |
| Raw 已跳过 | 0 |
| Entity | 368 |
| Topic | 33 |
| Comparison | 19 |
| Output | 10 |

## 待编译 Raw

- `raw/202310-superlinear-returns.md`
- `raw/20260802-lenny-cpo-regrets-product-management-whatnot.md`
- `raw/20260803-google-agent-skills-build-test-scale.md`
- `raw/20260803-latent-space-inference-engineering-baseten.md`
- `raw/20260804-agent-development-lifecycle-adlc.md`
- `raw/20260804-astro-software-factory-issue-triage.md`
- `raw/20260804-stacked-prs-giant-ai-generated.md`
- `raw/20260805-how-we-use-ai-cloudflare-os.md`

## 检查项

| 检查项 | 问题数 |
|--------|--------|
| `frontmatter` | 0 |
| `date` | 0 |
| `hidden-char` | 0 |
| `mathjax` | 0 |
| `wikilink` | 0 |
| `source_raw` | 0 |
| `tag` | 0 |
| `evidence` | 0 |
| `low-evidence` | 6 |
| `stale-core` | 3 |
| `entity` | 0 |
| `comparison` | 0 |
| `index` | 0 |
| `registry-consistency` | 0 |

## 问题明细

### low-evidence

- `wiki/entities/Alpha-Transfer.md` - `低证据页面 Alpha-Transfer 只能作为补 source 或探索线索`
- `wiki/sources/20260715-anthropic-talent-strategy-2026.md` - `低证据页面 20260715-anthropic-talent-strategy-2026 只能作为补 source 或探索线索`
- `wiki/sources/20260727-palantir-ai-sovereignty-alpha-playbook.md` - `低证据页面 20260727-palantir-ai-sovereignty-alpha-playbook 只能作为补 source 或探索线索`
- `wiki/sources/20260730-palantir-industry-ai-unified-namespace.md` - `低证据页面 20260730-palantir-industry-ai-unified-namespace 只能作为补 source 或探索线索`
- `wiki/sources/20260730-palantir-ontology-connecting-agents-to-decisions.md` - `低证据页面 20260730-palantir-ontology-connecting-agents-to-decisions 只能作为补 source 或探索线索`
- `wiki/sources/20260730-palantir-secure-rapid-software-development-sscs.md` - `低证据页面 20260730-palantir-secure-rapid-software-development-sscs 只能作为补 source 或探索线索`

### stale-core

- `wiki/entities/Boris-Cherny.md` - `核心页 Boris-Cherny 已 90 天未更新，入链 10 条`
- `wiki/entities/Claude-Code-CLI.md` - `核心页 Claude-Code-CLI 已 90 天未更新，入链 38 条`
- `wiki/entities/Judgment.md` - `核心页 Judgment 已 90 天未更新，入链 57 条`

## 运行命令

```bash
uv run --with pyyaml python tools/wiki-lint.py --fix-index --write-report
```

*本报告由 `tools/wiki-lint.py` 生成。*
