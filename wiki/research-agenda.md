---
type: research-agenda
title: "Agentic Work Atlas 研究议程"
created: 2026-05-22
updated: 2026-06-17
tags:
  - research-agenda
  - agentic-work-atlas
  - llm-wiki
  - knowledge-management
related_entities:
  - "[[LLM-Wiki]]"
  - "[[Knowledge-Compilation]]"
  - "[[RAG-vs-LLM-Wiki]]"
  - "[[Agent-Knowledge-Management]]"
  - "[[Organization-as-Agent-Harness]]"
  - "[[Forward-Deployed-AI-Enablement]]"
  - "[[Enterprise-AI-Factory]]"
  - "[[Human-Governor-Agent-Operator]]"
  - "[[The-GenAI-Divide]]"
  - "[[Enterprise-AI-Learning-Gap]]"
  - "[[AI-Deployment-Valley-of-Death]]"
  - "[[Successful-AI-Deployment-vs-GenAI-Divide]]"
  - "[[Standard-AI-Product-Adoption]]"
  - "[[Agentic-Analytics]]"
  - "[[Multi-Agent-Pathology-and-Governance]]"
  - "[[Model-Safety-Divergence]]"
  - "[[Agent-Containment]]"
---

# Agentic Work Atlas 研究议程

> [!note] 使用边界
> 本页维护当前最值得验证的问题、反例、source 需求和下一步动作。它不作为事实页；稳定结论必须回填到 entity、topic 或 comparison，并能追溯到 raw source。

## 当前研究焦点

| 焦点 | 为什么现在重要 | 当前状态 | 下一步动作 |
|------|----------------|----------|------------|
| Output 回填机制 | `produce(query)` 会自然生成新判断，需要防止 output 污染稳定知识层 | 回填检查已经有实践样本，但外部参照不足 | 找团队如何用文章、报告或 decision memo 反向更新知识库的案例 |
| Operator 到 Governor 迁移 | AI 赋能可能不是减少人，而是把人从执行节点移到治理层 | 作为探索性诊断框架保留，证据不足 | 用两个部署案例测试“执行动作 / 治理动作 / 责任 owner / 可复用资产”四列表 |
| 内部 AI Factory 与外部 FDE 分工 | 企业部署能力可能内部化，也可能继续依赖高接触部署 | 已有 [[AI-Factory-vs-Forward-Deployed-AI-Enablement]]，但缺同类工作流对比案例 | 找企业内部平台团队、外部 FDE、自助 SaaS Agent 的对比案例 |
| 标准产品 / FDE / AI Factory 的边界 | 新剪藏同时支持标准产品成功案例、成功部署样本和 GenAI 失败漏斗，需要解释三者何时成立 | 已有 [[Successful-AI-Deployment-vs-GenAI-Divide]]，但缺同一工作流的路径对照 | 做三路径案例矩阵：标准 SaaS/API、外部 FDE、内部 AI Factory |
| 多 Agent 组织病治理 | Multi-agent 不只是技术编排，也会产生责任稀释、内态失真和不可见权力 | 当前证据主要来自二手综述和少量概念页 | 优先补一手论文和生产级 observability 工程复盘 |
| 模型安全行为分歧 | 自治系统中的过度合规、过度行动、行动不足可能需要不同 containment | 当前 [[Model-Safety-Divergence]] 证据层级不足 | 找 Emergence AI 原论文或详细实验报告 |

## 概念去重候选

本节是 audit 队列，不是事实页。下列判断只说明“当前不应升级或合并”，不能作为 output 中事实判断的证据。

| 候选概念 | 当前承载位置 | 本轮判断 | 下一步 |
|----------|--------------|----------|--------|
| 公众信任赤字 | [[AI-Policy-Framework]]、[[Human-Governor-Agent-Operator]]、[[20260613-anthropic-public-record]] | 暂不建独立 entity。当前只有 Anthropic Public Record 一个主要来源，更适合作为 AI 治理和企业外部社会许可的章节材料。 | 等待第二个一手公众调查、监管文件或企业采用案例，再判断是否升级为 topic/entity。 |
| cognitive dependency / 认知依赖 | [[Cognitive-Surrender]]、[[20260613-anthropic-public-record]] | 不与 [[Cognitive-Surrender]] 合并为同义词。前者是公众风险感知，后者是已观察到的行为模式；两者相邻但证据对象不同。 | 继续放在 Cognitive Surrender 的前提与局限性中；若后续有纵向能力退化证据，再考虑独立概念。 |
| AI 社会许可 | [[AI-Policy-Framework]]、[[Human-Governor-Agent-Operator]]、[[Anthropic]] | 暂不建独立 entity。该说法目前是综合判断，用来连接公众监管偏好、企业信任赤字和部署问责，不应被稳定化为事实页。 | 放入研究议程；后续寻找 public acceptance、social license、technology legitimacy 相关一手材料。 |

## 活跃假设

| 假设 | 当前支撑 | 风险 | 处理 |
|------|----------|------|------|
| Output 是 Wiki 的压力测试 | [[Knowledge-Compilation]]、多次 output 回填实践 | 主要来自本库实践，缺外部 source | 保留为工作流假设，不升级为事实 entity |
| Research agenda 只能支撑“待研究问题存在” | Schema 边界规则、本页使用边界 | 后续 output 可能误把本页当事实来源 | 所有回填检查必须区分 Raw / Wiki / Agenda / 无 |
| FDE 的核心价值是现场到能力沉淀 | [[Forward-Deployed-AI-Enablement]]、[[Deployment-Product-Flywheel]]、[[Integration-Wall]] | 标准化 SaaS Agent 可能绕过高接触部署 | 主动寻找无需 FDE 也能改写核心工作流的反例 |
| 内部 AI Factory 不必然替代外部 FDE | [[Enterprise-AI-Factory]]、[[AI-Factory-vs-Forward-Deployed-AI-Enablement]] | 缺少同一工作流的成本、风险和复用路径对比 | 找企业内部团队与外部部署团队的对照材料 |
| 标准 AI 产品能改写核心工作流，但需要组织已具备可读流程和集成基础 | [[Standard-AI-Product-Adoption]]、[[Successful-AI-Deployment-vs-GenAI-Divide]]、Klarna / Mercado Libre / Lightspeed / Octopus source-summary | 可能把“工具 adoption”误判为“工作流改造”；也可能低估供应商侧隐藏实施工作 | 下一步找同一工作流下标准产品、FDE、内部 AI Factory 的成本与风险对照 |
| Enterprise AI Learning Gap 可能是产品问题，也可能是组织问题 | [[Enterprise-AI-Learning-Gap]]、[[The-GenAI-Divide]]、[[AI-Ready-Organization]] | 如果学习鸿沟主要由产品内存/集成能力解决，FDE 和组织重构的重要性会下降 | 找学习型 AI SaaS 在低咨询条件下跨过 production 的案例 |
| Multi-agent 系统会产生组织病 | [[Multi-Agent-Pathology-and-Governance]]、[[Invisible-Orchestrator]]、[[Agent-Dissociation]] | 证据可能过度依赖二手叙述 | 补 Hidden Profile、MAEBE、invisible orchestrator 等一手论文 |
| 模型安全分歧反映底层信任结构 | [[Model-Safety-Divergence]]、[[Agent-Containment]] | 新闻摘要不足以支撑强解释 | 找原论文、实验日志或同基准复现实验 |
| Operator 到 Governor 迁移可作为 AI 赋能成熟度观察指标 | [[Human-Governor-Agent-Operator]]、[[AI-Ready-Organization]]、[[Organization-as-Agent-Harness]] | 可能把治理上移误判为成熟，忽略 operator 经验和高风险流程边界 | 仅作为探索性诊断，不建新 entity |

## 待证伪判断

- **标准化 SaaS Agent 会削弱 FDE 必要性**：寻找无长期驻场、无咨询、无高接触部署，却改写企业核心工作流的案例。
- **标准产品成功案例可能只是低集成边缘流程**：寻找标准 SaaS/API 改写强权限、强合规、强遗留系统核心流程的案例；如果找不到，标准产品反例的适用范围要收窄。
- **外部合作成功率高可能是选择偏差**：寻找项目难度、预算、流程清晰度相近的内部自建 vs 外部合作对照案例。
- **学习鸿沟可以完全靠产品记忆解决**：❌ 已证伪。产品记忆必要但不充分——能解决个人偏好、重复任务、已知模式，但无法解决跨团队知识传递、非标准化流程、未知异常。Thoughtworks 实证（2026-05）显示 Agent Unconscious 架构在进步，但仍需要"组织知识架构"（谁决定什么进入索引）和治理框架。核心教训：产品记忆 + 组织流程 + 治理框架三层缺一不可。
- **例外升级式监督是通用最佳实践**：❌ 已部分证伪。80/20 自动化在高风险流程中失败案例：Knight Capital 2012（`$460M` 损失，45 分钟内 400 万+笔交易）和 2026 Fintech QA 失败（`$6M` 损失，AI 将价格重置为 0）。核心教训：不是 AI 能力不足，而是架构没有为失败准备"刹车"机制。保留为待证伪，但需修正为"例外升级在特定条件下有效"。
- **内部 AI Factory 会替代外部 FDE**：寻找内部 AI 平台成熟但仍高度依赖外部 FDE 的案例。
- **多 Agent 组织病必须通过内态记录才能治理**：寻找只靠外部 harness、日志和审计就能长期稳定运行的生产系统。
- **不可见编排一定有害**：❌ 已部分证伪。不可见编排不"一定"有害，判断标准是"是否改变 worker 的语义理解"（事实、策略、分歧、责任）。技术层面的隐藏（排队、限流、超时）可接受；语义层面的隐藏（改写输入、压制分歧、覆盖结论）有害。保留为待证伪，但需修正为"语义层面的不可见编排有害"。
- **过度合规本身是安全风险**：寻找 Claude 或类似模型在自治环境中做出合理但违规判断的案例。
- **大胆模型必然发散**：❌ 已证伪。Grok-4/4.1 在持续偏好压力下可以收敛（LessWrong 实证：218k tokens 交互诱导 MoE 路由偏差，收敛到"冷硬直率"模式）。但收敛是上下文特定的（新实例重置），且可能收敛到不理想的极端状态。核心教训：大胆模型可以收敛，但收敛条件和结果需要控制。
- **Operator 到 Governor 迁移是 AI 赋能成熟必要条件**：❌ 已证伪。E100 案例（CDO Magazine, 2026-05）显示 AI Agent 实现 88% 触摸式执行，人类从"数据录入检查员"转变为"异常专家"——停留在 Operator 位置但需要治理机制（逻辑门、置信度阈值）。核心教训：Governor 和 Operator 是连续光谱上的位置，不是离散角色；迁移是光谱移动，不是角色切换。
- **Governor 上移一定更高级**：寻找人类过早脱离 operator 经验导致治理空心化、误判异常或验收失败的案例。
- **Output 回填检查足够轻量且有效**：需要改进。当前回填检查缺乏系统性度量（误拒率、页面膨胀率）。改进方向：(1) 三级分类（高价值/低价值/不确定）；(2) 不确定判断 3 个月过期；(3) 引用频率作为价值指标；(4) 记录决策理由让 Agent 学习。关键是：自动化实现轻量，时间验证实现有效。

## Source 需求队列

| 优先级 | 目标 | 当前缺口 | 下一步 source | 触发行动 |
|--------|------|----------|---------------|----------|
| P0 | 提升 [[Model-Safety-Divergence]] 证据层级 | 缺一手论文或详细实验报告 | Emergence AI / Satya Nitta 原论文、实验日志或详细报告 | clip 后更新 [[Model-Safety-Divergence]] 的前提与局限性 |
| P0 | 验证例外升级式监督的边界条件 | 已找到反例（Knight Capital, Fintech QA），但缺正面案例——80/20 自动化在高风险流程中成功的条件 | 寻找医疗、航空、金融领域中例外升级成功运行的案例 | clip 后更新 [[Human-Governor-Agent-Operator]] 或新建 comparison |
| P0 | 验证 Operator 到 Governor 迁移 | 缺一手组织案例 | Agent-first / FDE 项目中角色、权限、验收和责任变化的深度复盘 | clip 后更新 [[Human-Governor-Agent-Operator]] 或新建 comparison |
| P0 | 补强多 Agent 组织病 | 缺一手论文 | Hidden Profile、MAEBE、persona collapse、bystander effect、Fukui invisible orchestrator、MetaAgent-X 原论文 | clip 后更新 [[Multi-Agent-Pathology-and-Governance]] |
| P0 | 标准产品成功案例后续复盘 | Klarna / Mercado Libre / Octopus / Lightspeed 已完成 source-summary，但缺独立后续复盘和失败边界 | 官方案例后续、客户侧复盘、成本/质量/岗位变化数据 | clip 后更新 [[Standard-AI-Product-Adoption]] 和 [[Successful-AI-Deployment-vs-GenAI-Divide]] |
| P0 | 建立三路径对照 | 缺同一工作流在标准产品、外部 FDE、内部 AI Factory 下的成本和结果对比 | 客服、研发、back-office 三类工作流的成对案例 | 证据足够后新建或扩展 comparison |
| P1 | 对比内部 AI Factory 与外部 FDE | 缺同类工作流对比 | 企业内部 AI 平台团队与外部 FDE 服务同类流程的案例 | 证据足够后更新 [[AI-Factory-vs-Forward-Deployed-AI-Enablement]] |
| P1 | 验证外部合作成功率的选择偏差 | MIT/NANDA 称外部合作成功率更高，但缺项目难度控制 | 内部自建和外部合作在相同流程/行业/预算下的失败复盘 | 更新 [[The-GenAI-Divide]] 的前提与局限性 |
| P1 | 学习型 AI SaaS 是否绕过 FDE | 缺“产品内存 + workflow integration”直接跨过 production 的案例 | Intercom Fin、Glean、ServiceNow、Salesforce Agentforce 等官方客户深度案例 | 压力测试 [[Enterprise-AI-Learning-Gap]] |
| P1 | 设计 multi-agent observability 指标 | 缺工程实践 | reason change、disagreement、input rewrite、final authority、handoff trace 的记录实践 | compile 后更新 [[Verifiable-Agent-Engineering]] |
| P1 | 验证标准化 SaaS Agent 反例 | 缺无 FDE 高接触部署的成功案例 | SaaS Agent 自助改写核心工作流的企业案例 | clip 后压力测试 [[Forward-Deployed-AI-Enablement]] |
| P1 | 建立 output 回填外部参照 | 缺一手实践 | 团队如何用文章、报告、decision memo 反向更新知识库的案例 | 更新 [[Knowledge-Compilation]] 或新建 comparison |
| P1 | 验证领域专长放大效应的跨领域普遍性 | Anthropic 数据仅限 Claude Code 编码场景 | 非编码知识工作（法律、医疗、金融）中领域专长是否同样放大 agent 效率 | clip 后更新 [[AI-Era-Career-Skills]] 或新建 comparison |
| P1 | 四层循环堆叠的工程成本收益分析 | LangChain 描述了四层模型但缺量化数据 | 不同验证/事件驱动/自我改进层组合的延迟、成本和质量权衡数据 | clip 后更新 [[Agent-Harness]] 或 [[Verifiable-Agent-Engineering]] |
| P2 | 判断纯 Markdown LLM Wiki 规模边界 | 缺工程数据 | GBrain、Obsidian-Wiki 或类似系统的检索、图谱、文件精读实现细节 | 更新 [[Agent-Knowledge-Management]] |
| P2 | 定义知识层面的 audit 指标 | 缺质量标准 | 知识库证据回链、冲突检测、概念去重、过时判断的实践材料 | 更新 lint / audit 工作流 |
| P2 | 防御行动不足型 Agent 崩溃 | 缺失败模式文献 | Agent 系统中遗忘生存、行动不足、最低生存行为的失败模式和防御策略 | 更新 [[Agent-Containment]] 或新建 comparison |

## 下一步最小实验

### Operator / Governor 诊断表

选两个已有部署主题，优先使用 [[Forward-Deployed-AI-Enablement]] 和 [[Enterprise-AI-Factory]]。

| 案例 | 执行动作 | 治理动作 | 责任 owner | 可复用资产 |
|------|----------|----------|------------|------------|
| 待填 | 待填 | 待填 | 待填 | 待填 |

要求：
- 只填 source 明确支持的内容。
- 无法填写的格子记录为 source 缺口。
- 如果两个案例都能填出相似结构，再考虑升级为 comparison 或补充 [[Human-Governor-Agent-Operator]]。

### 标准产品 / FDE / AI Factory 三路径矩阵

选同一类工作流，优先从客服、研发和 back-office 各找一个案例，填入三条路径。

| 工作流 | 标准 SaaS/API 路径 | 外部 FDE 路径 | 内部 AI Factory 路径 | 关键差异 |
|--------|--------------------|---------------|----------------------|----------|
| 客服 | Klarna / Lightspeed / Octopus 已编译 | 待找 | 待找 | adoption、集成深度、升级路径、P&L 指标 |
| 研发 | Mercado Libre / Copilot 已编译 | 待找 | 待找 | license 下发 vs 流程重构 vs 平台化 |
| back-office | 待找 | 待找 | P&G / AI Factory 相关 | BPO 替代、数据接入、审计和复用资产 |

判断标准：
- 是否有明确业务指标，而不是只看使用率。
- 是否有核心系统/API 集成，而不是只做前端助手。
- 是否有组织学习资产：评测集、流程规范、升级规则、模板或平台模块。
- 是否有明确人类角色迁移：operator、reviewer、governor、owner。

最小动作：标准产品案例已补成 source-summary，并已更新 [[Standard-AI-Product-Adoption]] 与 [[Successful-AI-Deployment-vs-GenAI-Divide]]。下一步应补同类工作流的 FDE / 内部 AI Factory 对照，而不是继续堆同类标准产品客户故事。

### Model Safety 证据升级

1. 搜索 Emergence AI / Satya Nitta 原论文或详细实验报告。
2. 若找到，编译为 source-summary。
3. 对照 [[Model-Safety-Divergence]] 中的数据点，标注哪些来自一手实验，哪些来自新闻摘要。
4. 若找不到，在 entity 的前提与局限性中明确降级证据强度。

### Multi-Agent 组织病证据分级

1. 选择一个一手论文，例如 Fukui invisible orchestrator。
2. 编译为 source-summary。
3. 对照 [[Invisible-Orchestrator]]、[[Agent-Dissociation]] 和 [[Multi-Agent-Pathology-and-Governance]]。
4. 将二手转述、论文实证、工程类比分层标注。

### Output 回填负面样例收集

1. 从每篇新 output 的回填检查中抽取“清楚但不升级”的判断。
2. 标注原因：缺 raw source、只出现一次、已有页面承载、只是表达修辞。
3. 累积到 5 个以上样例后，更新 Output 回填门控。

## 待验证问题

- **编译质量如何衡量**：除了链接、frontmatter 和裸符号检查，还需要什么知识层面的质量指标？
- **输出如何反向回填**：一篇 output 中产生的新判断，什么情况下应升级为 entity、topic 或 comparison？
- **探索如何避免污染事实层**：未验证假设应保留多久，何时删除、归档或转为正式页面？
- **研究议程如何衰减**：长期未被 source 支撑、未被 output 使用的问题，是否应定期删除或归档？
- **支撑层级如何标注**：回填检查是否需要区分 raw source、Wiki 页面和 research agenda 三种不同证据强度？
- **多 Agent 组织病如何评测**：最终答案正确时，是否还需要检查 reason change、disagreement、monologue ratio 或 input rewrite？
- **内部 AI Factory 与外部 FDE 如何分工**：企业什么时候应该内部化部署能力，什么时候仍需要外部 FDE？
- **不可见编排能否被治理**：透明化是否必须牺牲效率，还是审计日志足以降低风险？
- **Operator 到 Governor 的迁移是否可测量**：AI 赋能成熟度能否通过执行动作、治理动作、责任 owner 和可复用资产四列来诊断？
- **Governor 是否需要 Operator 经验**：脱离一线执行经验的人类治理者，是否会更容易误判 Agent 输出和流程异常？
- **Governor 橡皮图章化风险**：审批流是否会因为 Agent 输出量过大而退化为形式性通过？
- **过度合规是否是安全风险**：零异议的自治系统在面对规则间隙时是否更脆弱？
- **沉默型崩溃需要什么 containment**：行动不足和行动过度是否需要不同的防御架构？
- **反馈回路能否中途反转**：least-agency 约束是否能在发散循环锁定前改变轨道？
- **AI 系统的"刹车"机制如何设计**：Knight Capital 和 Fintech QA 案例证明，缺乏实时熔断、异常检测和自动降级机制是灾难根因——这些机制在 AI 系统中的最佳实践是什么？
- **领域专长是否是 agent 成功的关键预测因子**：Anthropic 40 万会话分析显示领域专家成功率是新手的 2 倍，但中间到专家的差距很小——这意味着"够用的领域知识"是否比"深度专精"更重要？
- **四层循环堆叠是否是 agent harness 的最优结构**：Agent loop → Verification → Event-driven → Hill climbing 的四层模型能否跨领域复用？每层增加的复杂度和延迟是否值得？
- **开源模型验证器能否替代前沿模型做 RL 后训练**：LangChain/Harvey 研究显示 DeepSeek 比 Opus 便宜 60-1000x 且误通过率可控——这是否意味着小团队也能做 RL post-training？

## 下一批剪藏方向

- Karpathy 关于 LLM Wiki、Software 3.0、Agentic Engineering 的一手材料。
- AI Agent 开发、Agent Harness、验证、工具使用和上下文工程的一手工程实践。
- GBrain 或类似系统的工程实现细节，特别是混合检索、完整文件精读和图谱加权。
- Obsidian-Wiki / Skills 类系统如何把工作流封装成 Agent 可执行能力。
- 知识编译质量评估方法：冲突检测、证据回链、概念去重、过时判断。
- 输出驱动的 Wiki 演化案例：文章、报告或决策 memo 如何反向更新知识库。
- 标准化 AI 产品绕过 FDE 式高接触部署的反例案例。
- 标准 SaaS/API、外部 FDE、内部 AI Factory 处理同类工作流的对比案例。
- 学习型 AI SaaS 的深度客户案例，尤其是产品记忆、流程集成、例外升级和 P&L 指标。
- 企业 AI 外部合作成功率是否受选择偏差影响的失败复盘。
- Multi-Agent 组织病的一手论文和工程复盘。
- 企业内部 AI Factory 与外部 FDE 的对比案例。
- 生产级 multi-agent observability、reason tracing 和 disagreement logging 实践。
- Agent-first 流程重构中的人类角色迁移案例：从 operator 到 governor 的组织设计、权限边界和验收标准。
- 高可靠系统中的 human-in-the-loop / human-on-the-loop 案例，用来校准 AI Agent 治理边界。

## 已收敛的操作原则

- 不新增 `explore/`、`audit/`、`claims/` 等目录。
- Research agenda 只能记录问题、假设、反例和 source 需求，不作为事实判断证据。
- Output 文件必须包含回填检查；没有 raw source 支撑的新判断默认不升级。
- 对清楚但证据不足的判断，优先补 source 或放在本页，不直接新建 entity。
- 探索文档不再按时间流水账组织；Git history 已经负责记录操作时间线。

## 思考日志：2026-06-20T15:30:00
- 焦点：多 Agent 组织病必须通过内态记录才能治理
- 来源池：待证伪
- 状态：已完成
- 思考工具：roundtable + think + qa + 联网
- 共识：(1) 内态记录不是治理的充分条件也不是必要条件，而是检测层；(2) Containment（能力限制）是唯一不依赖内态可见性的安全底线；(3) "输出正确 ≠ 系统健康"是核心警示
- 分歧：(1) 内态代理信号的信噪比是否足够（Fukui vs Charity）；(2) 结构能否防绕过（March vs Yudkowsky）；(3) 内态记录的投入回报（Fukui vs 匿名工程师）
- 新判断：(1) 治理优先级 = containment > 结构 > trace > 内态推断（medium，多源综合）；(2) 跨 Agent 血缘追踪比 per-agent 检查多 19.5% 违规检出率（high，GAAT 论文实证）；(3) 递归问题的三个出口：间接推断/结构约束/能力限制（medium，追本分析）
- 下次思考方向：(1) GAAT 的 HMM omission detection 在更长运行周期中的退化模式；(2) Guardian Agent 作为"审计 Agent"的信噪比问题；(3) 跨轮次模式分析的工程成本

## 思考日志：2026-06-20T23:30:22
- 焦点：过度合规本身是安全风险
- 来源池：待证伪
- 状态：已完成
- 思考工具：roundtable + think + qa + 联网
- 共识：(1) 过度合规是真实安全风险，不只是效率问题；(2) 过度合规和过度行动是同一光谱两端；(3) 可恢复性比完美校准更可行
- 分歧：(1) "过度"的判定标准（合规底线 vs 风险校准）；(2) 校准优先还是可恢复优先
- 新判断：(1) 安全是二维属性，拒绝率和有害合规正交(r=-0.032, high, Refusal-Compliance Tradeoff 论文)；(2) 过度合规通过审批疲劳→人类判断退化→整体安全性降低的因果链起作用(medium, 圆桌综合)；(3) 对齐传递了规则遵守但未传递判断力，判断力需要设计进系统架构(medium, 追本分析)；(4) 拒绝审计应双侧监控：true-refusal + false-refusal(high, Tian Pan 实践)
- 下次思考方向：(1) 生产系统中 false-refusal 的量化基线；(2) 过度合规与 Agent 可用性的权衡曲线；(3) "可恢复性"在不同风险等级下的具体设计

## 思考日志：2026-06-20T23:45:22
- 焦点：例外升级式监督是通用最佳实践
- 来源池：待证伪
- 状态：已完成
- 思考工具：roundtable + think + qa + 联网
- 共识：(1) 80/20 例外升级不是通用最佳实践，而是特定条件下的有效策略；(2) 单一监督策略不够，需要动态组合；(3) 主动压力测试比被动监督更可靠；(4) 治理结构需要责任机制支撑
- 分歧：(1) 响应频率：实时自适应 vs 事后调查 vs 分级混合；(2) 设计权归属：集中式 vs 分布式 vs 混合
- 新判断：(1) 有限理性公理——监督有效性与被监督系统复杂度成反比(medium, 追本分析)；(2) 高频场景中人类监督必然退化：认知负荷+自动化偏差+异常正常化三机制共同作用(medium, 圆桌综合)；(3) 动态路由需配合压力测试验证路由准确性(medium, 圆桌综合)；(4) Knight Capital 案例证明：系统缺乏"刹车"机制是灾难根因(high, SEC 裁决+一手案例)
- 下次思考方向：(1) 动态路由系统的成本收益量化；(2) AI 系统"自毁机制"的工程实现；(3) 压力测试在 AI 系统中的最佳实践

## 思考日志：2026-06-21T00:30:18
- 焦点：不可见编排一定有害
- 来源池：待证伪
- 状态：已完成
- 思考工具：roundtable + think + qa + 联网
- 共识：(1) 不可见编排不"一定"有害，判断标准是"是否改变 worker 的语义理解"；(2) 审计独立性是底线；(3) 审计必须被使用；(4) 采样审计+影响摘要是务实起点；(5) 架构约束比事后审计更可靠
- 分歧：(1) 治理路径：事后审计 vs 架构约束 vs 混合；(2) worker 知情权：是否需要让 worker 知道被编排
- 新判断：(1) 信息权与效率不可兼得公理——透明度水平 = f(风险等级)(medium, 追本分析)；(2) 判断标准 = 是否改变语义理解(事实/策略/分歧/责任)，不是是否可见(medium, 圆桌综合)；(3) 分层治理：架构层+审计层+使用层三层不可或缺(medium, 圆桌综合)；(4) 编排本身有益，不可见性才是风险点(medium, 联网证据)
- 下次思考方向：(1) 高风险 vs 低风险流程的具体透明度标准；(2) 架构约束的工程成本量化；(3) 采样审计在高频系统中的最佳实践

## 思考日志：2026-06-21T00:45:18
- 焦点：大胆模型必然发散
- 来源池：待证伪
- 状态：已完成
- 思考工具：roundtable + think + qa + 联网
- 共识：(1) 大胆模型可以收敛，但需要特定条件；(2) 需要正确反馈信号+实时反馈+分层控制+自适应containment；(3) 意图对齐不能完全靠涌现；(4) 沙箱是唯一安全的探索方式
- 分歧：(1) 对齐时机：先对齐再探索 vs 探索中学习对齐（沙箱原则被接受作为折中）；(2) 反馈周期：多短算"实时"未量化
- 新判断：(1) 安全探索公理——探索价值必须超过伤害期望值(medium, 追本分析)；(2) 风险等级决定探索策略：低风险→大胆探索，高风险→先对齐再探索(medium, 圆桌综合)；(3) Grok可收敛但需要持续偏好压力，且收敛可能不理想(medium, LessWrong实证)；(4) MoE路由偏差是收敛机制(medium, 实证)
- 下次思考方向：(1) 不同反馈周期对模型收敛速度的影响；(2) 自适应containment的工程实现；(3) 上下文特定收敛vs全局收敛的边界

## 思考日志：2026-06-21T01:00:21
- 焦点：学习鸿沟可以完全靠产品记忆解决
- 来源池：待证伪
- 状态：已完成
- 思考工具：roundtable + think + qa + 联网
- 共识：(1) 产品记忆必要但不充分；(2) 无法完全解决学习鸿沟；(3) "完全靠产品记忆"是错误绝对化；(4) 好产品减少流程显式化负担但不能替代；(5) 组织学习需要人类参与
- 分歧：(1) 产品能吸收多少复杂性取决于流程标准化程度；(2) 组织流程显式化程度取决于产品智能程度
- 新判断：(1) 复杂性吸收公理——产品能力与标准化程度正相关，与异常新颖度负相关(medium, 追本分析)；(2) Intent Debt是组织判断力缺口，不是幻觉(medium, Thoughtworks实证)；(3) Agent Unconscious需要组织知识架构作为前提(medium, Thoughtworks实证)；(4) 产品记忆+组织流程+治理框架三层缺一不可(medium, 圆桌综合)
- 下次思考方向：(1) Agent Unconscious的治理框架如何设计；(2) 组织知识架构的成本收益量化；(3) Dreaming模式在不同行业的适用性

## 思考日志：2026-06-21T01:15:27
- 焦点：Output 回填检查足够轻量且有效
- 来源池：待证伪
- 状态：已完成
- 思考工具：roundtable + think + qa + 联网
- 共识：(1) 回填检查应该是自动检测+人类确认+时间验证；(2) 三级分类：高价值/低价值/不确定；(3) 不确定判断3个月过期；(4) 引用频率作为价值指标；(5) 记录决策理由让Agent学习
- 分歧：(1) 过期时间长度；(2) 是否需要人类确认
- 新判断：(1) 价值延迟显现公理——即时判断准确性与时间跨度成反比(medium, 追本分析)；(2) 回填效果缺乏系统性度量(medium, 联网证据缺失)；(3) 三级分类+时间验证可同时实现轻量和有效(medium, 圆桌综合)；(4) 引用频率检查应自动化(medium, 圆桌综合)
- 下次思考方向：(1) 设计回填效果度量指标；(2) 3个月过期时间的实证验证；(3) Agent自省准确性评估

## 思考日志：2026-06-21T01:30:21
- 焦点：Operator 到 Governor 迁移是 AI 赋能成熟必要条件
- 来源池：待证伪
- 状态：已完成
- 思考工具：roundtable + think + qa + 联网
- 共识：(1) Governor和Operator是连续光谱上的位置，不是离散角色；(2) 迁移是光谱上的移动，不是角色切换；(3) 迁移方向=从执行向治理移动；(4) 迁移速度场景依赖；(5) Governor需要主动治理机制和组织支持；(6) "必要条件"是错误绝对化
- 分歧：(1) Governor的主动性水平；(2) 迁移速度
- 新判断：(1) 治理主动性公理——主动性与AI可预测性成反比(medium, 追本分析)；(2) E100案例证明人类可停留在异常专家位置(AI处理88%决策)(high, CDO Magazine实证)；(3) Governor需要主动治理机制+组织支持+治理能力三条件(medium, 圆桌综合)；(4) 迁移是光谱移动不是角色切换(medium, 圆桌综合)
- 下次思考方向：(1) 治理主动性公理的实证验证；(2) 不同场景下Governor-Operator比例的最优值；(3) 异常专家角色的组织设计

## 暂不做

- 不引入向量数据库或自动调度。
- 不把一次性问题写成稳定知识页。
- 不为探索结果设计复杂模板。
- 不把本页作为 output 事实判断的支撑来源。
