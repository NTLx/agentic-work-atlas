---
title: "Query 工作流（知识检索与上下文构建）"
type: schema-subdoc
---

> 本文档是 Agentic Work Atlas Schema 子文档，由 README.md 路由表按需加载。
> 本文件同时承担原 `schema/context-pack.md` 的职责（search-first + 有界上下文），不单独维护 Context Pack 文件。

# Query 工作流（知识检索与上下文构建）

## 检索策略：search-first

不再默认从完整 `index.md` 开始。`index.md` 只是人类浏览入口、顶层导航与不知道
搜索什么时的 fallback，不是每次查询的强制上下文。

```text
理解 query
↓
精确搜索标题 / aliases / tag / 关键词（不使用完整 index）
↓
找到 1–3 个 seed pages
↓
必要时沿 wikilink / relations 追一层
↓
打开最终 3–8 个相关页面
↓
必要时回溯 Raw / Source
```

## Intent（只允许五种）

| Intent | 目的 | 示例 |
|--------|------|------|
| `explain` | 理解一个概念 | 什么是 Knowledge Compilation？ |
| `compare` | 比较多个概念/方案 | A 和 B 有什么区别？ |
| `decide` | 支持选择或判断 | 应该选哪个方案？ |
| `explore` | 探索未知问题 | 关于 AI 替代有什么讨论？ |
| `produce` | 生成文章、报告等 | 写一篇分析报告 |

不要继续细分 intent。

## 上下文构建（临时 Context Pack）

Context Pack 是当前任务的内部 working memory，不保存成文件、不新增 YAML。Agent
内部临时判断五个变量：

- `intent`：五种 intent 之一
- `query`：原始问题
- `scope`：检索范围
- `grounding`：需要回链的证据
- `budget`：本次读取预算

内部临时 Context Pack 结构：

```text
Intent:
Query:
Scope:

Relevant pages:
- ...

Core claims:
- ...

Evidence:
- ...

Known boundaries:
- ...

Open gaps:
- ...

Do not assume:
- ...
```

默认不落盘。若保存，落入 `wiki/outputs/`，并在文末加入 `## 回填检查`。

Context Pack 不得直接升级为 entity/topic/comparison。只有其中的新判断通过回填
检查并能回链 raw/source/Wiki，才允许进入稳定 Wiki。

## 查询模式

| 模式 | 示例查询 | 检索路径 |
|-----|---------|---------|
| 概念查询 | “什么是 Knowledge Work?” | search → Entity → 必要时 Source |
| 主题查询 | “关于 AI 替代有什么讨论？” | search → Topic → Entities |
| 对比查询 | “A 和 B 有什么区别？” | search → comparisons |
| 溯源查询 | “这个观点来自哪篇文章？” | Wiki → Raw → source URL |

## 按需使用 Agent Skills

search-first 和 bounded context 优先于 Skill 选择。完成有限检索后，Agent 先判断
上下文是否已经足以回答：

```text
上下文足够 → 直接回答，可以完全不使用 Skill
上下文不足 → 说明最大的理解瓶颈
             ↓
             查看 Runtime 当前发现的 Skill 的 name + description
             ↓
             选择 none 或最小充分的相关 Skill
             ↓
             按需读取 SKILL.md，执行一次 reasoning enhancement
             ↓
             观察结果，必要时重新判断；然后回答
```

这里没有 Query → Skill 的固定映射。概念理解、机制深挖、结构辨认或争议分析都
可能需要不同能力，也都可能在已有上下文充分时不需要 Skill。Skill output 默认
是 Reasoning，不是 Evidence；答案中的事实仍须回链 Wiki、Source 或 Raw，且
遵守 `schema/skill-mapping.md` 的优先级、持久化和副作用边界。

查询只为当前回答建立 bounded context，不因为调用 Skill 自动创建 Entity、Topic、
Comparison、Raw 或外部笔记。
