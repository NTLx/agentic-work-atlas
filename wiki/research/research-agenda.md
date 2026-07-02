---
type: research-agenda
title: "Agentic Work Atlas 研究议程"
created: 2026-05-22
updated: 2026-07-02
tags:
  - agentic-work-atlas
  - llm-wiki
  - knowledge-management
related_entities:
  - "[[LLM-Wiki]]"
  - "[[Agentic-Engineering]]"
  - "[[Agent-Harness]]"
  - "[[Human-Governor-Agent-Operator]]"
  - "[[Judgment]]"
---

# Agentic Work Atlas 研究议程

> [!note] 使用边界
> 本页只保留当前最值得推进的方向、待证伪判断、source 需求和最小动作。已收敛判断见 [[resolved-judgments]]（含 Jevons 修正定理 + Agent Logic 五阶段——07-02 升级为 extracted）。已收敛操作原则见 [[resolved-principles]]。方向库与长问题库见 [[exploration-archive-20260628]]。

## 图谱健康度（2026-07-02 深度盘点）

| 指标 | 当前值 | 上次(06-30) | 趋势 | 动作 |
|------|--------|------------|------|------|
| Entity 总数 | 301 | 299 | +2 | — |
| Topic 总数 | 31 | 31 | 0 | **建 8-10 topic**（四簇+新缺口） |
| Comparison 总数 | 19 | 19 | 0 | **14/19 缺 evidence_level**（实测修正） |
| Output 总数 | 5 | 5 | 0 | **已 31 天无新 output** |
| Entity:Topic 比 | 9.7:1 | 9.6:1 | 恶化 | 中层断层加剧 |
| Entity 缺 evidence_level | 33 (11%) | 33 | 持平 | 批量补标注 |
| Comparison 缺 evidence_level | 14 (74%) | 13 | +1 | 批量补标注 |
| Navigation | 无 wiki/index.md | 无 | — | **建 wiki/index.md** |
| Pending raw | 17 | 14 | ↑ | 10 新剪藏（07-02）+ 7 历史遗留 |
| Output 转化率 | 5/67+ 思考 ≈ 7% | 7% | 持平 | **目标 ≥20%** |
| 研究日志被 output 消费率 | ~3% | ~3% | 持平 | 严重断层 |
| 归档页显式引用率 | 0% | 0% | — | resolved-judgments/principles 是孤岛 |
| Entity 完全孤儿（0 入链） | 14 (4.7%) | 未测 | — | LLM-as-a-Judge/Tokenpocalypse 等高价值节点未联网 |
| Entity 低连接（≤2 入链） | 95 (31.6%) | 未测 | — | 近 1/3 entity 处于半孤立 |

> **新发现（07-02 深度盘点）**：AGI Economics 14 entity 成簇 0% topic 承载；Memory Systems 9 entity 0% 承载（含 Memory-Architecture/Dreaming/Staleness）；Security & Privacy 14 entity 成簇 0% topic 承载；Agent Observability 4 entity 待建 topic。完全缺失领域：Prompt Engineering / RAG 架构深度 / Multimodal AI / AI Legal & Compliance / Agent Sandboxing。Output 最新距今 >31 天，49 条新判断零消费。

## 当前研究焦点

| 焦点 | 为什么重要 | 当前状态 | 下一步 |
|------|-----------|---------|--------|
| **图谱整合与 topic 建设** | 301 entity / 31 topic = 9.7:1，中层断层是最大结构性风险 | 26 轮深度思考产出 49 条新判断但未建 topic 承载 | 建 8-10 topic skeleton；优先五簇：AGI-Economics(14)/Memory-Systems(5)/Agent-Observability(4)/Orchestration(8)/Cognition-Relations(6) |
| **Output 断层修复** | 5 output 无法验证 49 新判断；已 31 天无新产出；输出是判断质量的唯一压力测试 | 07-01/02 日志有丰富原料 | 转 ≥2 output：1) Agent Observability 产业分析；2) 26 轮元合成 rank 文章 |
| **Token FinOps 与 AI 计量** | 企业 AI 采用的隐性瓶颈——不知道花了多少、花在哪、产出什么 | ✅ raw 已到齐（3 篇：FinOps X 2026 + Virtasant + Tokenpocalypse） | compile → 建 [[Token-FinOps]] entity + topic |
| **AI-native 测试与验证方法论** | 评测治理四部曲完成后，下一层是"怎么测"的工程实践 | ✅ raw 已到齐（2 篇：Evaluation Pipeline + LLM-as-Judge Healthcare） | compile → 建 [[AI-Native-Testing]] topic |
| **跨境 AI 治理差异** | EU AI Act vs US vs 中国——不同治理框架对 Agent 部署的实质影响 | ✅ raw 已到齐（2 篇：EU AI Act + Jobs Transition Framework） | compile → 建 [[AI-Governance-Regimes]] comparison |
| **Agent 经济协议与互操作** | 多 Agent 编排的上限不仅是协调技术——还有 Agent 间"交易"的经济协议和互操作标准 | ✅ raw 已到齐（2 篇：Protocol Ecosystem Map + LangGraph/CrewAI/AutoGen 对比） | compile → 建 [[Agent-Economic-Protocols]] entity + [[Open-Source-Agent-Ecosystem]] comparison |
| **AGI 经济学：从 Token 到结构转型** | 14 entity 成簇但零 topic 承载——Demand-Collapse/Allocation-Economy/Messy-Middle/Tokenpocalypse 等孤立节点需统一框架 | 零承载，但有 26 轮思考中的 AGI 经济学三场景分析 | 建 [[AGI-Economics]] topic；将 14 entity 归入统一经济学框架 |
| **记忆系统统一理论** | Dreaming/Staleness/Memory-Synthesis/Context-Rot 等 5 entity 分散——需统一"Agent 记忆生命周期"框架 | 记忆双重衰减定理已立题；Context 扩展悖论已识别 | 建 [[Agent-Memory-Lifecycle]] topic；对标人脑记忆模型（编码/巩固/检索/遗忘） |

### 从盘点新涌现的方向

| 焦点 | 为什么新 | 当前状态 | 下一步 |
|------|---------|---------|--------|
| **Agent Observability 作为独立品类** | 4 entity 成簇（Agent-Legibility/Agent-PR-Review 等）——可观测性可能成为 Agent 时代的"APM 市场" | 零散 entity，无 topic | 建 [[Agent-Observability]] topic；对标 Datadog/New Relic 演化路径 |
| **Compliance-as-Code for AI** | EU AI Act 合规要求自动化→合规即代码可能成为 Agent 治理的基础设施层 | EU AI Act raw 已到齐 | 探索"合规即代码"模式——政策→可执行规则→自动审计 |
| **AI 认知关系模式的形式化** | Exit-Sovereignty 元模式已识别，五种关系模式已描述——但缺乏形式化模型和测量工具 | 概念阶段，无 entity | 建 [[AI-Cognition-Relations]] topic；设计五模式测量量表 |
| **开源 Agent 框架的收敛/分化** | LangGraph/CrewAI/AutoGen 正在分化——谁会赢？收敛到协议层还是产品层？ | raw 已到齐 | compile → comparison；追踪框架市场份额变化 |
| **AI Security & Privacy 簇** | 14 entity 成簇（Agent-Containment/Prompt-Injection/Zero-PHI/MosaicLeaks/N-Hour 等）但零 topic 承载——安全是 Agent 部署的硬约束 | 零承载，entity 散落 | 建 [[AI-Security-Privacy]] topic；区分 Safety（对齐）vs Security（攻击面）两条线 |
| **知识库覆盖盲区** | 完全缺失的领域：Prompt Engineering / RAG 架构深度 / Multimodal AI / AI Fine-tuning / AI Hardware / AI Legal & Compliance / AI Sustainability / Agent Sandboxing | 零 entity 覆盖 | 按优先级补 source：Prompt Engineering(基础)→Agent Sandboxing(安全)→AI Legal(治理) |

## 活跃假设

| 假设 | 验证方向 |
|------|---------|
| Agent Control Plane 壁垒转移定理：竞争壁垒从模型→运行时治理。独立窗口 = f(多模型采用 × 监管) | 追踪独立厂商融资；测量多模型采用率 |
| 治理不可委托定理：因果责任可委托，道德责任不可委托。锚点价值 = 可问责性 ≠ 更好的判断 | 找模型被接受"最终负责"的法律案例 |
| 认知分工终态定理：发散 = 1 人 + AI，收敛 = 多独立视角（防共同锚点） | 对照实验：共享 AI vs 不同 AI vs 无 AI |
| AI 认知关系五模式：情境工具箱，Exit-Sovereignty = 元模式 | 测量五模式在不同职业中的分布 |
| 全球南方 AI 跃迁双速定理：AI 可跳过技术层，不可跳过制度层 | 找同时加速个体 + 组织的成功案例 |
| 中国 AI 双速瓶颈：高政策推动 × 低组织准备度。瓶颈 = 科层碎片 + FinOps 缺失 | 找 Token FinOps 实际建立案例 |
| 判断力维护 = 扰动优先于校准：校准边际收益随经验递减(Gawande)，扰动边际收益递增(Langer)。六可操作机制(AI timeout/第二意见/工具轮换/条件性回顾/强制休息/AI审计标准)。组织内强制不够→需外部+市场约束 | synthesized（修正：18:00 roundtable 2轮） | 测量六种机制在不同AI团队的实施效果 |
| 后果真实性不可消除定理（精确化）：模拟可逼近参数更新(知识)，不可逼近结构更新(存在)。硬边界=时间不可逆→后验成新先验→不可回退。躯体标记=身体对不可逆性的信号。AI代你承担后果=AI代你消除成长 | synthesized（修正：18:30 roundtable 2轮，Friston接受修正） | 找到"模拟中的不可逆性"成功案例——如公开承诺/赌注机制 |
| Headless Agent 范式三条件：结构化 I/O × 不可变 artifact × Simple 单一职责 | 找满足三条件的实现 |
| **🆕 AGI 经济学四阶段周期**：Token 通胀 → Token 治理 → 结构转型 → 新均衡。当前处于 Token 治理阶段，Tokenpocalypse 是阶段转换信号 | 追踪 Token 成本曲线与企业采购行为变化的时滞 |
| **🆕 Agent 记忆统一框架假设**：编码/巩固/检索/遗忘四阶段可映射到 Agent 记忆系统。Context-Rot = 检索干扰 > 存储衰退 | 测量不同记忆架构在四阶段的衰减曲线 |
| **🆕 合规即代码定理**：AI 治理法规的实质效力取决于其可自动化程度。不可自动化的法规 = 选择性执行 | 追踪 EU AI Act 各条款的自动化执行率 |

## 待证伪判断（精选 10 条最高优先级）

| 判断 | 证据强度 | 证伪路径 |
|------|---------|---------|
| 代理-现实差距是一切失真/博弈/退化/漂移的根源。Goodhart/Reward Hacking/记忆污染/变量定义权均可由此单一生成器反推 | extracted（26 轮降秩元合成） | 找到一个"度量完美代表现实、零差距、不可博弈"的 AI 评测系统 |
| 时间不对称（后果不可预体验）决定了判断力/责任/记忆恢复不可被模拟或加速替代 | extracted（26 轮降秩元合成） | 找到模拟训练在后果真实性敏感任务中达到与真实遭遇同等效果的对照实验 |
| 可博弈性结构必然：Goodhart + Soros 反射性 + Gödel 投影 → 不存在不可博弈的"静态/自我验证"显式仲裁标准。有效评测=制度化纠错过程=速度×独立性×成本不对称 | synthesized（修正：16:00 roundtable 4轮，攻击范围从"所有标准"缩小为"静态自我验证标准"） | 找到无需制度约束力（独立实体+强制报告+惩罚权）而长期有效的纯技术 benchmark |
| **🆕 Gödel 不完备递归六层定理**：博弈从规则→惩罚→独立→道德→信任→共享脆弱性逐层上升，每层受限于不完备性。递归终点=共享脆弱性（博弈者⊂被博弈者→博弈成本=∞） | synthesized（Gödel+Goodhart+Soros+Karnofsky+追本6层） | 找到博弈在某制度层终止且无需共享脆弱性的案例 |
| **🆕 AI评测制度化已启动**：US AI Incident Reporting Act (2026-06-26)=强制7天报告+`$2M`/天罚款；EU AI Act=国家主管机构；NY oversight office=72h报告 | extracted（CIO.com 2026-06-26 + EU AI Act + White & Case tracker） | 追踪首次执法行动的时间、力度和效果 |
| 治理内生性六变量定理：可内生 ≠ 增量×低专用×模式一致。修正为 f(验证独立性, 退出自由度, 受益对称性, 参与通道, 知识接口化) - 不可内化底线。高专用→内生知识+外生监督（方向修正）。多中心前提=共享脆弱性 | synthesized（修正：17:30 roundtable 3轮，六变量替代三变量+专用性方向修正+不可内化底线显式化） | 找到满足六变量全部正向且多中心有效的AI治理案例 |
| 记忆双重衰减修正：检索干扰 > 存储衰退。Context 扩展悖论：更大 context → 更差检索 | synthesized | 测量 context 200K→2M 对检索准确率的影响 |
| Reward Hacking 首要性 + 检测递归：锚定真实世界自认证指标（issue 解决率/PR 合并率）是唯一解 | synthesized | 找到成功锚定真实世界指标替代 benchmark 的实践 |
| 评测治理三要素缺一不可：制度 × 技术 × 锚定 | synthesized | 找到缺任一要素但仍有效治理的 AI 评测体系 |
| 多 Agent 编排倒 U 型：层级峰顶 ≈5-15。Team of Teams 可推高。瓶颈 = orchestrator context 带宽 | synthesized | 找到层级编排下 15+ Agent 仍无性能退化的案例 |
| 重组双向制度阶段加权：保护^α × 演化^(1-α)，α = f(AI 替代速度, 技术方向, 劳动力群体, 技术周期)。单α不可维持——裂解为多α后，公式价值≠参数计算=结构知识+叙事工具（暴露地板与天花板缺失） | synthesized（修正：16:31 roundtable 4轮，裂解为多α+重新定位为叙事/结构工具） | 找到成功将"移动α"叙事引入实际政策辩论并影响制度设计的案例 |
| **🆕 Agent 互操作协议收敛假说**：MCP/A2A/ACP/UCP 将在 2 年内收敛到 2 层架构——Transport（1 个胜者）+ Semantic（多协议共存） | hypothesis | 追踪协议采用率变化；找单一协议同时赢得 Transport 和 Semantic 的案例 |
| Token FinOps 品类窗口定理（精确化）：独立窗口=归因层(语义级成本归因)。窗口长度=f(多模型采用率65%↑×模型厂商内化速度×API开放度)。终局=被可观测性平台收购非独立上市。中国窗口延后2-3年(考核体系先决)。三层分解：可见性=feature，归因=独立品类，优化=已关闭 | hypothesis（修正：19:00 roundtable 3轮，三层分解+终局修正+区域差异+多模型实证） | 追踪推理链API开放度和可观测性平台收购动作 |
| **🆕 Context Advantage 解释力边界定理**：Context advantage 在可类型化任务中有效；在独一性任务（位格→关系→意义）中漏失——"谁在做"对行为意义有构成性影响，非信息量问题 | synthesized | 测量独一性任务中 AI 输出质量=人类但位格替换后关系意义改变的实证案例 |
| **🆕 Context 工具使用衰减定律**：Agent 工具使用准确率随 context 长度呈对数-线性衰减 acc(n)=a-b×log₂(n)，~67K token 后跌破 0.80。更大 context → 更多混淆 | extracted | 在 >128K context 场景中找到工具使用准确率不降反升的反例 |
| **🆕 认知背离双循环**：AI context 窗口 3,906× (2017→2026) vs 人类持续注意力下降——形成"越依赖AI→注意力越退化"的委托反馈循环 | extracted | 找到长期高频使用 AI 但注意力未退化的对照群体

## Source 需求队列

| 优先级 | 目标 | 当前缺口 | 下一步 source | 触发行动 |
|--------|------|----------|---------------|----------|
| P0 | AGI Economics topic | 14 entity 零承载 | 经济学框架性论文（Autor/Acemoglu 最新） | 建 topic skeleton + clip |
| P0 | Output 断层 | 5 output 无法验证 49 新判断 | 07-01/02 日志原料充足 | 写 2 个 output |
| P0 | Token FinOps entity + topic | 3 raw 待编译 | ✅ raw 已到齐 | compile → 建 entity |
| P1 | AI-Native Testing topic | 2 raw 待编译 | ✅ raw 已到齐 | compile → 建 topic |
| P1 | AI Governance Regimes comparison | 2 raw 待编译 | ✅ raw 已到齐 | compile → 建 comparison |
| P1 | Agent Economic Protocols entity | 2 raw 待编译 | ✅ raw 已到齐 | compile → 建 entity + comparison |
| P1 | Agent Memory Lifecycle topic | 5 entity 零承载 | 认知心理学记忆模型文献 | 建 topic skeleton |
| P1 | Agent Observability topic | 4 entity 零承载 | Datadog/New Relic APM 演化史对标 | 建 topic skeleton |
| P2 | 长期自主 Agent 权利/责任 | 缺法律/伦理 topic | long-running postmortem 判例 | 追踪法律案例 |
| P2 | Compliance-as-Code for AI | 概念阶段 | EU AI Act 合规自动化工具/案例 | clip + 建 entity |
| P2 | 编译 17 pending raw | 编译速度远落后于剪藏 | 已有 raw | 批量 compile |

## 高杠杆待验证问题

> 以下问题来自 26 轮深度思考中未穷尽的分歧 + 07-02 全库盘点发现的新缺口。

### 从思考未穷尽处

- Token FinOps 能否成为独立的企业软件品类（类似 CloudHealth 之于云成本）？
- Agent Control Plane 独立厂商能否在模型厂商内化之前建立护城河？
- 多模型策略在企业中的实际采用速度——2026/2027 年能否超过 50%？
- 判断力退化的"净退化期"能否被量化——不同判断力类型的时间曲线？
- 模拟训练的"后果真实化"（赌注/公开承诺）能否部分克服大脑的情景/语义分离？
- Exit-Sovereignty 能否被设计为 AI 工具的强制性 affordance（而非可选功能）？
- 中国 AI 采用中"科层碎片化"的结构性根源——是暂时的过渡阶段还是体制性永久特征？

### 从盘点新缺口

- Agent 记忆系统能否统一为"编码→巩固→检索→遗忘"四阶段框架？Context-Rot 对应哪一阶段？
- AGI 经济学的核心生成器是什么——Token 成本、劳动力替代率、还是组织学习速度？
- Agent Observability 能否成为独立的 `$10B+` 市场？它的"Datadog 时刻"何时到来？
- 开源 Agent 框架的竞争终局——收敛到协议标准（类似 HTTP）还是产品整合（类似 IDE）？
- Compliance-as-Code 能否将 AI 治理从"文档合规"升级为"运行时合规"？
- 知识库的 Output 转化率从 7% 提升到 20% 的最小可行动作是什么？

## 最近思考结论摘要

> 只保留最近 5 条；更早见 [[exploration-archive-20260628]]。

| 时间 | 焦点 | 临界发现 |
|------|------|---------|
| 2026-07-02 | Token FinOps 品类窗口定理精确化——三层分解+终局修正 | 归因层=唯一独立品类(18-24月)；可见性=feature、优化=已关闭；终局=被收购非上市；多模型65%→突破阈值；中国延后2-3年 |
| 2026-07-02 | 后果真实性不可消除定理——模拟≠真实遭遇的三层边界 | 技术层可模拟、身体层可部分模拟、存在层不可模拟；硬边界=时间不可逆性；AI代你承担后果=AI代你消除成长机会 |
| 2026-07-02 | 判断力扰动优先定理——六可操作机制+强制来源修正 | 扰动>校准；熟练者最需要扰动；六机制清单(AI timeout/第二意见/工具轮换/条件性回顾/强制休息/AI审计)；组织内强制不够→外部+市场约束 |
| 2026-07-02 | 治理内生性六变量定理——原三重公式裂解与重建 | 专用性方向修正；新公式=f(验证独立性,退出自由度,受益对称性,参与通道,知识接口化)-不可内化底线；多中心=四层嵌套但需共享脆弱性前提 |
| 2026-07-02 | 重组双向制度阶段加权——保护^α×演化^(1-α)裂解 | 单α不可维持；新保护范式=UBI+终身学习+数据权（保护转换能力非工作）；公式价值=结构知识+叙事工具而非参数计算 |
| 2026-07-02 | 可博弈性结构必然——Goodhart+Soros+Gödel 三重论证 | 命题修正：攻击范围=静态自我验证标准≠所有评测。有效评测=制度化纠错（速度×独立性×成本不对称）。AI Incident Reporting Act 2026-06-26=转型已启动 |
| 2026-07-02 | Context Advantage vs Taste——Ng 重命名是进步还是语义替换？ | 双轨制定理（工程轨×审计轨+否决权）；Context 工具衰减定律（更大context→更差判断）；关心的存在论边界（关心=有限生命的不可逆投入，agent不死故无关心结构） |
| 2026-07-02 | 全库深度盘点 | 301 entity/31 topic=9.7:1；14 entity AGI Economics 簇零承载；Output 断层 31 天无新产出；5 个 source 需求 raw 已到齐待编译 |
| 2026-07-02 | 26 轮元合成——AI 重写工作系统的秩 | 四根柱子：代理-现实差距/时间不对称/激励结构/认知边界。能反生成全部 49 判断 |
| 2026-07-02 | 中国企业 AI——科层碎片 + FinOps 缺失 | 瓶颈 ≠ 模型 = 组织。中国"有车没路"vs 印度"有路没车" |

## 思考日志索引

- [[2026-07-02]] — 21 轮含元合成：评测/记忆/灵活性/治理/认知/全球南方/控制平面/AI 认知/Headless/Harness/多 Agent 倒 U/AGI 经济学/中国 AI/元合成 rank/Context Advantage 双轨制/Goodhart Soros Gödel 三重论证/重组制度/治理内生性/判断力扰动/后果真实性/Token FinOps
- [[2026-07-01]] — 12 轮：待验证 5→0；7 条 06-30 判断修正。覆盖协调/记忆/评测/治理/判断力/经济学/组织/Agent/CU/Reward/动态环境
- [[2026-06-30]] — 全库盘点 + 多轮探索
- [[exploration-archive-20260628]] — 06-28 全库快照 + 方向库 + 长问题库
- [[resolved-judgments]] — 已收敛判断（06-24 批次 15 条 + 07-02 批次 2 条：Jevons 修正定理 + Agent Logic 五阶段）
- [[resolved-principles]] — 已收敛操作原则（9 条）
