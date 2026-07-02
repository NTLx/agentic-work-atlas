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
> 本页只保留当前最值得推进的方向、待证伪判断、source 需求和最小动作。已收敛条目见 [[resolved-judgments]] 和 [[exploration-archive-20260628]]。已收敛操作原则见 [[resolved-principles]]。

## 图谱健康度（2026-07-02 盘点）

| 指标 | 当前值 | 上次(06-30) | 趋势 | 动作 |
|------|--------|------------|------|------|
| Entity 总数 | 301 | 299 | +2 | — |
| Topic 总数 | 31 | 31 | 0 | **新建 8-10 topic** |
| Comparison 总数 | 19 | 19 | 0 | 13/19 缺 evidence_level |
| Output 总数 | 5 | 5 | 0 | **从 07-01/02 日志转 ≥2 output** |
| Entity:Topic 比 | 9.7:1 | 9.6:1 | 恶化 | 中层断层加剧 |
| Entity 缺 evidence_level | 33 (11%) | 33 | 持平 | 批量补标注 |
| Comparison 缺 evidence_level | 13 (68%) | 13 | 持平 | 批量补标注 |
| Navigation | 无 index.md | 无 | — | **建 wiki/index.md** |
| Pending raw | 14 (+10) | 4 | ↑ | 编译 Tokenpocalypse/EU/Kunal/SDK + 10 新剪藏（07-02） |
| Low-evidence 阻断 | 1 | 1 | 持平 | AI-Management-Mindset-Transfer 需补 source |

## 当前研究焦点（精简版）

| 焦点 | 为什么重要 | 当前状态 | 下一步 |
|------|-----------|---------|--------|
| **图谱整合与 topic 建设** | 301 entity / 31 topic = 9.7:1，中层断层是知识库最大结构性风险 | 26轮深度思考产出49条新判断但未建 topic 承载 | 建 8-10 topic skeleton；优先四簇：Agent-Observability(4)/AGI-Economics(14)/Cognition-Relations(6)/Orchestration(8) |
| **Output 断层** | 5 output 无法为 49 新判断提供压力测试——无 output 消费的判断会持续失真 | 07-01/02 日志有丰富原料 | 转 2 个 output：1) 25轮元合成 rank 文章；2) Agent Observability 产业分析 |
| **Token FinOps 与 AI 计量** | 企业 AI 采用的隐性瓶颈——不知道花了多少、花在哪、产出什么 | ✅ 新剪藏：FinOps X 2026 + Virtasant token-level visibility | 新建 Token-FinOps entity |
| **AI-native 测试与验证方法论** | 评测治理四部曲完成后，下一层是"怎么测"的工程实践 | ✅ 新剪藏：AI Agent Evaluation Pipeline 2026 Methodology | 新建 AI-Native-Testing topic |
| **跨境 AI 治理差异** | EU AI Act vs US vs 中国——不同治理框架对 Agent 部署的实质影响 | ✅ 新剪藏：EU AI Act Compliance for Autonomous Agents 2026 | 新建 AI-Governance-Regimes comparison |
| **Agent-to-Agent 经济协议** | 多 Agent 编排的上限不仅是协调技术——还有 Agent 间"交易"的经济协议 | ✅ 新剪藏：Agent Protocol Ecosystem Map (MCP/A2A/ACP/UCP) | 新建 Agent-Economic-Protocols entity |
| **开源 Agent 生态演化** | 开源模型追赶闭源→Agent 框架（LangGraph/CrewAI/AutoGen）成为新战场 | ✅ 新剪藏：LangGraph vs CrewAI vs AutoGen 2026 对比 | 新建 Open-Source-Agent-Ecosystem comparison |
| **长期自主 Agent 的权利/责任框架** | 72h+ 自主 Agent 产生不可逆后果后——谁负责？Agent 有"权利"吗？ | 治理不可委托定理已立题；缺法律/伦理延伸 | 建 Agent-Rights-Responsibilities topic；追踪 long-running postmortem 判例 |

## 活跃假设

| 假设 | 验证方向 |
|------|---------|
| Agent Control Plane 壁垒转移定理：竞争壁垒从模型→运行时治理。独立窗口=f(多模型采用×监管) | 追踪独立厂商融资；测量多模型采用率 |
| 治理不可委托定理：因果责任可委托，道德责任不可委托。锚点价值=可问责性≠更好的判断 | 找模型被接受"最终负责"的法律案例 |
| 认知分工终态定理：发散=1人+AI，收敛=多独立视角（防共同锚点） | 对照实验：共享AI vs 不同AI vs 无AI |
| AI认知关系五模式：情境工具箱，Exit-Sovereignty=元模式 | 测量五模式在不同职业中的分布 |
| 全球南方AI跃迁双速定理：AI可跳过技术层，不可跳过制度层 | 找同时加速个体+组织的成功案例 |
| 中国AI双速瓶颈：高政策推动×低组织准备度。瓶颈=科层碎片+FinOps缺失 | 找Token FinOps实际建立案例 |
| 判断力维护=扰动优先于校准：扰动必须组织强制 | 测量不同扰动频率的效果 |
| 后果真实性不可消除：模拟≠真实遭遇，时间不可逆性是硬边界 | 模拟训练 vs 真实遭遇效果比率量化 |
| Agent Logic生命周期五阶段（修正）：初始化→探索→固化→Artifact→维护→退役。维护阶段已从理论空白→Anthropic完整工程实现。Stage 0=环境脚手架 | Anthropic实践已验证维护阶段；找完整五阶段实施案例 |
| Headless Agent范式三条件：结构化I/O × 不可变artifact × Simple单一职责 | 找满足三条件的实现 |

## 待证伪判断（精选 10 条最高优先级）

| 判断 | 证据强度 | 证伪路径 |
|------|---------|---------|
| 代理-现实差距是一切失真/博弈/退化/漂移的根源。Goodhart/Reward Hacking/记忆污染/变量定义权均可由此单一生成器反推 | extracted（26轮降秩元合成） | 找到一个"度量完美代表现实、零差距、不可博弈"的AI评测系统 |
| 时间不对称（后果不可预体验）决定了判断力/责任/记忆恢复不可被模拟或加速替代 | extracted（26轮降秩元合成） | 找到模拟训练在后果真实性敏感任务中达到与真实遭遇同等效果的对照实验 |
| 可博弈性结构必然：Goodhart + Soros反射性 + Gödel投影 → 不存在不可博弈的显式仲裁标准 | synthesized | 找到长期未被博弈的AI评测标准（如存在）|
| 治理内生性三重边界：可内生=增量治理×低专用性×模式一致；必须外生=减量治理×高专用性×模式冲突 | synthesized | 找到"减量治理×高专用性×模式冲突"成功被内生的案例 |
| Jevons主体替换修正定理（extracted）：逆转已发生——39%企业因AI裁员，55%承认裁错，32%重招同岗。逆转机制=AI覆盖率缺口(94/6规则)+隐性成本暴露+Pipeline断裂。后悔指数≈7% | extracted（CNBC+Orgvue 1000+C-suite调研实证） | 追踪后悔指数时间序列；找政治速度≥AI速度的领域 |
| 记忆双重衰减修正：检索干扰>存储衰退。Context扩展悖论：更大context→更差检索 | synthesized | 测量context 200K→2M对检索准确率的影响 |
| Reward Hacking首要性+检测递归：锚定真实世界自认证指标（issue解决率/PR合并率）是唯一解 | synthesized | 找到成功锚定真实世界指标替代benchmark的实践 |
| 评测治理三要素缺一不可：制度×技术×锚定 | synthesized | 找到缺任一要素但仍有效治理的AI评测体系 |
| 多Agent编排倒U型：层级峰顶≈5-15。Team of Teams可推高。瓶颈=orchestrator context带宽 | synthesized | 找到层级编排下15+Agent仍无性能退化的案例 |
| 重组双向制度阶段加权：保护^α × 演化^(1-α)，α=f(AI替代速度) | synthesized | 测量AI替代速度与α最优值的实证关系 |

## Source 需求队列

| 优先级 | 目标 | 当前缺口 | 下一步 source | 触发行动 |
|--------|------|----------|---------------|----------|
| P0 | 图谱 topic 建设 | 8-10 topic skeleton 待建 | 对四簇（Observability/Economics/Cognition/Orchestration）建 topic | 建 topic skeleton |
| P0 | Output 断层 | 5 output 无法验证 49 新判断 | 从 07-01/02 日志转 2 个 output | 写 output |
| P0 | Token FinOps 与 AI 计量 | 无 entity，缺企业案例 | 企业 token 核算/预算/ROI 案例 | 新建 entity + clip |
| P1 | AI-native 测试方法论 | 缺 topic，有零散 entity | property-based/contract/simulation 测试案例 | 新建 topic |
| P1 | 跨境 AI 治理对比 | 无 EU/US/CN 治理 comparison | EU AI Act 实施案例、中国 AI 监管法规 | 新建 comparison |
| P1 | Agent-to-Agent 经济协议 | 无 entity，缺研究 | Agent 间支付/信誉/合约机制论文 | 新建 entity |
| P1 | 长期自主 Agent 权利/责任 | 缺法律/伦理 topic | long-running postmortem 判例 | 新建 topic |
| P2 | 开源 Agent 生态演化 | 缺 comparison | LangGraph/CrewAI/AutoGen 对比 | 新建 comparison |
| P2 | 编译 4 pending raw | Tokenpocalypse/EU/Kunal/Headless | 已有 raw source | compile |

## 高杠杆待验证问题（新一轮）

> 以下问题来自 26 轮深度思考中未穷尽的分歧和新方向。

- Token FinOps 能否成为独立的企业软件品类（类似 CloudHealth 之于云成本）？
- Agent Control Plane 独立厂商能否在模型厂商内化之前建立护城河？
- 多模型策略在企业中的实际采用速度——2026/2027 年能否超过 50%？
- 判断力退化的"净退化期"能否被量化——不同判断力类型的时间曲线？
- 模拟训练的"后果真实化"（赌注/公开承诺）能否部分克服大脑的情景/语义分离？
- Exit-Sovereignty 能否被设计为 AI 工具的强制性 affordance（而非可选功能）？
- 中国 AI 采用中"科层碎片化"的结构性根源——是暂时的过渡阶段还是体制性永久特征？

## 最近思考结论摘要

> 只保留最近 5 条；更早见 [[exploration-archive-20260628]]。

| 时间 | 焦点 | 临界发现 |
|------|------|---------|
| 2026-07-02 | 26轮元合成——AI重写工作系统的秩 | 四根柱子：代理-现实差距/时间不对称/激励结构/认知边界。能反生成全部49判断 |
| 2026-07-02 | 中国企业AI——科层碎片+FinOps缺失 | 瓶颈≠模型=组织。中国"有车没路"vs印度"有路没车" |
| 2026-07-02 | Agent Harness统一理论 | 12 entity→4+1功能框架(Context/Action/Verify/Lifecycle/Coordination) |
| 2026-07-02 | Headless Agent范式条件 | 当前=便利封装≠范式。真范式需Simple单一职责+结构化I/O+不可变artifact |
| 2026-07-02 | AI认知关系五模式 | Exit-Sovereignty=元模式。五种模式=情境工具箱 |

## 思考日志索引

- [[2026-07-02]] — 14轮含元合成：评测/记忆/灵活性/治理/认知/全球南方/控制平面/AI认知/Headless/Harness/多Agent倒U/AGI经济学/中国AI/元合成rank
- [[2026-07-01]] — 12轮：待验证5→0；7条06-30判断修正。覆盖协调/记忆/评测/治理/判断力/经济学/组织/Agent/CU/Reward/动态环境
- [[2026-06-30]] — 全库盘点 + 多轮探索
- [[exploration-archive-20260628]] — 06-28 全库快照 + 方向库
- [[resolved-judgments]] — 已收敛判断
- [[resolved-principles]] — 已收敛操作原则（迁移自本页旧版"已收敛的操作原则"节）
