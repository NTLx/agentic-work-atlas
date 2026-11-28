---
type: entity
title: Knowledge Compilation
aliases:
  - Knowledge Compilation
definition: "LLM Wiki 的核心操作，将原始知识源通过 LLM 转化为结构化 Wiki，旨在支持知识的持久治理与可验证复用"
created: 2026-04-13
updated: 2026-11-28
evidence_level: high
claim_type: mixed
tags:
  - knowledge-management
  - llm-wiki
  - workflow
related_entities:
  - '[[RAG-vs-LLM-Wiki]]'
  - '[[Context-Engineering]]'
  - '[[Multi-Layer-Memory]]'
  - '[[Andrej-Karpathy]]'
  - "[[Shortification-of-Learning]]"
source_raw:
  - '[[20260413-llm-wiki]]'
  - '[[一篇文章卖了20万，开源CC+Obsidian打造的LLM Wiki 内容创作3.0系统]]'
  - "[[20260602-karpathy-shortification-of-learning]]"
  - '[[20260625-ford-ai-quality-jd-power]]'
  - '[[20260726-berkeley-auto-software-dev]]'
---

# Knowledge Compilation

> **核心操作**：Raw → Wiki 的知识转化过程

## 定义

**Knowledge Compilation**（知识编译）是 LLM Wiki 的核心操作：

> 原始知识源经过 LLM 处理，转化为可追溯的结构化知识，供后续查询复用、纠错、更新与退役；复用收益需要测量。

Karpathy 关于 [[Shortification-of-Learning|学习短视频化]] 的提醒让这个定义更尖锐：保存资料不等于学习资料。Raw source 只是材料在场，编译才是主动加工。没有浓缩、质疑、对标和概念回填，知识库会退化成“看起来收藏了很多，实际每次还要从头理解”的资料堆。

## 与程序编译的类比

| 程序编译 | 知识编译 |
|---------|---------|
| 源代码 | Raw Sources（原始文档） |
| 编译器 | LLM Agent |
| 目标代码 | Wiki 层（Entities、Topics） |
| 运行时 | Query（查询） |
| 调试 | Lint（健康检查） |

## 编译流程（Ingest）

编译是 Raw → Wiki 的知识转化动作。具体执行流程、单次修改范围与运行约束，统一以 `schema/compile-workflow.md` 为准；lint 门禁以 `schema/lint-workflow.md` 与 `tools/wiki-lint.py` 为准。本文档只说明概念定位，不复制运行规则。

核心定位：compile 创建/更新 source summary 与少量已有稳定页面，必要时补充 typed relations 与重要综合判断；新研究问题交给 `explore`，不在 compile 中扩张。

## 编译产物类型

| 产物类型 | 描述 | 示例 |
|---------|------|------|
| **Entity** | 概念定义页面 | Agentic-Engineering.md |
| **Topic** | 主题整合页面 | Agentic-Engineering-Patterns.md |
| **Comparison** | 对比分析页面 | RAG-vs-LLM-Wiki.md |
| **Index** | 内容索引 | index.md |
| **History** | 操作记录 | git commit log |

## 编译 vs 检索

| 维度 | RAG（检索） | Compilation（编译） |
|-----|------------|-------------------|
| 处理时机 | Query 时 | Ingest 时 |
| 处理成本 | 检索及生成，可能有预计算 | 初始编译、持续维护及查询验证，可能减少重复综合 |
| 结果稳定性 | 受索引、检索和生成影响 | 同一版本可回查；知识及回答仍可能变化 |
| 知识累积 | 可有持久索引、缓存、摘要或图谱 | 显式维护可复用判断和证据 |
| 冗余处理 | 切片可能冗余 | 编译时已提炼 |

## 编译质量保障

### 质量门禁

确定性 lint 与语义证据审计是不同的质量门；执行和产物以 `schema/lint-workflow.md` 为准。Lint 通过不证明论断正确，也不保证旧错误已退役。

### 版本控制

Wiki 是 git repo，支持：

- 版本历史（追溯变更）
- 分支管理（实验性编译）
- 协作编辑（团队 Wiki）

## 编译策略

### 单源精细编译

Karpathy 推荐的方式：

> "I prefer to ingest sources one at a time and stay involved — I read the summaries, check the updates, and guide the LLM on what to emphasize."

优势：
- 深度参与知识提炼
- 确保 quality 和 relevance
- 建立个人理解

### 批量快速编译

适用于：

- 初始知识库建设
- 已有大量 raw sources
- 仍满足相同证据、准入与验收质量门；批量不是降低保真要求的理由

## 编译与 Query 的循环

> [!tip] 关键洞察
> **有独立增量且经质量门的查询结果可回填；普通查询默认只读**

```
Query → Answer → File back to Wiki → Compounding
```

示例：
- 对比、分析或关联先作为当前回答或 Output 候选；是否更新稳定页面取决于独立知识增量、证据、准入及晋升边界，不按请求类型自动创建。

这样探索也能累积，不只是 source 编译累积。

---

## 三步编译法（进阶）

> 饼干哥哥在 Karpathy 方案基础上的改进，增加了"质疑"和"对标"两步

### 核心流程

```
原文 → 浓缩 → 质疑 → 对标 → 结构化 Wiki
```

### 第一步：浓缩 (Condense)

- **原则**：用剃刀法则——删掉这条信息会影响理解吗？不会就删
- **输出**：核心结论（不超过 3 条）+ 支撑每条结论的关键证据
- **格式**：每条结论一行，证据缩进在下方

### 第二步：质疑 (Question) — 关键差异

针对每条核心结论，回答：
1. **前提假设**：这个结论依赖哪些前提假设？
2. **边界条件**：如果这些前提不成立（换行业/换市场/换规模），结论还成立吗？
3. **数据可靠**：作者的数据来源可靠吗？样本量、时间范围、地域限制？
4. **反例存在**：有没有作者没提到的反例或边界条件？

> [!important] 质疑的价值
> 避免孤立事实误导——如"转化率提升40%"的前提是"目标市场是北美"

### 第三步：对标 (Cross-reference)

1. **跨域洞察**：其他领域有没有类似现象？（技术↔商业↔管理↔科学）
2. **知识迁移**：这个知识可以迁移到哪些场景？
3. **跨域关联**：先判断机制是否可比较、有无独立证据；满足实体准入及写入边界才创建或更新。

> [!example] 跨域洞察示例
> - 领域 A："AI Agent 多步推理链在第 5 步后容易失控"
> - 领域 B："跨境电商供应链超过 4 个环节后出错率指数上升"
> - **候选假设而非证据**：若各步成功概率独立且固定为 p，全部成功概率为 p 的 n 次方。共享误差、纠错、重试、依赖及不同失败定义会改变关系。上述两个场景的具体步数仅为示例，不作为实测事实；跨域类比不能证明指数定律。

### 与 Karpathy 原方案的对比

| 步骤 | Karpathy 原始方案 | 饼干哥哥改进版 |
|-----|------------------|---------------|
| 第一步 | 读原文 → 写摘要 | 浓缩（更精炼） |
| 第二步 | 提取概念 | **质疑（新增）** |
| 第三步 | 更新索引 | **对标（新增）** |

### 编译产物示例

一篇 TikTok Shop 选品策略文章编译后产出：
- 1 篇编译摘要（浓缩 + 质疑 + 对标结果）
- 3 个概念条目（TikTok Shop 选品、AI 选品工具、跨境电商利润率）
- 更新全局索引和操作日志

> **关键价值**：下次编译相关文章时，AI 不是从零开始，而是读取已有概念条目，把新信息跟旧信息合并，标注异同

## 与多层记忆的关系

参见 [[Multi-Layer-Memory]]

| 记忆层 | 对应 | 编译角色 |
|-------|------|---------|
| 短期记忆 | 当前对话 | 无 |
| 工作记忆 | 当前模型可见上下文 | 可含检索原文、编译页或工具结果 |
| 长期记忆 | Wiki 层 | **编译产物** |

## 编译成本分析

| 维度 | 首次编译 | 后续使用 |
|-----|---------|---------|
| Token 成本 | 高（深度分析） | 低（直接查询） |
| 时间成本 | 高（触及多页面） | 低（结构化呈现） |
| 人工成本 | 依风险策展与审查 | 高影响判断、争议和更新仍可能需要人工复核 |
| 累积价值 | 基础建立 | 持续增值 |

---

## 关键数据点

- Karpathy 原 Gist 的约100来源/数百页面是设计经验示例，不是容量基准；本库已采用 search-first，规模能力应实测。
- 一次编译后，后续查询无需重复承担该 source 的完整理解与结构化成本（Query 自身的搜索、上下文读取与推理成本仍在）
- 三步编译法（浓缩 → 质疑 → 对标）的具体运行约束以 `schema/three-step-method.md` 为准

## 前提与局限性

- **前提**: LLM 具备足够的理解和综合能力，能准确提炼源材料的核心概念
- **前提**：检索策略按真实任务、召回、质量、延迟与成本验证；纯文件搜索或混合检索皆是候选。
- **边界条件**: 编译质量依赖 Schema 文档的质量，Schema 不完善会导致编译结果不一致
- **局限性**：冲突、时效与新证据是持续编译的正常对象；不能用永久不变或强制单一结论换取一致性。
- **局限性**: Karpathy 的方案是个人 Wiki 场景，团队/企业场景的协作和权限管理未深入讨论

## 关联概念

- [[RAG-vs-LLM-Wiki]] — 编译 vs 检索的对比
- [[Context-Engineering]] — 编译时的上下文优化
- [[Multi-Layer-Memory]] — 编译产物的记忆层级
- [[Software-Development-Autonomy-Levels]] — 跨域同构：其"specification distillation"（agent 把对话/示例/修正持续编译成持久结构化规格）是知识编译在软件规格域的实例
- [[20260625-ford-ai-quality-jd-power]] — 反面案例：Ford 案例提供制度知识迁移风险的讨论材料，不能单凭跨域类比识别质量缺陷的因果来源或证明人参与是所有编译任务的必要条件。
