---
title: "Research 模块规范"
type: schema-subdoc
---

> 本文档是 Agentic Work Atlas Schema 子文档，由 README.md 路由表按需加载。

# Research 模块规范

Research 是与 entities / topics / comparisons / sources / outputs 并列的 Wiki 模块，承载未验证问题、活跃假设和深度思考记录。它不是事实层，而是"我们正在研究什么"的操作层。

## 目录结构

```
wiki/research/
├── research-agenda.md          ← 活跃议程（cron 输入/输出索引，保持 ≤300 行）
└── research-logs/
    └── YYYY-MM-DD.md           ← 每日思考日志归档（按日期拆分）
```

## 渐进式披露

Research 模块的核心设计原则：**操作层紧凑，详情归档**。

- **research-agenda.md** 是 cron 深度思考 Agent 的输入文件，必须保持紧凑（≤300 行）。只保留操作节（选焦点用）和索引（溯源用）。
- **research-logs/** 存放完整思考日志，按日期拆分，按需查阅。
- **最近思考结论摘要**：agenda 内维护一张表格（最近 5 条结论精华），作为 cron Agent 的短期记忆桥接，避免重复探索已收敛的问题。

## Research Agenda Frontmatter

```yaml
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

## Research Log Frontmatter

```yaml
---
type: research-log
title: "研究日志 YYYY-MM-DD"
date: "YYYY-MM-DD"
tags:
  - research-log
  - deep-thinking
---
```

## 生命周期规则

| 状态 | 条件 | 处理 |
|------|------|------|
| 活跃 | 有 source 需求、待验证或待证伪 | 保留在 agenda 操作节 |
| 收敛 | 已被 compile/output 消化，或已有 source 支撑 | 移入 `## 已收敛的操作原则`，从活跃节删除 |
| 休眠 | 长期无进展、无 source 支撑、无 output 使用 | 归档到 research-logs/ 或直接删除 |

agenda 条目不得无限累积。当条目长期停留在活跃状态而无进展时，应在 explore 环节中决定：补 source、归档或删除。

## 操作边界

以下规则约束 Research 模块的写入行为，防止未验证内容伪装为稳定知识：

- **不新增目录**：不建 `explore/`、`audit/`、`claims/` 等子目录；所有研究内容在 `wiki/research/` 内完成。
- **不建一次性知识页**：单次思考的结论不直接创建 entity/topic；先沉淀到 agenda 或 research-logs，经验证后再升级。
- **agenda 不是事实源**：`evidence_level: low` 的页面不能单独支撑 output 新判断升级；agenda 条目同理。
- **每次思考后更新索引**：在 research-agenda.md 中更新"最近思考结论摘要"表格（保持 5 行）和"思考日志索引"。
