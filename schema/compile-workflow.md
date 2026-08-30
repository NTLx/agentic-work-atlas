---
title: "Ingest 工作流（知识编译）"
type: schema-subdoc
---

> 本文档是 Agentic Work Atlas Schema 子文档，由 README.md 路由表按需加载。

# Ingest 工作流（知识编译）

将原始材料编译为可回溯、可复用的结构化知识。Compile 固定的是知识
生命周期和质量门；具体使用哪种认知方法由 Agent 根据当前缺口动态判断，
不按材料类别拆成固定编译分支，也不预设材料类型与 Skill 的映射。

## 支持的 Raw 格式

`raw/` 接受以下文件格式：

| 格式 | 后缀 | 读取方式 | Frontmatter |
|------|------|----------|-------------|
| Markdown | `.md` | `read_text()` | 有 YAML frontmatter |
| PDF | `.pdf` | `tools/pdf-extract.py` 提取至 stdout/临时文件 | 无（元数据记录在 source summary） |

PDF 在编译期间可存放于 `raw/`，但不进入 Quartz 发布面。编译完成后的全文去留
由 `schema/compile-operations.md` 结算；可从稳定一手地址恢复的 PDF 默认降级为
`index`。

## 动态认知选择

完成基本读取和主题判题后，Agent 按 `schema/skill-mapping.md` 的协议执行：

1. 读取 raw source；只读正文，不向 raw 追加分析。检查元数据是否足以溯源；
   只有会阻断 lint 或渲染的元数据问题才做最小修复。
2. 按主题宪法判断是否属于主线，并查看当前 Wiki 中少量直接相关的
   source/entity/topic/comparison，先完成去重和语境定位。
3. 说清本次编译最大的认知瓶颈：是理解材料、澄清概念、辨认结构、检查边界、
   组织表达，还是无需额外方法即可完成。
4. 查看 Runtime 当前发现的 Skill 的 `name` 和 `description`，允许选择
   `none`；只有确实相关时才读取选中 Skill 的完整 `SKILL.md` 及其所需资源。
5. 执行一个最小认知动作。Skill 结果默认属于 reasoning，不是 Evidence；
   记录它与原文事实、推断和不确定性的区别。
6. 观察中间结果：已经足够就停止；若暴露出新的瓶颈，再重新查看能力描述并
   选择下一步。不要预先构造完整 Skill DAG，也不要为了“充分利用”而调用
   不必要的 Skill。

三步编译法仍可作为 source summary 的最低分析合同（详见
`schema/three-step-method.md`）：提炼核心结论及证据、检查前提和边界、做
必要的对标与约束分析。它约束内容质量，不规定某个 Skill 必须被调用。

## KnowledgeOps 不变量

完成动态认知动作后，按以下固定边界沉淀结果：

1. **生成 Source Summary**：默认创建或更新
   `wiki/sources/{raw 文件名 stem}.md`，按照 Source Summary 模板记录来源、
   核心结论、关键证据、边界、冲突和 reasoning。不要把分析追加到 raw；历史
   raw 中已有的 `## 编译摘要` 不主动清洗或迁移。
2. **评估稳定页面**：优先更新已有页面。仅当材料和 Entity/Topic/Comparison
   准入条件都满足时，才创建 0–N 个稳定页面；不得因为 Skill 产生了术语或
   一段漂亮解释就机械建页。Entity 的 `source_raw` 使用短链接格式，正文
   wikilink 使用既有命名规范；来源冲突按 `schema/conflict-markers.md` 标记。
3. **区分判断与证据**：重要 synthesized 判断使用统一的“判断 / 证据 / 边界”
   结构。证据必须指向 raw、source 或合规外部来源；Wiki 页面只能帮助定位，
   不能因重复了同一判断而成为第二份证据。
4. **执行 post-compile 质量门**：
   - `cross-link`：只补自然且有用的 source/entity/topic/comparison 链接；
     弱关联只记录，不为完整性强行加链。
   - `dedup-audit`：检查别名、缩写、翻译、更窄版本与已有页面的重叠，优先
     补 aliases 或更新已有页面。
   - `provenance-audit`：标记原文事实、Agent 综合判断、冲突和不确定性。
5. **处理写入格式**：普通 Markdown 直接遵循
   `schema/obsidian-rendering.md`，随后交给 deterministic lint；只有确实
   使用复杂 Obsidian 特性时，才按需选择相关 Skill。第三方 Skill 的默认
   输出路径不改变 Wiki 目录规则。
6. **更新导航**：按实际新增或删除的页面更新 `index.md`；有真实对比内容时
   才更新 comparison 页面。
7. **更新 Compile Registry 并结算 Raw 生命周期**：全文剪藏时先执行：

   ```bash
   uv run python tools/compile_registry.py ensure "<raw文件名>"
   ```

   编译完成后执行：

   ```bash
   uv run python tools/compile_registry.py mark-compiled "<raw文件名>" \
     --summary-path "wiki/sources/<raw文件名stem>.md"
   ```

   PDF 和 Markdown 均需登记；随后按 `schema/compile-operations.md` 选择
   `full` 或 `index`，compile 不直接选择 `removed`。
8. **校验**：按当前 HEAD 的提交日期运行只读 lint；存在 blocking issue 时不
     提交：

   ```bash
   uv run python tools/wiki-lint.py --as-of "$(git show -s --format=%cs HEAD)"
   ```

9. **提交与推送**：完成门按 README 和 `schema/git-commit-spec.md` 执行，
   结构化 commit 必须说明本次 Schema/KnowledgeOps 变化。

## 单篇改动边界

单篇编译默认只创建 Source Summary，并更新 0–2 个已有稳定页面。新建 Entity、
Topic 或 Comparison 必须分别满足对应准入条件；材料暴露出的新研究问题交给
`explore`，不在 compile 中自动扩张研究空间。

### 补充 Typed Relations（可选）

只有当“不知道关系的方向和类型，会影响未来理解或推理”时才写 `relations`；
否则用 `related_entities` 即可。predicate 白名单与用法见
`schema/frontmatter-spec.md`。不要为“图谱更完整”写空泛 `related_to`，也不要
给所有 Entity 批量补 relations。

`relations` 只允许出现在 `type: entity` 页面，target 只能指向
`wiki/entities/` 下的实体（Entity → Entity）；Entity → Source 的证据链继续用
`source_raw`。

### 重要综合判断（Claim + Evidence + Boundary）

当编译产生重要的 synthesized 判断（Agent 综合形成、可能被多个问题复用、可能
被新证据支持/削弱/限定、对结论有实质影响）时，在稳定页面正文使用统一三字段
格式：

- **判断**：Agent 自治程度提高通常会增加 verification 成本。
  - **证据**：[[Source-A]]；[[Source-B]]
  - **边界**：主要适用于长程、开放式、高自主任务。

约束：

- **Evidence 必须指向证据**：raw/source/一手 URL 可以；Entity/Topic 可以帮助
  定位，但不能因为 Wiki 自己重复了一次判断就变成第二份证据
  （`Evidence ≠ Reasoning`）。
- **Boundary 原则上必须给出**：确实无明确边界时写“当前未发现明确边界”，不
  默认无限适用。
- 不新增 `confidence`、`claim_id`、`status` 等字段；Research 引用稳定判断
  时使用 Source page + Claim 文本，CR 编号属于 Research 的既有机制。

单篇编译不因为动态 Skill 或综合判断而创建大量 Claim、给全图补 relations、
创建 Context Pack 文件、重扫 Wiki 或新建 Research。
