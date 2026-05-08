---
type: lint-report
title: "Lint Report"
date: "2026-05-08"
score: 98
previous_score: 100
---

# Lint Report — 2026-05-08

## 健康度: 98/100 (100 → 98, -2)

---

## 检查项汇总

| 检查项 | 状态 | 发现 | 扣分 |
|-------|------|------|------|
| Raw backlog | ✅ | 36 个 raw 全部编译 | 0 |
| 孤儿 entity | ✅ | 1 个作者 entity（正常） | 0 |
| 失效链接 | ✅ | 0 处断裂 | 0 |
| 一致性检查 | ✅ | 无冲突 | 0 |
| Entity 完整性 | ✅ | 概念 entity 全部完整 | 0 |
| 孤岛检测 | ⚠️ | 2 个新 entity | -2 |
| 摘要覆盖 | ✅ | 36/36 已覆盖 | 0 |
| Comparison 元数据 | ✅ | 6/6 | 0 |

---

## 孤岛检测详情 (-2 分)

| Entity | 入链 | 出链 | 说明 |
|--------|------|------|------|
| [[Elon-Musk]] | 1 | 0 | 今日新建 |
| [[达珍]] | 0 | 0 | 今日新建作者 entity |

**判断**: 不修复。两个 entity 均为今日 `compile(musk-question-requirements)` 新建，后续编译会自然累积链接。

---

## Index 同步修正

- Comparison 计数: 声明 4 → 修正为 6（补全 `Taste-vs-Judgment` 和 `Vibe-Coding-vs-Software-2.0`）

---

## 知识库状态统计

| 类别 | 数量 |
|------|------|
| Raw Sources | 36 |
| Entities | 101 (概念 + 作者) |
| Topics | 15 |
| Comparisons | 6 |
| **总计** | **158** |

---

*本报告由 Clips LLM Wiki Lint 工作流自动生成*
