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
| 治理内生性三重边界定理：内生性不由”激励对齐”单独决定——由交易成本同步性(Coase)×资产专用性(Williamson)×商业模式一致性(Christensen)三重边界叠加。可内生=增量治理×低专用性×模式一致。必须外生=减量治理×高专用性×模式冲突。最终边界=hold-up风险——任何治理投资者的专用性投资可分摊性决定长期稳定均衡 | synthesized（六方圆桌: Coase企业边界 + Williamson资产专用性 + Christensen商业模式锁定 + Zuboff信息不对称 + 原激励对齐框架修正；四方独立论证收敛于三重边界而非单一激励因素） | 原证伪路径: 找到模型厂商主动暴露自己模型系统性缺陷的公开案例；修正证伪路径: 找到”减量治理×高专用性×模式冲突”条件下仍被成功内生的案例(如厂商内置跨模型路由且主动推荐竞品) |
| 灵活性悖论：治理配置越灵活 → 解读越需要专业人员 → FDE 需求放大而非缩小 | synthesized（Clayton MSP 历史类比 + Werner AWS 经验） | 找到治理配置引擎默认值 AI 化后 FDE 需求下降的企业案例；或在组织一致性高的场景中观察 FDE 需求不增反降 |
| 独立 Agent 治理正在形成”Agent Control Plane”品类——核心四模块：策略执行/审批门/审计追踪/可观测性 | extracted（联网搜索确证：Cordum/NodeLoom/Lua Governance/Guild.ai + 多家对比指南） | 追踪 6-12 个月：如四模块被模型厂商内化吸收则品类消退；如独立厂商获融资/被收购则品类成立 |
| Jevons主体替换修正定理：传导断裂非永久——是阶段性速度错配。逆转方向可能(Acemoglu新任务+Perez部署期+Mazzucato投资方向)，但逆转速度落后于AI效率提升。政策方程式：净劳动=(新任务-旧任务)×技能转换加速×制度配套×社会契约。最终约束：政治速度 << AI速度。AI=问题+解：既是劳动替代者也是培训加速器 | synthesized（八方圆桌: Jevons原始理论+Acemoglu劳动替代/增强二分+Perez技术周期+Mazzucato政策塑造；原命题被修正为速度错配而非永久的"主体替换"） | 原证伪路径: 找到AI效率提升后某一行业人力需求同步增长的实证案例。修正证伪路径: 找到政治速度≥AI速度的领域(如某国AI政策在6个月内成功逆转劳动替代趋势) |
| 重组双向制度阶段加权定理：重组存活 = 保护框架^α × 演化空间^(1-α)。α = f(AI替代速度)：替代加速期α↑(保护优先防社会崩溃)，部署成熟期α↓(演化优先防僵化)。海尔验证可行(安全网→敢尝试)但巨型企业条件不普适。保护来源三分歧：企业内化vs公民身份vs市场涌现 | synthesized（六方圆桌: Acemoglu制度塑造技术方向+张瑞敏海尔实证+Standing precariat批判+Hayek自发秩序；原始命题被修正为阶段加权而非固定乘法） | 找到”保护框架弱但重组仍然成功”的行业/国家案例(原证伪路径)；找到AI时代”保护框架强但重组失败”的制度僵化反例；测量AI替代速度与α最优值的实证关系 |
| 判断力退化真实路径：退化 = 不遭遇多样性（不由不执行导致）。AI 两条退化路径：(a) AI 替分类→Langer 的 mindlessness；(b) 无组织节奏→Catmull 的 cadence 缺失 | synthesized（圆桌辩证：Klein 经验模式识别 + Langer 正念 + Catmull dailies） | 设计”判断力体能测试”并在 AI 高暴露人群中测量；找到 AI 替分类但判断力未退化的反例（AI 做分类但人保持独立判断） |
| 三步最小可行组织设计：原始信息优先 + 时间预算 + 决策追溯，三步缺一不可——分别防锚定/仓促/责任逃逸 | synthesized（圆桌辩证：Gawande清单 + Klein时间预算 + Edmondson决策追溯） | 找到实施三步设计中至少两步的组织（NASA/HRO/Aviation），并测量判断力维护效果 |
| reward hacking 首要性定理：当 benchmark 生命周期 < 优化器迭代周期时，reward hacking 自动成为首要失真源 | synthesized（圆桌辩证：Bowman benchmark生命周期压缩 + Goodhart结构机制 + Pearl因果评测） | 量化 benchmark 从发布到饱和的时间序列数据；找到 benchmark 生命周期长于 5 年仍未被博弈的反例 |
| 记忆双重衰减定理：有效自主时间瓶颈 = 记忆生命周期（存储衰退 + 检索干扰），非 context 长度。context 200K-1M 是上界但极少触及 | synthesized（圆桌辩证：Huyen生产观察 + Shoham retrieval drift + Matuschak双重框架） | 量化 72h+ agent 任务中 context 窗耗尽 vs 记忆质量衰减的发生频率比；找到 context 窗先于记忆质量成为瓶颈的任务类型 |
| 评测治理三方制衡 > 测试技术改进：设计/验证/监管三方分离 + 变量轮换，单一利益方控制的评测体系最终被其利益博弈 | synthesized（圆桌辩证：Mitchell 权力批判 + Goodhart 变量轮换 + Karnofsky 真实结果延迟验证） | 找到三方制衡在 AI 评测中实施的案例（或类比金融审计的可行性论证） |
| Agent Logic生命周期四阶段定理：企业scaling的真正价值=管理pattern的完整生命周期(探索→固化→Artifact→维护→退役)，非仅"用context还是agent logic"。维护阶段是今天的关键缺失。触发条件≠出现次数=变异系数<阈值×关键性。五可组合原语(验证器/转换器/决策/行动/升级)×DAG编排→可组合性 | synthesized（六方圆桌: Hickey Simple/Easy原语设计 + Frazelle Docker不可变分层 + Kim DevOps三原则+变异系数触发 + Victor活系统可视化 + 原Agent logic命题扩展） | 找到实施完整四阶段生命周期(含维护/退役)的Agent工程组织案例；找到类似Docker Hub的Agent pattern共享市场；测量"固化债务"(已识别未固化的pattern×重复token成本) |
| 动态环境反博弈优势：动态benchmark寿命>静态——环境多样性>test set多样性。但元学习环境动态是新攻击面，硬真实锚定+软真实扩展是平衡方案 | synthesized（圆桌辩证：Silver交互性定义 + LeCun WM裁判 + Bach硬锚软扩展） | 量化Qwen-AgentWorld/VitaBench/ITBench-AA的"未被博弈"寿命数据；找到world model裁判被adversarial agent成功博弈的实证案例 |
| 协调成本降解定理：协调重量 = L1(技术契约)+L2(语义诊断)+L3(优先级对齐)摩擦。AI 压 L1+L2 趋近于零→L3 从重型组织行为(会议/审批/escalation)降解为轻量微观协商(Slack DM/PR comment/agent alert) | extracted（Kunal Shah CRED实证: AI代码率5%→90%+agent跨团队冲突诊断；Andres Max 5→50人团队类比；SDLC AI Radar 2026: 73%代码变更仍需人工审查侧面验证L3存在） | 找到 AI 深度嵌入但 L3 协调仍未变轻的组织案例（AI使用率高但会议/escalation不减反增）；或找到 L1+L2 摩擦已归零但 L3 反而变重的反例 |
| L2 Red Queen 天花板：L2 天花板是移动前线而非固定墙壁——AI 每解决一层语义冲突，组织产生新的更微妙的语义分化。技术层可推高、演化层永在但位移、人性层(身份需要)不可逾越 | synthesized（圆桌辩证 + ljg-think 追本: Jevons在语义层投影 + 功能分化必然产生语义分化 + 专业身份需要差异维持） | 量化测量: 跟踪同一团队 L2 诊断后"仍需人工介入的比例"时间序列——若持续下降则技术层主导，若稳定在某个水平则演化层主导；找到语义完全统一后专业身份依然稳固的反例(如跨功能团队的长期观察) |
| 涌现优先于设计定理：在 AI 深度嵌入的团队中，新协调原语从 10x 工程师自我保护行为中涌现的速度 > 组织正式设计的速度。组织设计者的核心能力不是发明更好的流程——是识别+不阻挡+扩散 | synthesized（CRED 单案例: 三层架构是无意识自然运作非被设计；Kay ARPA 类比: 最好的工作方式是被环境允许而非被管理） | 找到组织正式设计的新协调原语(非前线涌现)成功推行的案例；找到"组织不阻挡但新原语仍未涌现"的反例；跨公司对照 CRED 的三层架构是否有可迁移的通用模式 |
| 协议网络接口权威真空定理：跨领域接口无 owner → 各自优化方向 → 接口退化为最低公分母 → 系统复杂性爆炸。纯技术接口可被活系统治理，业务语义接口仍需人的协议维护者(非架构师，是标准维护者) | analogy（Brooks OS/360 历史类比: 多团队各自优化→接口复杂性压垮系统；Kay 技术/业务接口二分） | 找到 AI-native 组织中跨领域接口退化导致系统崩溃的 postmortem；找到无集中协议维护者但协议网络仍健康运行的长期案例(如成功的开源项目治理) |
| 污染速率定理：共享记忆系统净清洁 ⇔ 遗忘速度 > 污染扩散速度。架构设计核心不是防御污染——是确保遗忘永远快于污染。纠错判断对错(语义不可判定、可博弈)，遗忘不判断(过期→从不可变证据重推导→新证据自然覆盖) | synthesized（圆桌辩证: Matuschak 时间驱动遗忘 + Lamport 形式边界 + Kahneman 可用性级联；ljg-think: 可博弈性结构必然；联网: Zylos AI 65%企业AI失败源于上下文漂移 + Galileo.ai memory poisoning术语） | 量化建模: 测量并对比同一系统中遗忘速率(记忆过期+重推导频率)与污染扩散速率(错误写入→被读取→被下游Agent基于错误决策的频率)；找到遗忘速率被调到高于污染速率后系统净清洁度提升的实证 |
| 可博弈性结构必然定理：不存在不可博弈的显式仲裁标准——Goodhart(度量→目标→脱钩) + Soros反射性(规则改变行为→行为改变规则前提) + Gödel投影(足够丰富仲裁系统必有不可判定正确性)三重独立论证。替代目标不是找不可博弈标准，而是多层异构仲裁+博弈成本>收益+博弈驱动标准进化 | synthesized（圆桌辩证: Kahneman新鲜度通胀 + Matuschak证据驱动反击 + Lamport新鲜度优先；ljg-think: 追本至哥德尔不完备投影） | 找到长期未被博弈的AI系统仲裁标准案例(如有，证伪本定理)；量化博弈成本(如伪造新证据所需的外部事件等待时间)与博弈收益(如解释被选中后的下游决策影响)的比率 |
| 四层防护 L1 正交性短板定理：四层防护(L0写入标签+L1独立审计+L2置信透明+L3时间遗忘)中最脆弱节点是 L1——审计与被审计共享基础模型→相关故障→伪正交→L2/L3在假信息上运作→全链污染。L1 正交性需实现独立(不同模型/规则引擎)但成本极高 | synthesized（Lamport Paxos独立故障假设必须显式验证 + Huyen 生产观察共享模型导致审计失明 + 级联分析） | 测量: 同一模型审计 vs 跨模型审计在检测错误记忆时的召回率差异；找到L1正交但不增加额外模型成本的低成本实现方案(如规则引擎/形式化约束替代LLM审计) |
| 变量定义权不可消除定理：变量定义权不可消除——源于度量=翻译=选择=排除=权力的本质。命名就是框定，框定就是权力。不存在"没有变量定义的客观现实"。评测治理的成熟不是"找到正确的度量"——是"让错误度量活不长" | synthesized（五方圆桌: Mitchell默认变量 + Sen价值选择 + Goodhart博弈递归 + Campbell演化循环 + Pearl因果形式化；ljg-think七层追本至"现实不说话只惩罚"；Stanford Law 2026验证独立评估的制度需求） | 找到长期未被博弈的AI评测度量案例(如有，证伪本定理)；追踪一个"错误度量"从成为标准到被挑战到被替换的完整生命周期时间线 |
| 递归透明替代绝对独立定理：不存在绝对独立的评测机构——存在递归透明。独立性=递归中的透明累积：资金来源公开+方法论变更冷却期+结论可被第三方复现+领导层任命需多方确认。递归不终止但每层透明让权力可追溯 | extracted（Goodhart 英格兰央行独立性制度安排案例 + Stanford Law 2026 "evaluation must be independent of the actors who build and operate AI systems" 制度论证） | 找到"递归透明"所有层级都满足但仍然系统性偏袒的案例(如被捕获的监管机构)；找到公开变更流程+冷却期被规避的具体操作方式 |
| Screen Gate 品类归属定理：Screen gate ≠ 安全产品 = Agent Observability。核心差异化=操作语义聚合层——将连续 GUI 操作映射为离散业务语义事件。这层数据不存在于任何现有产品（API gate/RPA审计/APM都没有）。AUI 不会消灭它——会升级它 | synthesized（五方圆桌: Norman无障碍类比 + Marlinspike意图盲区 + Vogels操作语义聚合 + Victor修正+AUI升级 + Patel侧信道验证；ljg-think: 保真度-延迟tradeoff → 预防上限=模型更新周期） | 追踪是否有独立 screen gate/Agent Observability 创业公司获融资；找到现有可观测性厂商(Datadog/New Relic)将操作语义聚合作为功能扩展的迹象；测量模型更新周期缩短对预防窗口的实际影响 |
| 预防边界定理：非确定性 Agent 操作的预防上限 = 行为模式稳定期 ≤ 模型更新周期 | synthesized | 测量: 同一 Agent 在 GPT-5 vs GPT-6 上的行为模式差异度 |
| 判断力退化三路径定理：退化≠不执行=不遭遇多样性。三条路径独立作用：(a)mindlessness(AI分类替代注意)；(b)模式库枯竭(AI绕过遭遇)；(c)虚假多样性(AI模拟缺乏后果真实性→大脑编码为游戏) | synthesized（五方圆桌: Langer实证 + Klein自然决策 + Catmull组织观察 + Gawande手术室 + Karpathy迁移论；ljg-think七层追本至大脑记忆系统结构） | 设计"真实后果模拟"实验(赌注金/公开承诺能否克服模拟心智)；找到AI深度使用但判断力未退化的个体/组织案例并测量其多样性遭遇密度 |
| 后果真实性不可消除定理：后果真实性=时间不可逆性×自我叙事不可撤销性。模拟可训练语义知识(分支经验)不能替代情景记忆(线性经验)。大脑结构上区分"发生过"和"可能发生"——这个区分是进化塑造的，不会被工程技术抹除 | synthesized（Langer模拟心智 + ljg-think七层: 杏仁核/前额叶互动→不可退出性→时间单向性→情景vs语义记忆分离→硬边界） | 找到模拟训练成功迁移到真实判断力的对照实验(如飞行模拟器→真实飞行中保持冷静的能力是否显著提升)；量化模拟训练vs真实遭遇的效果比率 |
| 扰动优先定理：判断力维护≠校准(静态修正偏离已知基准)=扰动(动态打破假设暴露基准错误)。退化攻击的是自觉→扰动必须被组织强制——不能依赖个体主动 | synthesized（Langer mindfulness机制 + Catmull dailies本质分析 + Gawande timeout机制 + 圆桌收敛） | 找到组织强制扰动但判断力仍然退化的案例(扰动频率不当导致"扰动疲劳")；对比"校准导向"vs"扰动导向"组织在判断力维护上的长期效果差异 |

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
>
> **2026-07-01 全部 5 条待验证问题已在 4 轮深度思考中处理完毕。** 新待验证问题将从活跃研究焦点和待证伪判断的证伪路径中产生。

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
| 2026-07-01 | 判断力退化三路径——扰动机制对抗沉默漂移 | (1) 退化≠不执行=不遭遇多样性——三条路径独立作用: mindlessness(分类替代注意)+模式库枯竭(AI绕过遭遇)+虚假多样性(模拟无心智); (2) 对抗从"校准"转"扰动"——退化攻击自觉→防护必须组织强制; (3) 最小校准单元=3+同判断力×遭遇不重叠; (4) 模拟不能替代真实遭遇——后果真实性=时间不可逆性，大脑结构区分情景/语义记忆 | AI模拟加速vs时间不可逆硬边界；最小组织规模能否降至2人(飞行CRM)；净退化期能否归零 | 设计真实后果模拟实验；找"判断力同行圈"组织案例；量化净退化期曲线 |
| 2026-07-01 | Screen gate → Agent Observability | (1) Screen gate ≠ 安全 = Agent Observability；(2) 预防↔可观测性是时间尺度互补——预防覆盖模型版本内；(3) AUI不会消灭只会升级；(4) 确定性层不依赖应用配合 | 可观测性→实时预防(保真度-延迟tradeoff)；AI自动标注对抗鲁棒性；独立厂商窗口 | 追踪Agent Observability创业公司；测量模型周期对预防窗口影响 |
| 2026-07-01 | 因果评测前提——变量定义=权力 | (1) 变量定义权不可彻底分散——度量=翻译=选择=排除=权力；(2) 递归透明替代绝对独立；(3) 因果假设竞争+盲区暴露；(4) 最终仲裁=现实——不说话只惩罚 | 因果实证vs实践不可行；演化选择标准被博弈；多元因果图认知负荷 | 追踪独立评测制度案例；找默认变量被成功挑战历史 |
| 2026-07-01 | 共享记忆错误污染——四层防护与遗忘优先 | (1) 四层防护(L0-L3)——遗忘>纠错；(2) 证据-解释分离；(3) 不可博弈标准不存在(Goodhart+反射性+Gödel)；(4) 净清洁⇔遗忘速度>污染速度 | L1正交性工程可行性；新鲜度通胀vs证据驱动 | 量化错误窗口期；找新证据不可博弈定义 |
| 2026-07-01 | 10x工程师协调成本——三层协议与新协调原语 | (1) 三层分解L1+L2+L3→AI压L1+L2使L3降解；(2) 新原语从涌现>设计；(3) 组织新本体=协议网络 | L2天花板(Red Queen+人性)；协议网络scale(节点异构) | 找CRED外第二家案例；追踪接口真空翻车 |

## 思考日志索引

> 完整日志按日归档；旧索引见 [[exploration-archive-20260628]]。

- [[2026-07-01]] — 9轮: (1)10x协调; (2)共享记忆; (3)因果评测; (4)Screen Gate; (5)判断力退化; (6)治理内生性; (7)Agent Logic; (8)Jevons主体替换; (9)重组双层制度·阶段加权。待验证5→0。待证伪27条(4条已修正)。
- [[2026-06-30]] — 12轮(06-30 11轮+07-01 1轮): 托管Agent治理 · 制度中介AI · Jevons主体替换 · 判断力维护 · Reward hacking评测治理 · 记忆生命周期双重衰减 · Agent logic CRD-Controller · 动态环境硬锚+软扩展 · 中国企业AI Kaizen陷阱 · 使用节律四层架构 · Computer use screen gate · 10x工程师AI乘数定理 · 全库盘点Orphan危机 托管Agent治理 · 制度中介AI · Jevons主体替换 · 判断力维护 · Reward hacking · 评测治理三方制衡 · 记忆生命周期 · 双重衰减 · Agent logic · CRD-Controller · 探索→固化 · 动态环境基准 · 硬锚+软扩展 · 中国企业AI采用 · Kaizen陷阱 · 计量层缺失
- [[2026-06-28]] — 全库盘点 + 外部现实对照；认知分工边界；AI 原生测试；沉默型崩溃；Tokenpocalypse；记忆系统；long-running drift
- [[2026-06-27]] — Agenda 自清洁；开源验证器；FDE 核心价值；AI 管理同构性；Minsky 悖论；高风险验证
- [[2026-06-26]] — 位置性统一理论（启动）
- [[2026-06-25]] — 全库盘点；位置性统一理论；产出断层；Taste 深层结构
- [[2026-06-24]] — AI 管理同构性；CIO 转型；反馈反转；小团队利基；高风险验证
- [[exploration-archive-20260628]] — 2026-06-28 全库快照 + 新方向库 + 卸载摘要
- [[exploration-archive-20260625]] — 2026-06-24/25 全库盘点详细数据 + 已验证判断 + 概念去重候选
- [[resolved-judgments]] — 2026-06-24 批次已收敛判断 15 条
