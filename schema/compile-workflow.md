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

## 支持的 Raw 格式

`raw/` 接受以下文件格式：

| 格式 | 后缀 | 读取方式 | Frontmatter |
|------|------|----------|-------------|
| Markdown | `.md` | `read_text()` | 有 YAML frontmatter |
| PDF | `.pdf` | `tools/pdf-extract.py` 提取至 stdout/临时文件 | 无（元数据记录在 source summary） |

PDF 在编译期间可存放于 `raw/`，但不进入 Quartz 发布面。编译完成后的全文去留由 `schema/compile-operations.md` 结算；可从稳定一手地址恢复的 PDF 默认降级为 `index`。

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

6. 评估并按需创建/更新 entity 页面
   └─ 写入 wiki/entities/
   └─ 优先更新已有页面；新 Entity 必须满足 `schema/entity-spec.md` 的准入条件
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

12. 更新 Compile Registry 并结算 Raw 生命周期
    └─ uv run python tools/compile_registry.py mark-compiled "<raw文件名>" --summary-path "wiki/sources/<raw文件名stem>.md"
    └─ PDF 和 Markdown 文件均需执行此步骤
    └─ 随后按 `schema/compile-operations.md` 选择 full / index；compile 不直接选择 removed

13. 提交 git commit 并推送（按 Commit 规范撰写）
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

5. 评估概念并按需创建/更新 entity 页面
   └─ 写入 wiki/entities/
   └─ 优先更新已有页面或写入 topic 小节；不得把单篇术语机械拆成 Entity
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

11. 更新 Compile Registry 并结算 Raw 生命周期
    └─ uv run python tools/compile_registry.py mark-compiled "<raw文件名>" --summary-path "wiki/sources/<raw文件名stem>.md"
    └─ PDF 和 Markdown 文件均需执行此步骤
    └─ 随后按 `schema/compile-operations.md` 选择 full / index；compile 不直接选择 removed

12. 提交 git commit 并推送（按 Commit 规范撰写）
```

## 单篇改动边界

单篇编译默认只创建 source summary，并更新 0–2 个已有稳定页面。新建 Entity、Topic 或 Comparison 必须分别满足对应准入条件；由材料暴露出的新研究问题交给 `explore`，不在 compile 中自动扩张研究空间。

### 补充 Typed Relations（可选）

只有当「不知道关系的方向和类型，会影响未来理解或推理」时才写 `relations`；否则用 `related_entities` 即可。predicate 白名单与用法见 `schema/frontmatter-spec.md`。不要为「图谱更完整」写空泛 `related_to`，也不要给所有 Entity 批量补 relations。

### 重要综合判断（Claim + Evidence + Boundary）

当编译产生重要的 synthesized 判断（Agent 综合形成、可能被多个问题复用、可能被新证据支持/削弱/限定、对结论有实质影响）时，在稳定页面正文使用统一三字段格式：

- **判断**：Agent 自治程度提高通常会增加 verification 成本。
  - **证据**：[[Source-A]]；[[Source-B]]
  - **边界**：主要适用于长程、开放式、高自主任务。

约束：
- **Evidence 必须指向证据**：raw/source/一手 URL 可以；Entity/Topic 可以帮助定位，但不能因为 Wiki 自己重复了一次判断就变成第二份证据（Evidence ≠ Reasoning）。
- **Boundary 原则上必须给出**：确实无明确边界时写「当前未发现明确边界」，不默认无限适用。
- 不新增 confidence/claim_id/status 等字段；Research 引用稳定判断时使用 Source page + Claim 文本，CR 编号属于 Research 的既有机制。

单篇编译不因为以上机制而：创建大量 Claim、给全图补 relations、创建 Context Pack 文件、重扫 Wiki 或新建 Research。
