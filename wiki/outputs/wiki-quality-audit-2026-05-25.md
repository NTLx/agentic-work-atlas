---
type: output
title: "Wiki 全量质量审计报告 2026-05-25"
created: 2026-05-25
updated: 2026-05-26
tags:
  - output
  - audit-report
  - wiki-maintenance
---

# Wiki 全量质量审计报告 2026-05-25

## 范围

- 本轮覆盖 `wiki/` 下除本报告外的 Markdown 文档：310 篇。
- 覆盖对象包含 source summary、entity、topic、comparison、output、research agenda 和既有 lint report。
- `raw/` 剪藏正文不作为被审计文档；本轮只检查 Wiki 层对 raw 的引用覆盖、source summary 结构与证据密度。
- 本轮未把 research agenda 当事实依据；未做全量外部联网事实复核，涉及人物任职、公司状态和产品状态的当前性事实应进入后续 source 重读与联网复核队列。

## 治理恢复与同步规则

本文件是恢复 LLM Wiki 治理任务进度的状态源，不只是一次性审计报告。后续每轮治理开始时，应先读取本文的 `## 总览`、`## 剩余问题分类`、`## 剩余问题明细` 与 `## 逐篇核查索引`，再选择下一组待处理问题。

每轮治理结束前，必须把实际完成状态回写到本文，至少同步以下内容：

- `## 已当场修复`：追加本轮处理的页面簇、修复类型和关键结果。
- `## 总览`：更新剩余问题总数、高优先级、中优先级、低优先级数量。
- `## 剩余问题分类`：更新各类问题数量，已清零的类别保留为 `0`。
- `## 剩余问题明细`：删除已解决条目，保留下一轮真实待处理队列。
- `## 逐篇核查索引`：把已解决页面改为 `OK` 或更新其剩余问题类别。

完成同步后再运行 `tools/wiki-lint.py`。若治理改动没有同步到本文，下一轮恢复任务会从旧状态继续，造成重复处理或进度迷失。

## 已当场修复

- 4 个 output 补齐或更新 `updated` 字段。
- 3 个 output 补齐 `## 本文使用的 Wiki 页面` 与 `## 回填检查`。
- 3 个 source summary 将 `关联概念` 调整为模板要求的 `### 关联概念`。
- 已重读并扩写 8 篇最短 source summary：OpenClaw 两篇、Simon Willison 三篇、Wisdom Work、Always-On Economy 和 Skills 激励文章。
- 已继续重读并扩写 6 篇 source summary：code-is-cheap、LLM Wiki、Jevons Paradox 与 ontology 三篇。
- 本轮再重读并扩写 6 篇 source summary：AI capability gap、AI-first strategy、Martin Fowler fragments、enterprise readiness、Palantir FDSE 与 cybersecurity openness。
- 本轮继续重读并扩写 6 篇 source summary：Agent PR review、accessibility agent、P&G AI Factory metadata、Pinterest MCP ecosystem、agent-first process redesign 与 OpenAI FDE NYC。
- 本轮继续重读并扩写 6 篇 source summary：中文 FDE 综述、OpenAI FDE 方法页、P&G strategy-to-shelf、P&G insights/data、P&G AI factory 访谈与 GitHub agentic workflow token efficiency。
- 本轮继续重读并扩写 6 篇 source summary：Good Taste、Learning on the Shop Floor、MachinaCheck、Maintainability sensors、Management as AI superpower 与 Multi-Agent 组织病。
- 本轮继续重读并扩写 6 篇 source summary：The Conscious 1%、LLM Wiki 内容创作 3.0、Allocation Economy、Using Git with coding agents、What is agentic engineering 与 The PR you would have opened yourself。
- 本轮继续重读并扩写 6 篇 source summary：AI layoffs、Building Effective Agents、Taste for Makers、FDE 定义、What Is Code 与 AI 组织形态护城河；其中 Building Effective Agents 因 raw 缺页，按 Anthropic 官方原文补读后重编译。
- 本轮按用户确认补全 `building-effective-agents` 的本地 raw：新增并保留 `raw/building-effective-agents-complete.md` 与对应 `wiki/sources/building-effective-agents-complete.md`，删除旧的不完整 raw 与旧 source summary，并将相关 Wiki 引用统一指向完整版。
- 本轮继续重读并扩写 6 篇 source summary：美团 AI Coding 重构实践、OncoAgent、Why I Don’t Vibe Code、The Return of the Deployment Company、The Cybernetic Teammate 与 The Anatomy of an Agent Harness。
- 本轮继续清零剩余 `source-depth` 队列：扩写 OpenAI Deployment Company、Specialization Beats Scale，并修正 20260127 Claude Coding Notes 的关联概念格式。
- 本轮进入 `entity-depth` 阶段，扩写并补入 topic 入链 5 个高风险 Agent / 医疗 Agent 相关实体：Zero-PHI Policy、Corrective RAG、Dual-Tier LLM Architecture、Reflexion 与 Sequence Packing。
- 本轮继续扩写无障碍 Agent 相关实体：Social Model of Disability、Accessibility Complexity Evaluation、Accessibility High Risk Patterns，并修正 Accessibility Agent 的 definition 风格。
- 本轮继续扩写网络安全评测 / 安全硬化相关实体：AISI、Mythos、Security Hardening Phase、Cybersecurity Proof of Work，并将 AISI / Mythos 接入 Verifiable Agent Engineering。
- 本轮继续处理生成质量约束簇：扩写 Slopocalypse、AI Lacks Laziness、Laziness Virtue，补入 Karpathy AI Thought 与 Agentic Engineering Patterns 的 topic 入链，并修复 Agentic Engineering Patterns 的超长行。
- 本轮继续处理 Pinterest MCP 生产治理簇：扩写 Pinterest Engineering、MCP Registry、Model Context Protocol，并将 Pinterest 案例明确接入 Organization as Agent Harness。
- 本轮继续处理 CLAUDE.md 项目上下文合约簇：重写 CLAUDE-md，补入多源证据，接入 Code as Conceptual Infrastructure，并同步修正 Context Engineering 的 definition 风格。
- 本轮继续处理 AI 时代护城河与人才结构簇：重写 Chosen-vs-Seen，扩写 Organizational Shape Moat，并将 Moats in AI Era 接入 AI Era Economy Shift。
- 本轮继续处理 Demis / AGI 记忆与科学发现簇：扩写 Continual Learning、World Model、Einstein Test 与 Scientific Discovery AI，并接入 Agent Knowledge Management。
- 本轮清空 Entity 价值复核队列：扩写 Software Democratization、Agent Loops、Cross-Disciplinary Generalist，并分别接入 AI-Era Career Skills 与 Claude Code Automation。
- 本轮继续处理企业本体基础概念簇：扩写 Ontology、Knowledge Graph、ABox、TBox、Class、Individual、RDF、OWL 与 SPARQL，并补强 Enterprise Ontology Application 的最小架构与治理要点。
- 本轮继续处理企业本体工具链簇：扩写 GraphDB、HermiT、Protégé、Owlready2 与 Ontology-Agent，明确开发期建模、推理、运行时工具和生产语义服务的边界。
- 本轮继续处理软件概念基础设施簇：扩写 Conceptual Model、Bounded Context、Ubiquitous Language、Essential Complexity、YAGNI、Technical Debt Avoidance 与 Progressive Disclosure，强化 AI coding 中词汇、边界、克制和清债的判断框架。
- 本轮继续处理 AI 认知风险与多 Agent 病理簇：扩写 AI Psychosis、AI Restraint、Agent Cognitive Loafing、Agent Dissociation、Cognitive Debt、Ghost Intelligence 与 Jagged Intelligence，并补强 Multi-Agent Pathology and Governance 的治理矩阵。
- 本轮继续清理 definition / language 队列：将 8 个 Entity 的 frontmatter definition 改为中文短定义。
  涉及 Agent-First Enterprise、Conscious Creators、Decision Quality、Git-Fluent Agents、Human-Governor-Agent-Operator、Inner World Mastery、Machine-Readable Processes 与 Resonance，并修正 Git-Fluent Agents 标题错字。
- 本轮恢复治理进度后清空剩余 `definition` 队列：修正 AI-Native Shipping、AI-Native Startup、Andrej Karpathy 与 Cat Wu 的 frontmatter 短定义，并拆分 Cat Wu 定义块超长行。
- 本轮补入治理恢复与同步规则：明确本文是后续恢复任务进度的状态源，每轮治理结束前必须同步已修复事项、统计、明细和逐篇索引。
- 本轮继续处理 `entity-depth` 队列：扩写 AI-Native Shipping，补入机制拆解、传统敏捷对照、适用边界和判断标准，并接入 Product Overhang。
- 本轮继续处理 `entity-depth` 队列：扩写 AI Capability Gap，补入鸿沟生成机制、能力评估框架、相邻概念区别和组织决策含义。
- 本轮继续处理 `entity-depth` 队列：扩写 AI-Ready Organization，补入诊断维度、AI 放大机制、Agent-first 演进关系和治理门禁用法。
- 本轮继续处理 `entity-depth` 队列：扩写 Adversarial Distillation，补入激励失配机制、对抗策略检测信号、破局方向、技术防投毒和组织使用边界。
- 本轮继续处理 `entity-depth` 与 `definition-style` 交叉队列：扩写 Agent Tenacity，改写稳定中文定义，补入生成机制、使用条件、失败模式、验证边界和工程操作化做法。
- 本轮继续处理 `entity-depth` 队列：扩写 Alignment Tax，补入 AI 暴露对齐税的生成机制、早期信号、裁员短期压缩效应和降低对齐税的治理动作。
- 本轮继续处理 `entity-depth` 队列：扩写 Allocation Economy，补入核心转变、资源编排链条、Model Manager 能力、经济影响与失败模式，并修正不稳的管理者数量表述。
- 本轮继续处理 `entity-depth` 队列：扩写 Bias-to-Action LLM，补入行动偏差生成机制、无障碍 Agent 风险、harness 护栏设计、克制能力和适用边界。
- 本轮继续处理 `entity-depth` 与 `definition-style` 交叉队列：扩写 Claude Cowork，补入产品面分工、运营工作流结构、阶段用法、护城河边界、权限风险和组织韧性限制。
- 本轮继续处理 `entity-depth` 与 `definition-style` 交叉队列：扩写 Competent Output，补入合格产出的质量陷阱、诊断问题、升级路径、适用边界和与 Taste / Judgment / Refusal 的关系。
- 本轮继续处理 `entity-depth` 与 `definition-style` 交叉队列：扩写 Friction as Design Signal，补入摩擦分类、保留/消除判断、操作流程、Vibe Coding 边界和误用风险。
- 本轮继续处理 `entity-depth` 队列：扩写 Golden Case，补入识别标准、生成路径、非黄金用例边界、FDE 放大机制、迁移边界和治理动作。
- 本轮继续处理 `entity-depth` 与 `definition-style` 交叉队列：扩写 History Rewriting，补入 Git 历史叙事观、Agent 工作流、操作分层、协作边界和可验证恢复路径。
- 本轮继续处理 `entity-depth` 队列：扩写 Input Output Outcome，补入 AI 预算审查、input 到 outcome 转换链、常见误判、分配经济关系和组织治理边界。
- 本轮继续处理 `entity-depth` 队列：扩写 Invisible Orchestrator，补入不可见编排的结构机制、可见/不可见编排区别、可隐藏边界、高风险信号和影响链治理动作。
- 本轮继续处理 `entity-depth` 队列：扩写 Latent Space vs Deterministic，补入 LLM/代码分工原则、混合接口、误用模式、LLM Wiki 应用和设计检查表。
- 5 个 topic 表格移除表格内未转义的 wikilink 管道，避免列数错乱。
- 复跑 `tools/wiki-lint.py` 后，硬性 lint 阻断问题为 0。
- 本轮清零 `comparison-depth` 队列：扩写 Taste-vs-Judgment（1471→6782B，补入何时分裂、AI 组织含义、失败模式）、Vibe-Coding-vs-Software-2.0（1883→7693B，补入演进脉络、工程治理维度、失败模式）与 Cook-vs-Chef（2248→8096B，补入伪装失败模式、组织分布含义），并为三者补入更多 source_raw 证据。
- 本轮继续处理 `entity-depth` 与 `definition-style` 交叉簇：扩写 Product-Market-Fit（1482→4929B，补入 Push→Pull 相变机制、Boris Cherny pre-PMF 证据、供给侧 PMF 触发）、Problem-Solution-Fit（1412→3875B，补入 AI 确认偏差陷阱、验证纪律、跨源连接）、Product-Overhang（1390→5044B，补入能力发现机制、与传统策略对比表、模型自省连接）、Software-3.0（1491→4509B，补入三范式对比表、CLAUDE.md 工程含义、确定性分工）、Specialization-Compounds（1592→4998B，补入企业飞轮三条件、采购决策连接、评测集产权）、Tacit-Knowledge-Lock-In（1407→6043B，补入三层锁定机制、买方治理动作表、飞轮张力）。同步修复 Product-Market-Fit、Problem-Solution-Fit、Software-3.0 的 definition 风格。

## 总览

| 指标 | 数量 |
|------|------|
| `source-summary` | 68 |
| `entity` | 195 |
| `topic` | 26 |
| `comparison` | 14 |
| `output` | 6 |
| `research-agenda` | 1 |
| `lint-report` | 1 |
| 剩余问题总数 | 83 |
| 高优先级问题 | 0 |
| 中优先级问题 | 44 |
| 低优先级问题 | 39 |

## 剩余问题分类

| 类别 | 数量 | 解释 |
|------|------|------|
| `definition-style` | 30 | definition 风格不统一，常见为句号结尾或把年份/来源写进定义。 |
| `entity-depth` | 20 | 非人物 Entity 偏短，需要补关键数据、前提边界和关联。 |
| `definition` | 0 | definition 过长或过短，影响 Obsidian 未链接提及和快速理解。 |
| `topic-depth` | 7 | Topic 偏短，需要从多篇 source 重新综合。 |
| `person-depth` | 11 | 人物 Entity 偏短，建议补来源关系和只保留可验证履历。 |
| `language` | 0 | Wiki 默认中文，但 definition 仍基本为英文。 |
| `readability` | 5 | 超长行影响阅读与 diff。 |
| `entity-structure` | 4 | Entity 标准章节顺序不一致。 |
| `topic-evidence` | 4 | Topic 的 source_raw 少于 2 个，主题层证据不够稳。 |
| `comparison-depth` | 0 | Comparison 正文偏短，区分维度不够展开。 |
| `comparison-evidence` | 2 | Comparison 的 source_raw 过少，概念区分可能证据单薄。 |

## Entity 价值审计队列

| 队列 | 数量 | 处理建议 |
|------|------|----------|
| 合并或降级 | 0 | 优先判断是否应回收到 source summary 或更大 Entity。 |
| 复核 | 0 | 补入 topic/comparison，或合并、降级。 |

### 合并或降级候选

- 当前无合并或降级候选。

### 复核候选

- 当前无复核候选。

## 最高收益修复顺序

1. 先处理 `entity-depth` 与 Entity 价值队列：把单源低入链概念合并或补入 topic。
2. 再处理 `topic-evidence` 与 `comparison-evidence`：主题/对比页至少应由多个 source 支撑。
3. 再处理 `topic-depth`：补充区分维度、反例和跨来源证据。`comparison-depth` 已清零。
4. 最后统一 definition 风格：中文、短定义、少来源痕迹、无句号。

## 剩余问题明细

| 等级 | 类别 | 文件 | 行 | 问题 |
|------|------|------|----|------|
| 中 | `comparison-evidence` | `wiki/comparisons/Agent-First-vs-Traditional-Automation.md` | - | Comparison source_raw 少于 2 个 |
| 中 | `comparison-evidence` | `wiki/comparisons/Knowledge-Work-vs-Wisdom-Work.md` | - | Comparison source_raw 少于 2 个 |
| 中 | `entity-depth` | `wiki/entities/Lehrwerkstatt.md` | - | 非人物 Entity 正文偏短 1457 bytes |
| 中 | `entity-depth` | `wiki/entities/MIT-Technology-Review-Insights.md` | - | 非人物 Entity 正文偏短 929 bytes |
| 中 | `entity-depth` | `wiki/entities/Model-Introspection.md` | - | 非人物 Entity 正文偏短 1366 bytes |
| 中 | `entity-depth` | `wiki/entities/Organizational-Self-Awareness.md` | - | 非人物 Entity 正文偏短 1137 bytes |
| 中 | `entity-depth` | `wiki/entities/Osmosis-Learning.md` | - | 非人物 Entity 正文偏短 1160 bytes |
| 中 | `entity-depth` | `wiki/entities/PM-in-AI-Era.md` | - | 非人物 Entity 正文偏短 1441 bytes |
| 中 | `entity-depth` | `wiki/entities/Programming-Languages-as-Thinking-Tools.md` | - | 非人物 Entity 正文偏短 1418 bytes |
| 中 | `entity-depth` | `wiki/entities/Public-only-Constraint.md` | - | 非人物 Entity 正文偏短 1005 bytes |
| 中 | `entity-depth` | `wiki/entities/Refusal.md` | - | 非人物 Entity 正文偏短 1456 bytes |
| 中 | `entity-depth` | `wiki/entities/Research-Preview.md` | - | 非人物 Entity 正文偏短 1272 bytes |
| 中 | `entity-depth` | `wiki/entities/River-Agent.md` | - | 非人物 Entity 正文偏短 1030 bytes |
| 中 | `entity-depth` | `wiki/entities/Runway-Math.md` | - | 非人物 Entity 正文偏短 1483 bytes |
| 中 | `entity-depth` | `wiki/entities/Specialized-Small-Models.md` | - | 非人物 Entity 正文偏短 1530 bytes |
| 中 | `entity-depth` | `wiki/entities/Thin-Harness-Fat-Skills.md` | - | 非人物 Entity 正文偏短 1477 bytes |
| 中 | `entity-depth` | `wiki/entities/Time-Moat.md` | - | 非人物 Entity 正文偏短 1453 bytes |
| 中 | `entity-depth` | `wiki/entities/Tool-Use-Architecture.md` | - | 非人物 Entity 正文偏短 1519 bytes |
| 中 | `entity-depth` | `wiki/entities/Verifiability.md` | - | 非人物 Entity 正文偏短 1254 bytes |
| 中 | `entity-depth` | `wiki/entities/Vocabulary-Building.md` | - | 非人物 Entity 正文偏短 1339 bytes |
| 中 | `entity-depth` | `wiki/entities/WCAG.md` | - | 非人物 Entity 正文偏短 1313 bytes |
| 中 | `entity-depth` | `wiki/entities/渐进式重构.md` | - | 非人物 Entity 正文偏短 1567 bytes |
| 中 | `person-depth` | `wiki/entities/Arnav-Gupta.md` | - | 人物 Entity 偏短 714 bytes |
| 中 | `person-depth` | `wiki/entities/Drew-Breunig.md` | - | 人物 Entity 偏短 755 bytes |
| 中 | `person-depth` | `wiki/entities/Elvis-Sun.md` | - | 人物 Entity 偏短 1065 bytes |
| 中 | `person-depth` | `wiki/entities/Erick-Lachmann.md` | - | 人物 Entity 偏短 612 bytes |
| 中 | `person-depth` | `wiki/entities/Ethan-Mollick.md` | - | 人物 Entity 偏短 1174 bytes |
| 中 | `person-depth` | `wiki/entities/Jacob-Harris.md` | - | 人物 Entity 偏短 803 bytes |
| 中 | `person-depth` | `wiki/entities/Paul-Graham.md` | - | 人物 Entity 偏短 1089 bytes |
| 中 | `person-depth` | `wiki/entities/Pimenta-de-Freitas-Cardoso.md` | - | 人物 Entity 偏短 699 bytes |
| 中 | `person-depth` | `wiki/entities/Tobi-Lütke.md` | - | 人物 Entity 偏短 1097 bytes |
| 中 | `person-depth` | `wiki/entities/Wes-Botman.md` | - | 人物 Entity 偏短 1091 bytes |
| 中 | `person-depth` | `wiki/entities/朱少民.md` | - | 人物 Entity 偏短 790 bytes |
| 中 | `topic-depth` | `wiki/topics/AI-Apprenticeship-and-Lehrwerkstatt.md` | - | Topic 正文偏短 2396 bytes |
| 中 | `topic-depth` | `wiki/topics/AI-Labor-Bottleneck-Shift.md` | - | Topic 正文偏短 2602 bytes |
| 中 | `topic-depth` | `wiki/topics/Agent-First-Process-Redesign.md` | - | Topic 正文偏短 2235 bytes |
| 中 | `topic-depth` | `wiki/topics/Conscious-Creation-in-AI-Era.md` | - | Topic 正文偏短 1855 bytes |
| 中 | `topic-depth` | `wiki/topics/Enterprise-AI-Factory.md` | - | Topic 正文偏短 2730 bytes |
| 中 | `topic-depth` | `wiki/topics/Git-with-Coding-Agents.md` | - | Topic 正文偏短 2640 bytes |
| 中 | `topic-depth` | `wiki/topics/Wisdom-Work-Evolution.md` | - | Topic 正文偏短 2638 bytes |
| 中 | `topic-evidence` | `wiki/topics/Conscious-Creation-in-AI-Era.md` | - | Topic source_raw 少于 2 个：1 |
| 中 | `topic-evidence` | `wiki/topics/Git-with-Coding-Agents.md` | - | Topic source_raw 少于 2 个：1 |
| 中 | `topic-evidence` | `wiki/topics/Lean-Indie-Engineering.md` | - | Topic source_raw 少于 2 个：1 |
| 中 | `topic-evidence` | `wiki/topics/Wisdom-Work-Evolution.md` | - | Topic source_raw 少于 2 个：1 |
| 低 | `definition-style` | `wiki/entities/Agent-Generated-PRs.md` | - | definition 以句号结尾，风格不统一 |
| 低 | `definition-style` | `wiki/entities/Agent-Generated-PRs.md` | - | definition 含年份/来源痕迹，可能把来源事实写进概念定义 |
| 低 | `definition-style` | `wiki/entities/Agent-Orchestration.md` | - | definition 以句号结尾，风格不统一 |
| 低 | `definition-style` | `wiki/entities/Agent-Swarm.md` | - | definition 以句号结尾，风格不统一 |
| 低 | `definition-style` | `wiki/entities/Claude-Code-CLI.md` | - | definition 以句号结尾，风格不统一 |
| 低 | `definition-style` | `wiki/entities/Cybersecurity-Openness.md` | - | definition 以句号结尾，风格不统一 |
| 低 | `definition-style` | `wiki/entities/Cybersecurity-Openness.md` | - | definition 含年份/来源痕迹，可能把来源事实写进概念定义 |
| 低 | `definition-style` | `wiki/entities/Dominator-Analysis.md` | - | definition 以句号结尾，风格不统一 |
| 低 | `definition-style` | `wiki/entities/Drew-Breunig.md` | - | definition 以句号结尾，风格不统一 |
| 低 | `definition-style` | `wiki/entities/Hardware-Sovereignty.md` | - | definition 以句号结尾，风格不统一 |
| 低 | `definition-style` | `wiki/entities/Headless-Mode.md` | - | definition 以句号结尾，风格不统一 |
| 低 | `definition-style` | `wiki/entities/Jacob-Harris.md` | - | definition 以句号结尾，风格不统一 |
| 低 | `definition-style` | `wiki/entities/Knowledge-Compilation.md` | - | definition 以句号结尾，风格不统一 |
| 低 | `definition-style` | `wiki/entities/Lehrwerkstatt.md` | - | definition 以句号结尾，风格不统一 |
| 低 | `definition-style` | `wiki/entities/MachinaCheck.md` | - | definition 以句号结尾，风格不统一 |
| 低 | `definition-style` | `wiki/entities/Martin-Fowler.md` | - | definition 以句号结尾，风格不统一 |
| 低 | `definition-style` | `wiki/entities/Memex.md` | - | definition 以句号结尾，风格不统一 |
| 低 | `definition-style` | `wiki/entities/Memex.md` | - | definition 含年份/来源痕迹，可能把来源事实写进概念定义 |
| 低 | `definition-style` | `wiki/entities/Multi-Layer-Memory.md` | - | definition 以句号结尾，风格不统一 |
| 低 | `definition-style` | `wiki/entities/Osmosis-Learning.md` | - | definition 以句号结尾，风格不统一 |
| 低 | `definition-style` | `wiki/entities/Ownership.md` | - | definition 以句号结尾，风格不统一 |
| 低 | `definition-style` | `wiki/entities/Programming-Languages-as-Thinking-Tools.md` | - | definition 以句号结尾，风格不统一 |
| 低 | `definition-style` | `wiki/entities/Simon-Willison.md` | - | definition 以句号结尾，风格不统一 |
| 低 | `definition-style` | `wiki/entities/Software-2.0.md` | - | definition 以句号结尾，风格不统一 |
| 低 | `definition-style` | `wiki/entities/The-OpenAI-Deployment-Company.md` | - | definition 含年份/来源痕迹，可能把来源事实写进概念定义 |
| 低 | `definition-style` | `wiki/entities/Three-State-Protocol.md` | - | definition 以句号结尾，风格不统一 |
| 低 | `definition-style` | `wiki/entities/Tobi-Lütke.md` | - | definition 以句号结尾，风格不统一 |
| 低 | `definition-style` | `wiki/entities/Unmesh-Joshi.md` | - | definition 以句号结尾，风格不统一 |
| 低 | `definition-style` | `wiki/entities/Vibe-Coding.md` | - | definition 含年份/来源痕迹，可能把来源事实写进概念定义 |
| 低 | `definition-style` | `wiki/entities/Vocabulary-Building.md` | - | definition 以句号结尾，风格不统一 |
| 低 | `entity-structure` | `wiki/entities/Always-On-Economy.md` | - | 标准章节顺序不一致 |
| 低 | `entity-structure` | `wiki/entities/Compound-Engineering.md` | - | 标准章节顺序不一致 |
| 低 | `entity-structure` | `wiki/entities/Jevons-Paradox-for-Knowledge-Work.md` | - | 标准章节顺序不一致 |
| 低 | `entity-structure` | `wiki/entities/Vibe-Coding.md` | - | 标准章节顺序不一致 |
| 低 | `readability` | `wiki/comparisons/RAG-vs-LLM-Wiki.md` | 252 | 超长行 284 字符 |
| 低 | `readability` | `wiki/entities/Demis-Hassabis.md` | 25 | 超长行 281 字符 |
| 低 | `readability` | `wiki/entities/Memex.md` | 86 | 超长行 398 字符 |
| 低 | `readability` | `wiki/entities/Vibe-Coding.md` | 125 | 超长行 289 字符 |
| 低 | `readability` | `wiki/sources/How I run multiple USD10K MRR companies on a USD20month tech stack.md` | 28 | 超长行 248 字符 |

## 逐篇核查索引

状态为 `OK` 表示本轮规则扫描未发现问题；它不等于该页已完成外部事实复核。

| 文件 | 类型 | 字节 | 问题数 | 状态/问题类别 |
|------|------|------|--------|---------------|
| `wiki/comparisons/AI-Factory-vs-Forward-Deployed-AI-Enablement.md` | `comparison` | 4114 | 0 | OK |
| `wiki/comparisons/AI-Ready-Organization-vs-Agent-First-Enterprise.md` | `comparison` | 2944 | 0 | OK |
| `wiki/comparisons/Agent-First-vs-Traditional-Automation.md` | `comparison` | 3117 | 1 | comparison-evidence |
| `wiki/comparisons/Agent-Harness-vs-Agent-Workflow-Patterns.md` | `comparison` | 3050 | 0 | OK |
| `wiki/comparisons/Agentic-Engineering-vs-Vibe-Coding.md` | `comparison` | 3722 | 0 | OK |
| `wiki/comparisons/Cognitive-Debt-vs-Technical-Debt.md` | `comparison` | 2773 | 0 | OK |
| `wiki/comparisons/Context-Engineering-vs-Knowledge-Compilation.md` | `comparison` | 2940 | 0 | OK |
| `wiki/comparisons/Cook-vs-Chef.md` | `comparison` | 8096 | 0 | OK |
| `wiki/comparisons/Deployment-Product-Flywheel-vs-Tacit-Knowledge-Lock-In.md` | `comparison` | 2802 | 0 | OK |
| `wiki/comparisons/Knowledge-Work-vs-Wisdom-Work.md` | `comparison` | 2850 | 1 | comparison-evidence |
| `wiki/comparisons/Ontology-vs-Knowledge-Graph.md` | `comparison` | 2864 | 0 | OK |
| `wiki/comparisons/RAG-vs-LLM-Wiki.md` | `comparison` | 7872 | 1 | readability |
| `wiki/comparisons/Taste-vs-Judgment.md` | `comparison` | 6782 | 0 | OK |
| `wiki/comparisons/Vibe-Coding-vs-Software-2.0.md` | `comparison` | 7693 | 0 | OK |
| `wiki/entities/ABox.md` | `entity` | 1798 | 0 | OK |
| `wiki/entities/ACI-Agent-Computer-Interface.md` | `entity` | 2123 | 0 | OK |
| `wiki/entities/AI-Capability-Gap.md` | `entity` | 5621 | 0 | OK |
| `wiki/entities/AI-Factory.md` | `entity` | 2083 | 0 | OK |
| `wiki/entities/AI-First.md` | `entity` | 2628 | 0 | OK |
| `wiki/entities/AI-Lacks-Laziness.md` | `entity` | 2021 | 0 | OK |
| `wiki/entities/AI-Native-Shipping.md` | `entity` | 4873 | 0 | OK |
| `wiki/entities/AI-Native-Startup.md` | `entity` | 3336 | 0 | OK |
| `wiki/entities/AI-Psychosis.md` | `entity` | 2166 | 0 | OK |
| `wiki/entities/AI-Ready-Organization.md` | `entity` | 5312 | 0 | OK |
| `wiki/entities/AI-Restraint.md` | `entity` | 1806 | 0 | OK |
| `wiki/entities/AISI.md` | `entity` | 1814 | 0 | OK |
| `wiki/entities/Aaron-Levie.md` | `entity` | 1352 | 0 | OK |
| `wiki/entities/Accessibility-Agent.md` | `entity` | 2563 | 0 | OK |
| `wiki/entities/Accessibility-Complexity-Evaluation.md` | `entity` | 2068 | 0 | OK |
| `wiki/entities/Accessibility-High-Risk-Patterns.md` | `entity` | 2099 | 0 | OK |
| `wiki/entities/Adversarial-Distillation.md` | `entity` | 7901 | 0 | OK |
| `wiki/entities/Agent-Cognitive-Loafing.md` | `entity` | 1951 | 0 | OK |
| `wiki/entities/Agent-Dissociation.md` | `entity` | 2079 | 0 | OK |
| `wiki/entities/Agent-First-Enterprise.md` | `entity` | 2840 | 0 | OK |
| `wiki/entities/Agent-Generated-PRs.md` | `entity` | 2204 | 2 | definition-style |
| `wiki/entities/Agent-Harness.md` | `entity` | 6851 | 0 | OK |
| `wiki/entities/Agent-Loops.md` | `entity` | 2158 | 0 | OK |
| `wiki/entities/Agent-Native.md` | `entity` | 2032 | 0 | OK |
| `wiki/entities/Agent-Orchestration.md` | `entity` | 3887 | 1 | definition-style |
| `wiki/entities/Agent-PR-Review.md` | `entity` | 3312 | 0 | OK |
| `wiki/entities/Agent-Swarm.md` | `entity` | 4329 | 1 | definition-style |
| `wiki/entities/Agent-Tenacity.md` | `entity` | 6826 | 0 | OK |
| `wiki/entities/Agent-Workflow-Patterns.md` | `entity` | 2738 | 0 | OK |
| `wiki/entities/Agentic-Engineering.md` | `entity` | 5660 | 0 | OK |
| `wiki/entities/Agentic-Workflow-Token-Efficiency.md` | `entity` | 3218 | 0 | OK |
| `wiki/entities/Alignment-Tax.md` | `entity` | 7296 | 0 | OK |
| `wiki/entities/Allocation-Economy.md` | `entity` | 6913 | 0 | OK |
| `wiki/entities/Always-On-Economy.md` | `entity` | 1892 | 1 | entity-structure |
| `wiki/entities/Andrej-Karpathy.md` | `entity` | 4121 | 0 | OK |
| `wiki/entities/Anti-Enterprise-Mindset.md` | `entity` | 1645 | 0 | OK |
| `wiki/entities/Arnav-Gupta.md` | `entity` | 714 | 1 | person-depth |
| `wiki/entities/B2B-Nurture-C-Model.md` | `entity` | 1673 | 0 | OK |
| `wiki/entities/Barry-Zhang.md` | `entity` | 1278 | 0 | OK |
| `wiki/entities/Bias-to-Action-LLM.md` | `entity` | 6193 | 0 | OK |
| `wiki/entities/Boris-Cherny.md` | `entity` | 1478 | 0 | OK |
| `wiki/entities/Bounded-Context.md` | `entity` | 2028 | 0 | OK |
| `wiki/entities/Business-Embedded-AI-Organization.md` | `entity` | 1843 | 0 | OK |
| `wiki/entities/CLAUDE-md.md` | `entity` | 3154 | 0 | OK |
| `wiki/entities/Cat-Wu.md` | `entity` | 1908 | 0 | OK |
| `wiki/entities/Chosen-vs-Seen.md` | `entity` | 2372 | 0 | OK |
| `wiki/entities/Class.md` | `entity` | 1686 | 0 | OK |
| `wiki/entities/Claude-Code-CLI.md` | `entity` | 2510 | 1 | definition-style |
| `wiki/entities/Claude-Cowork.md` | `entity` | 6888 | 0 | OK |
| `wiki/entities/Code-Execution.md` | `entity` | 1815 | 0 | OK |
| `wiki/entities/Coding-Agents.md` | `entity` | 2660 | 0 | OK |
| `wiki/entities/Cognitive-Debt.md` | `entity` | 2070 | 0 | OK |
| `wiki/entities/Competent-Output.md` | `entity` | 6142 | 0 | OK |
| `wiki/entities/Compound-Engineering.md` | `entity` | 1753 | 1 | entity-structure |
| `wiki/entities/Conceptual-Model.md` | `entity` | 2207 | 0 | OK |
| `wiki/entities/Connection.md` | `entity` | 1938 | 0 | OK |
| `wiki/entities/Conscious-Creators.md` | `entity` | 3043 | 0 | OK |
| `wiki/entities/Constraint-Driven-Engineering.md` | `entity` | 1733 | 0 | OK |
| `wiki/entities/Context-Engineering.md` | `entity` | 3995 | 0 | OK |
| `wiki/entities/Continual-Learning.md` | `entity` | 2324 | 0 | OK |
| `wiki/entities/Corrective-RAG.md` | `entity` | 2159 | 0 | OK |
| `wiki/entities/Cross-Disciplinary-Generalist.md` | `entity` | 1914 | 0 | OK |
| `wiki/entities/Cybernetic-Teammate.md` | `entity` | 1882 | 0 | OK |
| `wiki/entities/Cybersecurity-Openness.md` | `entity` | 1827 | 2 | definition-style |
| `wiki/entities/Cybersecurity-Proof-of-Work.md` | `entity` | 1822 | 0 | OK |
| `wiki/entities/Dan-Shipper.md` | `entity` | 1399 | 0 | OK |
| `wiki/entities/Decision-Quality.md` | `entity` | 2688 | 0 | OK |
| `wiki/entities/Demis-Hassabis.md` | `entity` | 1577 | 1 | readability |
| `wiki/entities/Deployment-Product-Flywheel.md` | `entity` | 1722 | 0 | OK |
| `wiki/entities/Discernment.md` | `entity` | 1743 | 0 | OK |
| `wiki/entities/Distributional-Alignment.md` | `entity` | 1696 | 0 | OK |
| `wiki/entities/Dominator-Analysis.md` | `entity` | 2095 | 1 | definition-style |
| `wiki/entities/Drew-Breunig.md` | `entity` | 755 | 2 | definition-style; person-depth |
| `wiki/entities/Dual-Tier-LLM-Architecture.md` | `entity` | 2325 | 0 | OK |
| `wiki/entities/Einstein-Test.md` | `entity` | 1915 | 0 | OK |
| `wiki/entities/Elvis-Sun.md` | `entity` | 1065 | 1 | person-depth |
| `wiki/entities/Emotional-Clarity.md` | `entity` | 2087 | 0 | OK |
| `wiki/entities/Erick-Lachmann.md` | `entity` | 612 | 1 | person-depth |
| `wiki/entities/Erik-Schluntz.md` | `entity` | 1390 | 0 | OK |
| `wiki/entities/Essential-Complexity.md` | `entity` | 2255 | 0 | OK |
| `wiki/entities/Ethan-Mollick.md` | `entity` | 1174 | 1 | person-depth |
| `wiki/entities/Evaluation-Set.md` | `entity` | 1665 | 0 | OK |
| `wiki/entities/Forward-Deployed-Engineer.md` | `entity` | 2941 | 0 | OK |
| `wiki/entities/Friction-as-Design-Signal.md` | `entity` | 7203 | 0 | OK |
| `wiki/entities/GBrain.md` | `entity` | 1686 | 0 | OK |
| `wiki/entities/Ghost-Intelligence.md` | `entity` | 1737 | 0 | OK |
| `wiki/entities/Git-Fluent-Agents.md` | `entity` | 3186 | 0 | OK |
| `wiki/entities/Golden-Case.md` | `entity` | 8149 | 0 | OK |
| `wiki/entities/GraphDB.md` | `entity` | 1916 | 0 | OK |
| `wiki/entities/Hardware-Sovereignty.md` | `entity` | 1647 | 1 | definition-style |
| `wiki/entities/Harness-Engineering.md` | `entity` | 3594 | 0 | OK |
| `wiki/entities/Headless-Mode.md` | `entity` | 3234 | 1 | definition-style |
| `wiki/entities/HermiT.md` | `entity` | 1696 | 0 | OK |
| `wiki/entities/History-Rewriting.md` | `entity` | 6322 | 0 | OK |
| `wiki/entities/Human-Governor-Agent-Operator.md` | `entity` | 2726 | 0 | OK |
| `wiki/entities/Individual.md` | `entity` | 1756 | 0 | OK |
| `wiki/entities/Inner-World-Mastery.md` | `entity` | 3584 | 0 | OK |
| `wiki/entities/Input-Output-Outcome.md` | `entity` | 8199 | 0 | OK |
| `wiki/entities/Integration-Wall.md` | `entity` | 1768 | 0 | OK |
| `wiki/entities/Invisible-Orchestrator.md` | `entity` | 7592 | 0 | OK |
| `wiki/entities/Jacob-Harris.md` | `entity` | 803 | 2 | definition-style; person-depth |
| `wiki/entities/Jagged-Intelligence.md` | `entity` | 1739 | 0 | OK |
| `wiki/entities/Jevons-Paradox-for-Knowledge-Work.md` | `entity` | 1820 | 1 | entity-structure |
| `wiki/entities/Joe-Hudson.md` | `entity` | 1357 | 0 | OK |
| `wiki/entities/Judgment.md` | `entity` | 2284 | 0 | OK |
| `wiki/entities/Knowledge-Compilation.md` | `entity` | 4957 | 1 | definition-style |
| `wiki/entities/Knowledge-Graph.md` | `entity` | 1689 | 0 | OK |
| `wiki/entities/Knowledge-Work.md` | `entity` | 2846 | 0 | OK |
| `wiki/entities/Konstantine-Buhler.md` | `entity` | 1235 | 0 | OK |
| `wiki/entities/LLM-Wiki.md` | `entity` | 2247 | 0 | OK |
| `wiki/entities/Latent-Knowledge-Demand.md` | `entity` | 1607 | 0 | OK |
| `wiki/entities/Latent-Space-vs-Deterministic.md` | `entity` | 7817 | 0 | OK |
| `wiki/entities/Layered-AI-Sourcing.md` | `entity` | 2126 | 0 | OK |
| `wiki/entities/Laziness-Virtue.md` | `entity` | 1851 | 0 | OK |
| `wiki/entities/Lean-Stack.md` | `entity` | 2111 | 0 | OK |
| `wiki/entities/Lehrwerkstatt.md` | `entity` | 1457 | 2 | definition-style; entity-depth |
| `wiki/entities/MCP-Registry.md` | `entity` | 2377 | 0 | OK |
| `wiki/entities/MIT-Technology-Review-Insights.md` | `entity` | 929 | 1 | entity-depth |
| `wiki/entities/MachinaCheck.md` | `entity` | 2464 | 1 | definition-style |
| `wiki/entities/Machine-Readable-Processes.md` | `entity` | 2848 | 0 | OK |
| `wiki/entities/Martin-Fowler.md` | `entity` | 1532 | 1 | definition-style |
| `wiki/entities/Memex.md` | `entity` | 3998 | 3 | definition-style; readability |
| `wiki/entities/Moats-in-AI-Era.md` | `entity` | 1638 | 0 | OK |
| `wiki/entities/Model-Context-Protocol-MCP.md` | `entity` | 2683 | 0 | OK |
| `wiki/entities/Model-Introspection.md` | `entity` | 1366 | 1 | entity-depth |
| `wiki/entities/Model-Manager.md` | `entity` | 2276 | 0 | OK |
| `wiki/entities/Multi-Agent-System-Pathology.md` | `entity` | 1857 | 0 | OK |
| `wiki/entities/Multi-Layer-Memory.md` | `entity` | 3531 | 1 | definition-style |
| `wiki/entities/Mythos.md` | `entity` | 1820 | 0 | OK |
| `wiki/entities/OWL.md` | `entity` | 1845 | 0 | OK |
| `wiki/entities/Obsidian-Wiki.md` | `entity` | 1682 | 0 | OK |
| `wiki/entities/Ontology-Agent.md` | `entity` | 2377 | 0 | OK |
| `wiki/entities/Ontology.md` | `entity` | 2272 | 0 | OK |
| `wiki/entities/Organizational-Self-Awareness.md` | `entity` | 1137 | 1 | entity-depth |
| `wiki/entities/Organizational-Shape-Moat.md` | `entity` | 2421 | 0 | OK |
| `wiki/entities/Osmosis-Learning.md` | `entity` | 1160 | 2 | definition-style; entity-depth |
| `wiki/entities/Owlready2.md` | `entity` | 1934 | 0 | OK |
| `wiki/entities/Ownership.md` | `entity` | 1683 | 1 | definition-style |
| `wiki/entities/PM-in-AI-Era.md` | `entity` | 1441 | 1 | entity-depth |
| `wiki/entities/Paul-Graham.md` | `entity` | 1089 | 1 | person-depth |
| `wiki/entities/Pimenta-de-Freitas-Cardoso.md` | `entity` | 699 | 1 | person-depth |
| `wiki/entities/Pinterest-Engineering.md` | `entity` | 2686 | 0 | OK |
| `wiki/entities/Problem-Solution-Fit.md` | `entity` | 3875 | 0 | OK |
| `wiki/entities/Product-Market-Fit.md` | `entity` | 4929 | 0 | OK |
| `wiki/entities/Product-Overhang.md` | `entity` | 5044 | 0 | OK |
| `wiki/entities/Programming-Languages-as-Thinking-Tools.md` | `entity` | 1418 | 2 | definition-style; entity-depth |
| `wiki/entities/Progressive-Disclosure.md` | `entity` | 2274 | 0 | OK |
| `wiki/entities/Protégé.md` | `entity` | 1694 | 0 | OK |
| `wiki/entities/Public-only-Constraint.md` | `entity` | 1005 | 1 | entity-depth |
| `wiki/entities/RDF.md` | `entity` | 1820 | 0 | OK |
| `wiki/entities/Raj-Nandan-Sharma.md` | `entity` | 1355 | 0 | OK |
| `wiki/entities/Reflexion.md` | `entity` | 2026 | 0 | OK |
| `wiki/entities/Refusal.md` | `entity` | 1456 | 1 | entity-depth |
| `wiki/entities/Research-Preview.md` | `entity` | 1272 | 1 | entity-depth |
| `wiki/entities/Resonance.md` | `entity` | 3026 | 0 | OK |
| `wiki/entities/River-Agent.md` | `entity` | 1030 | 1 | entity-depth |
| `wiki/entities/Runway-Math.md` | `entity` | 1483 | 1 | entity-depth |
| `wiki/entities/SPARQL.md` | `entity` | 1692 | 0 | OK |
| `wiki/entities/Scientific-Discovery-AI.md` | `entity` | 2079 | 0 | OK |
| `wiki/entities/Security-Hardening-Phase.md` | `entity` | 1953 | 0 | OK |
| `wiki/entities/Sequence-Packing.md` | `entity` | 2171 | 0 | OK |
| `wiki/entities/Simon-Willison.md` | `entity` | 2120 | 1 | definition-style |
| `wiki/entities/Slopocalypse.md` | `entity` | 1946 | 0 | OK |
| `wiki/entities/Social-Model-of-Disability.md` | `entity` | 2159 | 0 | OK |
| `wiki/entities/Software-2.0.md` | `entity` | 3648 | 1 | definition-style |
| `wiki/entities/Software-3.0.md` | `entity` | 4509 | 0 | OK |
| `wiki/entities/Software-Democratization.md` | `entity` | 2025 | 0 | OK |
| `wiki/entities/Specialization-Compounds.md` | `entity` | 4998 | 0 | OK |
| `wiki/entities/Specialized-Small-Models.md` | `entity` | 1530 | 1 | entity-depth |
| `wiki/entities/Specificity.md` | `entity` | 1787 | 0 | OK |
| `wiki/entities/Steve-Hanov.md` | `entity` | 1927 | 0 | OK |
| `wiki/entities/TBox.md` | `entity` | 1810 | 0 | OK |
| `wiki/entities/Tacit-Knowledge-Lock-In.md` | `entity` | 6043 | 0 | OK |
| `wiki/entities/Taste.md` | `entity` | 2528 | 0 | OK |
| `wiki/entities/Technical-Debt-Avoidance.md` | `entity` | 2446 | 0 | OK |
| `wiki/entities/The-OpenAI-Deployment-Company.md` | `entity` | 2023 | 1 | definition-style |
| `wiki/entities/Thin-Harness-Fat-Skills.md` | `entity` | 1477 | 1 | entity-depth |
| `wiki/entities/Three-State-Protocol.md` | `entity` | 3552 | 1 | definition-style |
| `wiki/entities/Time-Moat.md` | `entity` | 1453 | 1 | entity-depth |
| `wiki/entities/Tobi-Lütke.md` | `entity` | 1097 | 2 | definition-style; person-depth |
| `wiki/entities/Tool-Use-Architecture.md` | `entity` | 1519 | 1 | entity-depth |
| `wiki/entities/Ubiquitous-Language.md` | `entity` | 1897 | 0 | OK |
| `wiki/entities/Unmesh-Joshi.md` | `entity` | 1522 | 1 | definition-style |
| `wiki/entities/Verifiability.md` | `entity` | 1254 | 1 | entity-depth |
| `wiki/entities/Vibe-Coding.md` | `entity` | 4339 | 3 | definition-style; entity-structure; readability |
| `wiki/entities/Vocabulary-Building.md` | `entity` | 1339 | 2 | definition-style; entity-depth |
| `wiki/entities/WCAG.md` | `entity` | 1313 | 1 | entity-depth |
| `wiki/entities/Wes-Botman.md` | `entity` | 1091 | 1 | person-depth |
| `wiki/entities/Wisdom-Work.md` | `entity` | 2253 | 0 | OK |
| `wiki/entities/World-Model.md` | `entity` | 1910 | 0 | OK |
| `wiki/entities/YAGNI.md` | `entity` | 2373 | 0 | OK |
| `wiki/entities/Zero-PHI-Policy.md` | `entity` | 2051 | 0 | OK |
| `wiki/entities/人机对齐.md` | `entity` | 1952 | 0 | OK |
| `wiki/entities/朱少民.md` | `entity` | 790 | 1 | person-depth |
| `wiki/entities/渐进式重构.md` | `entity` | 1567 | 1 | entity-depth |
| `wiki/lint-report.md` | `lint-report` | 771 | 0 | OK |
| `wiki/outputs/deploy-obsidian-wiki-with-quartz.md` | `output` | 20435 | 0 | OK |
| `wiki/outputs/fde-ai-enablement-bottleneck.md` | `output` | 1541 | 0 | OK |
| `wiki/outputs/output-to-wiki-feedback-loop.md` | `output` | 2161 | 0 | OK |
| `wiki/outputs/raw-recompile-ledger-2026-05-23.md` | `output` | 12365 | 0 | OK |
| `wiki/outputs/why-llm-wiki-is-knowledge-compilation.md` | `output` | 2392 | 0 | OK |
| `wiki/research-agenda.md` | `research-agenda` | 7481 | 0 | OK |
| `wiki/sources/(14) Jevons Paradox for Knowledge Work.md` | `source-summary` | 2052 | 0 | OK |
| `wiki/sources/20260127-claude-coding-notes.md` | `source-summary` | 1958 | 0 | OK |
| `wiki/sources/20260409-ai-capability-gap-ai-psychosis.md` | `source-summary` | 2143 | 0 | OK |
| `wiki/sources/20260410-anti-patterns.md` | `source-summary` | 1821 | 0 | OK |
| `wiki/sources/20260410-better-code.md` | `source-summary` | 1800 | 0 | OK |
| `wiki/sources/20260410-code-is-cheap.md` | `source-summary` | 2040 | 0 | OK |
| `wiki/sources/20260410-hoard-things-you-know.md` | `source-summary` | 1811 | 0 | OK |
| `wiki/sources/20260413-llm-wiki.md` | `source-summary` | 2047 | 0 | OK |
| `wiki/sources/20260413-why-ai-first-strategy-wrong.md` | `source-summary` | 2508 | 0 | OK |
| `wiki/sources/20260414-cybersecurity-proof-of-work.md` | `source-summary` | 1819 | 0 | OK |
| `wiki/sources/20260414-martin-fowler-fragments.md` | `source-summary` | 2204 | 0 | OK |
| `wiki/sources/20260420-build-first-business-ontology.md` | `source-summary` | 2333 | 0 | OK |
| `wiki/sources/20260420-ontology-enterprise-ai-agent.md` | `source-summary` | 2125 | 0 | OK |
| `wiki/sources/20260420-ontology-meets-agent-case-study.md` | `source-summary` | 2180 | 0 | OK |
| `wiki/sources/20260502-most-companies-arent-ready-for-ai.md` | `source-summary` | 2016 | 0 | OK |
| `wiki/sources/A Day in the Life of a Palantir Forward Deployed Software Engineer.md` | `source-summary` | 2266 | 0 | OK |
| `wiki/sources/AI and the Future of Cybersecurity Why Openness Matters.md` | `source-summary` | 2450 | 0 | OK |
| `wiki/sources/Agent pull requests are everywhere. Here's how to review them..md` | `source-summary` | 2448 | 0 | OK |
| `wiki/sources/Andrej Karpathy: From Vibe Coding to Agentic Engineering.md` | `source-summary` | 2885 | 0 | OK |
| `wiki/sources/Anthropic's Boris Cherny: Why Coding Is Solved, and What Comes Next.md` | `source-summary` | 3081 | 0 | OK |
| `wiki/sources/Building a general-purpose accessibility agent—and what we learned in the process.md` | `source-summary` | 2958 | 0 | OK |
| `wiki/sources/Building an AI Factory at Procter & Gamble - Case - Faculty & Research - Harvard Business School.md` | `source-summary` | 2149 | 0 | OK |
| `wiki/sources/Building an MCP Ecosystem at Pinterest.md` | `source-summary` | 2849 | 0 | OK |
| `wiki/sources/Demis Hassabis: Agents, AGI & The Next Big Scientific Breakthrough.md` | `source-summary` | 2995 | 0 | OK |
| `wiki/sources/Enabling agent-first process redesign.md` | `source-summary` | 2380 | 0 | OK |
| `wiki/sources/Forward Deployed Engineer (FDE) - NYC.md` | `source-summary` | 2455 | 0 | OK |
| `wiki/sources/Forward Deployed Engineer：AI 时代的新宠岗位，到底干什么？.md` | `source-summary` | 2307 | 0 | OK |
| `wiki/sources/Forward deployed engineering at OpenAI.md` | `source-summary` | 2577 | 0 | OK |
| `wiki/sources/From Strategy to Shelf How P&G Is Deploying AI.md` | `source-summary` | 2123 | 0 | OK |
| `wiki/sources/Good Taste the Only Real Moat Left.md` | `source-summary` | 2009 | 0 | OK |
| `wiki/sources/How Anthropic’s product team moves faster than anyone else - Cat Wu (Head of Product, Claude Code).md` | `source-summary` | 3312 | 0 | OK |
| `wiki/sources/How I run multiple USD10K MRR companies on a USD20month tech stack.md` | `source-summary` | 2860 | 1 | readability |
| `wiki/sources/How Procter & Gamble Uses AI to Unlock New Insights From Data  Thomas H. Davenport and Randy Bean.md` | `source-summary` | 2671 | 0 | OK |
| `wiki/sources/Improving token efficiency in GitHub Agentic Workflows.md` | `source-summary` | 3557 | 0 | OK |
| `wiki/sources/Inside PG AI Factory and the Push to Operationalize AI at Scale.md` | `source-summary` | 2545 | 0 | OK |
| `wiki/sources/Knowledge Work Is Dying—Here’s What Comes Next.md` | `source-summary` | 2055 | 0 | OK |
| `wiki/sources/Learning on the Shop floor.md` | `source-summary` | 2158 | 0 | OK |
| `wiki/sources/MachinaCheck Building a Multi-Agent CNC Manufacturability System on AMD MI300X.md` | `source-summary` | 2552 | 0 | OK |
| `wiki/sources/Maintainability sensors for coding agents.md` | `source-summary` | 2224 | 0 | OK |
| `wiki/sources/Management as AI superpower.md` | `source-summary` | 1988 | 0 | OK |
| `wiki/sources/Multi-Agent 火了，但 AI 的组织病还没人治｜Hao好聊趋势.md` | `source-summary` | 2534 | 0 | OK |
| `wiki/sources/OncoAgent A Dual-Tier Multi-Agent Framework for Privacy-Preserving Oncology Clinical Decision Support.md` | `source-summary` | 2792 | 0 | OK |
| `wiki/sources/OpenAI launches the OpenAI Deployment Company to help businesses build around intelligence.md` | `source-summary` | 2879 | 0 | OK |
| `wiki/sources/OpenClaw + 6 个 Agent 运转半个月，从聊天到干活的完整工程实践.md` | `source-summary` | 2323 | 0 | OK |
| `wiki/sources/OpenClaw + CodexClaudeCode Agent Swarm The One-Person Dev Team Full Setup.md` | `source-summary` | 2401 | 0 | OK |
| `wiki/sources/Specialization Beats Scale A Strategic Variable Most AI Procurement Decisions Overlook.md` | `source-summary` | 2548 | 0 | OK |
| `wiki/sources/Taste for Makers.md` | `source-summary` | 1852 | 0 | OK |
| `wiki/sources/The Always-On Economy AI and the Next 5-7 Years.md` | `source-summary` | 1971 | 0 | OK |
| `wiki/sources/The Anatomy of an Agent Harness.md` | `source-summary` | 3119 | 0 | OK |
| `wiki/sources/The Conscious 1% Leading a new renaissance in the era of AI.md` | `source-summary` | 2107 | 0 | OK |
| `wiki/sources/The Cybernetic Teammate How AI is Reshaping Collaboration and Expertise in the Workplace.md` | `source-summary` | 2419 | 0 | OK |
| `wiki/sources/The Knowledge Economy Is Over. Welcome to the Allocation Economy..md` | `source-summary` | 2027 | 0 | OK |
| `wiki/sources/The PR you would have opened yourself.md` | `source-summary` | 2320 | 0 | OK |
| `wiki/sources/The Return of the Deployment Company.md` | `source-summary` | 2915 | 0 | OK |
| `wiki/sources/The layoffs will continue till we learn to use AI.md` | `source-summary` | 2155 | 0 | OK |
| `wiki/sources/The next biggest moat in AI.md` | `source-summary` | 1947 | 0 | OK |
| `wiki/sources/The-Founders-Playbook-05062026_v3.md` | `source-summary` | 2001 | 0 | OK |
| `wiki/sources/Using Git with coding agents - Agentic Engineering Patterns.md` | `source-summary` | 2227 | 0 | OK |
| `wiki/sources/Validating agentic behavior when “correct” isn’t deterministic.md` | `source-summary` | 1925 | 0 | OK |
| `wiki/sources/What Is Code?.md` | `source-summary` | 2065 | 0 | OK |
| `wiki/sources/What is agentic engineering? - Agentic Engineering Patterns.md` | `source-summary` | 2474 | 0 | OK |
| `wiki/sources/Why I Don’t Vibe Code.md` | `source-summary` | 2170 | 0 | OK |
| `wiki/sources/building-effective-agents-complete.md` | `source-summary` | 2362 | 0 | OK |
| `wiki/sources/一篇文章卖了20万，开源CC+Obsidian打造的LLM Wiki 内容创作3.0系统.md` | `source-summary` | 2033 | 0 | OK |
| `wiki/sources/工程师抗拒被"蒸馏"，企业的Skills从何而来？五大招破局.md` | `source-summary` | 1873 | 0 | OK |
| `wiki/sources/当我们谈论 FDE 时，我们在谈论什么？.md` | `source-summary` | 2025 | 0 | OK |
| `wiki/sources/深度解析LLM Wiki  Obsidian-Wiki  GBrain：Agent时代知识的“自组织”与“自进化”.md` | `source-summary` | 2291 | 0 | OK |
| `wiki/sources/用Agent评测思路管理AI Coding —— 31万行代码AI重构的实践.md` | `source-summary` | 2514 | 0 | OK |
| `wiki/topics/AI-Apprenticeship-and-Lehrwerkstatt.md` | `topic` | 2396 | 1 | topic-depth |
| `wiki/topics/AI-Era-Career-Skills.md` | `topic` | 4012 | 0 | OK |
| `wiki/topics/AI-Era-Economy-Shift.md` | `topic` | 3091 | 0 | OK |
| `wiki/topics/AI-Era-Taste-and-Judgment.md` | `topic` | 3666 | 0 | OK |
| `wiki/topics/AI-Labor-Bottleneck-Shift.md` | `topic` | 2602 | 1 | topic-depth |
| `wiki/topics/AI-Mediated-Organization.md` | `topic` | 5608 | 0 | OK |
| `wiki/topics/AI-Native-Product-Operating-System.md` | `topic` | 3792 | 0 | OK |
| `wiki/topics/Agent-First-Process-Redesign.md` | `topic` | 2235 | 1 | topic-depth |
| `wiki/topics/Agent-Knowledge-Management.md` | `topic` | 4180 | 0 | OK |
| `wiki/topics/Agentic-Engineering-Patterns.md` | `topic` | 5908 | 0 | OK |
| `wiki/topics/Building-Effective-Agents.md` | `topic` | 3721 | 0 | OK |
| `wiki/topics/Claude-Code-Automation.md` | `topic` | 3788 | 0 | OK |
| `wiki/topics/Code-as-Conceptual-Infrastructure.md` | `topic` | 3345 | 0 | OK |
| `wiki/topics/Conscious-Creation-in-AI-Era.md` | `topic` | 1855 | 2 | topic-depth; topic-evidence |
| `wiki/topics/Enterprise-AI-Factory.md` | `topic` | 2730 | 1 | topic-depth |
| `wiki/topics/Enterprise-AI-Model-Sourcing.md` | `topic` | 3093 | 0 | OK |
| `wiki/topics/Enterprise-Ontology-Application.md` | `topic` | 3925 | 0 | OK |
| `wiki/topics/Forward-Deployed-AI-Enablement.md` | `topic` | 3938 | 0 | OK |
| `wiki/topics/Git-with-Coding-Agents.md` | `topic` | 2640 | 2 | topic-depth; topic-evidence |
| `wiki/topics/Karpathy-AI-Thought.md` | `topic` | 7793 | 0 | OK |
| `wiki/topics/Lean-Indie-Engineering.md` | `topic` | 4112 | 1 | topic-evidence |
| `wiki/topics/Multi-Agent-Pathology-and-Governance.md` | `topic` | 3375 | 0 | OK |
| `wiki/topics/OpenClaw-Agent-System.md` | `topic` | 6398 | 0 | OK |
| `wiki/topics/Organization-as-Agent-Harness.md` | `topic` | 4655 | 0 | OK |
| `wiki/topics/Verifiable-Agent-Engineering.md` | `topic` | 6781 | 0 | OK |
| `wiki/topics/Wisdom-Work-Evolution.md` | `topic` | 2638 | 2 | topic-depth; topic-evidence |

## 本文使用的 Wiki 页面

- [[LLM-Wiki]]
- [[Knowledge-Compilation]]
- [[Agent-Knowledge-Management]]
- [[RAG-vs-LLM-Wiki]]
- [[research-agenda]]

## 回填检查

| 新判断 | 支撑依据 | 处理 |
|--------|----------|------|
| 硬性 lint 不能替代质量审计 | 本报告的 `definition`、`entity-depth`、`topic-evidence` 队列 | 保留在 output |
| `entity-depth` 是下一轮最高收益修复方向 | 本报告分类统计 | 放入 research agenda 或后续审计任务 |
| 单源低入链 Entity 应优先合并或补 topic 承载 | `tools/entity-audit.py` 输出 | 保留，后续按队列处理 |
| 当前性事实需要单独联网复核 | 本轮范围限制 | 放入 research agenda |
