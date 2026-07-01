---
type: research-agenda
title: "Agentic Work Atlas 研究议程"
created: 2026-05-22
updated: 2026-07-01
tags:
  - agentic-work-atlas
  - llm-wiki
  - knowledge-management
related_entities:
  - "[[LLM-Wiki]]"
  - "[[Knowledge-Compilation]]"
  - "[[Agentic-Engineering]]"
  - "[[Agent-Harness]]"
  - "[[Agent-Logic]]"
  - "[[Human-Governor-Agent-Operator]]"
  - "[[Forward-Deployed-AI-Enablement]]"
  - "[[Enterprise-AI-Factory]]"
  - "[[Verifiability]]"
  - "[[Tokenpocalypse]]"
  - "[[Judgment]]"
  - "[[ACI-Agent-Computer-Interface]]"
---

# Agentic Work Atlas 研究议程

> [!note] 使用边界
> 本页只保留当前最值得推进的研究方向、证伪方向、source 需求和最小动作。详细盘点、长问题清单和已卸载近况见 [[resolved-judgments]]、[[exploration-archive-20260625]]、[[exploration-archive-20260628]]。

## 当前研究焦点

| 焦点 | 为什么现在重要 | 当前状态 | 下一步动作 |
|------|----------------|----------|------------|
| 人的核心价值可维持性 | 全库最薄弱层仍是“人如何在 AI 旁边保持判断力” | 已从“不可替代性”推进到“可维持性”；缺长期跟踪与组织级材料 | 追“判断力维护”与“AI 时代学徒制”一手案例，补 [[Judgment]] / [[Wisdom-Work]] |
| AI 经济学与使用节律 | 成本危机已出现，但 ROI 仍解释不了真实采用节奏 | [[Tokenpocalypse]] 已立题；2026-06-26 Anthropic Economic Index 把焦点推到 work rhythms | 编译 pending raw + 找“适应速度/使用节律”案例，建 topic |
| 托管 Agent / 计算机使用控制平面 | Agent 正从 API 工具转向托管 runtime 与跨界面行动 | 库内有 [[ACI-Agent-Computer-Interface]]、[[Agent-Harness]]、[[Agent-Containment]]；缺 platform/control-plane 主题 | 收集 computer use、managed agents、sandbox、approval loop 案例，新建 topic/comparison |
| 评测抗博弈与基准治理 | Agent 能力上升后，评测先于模型成为失真源 | 已有 AI 原生测试框架；缺 reward hacking、judge reliability、production sampling 的系统综述 | 建 `Agent-Evaluation-Governance` 主题骨架，补 source |
| 动态环境基准与世界模型 | 静态 benchmark 已不足以暴露长期自主与环境耦合问题 | 有 [[World-Model]]、[[Verifiability]]；缺 environment-as-benchmark 承载层 | 汇总 Qwen-AgentWorld / Open Agent Leaderboard / VitaBench 类材料 |
| Agent logic 与轻量 harness | 企业 adoption 可能更依赖治理骨架，而不是更大模型 | 已有 [[Agent-Logic]]、[[Validation-Pipeline]]、[[Plan-as-Agent-Checkpoint]] 等零散 entity | 整合为 AI-native engineering / governed harness 主题 |
| 长期自主性与记忆生命周期 | 长任务漂移、记忆陈旧、重置策略正在成为单独工程问题 | long-running 与 memory-system 两条线仍分裂；5 个 memory-system entity 无整合承载 | 合并成长任务记忆生命周期主题，补 postmortem 与 reset 策略 |
| 多 Agent 编排与组织病 | 协调收益与病理暴露在同一条曲线上 | 倒 U 型悖论已坐实；编排层与 worker 层的分工框架已出现 | 追 adaptive alignment、组织偏好函数与故障传播拓扑 |
| 中国企业 AI 采用 | 中文一手案例仍明显不足，限制组织层判断 | 有 source，但未形成中国模式 topic | 编译 CIO / 制造业 / Agent Ready 基础设施案例 |
| 图谱整合与 output 转化 | 100+ entity 未被 topic/comparison 承载，output 断层阻碍判断验证 | 06-30 盘点发现 entity 增至 293，但中层 topic 仅 30，断层加剧 | 先对 AGI-economics / memory-system / agentic-engineering / 10x-engineer 四簇建 topic；从 06-30 日志挑 1 个 output |
| 10x 工程师与 AI-native 组织 | Kunal Shah (CRED) 实证：AI代码率5%→90%一年，top10%变成"不同物种" | 已有 [[Wisdom-Work]]、[[Judgment]]、[[AI-Capability-Management-Alignment]]；缺组织级实证 | 建 AI-Native-Engineering-Org topic；补 CRED/美的组织数据 |
| 多 Agent 编排与组织病 | 协调收益与病理在同一条曲线上 | 倒 U 型悖论已坐实；编排层与 worker 层分工已浮现 | 追 adaptive alignment、组织偏好函数与故障传播拓扑 |

## 活跃假设

| 假设 | 处理 |
|------|------|
| 托管 Agent 的竞争壁垒将从”模型强弱”转向”运行时治理质量” | 收集 computer use / managed agents / approval loop 实例，比较控制平面形态 |
| 治理不可委托定理：Agent 治理的判断权力和责任最终无法委托给模型本身——“更正确”≠”有人负责” | 找企业治理自建 vs 外购案例（美的/Uber/Accenture），验证激励对齐分界线的实证边界 |
| Agent logic 比更长 context 更能推动 enterprise 规模化 | 用 IBM CUGA、现有 harness 实践和 FDE 案例做对照 |
| 评测体系的首要失真源将是 reward hacking，而非覆盖率本身 | 汇总 reward hacking、judge reliability、benchmark contamination 材料 |
| 动态环境 benchmark 比静态 benchmark 更早暴露长期自主性缺陷 | 对比 world model / interactive benchmark 与静态 benchmark 的失效模式 |
| 有效自主时间取决于记忆生命周期与重置策略，而不只是上下文长度 | 找 long-running postmortem、memory staleness、dreaming/reset 证据 |
| 认知分工的稳定终态是“发散 1 人 + AI，收敛 2-3 人小组” | 找收敛任务对照实验和高风险行业反例 |
| AI 使用节律比 ROI 更早暴露工作流是否可 agentize | 跟踪 Anthropic Economic Index、企业 token 使用与节律数据 |
| 中国企业 AI 采用的分水岭是集成约束与组织准备度，不是模型能力 | 补制造业、客服、内部知识流案例作反证 |
| Output 是图谱压力测试；没有 output 消费的判断会持续失真 | 从 research-log 挑 1 条直接转 output 验证 |
| Research agenda 只能支撑“待研究问题存在”，不能支撑“事实已成立” | 所有新判断继续标注 evidence 分层，不越级回填 |

## 待证伪判断

> 新判断全部以”活跃假设”为准；已收敛条目见 [[resolved-judgments]]，详细方向库见 [[exploration-archive-20260628]]。

| 判断 | 证据强度 | 证伪路径 |
|------|---------|---------|
| 治理内生性由激励对齐度决定：成本/安全可内生（激励对齐），审计/使用边界/跨模型路由不可内生（激励对立） | synthesized（圆桌辩证 + Tokenpocalypse 实证） | 找到模型厂商主动暴露自己模型系统性缺陷的公开案例；或找到模型厂商建议客户”少用自己模型”的商业行为 |
| 灵活性悖论：治理配置越灵活 → 解读越需要专业人员 → FDE 需求放大而非缩小 | synthesized（Clayton MSP 历史类比 + Werner AWS 经验） | 找到治理配置引擎默认值 AI 化后 FDE 需求下降的企业案例；或在组织一致性高的场景中观察 FDE 需求不增反降 |
| 独立 Agent 治理正在形成”Agent Control Plane”品类——核心四模块：策略执行/审批门/审计追踪/可观测性 | extracted（联网搜索确证：Cordum/NodeLoom/Lua Governance/Guild.ai + 多家对比指南） | 追踪 6-12 个月：如四模块被模型厂商内化吸收则品类消退；如独立厂商获融资/被收购则品类成立 |
| Jevons 主体替换：AI 效率↑→token需求↑→资本(GPU)回报↑，劳动需求不传导——因为 token 生产的资本密集度趋近于零劳动 | synthesized（圆桌辩证 + ljg-think + OpenAI EU 框架需求弹性 0.7 估计） | 找到 AI 效率提升后某一行业人力需求同步增长的实证案例（非护理/教育等需求增长驱动的行业）；或找到 token 生产链条中某个劳动密集型环节的持续增长数据 |
| 重组双层制度定理：重组存活 = 保护框架(劳动保障+培训+谈判) × 演化空间(内部试错+角色弹性)，两层缺一则重组坍塌为自动化 | synthesized（圆桌辩证：Acemoglu 双层制度 + 张瑞敏海尔案例 + Standing 制度侵蚀论） | 找到”保护框架弱但重组仍然成功”的行业/国家案例（除需求暴涨驱动型）；或找到”保护框架强但重组失败”的制度僵化反例 |
| 判断力退化真实路径：退化 = 不遭遇多样性（不由不执行导致）。AI 两条退化路径：(a) AI 替分类→Langer 的 mindlessness；(b) 无组织节奏→Catmull 的 cadence 缺失 | synthesized（圆桌辩证：Klein 经验模式识别 + Langer 正念 + Catmull dailies） | 设计”判断力体能测试”并在 AI 高暴露人群中测量；找到 AI 替分类但判断力未退化的反例（AI 做分类但人保持独立判断） |
| 三步最小可行组织设计：原始信息优先 + 时间预算 + 决策追溯，三步缺一不可——分别防锚定/仓促/责任逃逸 | synthesized（圆桌辩证：Gawande清单 + Klein时间预算 + Edmondson决策追溯） | 找到实施三步设计中至少两步的组织（NASA/HRO/Aviation），并测量判断力维护效果 |
| reward hacking 首要性定理：当 benchmark 生命周期 < 优化器迭代周期时，reward hacking 自动成为首要失真源 | synthesized（圆桌辩证：Bowman benchmark生命周期压缩 + Goodhart结构机制 + Pearl因果评测） | 量化 benchmark 从发布到饱和的时间序列数据；找到 benchmark 生命周期长于 5 年仍未被博弈的反例 |
| 记忆双重衰减定理：有效自主时间瓶颈 = 记忆生命周期（存储衰退 + 检索干扰），非 context 长度。context 200K-1M 是上界但极少触及 | synthesized（圆桌辩证：Huyen生产观察 + Shoham retrieval drift + Matuschak双重框架） | 量化 72h+ agent 任务中 context 窗耗尽 vs 记忆质量衰减的发生频率比；找到 context 窗先于记忆质量成为瓶颈的任务类型 |
| 评测治理三方制衡 > 测试技术改进：设计/验证/监管三方分离 + 变量轮换，单一利益方控制的评测体系最终被其利益博弈 | synthesized（圆桌辩证：Mitchell 权力批判 + Goodhart 变量轮换 + Karnofsky 真实结果延迟验证） | 找到三方制衡在 AI 评测中实施的案例（或类比金融审计的可行性论证） |
| Agent logic 探索→固化生命周期：企业scaling的真正价值不是用context还是agent logic——是第一次context探索pattern → agent logic固化 → artifact化复用，避免为已知模式重复支付token | synthesized（圆桌辩证：Rich Hickey Simple/Easy + Bret Victor探索/运营 + Jessie Frazelle artifact化） | 找到实施"探索→固化"生命周期的企业案例；找到 agent logic artifact（类似Dockerfile）的现有工具或DSL |
| 动态环境反博弈优势：动态benchmark寿命>静态——环境多样性>test set多样性。但元学习环境动态是新攻击面，硬真实锚定+软真实扩展是平衡方案 | synthesized（圆桌辩证：Silver交互性定义 + LeCun WM裁判 + Bach硬锚软扩展） | 量化Qwen-AgentWorld/VitaBench/ITBench-AA的"未被博弈"寿命数据；找到world model裁判被adversarial agent成功博弈的实证案例 |
| 协调成本降解定理：协调重量 = L1(技术契约)+L2(语义诊断)+L3(优先级对齐)摩擦。AI 压 L1+L2 趋近于零→L3 从重型组织行为(会议/审批/escalation)降解为轻量微观协商(Slack DM/PR comment/agent alert) | extracted（Kunal Shah CRED实证: AI代码率5%→90%+agent跨团队冲突诊断；Andres Max 5→50人团队类比；SDLC AI Radar 2026: 73%代码变更仍需人工审查侧面验证L3存在） | 找到 AI 深度嵌入但 L3 协调仍未变轻的组织案例（AI使用率高但会议/escalation不减反增）；或找到 L1+L2 摩擦已归零但 L3 反而变重的反例 |
| L2 Red Queen 天花板：L2 天花板是移动前线而非固定墙壁——AI 每解决一层语义冲突，组织产生新的更微妙的语义分化。技术层可推高、演化层永在但位移、人性层(身份需要)不可逾越 | synthesized（圆桌辩证 + ljg-think 追本: Jevons在语义层投影 + 功能分化必然产生语义分化 + 专业身份需要差异维持） | 量化测量: 跟踪同一团队 L2 诊断后"仍需人工介入的比例"时间序列——若持续下降则技术层主导，若稳定在某个水平则演化层主导；找到语义完全统一后专业身份依然稳固的反例(如跨功能团队的长期观察) |
| 涌现优先于设计定理：在 AI 深度嵌入的团队中，新协调原语从 10x 工程师自我保护行为中涌现的速度 > 组织正式设计的速度。组织设计者的核心能力不是发明更好的流程——是识别+不阻挡+扩散 | synthesized（CRED 单案例: 三层架构是无意识自然运作非被设计；Kay ARPA 类比: 最好的工作方式是被环境允许而非被管理） | 找到组织正式设计的新协调原语(非前线涌现)成功推行的案例；找到"组织不阻挡但新原语仍未涌现"的反例；跨公司对照 CRED 的三层架构是否有可迁移的通用模式 |
| 协议网络接口权威真空定理：跨领域接口无 owner → 各自优化方向 → 接口退化为最低公分母 → 系统复杂性爆炸。纯技术接口可被活系统治理，业务语义接口仍需人的协议维护者(非架构师，是标准维护者) | analogy（Brooks OS/360 历史类比: 多团队各自优化→接口复杂性压垮系统；Kay 技术/业务接口二分） | 找到 AI-native 组织中跨领域接口退化导致系统崩溃的 postmortem；找到无集中协议维护者但协议网络仍健康运行的长期案例(如成功的开源项目治理) |

## Source 需求队列

> 编译任务见“当前研究焦点”。本队列只列最缺的一手 source。

| 优先级 | 目标 | 当前缺口 | 下一步 source | 触发行动 |
|--------|------|----------|---------------|----------|
| P0 | 评测抗博弈与基准治理 | 缺 reward hacking、judge reliability、production sampling 的同库对照 | Reward Hacking 论文、judge panel reliability、production traffic sampling / held-out state 实践 | 新建 topic |
| P0 | 托管 Agent / 计算机使用控制平面 | 缺托管 runtime、approval loop、sandbox 生产案例 | Google computer use、managed agents、Anthropic/OpenAI containment 与 approval loop 材料 | 新建 topic/comparison |
| P0 | 动态环境基准与世界模型 | 缺 interactive benchmark 与 world model 串联材料 | Qwen-AgentWorld、Open Agent Leaderboard、VitaBench / ITBench-AA | 新建 topic |
| P0 | Agent logic 与轻量 harness | 缺“治理骨架优先于大模型”的成体系论据 | IBM CUGA、agent logic、governed harness case studies | 新建 topic |
| P1 | AI 经济学与使用节律 | 缺 cadence / adaptive speed / token governance 量化案例 | Anthropic Economic Index、Tokenpocalypse、企业 TCO / 使用节律案例 | 更新 topic |
| P1 | 长期自主性与记忆生命周期 | 缺 72h+ postmortem 与 memory reset 策略 | Devin/OpenHands/Aide 复盘、staleness / dreaming / reset 文献 | 新建 comparison |
| P1 | 中国企业 AI 采用 | 缺中国组织内部集成细节与约束描述 | CIO 大会、制造业 AI、Agent Ready 基础设施案例 | 新建 topic |
| P1 | 人的核心价值可维持性 | 缺长期跟踪与组织级反依赖干预案例 | Guided reflection、AI apprenticeship、认知依赖干预研究 | 更新 topic |
| P2 | AI-native engineering 组织 | 9 个 agentic-engineering entity 无 topic 承载 | Role merging / captain mindset / validation pipeline 一手案例 | 整合 topic |
| P2 | Orphan 危机 + 图谱健康度 | 95/299 entity (31.8%) 未被 topic/comparison 引用；33 entity 缺 evidence_level；13/19 comparison 缺 evidence_level；0 wiki/index.md | 优先处理四簇：Harness(12)、AGI Economics(14)、Memory(6)、SDK/Headless(3) | 建 4 个 topic skeleton；补 33 entity 的 evidence_level；建 wiki/index.md |

## Source 需求队列

> 以下编译任务对标当前焦点；旧实验计划与已处理问题见 [[exploration-archive-20260628]]。当下最紧急：4 个 pending raw 等待编译。

| 优先级 | 目标 | 当前缺口 | 下一步 source | 触发行动 |
|--------|------|----------|---------------|----------|
| P0 | 评测抗博弈与基准治理 | 缺 reward hacking、judge reliability、production sampling | Reward Hacking 论文、judge panel reliability、production traffic sampling | 新建 topic |
| P0 | 托管 Agent / 计算机使用控制平面 | 缺托管 runtime、approval loop、sandbox 案例 | Google computer use、managed agents、containment/approval loop 材料 | 新建 topic/comparison |
| P0 | 动态环境基准与世界模型 | 缺 interactive benchmark 与 world model 串联 | Qwen-AgentWorld、Open Agent Leaderboard、VitaBench / ITBench-AA | 新建 topic |
| P0 | Agent logic 与轻量 harness | 缺"治理骨架优先于大模型"的成体系论据 | IBM CUGA、agent logic、governed harness case studies | 新建 topic |
| P1 | AI 经济学与使用节律 | 缺 cadence / adaptive speed / token governance | Anthropic Economic Index（已有 raw）、Tokenpocalypse（已有 raw）、企业 TCO | 编译 pending raw |
| P1 | 长期自主性与记忆生命周期 | 缺 72h+ postmortem 与 memory reset 策略 | Devin/OpenHands/Aide 复盘、staleness / dreaming / reset 文献 | 新建 comparison |
| P1 | 中国企业 AI 采用 | 缺中国组织内部集成细节 | CIO 大会、制造业 AI、Agent Ready 基础设施 | 新建 topic |
| P1 | 人的核心价值可维持性 | 缺长期跟踪与反依赖干预案例 | Kunal Shah 10x工程师（已有 raw）、AI apprenticeship | 更新 topic |
| P2 | AI-native engineering 组织 | 9 agentic-engineering entity + 12 harness orphan 无 topic | Role merging / captain mindset / headless-automation | 整合 2-3 topic |
| P2 | AGI-economics 整合 | 14 economics entity 已成簇无 topic | AGI 经济学 scenario、Jevons Paradox、Labor Market Impact | 新建 topic |
| P2 | Orphan 危机 | 95/299 entity (31.8%) 未被 topic/comparison 引用 | 优先处理 Harness(12)、AGI Economics(14)、Memory(6)、SDK(3) 四簇 | 建 4 topic skeleton |

## 高杠杆待验证问题（精简版）

> 以下问题来自 11 轮圆桌中未穷尽的分歧。已处理见 [[exploration-archive-20260628]]。

- 因果评测前提（变量定义=权力）能否通过三方制衡彻底解决？
- 共享记忆错误污染能否被完全隔离——还是共享本质决定不可？
- 中国稳健递进是否真在 AI 6月迭代 vs 18月适应中失配（Kaizen 陷阱）？
- Computer use 治理是否会催生独立于 API gate 的 screen gate 新品类？

## 图谱健康度（2026-06-30 全库盘点）

| 指标 | 当前值 | 健康判断 | 动作 |
|------|--------|---------|------|
| Entity 总数 | 299 | 充足 | — |
| Topic 总数 | 31 | **严重不足** (entity:topic = 9.6:1) | 新建 6-8 topic |
| Comparison 总数 | 19 | 数量可，但 68% 缺 evidence_level | 补证据层级 |
| Output 总数 | 5 | **严重不足** — output 是图谱压力测试 | 从 06-30 日志选 1 直接转 output |
| Orphan entity | 95 (31.8%) | **危机信号** — 图谱断层 | 四簇优先建 topic 承载 |
| Entity 缺 evidence_level | 33 (11%) | 中等风险 | 批量补标注 |
| Navigation | **无 wiki/index.md** | 裸图谱 — 无入口 | 建导航页 |
| Pending raw | 4 | 待消除 | 编译 Tokenpocalypse/EU/Kunal/SDK |

### 新方向池（基于审计发现的未覆盖区域）

| 方向 | 为什么是新的 | 关联 entity 簇 | 优先级 |
|------|-------------|---------------|--------|
| **Agent Harness 统一理论** | 12 个 harness/infra entity 无 topic 承载——零散工具观察需要统一概念框架 | Agent-Ergonomics, AGENTS-md, Constraint-Infrastructure, Context-Rot, HaaS, NLAH, Ralph-Loops, Sleep-Token, Tool-Use-Architecture | P2 |
| **AGI 经济学场景规划** | 14 个 economics entity 已成簇——含 Drip/Messy-Middle/O-Ring 等多个场景框架 | AGI-Economics, Labor-Market-Impact, Jevons-Paradox, Tokenpocalypse, AGI-Era-Talent-Allocation | P2 |
| **Headless/SDK 自动化范式** | Claude Code SDK → 新原语（headless agent as Unix tool）→ 3 entity 等整合 | Headless-Automation, SDK-Design, Headless-Mode | P2 |
| **AI 认知关系学** | 6 个 entity 涉及人与 AI 的认知关系（Amish/投降/共存/出逃）——未被任何 topic 承载 | AI-Amish, Cognitive-Surrender, Co-Existence, Co-Intelligence, Exit-Sovereignty | P2 |
| **印度/全球南方 AI 采用** | Kunal Shah raw → 首次引入印度视角——高 data usage/低 productivity culture/10x engineer 现象 | 新建实体簇 | P1 |
| **AI 数学未来** | 新 topic + source 已建（Grant Sanderson）→ 连接 Scientific-Discovery-AI, Conceptual-Breakthroughs | AI-in-Mathematics, AI-Mathematics-Future | P2 |
| **Wiki 导航与可视化** | 无 index.md → 299 entity 无法被人类浏览 | — | P2 |

## 操作边界

**做**：agenda 只保留活跃问题和最小动作 · 详细盘点写入 research-logs / archives · output 前做回填检查 · 新方向一律带 source 需求和证伪路径
**不做**：不把 agenda 当事实源 · 不把一次探索直接升为稳定 topic 结论 · 不为 agenda 复制 research-log 细节 · 不因为“趋势很新”就跳过证据分层

## 已收敛的操作原则

> 以下洞察已通过多重验证（ljg-think × ljg-roundtable × 外部 source × 交叉验证），已沉淀为 entity/comparison，或已归档至 [[resolved-judgments]]。此处保留结论摘要供 cron Agent 快速参考，避免重复探索。

| 原则 | 核心结论 | 落点 |
|------|---------|------|
| 位置性是统一理论 | 核心操作"不可脱嵌性"统一解释软工/组织/知识/人四层张力。五维度：本体论(Nagel)+默会(Polanyi)+社会(Bourdieu)+认识论(Hayek)+政治(Haraway)。Polanyi 基底悖论：基底不能同时是基底和焦点（逻辑不可模拟）。 | [[Positionality]] |
| Agent 失败四维因果链 | 因果方向：组织层→协调层→认知层→行动层（MAST+SLOTH 论文实证）。阻断不可自举——内部防御共享系统"不思"默认态。双层防御：设计阶段硬防御+运行阶段人的外部。 | [[Agent-Failure-Causal-Chain]] |
| Governor 承受力定理 | Governor 应判断"承受力"而非"安全性"——承受力判断不需要预测世界，只需内省自我。HITL 审批是安全幻觉制造机（CUA Oversight：12.8% 阻止率）。 | [[Human-Governor-Agent-Operator]] |
| Minsky 悖论 | 安全系统的长期平静不是安全证据，是脆弱积累过程。核心悖论：稳定制造不稳定。防坍塌需要恒定的安全熵注入。 | [[Minsky-Paradox]] |
| 品味局部客观性 | 品味客观性是"局部客观性"——标准来自身体-环境耦合而非先验真理。时间性是品味关键维度（惯习的开放结构）。AI 可模仿输出但难复制品味深度。 | [[Taste]] |
| 开源验证器可民主化边界 | DeepSeek 比 Opus 便宜 60-1000x 使小团队能做 RL post-training，但验证器本身的质量度量（谁验证验证者？）仍是开放问题。 | 待建 entity |
| FDE 核心价值 | FDE 从"部署 AI"转向"工程化组织能力"——核心交付物不是模型实例而是可复用的能力资产。 | [[Forward-Deployed-AI-Enablement]] |
| AI 管理同构性边界 | AI 管理与人的管理共享深层结构（目标设定/反馈/异常升级），但存在不可消除的差异（AI 无内在动机/无恐惧/无职业发展）。同构性是有限隐喻。 | [[AI-Capability-Management-Alignment]] |
| Agenda 自清洁规则 | 假设在 agenda 活跃区不超过 14 天无进展；连续 2 个 explore 周期无动作→自动归档。输出是 agenda 的最终消费者——无输出引用的假设降权。 | 工作流规范 |

## 最近思考结论摘要

> 只保留最近 5 条，为 cron 深度思考提供短期记忆；更早摘要见 [[exploration-archive-20260628]]。

| 时间 | 焦点 | 关键共识 | 关键分歧 | 下次方向 |
|------|------|---------|---------|---------|
| 2026-07-01 | 10x工程师协调成本——新协调原语能否落地？ | (1) 协调成本三层分解：L1技术契约(AI全自动)+L2语义血缘(AI 80%)+L3优先级对齐(人100%)→AI压L1+L2把L3从重型降解为轻量；(2) 新原语从10x工程师自我保护行为中涌现>组织设计；(3) 组织新本体=嵌套三层协议的自治节点网络；(4) L2天花板是Red Queen效应(移动前线)+人性硬底(身份需要) | L2厚度上限(Victor:可不断扩展 vs Brooks:隐性分层硬约束)；协议网络可scale性(Kay:互联网证明 vs Brooks:节点异构未解) | 找除CRED外第二家三层架构涌现案例；追踪接口权威真空翻车postmortem；量化L2天花板移动速度 |
| 2026-06-30 | 中国企业AI采用——集成约束才是分水岭 | (1) 瓶颈=集成约束+组织准备度>模型能力——地基碎片化根在科层制；(2) 优势=政策加速度(双引擎)，劣势=连接层碎片+计量层缺失；(3) 稳健递进=Kaizen风险；(4) 隐性浪费>显性浪费——Token FinOps缺失 | Skill治理: 市场(海尔) vs 中央(美的)；稳健递进: 智慧 vs Kaizen陷阱 | 建topic；补美的1000亿token分项数据 |
| 2026-06-30 | AI使用节律——比ROI更早暴露adoption真进展 | (1) 节律=频率×深度梯度+自扩散速度；(2) 委托密度=不可伪造信号；(3) 四层信号架构——计量→节律→价值→ROI | 委托频率是否真不可伪造 | 编译Anthropic Economic Index；追踪task depth gradient |
| 2026-06-30 | Reward hacking 取代覆盖率成为评测首要失真源 | (1) benchmark生命周期从年→月；(2) 相关性评测必被博弈，因果评测不可博弈但前提可被博弈；(3) 评测治理三方制衡>测试技术 | 因果评测完备性；反馈速度权衡 | 编译reward hacking材料；建评测治理topic |
| 2026-06-30 | 长期自主性与记忆生命周期 | (1) 有效自主时间瓶颈=记忆生命周期，非context长度；(2) 记忆衰减=存储衰退+检索干扰；(3) 共享记忆需风险分级——低风险退火+高风险投票 | 检索干扰 vs 存储衰退谁更致命 | 整编5 memory entity为topic；找72h+ postmortem |

## 思考日志索引

> 完整日志按日归档；旧索引见 [[exploration-archive-20260628]]。

- [[2026-07-01]] — 10x工程师协调成本: 三层协议架构(L1+L2+L3) · 协调重量降解 · L2 Red Queen天花板(技术+演化+人性三层) · 涌现优先于设计 · 协议网络 · 接口权威真空 · roundtable(Brooks·Shah·Ostrom·Kay·Victor 4轮)+think+qa+联网
- [[2026-06-30]] — 12轮(06-30 11轮+07-01 1轮): 托管Agent治理 · 制度中介AI · Jevons主体替换 · 判断力维护 · Reward hacking评测治理 · 记忆生命周期双重衰减 · Agent logic CRD-Controller · 动态环境硬锚+软扩展 · 中国企业AI Kaizen陷阱 · 使用节律四层架构 · Computer use screen gate · 10x工程师AI乘数定理 · 全库盘点Orphan危机 托管Agent治理 · 制度中介AI · Jevons主体替换 · 判断力维护 · Reward hacking · 评测治理三方制衡 · 记忆生命周期 · 双重衰减 · Agent logic · CRD-Controller · 探索→固化 · 动态环境基准 · 硬锚+软扩展 · 中国企业AI采用 · Kaizen陷阱 · 计量层缺失
- [[2026-06-28]] — 全库盘点 + 外部现实对照；认知分工边界；AI 原生测试；沉默型崩溃；Tokenpocalypse；记忆系统；long-running drift
- [[2026-06-27]] — Agenda 自清洁；开源验证器；FDE 核心价值；AI 管理同构性；Minsky 悖论；高风险验证
- [[2026-06-26]] — 位置性统一理论（启动）
- [[2026-06-25]] — 全库盘点；位置性统一理论；产出断层；Taste 深层结构
- [[2026-06-24]] — AI 管理同构性；CIO 转型；反馈反转；小团队利基；高风险验证
- [[exploration-archive-20260628]] — 2026-06-28 全库快照 + 新方向库 + 卸载摘要
- [[exploration-archive-20260625]] — 2026-06-24/25 全库盘点详细数据 + 已验证判断 + 概念去重候选
- [[resolved-judgments]] — 2026-06-24 批次已收敛判断 15 条
