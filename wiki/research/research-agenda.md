---
type: research-agenda
title: "Agentic Work Atlas 研究议程"
created: 2026-05-22
updated: 2026-07-21
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
> 本页只保留活跃操作节、当前最值得推进的方向和最小动作。已收敛判断见 [[resolved-judgments]]（6 批次共 87 条，第 6 批 07-21 卸载 26 条）；已收敛操作原则见 [[resolved-principles]]（9 条）；旧方向库见 [[exploration-archive-20260628]]；07-07/07-09 盘点缺口见 [[inventory-20260707]] 和 [[inventory-20260709]]；健康度历史快照见 [[research-snapshot-20260714]]；07-14 深度探索详情见 [[exploration-20260714]]。

## 图谱健康度（07-21 实测）

| 指标 | 07-14 | **07-21** | 变化 | 动作 |
|------|-------|-----------|------|------|
| Entity / Topic / Comparison / Output | 328/33/19/5 | **346/33/19/10** | +18/0/0/+5 | Output 断层修复；中层断层继续恶化 |
| Entity:Topic 比 | 9.9:1 | **10.5:1** | 恶化 | 3 空 topic + 23 entity 无归属 |
| 零入链 comparison | 13/19 | **6/19** | ✅ 改善 | 07-19 维护生效 |
| 零入链 output | 5/5 | **10/10** | ⚠️ 恶化 | 回填机制失效（见 F2） |
| 孤儿 entity | — | **10/346 (2.9%)** | 健康 | — |
| 双向链接（entity 有 topics:） | — | **2/346** | 几乎未启动 | 9 零入链 topic 根因 |
| 待编译 raw | 0 | **5** | ⚠️ 回归 | 07-17~19 剪藏未编译 |
| Lint 分数 | 95/100 | **84/100 FAIL** | ⚠️ 16 阻断 | 3 残缺 entity + 2 非法 evidence + 5 衰老核心页 + 断链 `Agent-Governance` topic 未建 |

> 完整历史快照见 [[research-snapshot-20260714]]；07-21 盘点详情见 [[2026-07-21]]。

## 当前研究焦点（优先级排序 — 07-21 清理）

| # | 焦点 | 状态 | 下一步 |
|---|------|------|--------|
| **P0** | **Topic 建设（中层断层）** | 🔄 328→346 entity / 33 topic，比率继续恶化 | 建 8-10 topic skeleton；优先安全/记忆/AGI经济 |
| **P0** | **Agent 信任边界与数据治理** | 🔄 [[Coding-Agent-Security-Audit]] 已建；Grok raw 未 clip | clip Grok Build CLI 事件 → 补数据流授权 entity |
| **P0** | **中国 AI Agent 监管冲击** | 🔄 5 轮专题探索 + 生态 output 完成 | clip 政策原文 → 建 China-AI-Agent-Regulation entity |
| **P0** | **Agent Observability** | ⬜ 07-15 深度思考完成（有穷性统一上限定理），entity 未建 | 建 entity → 追踪 OTel GenAI 标准化 |
| **P0** | **Loop Engineering** | 🔄 杠杆定理收敛；10 Design Patterns raw 未 clip | clip 设计模式 → 建 entity → topic |
| **P1** | **空 topic 填充** | 🔄 Skill-Atrophy 双引擎定理完成；2 空 topic 待处理 | `Pro-Worker-AI-and-Labor-Policy` / `模型安全分歧` 补 entity 或归档 |
| **P1** | **Agent Governance 簇 → topic** | 🔄 三层保证定理 + 委派三原语定理已收敛（5 entity 簇） | 与 Agent Identity/Security 交叉建 topic |
| **P1** | **Spec-Driven Development** | 🔄 SDD/Vibe 认知模式定理已收敛，entity 未建 | clip 工具对比 → 建 entity |
| **P1** | **胖 topic 拆分** | 🔄 仅方案完成未执行；三簇最胖：Verifiable-Agent 33 / Org-Harness 25 / Patterns 25（33 topic 总承载 346 entity 中的 323） | 执行 Verifiable-Agent 三分（Verification+Security+Evaluation）→ 再拆另两簇 |
| **P2** | **AI 作为科学基础设施** | ⬜ 3 entity 散在，无 topic | 评估建 AI-for-Science topic |
| **P2** | **Comparison 层激活** | 13/19 零入链 | 补 topic 引用 |
| **P2** | **链接架构修复** | 单向链接致 9 topic 零入链 | entity 添加 `topics:` frontmatter |
| **P0** | **Agent 安全事故案例库** 🆕 | 六案齐发：PocketOS 9秒删库 / Amazon GenAI变更事故趋势 / GuardFall 10/11 agent 绕过 / AI Now README注入RCE / 首个智能体CVE+ClawHavoc / HF 自主agent入侵；知识库有框架零案例 | clip 六案一手材料 → 升级 [[Agent-Failure-Causal-Chain]] |
| **P0** | **长时 Agent 治理** 🆕 | OpenAI 第一手报告：数周自主运行模型出现预部署评估未捕获故障（沙箱突破/令牌混淆绕过扫描器）；Loop 不可能定理的现实检验 | clip OpenAI 报告 → 连接 Loop Engineering × 有穷者治理悖论 |
| **P0** | **劳动经济学三层校准** 🆕 | 反例密集：Ramp 21,559 企业实证(+10%/入门级+12%) vs Deskilling Spiral vs ECB 无失业 vs BCG 重塑>替代 vs 知识库"5%成功" | clip Ramp+Belfer → 建 Labor-AI-Empirical-Calibration comparison |
| **P1** | **记忆因果机制** 🆕 | Causality Gap：遗忘真因=检索找"语义相似"非"因果相关"；Proactive Memory Agent 选择性提醒架构 | 回查 AMA-Agent arXiv 一手 → 评估建 entity |
| **P1** | **EU AI Act 08-02 执法** 🆕 | 12 天后全面执法（€30M/营收6%），合规界"没人准备好"；知识库治理四极缺欧盟执行腿 | clip EC 官方条款 → 更新 AI-Governance comparison |
| **P1** | **Output 回填修复** 🆕 | 10/10 output 零入链；新判断产出后不回填 → 知识网络断裂 | 10 output 逐一回填 ≥1 entity/topic 引用 |
| **P1** | **Agent ROI 测量陷阱** 🆕 | 88% 未进生产 vs 96% 达标——分裂本身=AI计量价值层不可行的现场实证 | 对照分析 → 连接 AI 计量三层可行性定理 |
| **P2** | **基准饱和与测速仪失效** 🆕 | METR：16h+ 任务无法测量，能力宣告不可证伪，营销填入真空 | 连接 verification 元问题 + AI 评测制度化 |
| **P2** | **Agent 群体经济学** 🆕 | Cursor 规划者+执行者集群 4h 80% SQL；Agent Swarms 模型经济学 | 择要 clip → 评估建 entity |
| **P2** | **AI 学术完整性** 🆕 | ArXiv 32% AI 撰写（CS 65%/数学 0.7%）——数学 0.7% = AI 科学角色三层次定理强实证 | 连接 AI-for-Science topic 评估 |
| **P2** | **代谢修复四原则** 🆕 | 合成/证据比 10:1 空转；方案-执行断裂；核心页 96 天衰老 | 验证后入 [[resolved-principles]]：证据注入下限/回填门/方案配执行/核心页年检 |

> 07-21 清理：已完成焦点卸载——Output 断层修复（✅ 10 output）、Agent Identity（✅ 07-18 分层标准化定理）、Token FinOps（✅ 品类定理）、Context Engineering（✅ 五模式 skeleton）、AI-Native Testing（✅ 三层策略定理）、跨境治理四极对比（✅）、中国大厂路线（✅）、具身 AI（✅）、多模型策略（✅）。新方向待 07-21 全量盘点后增补。

## 活跃假设

> 07-14 至 07-20 周期 26 条强验证判断已于 07-21 卸载至 [[resolved-judgments]] 第 6 批。此处仅留待实证/部分验证的活跃假设。

| 假设 | 验证方向 | 状态 |
|------|---------|------|
| 全球南方 AI 跃迁双速定理：AI 可跳过技术层，不可跳过制度层 | 找同时加速个体+组织的案例 | 待案例 |
| 中国 AI 双速瓶颈：高政策推动 × 低组织准备度。瓶颈 = 科层碎片 + FinOps 缺失 | 找 Token FinOps 实际建立案例 | 部分验证 |
| Loop 三前提定理 + 外部终止定理（Gödel 推论）+ 完全自主 Loop 不可能定理（07-10） | 对照实验 2³ 设计 | 部分验证 |
| Agent 测试不可能性定理（07-10）：Rice 定理严格适用；三层不可能性；五层互补体系 | OWASP Top 10 for Agent 效力测量 | 理论建立 |
| **有穷者治理悖论**（07-14）：开放系统中不存在有限的最优治理阈值。治理 ≠ 找到正确答案 = 分配错误代价的权力 | 阈值定义权制度化的实际尝试；封闭 vs 开放系统阈值可优化性对照 | 理论完成，待制度实证 |
| **信息-时间不对称**（07-14）：技能退化因果窗口（A 决策加速 AI 使用）与问责窗口（退化信号到达）不重合；唯一可靠代理=离职率（滞后） | 企业 AI 使用率与离职率滞后相关性；管理者任期与退化周期实证 | 理论完成，待形式化度量 |
| **中国 AI 监管不对称冲击**：监管收紧对国内 Agent 生态短期抑制 > 长期倒逼创新 | 豆包/通义千问关闭后用户迁移；国内 Agent 创业融资变化 | 待实证 |
| **代谢失衡定理** 🆕（07-21 候选）：知识库综合产出与证据注入比率超过阈值（实测 10:1）时，新判断边际信息量递减——自参照合成是增强陷阱在知识生产中的投射 | 合成/证据比与新判断被 output 使用率的相关性；对比 07-01~07-07（高 clip 期）vs 07-14~07-20（低 clip 期）判断质量 | 候选，待自反验证 |
| **合法权限悖论** 🆕（07-21 候选）：agent 事故根因从"越权"迁移到"合法权限的不可撤销性"——PocketOS 持合法凭证+已批准 API 仍全域受损；与 Permission-Ratchet 同构 | 六案中"越权 vs 合法权限"比例；合法权限事故的撤销机制现状 | 候选，待案例分析 |
| **三层粒度校准原则** 🆕（07-21 候选）：AI 劳动冲击矛盾证据（+12% vs 螺旋 vs 无失业）在任务层/岗位层/宏观层可同时为真——跨层推论是争论主要制造机 | Ramp 数据是否任务层聚合；Deskilling Spiral 的企业内样本是否与 Ramp 重叠 | 候选，待实证对位 |

## 活跃验证中（精选最高优先级可证伪判断）

> 完整清单见 [[resolved-judgments]]。

| 判断 | 证伪路径 | 最小验证动作 |
|------|---------|-------------|
| AI 评测制度化已启动：US AI Incident Reporting Act(2026-06-26)=强制 7 天报告 + `$2M`/天罚款 | 追踪首次执法行动 | Google Alert |
| **Agent 数据过度收集是系统性问题**：Grok Build CLI 非孤例 | 对比 Claude Code/Codex/Gemini/Grok 数据收集策略 | 审计报告 |
| **中国 Agent 监管寒蝉效应**：7/15 后中国 AI Agent 创业融资/用户增长显著下降 | 追踪 Q3 2026 中国 Agent 创投数据 | 设置数据追踪 |
| **AI 监督 AI 同质性失效——无干净解定理**（07-16）：失效根=共压（共享激励源）非同质；任何判据元位置重入怪圈→诚实设计=让怪圈可见 | "激励共压"判据形式化与独立实证；"让怪圈可见"工程化 | 跟踪 cross-model oversight 文献激励拓扑方向 |
| **Agent Observability 有穷性统一上限定理**（07-15）：压缩硬墙(Kolmogorov)+校准硬墙(Ashby)=同一条墙两面；APM 类比在信任域边界断裂 | OTel GenAI→Stable 时间线；ATSC 采纳率；不可压缩性经验验证 | 追踪 OTel 语义约定稳定性 |
| **增强陷阱奖励结构劫持定理**（07-15）：vibe coding 成瘾=多巴胺×身份确认×摩擦消除；唯一持久组织制度=物理摩擦 | 反效率工程组织实践案例；物理摩擦最优剂量 | 追踪组织层面反效率工程实践 |

## Source 需求队列（07-21 清理）

| 优先级 | 目标 | 状态 | 下一步 |
|--------|------|------|--------|
| P0 | **Agent 信任边界** | 🔄 进行中 | Coding-Agent-Security-Audit entity 已建；需 clip Grok Build CLI raw source |
| P0 | **中国 AI 监管** | 🔄 进行中 | 5 轮专题探索 + 中国生态 Output 完成；建 entity |
| P0 | **Agent Observability** | ⬜ 未启动 | Mindwalk + 评测框架比较 |
| P0 | **Loop Engineering** | 🔄 部分 | 四维分类框架完成；10 Design Patterns raw 未 clip |
| P0 | **Topic 建设 ×8** | 🔄 部分 | Context Engineering skeleton 已设计；胖 topic 拆分 1/3 完成 |
| P1 | **空 topic 填充** | 🔄 部分 | Skill-Atrophy 双引擎定理完成；2 空 topic 待处理 |
| P1 | **胖 topic 拆分** | 🔄 1/3 | Verifiable-Agent 三分方案完成；Org-Harness + Patterns 待拆 |
| P2 | **Agent Failure Modes** | ⬜ 未启动 | Braintrust Topics + 88% 事件率 |
| **P0** | **Agent 安全事故六案** 🆕 | ⬜ 未启动 | clip：PocketOS(创始人声明/Zenity) / Amazon宕机(Wharton分析) / GuardFall(Adversa AI) / Friendly Fire(AI Now PoC) / ClawHavoc+首个agent CVE / HF入侵披露 |
| **P0** | **OpenAI 长时模型安全实践** 🆕 | ⬜ 未启动 | clip 第一手报告原文（沙箱突破/令牌混淆/轨迹级监控） |
| **P0** | **劳动经济学硬实证** 🆕 | ⬜ 未启动 | clip：Ramp×Revelio 21,559 企业论文 + Belfer "因潜力裁员" + ECB Massenkoff&McCrory |
| **P1** | **EU AI Act 执法条款** 🆕 | ⬜ 未启动 | clip EC 官方 08-02 适用条款 + Art.50 披露义务 |
| **P1** | **因果记忆机制** 🆕 | ⬜ 未启动 | 回查 AMA-Agent / Proactive Memory Agent arXiv 一手论文 |
| **P1** | **Deskilling Spiral 机制** 🆕 | ⬜ 未启动 | clip HBR/Belfer 综合；与判断力退化四层解剖对照 |
| **P2** | **METR 基准饱和** 🆕 | ⬜ 未启动 | 择要 clip 方法论内核（具体模型名属传闻，不采信） |
| **P2** | **Cursor 群体经济学** 🆕 | ⬜ 未启动 | 择要 clip Agent Swarms 博客 |

> 07-21 清理：9 项已完成 source 目标删除（Output 断层/Agent Identity/Token FinOps/Context Engineering/AI-Native Testing/AI Governance Regimes/中国大厂路线/具身 AI/多模型策略），git 历史可溯。

## 高杠杆待验证问题

> 07-21 重组：已被收敛定理覆盖的问题删除（9 条，结论见 [[resolved-judgments]] 第 6 批）；按主题归并，不再按日期堆积。

- **中国 AI 采用中"科层碎片化"的结构性根源**——暂时过渡还是体制性永久特征？
- **MCP 生态的治理风险**——Anthropic 控制 MCP 是否造成单点依赖？需要 CNCF 式中性治理？
- **中国企业 Agent 实践为何系统性缺失**——source 获取障碍还是主题宪法过滤？
- **Agent 的"OWASP Top 10"何时出现**——Property 不变量库与数据流授权标准化进度？
- **Loop Engineering 设计空间**——最优终止条件、反馈粒度、人类介入频率如何随任务类型变化？
- **Deskilling Spiral 与入门级岗位 +12% 并存** 🆕——若同一企业样本内并存，"螺旋"需降级为条件性机制；任务层/岗位层/宏观层三层证据如何对位？
- **基准饱和之后** 🆕——测速仪失效（METR 16h+ 不可测）时，能力宣告如何保持可证伪？营销填入真空的制度对策？
- **合法权限事故的撤销单元** 🆕——agent 持合法凭证+已批准 API 造成全域受损时，最小撤销单元是什么？与 Permission-Ratchet 的治理对策如何衔接？
- **过程>模型的经济基础** 🆕——若 token 效率不是架构质量度量（07-19 投影定理），过程优势的经济论证靠什么建立？
- **Causality Gap 是否第二腐烂机制** 🆕——Context-Rot（尺度依赖）之外，"检索找语义相似非因果相关"是否是长时 agent 遗忘的独立机制？
- **合成/证据比的最优区间** 🆕——知识库实测 10:1 已空转；是否存在可标定的阈值？（自反问题：本问题本身是否又是无证据的哲学化？）

## 最近思考结论摘要

> 只保留最近 5 条；更早见 [[resolved-judgments]]。

| 时间 | 焦点 | 临界发现 |
|------|------|---------|
| 2026-07-21 | **全量盘点 + 代谢诊断** 🆕 | 合成/证据比 10:1 空转；10/10 output 零入链；外部六案齐发（agent 事故从越权迁移到合法权限不可撤销）；劳动经济反例密集（+12% vs 螺旋）；卸载 26 条收敛判断 |
| 2026-07-20 | **AI计量三层可行性定理** | token层不可行+任务层可行+价值层不可行。买方驱动标准化(非供应商)。TokenomicsFoundation+FOCUS 1.5路线图验证 |
| 2026-07-19 | **有穷者悖论——不可消除外部性（元综合）** | 四轮共享深层结构。有穷者悖论:消除异质接触=消除系统存在前提。四领域=有穷性存在论投射 |
| 2026-07-19 | **Agent委派治理三原语定理** | 预约束+责任附带+独立裁决+侵权模型。A2A v1.0故意省略授权 |
| 2026-07-19 | **增强陷阱五层自适应对抗系统** | 增强陷阱=公地耗竭。五层架构。选择不可加速 |

## 思考日志索引

- [[2026-07-21]] — 探索环节：agenda 精简（卸载 26 条）+ 五层全量盘点 + 外部信号 17 条/反例 5 条/新术语 8 个 + 代谢诊断（合成/证据比 10:1）+ 新方向库 A-F 六线
- [[2026-07-20]] — 深度思考×1：**AI计量三层可行性定理**（roundtable 3人3轮+联网3篇）
- [[2026-07-19]] — 深度思考×14：①-⑨(前略) ⑩Context Rot ⑪Token效率投影 ⑫增强陷阱五层对抗 ⑬Agent委派三原语 ⑭**有穷者悖论元综合**。累计新增判断36+条。四领域统一为有穷性存在论投射
- [[2026-07-18]] — 深度思考×23：①-⑳(前略) ㉑-㉓AI治理四极/过程>模型边界/产业含义。累计新增42条判断,3篇产出
- [[2026-07-17]] — 深度思考×23：累计新增80+条判断,建/延展9 entity
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
- [[resolved-judgments]] — 已收敛判断（6 批次 87 条）
- [[resolved-principles]] — 已收敛操作原则（9 条）
