---
title: "Entity 规范与概念筛选标准"
type: schema-subdoc
---

> 本文档是 Agentic Work Atlas Schema 子文档，由 README.md 路由表按需加载。

# Entity 规范与概念筛选标准

Entity 不是术语抽取结果，而是可复用的知识节点。默认立场是**不建**：只有当独立页面能降低未来理解成本、承载多源综合或作为 topic/comparison 的枢纽时，才建立 Entity。

## Entity 准入信号

新建 Entity 前至少满足以下 2 项；只满足 1 项时，优先写入 source summary 或 topic 小节。

| 信号 | 判定标准 |
|------|---------|
| 多源复用 | 已在 2 篇以上 raw 中出现，或确定会在后续主题中持续复用 |
| Topic 承载 | 某个 topic/comparison 需要它作为结构节点 |
| 概念稳定 | 是明确命名的方法论、框架、范式、协议或长期概念 |
| 冲突整合 | 不同来源对它有不同定义、前提或边界，需要独立页记录 |
| 高查询价值 | 未来很可能被直接问"什么是 X"或用于跨文章比较 |
| Actor 验证 | 作者/组织/项目确有持续来源价值，且可记录 `validated_source` |

| 类型 | 处理方式 | 示例 |
|------|---------|------|
| 工具/产品名 | 默认不建，除非多次复用或是架构关键节点 | OpenClaw, Obsidian |
| 单篇内部细节 | 不建 Entity，放入来源摘要或 topic 小节 | 某次实验参数、单篇指标 |
| 框架/方法论（单篇出现） | 默认不建，除非具有强迁移价值 | HUMAN-3.0, Runtime-RAG |
| 人名（仅提及） | 不建 Entity | Dan-Koe |
| 通用泛概念（单篇出现） | 不建 Entity | AI-Adoption, AI-Transformation |
| 多篇文章重复出现 | 评估后建 Entity | Taste, Agentic-Engineering |

## Entity 留存规则

- **核心 Entity**：多源、topic/comparison 承载，或图谱入链高；保留并持续维护。
- **支撑 Entity**：单源但被多个 Entity 引用；保留，但应补入 topic 或 comparison。
- **候选 Entity**：单源、无 topic/comparison 承载；进入复核队列。
- **降级候选**：单源且无图谱入链；优先合并到更大的 Entity/topic/source summary，除非用户明确需要独立页。
- **删除前置条件**：删除前必须确认内容已迁移到 raw/source summary/topic，且所有 wikilink 已修复。

> **"图谱入链"口径**：本节的"图谱入链"指**知识层互引口径**（被其他 entity 引用），由 `entity-audit.py` 的 `entity_in` 字段提供。区分三档口径（全图入链 / 知识层互引 / 整合层承载）见 `schema/fragmentation-metrics.md`。"无图谱入链"在该口径下指 `entity_in==0`，不等于"全库无人引用"。

## Entity 审计命令

```bash
python3 tools/entity-audit.py --write-report
```

中文报告输出到 `docs/entity-audit-YYYY-MM-DD.md`（`docs/` 已被 Quartz 忽略），分为：
- `keep`：结构价值明确
- `keep-actor`：已验证人物/组织类节点
- `strengthen`：值得保留但需要补来源或链接
- `review`：复核队列；单源且缺 topic/comparison 承载
- `merge-or-demote`：合并或降级队列；单源且无图谱入链
- `疑似重复队列`：基于标题、aliases 和 token overlap 的重复候选；只用于复核，不自动合并

## 重复来源：保留一手来源

同一文章的多语言版本/翻译版本共存时，**只保留一手来源**（原文），删除翻译副本。
- 判断标准：语言（原文优先）、来源层级（X/博客 > 微信转载）、完整性

## Raw 关联概念规范

- 此规范只用于理解和清理历史 raw；新编译禁止向 raw 新增"关联概念"区块。
- 历史 raw 中已有的关联概念必须使用 `[[wikilink]]` 格式，禁止纯文本（如 `- ConceptName` 无效）。
- 所有链接必须指向已存在的 Entity/Topic 页面。
- 新流程的关联概念必须沉淀到 `wiki/sources/`、Entity、Topic 或 Comparison，并确保每条引用都有对应页面。