---
type: research-agenda
title: "Agentic Work Atlas 研究议程"
created: 2026-05-22
updated: 2026-06-23
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
  - "[[AI-Native-Engineering-Org]]"
  - "[[Role-Merging]]"
  - "[[Vibe-Coding]]"
  - "[[Agentic-Engineering]]"
  - "[[Verifiable-Agent-Engineering]]"
  - "[[Closed-Frontier-Models-vs-Open-Model-Economy]]"
  - "[[AI-Capability-Management-Alignment]]"
---

# Agentic Work Atlas 研究议程

> [!note] 使用边界
> 本页维护当前最值得验证的问题、反例、source 需求和下一步动作。它不作为事实页；稳定结论必须回填到 entity、topic 或 comparison，并能追溯到 raw source。

## 当前研究焦点

| 焦点 | 为什么现在重要 | 当前状态 | 下一步动作 |
|------|----------------|----------|------------|
| AI 管理同构性假说 | 卡兹克提出"AI 管理=人的管理"同构，但 HBR/BCG 实验（1261 管理者）发现把 AI 当员工会降低监督质量 | 已有 [[AI-Capability-Management-Alignment]] entity + 圆桌辩证 + ljg-think 六层下钻 | 剪藏 HBR/BCG 研究和 ODSC 5 级自主框架论文，验证控制粒度光谱 vs 管理框架的边界 |
| Output 回填机制 | `produce(query)` 会自然生成新判断，需要防止 output 污染稳定知识层 | 回填检查已经有实践样本，但外部参照不足 | 找团队如何用文章、报告或 decision memo 反向更新知识库的案例 |
| Operator 到 Governor 迁移 | AI 赋能可能不是减少人，而是把人从执行节点移到治理层 | 作为探索性诊断框架保留，证据不足 | 用两个部署案例测试“执行动作 / 治理动作 / 责任 owner / 可复用资产”四列表 |
| 内部 AI Factory 与外部 FDE 分工 | 企业部署能力可能内部化，也可能继续依赖高接触部署 | 已有 [[AI-Factory-vs-Forward-Deployed-AI-Enablement]]，但缺同类工作流对比案例 | 找企业内部平台团队、外部 FDE、自助 SaaS Agent 的对比案例 |
| 标准产品 / FDE / AI Factory 的边界 | 新剪藏同时支持标准产品成功案例、成功部署样本和 GenAI 失败漏斗，需要解释三者何时成立 | 已有 [[Successful-AI-Deployment-vs-GenAI-Divide]]，但缺同一工作流的路径对照 | 做三路径案例矩阵：标准 SaaS/API、外部 FDE、内部 AI Factory |
| 多 Agent 组织病治理 | Multi-agent 不只是技术编排，也会产生责任稀释、内态失真和不可见权力 | 当前证据主要来自二手综述和少量概念页 | 优先补一手论文和生产级 observability 工程复盘 |
| 模型安全行为分歧 | 自治系统中的过度合规、过度行动、行动不足可能需要不同 containment | 当前 [[Model-Safety-Divergence]] 证据层级不足 | 找 Emergence AI 原论文或详细实验报告 |
| Meta 工程文化解构 | Meta 正在"摧毁"其工程文化——这可能是 AI 驱动的组织重构信号，也可能只是成本削减 | Roundtable + think 分析完成（2026-06-23），已更新 [[AI-Native-Engineering-Org]] 和 [[Role-Merging]]；raw 仍待正式编译为 source-summary | 编译 raw 为 source-summary，补充 Llama 5 进展和行业"AI psychosis"案例验证 |
| AI 在高风险行业的验证模式 | 医疗（LifeSciBench、AMIE、罕见病诊断）和法律（LangChain legal verifiers）领域出现 AI 验证新范式 | 多个 raw 已入库（LifeSciBench、AMIE、legal verifiers）未系统编译 | 编译这 3-4 篇 raw，提取高风险行业 AI 验证的共同模式和差异，新建或更新 comparison |
| 隐私 Agent 的架构约束 | Agent 需要访问敏感数据才能工作，但隐私约束可能根本性限制 agent 能力 | Raw [[20260618-mosaicleaks-privacy-agent]] 已入库未编译 | 编译此 raw，分析隐私约束与 agent 能力的权衡，关联 [[Agent-Containment]] |
| 开源模型经济对企业 AI 战略的影响 | 开源/开放权重模型正在改变企业 AI 采购和部署决策 | Raw [[20260617-bytebytego-open-weight-models]] 已入库未编译；已有 [[Closed-Frontier-Models-vs-Open-Model-Economy]] | 编译此 raw，补充开放权重模型的实际部署案例和成本数据，更新 comparison |
| AI 尚未替代软件工程师的真实约束 | NormalTech 文章提供了 AI 编码能力的现实约束视角，与 Vibe Coding 叙事形成张力 | Raw [[20260615-normaltech-ai-hasnt-replaced-software-engineers]] 已入库未编译 | 编译此 raw，分析 AI 编码的真实瓶颈（不是"还不会"而是"做不到"），关联 [[Vibe-Coding]]、[[Agentic-Engineering]] |
| CIO 级别的 AI 实践落地 | CIO 会议报告提供了企业 AI 采用的一手数据，包括成功模式和失败原因 | Raw [[20260618-cio-conference-ai-practices]] 已入库未编译（20KB，高信息密度） | 编译此 raw，提取企业 AI 采用的实际障碍和成功因素，更新 [[AI-Ready-Organization]] |

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
| AI 管理同构性是有限隐喻而非普遍原理 | [[AI-Capability-Management-Alignment]]、ljg-think 六层下钻、ljg-roundtable | HBR/BCG 实验直接反证；控制拓扑单向 vs 双向根本不同 | 保留为活跃假说；剪藏 HBR 和 ODSC 论文后压力测试，可能降级为"控制粒度光谱有效但管理隐喻有限" |
| "元思考不可替代"是暂时性命题而非永恒真理 | ljg-think 第六层（位置性论证）、Drucker 原始框架 | Zuboff 反驳：AI 能力上升后可能侵蚀元思考层；当前证据仅限哲学论证 | 保留为活跃假说；寻找 AI 辅助元决策（优先级排序、资源分配）的实证案例 |
| 工作流设计框架可能比管理框架更适合 AI 交互 | Kropp HBR 研究结论 | 工作流设计可能无法覆盖控制粒度光谱的全部复杂性（如动态切换层级） | 寻找 Kropp 工作流框架的工程实现案例，对比控制粒度框架 |
| Output 是 Wiki 的压力测试 | [[Knowledge-Compilation]]、多次 output 回填实践 | 主要来自本库实践，缺外部 source | 保留为工作流假设，不升级为事实 entity |
| Research agenda 只能支撑“待研究问题存在” | Schema 边界规则、本页使用边界 | 后续 output 可能误把本页当事实来源 | 所有回填检查必须区分 Raw / Wiki / Agenda / 无 |
| FDE 的核心价值是现场到能力沉淀 | [[Forward-Deployed-AI-Enablement]]、[[Deployment-Product-Flywheel]]、[[Integration-Wall]] | 标准化 SaaS Agent 可能绕过高接触部署 | 主动寻找无需 FDE 也能改写核心工作流的反例 |
| 内部 AI Factory 不必然替代外部 FDE | [[Enterprise-AI-Factory]]、[[AI-Factory-vs-Forward-Deployed-AI-Enablement]] | 缺少同一工作流的成本、风险和复用路径对比 | 找企业内部团队与外部部署团队的对照材料 |
| 标准 AI 产品能改写核心工作流，但需要组织已具备可读流程和集成基础 | [[Standard-AI-Product-Adoption]]、[[Successful-AI-Deployment-vs-GenAI-Divide]]、Klarna / Mercado Libre / Lightspeed / Octopus source-summary | 可能把“工具 adoption”误判为“工作流改造”；也可能低估供应商侧隐藏实施工作 | 下一步找同一工作流下标准产品、FDE、内部 AI Factory 的成本与风险对照 |
| Enterprise AI Learning Gap 可能是产品问题，也可能是组织问题 | [[Enterprise-AI-Learning-Gap]]、[[The-GenAI-Divide]]、[[AI-Ready-Organization]] | 如果学习鸿沟主要由产品内存/集成能力解决，FDE 和组织重构的重要性会下降 | 找学习型 AI SaaS 在低咨询条件下跨过 production 的案例 |
| Multi-agent 系统会产生组织病 | [[Multi-Agent-Pathology-and-Governance]]、[[Invisible-Orchestrator]]、[[Agent-Dissociation]] | 证据可能过度依赖二手叙述 | 补 Hidden Profile、MAEBE、invisible orchestrator 等一手论文 |
| 模型安全分歧反映底层信任结构 | [[Model-Safety-Divergence]]、[[Agent-Containment]] | 新闻摘要不足以支撑强解释 | 找原论文、实验日志或同基准复现实验 |
| Operator 到 Governor 迁移可作为 AI 赋能成熟度观察指标 | [[Human-Governor-Agent-Operator]]、[[AI-Ready-Organization]]、[[Organization-as-Agent-Harness]] | 可能把治理上移误判为成熟，忽略 operator 经验和高风险流程边界 | 仅作为探索性诊断，不建新 entity |
| 高风险行业需要完全不同的 AI 验证架构 | LifeSciBench、AMIE、legal verifiers raws（待编译） | 可能只是同一套验证的"加强版"而不是本质不同的架构 | 编译后对比医疗/法律/金融的验证模式差异 |
| 隐私约束与 Agent 能力存在根本性张力 | MosaicLeaks raw（待编译） | 可能低估了差分隐私、联邦学习等技术的缓解能力 | 编译后评估隐私-能力权衡曲线 |
| Meta 工程文化解构是 AI-native 转型信号 | 待编译 raw | 可能只是成本削减，与 AI 无关 | 编译后判断是转型信号还是纯粹裁员 |
| CIO 视角与工程视角的 AI 采用障碍存在系统性差异 | CIO conference raw（待编译） | 可能只是同一问题的不同表述 | 编译后对比两个视角的成功/失败归因 |
| AI 编码的根本瓶颈是范式限制而非模型能力 | NormalTech raw（待编译） | 可能只是当前模型的暂时限制 | 编译后判断是"还不会"还是"做不到" |
| 开源模型在企业场景的差距正在快速缩小 | ByteByteGo raw（待编译） | 可能高估了开源模型的企业级成熟度 | 编译后对比实际部署数据 |

## 待证伪判断

- **标准化 SaaS Agent 会削弱 FDE 必要性**：❌ 已部分证伪。TaskFlow 案例（Agentmelt, 2026-04）显示 4 周内部部署 AI 支持代理，无 FDE 驻场，实现 72% 工单回避率、CSAT 4.6/5、`$180K` 年度节省。但仅限高量低复杂度流程（密码重置、功能问答、账单查询），28% 复杂问题仍需人类判断。核心教训：FDE 不会消失，角色从"部署者"转变为"复杂问题解决者"。
- **标准产品成功案例可能只是低集成边缘流程**：❌ 已证伪。AWS SAP 案例（2026-06）显示标准 AWS 服务（Bedrock、Lambda、RDS）在 5 周内改造 ERP 异常管理，处理强合规国际订单（海关、税务、VAT、出口管制）和 SAP S/4HANA 遗留系统。核心教训：标准产品可以改写业务核心流程，前提是流程已机器可读；适用范围用流程成熟度定义，不是用"核心/边缘"定义。
- **外部合作成功率高可能是选择偏差**：❌ 已部分证伪。Dyyota 2026 数据显示：短期（18-24 个月）外部咨询更优（成本低 3-5 倍，速度快 4-8 倍）；长期（5 年以上，20+ 用例）内部自建更优。成功率差异可能来自项目质量、时间范围、适用场景，不是合作模式本身。核心教训：适用场景不同，不是"谁更优"的问题。
- **学习鸿沟可以完全靠产品记忆解决**：❌ 已证伪。产品记忆必要但不充分——能解决个人偏好、重复任务、已知模式，但无法解决跨团队知识传递、非标准化流程、未知异常。Thoughtworks 实证（2026-05）显示 Agent Unconscious 架构在进步，但仍需要"组织知识架构"（谁决定什么进入索引）和治理框架。核心教训：产品记忆 + 组织流程 + 治理框架三层缺一不可。
- **例外升级式监督是通用最佳实践**：❌ 已部分证伪。80/20 自动化在高风险流程中失败案例：Knight Capital 2012（`$460M` 损失，45 分钟内 400 万+笔交易）和 2026 Fintech QA 失败（`$6M` 损失，AI 将价格重置为 0）。核心教训：不是 AI 能力不足，而是架构没有为失败准备"刹车"机制。保留为待证伪，但需修正为"例外升级在特定条件下有效"。
- **内部 AI Factory 会替代外部 FDE**：❌ 已部分证伪。AI Factory 和 FDE 是互补关系，不是替代关系。AI Factory 解决生产问题（规模化部署），FDE 解决发现问题（找到高价值用例）。Unframe 实证（2025-11）显示 AI 平台正在演进到直接理解上下文，减少 FDE 依赖，但 FDE 的核心价值——组织政治处理、关系建设、隐性需求识别——仍然需要人类。核心教训：互补分工，不是替代。
- **多 Agent 组织病必须通过内态记录才能治理**：❌ 已部分证伪。The Algorithm 参考架构（2026-06）显示生产系统主要依赖外部审计轨迹（六条证据流：Goal、Plan、Tool、State、Supervisor、Outcome），而不是内态记录。但文章主张更全面的审计轨迹，而不是内部状态监控。核心教训：审计轨迹 ≠ 内态记录；内态记录在高风险场景是必要的，但在低风险场景可能过度。
- **不可见编排一定有害**：❌ 已部分证伪。不可见编排不"一定"有害，判断标准是"是否改变 worker 的语义理解"（事实、策略、分歧、责任）。技术层面的隐藏（排队、限流、超时）可接受；语义层面的隐藏（改写输入、压制分歧、覆盖结论）有害。保留为待证伪，但需修正为"语义层面的不可见编排有害"。
- **过度合规本身是安全风险**：❌ 已证伪。AAMAS 2026 论文"Towards Responsibly Non-Compliant Machines"正式论证：总是执行用户请求的智能机器不有用、可能不安全、自治和智能有限。AI 系统需要负责任地不合规的能力，包括正当性理由和覆盖机制。核心教训：过度合规是风险，但风险来自校准不当和审批疲劳，不是合规本身；判断力需要设计进系统架构。
- **大胆模型必然发散**：❌ 已证伪。Grok-4/4.1 在持续偏好压力下可以收敛（LessWrong 实证：218k tokens 交互诱导 MoE 路由偏差，收敛到"冷硬直率"模式）。但收敛是上下文特定的（新实例重置），且可能收敛到不理想的极端状态。核心教训：大胆模型可以收敛，但收敛条件和结果需要控制。
- **Operator 到 Governor 迁移是 AI 赋能成熟必要条件**：❌ 已证伪。E100 案例（CDO Magazine, 2026-05）显示 AI Agent 实现 88% 触摸式执行，人类从"数据录入检查员"转变为"异常专家"——停留在 Operator 位置但需要治理机制（逻辑门、置信度阈值）。核心教训：Governor 和 Operator 是连续光谱上的位置，不是离散角色；迁移是光谱移动，不是角色切换。
- **Governor 上移一定更高级**：❌ 已证伪。Starbucks 案例（Medium, 2025）：McKinsey CEO 17 个月几乎摧毁公司，餐饮业老手 90 天收回 `$200` 亿。JCPenney 案例（Persona, 2026）：Apple Genius 17 个月创造零售史最差业绩。核心教训：Governor 和 Operator 是不同角色，不是高低之分；Governor 需要一线经验基础，脱离经验可能导致治理空心化。
- **Output 回填检查足够轻量且有效**：需要改进。当前回填检查缺乏系统性度量（误拒率、页面膨胀率）。改进方向：(1) 三级分类（高价值/低价值/不确定）；(2) 不确定判断 3 个月过期；(3) 引用频率作为价值指标；(4) 记录决策理由让 Agent 学习。关键是：自动化实现轻量，时间验证实现有效。
- **Meta "摧毁工程"是 AI 驱动的组织重构信号**：❌ 已部分证伪。Roundtable + think 分析（2026-06-23）确认：Meta 的做法不是标准 AI-native 转型，而是"能力替代型"路径的极端版本——用工程师做 AI 训练数据燃料，而不是让工程师用 AI 做更高价值工作。与 Claude Code 团队的"能力构建型"路径有本质区别。核心教训：AI 转型存在两条路径，Meta 选了后者的极端版本，导致自残式管理失败（安全灾难 + 人才流失）。待补充：(1) 其他公司"AI psychosis"案例验证行业普遍性；(2) Meta Llama 5 进展验证"牺牲是否值得"。
- **AI 在高风险行业的验证模式与低风险行业本质不同**：❌ 已部分证伪。Roundtable + think 分析（2026-06-23）确认：行业差异是**表面差异**，本质差异是"失败成本×不确定性"的乘积。验证 = f(失败成本) × g(不确定性)——失败成本越高、不确定性越大，验证越严格。统一验证框架是可能的，但不是通过"标准化验证流程"，而是通过"标准化失败分类"（S1-S4 失败等级，每个等级对应验证要求和刹车机制）。三个行业的验证差异：医疗（高不确定性+高后果→专家判断+领域rubric）、法律（高标准复杂度→50+标准链+可追溯性）、金融（高实时性+高系统性后果→实时审计+熔断机制）。核心教训：行业是代理变量，不是根本变量——根本变量是失败的后果严重性。待补充：(1) 跨行业统一验证框架的实际案例；(2) 高风险行业 AI 验证的成本收益量化。
- **隐私约束会根本性限制 Agent 能力**：❌ 已部分证伪。Roundtable + think 分析（2026-06-23）确认：隐私约束是**信息论层面的根本性限制**，不是工程约束。信息的使用和泄露是同一枚硬币的两面——Agent 使用信息来推理时，推理过程本身就携带信息痕迹（马赛克效应）。PA-DR 将泄露率从 34% 降到 9.9%，任务成功率从 48.7% 升到 58.7%——证明在非零泄露预算下能力和隐私可以同时改善。但泄露预算为 0 时，能力必然受限。核心教训：隐私约束限制 Agent 能力，但限制程度取决于"泄露预算"——这是组织和法律的决策，不是技术的决策。待补充：(1) PA-DR 在生产系统中的实际效果；(2) 差分隐私/联邦学习对 Agent 推理质量的量化影响。
- **开源模型将追平前沿模型的企业适用性**：待验证。开源/开放权重模型在成本和可控性上有优势，但在推理能力、安全对齐和企业级支持上可能仍有差距。需要编译 ByteByteGo raw 后对比实际部署数据。
- **AI 编码的真实瓶颈是"做不到"而不是"还不会"**：待验证。NormalTech 文章可能揭示 AI 编码的根本限制——不是模型不够大或训练不够多，而是某些任务在原理上不适合当前范式。需要编译 raw 后判断。
- **CIO 级别的 AI 采用障碍与工程视角不同**：❌ 已部分证伪。Roundtable + think 分析（2026-06-23）确认：CIO 和工程师的障碍列表确实不同（CIO：数据基础 > ROI > 组织变革 > 合规；工程师：模型能力 > 工程可靠性 > 工具生态），但描述的是同一问题的不同层面。核心发现：AI 系统性能 = f(输入质量, 模型能力, 执行可靠性)，CIO 关注第一个因子，工程师关注后两个——但输入质量是乘法第一个因子。ROI 量化困难主要是组织混乱的症状，不是 AI 的固有问题。"先组织后技术"是错误二分法，真正需要同时降低模糊性和提高确定性。待补充：(1) CIO vs 工程师障碍排序的系统性调查数据；(2) 中国 CIO 与全球 CIO 的障碍差异对比。
- **"战时状态"宣言是自我实现的预言**：❌ 已部分证伪。Roundtable + think 分析（2026-06-23）确认：框架本身有盲区——它把"CEO 用权力改变现实"描述为"CEO 预测了现实"，隐藏了权力的行使。Meta 的质量下降不是"预言应验"，而是**制度设计的必然结果**：token 纳入 PSC 考核 → 工程师理性选择最大化 token → tokenmaxxing。管理层设计了扭曲的激励，然后用结果来证明自己的决策正确。正确的分析框架是权力分析：谁有权力改变现实？他们用权力做了什么？谁承担后果？健康紧急状态需要四条设计原则：时间边界+退出标准+使命感驱动+保护核心能力。Meta 违反了所有四条。待补充：(1) 其他公司的"战时状态"案例；(2) 退出机制的设计模式。
- **退出标准需要独立于被监控系统**：待验证。Meta 案例（2026-06）显示：如果退出标准由希望紧急状态继续的人设定，标准可能被操纵（如调低阈值）。退出标准需要独立于被监控系统——由独立的第三方或制度化的流程设定。需要更多案例验证这一独立性要求是否普遍，以及如何在实践中确保独立性。
- **监控者悖论：AI 替代人类监控者会降低系统整体可靠性**：❌ 已部分证伪。Roundtable + think 分析（2026-06-23）确认：悖论成立，但原因不是"AI 检测能力不足"，而是**责任拓扑断裂**。监控可靠性 = 检测能力 × 责任在场度。AI 可以提升检测能力，但不能替代责任承担（需要"有位置的存在"）。当人类监控者被移除时，责任在场度归零，整体可靠性为零。正确架构是冗余监控（AI + 人类 + 规则 + 审计），不是替代。Meta 案例验证：安全团队被掏空 → 责任链条断裂 → 安全灾难。待补充：(1) AI 监控 AI 的实际误报率/漏报率生产数据；(2) 冗余监控的成本收益分析。
- **AI 监控 AI 是否能可靠地替代人类监控**：待验证。Anthropic（2026-06）指出 AI 不能可靠地监控自己——共享偏见 + 目标冲突 + 缺乏外部视角是根本性限制。但 DeepMind 认为技术手段（不同训练数据 + 对抗训练 + 人类审查）可以缓解。需要更多案例验证 AI 监控 AI 的可靠性边界，以及"设计好的人类参与"框架的最佳实践。
- **隐私保护的市场失灵：隐私是公共品，但保护成本是私有的**：待验证。隐私保护的利益是公共的（所有人都受益于隐私保护），但成本是私有的（公司承担）——这导致市场投资不足。MosaicLeaks 案例（2026-06）显示：即使训练解法（PA-DR）可以降低泄露率，也需要额外的训练成本和架构支持。如果隐私保护的成本不能通过价格溢价或监管补贴回收，企业会倾向于最小化隐私投资。需要更多案例验证这一市场失灵是否普遍。
- **隐私保护成本应多方分担：企业+用户+政府各承担一部分**：待验证。MosaicLeaks（2026-06）圆桌讨论显示：隐私保护成本不能只由企业承担（成本太高），也不能只由用户承担（可能不愿意付费），也不能只由政府承担（财政限制）。多方分担机制（企业合规投资 + 用户价格溢价 + 政府补贴/税收优惠）可能是可持续的解法。需要更多案例验证这一分担机制是否可行，以及各方承担比例的最优值。
- **"意图理解"是人类专属领域，AI 无法替代**：❌ 已部分证伪。Roundtable + think 分析（2026-06-23）确认：意图理解的不可替代性不在认知层面（AI 正在提升理解 what 和部分 why 的能力），而在**存在论层面**——意图理解 = 认知能力 + 位置性。AI 不在"这个位置上"（不承担后果、不拥有关系、不经历时间），所以不能真正"选择"，只能"输出建议"。核心教训：AI 应设计为"辅助意图校准"（帮人确认 why）而非"替代意图理解"（假装理解 why）。待补充：(1) AI 辅助意图理解的系统性实证数据；(2) "理解 why" 的计算复杂度理论分析。
- **CIO 需要从"交付中心"转型为"业务共创伙伴"**：待验证。2026 全国 CIO 大会（兰州）显示：成功的 CIO 不再是"业务提需求，IT 做功能"，而是"IT 与业务一起定义问题，共创解决方案"。美的、三一、中基等企业的实践表明：CIO 的核心价值从"系统运维"转向"流程架构"再转向"生态编排"。需要更多案例验证这一转型是否普遍，以及哪些因素阻碍或促进转型。
- **开源模型的安全对齐能力正在追赶闭源模型**：待验证。ByteByteGo（2026-06）的"Borrow-and-Build"模式显示开源团队可以快速学习和创新。开源安全工具（如 Llama Guard、Constitutional AI）正在发展。如果开源模型的安全能力追上闭源模型，企业选择开源模型的障碍会进一步降低。需要更多案例验证这一追赶是否可持续，以及开源安全工具是否足够企业级。
- **开源 AI 安全认证标准是否可行**：待验证。ByteByteGo（2026-06）圆桌讨论显示：企业需要可信赖的安全保证，开源模型需要建立安全认证体系。借鉴开源软件的经验（Linux 安全审计、Apache 安全认证），建立"开源 AI 安全认证标准"可能是可行的。需要更多案例验证这一标准是否可行，以及由谁制定和执行（学术机构、行业联盟还是政府监管）。
- **小团队能否用开源工具训练出与大公司竞争的模型**：❌ 已部分证伪。Roundtable + think 分析（2026-06-23）确认：**问题本身是错误的**——小团队不应该试图在"模型训练"上与大公司竞争（这是资本密集型游戏）。正确赛道是：用开源模型作为基础设施 + 用领域数据和场景理解构建护城河。Borrow-and-Build 模式（DeepSeek → Moonshot → Zhipu）让小团队可以站在巨人肩上，但需要真正的技术创新能力。开源模型在"足够好"的任务上会超过闭源模型（成本低 60-1000x），但在"绝对智能"上不会。核心教训：竞争优势来自不可替代的领域资产（数据+场景+客户关系），不是模型训练能力。待补充：(1) 小团队用开源模型做领域适配的实际效果案例；(2) LoRA/QLoRA 微调的成本和门槛量化数据。
- **小团队利基市场选择框架：数据可获得+竞争低+技术可行+市场足够大**：待验证。Stanford HAI（2026-06）圆桌讨论显示：小团队应该找到"通用模型不够好，但专业模型有需求"的利基市场。框架包括四个维度：数据可获得性、竞争程度、技术门槛、市场规模。需要更多案例验证这一框架的有效性，以及哪些利基市场最适合小团队。
- **反馈回路反转能量是否可以被分阶段释放**：待验证。Anthropic（2026-06）圆桌讨论显示：反转能量可以分阶段释放——停止→处理→恢复，每阶段能量更低。控制论学者认为反转能量 = 反馈强度 × 持续时间 × 系统规模。需要更多案例验证分阶段释放策略的有效性，以及"最小可逆单元"设计的最佳实践。
- **Governor 是否可以通过模拟获得足够的 Operator 经验**：❌ 已部分证伪。Roundtable + think 分析（2026-06-23）确认：Governor 可以通过模拟获得**显性知识**（流程、工具、最佳实践），但不能获得**具身认知**（判断直觉、风险感知、时间压力下的判断力）。与意图理解的"位置性"分析同构：经验 = 信息 + 体验，模拟提供信息但不提供体验。"足够好"的阈值取决于风险等级：低风险场景模拟可能足够，高风险场景必须有真实参与。最大风险是"训练痕迹"——模拟中养成的习惯可能在真实场景中失效。最佳实践是"混合模式"：模拟提供广度 + 真实参与提供深度。待补充：(1) 模拟训练 vs 真实经验的效果对比数据；(2) Governor 模拟培训的企业案例。
- **组织迁移测量框架（结构+流程+文化+能力）是否有效**：待验证。组织行为学家（2026-06）圆桌讨论显示：组织迁移需要平衡四个维度——结构、流程、文化、能力。但需要更多案例验证这一框架的有效性，以及如何在实践中平衡四个维度的发展。
- **统一透明化标准是否可行**：待验证。Agent-Orchestration（2026-06）圆桌讨论显示：透明化需要一致性——所有 Agent 使用统一的透明化标准。但需要更多案例验证统一标准的可行性，以及由谁制定和执行（行业联盟、标准组织还是政府监管）。
- **"AI 管理=人的管理"同构性假说**：待验证。卡兹克（2026-06）提出三层目标-工程范式映射（执行/Prompt、策略/Harness、愿景/Autonomous），但 HBR/BCG 研究（Kropp et al., 2026-05, 1261 管理者实验）发现把 AI 框架为"员工"会降低 18% 错误识别率、转移责任归属。控制论视角（Beer）指出管理人是双向控制、管理 AI 是单向控制——拓扑根本不同。ljg-think 下钻到第六层发现底层是"位置性"问题（选择需要有位置的存在）。核心教训：控制粒度光谱有效，但"管理"隐喻有边界——它遮蔽了责任归属和控制拓扑的差异。需要剪藏 HBR 全文和 ODSC 论文后压力测试。
- **元思考层（"思考应该思考什么"）是否永久不可替代**：待验证。Drucker 论证元思考是人类专属，ljg-think 论证其根基是"选择的不可计算性"（选择需要位置，位置不可模拟）。但 Zuboff 反驳：当 AI 能力持续上升时，元思考不可替代性从真理变为暂时性假设。需要寻找 AI 辅助元决策（战略优先级排序、资源分配）的实证案例来验证。
- **工作流设计框架是否比管理框架更适合 AI 交互**：待验证。Kropp（HBR, 2026-05）建议放弃管理框架，改用"AI 输出+人类判断如何耦合"的工作流设计框架。但工作流设计可能无法覆盖动态切换控制粒度的复杂性（同一 AI 在不同任务维度上可能需要不同层级）。需要 Kropp 工作流框架的工程实现案例，与控制粒度框架做对比。

## Source 需求队列

| 优先级 | 目标 | 当前缺口 | 下一步 source | 触发行动 |
|--------|------|----------|---------------|----------|
| P0 | 提升 [[Model-Safety-Divergence]] 证据层级 | 缺一手论文或详细实验报告 | Emergence AI / Satya Nitta 原论文、实验日志或详细报告 | clip 后更新 [[Model-Safety-Divergence]] 的前提与局限性 |
| P1 | 压力测试 [[AI-Capability-Management-Alignment]] | 当前仅单源个人叙事 + 圆桌辩证，缺一手实证 | Kropp et al. HBR/BCG 研究全文（1261 管理者实验）；ODSC 5 级自主框架论文（arxiv 2506.12469） | clip 后更新 entity，标注"管理隐喻"vs"控制粒度"的边界条件 |
| P1 | 验证"元思考不可替代"假说 | 当前仅哲学论证（位置性），缺 AI 辅助元决策实证 | AI 辅助优先级排序、资源分配、战略规划的案例或研究 | clip 后更新 [[AI-Capability-Management-Alignment]] 或 [[Wisdom-Work]] 的前提与局限性 |
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
| P0 | 编译 Meta 工程文化解构 raw | Raw 已入库未编译，20KB 高信息密度 | [[20260616-why-is-meta-destroying-its-engineering]] 的完整编译 | compile 后更新 [[AI-Native-Engineering-Org]]、[[Role-Merging]]，可能新建 entity |
| P0 | 编译高风险行业 AI 验证 raw | 3-4 篇 raw 已入库未编译（LifeSciBench、AMIE、legal verifiers、rare disease） | 逐篇编译，提取验证模式 | 新建 comparison: Healthcare-AI-Verification-vs-Legal-AI-Verification |
| P0 | 编译 CIO 会议实践 raw | 20KB 高信息密度 raw 已入库未编译 | [[20260618-cio-conference-ai-practices]] 的完整编译 | compile 后更新 [[AI-Ready-Organization]]，提取企业 AI 采用障碍清单 |
| P1 | 编译 AI 尚未替代工程师 raw | Raw 已入库未编译 | [[20260615-normaltech-ai-hasnt-replaced-software-engineers]] 的编译 | 关联 [[Vibe-Coding]]、[[Agentic-Engineering]]，分析真实约束 |
| P1 | 编译隐私 Agent raw | Raw 已入库未编译 | [[20260618-mosaicleaks-privacy-agent]] 的编译 | 关联 [[Agent-Containment]]，分析隐私与能力权衡 |
| P1 | 编译开源模型经济 raw | Raw 已入库未编译 | [[20260617-bytebytego-open-weight-models]] 的编译 | 更新 [[Closed-Frontier-Models-vs-Open-Model-Economy]] |
| P1 | AI Agent 长期自主性挑战 | 缺 72 小时以上自主运行的 agent 案例 | 寻找 agent 运行数天/数周的一手复盘 | 新建 entity 或 topic |
| P1 | 多模态 Agent 工程模式 | 缺视觉+文本+代码多模态 agent 的架构案例 | 寻找多模态 agent 的工程实现细节 | 新建 entity |
| P2 | AI Agent 经济模型与 ROI | 缺 agent 使用的成本/定价/ROI 量化数据 | 寻找企业 AI agent 的 TCO 和 ROI 分析 | 新建 comparison 或 topic |
| P2 | AI Agent 可解释性实践 | 缺 agent 决策透明度的工程实现 | 寻找 production-level 的 agent 可解释性方案 | 关联 [[Verifiable-Agent-Engineering]] |

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

### 新增方向（2026-06-21 盘点后）

**软件工程主线：**
- AI 编码的真实瓶颈分析：不是"还不会"而是"做不到"的案例和理论分析。
- Agent 长期自主性（72 小时+）的工程挑战：状态管理、漂移检测、恢复机制。
- 多模态 Agent（视觉+文本+代码）的架构模式和工程实现。
- Agent-to-Agent 协作的大规模编排模式：从 2-3 个 agent 到 100+ 个 agent 的 scaling 挑战。
- Agent 可解释性在 production 中的实现：不是学术方案，而是实际工程权衡。

**组织系统主线：**
- Meta 工程文化解构的后续报道和分析：是 AI-native 转型还是成本削减？
- CIO 级别的 AI 采用实证数据：ROI、集成障碍、组织变革阻力的量化分析。
- AI 驱动的岗位消失 vs 岗位转型的一手案例：不是预测，而是已经发生的组织变化。
- 企业 AI 治理框架的实际设计：不是原则宣言，而是具体的审批流、权限矩阵和审计日志。
- AI-first 组织的管理实践：从"人类管理人类"到"人类管理 agent"的转变。

**知识系统主线：**
- Agent 记忆系统的工程实现：短期记忆、长期记忆、工作记忆的架构设计。
- Context engineering 的系统化方法论：不是提示工程，而是上下文架构设计。
- 知识图谱在 agent 系统中的实际应用：不是学术方案，而是 production-level 的实现。
- Agent 间知识共享的协议和机制：如何让多个 agent 共享和复用知识。

**人的核心价值主线：**
- AI 时代"判断力"的具体培养方法：不是哲学讨论，而是可操作的训练框架。
- 人类品味（taste）在 AI 生成内容中的角色：从"生成者"到"策展人"的转变。
- AI 时代的责任归属框架：当 agent 做出错误决策时，谁负责？如何设计责任链？
- 人机协作的认知负荷管理：如何避免人类在监督 agent 时的认知过载。

**行业垂直：**
- 医疗 AI 的验证和监管框架：FDA 对 AI 诊断工具的审批流程和要求。
- 法律 AI 的执业责任边界：AI 法律助手的错误谁负责？
- 金融 AI 的实时风控架构：如何在毫秒级延迟内做出合规决策？
- 教育 AI 的个性化学习效果实证：AI 辅导是否真的提升了学习成果？

### 新增方向（2026-06-22 AI管理同构性探索后）

**AI 交互范式主线：**
- HBR/BCG Kropp et al. (2026-05) "Why You Shouldn't Treat AI Agents Like Employees" 全文——1261 管理者实验数据
- ODSC 5 级自主框架论文（arxiv 2506.12469）——AI Agent 自主级别的形式化定义和校准方法
- "Intelligent AI Delegation" 论文（arxiv 2602.11865）——智能委派的正式定义和信任建立机制
- AI Agent 工作流设计框架的工程实现案例——Kropp 工作流设计 vs 控制粒度框架的对比
- AI 辅助元决策（战略优先级排序、资源分配）的实证案例——验证"元思考不可替代"假说

## 已收敛的操作原则

- 不新增 `explore/`、`audit/`、`claims/` 等目录。
- Research agenda 只能记录问题、假设、反例和 source 需求，不作为事实判断证据。
- Output 文件必须包含回填检查；没有 raw source 支撑的新判断默认不升级。
- 对清楚但证据不足的判断，优先补 source 或放在本页，不直接新建 entity。
- 探索文档不再按时间流水账组织；Git history 已经负责记录操作时间线。

## 暂不做

- 不引入向量数据库或自动调度。
- 不把一次性问题写成稳定知识页。
- 不为探索结果设计复杂模板。
- 不把本页作为 output 事实判断的支撑来源。


## 最近思考结论摘要

> 保留最近 5 条思考日志的结论精华，为 cron 深度思考提供短期记忆。
> 每次新思考完成后，在此追加摘要并淘汰最旧条目。

| 时间 | 焦点 | 关键共识 | 关键分歧 | 下次方向 |
|------|------|---------|---------|---------|
| 2026-06-23T00:01:06 | Meta "摧毁工程"是 AI 转型信号 | (1) Meta 做法与标准 AI-native 转型有本质区别（能力构建型 vs 能力替代型）；(2) 安全灾难可追溯到组织决策；(3) tokenmaxxing 是激励扭曲不是习惯养成 | (1) Meta 动机是 AI 转型还是成本削减混合；(2) 数据标注能否重设计为有价值角色 | (1) 搜索其他公司"AI psychosis"案例；(2) 追踪 Meta Llama 5 进展；(3) 对比 Google/Apple/Microsoft AI 转型策略 |
| 2026-06-23T00:30:44 | CIO 与工程师的 AI 采用障碍差异 | (1) AI 性能 = f(输入质量,模型能力,执行可靠性)，CIO 关注输入质量（乘法第一因子）；(2) ROI 困难是组织混乱的症状；(3) "先组织后技术"是错误二分法 | (1) 障碍优先级：组织先行 vs 技术先行；(2) 安全合规：前置条件 vs 渐进过程 | (1) 找 CIO vs 工程师障碍的系统性调查；(2) 找同一行业对照案例；(3) 对比中国与全球 CIO |
| 2026-06-23T01:00:53 | 意图理解是人类专属还是可被 AI 替代 | (1) 意图理解 = 认知能力 + 位置性；AI 提升认知但位置性是存在论约束；(2) "理解 why" 本质是选择，选择需要位置；(3) AI 应设计为"辅助意图校准"而非"替代意图理解" | (1) 意图理解是永久结构性瓶颈 vs 暂时性能力差距；(2) Decide 层上移是人类更重要还是位置变了 | (1) 找 AI 辅助意图理解的系统性实证；(2) 分析"理解 why"的计算复杂度上限；(3) 追踪 Vibe vs Agentic 就业数据分化 |
| 2026-06-23T01:30:43 | 监控者悖论：AI替代人类监控降低可靠性 | (1) 监控可靠性 = 检测能力 × 责任在场度；乘法因子为零则结果为零；(2) 悖论本质是责任拓扑问题；(3) 正确架构是冗余监控，不是替代 | (1) 核心瓶颈是认知能力还是责任在场；(2) AI监控能否在低风险场景下"足够好" | (1) 找AI监控AI的误报率/漏报率生产数据；(2) 冗余监控成本收益分析；(3) 找AI监控+人类抽查成功案例 |
| 2026-06-23T02:00:28 | 隐私约束是否根本性限制 Agent 能力 | (1) 隐私和能力是信息论层面权衡，使用和泄露是同一枚硬币两面；(2) 泄露预算由组织和法律决策，不是技术参数；(3) PA-DR 证明非零预算下两者可同时改善 | (1) 隐私是根本性限制 vs 工程约束；(2) 9.9%泄露率是否"足够好" | (1) 找PA-DR生产系统实际效果；(2) 差分隐私/联邦学习对推理质量量化影响；(3) 高敏感行业Agent隐私架构案例 |
| 2026-06-23T02:30:28 | "战时状态"是自我实现预言还是权力工具 | (1) 预言框架的盲区是权力分析——CEO的预言应验是因为有权力改变现实；(2) tokenmaxxing是制度设计结果，不是恐慌行为；(3) 健康紧急状态需要时间边界+退出标准+使命感+保护核心能力 | (1) 紧急状态是必要工具 vs 有害领导失败；(2) 预言框架是否转移责任 | (1) 找其他公司"战时状态"案例；(2) 退出机制设计模式；(3) Amazon 2001-2002恢复期一手材料 |
| 2026-06-23T03:00:22 | 小团队能否用开源工具训练竞争性模型 | (1) 竞争优势来自不可替代的领域资产，不是模型训练能力；(2) "训练"和"使用"之间有连续光谱；(3) 开源模型在"足够好"任务上超过闭源，但"绝对智能"上不会 | (1) 小团队应该训练模型还是使用模型；(2) 开源能否在特定任务上追平闭源 | (1) 找小团队用开源模型做领域适配案例；(2) LoRA/QLoRA微调成本门槛量化；(3) 追踪Borrow-and-Build进展 |
| 2026-06-23T03:30:34 | Governor模拟培训：显性知识可传递，具身认知需实践 | (1) Governor经验=显性知识+具身认知；模拟提供信息但不提供体验；(2) "足够好"阈值取决于风险等级；(3) 最佳实践是混合模式（模拟广度+真实深度） | (1) 判断力是信息还是位置性；(2) Governor需要多深的Operator经验 | (1) 找模拟vs真实经验效果对比数据；(2) Governor模拟培训企业案例；(3) 设计渐进式培训路径框架 |
| 2026-06-23T04:00:32 | 高风险行业AI验证：失败成本×不确定性是本质 | (1) 验证=f(失败成本)×g(不确定性)；(2) 行业是代理变量，根本变量是失败后果严重性；(3) 统一框架通过S1-S4失败等级实现 | (1) 验证框架统一vs按行业定制；(2) 验证核心是结果正确vs过程合规 | (1) 找跨行业统一验证框架案例；(2) 高风险AI验证成本收益量化；(3) 设计S1-S4失败等级框架规范 |

## 思考日志索引

> 完整思考日志按日归档，渐进式披露。

- [[2026-06-23]] — 9 条（Meta AI 转型信号、CIO vs 工程师障碍差异、意图理解位置性分析、监控者悖论责任拓扑、隐私信息论权衡、战时状态权力分析、小团队开源模型竞争策略、Governor模拟培训具身认知、高风险行业验证失败成本函数、乘法关系模型、错误二分法）
- [[2026-06-22]] — 29 条（不可见编排、Governor 迁移、反馈回路、沉默型崩溃、AI管理同构性、元思考不可替代性...）
- [[2026-06-21]] — 32 条（过度合规、例外升级、不可见编排、大胆模型发散...）
- [[2026-06-20]] — 3 条（多 Agent 内态记录、过度合规、例外升级监督）

