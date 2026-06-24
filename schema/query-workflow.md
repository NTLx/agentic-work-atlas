---
title: "Query 工作流（知识检索）"
type: schema-subdoc
---

> 本文档是 Agentic Work Atlas Schema 子文档，由 README.md 路由表按需加载。

# Query 工作流（知识检索）

## 检索优先级

```
1. Schema (README.md)  → 了解知识库边界和结构
2. index.md            → 快速定位相关内容
3. Entity pages        → 概念定义和关联
4. Topic pages         → 主题深度分析
5. Raw sources         → 原始证据（仅溯源时）
```

## 查询模式

| 模式 | 示例查询 | 检索路径 |
|-----|---------|---------|
| 概念查询 | "什么是 Knowledge Work?" | Schema → index → Entity → Raw |
| 主题查询 | "关于 AI 替代有什么讨论？" | Schema → index → Topic → Entities |
| 对比查询 | "A 和 B 有什么区别？" | Schema → index → comparisons |
| 溯源查询 | "这个观点来自哪篇文章？" | Wiki → Raw → source URL |

## Query 增强（ljg 驱动）

| 增强 | 方式 | 效果 |
|------|------|------|
| **ljg-qa 问答提取** | 对查询中的概念调用 ljg-qa | Q-A 对直接回答"什么是 X"并提供推理链 |
| **ljg-think 追本之箭** | 对复杂观点/现象调用 ljg-think | 层层降深，揭示底层结构 |
| **ljg-roundtable 圆桌** | 对有争议的话题调用 ljg-roundtable | 多立场辩证，暴露分歧和共识边界 |
