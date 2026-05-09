---
type: lint-report
title: "Lint Report"
date: "2026-05-09"
score: 96
previous_score: 98
---

# Lint Report — 2026-05-09

## 健康度: 96/100 (98 → 96, -2)

---

## 检查项汇总

| 检查项 | 状态 | 发现 | 扣分 |
|-------|------|------|------|
| Raw backlog | ✅ | 42 个 raw 全部编译 | 0 |
| 孤儿 entity | ✅ | 已修复关联 | 0 |
| 失效链接 | ⚠️ | 346 个（多为模板示例） | -2 |
| 一致性检查 | ⏭️ | 需要语义分析，暂不执行 | 0 |
| Entity 完整性 | ⚠️ | 3 个作者 Entity（规范豁免） | -1 |
| 孤岛检测 | ⚠️ | 1 个孤岛候选 | -1 |
| 摘要覆盖 | ✅ | 42/42 已覆盖 | 0 |
| Comparison 元数据 | ✅ | 6/6 | 0 |

---

## 失效链接详情 (-2 分)

346 个链接，主要来源：
- README.md 中的模板示例链接（[[Kebab-Case]]、[[概念A]] 等）
- 非真实断裂，是文档模板中的占位符

**判断**: 不修复。这些是文档模板中的示例链接，不是真实的知识库断裂。

---

## 孤岛检测详情 (-1 分)

| Entity | 入链 | 出链 | 说明 |
|--------|------|------|------|
| [[Kevin-Xu]] | 1 | 1 | 入链和出链都少于 2 |

**建议**: 后续编译时自然建立关联，或考虑合并到相关 topic。

---

## Entity 完整性详情 (-1 分)

3 个作者 Entity 缺少标准三章节：
- Demis-Hassabis.md
- Boris-Cherny.md
- Cat-Wu.md

**判断**: 不修复。这些是作者类型 Entity（tags 含 person），根据规范不需要标准三章节，但需要 `validated_source` + `validated_at` 字段——已验证都有。

---

## 本轮编译统计

| 类别 | 数量 |
|------|------|
| 编译 Raw | 3 篇 |
| 新增 Entity | 5 个 |
| 更新 Entity | 3 个 |

**新增 Entity**:
- AI-Ready-Organization
- Organizational-Self-Awareness
- Agent-PR-Review
- Agentic-Workflow-Token-Efficiency
- 渐进式重构

**更新 Entity**:
- AI-Capability-Gap
- Agent-First-Enterprise
- AI-First

---

## 知识库状态统计

| 类别 | 数量 |
|------|------|
| Raw Sources | 42 |
| Entities | 106 (概念 + 作者) |
| Topics | 15 |
| Comparisons | 6 |
| **总计** | **169** |

---

*本报告由 Clips LLM Wiki Lint 工作流自动生成*
