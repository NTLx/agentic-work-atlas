---
title: "YAML Frontmatter 规范"
type: schema-subdoc
---

> 本文档是 Agentic Work Atlas Schema 子文档，由 README.md 路由表按需加载。

# YAML Frontmatter 规范

## Raw Sources

Raw frontmatter 是剪藏元数据，不是编译产物。编译阶段不得为了"补全知识图谱"而回写 raw frontmatter 或正文；作者、概念、主题等结构化关系应写入 `wiki/sources/`、Entity、Topic 或 Comparison。只有 metadata 本身导致 lint/渲染/链接失败时，才允许最小修复。

Raw 生命周期由 `state/raw-registry.json` 管理。`raw_state: full` 时原文件必须存在且正文不可改；`index` 时原文件从当前工作树移除，由同名 source summary 保存 canonical URL、原始正文摘要哈希与证据定位；`removed` 只保留 Registry 墓碑及必要的删除说明。

为兼容历史页面，稳定页的 `source_raw` 表示“原始证据身份”：`full` 时链接到 `raw/` 全文，`index` 时同名链接落到 source summary，并由 Registry 的 canonical URL 与哈希恢复原文。`removed` 不再是可用 Evidence，禁止继续出现在稳定页的 `source_raw` 中。

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

> 修改 stable Wiki 页面**知识正文**时必须同步更新 frontmatter 的 `updated` 日期；纯格式修复（不改变知识内容）除外。`stale-core` 检查依赖该字段判断知识老化。

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

### Typed Relations（可选）

绝大部分概念关系使用 `related_entities` 表达，其语义是「两个概念存在值得导航的关联」。

仅当**关系方向本身具有推理价值**时才使用可选 `relations` 字段。判断标准：如果不知道关系的方向和类型，会不会影响未来理解或推理？会才使用；否则 `related_entities` 即可。

```yaml
related_entities:
  - "[[Context-Engineering]]"
  - "[[Agent-Harness]]"
relations:
  depends_on:
    - "[[Agent-Verification]]"
  enables:
    - "[[Agent-Autonomy]]"
```

第一版只允许下列六种 predicate，不继续扩展：

| Predicate | 含义 |
|-----------|------|
| `is_a` | A 是 B 的一种 |
| `part_of` | A 是 B 的组成部分 |
| `depends_on` | A 成立或运行依赖 B |
| `enables` | A 使 B 成为可能 |
| `contradicts` | A 与 B 的核心判断存在实质冲突 |
| `supersedes` | A 在特定语境下取代 B |

规则：
- `relations` 只允许出现在 `type: entity` 页面，target 只能指向 `wiki/entities/` 下的实体（Entity → Entity）。
- Entity → Source 的证据链继续用 `source_raw`；Entity → Topic 的导航继续用普通 wikilink。
- 不要为「图谱更完整」写 `related_to` 之类的空泛 predicate——它与 `related_entities` 重复。
- 不强制所有页面都有 `relations`；没有推理价值就省略。
- Target 使用 kebab-case wikilink（`[[Agent-Verification]]`）；lint 校验页面类型、predicate 白名单与 target 是否指向实体。

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
