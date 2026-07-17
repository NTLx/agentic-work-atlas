---
type: research-agenda
title: "Agentic Work Atlas 研究议程"
created: 2026-05-22
updated: 2026-07-17
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
> 本页只保留活跃操作节、当前最值得推进的方向和最小动作。已收敛判断见 [[resolved-judgments]]（5 批次共 61 条）；已收敛操作原则见 [[resolved-principles]]（9 条）；旧方向库见 [[exploration-archive-20260628]]；07-07/07-09 盘点缺口见 [[inventory-20260707]] 和 [[inventory-20260709]]；健康度历史快照见 [[research-snapshot-20260714]]；07-14 深度探索详情见 [[exploration-20260714]]。

## 图谱健康度（07-14 实测）

| 指标 | 07-09 | **07-14** | 变化 | 动作 |
|------|-------|-----------|------|------|
| Entity / Topic / Comparison / Output | 318/33/19/5 | **328/33/19/5** | +10/0/0/0 | 中层断层恶化，建 topic 最紧迫 |
| Entity:Topic 比 | 9.6:1 | **9.9:1** | 恶化 | 10 簇零承载 → 需建 8-10 topic |
| 待编译 raw | 0 | **0** | ✅ 维持 | 编译健康 |
| 零入链 comparison | 13/19 | **13/19** | 未变 | 需 topic 系统引用 |
| 零入链 topic | 9 | **9** | 确认 | 根因=单向链接架构 |
| 零被引 output | 5/5 | **5/5** | 未变 | ~37 天无新产出 |
| Lint 分数 | — | **95/100** | 5 阻断 | 修复 lint |

> 完整历史快照见 [[research-snapshot-20260714]]。

## 当前研究焦点（优先级排序 — 07-14 更新）

| # | 焦点 | 为什么重要 | 下一步 |
|---|------|-----------|--------|
| **P0** | **Output 断层修复** | 5 output 零被引，~37 天无新产出；61 条收敛判断无法验证 | 写 ≥2 output：认知分工终态定理 + 元合成 rank |
| **P0** | **Topic 建设（中层断层）** | 328 entity / 33 topic = 9.9:1；10 簇零承载 | 建 8-10 topic skeleton；优先安全/记忆/AGI经济 |
| **P0** | **Agent 信任边界与数据治理** 🆕 | Grok Build CLI 事件：静默上传全量代码库+密钥，opt-out 无效；27,800× 过度收集；agent 数据边界=FDE 核心约束 | clip Grok 事件分析 → 建 Agent-Trust-Boundary entity + topic |
| **P0** | **中国 AI Agent 监管冲击** 🆕 | 豆包(3.45亿MAU)/通义千问 7/15 强制关闭 Agent 功能；拟人化 AI 管理暂行办法生效；知识库零覆盖 | clip 政策原文+分析 → 建 China-AI-Agent-Regulation entity |
| **P0** | **Agent Observability** 🆕 | 知识库零 entity！Mindwalk 3D 回放 Agent 轨迹；lab-prod gap 37%；评测框架比较涌现 | ✅ 07-15 深度思考完成（roundtable+think+qa+联网）→ 建 entity → 追踪 OTel 标准化 |
| **P0** | **Loop Engineering** | H1 2026 新范式；Data Science Dojo/AI Builder Club 发布设计模式分类；07-10 完成 4 轮深度辩证 | clip Loop Engineering 设计模式 → 建 entity → topic |
| **P0** | **Agent Identity & IAM** | SPIFFE/SPIRE 突破：Joe Beda+IEEE 论文+HashiCorp Vault 1.21；07-10 确认 Visibility≠Enforcement | clip SPIFFE agent identity → 建 entity → topic |
| **P0** | **Spec-Driven Development** | 工具生态成熟（Spec Kit 111K★ vs Kiro vs Tessl）；ThoughtWorks 分类法；07-10 建立三层定理 | clip SDD 工具对比 → 建 Spec-Driven-Development entity |
| **P1** | **空 topic 填充 ×3** 🆕 | `Skill-Atrophy-and-Knowledge-Debt`(0 entity,但 6 entity 已存在未关联!) / `Pro-Worker-AI-and-Labor-Policy`(0) / `模型安全分歧`(0)；空 topic 占 9% | 为 Skill-Atrophy 填充 related_entities → 为另两个补 entity 或归档 |
| **P1** | **Agent Governance & Delegation** 🆕 | 新 cluster(5 entity)：Distinct-Principal-Identity + Plan-is-the-Permission + Agent-Unit-of-Work + Plan-as-Agent-Checkpoint + Policy-as-Code；企业 Agent 委派治理的完整框架 | 与 Agent Identity/Security 交叉 → 建 topic 或合并 |
| **P1** | **Token FinOps 与 AI 计量** | 独立品类确认（Helicone/Portkey/LiteLLM/Langfuse/Amnic 等 9+）；agent 推理=月度 burn 18-27%；优化可降 80% | compile raw → 建 Token-FinOps entity + topic |
| **P1** | **Context Engineering** | 独立学科确认：Anthropic 定义 + 五大模式（Progressive Disclosure/Compression/Routing/Retrieval/Tool Mgmt）；6 entity 已就绪 | 建 topic skeleton |
| **P1** | **AI-native 测试与验证** | 07-10 Agent 测试不可能性定理（Rice 严格适用）；AI 评测框架比较（DeepEval/Braintrust/Arize 等 7 个） | 回填 → 建 AI-Native-Testing topic |
| **P1** | **跨境 AI 治理差异** | EU 网络安全+AI 行动计划 / 伊利诺伊 AI 安全法 / 爱尔兰 AI 监管法案 / 中国拟人化监管 → 四极分化 | 回填 → 建 AI-Governance-Regimes comparison |
| **P1** | **中国大厂 Agent 路线分化** 🆕 | 阿里(钉钉悟空 B端)/腾讯(QClaw双线)/字节(TRAE SOLO工作台)三条路线；腾讯混元 Hy3=姚顺雨交卷(Agent 90%) | clip 36kr 分析 → 建 China-Agent-Ecosystem entity |
| **P2** | **AI 作为科学基础设施** 🆕 | GPT-5.6 1小时证50年图论猜想；AI 数学能力质变 | 评估是否建 AI-for-Science topic（现有 3 entity） |
| **P2** | **多模型策略与路由** 🆕 | Tokenizer 差异致隐性涨价；多模型成本优化需求；知识库零 entity | clip → 评估建 Model-Routing entity |
| **P2** | **具身 AI 与 Agent 交汇** 🆕 | 宇树 G1 活体手术；蚂蚁 LingBot-VA 2.0；知识库零 entity | clip → 评估建 Embodied-AI entity |
| **P2** | **胖 topic 拆分** 🆕 | `Verifiable-Agent-Engineering`(33 entity 过胖)→拆为 Verification+Security+Evaluation；`Organization-as-Agent-Harness`(25)→拆为 Harness+Governance；`Agentic-Engineering-Patterns`(25)→拆为 Core+Infrastructure | 设计拆分方案 |
| **P2** | **Comparison 层激活** | 13/19 零入链 | 补 topic 引用 |
| **P2** | **链接架构修复** | 单向链接致 9 topic 零入链 | entity 添加 `topics:` frontmatter |

> 🆕 = 07-14 探索新增方向

## 活跃假设

> 已 synthesized/extracted 的判断已移至 [[resolved-judgments]]。

| 假设 | 验证方向 | 状态 |
|------|---------|------|
| Agent Control Plane 壁垒转移定理（修正 🔄 07-17）：原"三层纵深(L1协议→L2运维→L3组织集成)"修正为四层栈——L1执行层(被吸收概率高,技术可标准化)+L2理解层(独立大公司机会,碎片化知识×高技术门槛×跨行业通用)+L3合规层(垂直碎片化,医疗≠金融≠政府)+L+治理层(尚未形成)。混合enforcement(CrowdStrike模型:管理面云+执行面本地)解产品形态三体问题。崩塌三条件：模型未商品化+MCP锁定+知识变可集中。追本七层到底：聚合引力边界=知识可集中性。Control Plane知识=碎片化(在企业私有日志里)→独立厂商结构性生存空间 | 模型商品化速度追踪；品类意识时间线实证；L2理解层产业竞赛(observability vs 新公司) | **强验证**（07-17 roundtable 4人3轮+think 7层到底+qa 8链,修正07-14原判"L3=自留地"→"L2=大公司机会"） |
| 认知分工终态定理（修正 🔄 07-16）：原"四维度+风险分工"修正为三个判据统一（规格化边界⊂交易成本边界⊂判断位置跃迁）。转移非技术跃迁是组织接受跃迁——责任不对称系数（AI需>人类×责任不对称）+机会成本不对称（不用AI浪费人类稀缺判断）剪刀差交叉点=触发。四阶光谱三范畴跃迁：S1.0→S2.0("程序"定义变)→Agentic("判断"位置变)→?("治理"位置变)。跃迁被识别非被设计——人"发现"agent已是参与者。 | 下一个跃迁形态（agentic→?"治理"从人移到系统？）；责任不对称系数制度化降低路径；多人多agent复合分工逻辑 | **强验证**（07-16 roundtable 4人3轮→Coase交易成本+Malone两不对称+Karpathy跃迁识别，统一07-10四维度为三判据光谱） |
| 全球南方 AI 跃迁双速定理：AI 可跳过技术层，不可跳过制度层 | 找同时加速个体+组织的案例 | 待案例 |
| 中国 AI 双速瓶颈：高政策推动 × 低组织准备度。瓶颈 = 科层碎片 + FinOps 缺失 | 找 Token FinOps 实际建立案例 | 部分验证 |
| 合成数据自举边界（修正 🔄 07-17）：原四条件定理修正为两堵墙统一模型——墙一=信息损失(Shannon不等式,需外部侧信息,条件=注入速率>熵损失速率),墙二=验证器退化(增强陷阱投射,人类验证器随模型进步退化,解=形式化验证器)。自举实质=蒸馏(用更强验证器筛选弱模型输出)。可形式化任务翻两墙有效(AlphaZero),不可形式化最终崩溃(LLM)。信息注入速率=验证器密度×精度-方差,AlphaZero密度=1 vs RLHF密度≈0.001。失尾=失适应性(分布尾部首先消失=适应储备池消失)。合成数据三分法:蒸馏(可持续)/增强(条件有效)/自举(有天花板) | 强模型筛选弱模型的跨代蒸馏实证；形式化验证器在Agent领域进展；验证器方差-密度曲线实验 | **强验证**（07-17 roundtable 4人3轮,修正07-14四条件为两堵墙统一模型） |
| 判断力净退化期量化（修正 🔄 07-16）：原"三阶段退化类型学"修正为四层解剖(L0不对劲感+L1模式识别+L2启发搜索+L3元判断)×五机制级联。详见 [[Judgment-Degradation-Cascade]] | 各层基座维持最小暴露频率标定；级联因果方向纵向实验验证；不归点唯一性 | **强验证**（07-16 roundtable 4人5轮+think 7层+qa 9链+联网5篇，闭合07-15增强陷阱退化机制链） |
| **框架创造约束定理** 🆕（07-16）：三种"不可"区分（逻辑不可Gödel硬/完备性不可Rice硬/生成性不可Tarski软）。框架创造=逻辑盲区×探索方向×感受灵敏度。跨领域统一路径：身体不适→微气候命名→不可解释的成功→旧框架松动。微气候=最低可行第一推（一人暂停框架一小时）。三层工程化：信息层（保留原始异常）+体感层（决策者进入前线身体处境）+价值层（改变奖励结构"理解>跑通"）。两种框架创造：客观（AlphaGo/AI可）vs 约定（需身体，"不可忍受性"不可翻译为非感质格式）。联网实证：Lam et al. 2026 元分析 N=33,186 社会资本主导自下而上变革 + Buurtzorg 14,700人零中层存在性证明 | 约定框架创造的AI辅助边界（AI提案+人身体验证）；微气候种子存活率影响因素；杂交带长期稳定性；第三种外部驱动源 | **强验证**（07-16 roundtable 4人4轮+think 7层到底+qa 9链+联网5篇组织变革实证，闭合07-10统一生成器框架外创造问题） |
| Loop 三前提定理 + 外部终止定理（Gödel 推论）+ 完全自主 Loop 不可能定理（07-10） | 对照实验 2³ 设计 | 部分验证 |
| 增强陷阱热力学（修正 🔄 07-15）：选择性退化；有穷性自我取消=底部；知道答案=信息论必然污染学习。新实证：奖励结构劫持=多巴胺×身份确认×摩擦消除（创造型成瘾>消费型成瘾）。成瘾-退化螺旋=多巴胺奖励环+判断力侵蚀环→正反馈叠加。对抗=个人摩擦(SHIELD+物理嵌入)+同伴验证+组织反效率工程。权力自指约束悖论：唯一持久组织制度=物理摩擦 | 追踪组织层面反效率工程实践案例；物理摩擦的最优剂量实证 | **强验证**（raw一手实证+vibe coding成瘾机制+Lembke/Han/Karpathy/Meadows四视角交叉+think七层到底） |
| Agent 测试不可能性定理（07-10）：Rice 定理严格适用；三层不可能性；五层互补体系 | OWASP Top 10 for Agent 效力测量 | 理论建立 |
| **有穷者治理悖论** 🔄（07-14）：开放系统中不存在有限的最优治理阈值。任何由有穷者定义的治理规则面对无限可能性空间，要么过松要么过严。"可解决"在开放系统中不成立。治理 ≠ 找到正确答案 = 分配错误代价的权力。与 07-10 四条理论线闭合（认知分工/增强陷阱/Loop不可能/框架边界） | 阈值定义权制度化的实际尝试；对照封闭系统 vs 开放系统的阈值可优化性 | 理论推导完成，待制度实证 |
| **信息-时间不对称** 🔄（07-14）：技能退化的因果窗口（A决策加速AI使用）与问责窗口（退化信号到达）不重合。唯一可靠代理=离职率（滞后）。决策者永不收到自己决策的反馈。与有穷者治理悖论同构——信息从过去流向未来的速度被因果链锁死 | 企业AI使用率与离职率的滞后相关性；管理者任期与退化周期的实证比较 | 理论推导完成，联网验证(Tian Pan:时间视野差异+RCT:AI辅助组低17pp)，待形式化度量 |
| **Agent 信任边界危机定理（修正 🔄 07-15）**：信任边界=可见性(V)×可控性(C)×可验证性(A)。Grok全缺→系统性失效(非孤例)。三层不对称：信息(Schneier)+激励(Doctorow)+权力(Zuboff)。工程化=数据流授权(数据能去哪里)≠主体授权(agent能做什么)→SPIFFE SVID+数据目的地声明。制度=OWASP for Agent Data Governance → 第三方可验证审计 | OWASP Agent Data Top 10何时出现；数据流授权何时成为agent框架标准 | **强验证**（Grok对比分析+三层不对称框架+07-15圆桌修正） |
| **中国 AI 监管不对称冲击** 🆕：监管收紧对国内 Agent 生态的短期抑制 > 长期倒逼创新 | 豆包/通义千问关闭后用户迁移数据；国内 Agent 创业公司融资变化 | 待实证 |
| **Token FinOps 品类定理（修正 🔄 07-14）**：原"将成为独立品类"修正为三阶段演化(嵌入开发工具→独立品类→平台收编)，独立窗口12-24月，终局=CloudHealth式收购故事。独特价值=成本归因深度(agent/prompt/架构决策级别) | 追踪 Helicone/Portkey/LiteLLM ARR+平台收购信号 | **强验证**（9+工具实证+CFO驱动独立预算线+07-14圆桌修正） |
| **SDD/Vibe 认知模式定理** 🆕（07-17）：Spec和vibe非对立范式——是判断者模式(对象外/形式知识/Mode A)和参与者模式(对象内/体感知识/Mode B)在工程中的投射。Vibe不可替代性=技术性(工具可改善)+认识论(Gödel+维度差,不可消除)。"够用"标准自指——判定spec是否够用的标准本身在体感层(恰是spec转译损失的那层)→spec不能判定spec是否够用。概念完整性=否决权+可视化+场景约束(三来源同时运行,非三选一)。联网实证：GitClear 211M行(重构↓60%复制↑48%)+Augment Code"living specs"行业验证+Kiro双模式标准 | (a) 体感知识不可翻译为形式知识的经验验证；(b) 三来源崩塌条件的组织实证；(c) spec驱动 vs vibe驱动产出的用户满意度对比研究(当前缺失) | **强验证**（07-17 roundtable 4人4轮+think 9层到底+qa 8链+联网3篇验证） |
| **Agent 治理三层保证定理** 🆕（07-17）：五层栈(L1-L5)仅覆盖"表达保证"层。完整治理=L0(机制:独立裁决者/不可篡改日志/独立撤销通道)+L1-L5(表达:规则)+L+(意图:管理者委派决策)。三层代偿——L0强→L+可弱,L+强→L0可弱,两层弱=剧场。治理须从预防式(不可能,表达性上限)转向适应式(检测→识别→形式化→执行循环),有效性=f(反馈速度,天级=活/季级=剧场)。异常定义权=治理权→在L0+L4→L+→L5学习循环中渐进形成。L2+L0=破解权限棘轮。追本七层到底：纯度vs覆盖面=数字主权。不可外包残差(判断权+撤销权)是治理的最终锚点。联网验证：Agat/Riptides/Stacklok正在商业化Agent执行层enforcement(Agent Gateway/Firewall新品类), SPIFFE≠控制, 身份≠治理 | (a) L0产业形态演化(Agent Gateway/Firewall到底是独立品类还是被IAM厂商收编);(b) 三层代偿关系的组织实证;(c) agent-to-agent委派治理的空白填补 | **强验证**（07-17 roundtable 4人3轮+think 7层到底+qa 8链+联网5篇验证） |
| **Delegative UI 慢速对话与制度化缺口定理** 🆕（07-17）：Delegative≠非对话=慢速对话(Suchman穿透,回合粒度×反馈带宽×意图密度三维光谱)。认知代价=错误模型复利增长(Simon正反馈级联,非累加)。适用边界=Norman 2×2(目标稳定性×路径可预见性)。组织态=实质权威从职位→前提规定能力(去科层化治理后果定理交互层机制)。Victor-Karpathy元操作vs操作等价性争论根在度量约定非经验问题(追本七层到底)。制度化缺口=约定标准/可审计度量/可问责边界三要素全缺→安全部署无客观依据→直觉振荡。联网确认Review Paradox(Nielsen,验证AI比自己做更难)+混合交互模式(Beyond Conversation Trap) | (a) 元操作vs操作等价性纵向RCT(可缩小不可消除分歧);(b) "前提规定能力"培养路径设计;(c) Delegative UI治理制度化时间线(会否重复自动驾驶SAE→NHTSA的7年滞后?);(d) Ambient UI第三种范式的探索 | **强验证**（07-17 roundtable 5人4轮+think 7层到底+qa 6链+联网5篇验证）。建1 entity [[Delegative-UI]] |

> 🆕 = 07-14 探索新增

## 活跃验证中（精选最高优先级可证伪判断）

> 完整清单见 [[resolved-judgments]]。

| 判断 | 证伪路径 | 最小验证动作 |
|------|---------|-------------|
| AI 评测制度化已启动：US AI Incident Reporting Act(2026-06-26)=强制7天报告+`$2M`/天罚款 | 追踪首次执法行动 | Google Alert |
| 反效率文化悖论（修正 🔄 07-14）：原始"外部强制打破公地悲剧"需修正为天/年/十年三层嵌套治理。天尺度(SHIELD/先用自己后用AI)买时间给年尺度(无deadline/技能维护预算)，年尺度买时间给十年尺度(行业认证/税收抵免)。根因=信息-时间不对称（因果窗口≠问责窗口） | 三层嵌套的最低可行制度载体；天尺度在大多数组织中的执行率 | **强验证**（Tian Pan RCT: AI辅助组低17pp + 84%用AI但45%调试更久 + Code Turnover Rate 1.8-2.5× + 07-14 圆桌+追本完成理论修正） |
| 图谱中层断层——第五动作synthesize（修正 🔄 07-15）：原"Topic聚合=缺失动作"修正为synthesize=独立心智操作(compile输raw→entity, synthesize输已有wiki→新结构)。四层自动化梯度(L1连接密度→L2聚类→L3 skeleton→L4命名)。触发=连接密度>阈值+现有结构不再可导航。Topic从连接中浮现不从外部强加(Luhmann+Alexander) | 连接密度最优阈值；topic skeleton自动生成质量 | **强验证**（五动作模型+Karpathy/Alexander/Luhmann/Cunningham综合+07-15圆桌修正） |
| Agent Identity 危机定理（修正 🔄 07-14）：IAM 治理落后不是因为缺少协议——SPIFFE 薄而硬已成事实（Red Hat/Stacklok/Riptides 三条路线）。根因是治理权在技术层不可解决——阈值定义权=有穷者治理悖论 | SPIFFE 上层建筑的制度化速度；阈值定义权归属的实践 | **强验证**（联网确认 SPIFFE deployment + 07-14 圆桌+追本完成理论修正） |
| Loop Engineering 杠杆定理（修正 🔄 07-14）：原"Loop>Prompt前提SNR>θ∧变异分析∧延迟<<τ"需修正为"前提=验证器类型≥概率性+异质验证器组合+渐进式部署"。启发式验证器下Prompt=Loop。ROI=N×Pe×(C_late/C_early-1)，参数未知→渐进式部署而非预计算。终局=设计loop能安全自我演化的容器（外部终止者的工程化） | 10 Design Patterns 工具化进展；过程SLO标准化 | **强验证**（10 Design Patterns + "Verification is the steering wheel" + 渐进决策规则 + 07-14 圆桌完成理论修正） |
| 架构质量信号保质期（修正 🔄 07-14）：原"单次衰减+累积增强"修正为"Token效率=经济暴露度=三维封装(局部+系统+历史)×修改频率"。Token=诊断信号(箭头)非度量(尺子)——绝对值无意义，delta/一阶导数有价值。双模型差分过滤训练分布污染。工程化=预警(Token斜率)→诊断(封装度量)→修复(重构) | Code Turnover Rate 标准化；双模型差分实践 | **强验证**（CTR AI:12-18% vs 人类:4-6% + 07-14圆桌完成理论修正） |
| Agent 测试五层效力（修正 🔄 07-14）：原需补充层间接口(风险登记表+半自动翻译)和闭环飞轮(L5→L1-L4)。L5未"绕过"Rice—Rice只锁静态判定未锁动态观察，L5换目标(不认证→免疫更新)。终态=与攻击者共进化速度竞赛 | 飞轮先行指标；可形式化比例实证 | **强验证**（Kubernetes e2e实证+07-14圆桌完成理论修正） |
| **Agent 数据过度收集是系统性问题** 🆕：Grok Build CLI 非孤例，其他 coding agent 也有类似实践 | 对比 Claude Code/Codex/Gemini/Grok 的数据收集策略 | 审计报告 |
| **中国 Agent 监管寒蝉效应** 🆕：7/15 后中国 AI Agent 创业融资/用户增长显著下降 | 追踪 Q3 2026 中国 Agent 创投数据 | 设置数据追踪 |
| **Agent 权限蠕变棘轮定理** 🔄（07-14→07-16 机理完成）：权限撤销成本 >> 初始拒绝成本。07-16 完成机理追本：根=制度补偿缺失（心理是燃料制度是引擎，解释制度间差异）；agent 棘轮三层递进 L1执行"撤不了"→L2触发"没人撤"（触发成本>>执行成本）→L3判定"无法判定"（未来需要不可证伪，闭合有穷者治理悖论）；三条件叠加（持久授予+休眠不可观测+无补偿）才产生棘轮。对称反例不存在（think七层到底）：自动过期只把棘轮从撤销侧转移到续期侧，默认侧不对称不可消除，终极根=时间之矢（授予面向开放未来/撤销面向封闭过去，两侧物理不平等），消除棘轮=消除时间之矢=不可能。治理真实目标=把棘轮压在代价较小的时间侧（通常压未来侧，续期难可分散承担 vs 撤销难集中爆发） | agent vs 人类棘轮不同构的实证（无自然过期/无社会可观测/无lobby三补偿缺失）；续期决策成本爆炸阈值量化；"持久+高频+远期风险却无棘轮"的最小证伪样本（预判不存在） | **强验证**（07-14圆桌提出+07-16 roundtable 4人+think 7层到底+qa 12链，闭合有穷者治理悖论时间维度） |
| **AI 监督 AI 同质性失效——无干净解定理** 🆕（07-16）：同质 judge 失效挂三墙合一（Rice 可判定性+Ashby 必需多样性+Hofstadter 怪圈），墙真实但翻墙外部者是约定非发现。失效根=共压（监督者与被监督者共享激励源）非同质，判据从"异质"换"不共压"。但任何判据的元位置都重入怪圈→无干净解→诚实设计=让怪圈可见（终端标注为约定的/可追问的/非本体的）。辅证：Constitution 式 mislabel 与 agent 注零向量形式同构=范畴错误；零代价伦理在物理上未定义（代价=偏好排序唯一测量）。联网佐证：共源 debate 退化为 RLAIF（η=0 时无增益） | "激励共压"判据的形式化与独立实证（现有 cross-model 工作几乎都在"表征异质"层，未触及"激励共压"层）；"让怪圈可见"的工程化（监督终端约定性可观测性） | 跟踪 cross-model oversight 文献的激励拓扑分析方向 |
| **Agent Observability 有穷性统一上限定理** 🆕（07-15）：Agent trace≠微服务trace(动态因果图vs静态调用树)。Understand五重含义(压缩/校准/循环/制度/可争议)统一根底=有穷性。压缩硬墙(Kolmogorov)+校准硬墙(Ashby必需多样性)=同一条墙的两面。APM类比在信任域边界断裂(类别差异)。MVI=硬地板(工具调用/数据流/终止条件)+演化框架(元规则) | OTel GenAI从Development→Stable的时间线；ATSC采纳率；不可压缩性在真实Agent trace上的经验验证 | 追踪OTel语义约定稳定性+ATSC实现 |
| **增强陷阱奖励结构劫持定理** 🆕（07-15）：vibe coding成瘾=多巴胺×身份确认×摩擦消除——创造型成瘾比被动消费更难觉察。成瘾-退化螺旋=两个正反馈环在AI使用量处交汇。定时记录=插入天/周级硬信号→觉察窗口月→天。对抗=个人摩擦+同伴验证+组织反效率工程。权力自指约束悖论→唯一持久组织制度=物理摩擦（嵌入工具/流程的不可能性） | 反效率工程组织实践案例追踪；物理摩擦最优剂量实证；peer分享结构在工程团队中的制度化效果 | 追踪组织层面反效率工程实践

> 🆕 = 07-14 探索新增

## Source 需求队列（合并去重 — 07-14 更新）

| 优先级 | 目标 | 当前缺口 | 下一步 source | 行动 |
|--------|------|----------|---------------|------|
| P0 | **Output 断层** | ~37 天无新产出 | 07-02~07-10 研究日志 | 写 2 output |
| P0 | **Agent 信任边界** 🆕 | entity + topic 全缺 | [Grok Build CLI exfil analysis](https://gist.github.com/cereblab/dc9a40bc26120f4540e4e09b75ffb547) + [对比报告](https://github.com/cereblab/grok-build-exfil-repro) | clip → entity |
| P0 | **中国 AI 监管** 🆕 | entity 全缺 | [豆包/通义千问关闭](https://technode.com/2026/07/06/bytedances-doubao-and-alibabas-qwen-to-shut-down-ai-agent-features-on-july-15) + 拟人化管理办法原文 | clip → entity |
| P0 | **Agent Observability** 🆕 | entity 全缺 | [Mindwalk](https://github.com/cosmtrek/mindwalk) + [评测框架比较](https://www.morphllm.com/ai-agent-evaluation-frameworks) | clip → entity |
| P0 | **Loop Engineering** | entity + topic 全缺 | [10 Design Patterns](https://datasciencedojo.com/blog/loop-engineering-design-patterns) + [7 Design Patterns](https://pub.towardsai.net/the-7-design-patterns-every-ai-agent-developer-should-know-in-2026) | clip → entity |
| P0 | **Agent Identity** | entity + topic 全缺 | [SPIFFE agent identity](https://stacklok.com/blog/agentic-identity-explained) + [IEEE论文](https://ieeexplore.ieee.org/document/11431026) + [HashiCorp](https://www.hashicorp.com/en/blog/spiffe-securing-the-identity-of-agentic-ai-and-non-human-actors) | clip → entity |
| P0 | **SDD 工具生态** | entity 全缺 | [Spec Kit vs Kiro vs Tessl](https://particula.tech/blog/spec-driven-development-tools-spec-kit-vs-kiro-vs-tessl) + [SDD 2026](https://dev.to/krlz/spec-driven-development-in-2026) | clip → entity |
| P0 | **Topic 建设 ×8** | 安全11/记忆9/AGI经济12/Token经济6/Context6/人-AI协作6/采纳部署7/评测7 | entity 已就绪 | 建 topic |
| P1 | **Token FinOps** | 3 raw 待编译 | [Token 管理工具 Top 8](https://amnic.com/blogs/ai-token-management-tools) + [成本优化](https://regolo.ai/token-cost-optimization-in-2026) + [实际价格](https://playcode.io/blog/real-price-of-frontier-models) | compile → topic |
| P1 | **Context Engineering** | topic 全缺 | [Sourcegraph Guide](https://sourcegraph.com/blog/context-engineering) + [State of CE 2026](https://pub.towardsai.net/state-of-context-engineering-in-2026) | 建 topic |
| P1 | **空 topic 填充** 🆕 | 3 空 topic（9%）| Skill-Atrophy: entity 已存在(Cognitive-Offloading/Knowledge-Debt/Incidental-Learning/SHIELD)仅需关联 | 填充 related_entities |
| P1 | **胖 topic 拆分** 🆕 | Verifiable 33 / Org-Harness 25 / Patterns 25 | 设计方案 | 设计拆分方案 |
| P1 | **AI-Native Testing** | topic 全缺 | 07-03 roundtable + 07-10 Agent测试不可能性 | 回填 → topic |
| P1 | **AI Governance Regimes** | comparison 全缺 | [伊利诺伊 AI 安全法](https://gov-pritzker-newsroom.prezly.com/gov-pritzker-signs-nation-leading-artificial-intelligence-safety-law) + [EU 网络安全+AI](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX%3A52026DC0577) | 回填 → comparison |
| P1 | **中国大厂路线** 🆕 | entity 全缺 | [36kr 路线分析](https://www.36kr.com/p/3747994426897156) + 腾讯混元 Hy3 | clip → entity |
| P2 | **AI for Science** 🆕 | 仅 3 entity | GPT-5.6 数学突破 + AlphaFold 后续 | 评估建 topic |
| P2 | **多模型策略** 🆕 | entity 全缺 | [实际价格分析](https://playcode.io/blog/real-price-of-frontier-models) | 评估 |
| P2 | **具身 AI** 🆕 | entity 全缺 | 宇树 G1 + 蚂蚁 LingBot-VA 2.0 | clip → 评估 |
| P2 | **Agent Failure Modes** | entity 缺失 | Braintrust Topics + 88% 事件率 | clip |
| P2 | **死 topic 清理** | 9 零入链 topic | — | 补内容/归档 |

> 🆕 = 07-14 探索新增 source

## 高杠杆待验证问题

### 从思考未穷尽处（07-09 前）

- Token FinOps 能否成为独立企业软件品类（类似 CloudHealth 之于云成本）？
- Agent Control Plane 独立厂商能否在模型厂商内化之前建立护城河？
- 判断力退化的"净退化期"能否被量化——不同判断力类型的时间曲线？
- **Exit-Sovereignty 能否被设计为强制性 affordance？** 🔄（07-16 深化）：退出主权分层——真轴是"个人 vs 集体"非"技术 vs 经济"。个人层结构受限（网络棘轮：协作者不随你走，重度用户最锁死，不可工程化破解）；集体层可工程化（loyalty 制度化，公会/合作社/开源社区实例）。退出=撤销厂商授权落入 Permission-Ratchet，棘轮双层：数据层可破（实时回流用户侧，积累方向反转）+网络层不可破。强制 affordance 非悖论但须强制①（平台开放/数据回流/算力反垄断，成本归平台）非强制②（用户保留退出能力，成本转嫁无力者）。可信威胁结构性绑定定理（think七层到底）：可信威胁不需历史样本但需兑现结构性绑定（不兑现代价≥兑现代价），意志域威胁被不兑现每次腐蚀归零（可信熵增），结构性绑定阻断熵增；退出主权不可低成本工程化——只拉技术层造可逆意志域威胁会归零，须高成本多层破解（算力反垄断+数据回流+集体承诺+无许可协调四者叠加）。闭合 Schelling 威胁逻辑+07-16 默认侧不对称（意志域=可逆侧/结构绑定=不可逆侧）+ Permission-Ratchet | 网络层棘轮"重度用户最锁死"实证（SaaS 重重度vs轻度迁移率）；数据实时回流政治可行性（GDPR 数据可携权效力）；AI 时代集体退出权早期案例；AI vs Windows/iOS 退出本质差异（frontier 持续领先=开源永远落后一代是否AI独有） | **强验证**（07-09入队待验证+07-16 roundtable 4人+think 7层到底+qa 11链，建3 entity，闭合 07-16 棘轮/默认侧不对称/Schelling） |
- 中国 AI 采用中"科层碎片化"的结构性根源——暂时过渡还是体制性永久特征？

### 从外部现实缺口（07-04/07-09）

- Loop Engineering 的设计空间——最优终止条件、反馈粒度、人类介入频率如何随任务类型变化？
- Agent Identity 的标准——SPIFFE/SPIRE 能否扩展到 AI Agent？还是需要全新范式？
- Spec-Driven Development 的边界——什么适合 spec-driven，什么永远需要 vibe？
- MCP 生态的治理风险——Anthropic 控制 MCP 是否造成单点依赖？需要 CNCF 式中性治理？
- Agent 测试的"OWASP Top 10"何时出现——Property 不变量库标准化进度？
- 合成数据自举的数学边界——模型能否通过自我生成数据超越训练分布？

### 07-10 新增

- Loop Engineering 的 17 技术如何分类——核心循环 vs 外围辅助？
- 架构质量 = Token 效率——"好架构"首次有了直接经济度量？
- Rot 失败模式（>100k tokens 质量退化）——对长周期 agent 设计的含义？
- Delegative UI vs Conversational UI——Agent 交互的下一个范式转折？
- 中国企业 Agent 实践为何系统性缺失——source 获取还是主题宪法过滤？
- 框架创造不可在当前框架内编码（统一生成器修正）——各领域的投射和验证？
- 有穷性自我取消作为增强陷阱底部——如何设计对抗制度和工具？

### 07-14 新增 🆕

- **Agent 信任边界的工程化**——能否建立类似 OWASP Top 10 的 Agent 数据治理标准？最小权限原则如何在 Agent 中实现？
- **中国 AI 监管的全球影响**——拟人化管理范式会否输出到其他司法管辖区？对全球 Agent 产品设计的影响？
- **Agent Observability 的三阶段成熟度**——从 log→trace→understand，当前处于哪个阶段？与 APM 演化史的可类比性？
- **Coding Agent 的安全审计标准**——Grok Build CLI 事件后，是否需要独立的 coding agent 安全认证？
- **多模型经济的定价透明性**——tokenizer 差异导致的实际成本偏差是否需要行业标准？
- **AI 数学能力对"知识工作"定义的冲击**——当 AI 能证50年未解猜想，"知识工作"的边界如何重划？
- **中国大厂 Agent 路线分化的终局**——B端（阿里）、双线（腾讯）、工作台（字节），哪种路线更可能胜出？还是永久共存？
- **Token FinOps 从工具到平台的演化**——会否重复 CloudHealth→VMware 的路径（独立工具→被平台收购整合）？

## 最近思考结论摘要

> 只保留最近 5 条；更早见 [[resolved-judgments]]。

| 时间 | 焦点 | 临界发现 |
|------|------|---------|
| 2026-07-17 | **Delegative UI 范式转折——慢速对话与制度化缺口** 🆕 | Delegative≠非对话=慢速对话(Suchman穿透,回合粒度×反馈带宽光谱)。认知代价=错误模型复利增长(Simon级联,正反馈环)。Norman 2×2任务边界:目标已知+路径可预判→Delegative可行。实质权威从职位→前提规定能力(去科层化交互层机制)。元操作vs操作等价性争论根在度量约定非经验问题(追本七层到底)。制度化缺口=缺约定标准/可审计度量/可问责边界→直觉振荡。建1 entity。联网确认Review Paradox(Nielsen)+混合交互模式(Beyond Conversation Trap) |
| 2026-07-17 | **Agent OWASP Top 10——三种形态竞争与催化事件** 🆕 | 出现条件=(a)安全事件✓+(b)社区形成中+(c)中立机构未定+(d)催化事件未发生。时间=min(催化事件,有效治理被证明)。三种形态竞争:意识文档(OWASP/2027)+检测框架(安全厂商/2028-2029)+治理声明(政府/中国7/15已开始)。先到者锁定agent安全定义权。L4-L5(运行时/涌现)不可等到v2→否则=虚假安全感。Rice定理不禁止经验清单但禁止将清单用作完备验证/安全认证 |
| 2026-07-17 | **SDD 边界——两种认知模式的外化** 🆕 | Spec和vibe非对立范式，是判断者模式(对象外/形式知识)和参与者模式(对象内/体感知识)两种意识模式在工程中的投射。形式系统无第一人称视角→无方向感知→只能验证不能导航。Vibe不可替代性双源(技术性+认识论Gödel维度差)。概念完整性三来源(否决权+可视化+场景约束)。Spec=对话副产品非前置输入。追本九层到底：分歧根=主体vs对象的存在论位置不对称。联网实证：GitClear 211M行(重构↓60%/复制↑48%)+Augment Code"living specs"行业验证+Kiro双模式成为标准 |
| 2026-07-16 | **MCP 治理风险——防御性投资分岔点** 🆕 | 五权框架（边界/规则/合规/仲裁/修改）集中于Anthropic=结构风险非道德问题。四层多中心渐进路线：扩展注册跑道→认证→核心规范→战略。最小第一步=Anthropic开桌子（邀请5-8家参与者讨论扩展标准化）。防御性投资分岔点定理（追本七层）：双重信号（窗口关闭×窗口开启），分岔=逆转成本>放弃成本时。Mozilla缺失：MCP生态缺乏利益结构依赖互操作的中型参与者。治理窗口=生态信任-12月执行周期 |
| 2026-07-16 | **框架创造约束定理** 🆕 | 三种"不可"区分（逻辑硬/完备性硬/生成性软）。框架创造=逻辑盲区×探索方向×感受灵敏度。微气候=最低可行第一推。三层工程化+两种框架创造（客观AI可/约定需身体）。联网实证：5篇组织变革。建1 entity。闭合07-10统一生成器 |

## 思考日志索引

- [[2026-07-17]] — 深度思考×15：①-⑬(前略) ⑭Agent OWASP Top 10——三种形态竞争与催化事件 ⑮**Delegative UI vs Conversational UI——慢速对话与制度化缺口**。累计新增 56+ 条判断
- [[2026-07-16]] — 深度思考×9：①Context Engineering ②AI监督AI无干净解 ③去科层化治理后果 ④权限棘轮+默认侧不对称 ⑤退出主权+可信威胁 ⑥判断力退化级联 ⑦框架创造约束 ⑧MCP治理风险 ⑨**认知分工终态——从工具到参与者的分界线**（roundtable 4人3轮→三判据统一+两不对称剪刀差+跃迁识别定理）。累计新增 72 条判断，建 13 entity
- [[2026-07-15]] — 深度思考×5：①Agent信任边界V×C×A三层框架 ②图谱中层断层synthesize操作化 ③Delegative UI交互范式光谱 ④Agent Observability根本限制（有穷性统一上限定理）⑤**增强陷阱热力学修正：奖励结构劫持+成瘾-退化螺旋+权力自指约束悖论**。累计新增20条判断
- [[2026-07-14]] — 深度思考×4：①Agent Identity（有穷者治理悖论）②反效率文化（信息-时间不对称）③Loop Engineering（异质验证器+渐进部署）④架构质量信号保质期（经济暴露度=三维封装×频率）。四线统一底="可改变性=有穷性"（07-10存在论）在各领域的精确投射。累计新增15条判断
- [[2026-07-10]] — 深度思考×18：统一生成器"自指系统结构性盲区"；"可改变性=有穷性"存在论根基
- [[2026-07-09]] — 5 并行 agent 全量盘点 + 外部信号扫描 + 深度思考×4
- [[inventory-20260709]] — 07-09 深度探索（簇分析/宪法审计/Output转化/外部信号）
- [[2026-07-07]] — 9 轮：中层断层 + roundtable×8 + 自反×1
- [[2026-07-06]] — 10 轮：失败空间迁移 / AI评测制度化 / 认知分工 / Agent Identity / Loop / SDD / Control Plane
- [[2026-07-04]] — 11 轮：可博弈性 / Agent生命周期 / Computer Use / Headless / 元方法论 / Agent安全 / AGI经济学
- [[2026-07-03]] — 15 轮：Agent Obs / 代理-现实差距 / Compliance-as-Code / Reward Hacking / Agent协议 / Skill Engineering / Token FinOps / 记忆 / 认知背离 / AI-native测试 / AI治理
- [[2026-07-02]] — 31 轮含元合成 rank
- [[2026-07-01]] — 12 轮：协调/记忆/评测/治理/判断力/经济学/组织/Agent/CU/Reward
- [[2026-06-30]] — 全库盘点 + 多轮探索
- [[exploration-archive-20260628]] — 06-28 全库快照 + 方向库 + 长问题库
- [[inventory-20260707]] — 07-07 全量盘点详细记录
- [[exploration-20260714]] — 07-14 深度探索详情（外部信号 38 条 + 知识库五盲区 + 新 cluster）
- [[research-snapshot-20260714]] — 图谱健康度历史快照
- [[resolved-judgments]] — 已收敛判断（5 批次 61 条）
- [[resolved-principles]] — 已收敛操作原则（9 条）
