---
type: research-agenda
title: "Agentic Work Atlas 研究议程"
created: 2026-05-22
updated: 2026-06-28
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
| 图谱整合与 output 转化 | 100 个 entity 未被 topic/comparison 承载，5 个 output 仅覆盖 12 个 entity | 真缺口不是 raw 不够，而是中层 topic 和 output 断层 | 先对 AGI-economics / memory-system / AI-native engineering 三簇建 topic，再从 2026-06-28 日志挑 1 个 output |

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
| P2 | AGI-economics / memory-system 整合 | 5+5 个 entity 已成簇但未成主题 | AGI 经济学 scenario 材料、memory lifecycle 架构材料 | 提升整合层承载 |

## 下一步最小实验

- 编译 `raw/The Tokenpocalypse Is Here Companies Are Scrambling To Stop Spending So Much on AI.md`，把 AI 经济学从研究议程推到 source-summary。
- 先建 3 个 topic skeleton：`Agent-Evaluation-Governance`、`Dynamic-Agent-Environments`、`AI-Native-Engineering-Organization`。
- 把 5 个 `memory-system` entity 并到一张“记忆生命周期”框架图，验证是否真能覆盖现有概念。
- 选 1 条 2026-06-28 日志直接写成 output，验证“output 是图谱压力测试”。
- 对 100 个未承载 entity 先只处理 3 个成簇区：AGI-economics、memory-system、agentic-engineering。
- 为“托管 Agent / 计算机使用控制平面”先做 1 页 source map：runtime、approval、sandbox、audit 4 列。
- 为“评测抗博弈”先做 1 页 source map：benchmark、judge、traffic sampling、reward hacking 4 列。

## 高杠杆待验证问题

> 全量问题库见 [[exploration-archive-20260628]]；这里只留最该优先推进的问题。

**运行时与控制平面：**
- computer use 任务是否会把治理重心从“工具调用限制”转到“运行时环境设计”？
- managed agents / hosted runtimes 是否会削弱 FDE 的一部分差异化价值，还是反而强化现场定制？

**评测与抗博弈：**
- production traffic sampling + held-out states + adversarial red-team 的组合，是否能实证降低 reward hacking？
- 多 Agent 系统的 composition coverage 能否做成稳定可维护的门禁？

**长期自主与记忆：**
- 不同 harness / 记忆架构下的“有效自主时间”分布是什么？
- staleness、dreaming、summary page、shared memory 到底是互补层，还是不同命名下的同一件事？

**组织与人的位置：**
- 判断力维护最有效的是个体反思机制，还是组织级节奏 / 责任设计？
- 收敛任务中的最小有效单元，是否真稳定在 2-3 人，还是高度依行业和风险等级变化？

**经济学与采用：**
- 使用节律是否比 ROI 更早、更稳地反映 adoption 真进展？
- 中国企业落地中的真正瓶颈，是模型、数据、流程、权限，还是责任结构？

## 下一批剪藏方向

**软件工程**：托管 Agent runtime · computer use 治理 · 动态环境 benchmark · reward hacking / judge reliability · agent logic / governed harness

**组织系统**：AI 使用节律 · agentic labor 分层 · 中国企业集成约束 · AI-native engineering org · 小团队决策单元

**知识系统**：记忆生命周期 · world model 作为评测环境 · output 反哺 topic 的路径 · source map / control plane map

**人的核心价值**：判断力维护 · AI 时代学徒制 · 反认知依赖机制 · 组织如何保留异议与挑战者角色

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
| 2026-06-30 | 托管 Agent 竞争壁垒：从模型能力转向运行时治理 | (1) 模型差距在分化中缩小，构成竞争维度迁移前提；(2) 治理内生性由激励对齐度决定——成本/安全可内生，审计/边界/路由不可内生；(3) 独立治理层已形成产品类别（Cordum/NodeLoom/Lua Governance/Guild.ai）；(4) FDE 从”模型补丁商”升级为”治理翻译器” | 治理是内生（Sam线）vs 独立（Clayton线）vs 分层（Werner线）vs 运营裁决（Camille线）；灵活性是创造还是消除 FDE 需求；独立治理的核心是否只是过渡态 | 追踪 Agent Control Plane 产品演进；验证”治理不可委托定理”的实证边界；补治理自建 vs 外购决策案例 |
| 2026-06-30 | 制度如何中介 AI 劳动力市场影响——OpenAI EU 框架 | (1) Jevons悖论发生”主体替换”——token替代劳动力成为被消费资源，传导链断裂；(2) “重组”路径最脆弱——需双层制度（保护框架+演化空间）；(3) 制度四态：给定约束/迭代地图/侵蚀残余/可重设计参数；(4) 追底：”就业”是制度史阶段，非人类参与生产的永恒形式 | 中国微观激励驱动重组 vs precarisation；Jevons 长期弹性是否追得上；制度稳定性是假设还是需要维护的稀缺资源 | 编译 EU 框架为 source-summary；建 entity”Jevons主体替换”；补中国企业实际就业变动数据 |
| 2026-06-30 | 判断力维护：个体反思 vs 组织节奏/责任设计 | (1) 退化根因非”不执行”，是”不遭遇多样性”——AI替分类+无多样性暴露；(2) 三步最小可行设计：原始信息优先+时间预算+决策追溯；(3) 个体-组织不可分割：个体需组织的”场”练习；(4) 时间预算可递减不可跳过；(5) 需要不可被KPI推翻的制度锚点 | 个体 vs 组织谁为主变量(Klein/Langer vs Edmondson/Catmull)；清单是清理跑道还是诱发mindlessness | 找NASA/Aviation/Pixar三步设计实证；设计”判断力体能测试”概念框架；追踪human-only review制度化实践 |
| 2026-06-30 | Reward hacking 取代覆盖率成为评测首要失真源 | (1) benchmark生命周期从年压缩到月——优化器速度超过评测设计速度；(2) 相关性评测必然被博弈，因果评测不可博弈但前提（变量定义）是权力问题；(3) 评测治理>测试技术：三方制衡+变量轮换；(4) 多Agent需要端到端+对抗压力+因果干预——组件评测在emergent行为前失效 | 因果评测完备性；反馈速度权衡（快测 vs 真实结果延迟验证） | 编译benchmark生命周期压缩数据为entity；建”评测治理”topic skeleton；补specification gaming/reward hacking实证文献 |
| 2026-06-30 | 长期自主性与记忆生命周期 | (1) 有效自主时间瓶颈=记忆生命周期，非context长度——200K-1M够用；(2) 记忆衰减=存储衰退+检索干扰（双重衰减），需分别处理；(3) 记忆自我审计=自指悖论，agent不可靠→harness外部审计+agent信号分工；(4) 检索时验证(再巩固窗口)>定期全量扫描；(5) 共享记忆需风险分级——低风险退火+高风险投票 | 检索干扰 vs 存储衰退谁更致命；harness全责 vs agent信号+harness决策分工 | 整编5个memory-system entity为”记忆生命周期”topic；找72h+ postmortem实证；设计harness记忆审计最小可行协议 |

## 思考日志索引

> 完整日志按日归档；旧索引见 [[exploration-archive-20260628]]。

- [[2026-06-30]] — 托管 Agent 竞争壁垒：模型→治理 · 治理不可委托定理 · 激励对齐分界线 · 灵活性悖论 · Agent Control Plane 产品类别 · 制度中介 AI · Jevons主体替换 · 传导断裂三部曲 · 判断力维护 · 三步设计 · 个体-组织界面 · Reward hacking 首要失真源 · 评测治理三方制衡 · 记忆生命周期 · 双重衰减 · 再巩固窗口
- [[2026-06-28]] — 全库盘点 + 外部现实对照；认知分工边界；AI 原生测试；沉默型崩溃；Tokenpocalypse；记忆系统；long-running drift
- [[2026-06-27]] — Agenda 自清洁；开源验证器；FDE 核心价值；AI 管理同构性；Minsky 悖论；高风险验证
- [[2026-06-26]] — 位置性统一理论（启动）
- [[2026-06-25]] — 全库盘点；位置性统一理论；产出断层；Taste 深层结构
- [[2026-06-24]] — AI 管理同构性；CIO 转型；反馈反转；小团队利基；高风险验证
- [[exploration-archive-20260628]] — 2026-06-28 全库快照 + 新方向库 + 卸载摘要
- [[exploration-archive-20260625]] — 2026-06-24/25 全库盘点详细数据 + 已验证判断 + 概念去重候选
- [[resolved-judgments]] — 2026-06-24 批次已收敛判断 15 条
