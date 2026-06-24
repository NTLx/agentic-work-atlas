---
title: "Compile 操作注意事项"
type: schema-subdoc
---

> 本文档是 Agentic Work Atlas Schema 子文档，由 README.md 路由表按需加载。

# Compile 操作注意事项

- **先判题后编译** — 新 raw 在进入编译流程前，必须先按“主题宪法”和“Raw 价值评判与去留原则”判断是否属于主线；不属于则归档或剔除，而不是机械编译
- **不要修改 raw 正文** — raw 是只读证据层；历史 raw 中已有 `## 编译摘要` 保留，新编译必须更新 `wiki/sources/` 与 Wiki 层，避免污染原文 source of truth
- **raw 元数据修复要最小化** — 仅当 frontmatter、日期、文件名或链接安全阻断 lint/渲染时才改 raw；不得把作者补全、概念关系或编译判断当作 raw 修复
- **git add 必须从根目录执行** — 子目录执行 `git add -A` 会意外添加外部符号链接（.codebuddy/ 等），应 `cd /Users/lx/Obsidian/Clips && git add <target-dir>/`
- **X/Twitter 剪藏 author 格式**：若 Author Entity 已存在，用 `[[Author-Name]]` wikilink 格式；若不存在，先用纯文本