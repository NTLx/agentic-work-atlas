---
title: "YAML Frontmatter 规范"
type: schema-subdoc
---

> 本文档是 Agentic Work Atlas Schema 子文档，由 README.md 路由表按需加载。

# YAML Frontmatter 规范

## Raw Sources

Raw frontmatter 是剪藏元数据，不是编译产物。编译阶段不得为了"补全知识图谱"而回写 raw frontmatter 或正文；作者、概念、主题等结构化关系应写入 `wiki/sources/`、Entity、Topic 或 Comparison。只有 metadata 本身导致 lint/渲染/链接失败时，才允许最小修复。

```yaml
---
type: raw
source: "https://example.com/article"
author:
  - "[[Author-Name]]"  # ⚠️ 必须使用 kebab-case 文件名格式（而非 "Author Name"）
  - "作者名"           # 不存在时用纯文本
published: "2026-04-08"
created: "2026-04-08"
tags:
  - clippings
  - {主题标签}
---
```

**历史相关链接部分结构**（仅适用于已有 raw；新编译不再向 raw 新增此区块）：
- 作者 Entity: `[[Author-Name]]`
- 相关概念 entities: `[[Concept-A]], [[Concept-B]]`
- 思想先驱: `[[Memex]]`（如有历史关联）
- 对比分析: `[[Concept-A-vs-Concept-B]]`
- 思想体系 topic: `[[Topic-Name]]`

## Entity Pages

```yaml
---
type: entity
title: {概念名}
aliases:
  - {概念名自然写法}  # 自然语言名称，供 Obsidian "未链接提及" 识别
definition: "{一句话定义}"
created: {YYYY-MM-DD}
updated: {YYYY-MM-DD}
tags:
  - {领域}
related_entities:
  - "[[Concept-A]]"  # ⚠️ 必须使用 kebab-case 文件名格式
source_raw:
  - "[[文章名]]"  # ⚠️ 短链接格式（纯文件名，不含路径）
---
```

**Wikilink 格式规范**：
- ✅ 正确：`[[Vibe-Coding]]`、`[[Software-2.0]]`、`[[Andrej-Karpathy]]`
- ❌ 错误：`[[Vibe Coding]]`、`[[Software 2.0]]`（空格格式会失效）

**引用显示规范**：
- 正文引用 Entity 时优先使用管道语法：`[[Kebab-Case|Natural Name]]`
- 示例：`[[Vibe-Coding|Vibe Coding]]`、`[[Knowledge-Work|Knowledge Work]]`
- 好处：渲染时显示自然名称，同时保持 kebab-case 文件名兼容性

## Author Entity Pages

```yaml
---
type: entity
title: {Author Name}
aliases:
  - {Author Name}  # 自然语言名称，供 Obsidian "未链接提及" 识别
definition: "{一句话定义作者身份}"
validated_source: "https://验证来源URL"
validated_at: "2026-04-13"
created: {YYYY-MM-DD}
updated: {YYYY-MM-DD}
tags:
  - {领域}
source_raw:
  - "[[文章名]]"
---
```

**Author Entity 工作流**：
1. 使用 BrowserOS 搜索验证作者身份
2. 记录验证来源 URL 和日期
3. 无法验证时，文章 author 使用纯文本

## Research 页面

Research 模块有两种页面类型：

```yaml
# research-agenda.md — 活跃议程
---
type: research-agenda
title: "{知识库名} 研究议程"
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags:
  - research-agenda
related_entities:
  - "[[Entity-Name]]"
---
```

```yaml
# research-logs/YYYY-MM-DD.md — 每日思考日志
---
type: research-log
title: "研究日志 YYYY-MM-DD"
date: "YYYY-MM-DD"
tags:
  - research-log
  - deep-thinking
---
```

Research 页面不需要 `source_raw`、`definition` 或 Entity 标准三章节。`research-agenda` 类型不纳入 lint 的 entity 完整性检查。