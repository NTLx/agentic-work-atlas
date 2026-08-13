---
type: lint-report
title: "Agentic Work Atlas Lint 报告"
date: "2026-08-13"
score: 100
status: "PASS"
tags:
  - lint-report
  - wiki-maintenance
---

# Agentic Work Atlas Lint 报告 - 2026-08-13

> [!summary] 状态
> 门禁: **PASS**
> 分数: **100/100**
> 阻断问题: **0**

## 统计

| 类别 | 数量 |
|------|------|
| Raw 来源 | 254 |
| Raw 已编译 | 238 |
| Raw 待编译 | 16 |
| Raw 已跳过 | 0 |
| Entity | 370 |
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
- `raw/20260806-openai-chatgpt-work-adoption.md`
- `raw/20260810-the-playbook-for-building-high-talent.md`
- `raw/20260811-databricks-genie-grounding-governance.md`
- `raw/20260811-vasuman-ai-adoption-is-a-myth.md`
- `raw/20260812-github-ai-first-contributors.md`
- `raw/20260812-google-recall-bottleneck-factuality.md`
- `raw/20260813-pl-tokens-token-efficiency.md`
- `raw/20260215-recall-bottleneck-parametric-factuality.pdf`
- `raw/20260731-tragedy-cognitive-commons-ai-expertise.pdf`

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
| `stale-core` | 8 |
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

- `wiki/entities/Agent-Native.md` - `核心页 Agent-Native 已 92 天未更新，入链 10 条`
- `wiki/entities/Agent-PR-Review.md` - `核心页 Agent-PR-Review 已 94 天未更新，入链 16 条`
- `wiki/entities/Boris-Cherny.md` - `核心页 Boris-Cherny 已 97 天未更新，入链 10 条`
- `wiki/entities/Claude-Code-CLI.md` - `核心页 Claude-Code-CLI 已 97 天未更新，入链 38 条`
- `wiki/entities/GBrain.md` - `核心页 GBrain 已 92 天未更新，入链 10 条`
- `wiki/entities/Judgment.md` - `核心页 Judgment 已 97 天未更新，入链 57 条`
- `wiki/entities/Knowledge-Work.md` - `核心页 Knowledge-Work 已 92 天未更新，入链 24 条`
- `wiki/entities/Software-2.0.md` - `核心页 Software-2.0 已 92 天未更新，入链 9 条`

## 运行命令

```bash
uv run --with pyyaml python tools/wiki-lint.py --fix-index --write-report
```

*本报告由 `tools/wiki-lint.py` 生成。*
