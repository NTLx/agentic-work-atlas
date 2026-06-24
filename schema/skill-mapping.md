---
title: "ljg 技能与 Wiki 工作流映射"
type: schema-subdoc
---

> 本文档是 Agentic Work Atlas Schema 子文档，由 README.md 路由表按需加载。

# ljg 技能与 Wiki 工作流映射

核心技能（四大环节均会调用）：

| 技能 | 所在环节 | 定位 | Wiki 输出目录 | 编译产出 |
|------|----------|------|-------------|---------|
| **ljg-paper** (读论文) | compile | 论文类文章编译器 | `wiki/entities/` | 8 段式结构 → 浓缩+质疑+对标 + 核心概念提取 |
| **ljg-paper-river** (倒读法) | compile | 研究型论文关系构建器 | `wiki/comparisons/` | 5 层倒读+正向追踪 → 概念演化脉络 + 对比分析维度 |
| **ljg-book** (拆书) | compile | 书籍类 raw 编译器 | `wiki/entities/` | 五件事说清：问题/不证之物/框架/结论/takeaway |
| **ljg-qa** (问答提取) | compile, explore | 信息提问机 | 编译时注入 source summary；探索时生成探测问题 | 核心观点抽成 Q-A 对，为 entity/topic 提供结构化骨架 |
| **ljg-think** (追本之箭) | compile(追加), explore | Topic 深度分析 | `wiki/topics/` | 层层降深（表象→机理→原理→公理）→ 主题深度分析 |
| **ljg-rank** (降秩) | compile(追加), explore | 领域级分析 | `wiki/topics/` | 找 2-3 个不可约生成器 → Topic 核心结构 |
| **ljg-plain** (白话) | audit, produce | 质量控制 | N/A | Entity definition / Output 可读性校验（12 岁可读测试） |
| **ljg-writes** (写作引擎) | produce | 输出放大器 | `wiki/outputs/` | 观点驱动写作 → 博客/笔记作品 |
| **ljg-roundtable** (圆桌) | produce, explore | 多视角辩证 | `wiki/outputs/` 或 `wiki/research/research-agenda.md` | 结构化多立场辩论 → 证伪方向、分歧点、共识边界 |
| **obsidian-markdown** | audit(全环节) | 写入守卫 | N/A（质量门） | **所有 `.md` 文件写入前必调用** — 确保 Obsidian Flavored Markdown 合规 |

辅助技能（特定场景可选，不做强制引导）：

| 技能 | 适用场景 | 定位 | 说明 |
|------|----------|------|------|
| **aihot** | explore | AI 资讯查询 | 查询最新 AI 行业动态，为探索提供外部参照。不是编译工具，只在探索需要"外部现实对照"时使用 |
| **json-canvas** | produce(可选) | Canvas 可视化 | 创建知识结构可视化（.canvas 文件）。仅在用户明确需要图谱类视觉输出时使用 |
| **obsidian-bases** | audit(可选) | 数据视图管理 | 创建审计数据视图（.base 文件）。仅在用户需要交互式数据仪表板时使用 |

不适合纳入知识编译工作流的技能：

| 技能 | 理由 |
|------|------|
| **ljg-relationship** | 人际关系结构分析（移情、阻抗、潜意识模式），属于人际心理分析，不属于知识编译 |

已移除的僵尸映射（磁盘上不存在，schema 引用已过时）：

| 技能 | 替代方案 |
|------|------|
| ljg-read (伴读) | 标准路径三步编译法的浓缩/质疑/对标步骤已覆盖预处理功能 |
| ljg-learn (概念解剖) | ljg-paper + ljg-qa 的组合可覆盖概念拆解功能 |
| ljg-card (铸) | 暂无替代；如需传播卡片，用户可手动制作或后续恢复该技能 |