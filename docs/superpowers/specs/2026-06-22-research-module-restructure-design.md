# Research 模块重构设计规格

**版本**: v1.0
**创建日期**: 2026-06-22
**状态**: 已批准

---

## 背景与动机

`wiki/research-agenda.md` 膨胀到 918 行（110KB），其中 62 条思考日志占 68%。该文件同时承担双重角色：
1. **输入**：cron 深度思考 Agent 从中选取焦点（待证伪判断、待验证问题）
2. **输出**：每次思考后追加日志条目

两个角色叠加导致文件持续增长，影响 Agent 上下文效率和可读性。

## 设计目标

1. **渐进式披露**：操作节（选焦点）保持紧凑可见；完整日志归档到独立文件按需查阅
2. **正式 Research 模块**：`wiki/research/` 成为与 entities/topics/comparisons 并列的 Wiki 模块
3. **Quartz 发布**：Research 模块自动成为可访问的网页
4. **cron 兼容**：深度思考工作流的双重角色（输入+输出）正常运行

## 目录结构

```
wiki/research/
├── research-agenda.md          ← 操作层（~300 行）
└── research-logs/
    ├── 2026-06-20.md           ← 1 条日志
    ├── 2026-06-21.md           ← 38 条日志
    └── 2026-06-22.md           ← 23 条日志
```

## research-agenda.md 重构

### 保留（操作节，cron 读取）

当前研究焦点、概念去重候选、活跃假设、待证伪判断、Source 需求队列、下一步最小实验、待验证问题、下一批剪藏方向、已收敛的操作原则、暂不做。

### 新增：最近思考结论摘要

在"暂不做"之后插入，保留最近 5 条思考结论精华（表格形式），为 cron 提供短期记忆。

### 新增：思考日志索引

链接到 `wiki/research/research-logs/YYYY-MM-DD.md` 归档文件。

### 移除

line 293-918 的 62 条完整思考日志 → 移入归档文件。

## 归档文件格式

每个 `wiki/research/research-logs/YYYY-MM-DD.md`：
- frontmatter: type=research-log, date, tags=[research-log, deep-thinking]
- 当日所有思考日志条目，按时间倒序排列

## Cron Prompt 变更

### 路径更新（6 处）

| 原文 | 更新为 |
|------|--------|
| `research-agenda.md 的"待证伪判断"节` | `wiki/research/research-agenda.md 的"待证伪判断"节` |
| `research-agenda.md 的"待验证问题"节` | `wiki/research/research-agenda.md 的"待验证问题"节` |
| `在 research-agenda.md 末尾追加` | `在 wiki/research/research-logs/YYYY-MM-DD.md 追加` |
| `在 research-agenda.md 的"思考日志"区块` | `在 wiki/research/research-logs/YYYY-MM-DD.md` |
| `在 research-agenda.md 的"待证伪判断"节` | `在 wiki/research/research-agenda.md 的"待证伪判断"节` |
| `只进 research-agenda` | `只进 wiki/research/research-agenda.md` |

### 新增规则

- **规则 6**：每次思考后更新 research-agenda.md 的"最近思考结论摘要"表格（保持 5 行）和"思考日志索引"
- **短期记忆加载**：阶段 1 选焦点前先阅读"最近思考结论摘要"，避免重复探索

## Schema 变更（README.md）

- 两处 `wiki/research-agenda.md` 路径更新为 `wiki/research/research-agenda.md`
- 两层架构图新增 `research/` 子目录

## 兼容性

| 组件 | 影响 | 说明 |
|------|------|------|
| Quartz | 无需改动 | `wiki/` 不在 ignorePatterns 中 |
| wiki-lint.py | 无需改动 | `path.name` 匹配文件名，`wiki.rglob("*.md")` 覆盖子目录 |
| wikilink | 无需改动 | `[[research-agenda]]` 基于文件名解析，Obsidian shortest-path 兼容 |
| index.md | 无需改动 | 当前未引用 research-agenda |

## 迁移步骤

1. 创建 `wiki/research/research-logs/` 目录
2. 从 `wiki/research-agenda.md` 提取 62 条日志，按日拆分写入 3 个归档文件
3. 在 research-agenda.md 中新增"最近思考结论摘要"和"思考日志索引"节
4. 删除原文件中的 62 条完整日志
5. `git mv wiki/research-agenda.md wiki/research/research-agenda.md`
6. 更新 `tools/daily-thinking-agent-prompt.md` 路径引用
7. 更新 `docs/superpowers/specs/2026-06-20-daily-thinking-agent-design.md`（v1.0→v1.1）
8. 更新 `README.md` Schema 路径引用
9. 运行 lint 验证
10. 提交并推送

## 用户审阅项

1. ✅ 目录结构：`wiki/research/` 含 agenda + research-logs/
2. ✅ 渐进式披露：操作节保留，日志归档，摘要桥接
3. ✅ Cron 兼容：路径更新 + 短期记忆加载 + 摘要更新规则
4. ✅ Quartz 自动发布，lint/wikilink 无需改动
5. ✅ 用户自行更新 cron 任务配置
