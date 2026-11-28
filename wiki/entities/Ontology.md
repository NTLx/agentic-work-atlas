---
type: entity
title: Ontology
aliases:
  - Ontology
  - 本体
  - 本体论
  - Ontology-Augmented Generation
  - OAG
  - 本体增强生成
definition: "把业务概念、关系和规则形式化为机器可读语义层，用来约束 Agent 对企业事实的解释与推理"
created: 2026-04-20
updated: 2026-11-28
tags:
  - Enterprise-AI
evidence_level: high
claim_type: mixed
related_entities:
  - '[[Ontology-Agent]]'
  - '[[Knowledge-Graph]]'
  - '[[Enterprise-Ontology-Application]]'
  - '[[UModel]]'
  - '[[Decision-Centric-Architecture]]'
source_raw:
  - '[[20260420-ontology-enterprise-ai-agent]]'
  - '[[20260420-build-first-business-ontology]]'
  - '[[20260420-ontology-meets-agent-case-study]]'
  - '[[20260613-ontology-for-agent-optimization]]'
  - '[[20260613-ontology-tokenmaxxing]]'
  - '[[20260730-palantir-ontology-connecting-agents-to-decisions]]'
  - '[[20260730-palantir-industry-ai-unified-namespace]]'
  - '[[20260730-palantir-responsible-ai-hallucinations-ontology]]'
  - '[[20260901-databricks-genie-ontology-data-stack]]'
  - '[[20261002-databricks-buy-side-nav-finance]]'
---

# Ontology（本体）

> [!definition] 定义
> 把业务概念、关系和规则形式化为机器可读语义层，用来约束 Agent 对企业事实的解释与推理

## 关键数据点

- **核心定位**：本体不是另一个数据库，而是业务世界的语义地图。它回答"什么是什么、对象之间如何关联、什么条件成立"。
- **组成方式**：描述逻辑常区分 TBox（术语、公理）、ABox（个体断言）与关系公理；OWL ontology 可以包含实例断言，并不等同于 TBox。依据 [W3C OWL 2 Primer](https://www.w3.org/TR/owl-primer/) §2、§4.7：开放世界下缺事实不等于假，不同名称不必表示不同对象。逻辑一致性/蕴含不是数据完整性校验；[SHACL](https://www.w3.org/TR/shacl/#MinCountConstraintComponent) 等可验证指定数据图的形状约束，仍需实际权限、业务时效、事务和外部效果检查。
- **企业价值**：当 ERP、OMS、MES 等系统对同一词使用不同口径时，本体提供共享语义层，降低 Agent 把同词误判为同义的风险。
- **Agent 价值**：[[Ontology-Agent]] 不让 LLM 直接猜业务规则，而是把关键规则判定交给本体工具和推理机，再由 LLM 解释结果、组织行动。
- **与知识图谱的区别**：[[Knowledge-Graph]] 更偏事实集合，本体更偏概念、关系、约束和可推理结构。两者常配合使用，但不能互相替代。
- **与代码的关系**：本体把业务概念从 prompt、流程和 if/else 中抽出来，成为可版本化、可测试、可解释的概念基础设施。
- **Token 效率价值（限定）**：结构查询可减少某些探索成本。[Codebase-Memory](https://arxiv.org/html/2603.27277v1) §4.1 表6、§5.4：31 个仓库、每语言一个仓库、单一 Claude Opus 4.6 后端，图工具约1000 vs 文本探索10000 tokens/题、2.3 vs 4.8 tool calls/题，但质量评分0.83 vs 0.92；第一作者人工评分。静态代码图不等于 OWL 本体，也不能外推到企业完整工作流或实际货币成本。85–99% 为异质历史样本的输入占比，不是普遍规律。
- **运维领域实证**：阿里云 [[UModel]] 在运维场景中实现从"面向数据"到"面向对象"的转变，告警时直接定位实体并沿关系链聚合关联数据，避免多轮元数据查询和字段映射推断的 Token 开销。
- **长期价值判断**：动态私有事实、共享语义与可审计规则是外部知识机制的候选价值；形式可随模型、工具及组织变化。退役“本体不会被模型替代”的必然性及用 Palantir 市值证明单一技术价值的论证。市值受多种商业和市场因素影响，不识别技术因果贡献。
- **决策中心定位**（2026-04 Palantir 官方架构文）：Palantir 把 Ontology 定位为"决策操作系统"而非数据库升级——数据架构只描述数据，Ontology 进一步建模决策（上下文、候选选项、下游影响）与行动（"动词"），并自动记录 end-to-end decision lineage 作为 agentic memory 与 fine-tuning 的燃料。详见 [[Decision-Centric-Architecture]]。⚠️ vendor 立场，机制可验证、定位表述需打折。
- **与 UNS 的层次关系**：Palantir 制造业材料将 UNS 定位为数据层，Ontology 叠加逻辑及动作；属厂商架构选择。跨系统映射、局部命名空间也可承载语义，不要求先统一全公司命名。
- **反幻觉 grounding 层**（2024-07 Palantir Responsible AI #1）：幻觉是 LLM 生成能力的结构性副产品，不可仅靠 retrain 消除，因此需要架构层 grounding。Palantir 把 LLM 经 search-query 间接访问 Ontology（元数据 + data 工具，而非 prompt 塞全表）的模式命名为 **OAG（Ontology-Augmented Generation）**——RAG 的企业领域特化。它与 tool handoff（计算交接给确定性函数）、human-in-the-loop 审核（提案入队不直接落库）构成按幻觉成因分层的三层防御，三层都建在 Ontology 的 data/logic/action 三要素上。⚠️ vendor 立场：机制可验证，演示为虚构案例、无失效率数据；且 grounding 有效性受制于 ABox 事实的新鲜度与建模质量。

## Genie Ontology：从权威语义到推断上下文

Databricks（2026-09）提供了企业数据栈中的一个具体实现：semantic model 负责刻意定义的业务概念、关系和指标，Genie Ontology 在此基础上从 governed tables、queries、dashboards、notebooks 和 Agent assets 推断更广的上下文，并按 authority、relevance 和 permissions 在回答时取用。其核心做法是 **model the head, infer the tail**：关键定义先由人硬化，长尾知识再从受治理资产中学习。

Databricks（2026-10）又以买方资管财务说明了这一语义层的目标场景：基金、策略、份额类别、估值和费用安排的含义会随业务变化；后台 Agent 先摄取托管人文件、对照市场价格并生成初步 NAV，再让财务人员复核，并为数字保留来源线索。该文属于产品介绍，没有提供客户部署数据或独立效果评估；它补充的是厂商所描述的工作流形态，不是已验证的效果证据（[[20261002-databricks-buy-side-nav-finance]]）。

这条路径把 Ontology 的落地条件具体化为六层渐进建设：物理数据基础与 golden records、元数据、语义层、context-rich 资产、治理、持续评估。Metric Views、Pages 和 Domains 让指标、术语、权威资产和业务范围可被 Agent 查询；权限决定可检索上下文，因此同一问题可以因用户授权不同而产生不同答案。

**判断**：Ontology 的可信度不只来自概念模型是否正确，还来自事实、资产权威性、权限和持续评估能否共同维持一致语境。
- **证据**：[[20260901-databricks-genie-ontology-data-stack]]；[[20260730-palantir-responsible-ai-hallucinations-ontology]]
- **边界**：Databricks 的六层路径是厂商实践建议，不是跨企业效果研究；若基础数据、元数据或业务共识错误，Ontology 可能把错误口径更稳定地传播。

## 何时值得使用

本体适合规则明确、概念复用高、解释责任强的企业场景。例如订单是否可发货、商品是否属于特殊处理类别、供应商是否满足准入条件、合规对象是否触发审查等。

这些场景的共同点是：错误不是普通问答质量问题，而会影响真实流程、权限、承诺或责任归属。此时只靠 RAG 或长 prompt 不够，因为文本上下文无法稳定表达约束，也无法保证不同 Agent 使用同一套业务口径。

本体不适合把所有企业数据一次性装进去。交易明细、日志、库存数量和客户互动仍应留在数据库或业务系统中。本体只保留稳定语义和必要映射，运行时按需从系统取事实，注入 ABox，再调用推理。

## 与 Agent 系统的分工

| 层次 | 主要职责 | 典型承载 |
|------|----------|----------|
| 业务概念 | 定义对象类型、关系、约束 | 本体 / TBox |
| 事实数据 | 存储订单、客户、库存、状态 | 数据库 / ABox / 知识图谱 |
| 确定性判断 | 根据规则推导分类和结论 | OWL 推理机 / GraphDB |
| 语言交互 | 理解请求、选择工具、解释结果 | LLM Agent |

这个分工的价值在于把高风险判断从模型内部迁移到可审计组件。LLM 仍然重要，但它负责调度和解释，不负责凭自然语言直觉决定业务规则是否成立。

## 前提与局限性

- **形式化前提**：关键业务概念必须能被说清楚，并能转写成类、属性、关系、约束或规则。
- **组织前提**：领域专家必须参与建模。没有业务共识时，本体只会把错误口径形式化。
- **数据前提**：ABox 事实必须可靠。TBox 再正确，如果事实字段延迟、缺失或含义混乱，推理结果仍会错。
- **工程局限**：推理比普通查询更重，高频实时场景需要缓存、预计算、增量推理或规则下沉。
- **表达局限**：OWL 适合逻辑分类、蕴含及一致性检查；开放世界缺失不自动构成违规。数据校验、时间窗口、审批、权限与动作应由对应执行机制处理，不能用推理结果直接授权。
- **成本边界**：本体把规则维护集中化，但不会让维护消失。它需要版本治理、规则测试、变更评审和生产监控。

## 关联概念

- TBox：本体的概念与规则部分
- ABox：本体的事实数据部分
- RDF：基础数据标准（三元组）
- OWL：高级本体表示语言
- Protégé：本体建模工具
- [[Ontology-Agent]]：基于本体的 AI Agent
- [[Knowledge-Graph]]：事实数据的集合（与本体互补）
- [[Enterprise-Ontology-Application]]：企业级本体进入 AI Agent 的主题页
- [[UModel]]：阿里云基于本体论的 IT 世界统一建模框架
