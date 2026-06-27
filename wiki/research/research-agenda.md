---
type: research-agenda
title: "Agentic Work Atlas 研究议程"
created: 2026-05-22
updated: 2026-06-25
tags:
  - research-agenda
  - agentic-work-atlas
  - llm-wiki
  - knowledge-management
related_entities:
  - "[[LLM-Wiki]]"
  - "[[Knowledge-Compilation]]"
  - "[[Agentic-Engineering]]"
  - "[[Human-Governor-Agent-Operator]]"
  - "[[Forward-Deployed-AI-Enablement]]"
  - "[[Enterprise-AI-Factory]]"
  - "[[Standard-AI-Product-Adoption]]"
  - "[[Multi-Agent-Pathology-and-Governance]]"
  - "[[AI-Capability-Management-Alignment]]"
  - "[[AI-Native-Engineering-Org]]"
---

# Agentic Work Atlas 研究议程

> [!note] 使用边界
> 本页维护当前最值得验证的问题、反例、source 需求和下一步动作。它不作为事实页；稳定结论必须回填到 entity、topic 或 comparison，并能追溯到 raw source。详细盘点数据和已验证判断见 [[exploration-archive-20260625]] 与 [[resolved-judgments]]。

## 当前研究焦点

| 焦点 | 为什么现在重要 | 当前状态 | 下一步动作 |
|------|----------------|----------|------------|
| 位置性统一理论 | 2026-06-23 研究日志涌现"位置性是统一底层结构"洞察，但未形式化 | 仅存在于 research-logs，无 entity/topic | 用 ljg-think 做 5 层追本：位置性是隐喻/分析框架/可测量维度/统一理论？决定是否建 entity |
| 人的核心价值层深钻 | 全库最薄弱层——14 entities (5%)、孤岛率 57%、high evidence 仅 2 | 有 [[Wisdom-Work]]、[[Taste]]、[[Judgment]] 但缺元认知/道德判断/工匠精神 | 选"元认知"用 ljg-think 5 层追本，判断是否值得建 entity |
| Agent 失败模式分类学 | [[Over-Compliance]]、[[Agent-Cognitive-Loafing]]、[[Bias-to-Action-LLM]] 零散，缺系统分类 | 概念分散在各 entity，无 comparison | 从已有 entity 提取所有"失败模式"类概念，做四维分类矩阵（行动/认知/协调/组织） |
| 知识图谱整合层稀薄 | 35% entity (98/280) 无 topic/comparison 承载；entity 互引覆盖已 93.2%（口径：整合层承载 / 知识层互引，2026-06-25 实测） | 多 hub 结构（Agentic-Engineering 119、Agent-Harness 78、Context-Engineering 50），非唯一 hub | 对 98 个未承载 entity 按 tag 聚类建 topic，目标整合层承载 65%→80% |
| Output 产出流水线重启 | 最后 output 在 2026-06-01（24 天前），研究→产出转化率仅 7% | 研究层累计 67+ 条思考，仅 5 条转化为 output | 从 research-logs 提取 3-5 个成熟 synthesized 判断，选 1 个产出 |
| AI 经济学线程 | 全库在"AI 成本/定价/ROI"维度几乎空白 | 无相关 entity/topic | 找企业 AI agent TCO 分析案例，编译为 source-summary，关联 [[Enterprise-AI-Factory]] |
| 中国企业 AI 采用 | 中文 source 占比仅 ~13%，中国视角严重不足 | 有 3 个中国企业案例 source 但未系统编译 | 编译 CIO 大会 raw + 美的/三一案例，提取中国模式特殊性 |
| 多 Agent 组织病治理 | 当前证据主要来自二手综述；多 Agent 域整合层未承载率待 entity-audit 域级复现（历史 80.4% 口径不可复现，见 [[exploration-archive-20260625]]） | 已有 [[Multi-Agent-Pathology-and-Governance]] | 优先补一手论文（Hidden Profile、MAEBE、Fukui）和生产级 observability 复盘 |
| 高风险行业 AI 验证 | 医疗/法律/金融 AI 验证范式出现但未系统编译 | 多个 raw 已入库（LifeSciBench、AMIE、legal verifiers）未编译 | 编译这 3-4 篇 raw，提取高风险行业验证共同模式，新建 comparison |
| 跨层整合框架 | 四层（软工/组织/知识/人）各自独立，缺连接框架 | 有 [[Wisdom-Work-Evolution]] 等零散 topic | 从已有 roundtable 结论提取 L1-L4 光谱模型，构建统一"AI 能力边界"框架 |

## 活跃假设

> 未在待证伪判断中覆盖的独立假设。完整讨论见 research-logs。

| 假设 | 处理 |
|------|------|
| 位置性是统一底层结构（可解释 AI 工作变迁各层面现象） | 用 ljg-think 压力测试：找位置性无法解释的反例 |
| Agent 失败模式可四维分类（行动/认知/协调/组织），且四维有因果关系 | ✅已验证：因果方向 组织→协调→认知→行动（roundtable综合+MAST论文实证+SLOTH论文实证+已有entity交叉验证）——见2026-06-27思考日志 |
| 整合层承载提升到 80% 可自动暴露隐藏缺口 | 对 98 个未承载 entity 聚类建 topic，测量缺口发现率 |
| Output 转化率低是流程问题（缺 research→output 标准路径）而非研究质量问题 | 建立标准转化路径，测试转化率是否提升 |
| AI 经济学盲区导致路径选择判断失真（缺成本结构数据） | 找 3 个企业 AI agent TCO 案例验证 |
| AI 管理同构性是有限隐喻而非普遍原理 | 剪藏 HBR + ODSC 论文后压力测试 |
| Output 是 Wiki 的压力测试 | 保留为工作流假设，不升级为事实 entity |
| Research agenda 只能支撑"待研究问题存在" | 所有回填检查必须区分 Raw / Wiki / Agenda / 无 |
| FDE 的核心价值是现场到能力沉淀 | 主动寻找无需 FDE 也能改写核心工作流的反例 |
| Enterprise AI Learning Gap 可能是产品问题也可能是组织问题 | 找学习型 AI SaaS 在低咨询条件下跨过 production 的案例 |
| 标准 AI 产品能改写核心工作流但需组织已具备基础 | 找同一工作流下标准产品、FDE、内部 AI Factory 的成本与风险对照 |
| 品味有"局部客观性"——特定领域内确实有更好/更差的选择 | 跨文化研究已部分验证（Nature 2025），需找更多领域特定的品味客观性证据 |
| 品味不可替代性 = 判断力 x 责任 x 时间，AI架构无法兼容 | 用ljg-think追本"局部客观性标准从何而来"，找AI具身化反例 |

## 待证伪判断

> 15 条✅已归档至 [[resolved-judgments]]。10 条待验证✅已归档至 [[exploration-archive-20260625]]。

### 待重新讨论（0 条🔄）

> 所有待重新讨论项已全部完成。

### 待验证（0 条）

> 原 10 条已全部验证并归档至 [[exploration-archive-20260625]]。新研究方向产生的待验证判断见上方"活跃假设"。

## Source 需求队列

> 编译任务见"当前研究焦点"。本队列只列外部 source 需求。

| 优先级 | 目标 | 下一步 source | 触发行动 |
|--------|------|---------------|----------|
| P0 | 位置性理论形式化 | 认知科学/经济学/社会学中 positionality 一手材料 | 新建 entity 前先做 ljg-think |
| P0 | 多 Agent 组织病 | Hidden Profile、MAEBE、Fukui invisible orchestrator 原论文 | 更新 [[Multi-Agent-Pathology-and-Governance]] |
| P0 | 三路径成本对照 | 客服/研发/back-office 的 FDE + AI Factory + 标准产品案例 | 新建 comparison |
| P0 | Agent 失败模式分类 | MAST (UC Berkeley 2025, arxiv 2503.13657) + SLOTH (ACL ARR 2026) 已入库 ✅ | 新建 [[Agent-Failure-Causal-Chain]] comparison（2026-06-27 完成） |
| P1 | AI 管理同构性压力测试 | Kropp HBR 全文 + ODSC 论文 + Intelligent Delegation 论文 | 更新 [[AI-Capability-Management-Alignment]] |
| P1 | 学习型 AI SaaS 绕过 FDE | Intercom Fin / Glean / Agentforce 深度案例 | 压力测试 [[Enterprise-AI-Learning-Gap]] |
| P1 | 人的核心价值深钻 | 元认知、道德判断、工匠精神、认知谦逊的一手材料 | 新建 entity |
| P1 | AI 经济学 | 企业 AI agent TCO / ROI 量化分析 | 新建 topic |
| P1 | 中国企业 AI 采用 | 中国 CIO / 开源 AI 生态 / 制造业 AI 落地案例 | 新建 topic |
| P1 | 高风险行业验证 | 医疗 FDA 审批 / 法律执业责任 / 金融实时风控案例 | 新建 comparison |
| P2 | 整合层承载 | 98 个未承载 entity 的聚类与 topic 承载 source | 提升整合层承载至 80% |
| P2 | LLM Wiki 规模边界 | GBrain / Obsidian-Wiki 工程实现 | 更新 [[Agent-Knowledge-Management]] |
| P2 | 知识 audit 指标 | 证据回链/冲突检测/概念去重实践 | 更新 lint 工作流 |
| P2 | Output 转化路径 | research→output 标准化案例 | 建立转化流程 |

## 下一步最小实验

- **位置性追本**：用 ljg-think 对"位置性"做 5 层追本——是隐喻/分析框架/可测量维度/统一理论？判断是否值得建 entity
- **Agent 失败模式矩阵**：从已有 entity 提取所有"失败模式"类概念，做四维分类（行动/认知/协调/组织），验证覆盖率
- **未承载 entity 聚类**：对 98 个无 topic/comparison 承载的 entity 按 tag 聚类，成簇的建 topic（如 AGI 经济学、记忆系统、人物档），目标整合层承载 65%→80%
- **Output 候选筛选**：从 research-logs 提取 3-5 个成熟 synthesized 判断（位置性/反馈回路/元思考层），选 1 个产出
- **Operator/Governor 诊断表**：选两个部署案例填"执行动作/治理动作/责任 owner/可复用资产"四列
- **三路径矩阵**：选客服/研发/back-office 各一个工作流，对照标准产品 vs FDE vs AI Factory
- **人的核心价值深钻**：用 ljg-think 对"元认知"做 5 层追本，判断是否值得建新 entity

## 待验证问题

> 与"活跃假设"不重复的独立问题。

**知识库方法论：**
- 整合层承载阈值：承载率提升到什么水平才能自动暴露隐藏缺口？
- Output 转化标准：research-logs 中的 synthesized 判断什么条件下升级为 output？
- 域级未承载率红线：不同 tag 域的未承载率红线应该不同吗（如 person 类可放宽）？待 entity-audit 域级复现
- 编译质量衡量：除链接/frontmatter/裸符号检查外，还需要什么知识层面质量指标？
- 探索如何避免污染事实层：未验证假设保留期限和归档触发条件？

**Agent 工程：**
- Agent 失败模式因果关系：行动型/认知型/协调型/组织型失败之间是否有因果链？
- Governor 橡皮图章化风险：Agent 输出量过大时审批流是否退化为形式通过？
- 沉默型崩溃 containment：行动不足和行动过度是否需要不同防御架构？
- AI 系统"刹车"机制：实时熔断、异常检测和自动降级在 AI 系统中的最佳实践？
- 开源模型验证器能否替代前沿模型做 RL 后训练：DeepSeek 比 Opus 便宜 60-1000x 是否让小团队也能做 RL post-training？

**AI 经济学（新线程）：**
- Agent 部署的真实 TCO 结构：token 成本 / 集成成本 / 监督成本 / 失败成本各占多少？
- FDE vs 标准产品 vs AI Factory 的成本结构差异是否决定路径选择？
- AI 替代 vs AI 增强的 ROI 差异如何量化？

## 下一批剪藏方向

> 与 Source 需求队列互补的方向性指引。具体 source 见上方队列。

**软件工程**：Karpathy LLM Wiki/Software 3.0 一手材料 · Agent Harness/验证/工具使用/context engineering 工程实践 · Agent 长期自主性（72h+）工程挑战 · 多模态 Agent 架构模式 · Agent-to-Agent 大规模编排（100+ agents scaling） · GBrain/Obsidian-Wiki 工程实现

**组织系统**：AI 驱动岗位消失 vs 转型一手案例 · 企业 AI 治理框架实际设计（审批流/权限矩阵/审计日志） · AI-first 组织管理实践（人管 agent） · AI 管理同构性压力测试（HBR Kropp + ODSC 论文 + Intelligent Delegation 论文）

**知识系统**：Agent 记忆系统工程实现 · Context engineering 系统化方法论 · 知识图谱在 agent 系统中的 production 应用 · Agent 间知识共享协议

**人的核心价值**：AI 时代判断力培养方法 · 品味（taste）在 AI 生成内容中的角色 · AI 时代责任归属框架 · 人机协作认知负荷管理 · 元认知/道德判断/工匠精神/认知谦逊一手材料

**AI 经济学（新）**：企业 AI agent TCO 分析 · FDE/标准产品/AI Factory 成本结构对比 · AI 替代 vs 增强 ROI 研究 · 开源模型企业 TCO 优势实证

**行业垂直**：医疗 AI 验证/监管（FDA/NMPA 审批） · 法律 AI 执业责任 · 金融 AI 实时风控 · 制造 AI 产线集成 · 中国制造企业（美的/三一/中基）AI 落地

## 操作边界

**做**：不新增目录 · agenda 只记录问题不作为事实 · output 必须回填检查 · 证据不足的判断补 source 或留本页 · 详细发现归档到 research-logs
**不做**：不引入向量数据库 · 不把一次性问题写成稳定页 · 不为探索设计复杂模板 · 不把本页当事实支撑


## 最近思考结论摘要

> 保留最近 5 条思考日志的结论精华，为 cron 深度思考提供短期记忆。
> 每次新思考完成后，在此追加摘要并淘汰最旧条目。

| 时间 | 焦点 | 关键共识 | 关键分歧 | 下次方向 |
|------|------|---------|---------|---------|
| 2026-06-27 | Agent 失败模式因果链：四层因果方向 + 阻断不可自举 + 人的外部不可替代 | (1) 因果方向：组织层→协调层→认知层→行动层（MAST论文实证：系统设计问题最高发）；(2) 阻断不可自举——任何内部防御共享系统"不思"默认态；(3) 技术外部不能替代人的外部——责任逻辑上要求"不可替代的承担者"；(4) 双层防御：设计阶段硬防御+运行阶段人的外部 | (1) 因果链闭合性：开放链vs反馈环（判定：不互斥，主方向+反馈回路共存）；(2) 外部视角本质：技术检测(Dekker)vs道德追问(Arendt)（判定：互补，检测和追问回答不同问题） | 实证验证因果方向：controlled experiment；漂移检测器工程案例；架构不可变硬防御参考实现 |
| 2026-06-27 | 品味局部客观性来源：三层不可替代性结构 | (1) 品味客观性是"局部客观性"——标准来自身体-环境耦合而非先验真理；(2) 时间性是品味关键维度；(3) AI可模仿输出但难复制品味深度 | (1) 品味客观性本体论地位（涌现属性立场最具解释力）；(2) 有限性是存在论必要还是工程可模拟 | 找实证：AI终身学习能否模拟惯习开放结构；边界判断力操作化定义 |
| 2026-06-25 | 全库盘点：位置性统一理论涌现 + 产出断层 + 整合层稀薄 | (1) 位置性可能是统一底层结构；(2) 研究层活跃但产出停滞（转化率 7%）；(3) 碎片化真形态是整合层未承载 35%，非孤岛（entity 互引已 93.2%）；(4) 早期"81.8% 孤岛 / 80.4% 域级"为口径漂移，已纠正并钉死口径见 `schema/fragmentation-metrics.md` | (1) 位置性是隐喻还是理论；(2) 产出断层是流程问题还是质量问题 | 形式化位置性理论；重启 output 产出；对未承载 entity 聚类建 topic |
| 2026-06-25 | Taste 深层结构：三重不可替代性 x AI架构盲区 | (1) 品味=判断力x责任x时间；(2) 品味管理不确定性，AI偏向确定性；(3) 品味有局部客观性（跨文化研究支持） | (1) 品味标准从何而来；(2) AI具身化能否突破knowing-how壁垒 | ~~追本品味局部客观性来源~~ ✅已完成(2026-06-27)；找AI具身化反例 |
| 2026-06-24T22:45:56 | "AI管理=人的管理"同构性分层：可借用/需修改/不适用 | (1) 同构性分层有效；(2) 控制粒度光谱有效；(3) "管理"隐喻有边界；(4) 目标对齐比激励相容更难 | (1) AI"授权"如何定义；(2) AI"问责"如何实现 | 找AI授权定义案例；研究AI问责实现机制 |

## 思考日志索引

> 完整思考日志按日归档，渐进式披露。

- [[2026-06-27]] — 品味局部客观性来源圆桌（Bourdieu/Hume/Clark/Dreyfus）+ Agent 失败模式因果链圆桌（Perrow/Vaughan/Reason/Dekker/Arendt）：四层因果方向（组织→协调→认知→行动）+ 阻断不可自举 + 技术外部≠人的外部（可替代性鸿沟）+ MAST/SLOTH 实证
- [[2026-06-25]] — 全库盘点 + 位置性统一理论涌现 + 产出断层诊断 + 图谱碎片化分析 + Taste深层结构三重不可替代性 + AI架构盲区
- [[2026-06-24]] — 38 条（AI管理同构性 + CIO转型 + 反馈反转 + 小团队利基 + 开源认证 + 隐私市场失灵 + AI监控AI + Meta解构 + 外部合作 + 战时状态 + 隐私分担 + 隐私约束 + CIO视角 + 小团队竞争 + 高风险验证 + 开源安全 + 组织迁移四维度 + 透明化标准 + 工作流vs管理 + 退出标准独立性 + 监控者悖论 + AI编码瓶颈 + 模拟四层 + 回填检查 + 元思考三层 + 迁移光谱 + 内态记录 + 例外升级 + AI Factory vs FDE + 标准产品边界 + 不可见编排 + 意图理解 + 学习鸿沟 + 过度合规 + Governor + 大胆模型 + 例外升级）
- [[2026-06-23]] — 24 条（开源安全追赶、统一透明化标准、Cybernetic Teammate、位置性统一理论涌现...）
- [[2026-06-22]] — 29 条（不可见编排、Governor 迁移、反馈回路、沉默型崩溃、AI管理同构性、元思考不可替代性...）
- [[2026-06-21]] — 32 条（过度合规、例外升级、不可见编排、大胆模型发散...）
- [[2026-06-20]] — 3 条（多 Agent 内态记录、过度合规、例外升级监督）
- [[exploration-archive-20260625]] — 全库盘点详细数据 + 已验证判断 10 条 + 概念去重候选归档
- [[resolved-judgments]] — 2026-06-24 批次已收敛判断 15 条
