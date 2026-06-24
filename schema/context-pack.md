---
title: "Context Pack（有界上下文包）"
type: schema-subdoc
---

> 本文档是 Agentic Work Atlas Schema 子文档，由 README.md 路由表按需加载。

# Context Pack（有界上下文包）

`context-pack(query, budget)` 是给后续 Agent 或输出任务使用的临时上下文，不是稳定知识页面。

生成顺序：
1. 先读 `index.md` 和相关页面 frontmatter，按标题、aliases、tags、summary、入链关系筛候选。
2. 只打开最相关的 3-8 个页面，必要时沿 wikilink 追一层。
3. 输出固定包含：相关页面、核心结论、证据强度、关键 source、已知缺口、不得越界的假设。
4. 默认只在对话中输出；若保存，落入 `wiki/outputs/`，并在文末加入 `## 回填检查`。

Context Pack 不得直接升级为 entity/topic/comparison。只有其中的新判断通过回填检查并能回链 raw/source/Wiki，才允许进入稳定 Wiki。
