---
title: "Git Commit 规范（操作历史记录）"
type: schema-subdoc
---

> 本文档是 Agentic Work Atlas Schema 子文档，由 README.md 路由表按需加载。

# Git Commit 规范（操作历史记录）

知识库使用结构化 git commit 替代 log.md 记录所有操作历史。剪藏、编译、输出、探索四大环节以及修复、lint、schema 更新完成后，必须提交 git commit 并推送到远端，commit message 即为 LLM Wiki 操作日志。

## Commit Message 格式

```
<type>(<scope>): <subject>

<body>
```

**各段说明：**

| 段落 | 必填 | 说明 |
|------|------|------|
| `<type>(<scope>): <subject>` | ✅ | 标题行，不超过 72 字符 |
| `<body>` | ✅ | 详细描述变更内容 |

## Type 枚举

| Type | 含义 | 示例 |
|------|------|------|
| `compile` | 知识编译（Ingest） | `compile(Karpathy-AI-Capability-Gap): 编译 Karpathy AI 能力鸿沟帖` |
| `fix` | 修复问题（lint 修复、链接修复等） | `fix(wikilinks): 修复 18 处 ASCII/Unicode 撇号不匹配` |
| `refactor` | 重构（格式转换、架构调整） | `refactor(entities): 转换 4 个 ljg-learn 输出为标准格式` |
| `lint` | Lint 审计 | `lint: 执行完整 lint 检查，健康度 72→96` |
| `docs` | 文档/Schema 更新 | `docs(schema): 新增时间与事实规范章节` |
| `clip` | 剪藏新文章到 raw/ | `clip(steve-hanov): 剪藏 Steve Hanov 精益技术栈文章` |
| `output` | 创建 Output 作品 | `output(quartz-tutorial): 创建 Quartz 部署教程` |
| `explore` | 更新研究议程或探索问题 | `explore(ai-deployment): 更新标准产品/FDE/AI Factory 三路径问题` |

## Scope 规范

Scope 标识操作的聚焦对象，使用 kebab-case：

| 场景 | Scope 示例 |
|------|-----------|
| 编译单篇文章 | 文章主题关键词：`Karpathy-AI-Capability-Gap`、`Lean-Stack` |
| 批量操作 | 操作范围：`entities`、`topics`、`all-raw` |
| 修复特定问题 | 问题对象：`wikilinks`、`frontmatter`、`source-raw` |
| Schema 更新 | `schema` |

## Body 模板（按 Type 分）

### compile 类型

```
- 来源: {URL} ({平台}, {作者})
- 编译方式: {标准路径/ljg 增强路径}
- 新增 Entity: {Entity-A}, {Entity-B}
- 更新 Entity: {Entity-C}, {Entity-D}
- 新增 Topic: {Topic-A}
- 更新 Topic: {Topic-B}
- 索引: {N}→{M} entities, {X}→{Y} raw articles
```

### fix 类型

```
- 修复内容: {具体问题描述}
- 影响文件: {文件列表}
- 修复方式: {如何修复}
```

### lint 类型

```
- 检查项: {列出检查的 8 项}
- 发现问题: {具体问题}
- 修复情况: {修复了什么}
- 健康度: {旧分}→{新分}
```

### refactor 类型

```
- 重构内容: {什么从什么变为什么}
- 影响文件: {文件列表}
```

### clip 类型

```
- 来源: {URL}
- 作者: {作者名}
- 主题: {关键词}
```

### explore 类型

```
- 探索范围: {主题或问题}
- 新增问题: {关键问题}
- 证伪方向: {需要寻找的反例}
- Source 需求: {下一轮剪藏目标}
```

## Commit 示例

**编译操作：**
```
compile(Karpathy-AI-Capability-Gap): 编译 Karpathy AI 能力鸿沟帖

- 来源: https://x.com/karpathy/status/... (X/Twitter, Andrej Karpathy)
- 编译方式: 标准路径（三步编译法）+ 附加思考整合
- 附加资料: 池建强微信公众号 + 墨问笔记
- 新增 Entity: AI-Psychosis, AI-Capability-Gap
- 更新 Entity: Andrej-Karpathy, Vibe-Coding, Software-2.0, Claude-Code-CLI
- 更新 Topic: Karpathy-AI-Thought (新增概念矩阵)
- 索引: 67→69 entities, 25→26 raw articles
```

**Lint 修复：**
```
fix(entity-completeness): 全面修复 Entity 完整性 (42/42) 并优化 lint 工作流

- 修复内容: 补全 42 个概念 Entity 的标准三章节（关键数据点、前提与局限性、关联概念）
- 影响文件: 42 个 entity 文件
- 修复方式: 为缺失章节添加占位内容，统一标题命名
```

**Schema 更新：**
```
docs(schema): 用 Git Commit 规范替代 log.md 记录操作历史

- 删除 3 个 log.md 文件（根目录、raw/、wiki/）
- 新增 Git Commit 规范章节（type/scope/body 模板）
- 更新所有 log.md 引用（架构图、工作流步骤、关键文件表、Quartz 配置）
```

## 操作历史查询命令

| 查询需求 | Git 命令 |
|---------|---------|
| 最近 10 次操作 | `git log --oneline -10` |
| 某篇文章的编译历史 | `git log --grep "文章关键词"` |
| 某个 Entity 的变更历史 | `git log -- wiki/entities/Entity-Name.md` |
| 所有编译操作 | `git log --grep "^compile"` |
| 所有修复操作 | `git log --grep "^fix"` |
| 所有剪藏操作 | `git log --grep "^clip"` |
| 所有输出操作 | `git log --grep "^output"` |
| 所有探索操作 | `git log --grep "^explore"` |
| 某次操作的详细变更 | `git show <commit-hash>` |
| 某次操作的文件列表 | `git show --stat <commit-hash>` |
| 某段时间内的操作 | `git log --since="2026-04-01" --until="2026-04-15"` |
| 某个目录的所有变更 | `git log -- wiki/entities/` |
| 搜索 body 中的关键词 | `git log --grep="AI-Psychosis"` |

## Commit 规范

- **标题行不超过 72 字符**：超出时缩写 scope 或 subject
- **Body 默认填写**：至少包含「做了什么」和「影响了什么」；极小的单文件元数据修复可只用标题行
- **compile 类型建议列出 Entity 变更**：新增/更新的 Entity 应在 body 中列出，便于以后从 git history 追溯知识图谱变化
- **fix 类型必须说明修复方式**：不能只写"修复了 bug"
- **每次操作一个 commit**：编译一个 raw source = 一个 commit，不要批量合并多个编译
- **四大环节完成即推送**：`clip`、`compile`、`output`、`explore` 完成后必须 `git push`，远端 commit history 才是完整 LLM Wiki 日志