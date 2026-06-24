---
title: "Source Summary 模板与证据强度"
type: schema-subdoc
---

> 本文档是 Agentic Work Atlas Schema 子文档，由 README.md 路由表按需加载。

# Source Summary 输出模板

新编译默认创建 `wiki/sources/{raw 文件名}.md`，用于承载三步编译摘要并满足 lint 的摘要覆盖检查。`raw/` 只保存原文和剪藏元数据；除最小元数据修复外，编译流程不得写入 raw。

```markdown
---
type: source-summary
title: "{原文标题}"
source_raw:
  - "[[{raw 文件名}]]"
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags:
  - source-summary
  - {主题标签}
evidence_level: medium
claim_type: mixed
---

# {原文标题}

## 编译摘要

### 1. 浓缩
- **核心结论1**: xxx
  - 关键证据: xxx
- **核心结论2**: xxx
  - 关键证据: xxx
- **核心结论3**: xxx（可选）

### 2. 质疑
- **关于"结论1"的质疑**: xxx
- **关于"结论2"的质疑**: xxx
- **关于数据可靠性的质疑**: xxx（如有）

### 3. 对标
- **跨域关联1**: 此现象类似 [xxx领域]，可迁移到 yyy 场景
- **跨域关联2**: ...（如有）

### 关联概念
- [[概念A]]
- [[概念B]]
```

# 证据强度与推断标记

Wiki 层页面可使用两个轻量 frontmatter 字段帮助 Agent 判断可信度：

| 字段 | 取值 | 含义 |
|------|------|------|
| `evidence_level` | `high` / `medium` / `low` | 当前页面核心判断的证据强度 |
| `claim_type` | `extracted` / `synthesized` / `mixed` | 页面主要内容是原文提取、跨来源综合，还是二者混合 |

使用规则：
- `high`：一手来源、多源互证、或已被 topic/comparison 反复复用。
- `medium`：单一高质量来源，或多源但仍存在边界条件。
- `low`：来源弱、单源、强推断、营销性材料、或尚未解决冲突。
- `extracted`：主要是 source 明确说出的事实、数据、框架。
- `synthesized`：主要是 Agent 跨来源建立的模型、类比、比较或判断。
- `mixed`：既有事实提取，也有综合判断，是默认值。

正文中不强制逐句打标，但必须遵守：
- 原文明确事实可直接写入，并通过 `source_raw` 回链。
- 跨来源综合判断应在句中或段尾标明“综合判断”，避免伪装成原文事实。
- 冲突或不确定内容必须进入 `## 前提与局限性`、`## 冲突标记` 或 research agenda。
- `evidence_level: low` 的页面不能单独支撑 output 新判断升级，只能作为补 source 或探索线索。

历史兼容：已有 raw 文件中的以下格式可以保留，但新编译不得继续使用这种写入位置。

```markdown
---

## 编译摘要

### 1. 浓缩
- **核心结论1**: xxx
  - 关键证据: xxx
- **核心结论2**: xxx
  - 关键证据: xxx
- **核心结论3**: xxx（可选）

### 2. 质疑
- **关于"结论1"的质疑**: xxx
- **关于"结论2"的质疑**: xxx
- **关于数据可靠性的质疑**: xxx（如有）

### 3. 对标
- **跨域关联1**: 此现象类似 [xxx领域]，可迁移到 yyy 场景
- **跨域关联2**: ...（如有）

### 关联概念
- [[概念A]]
- [[概念B]]
```