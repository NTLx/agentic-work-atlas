---
title: "Lint 工作流（知识审计）"
type: schema-subdoc
---

> 本文档是 Agentic Work Atlas Schema 子文档，由 README.md 路由表按需加载。

# Lint 工作流（知识审计）

| 检查项 | 条件 | 处理方式 |
|-------|------|---------|
| Raw backlog | raw/ 中超过 7 天的文件 | 提醒 compile |
| 孤儿 entity | 无 topic 页面引用的 entity | 关联到相关 topic |
| 失效链接 | wikilinks 指向不存在的页面 | 修复或删除链接 |
| **一致性检查** | 同一概念在不同 Entity 中的定义是否冲突 | 列出冲突位置和建议统一方向 |
| **完整性检查** | Entity 是否包含必填字段（定义、关键数据点、前提与局限性、关联概念） | 标记缺失字段 |
| **孤岛检测** | 入链和出链都少于 2 的页面（仅实体 entities 和对比 comparisons，排除 outputs 和 topics） | 建议建立关联或合并 |
| **摘要覆盖检查** | raw/ 中哪些文件既没有历史 `## 编译摘要`，也没有同名 `wiki/sources/{raw 文件名}.md` source summary | 列出待处理文件 |
| **Comparison 元数据** | 所有 comparison 必须有 `updated` 字段 | 补全缺失 |
| **Tag 质量** | tag 超过 5 个、包含空格/下划线/特殊字符、疑似一次性标签 | 默认非阻断提醒 |
| **证据字段** | `evidence_level` / `claim_type` 取值不合法 | 阻断，必须修正 |
| **低证据页面** | `evidence_level: low` 的页面 | 默认非阻断提醒，只能作为补 source 或探索线索 |
| **过时核心页** | 入链较多且超过 90 天未更新 | 默认非阻断提醒，进入重编译队列 |
| **重复概念候选** | Entity 标题、aliases 或 token 高度重叠 | 进入 entity-audit 复核队列，不自动合并 |

---

## Lint 工具

通用维护脚本放在 `tools/`，不绑定任何 Agent 插件目录。

```bash
uv run --with pyyaml python tools/wiki-lint.py --fix-index --write-report
```

该脚本检查：
- YAML/frontmatter 是否能被 Quartz 解析
- 日期是否为 `YYYY-MM-DD`
- 裸 `$` 是否会触发 Obsidian MathJax（不扫描 raw 原文正文，避免为渲染清洗而改动证据源）
- wikilink 和 `source_raw` 是否指向真实文件
- index.md 计数是否与文件系统一致
- tag 数量和链接安全质量
- 一次性 tag 与低证据页面
- `evidence_level` / `claim_type` 字段取值是否合法
- 入链较多但长期未更新的过时核心页
- Entity 标准章节和作者 Entity 验证字段
- raw 摘要覆盖：历史 raw 内 `## 编译摘要` 或同名 `wiki/sources/` source summary 二者满足其一即可
- raw 只做结构性门禁：frontmatter、日期和 source/raw 链接可追溯；正文清洗类问题不得成为改写 raw 的理由
- `wiki/lint-report.md` 是否可生成当前报告

`tools/` 必须列入 Quartz `ignorePatterns`，避免脚本被当作内容发布。

---

## Entity 章节规范

**概念 Entity**（tags 不含 person）必须包含以下三个标准章节：
1. `## 关键数据点` — 从 raw 源提取的关键数据、统计、事实
2. `## 前提与局限性` — 概念成立的前提条件和适用边界
3. `## 关联概念` — 与其他概念的关系（统一标题，非"相关概念"/"外部链接"等变体）

**作者 Entity**（tags 含 person）不需要以上三章，但必须有：
- `validated_source` + `validated_at` frontmatter 字段

## Lint 评分计算规则

- 每个检查项按权重扣分（总分 100）
- 扣分必须对应具体缺失项数量，不应用主观权重
- 某检查项全部修复后必须恢复满分

## Lint 执行注意事项

- **Agent 结果必须用 grep 二次验证**（文件系统是真相，agent 可能基于过期缓存）
- 失效链接检查中，代码块内的 `[[wikilink]]` 占位符（如教程示例）不算真实断裂
- 评分报告必须列出具体扣分项及每项对应文件，不使用笼统描述
- **blocking vs non-blocking**：`entity`/`mathjax`/`source_raw`/`wikilink`/`frontmatter`/`date`/`evidence` 为阻断级（exit code 1，CI 失败）；`tag`（数量超标、一次性 tag）、`low-evidence`、`stale-core` 为非阻断级（仅警告）。修复 CI 时只关注阻断级问题