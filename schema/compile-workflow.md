---
title: "Ingest 工作流（知识编译）"
type: schema-subdoc
---

> 本文档是 Agentic Work Atlas Schema 子文档，由 README.md 路由表按需加载。

# Ingest 工作流（知识编译）

将原始文章编译为结构化知识。提供两条路径：

- **标准路径**：三步编译法（浓缩 → 质疑 → 对标与旁逸），适合普通文章
- **ljg 增强路径**：调用相关 ljg 技能进行深度编译，输出结构化知识 + Entity 页面

**核心原则**：Agent 基于材料特征自主决定路径选择和技能叠加，无需用户判断或推进。

## 自主路径选择

```
Agent 读取 raw source → 自动判断材料类型 →
  ├─ 论文/学术文章 → ljg 增强路径（ljg-paper）
  ├─ 书籍/长篇著作 → ljg 增强路径（ljg-book）
  ├─ 高密度结构化文章 → ljg 增强路径（ljg-qa）
  └─ 普通文章/博客/新闻 → 标准路径（三步编译法）
```

如果材料同时满足多个增强条件（如：既是论文又引入新概念），基础技能和增强技能叠加使用。

## ljg 增强路径

```
1. 读取 raw source 内容
   └─ 只读读取 raw，不向 raw 写入分析
   └─ 检查 frontmatter 是否足以溯源；缺失信息优先记录到 source summary
   └─ 若 raw 元数据阻断 lint，只做最小元数据修复，不改正文

2. 选择基础 ljg 技能（按材料类型自主路由）
   ├─ ljg-paper（读论文） → 论文类文章
   │  └─ 命题七拍叙事 + 速读卡 → 浓缩+质疑+对标 + 核心概念 → entity
   ├─ ljg-paper-river（倒读法） → 研究型论文关系构建
   │  └─ 5 层倒读链路 → 概念演化脉络 → comparison
   ├─ ljg-book（拆书） → 书籍类 raw
   │  └─ 取景框 f(x) + hard-to-vary 检验 + 参考系图 → entity
   └─ ljg-qa（问答提取） → 高密度文章需要结构化骨架时
      └─ Q-A 对 → 注入 source summary，为 entity 提供推理链

3. 执行基础 ljg 技能

4. 自主评估增强技能（按材料特征叠加，可触发多个）
   ├─ 源材料引入新概念（entity 库中未深入的核心术语）
   │  └─ 调用 ljg-learn → 八维度解剖 → 顿悟句 → 充实 entity 定义
   ├─ 源材料涉及新领域/行业（首次出现的领域级分析）
   │  └─ 调用 ljg-rank + ljg-constraint → 生成器 + 约束 → 领域骨架 topic
   ├─ 源材料含跨域引用或类比（引用其他领域文献/现象）
   │  └─ 调用 ljg-read → 伴读式分析 → 跨域旁逸洞察 → 注入 source summary
   └─ 源材料讨论 AI 公司/产品/项目（FDE 相关）
      └─ 调用 ljg-invest → 秩序创造机器框架 → 判断收录深度

5. 编译摘要沉淀到 Wiki 层
   └─ 默认创建或更新 `wiki/sources/{raw 文件名}.md`
   └─ 将 ljg 技能输出注入 Wiki 标准 YAML frontmatter
   └─ 搬运到 wiki/{entities|topics|comparisons}/
   └─ 历史 raw 中已有 `## 编译摘要` 保留，但新流程禁止追加到 raw

6. 创建/更新 entity 页面
   └─ 写入 wiki/entities/
   └─ wikilink 必须使用 kebab-case 文件名格式（如 [[Vibe-Coding]]）
   └─ source_raw 必须使用短链接格式（纯文件名）
   └─ 如有冲突，在 entity 中标注冲突标记
   └─ 若有 ljg-learn 输出，将顿悟句作为 entity 的一句话定义锚点

7. 创建/更新 topic 页面
   └─ 写入 wiki/topics/
   └─ 若有 ljg-rank + ljg-constraint 输出，将生成器和约束配对写入 topic

8. 更新 comparisons（如有对比概念）

9. Wiki 写入校验：调用 obsidian-markdown 技能确保格式合规

10. 执行 post-compile 质量门
    └─ cross-link：补充 source summary、entity、topic、comparison 之间的自然链接
    └─ provenance-audit：标记低证据、综合判断和冲突
    └─ dedup-audit：检查是否与既有 entity/topic/comparison 重复

11. 更新 index.md + comparisons（如有对比概念）

12. 提交 git commit 并推送（按 Commit 规范撰写）
```

## 标准路径（三步编译法）

```
1. 读取 raw source 内容
   └─ 只读读取 raw，不向 raw 写入分析
   └─ 检查 frontmatter 是否足以溯源（author/source/published/created 等）
   └─ raw 元数据缺失不阻断编译时，优先在 source summary 补充说明
   └─ 只有 frontmatter、文件名或日期格式阻断 lint/渲染时，才做最小 raw 元数据修复
   └─ 扫描 `$` 符号；raw 中原文裸 `$` 不作为编译时改写理由，必要时在 source summary 中记录渲染风险

2. 执行三步编译法（浓缩 → 质疑 → 对标与旁逸）
   └─ 浓缩：提取核心结论（≤3条）+ 关键证据
   └─ 质疑：审视前提假设、数据可靠性、边界条件
   └─ 对标与旁逸：跨领域找类似现象 + 识别跨域类比 + 约束分析
      （详见 schema/three-step-method.md 第三步）

3. 生成 source summary
   └─ 按照 Source Summary 输出模板格式
   └─ 优先写入 `wiki/sources/{raw 文件名}.md`
   └─ 不写入 raw 原文层；即使用户要求保留编译摘要，也应写入 `wiki/sources/`

4. 自主评估增强技能（标准路径同样触发，按材料特征叠加）
   ├─ 源材料引入新概念 → ljg-learn
   ├─ 源材料涉及新领域 → ljg-rank + ljg-constraint
   ├─ 源材料含跨域引用 → ljg-read
   └─ 源材料讨论 AI 公司/产品 → ljg-invest
   （评估标准与增强路径步骤 4 相同）

5. 为每个概念创建/更新 entity 页面
   └─ 写入 wiki/entities/
   └─ wikilink 必须使用 kebab-case 文件名格式（如 [[Vibe-Coding]]）
   └─ source_raw 必须使用短链接格式（纯文件名）
   └─ 如有冲突，在 entity 中标注冲突标记
   └─ 若有 ljg-learn 输出，将顿悟句作为 entity 的一句话定义锚点

6. Wiki 写入校验：调用 obsidian-markdown 技能检查新写入的 Wiki 文件格式合规
   └─ 确保 frontmatter 有效（YAML 特殊字符引号包裹）
   └─ 确保 wikilink kebab-case 规范
   └─ 确保 Wiki 层 MathJax 冲突已处理（`$` 被包裹或转义）
   └─ 确保 callout/properties/emphasis 语法正确

7. 创建/更新 topic 页面
   └─ 写入 wiki/topics/

8. 更新 comparisons（如有对比概念）
   └─ 添加新论述、关联已有 entity

9. 执行 post-compile 质量门
   └─ **cross-link**：检查新页面是否自然链接到已有 source/entity/topic/comparison；弱关联只报告，不强行加链
   └─ **dedup-audit**：检查新概念是否只是既有 Entity 的别名、缩写、翻译或更窄版本；优先补 aliases，不急着新建页面
   └─ **provenance-audit**：检查新判断是否区分原文事实、综合判断和冲突/不确定内容

10. 更新 index.md
    └─ 添加新的 entity 和 topic 条目

11. 提交 git commit 并推送（按 Commit 规范撰写）
```

## 周期性自治：盲区扫描

Agent 在编译流程中自主维护盲区扫描周期：

```
计数器：每完成 1 篇编译 → counter + 1
当 counter ≥ 5 时：
  ├─ 自动触发 ljg-blind（盲区扫描）
  ├─ 扫描最近对话历史，暴露思维盲区
  ├─ 从微信读书挑选精准补章
  ├─ 输出充实 wiki/research/research-agenda.md 的 Source 需求队列
  └─ counter 归零
```

此机制确保知识库不会在某个方向上过度自信而不自知。

**触及范围**：单篇 source 编译可能影响 10-15 个 wiki 页面
- 新建 entities（3-5 个）
- 更新相关 entities（添加关联）
- 创建/更新 topic（整合主题）
- 更新 comparisons（如有对比）
- 更新 index.md
- 提交 git commit 并推送
