---
type: lint-report
title: "Lint Report"
date: "2026-05-01"
score: 98.6
previous_score: 100
---

# Lint Report - 2026-05-01

## 健康度: 98.6/100 (100 → 98.6, -1.4)

---

## 检查项汇总

| 检查项 | 状态 | 发现 | 扣分 |
|-------|------|------|------|
| Raw backlog | ✅ | 所有 34 个 raw 文件已包含编译摘要 | 0 |
| Entity 完整性 | ✅ | 77 个概念 entity 全部包含三个标准章节 | 0 |
| 失效链接 | ✅ | 3 处断裂，全部修复 | -2.0 |
| 孤儿 entity | ✅ | 2 个孤儿已关联到 topic | -0.9 |
| 孤岛检测 | ✅ | 未发现孤岛页面 | 0 |
| 一致性检查 | ✅ | 未发现定义冲突 | 0 |
| Comparison 元数据 | ✅ | 所有 comparison 有 updated 字段 | 0 |
| 作者验证字段 | ✅ | 1 个缺失已修复 | -0.5 |

---

## 修复记录

### 1. 失效 Wikilink 修复 (3 处)

**问题文件**: `wiki/topics/Enterprise-Ontology-Application.md`

| 原链接 | 修复后 |
|--------|--------|
| `[[20260420-ontology-enterprise-ai-agent.md]]` | `[[20260420-ontology-enterprise-ai-agent]]` |
| `[[20260420-build-first-business-ontology.md]]` | `[[20260420-build-first-business-ontology]]` |
| `[[20260420-ontology-meets-agent-case-study.md]]` | `[[20260420-ontology-meets-agent-case-study]]` |

**问题**: source_raw wikilink 包含 `.md` 后缀，不符合规范。

---

### 2. 孤儿 Entity 修复 (2 个)

| Entity | 修复方式 |
|--------|----------|
| `Class` | 在 Enterprise-Ontology-Application topic 的表格中添加 wikilink |
| `Individual` | 在 Enterprise-Ontology-Application topic 的表格中添加 wikilink |

---

### 3. 作者验证字段修复 (1 个)

**Entity**: `Memex.md`

**添加字段**:
```yaml
validated_source: "https://www.theatlantic.com/magazine/archive/1945/07/as-we-may-think/303881/"
validated_at: "2026-05-01"
```

---

## 知识库状态统计

| 类别 | 数量 |
|------|------|
| Raw Sources | 34 |
| Entities | 97 (概念 77 + 作者 20) |
| Topics | 14 |
| Comparisons | 4 |
| **总计** | **149** |

---

## 建议

1. **Wikilink 规范**: 所有 wikilink 必须使用 kebab-case，禁止 `.md` 后缀
2. **新建 Entity 检查**: 创建后确认是否被相关 topic 引用
3. **作者 Entity**: 必须填写 `validated_source` 和 `validated_at`
4. **定期 Lint**: 建议每月执行一次完整 lint 检查

---

*本报告由 Clips LLM Wiki Lint 工作流自动生成*
