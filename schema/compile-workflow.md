---
title: "Ingest 工作流（知识编译）"
type: schema-subdoc
---

> 本文档是 Agentic Work Atlas Schema 子文档，由 README.md 路由表按需加载。

# Ingest 工作流（知识编译）

将原始文章编译为结构化知识。提供两条路径：

- **标准路径**：三步编译法（浓缩 → 质疑 → 对标），适合普通文章
- **ljg 增强路径**：调用相关 ljg 技能进行深度编译，输出结构化知识 + Entity 页面

## ljg 增强路径

```
1. 读取 raw source 内容
   └─ 只读读取 raw，不向 raw 写入分析
   └─ 检查 frontmatter 是否足以溯源；缺失信息优先记录到 source summary
   └─ 若 raw 元数据阻断 lint，只做最小元数据修复，不改正文

2. 选择 ljg 技能（根据文章类型）
   ├─ ljg-paper（读论文） → 论文类文章
   │  └─ 8 段式结构 → 浓缩+质疑+对标 + 核心概念 → entity
   ├─ ljg-paper-river（倒读法） → 研究型论文
   │  └─ 5 层倒读链路 → 概念演化脉络 → comparison
   ├─ ljg-book（拆书） → 书籍类 raw
   │  └─ 五件事（问题/不证之物/框架/结论/takeaway）→ entity
   └─ ljg-qa（问答提取） → 高密度文章需要结构化骨架时
      └─ Q-A 对 → 注入 source summary，为 entity 提供推理链

3. 执行 ljg 技能 → 输出到 ~/Documents/notes/*.md

4. 手动搬运 ljg 输出到 Wiki
   └─ 将 ~/Documents/notes/ 中的 ljg 输出注入 Wiki 标准 YAML frontmatter
   └─ 搬运到 wiki/{entities|topics|comparisons|outputs}/

5. 多主题文章 → 按需追加 ljg 深度编译
   ├─ ljg-think（追本之箭） → wiki/topics/ （层层降深）
   └─ ljg-rank（降秩） → wiki/topics/ （不可约生成器）

6. 编译摘要沉淀到 Wiki 层
   └─ 默认创建或更新 `wiki/sources/{raw 文件名}.md`
   └─ 同步更新 entity/topic/comparison
   └─ 历史 raw 中已有 `## 编译摘要` 保留，但新流程禁止追加到 raw

7. 执行 post-compile 质量门
   └─ cross-link：补充 source summary、entity、topic、comparison 之间的自然链接
   └─ provenance-audit：标记低证据、综合判断和冲突
   └─ dedup-audit：检查是否与既有 entity/topic/comparison 重复

8. 更新 index.md + comparisons（如有对比概念）

9. 提交 git commit 并推送（按 Commit 规范撰写）
```

## 标准路径（三步编译法）

```
1. 读取 raw source 内容
   └─ 只读读取 raw，不向 raw 写入分析
   └─ 检查 frontmatter 是否足以溯源（author/source/published/created 等）
   └─ raw 元数据缺失不阻断编译时，优先在 source summary 补充说明
   └─ 只有 frontmatter、文件名或日期格式阻断 lint/渲染时，才做最小 raw 元数据修复
   └─ 扫描 `$` 符号；raw 中原文裸 `$` 不作为编译时改写理由，必要时在 source summary 中记录渲染风险

2. 执行三步编译法（浓缩 → 质疑 → 对标）
   └─ 浓缩：提取核心结论（≤3条）+ 关键证据
   └─ 质疑：审视前提假设、数据可靠性、边界条件
   └─ 对标：跨领域找类似现象，建立知识迁移

3. 生成 source summary
   └─ 按照 Source Summary 输出模板格式
   └─ 优先写入 `wiki/sources/{raw 文件名}.md`
   └─ 不写入 raw 原文层；即使用户要求保留编译摘要，也应写入 `wiki/sources/`

4. 为每个概念创建/更新 entity 页面
   └─ 写入 wiki/entities/
   └─ ⚠️ wikilink 必须使用 kebab-case 文件名格式（如 [[Vibe-Coding]]）
   └─ ⚠️ source_raw 必须使用短链接格式（纯文件名）
   └─ 如有冲突，在 entity 中标注冲突标记

5. ⚠️ Wiki 写入校验：调用 obsidian-markdown 技能检查新写入的 Wiki 文件格式合规
   └─ 确保 frontmatter 有效（YAML 特殊字符引号包裹）
   └─ 确保 wikilink kebab-case 规范
   └─ 确保 Wiki 层 MathJax 冲突已处理（`$` 被包裹或转义）
   └─ 确保 callout/properties/emphasis 语法正确

6. 创建/更新 topic 页面
   └─ 写入 wiki/topics/

7. 更新 comparisons（如有对比概念）
   └─ 添加新论述、关联已有 entity

8. 执行 post-compile 质量门
   └─ **cross-link**：检查新页面是否自然链接到已有 source/entity/topic/comparison；弱关联只报告，不强行加链
   └─ **dedup-audit**：检查新概念是否只是既有 Entity 的别名、缩写、翻译或更窄版本；优先补 aliases，不急着新建页面
   └─ **provenance-audit**：检查新判断是否区分原文事实、综合判断和冲突/不确定内容

9. 更新 index.md
   └─ 添加新的 entity 和 topic 条目

10. 提交 git commit 并推送（按 Commit 规范撰写）
```

**触及范围**：单篇 source 编译可能影响 10-15 个 wiki 页面
- 新建 entities（3-5 个）
- 更新相关 entities（添加关联）
- 创建/更新 topic（整合主题）
- 更新 comparisons（如有对比）
- 更新 index.md
- 提交 git commit 并推送