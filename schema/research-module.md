---
title: "Research 模块规范"
type: schema-subdoc
---

> 本文档是 Agentic Work Atlas Schema 子文档，由 README.md 路由表按需加载。

# Research 模块规范

Research 是与 entities / topics / comparisons / sources / outputs 并列的 Wiki 模块，承载未验证问题、活跃假设和深度思考记录。它不是事实层，而是"我们正在研究什么"的操作层。

> **运行行为归属**：Recompile 的选择、Gap 判断、Action、Delta 与稳定页写入规则，统一以 `schema/recompile-workflow.md` 为准。本文档不重复定义运行行为，只维护 Research 的数据结构、生命周期与日志规则。

## 目录结构

```
wiki/research/
├── research-agenda.md          ← 活跃议程（cron 输入/输出索引，保持紧凑）
└── research-logs/
    └── YYYY-MM-DD.md           ← 每日思考日志归档（按日期拆分）
```

## 渐进式披露

Research 模块的核心设计原则：**操作层紧凑，详情归档**。

- **research-agenda.md** 是定时 Claim Recompile Agent 的输入文件，必须同时满足：≤300 行、≤60 KB、最长单行 ≤600 字符。只保留操作节和索引；解释 Delta 所需的详情进入日志。
- **research-logs/** 存放证据、关键推理和结果构成的紧凑判定链，按日期拆分，按需查阅；不保存 Skill transcript。
- **最近思考结论摘要**：agenda 内维护一张表格（最近 5 条结论精华），作为 cron Agent 的短期记忆桥接，避免重复探索已收敛的问题。

## Claim Recompile Queue

`research-agenda.md` 维护 `## Claim Recompile Queue`，作为定时重编译的唯一选题入口。队列最多保留 12 个活跃 Claim；发现新问题属于普通 `explore`，不能由 recompile 扫描全库生成。

每个 Claim 使用稳定 ID，并保持字段紧凑：

```markdown
### CR-001 · Claim 简称
- Status: ready | blocked | resolved
- Priority: P0 | P1 | P2
- Claim: 一句可判断真伪或边界的命题
- Gap: Evidence | Counterexample | Boundary | Mechanism
- Evidence: raw/<精确文件名> | <一手 URL>；source summary 只作导航，同源只计一次
- Evidence goal: 什么观察会改变判断
- Last checked: YYYY-MM-DD · delta
- Next: 下一步唯一主要动作
- Retry: now | YYYY-MM-DD | new-source:<目标>
```

选择规则：`Status: ready`、Retry 条件已满足、最近未检查、再按优先级与 `Last checked` 最旧者选择；`blocked` 必须写明恢复条件。具体选择与可行动条件判定以 `schema/recompile-workflow.md` 为准。

## Recompile Delta

Delta 的类型、Basis 检查、证据单位约束与"一次检查只记录一个 Delta"的规则，属于 recompile 运行行为，统一以 `schema/recompile-workflow.md` 为准。本文档不重复定义。

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
| 收敛 | Claim 已 falsified、已解决或没有下一动作 | 从 Queue 移除，结果保留在 research log；晋升候选交给 compile/audit |
| 休眠 | 长期无进展、无 source 支撑、无 output 使用 | 标为 blocked 并写 Retry，或由普通 explore 归档/删除 |
| 历史冗余 | 无 agenda/稳定页引用、无独特 Evidence locator，且结论已迁移或没有 decision-grade 增量 | 从工作树删除；在日志索引记录范围与可恢复 Git commit |

agenda 条目不得无限累积。当条目长期停留在活跃状态而无进展时，应在 explore 环节中决定：补 source、归档或删除。

Research 日志也不永久保留。压缩前必须检查 Wiki/agenda 反向引用；删除批次必须可从一个明确 Git commit 恢复。不要在仓库内另建 archive 复制全文，也不要把 transcript 重写成另一份长摘要。

## 操作边界

以下规则约束 Research 模块的写入行为，防止未验证内容伪装为稳定知识：

- **不新增目录**：不建 `explore/`、`audit/`、`claims/` 等子目录；所有研究内容在 `wiki/research/` 内完成。
- **不建一次性知识页**：单次思考的结论不直接创建 entity/topic；先沉淀到 agenda 或 research-logs，经验证后再升级。
- **agenda 不是事实源**：`evidence_level: low` 的页面不能单独支撑 output 新判断升级；agenda 条目同理。
- **定时重编译边界**：recompile 对稳定页的修改权限、每轮动作预算与 promotion candidate 机制，以 `schema/recompile-workflow.md` 为准，本文档不重复定义。
- **外部搜索先登记**：尚未 clip/compile 的 URL 只进入日志和 Source 需求队列，不进入稳定 Wiki。
- **每次思考后更新索引**：在 research-agenda.md 中更新"最近思考结论摘要"表格（保持 5 行）和"思考日志索引"。
