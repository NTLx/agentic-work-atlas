---
type: topic
title: "Agent 知识管理与自进化"
created: 2026-05-13
updated: 2026-11-28
evidence_level: medium
claim_type: mixed
tags:
  - knowledge-management
  - AI
  - agent
  - topic
related_entities:
  - "[[LLM-Wiki]]"
  - "[[GBrain]]"
  - "[[Obsidian-Wiki]]"
  - "[[Progressive-Disclosure]]"
  - "[[Thin-Harness-Fat-Skills]]"
  - "[[Latent-Space-vs-Deterministic]]"
  - "[[Harness-Engineering]]"
  - "[[Knowledge-Compilation]]"
  - "[[Memex]]"
  - "[[Corrective-RAG]]"
  - "[[Continual-Learning]]"
  - "[[World-Model]]"
  - "[[Scientific-Discovery-AI]]"
  - "[[Einstein-Test]]"
  - "[[Shortification-of-Learning]]"
  - "[[Agentic-Analytics]]"
source_raw:
  - "[[20261027-a16z-databricks-future-of-firm]]"
  - "[[20261027-ai2-novelty-bench]]"
  - "[[20261027-replit-cloud-agents-company-codebase]]"
  - "[[20261113-oreilly-what-makes-agent-self-evolving]]"
  - "[[20261113-anthropic-building-always-on-agents]]"
  - "[[20261110-latentspace-resend-designing-for-agents]]"
  - "[[20261020-tessl-claim-based-agent-memory]]"
  - "[[20261013-tessl-how-open-is-your-software-factory.md]]"
  - "[[20260413-llm-wiki]]"
  - "[[一篇文章卖了20万，开源CC+Obsidian打造的LLM Wiki 内容创作3.0系统]]"
  - "[[深度解析LLM Wiki  Obsidian-Wiki  GBrain：Agent时代知识的“自组织”与“自进化”]]"
  - "[[Demis Hassabis: Agents, AGI & The Next Big Scientific Breakthrough]]"
  - "[[20260602-karpathy-shortification-of-learning]]"
  - "[[20260603-anthropic-self-service-data-analytics]]"
  - "[[20260902-bytebytego-rag-translator-model]]"
  - "[[20260902-meta-organizational-second-brain]]"
---

# Agent 知识管理与自进化

## Reflective Memory / Dreaming：保存可迁移经验，而不是把局部用户事实写成通用指令（2026-11）

[[20261113-oreilly-what-makes-agent-self-evolving]]（「Harness modules: What can evolve?」）区分可泛化的经验（例如先核对全体用餐者预算和饮食限制）与单个用户/某次聚餐的事实（这次预算 25 美元）。Reflective Memory 可将过去错误转成下次使用的策略；Dreaming 则在会话间整理、合并与清除重复记忆，遇到冲突需要返回原始证据核对。作者明确指出：**整理得更整洁不等于对新任务更有帮助**，应使用旧记忆与新记忆的独立任务对比测量效果。

- **判断（综合）**：Wiki 的知识提炼目标是 `evidence-linked reusable lesson`，不是把用户私有偏好、过期单次参数和 n8n 队列状态混入公共知识。记忆修订要留来源、适用范围、版本和原有事实；索引/检索策略改进也需要可复验的真正任务成功增益。
- **证据**：[[20261113-oreilly-what-makes-agent-self-evolving]]（Reflective Memory、Dreaming）；与 [[20261113-anthropic-building-always-on-agents]] 的 Memory 四分类和“别复制别的权威事实源”原则互补。
- **边界**：这不是推荐 Dreaming 自动覆盖所有旧知识。没有独立评测、冲突审计或回滚时，不应自主写入治理规则。



## Anthropic 长期 Memory 的四种内容与「能查到的存指针」原则（2026-11）

[[20261113-anthropic-building-always-on-agents]]（原文「Memory / Inside the context window」）将跨 Run Memory 分成 **user instructions / user notes / past messages / task progress**，推荐持久目录与按需读取索引，并明确**其它系统已有权威数据时，只存指针而非重复拷贝**。长 Session compaction 或新建 Session 都会丢细节，因此长任务执行中须及时将关键进度写入持久存储；可选 dreaming 对历史 session 做主动整理和去旧，但不是必要的可靠性机制。

- **判断（综合）**：`LLM context ≠ durable memory ≠ authoritative operational state`。LLM WiKi 适合保留来源、Claim、结构化洞察和引用；n8n 任务队列的占有权、租约、终态与回执仍应由 Broker 保有，Agent 仅引用权威状态，避免“双真相源”。
- **边界**：文件式记忆不自动解决跨用户隐私、错误学习、TTL、更新审查和权限撤销；Dreaming 的总结也应拥有来源和可恢复性，不应直接篡改审计事实。
- **证据**：[[20261113-anthropic-building-always-on-agents]]（Memory、Inside the context window）。



## Resend 客服知识沉淀：把高频支持转成可复用产品约束（2026-11）

[[20261110-latentspace-resend-designing-for-agents]]（**17:05–20:11、58:28–1:03:07**）展示两级知识代谢：Resend 曾要求客服在回复重复问题前先写成文档并分享链接，避免专业答复只存在支持会话；进一步将最常见的 DNS 错误、邮件模版和投递约束编入产品校验，减少后续支持需求。另一个方向则是把计费等事实输出为机器可读 Markdown，修复 Agent 读不懂 JavaScript 滑块导致的错误报价。

- **判断（综合）**：知识代谢不能止于“文档条数增多”：**重复失败/工单 → 来源确认 → 可版本化知识/规则 → 产品内自助验证 → 真实任务复测 → 弃用过时内容**。HTML/Markdown/API 最好共用事实源，并定期校对模型是否仍给正确答案。
- **证据**：[[20261110-latentspace-resend-designing-for-agents]]，18:33–19:06 和 1:01:19–1:02:58。
- **边界**：这些是受访者的产品实践，不能直接推导“所有支持工单都值得单独成篇”；组织知识的隐私/权限边界和解决问题的成本仍需判断。



## 从 Chunk 记忆到具备时间、来源与权限的 Claim（2026-10）

[[20261020-tessl-claim-based-agent-memory]] 讨论团队记忆与个人检索的区别：从观察中抽取带说话人、时间区间和原始证据 span 的 Claim；不覆盖旧事实，而以 supersedes 显式衔接；对“没有答案”标记已查无证据与超出知识范围。作者还把主体授权移动到模型前的检索层，避免让生成模型判断哪些信息该隐去。

- **判断**：知识记忆的关键治理对象是可追溯且有权限的命题，而非文件数量或 embedding 命中；来源有效性、时间与用户身份须先于生成。
- **证据**：[[20261020-tessl-claim-based-agent-memory]]（Store claims not chunks、Make time and absence explicit、Decide permissions before the model runs）。
- **边界**：基准数据为系统作者自报，Claim 蒸馏可能丢失反证或语境；对 LLM WiKi 的全文去留仍须遵守现行 Raw lifecycle 而不是无条件丢弃原文。



> [!summary] 主题概述
> 持久知识编译、运行时检索、经验学习与模型训练是不同设计维度。LLM Wiki、Obsidian-Wiki、GBrain 是不同实现实例，不构成完整分类或性能排序。

## 运行时检索与持久知识治理

基础 RAG 可在查询时重新综合原文；它也可以使用持久索引、缓存、预计算摘要和知识图谱。LLM Wiki 关注跨查询持久维护知识及证据。编译可能提前发现冲突、减少重复理解，也可能漏掉反证或传播旧误解；二者可组合。

参见 [[RAG-vs-LLM-Wiki]]

## Compile-time 知识层

本库的重编译经验说明，LLM Wiki 的关键不是“每篇文章都有摘要”，而是有独立复用价值的材料是否被适当编译，低价值或重复来源是否按生命周期结算：

| 层 | 承载内容 | 失败形态 |
|----|----------|----------|
| Entity | 稳定概念、定义、边界、来源 | 概念太碎、只有名词没有判断 |
| Topic | 多篇文章的生成结构 | 只罗列来源，没有解释机制 |
| Comparison | 相邻概念的差异 | 把对比写成并列表 |
| Output | 对外表达和压力测试 | 新判断没有回填检查 |

质量需由真实查询的正确性、证据可回查性、时间有效性、维护与使用成本验证。减少不必要的重读不等于禁止回查原文；高影响、冲突、过时及未知范围问题需要回溯证据。

Karpathy 关于 [[Shortification-of-Learning|学习短视频化]] 的判断给这个规则补了认知层理由：顺滑地“看过”不等于学会。剪藏 raw 只是把材料放进仓库，编译才是主动处理。没有 source-summary、entity、topic、comparison 和冲突标记，知识库会变成长文本版短视频流：内容很多，理解很少。

## Raw access 不是知识管理

Anthropic 自助数据分析实践提供了一个反向证据：让 agent 访问数千个历史 SQL 文件，只让准确率提升不到 1 个百分点；80% 错误答案的答案其实已经在 corpus 中，但 agent 没有正确使用。真正提升来自 domain skills、semantic layer、canonical datasets、evals 和 correction harvesting。

这说明 Agent 知识管理的关键不是“能不能搜到”，而是“是否把材料编译成可执行、可验证、会随系统变更更新的知识资产”。[[Agentic-Analytics]] 是 LLM Wiki 思路在企业数据分析中的工程化版本。

## 高密度知识与稀疏证据的分层

Meta 的 Organizational Second Brain 给出一个可迁移的分层：高密度、经常被引用的组织立场、决策框架和边界例子进入可维护的 wiki；低密度、只在特定情境出现的规格、历史记录和外部材料继续通过 semantic/lexical RAG 按需获取。

ByteByteGo 的检索分析补上了另一半：RAG 的 embedding 只是证据入口，语义相似不保证回答相关；版本、数字、否定、权限和领域词汇仍需 metadata、规则、reranker 或确定性工具约束。综合判断：知识层负责沉淀“组织如何理解”，RAG 负责补充“这次需要的稀疏证据”，二者不能互相冒充。

## LLM Wiki 的三层架构

1. **Raw Sources（原始资料层）**：原设计强调正文不可变。本库按 schema/compile-operations.md 维护 full/index/removed 生命周期，正文不可变不等于永久保留全文
2. **Wiki 层**：可版本化的结构化知识，由 Agent 按治理、证据与晋升约束维护
3. **Schema（规则层）**：定义系统运行规则和约定的元指令文件

核心操作闭环：**Ingest（摄入）→ Query（查询）→ Lint（维护）**

本库实际操作、读写边界及维护纪律以 README.md 与 schema 为准；概念上区分剪藏、编译、产出、探索与跨切面的审计，查询默认只读。这条拆分很重要，因为它防止三种混淆：把 output 当稳定事实、把 research agenda 当证据、把 raw 摘要当 wiki 编译。

## 三种工程化实现

### LLM Wiki（Karpathy）
- 纯 Markdown 文件 + Schema 指导
- 极简哲学，零依赖
- 原设计面向多种知识场景；适用规模不是已证实的固定阈值
- 参见 [[LLM-Wiki]]

### Obsidian-Wiki
- 基于 Skill 的多 Agent 框架
- 历史来源描述多种 Agent 集成；当前支持与权限按实际版本核验
- 核心创新：Agent History Ingest（自动扫描历史记录）、Delta 追踪、溯源标记
- 参见 [[Obsidian-Wiki]]

### GBrain（Garry Tan）
- 混合检索架构：向量粗筛 + 文件精读
- 基于规则的图谱实体关系管理
- 设计哲学：[[Thin-Harness-Fat-Skills]]、[[Latent-Space-vs-Deterministic]]
- 可作为关系及规模检索的候选；原 49.1% 产品评分已被官方勘误撤回，详见 [[GBrain]]
- 参见 [[GBrain]]

## 知识自进化的路径

### 外部知识和技能的经验复用
- Skill 机制可持久保存可复用经验；加载成功不等于行为改进
- 将非结构化知识转化为可被 Agent 高效调用的结构化资产
- 代价：可能增加读取往返与维护；实际响应速度需对照测量
- 参见 [[Progressive-Disclosure]]

### 重量级路径：RL 训练
- 通过强化学习深度训练模型
- 门槛和成本高，面向研究人员和特定 Benchmark 优化

### 候选方案：混合架构
- 向量检索/关键词索引解决"找得快"
- 按需展开证据，控制上下文；召回、时效、阅读和综合仍须验收
- 离线自我迭代保持知识新鲜度

## 质量门：编译不是一次性总结

LLM Wiki 的主要风险是把错误理解固化成知识层。为降低这个风险，编译必须至少有三类门禁：

- **可追溯**：稳定判断能回到 raw source，关键分歧标记来源。
- **可区分**：entity 与 topic 不是换名复制，而是真的划清概念边界。
- **可审查**：Markdown、wikilink、frontmatter 和裸 `$` 等渲染问题必须被 lint 拦住。

这也是为什么本库要求 Obsidian Markdown 写入守卫和 `tools/wiki-lint.py`。知识系统的可信度不只来自模型理解，也来自文件系统层面的可验证约束。

## 长期记忆仍是 Agent 的硬缺口

Demis Hassabis 的 AGI 访谈从另一个方向支持了这个 Topic：当前模型仍缺持续学习、长期推理和一致性。把所有内容塞进百万 token context window 不是长期记忆，只是更大的工作记忆；它会把不重要、错误或过时的信息也一起塞进去，检索和判断成本仍然存在。

因此，Agent 知识管理不能只追求更长上下文。更稳的方向是把 raw source、编译后的 wiki、检索索引、专用工具和人类策展分层组织起来。Hassabis 提到的 [[Tool-Use-Architecture|Tool-Use Architecture]] 也指向同一结构：通用模型不应把所有专业知识塞进一个巨大脑袋，而应成为专用系统和知识工具的协调者。

## AGI 视角：从外部记忆到持续学习

[[Continual-Learning|持续学习]]是 Agent 知识管理的上游研究问题。现在的工程系统通常用外部 memory、RAG、wiki、skills 和 lint 来模拟学习，但这些机制仍然需要明确的晋升、清理和验证规则。它们能让系统“不从零开始”，却不等于模型本身已经学会了如何更新自己。

[[World-Model|世界模型]]是持续学习要更新的对象之一。没有世界模型，Agent 保存再多历史，也只是保存了原始记录；有了世界模型，系统才可能把经验压缩成对环境、因果关系和行动后果有预测力的结构。

[[Scientific-Discovery-AI|科学发现 AI]]把这个问题推到高压场景：一个科学 Agent 需要多轮实验、工具调用、假设修正和失败积累。[[Einstein-Test|Einstein Test]]则进一步要求系统不只是解已有问题，而是提出后来才出现的深层问题或理论。这个链条说明，Agent 知识管理的终点不是“存得多”，而是“学得准、忘得对、能迁移、能提出新问题”。

## 科学数据的 AI-ready 不是“公开可下载”

Hugging Face 与多家研究机构在 2026-10-29 启动 Project ProtoStar，明确把公开科学成果的“可访问”与“可复用”区分开：数据、模型和代码即使已经公开，如果仍散落在不兼容系统、静态/遗留格式中，或缺少文档、metadata、licensing 与 provenance，研究者和 AI 系统仍难以发现、解释、组合和复用。ProtoStar 因此把 machine-actionable formats、开放基础设施和 publishing guidance 作为基础设施层，并用公开 challenge 去观察真实 reuse、interoperability 和 documentation gap。

**判断**：面向生物信息学和 AI for Science 的知识/数据基础设施，应把“AI-ready scientific artifact”定义为一组可验证的复用条件，而不是“文件已经公开”：至少需要机器可操作格式、足够 metadata、许可边界、provenance、长期可恢复性，以及真实下游复用对 interoperability 的压力测试。公开访问是必要条件之一，但不是可复用性的证明。

- **证据**：Hugging Face 官方《Announcing Project ProtoStar: Making Publicly Funded Science AI-Ready》（2026-10-29）：https://huggingface.co/blog/announcing-project-protostar ；Project ProtoStar：https://huggingface.co/project-protostar 。文章同时给出 NIH/NCBI、NASA 等已有公开资源的下载与文档化背景，并说明 open challenges 的目标之一是形成关于 reuse barriers 的实践证据。
- **边界**：ProtoStar 当前仍处于 initiative launch / challenge 启动阶段；它能支持基础设施设计与问题定义，不能证明该计划已经提高跨机构复用率、科学产出或 AI discovery 质量。后续 adoption/outcome 应作为新的 evidence，而不是从启动声明外推。

## 人类角色的转变

在 LLM Wiki 范式下，人类的角色从"知识维护者"转变为"知识策展人"：

- **策展来源**：选择有价值的信息源
- **引导分析**：提出好问题，指导 LLM 的编译方向
- **最终理解**：LLM 负责信息填充和重排，人负责顶层判断

> [!quote] Karpathy
> Obsidian is the IDE; the LLM is the programmer; the wiki is the codebase.

更精确地说，人类不是退出理解，而是退出低价值搬运。人仍然负责三件事：判断哪些 source 值得收录，决定哪些概念需要稳定化，以及通过 output 反向检验 wiki 是否真的有用。

## 思想渊源

- [[Memex]] — Vannevar Bush 1945 年的个人知识存储愿景，LLM Wiki 的思想先驱
- LLM 降低部分维护劳动，但证据校准、冲突裁决和知识退役仍有实际成本

---

## 结论

Agent 知识管理的第一性原理是：让知识从一次性上下文，变成可版本化、可链接、可审查、可复用的中间层。

检索增强回答与持久知识治理可以互补。知识价值来自实际复用、可靠更新及发现错误的能力，而非文件数量或架构名称。

---

### 软件工厂的知识迁移性

Tessl 将软件工厂的长期产出扩展到代码之外：架构决定、review 纠错、事故约束、skills 与 evals 会积累为组织 know-how。多模型或开放接口不自动等于开放；更有力的检验是把一项维护过的 skill、决策与评测带到另一 Agent/harness，验证其能否重用并通过检查。可迁移仍需适配权限、工具和记忆语义，并承担持续维护成本；作者也提醒，临时 workaround 不能未经审核升格为政策。该框架来自供应商文章，应视为评估问题，而非产品能力的独立验证。

来源：[[20261013-tessl-how-open-is-your-software-factory]]。

### 从审查反馈到跨模型组织资产，而非无门槛记忆增长（2026-11）

[[20261027-replit-cloud-agents-company-codebase]] 将评审意见变成待工程师批准的团队 Skills（early access）；[[20261027-a16z-databricks-future-of-firm]] 主张保存定义、权限、人工覆盖、结果与例外，使知识跨模型保留；[[20261027-ai2-novelty-bench]] 提醒新颖性 judge 存在不稳定性。**综合判断**：反馈只生成候选；经来源、去重、适用范围、独立评测、批准和回归后才能成为长期知识。业务系统保持权威状态，Wiki 保存可回查知识与指针。厂商自报效率和投资者护城河论点不能证明收益普适。
