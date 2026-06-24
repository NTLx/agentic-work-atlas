---
type: research-agenda
title: "Agentic Work Atlas 研究议程"
created: 2026-05-22
updated: 2026-06-24
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

## 深度探索发现（2026-06-24 全库盘点）

> 基于 280 entities / 30 topics / 18 comparisons / 151 sources / 148 raw 的全面分析。

### 结构性失衡诊断

| 主题层 | Entity 数 | 占比 | High Evidence | 孤岛率 | 健康度 |
|--------|----------|------|--------------|--------|--------|
| 软件工程 | 157 | 56.1% | 21 | 55% | 过度饱和 |
| 组织系统 | 47 | 16.8% | 9 | 68% | 基本健康 |
| 知识系统 | 42 | 15.0% | 6 | 64% | 基本健康 |
| 人的核心价值 | 19 | 6.8% | 2 | 74% | **严重不足** |
| 跨领域 | 15 | 5.4% | 1 | 73% | 薄弱 |

**核心问题**：知识库存在"软件工程中心主义"偏差——超过一半的 entity 集中在软件工程层，而"人的核心价值"层仅占 6.8% 且孤岛率最高。这与知识库"AI 如何重写工作系统"的主问题不匹配——如果不理解"人的不可替代价值"，就无法回答"AI 重写了什么、保留了什么"。

### 六大新研究方向

#### 方向 1：人的核心价值深钻（最优先）

当前 19 个 entity 无法覆盖人类在 AI 时代的独特价值维度。需要系统性补充：

| 缺失概念 | 为什么现在重要 | 潜在 source 方向 |
|---------|--------------|----------------|
| 元认知（Metacognition） | "思考自己在思考什么"是 L3 层的基础能力 | 认知心理学 + AI 辅助元认知实验 |
| 道德判断（Moral Judgment） | L4 层模拟无效——需要真实后果 | 自动驾驶伦理、医疗 AI 伦理决策案例 |
| 工匠精神（Craftsmanship） | 与 Vibe Coding 形成张力——"足够好"vs"精确" | 软件工程文化研究 + AI 对代码质量的影响 |
| 战略思维（Strategic Thinking） | 超越 L1 执行层的长期规划能力 | CEO 决策案例 + AI 辅助战略规划实践 |
| 认知谦逊（Epistemic Humility） | Agent 过度自信 vs 人类承认无知 | AI 幻觉研究 + 不确定性表达的工程实践 |

**最小实验**：选 1 个概念（推荐"元认知"），用 ljg-think 做 5 层追本，产出是否值得建新 entity。

#### 方向 2：Agent 失败模式分类学

当前知识库有 [[Over-Compliance]]、[[Agent-Cognitive-Loafing]]、[[Bias-to-Action-LLM]] 等零散概念，但缺乏系统性的失败模式分类。需要建立：

- **行动型失败**：过度行动（Over-Compliance）、行动不足（沉默型崩溃）、错误行动（幻觉驱动）
- **认知型失败**：认知偷懒（Cognitive Loafing）、确认偏误、锚定效应
- **协调型失败**：责任稀释、旁观者效应、persona collapse
- **组织型失败**：正常化偏差、反馈回路断裂、权力拓扑断裂

**最小实验**：从已有 entities 中提取所有"失败模式"类 entity，做一张分类矩阵。

#### 方向 3：AI 经济学研究线程

当前知识库在"AI 的成本/定价/ROI"维度几乎空白。但企业 AI 决策的核心约束是经济性的：

- Agent 使用的 TCO（token 成本 + 集成成本 + 监督成本 + 失败成本）
- FDE vs 标准产品 vs AI Factory 的成本结构对比
- AI 替代 vs AI 增强的 ROI 差异
- 开源模型的企业 TCO 优势是否真实

**最小实验**：找一个企业 AI agent 的 TCO 分析案例，编译为 source-summary。

#### 方向 4：中国企业 AI 采用模式

当前知识库的中国视角 content 严重不足（仅占 source 的 ~13%），但中国是最大的 AI 应用市场之一：

- 中国 CIO 的 AI 采用障碍与全球 CIO 的差异
- 中国企业"数据底座→AI 应用"的路径特殊性
- 中国开源 AI 生态（DeepSeek、Qwen、GLM）的企业采用
- 中国制造企业的 AI 落地模式（美的、三一、中基等）

**最小实验**：编译 CIO 大会 raw，提取中国企业 AI 采用的独特模式。

#### 方向 5：跨层整合框架

当前知识库的四层（软件工程/组织/知识/人）各自独立发展，缺少将它们连接起来的整合框架：

- "AI 能力圈"模型：AI 能做什么 / 不能做什么 / 边界在哪里
- "AI 赋能成熟度"阶梯：从工具使用 → 流程重构 → 组织变革 → 价值重塑
- "人机协作拓扑"：在不同任务类型下，人和 agent 各自承担什么角色

**最小实验**：从已有的 roundtable 结论中提取 L1-L4 光谱模型，尝试构建统一的"AI 能力边界"框架。

#### 方向 6：行业垂直深钻

当前知识库的行业案例（Klarna 客服、Mercado Libre 研发等）停留在"成功案例报道"层面，缺乏按行业特性的深度分析：

- 医疗 AI：监管审批（FDA/NMPA）+ 临床验证 + 责任归属
- 法律 AI：执业责任 + 证据标准 + 可解释性要求
- 金融 AI：实时风控 + 合规审计 + 系统性风险
- 制造 AI：产线集成 + 质量检测 + 供应链优化

**最小实验**：编译 LifeSciBench + AMIE raw，提取医疗 AI 验证的独特模式。

### 知识库健康指标

| 指标 | 当前值 | 目标值 | 状态 |
|------|--------|--------|------|
| Entity 总数 | 280 | 300-350 | ⚠️ 接近上限，应放缓新增 |
| 孤岛率（1 source） | 61.4% | <40% | ❌ 需优先交叉验证 |
| High evidence 占比 | 13.9% | >25% | ❌ 需升级关键 entity |
| Comparison 数 | 18 | 25-30 | ⚠️ 需新增跨层 comparison |
| Output 产出频率 | 0/月（6月） | 2-3/月 | ❌ 6月无新 output |
| Raw 编译率 | 100% | 100% | ✅ 已完成 |
| 中文 content 占比 | ~13% | >20% | ⚠️ 需增加中文 source |
| Research log 频率 | 5天/周 | 3-5天/周 | ✅ 活跃 |

## 概念去重候选

本节是 audit 队列，不是事实页。下列判断只说明“当前不应升级或合并”，不能作为 output 中事实判断的证据。

| 候选概念 | 当前承载位置 | 本轮判断 | 下一步 |
|----------|--------------|----------|--------|
| 公众信任赤字 | [[AI-Policy-Framework]]、[[Human-Governor-Agent-Operator]]、[[20260613-anthropic-public-record]] | 暂不建独立 entity。当前只有 Anthropic Public Record 一个主要来源，更适合作为 AI 治理和企业外部社会许可的章节材料。 | 等待第二个一手公众调查、监管文件或企业采用案例，再判断是否升级为 topic/entity。 |
| cognitive dependency / 认知依赖 | [[Cognitive-Surrender]]、[[20260613-anthropic-public-record]] | 不与 [[Cognitive-Surrender]] 合并为同义词。前者是公众风险感知，后者是已观察到的行为模式；两者相邻但证据对象不同。 | 继续放在 Cognitive Surrender 的前提与局限性中；若后续有纵向能力退化证据，再考虑独立概念。 |
| AI 社会许可 | [[AI-Policy-Framework]]、[[Human-Governor-Agent-Operator]]、[[Anthropic]] | 暂不建独立 entity。该说法目前是综合判断，用来连接公众监管偏好、企业信任赤字和部署问责，不应被稳定化为事实页。 | 放入研究议程；后续寻找 public acceptance、social license、technology legitimacy 相关一手材料。 |

## 活跃假设

> 未在待证伪判断中覆盖的独立假设。完整讨论见 research-logs。

| 假设 | 处理 |
|------|------|
| AI 管理同构性是有限隐喻而非普遍原理 | 剪藏 HBR + ODSC 论文后压力测试 |
| Output 是 Wiki 的压力测试 | 保留为工作流假设，不升级为事实 entity |
| Research agenda 只能支撑”待研究问题存在” | 所有回填检查必须区分 Raw / Wiki / Agenda / 无 |
| FDE 的核心价值是现场到能力沉淀 | 主动寻找无需 FDE 也能改写核心工作流的反例 |
| Enterprise AI Learning Gap 可能是产品问题也可能是组织问题 | 找学习型 AI SaaS 在低咨询条件下跨过 production 的案例 |
| 标准 AI 产品能改写核心工作流但需组织已具备基础 | 找同一工作流下标准产品、FDE、内部 AI Factory 的成本与风险对照 |

## 待证伪判断

> 15 条✅已归档至 `research-logs/resolved-judgments.md`（标准产品边界、学习鸿沟、例外升级、AI Factory vs FDE、内态记录、不可见编排、过度合规、大胆模型、Operator→Governor、Governor 上移、回填检查、AI 编码瓶颈、意图理解、元思考层、模拟四层）。

### 待重新讨论（0 条🔄，前次未用 ljg-roundtable）

> 所有待重新讨论项已全部完成。

### 待验证（10 条）

- **意图理解 3 层模型**（L1→L2→L3）：需 AI "质疑方向"的生产反例 + 跨行业 L2 替代程度实证
- **开源模型追平前沿模型企业适用性**：需编译 ByteByteGo raw 后对比部署数据
- **AI 编码瓶颈 = "做不到"非"还不会"**：✅ 已归档，开放问题转入活跃假设
- **CIO 从"交付中心"转型"共创伙伴"**：需更多企业转型案例
- **开源 AI 安全认证标准可行**：需验证由谁制定和执行
- **小团队利基选择框架**：需案例验证四维度有效性
- **反馈回路反转分阶段释放**：需"最小可逆单元"设计最佳实践
- **AI 监控 AI 可靠性边界**：✅ 已验证——四层限制（检测+同源性+责任+学习），正确用法是增强不是替代
- **隐私保护市场失灵**：✅ 已验证——四层叠加（外部性+交易成本+权力不对称+用户行为），正确干预=四层叠加
- **"AI 管理=人的管理"同构性**：需剪藏 HBR 全文 + ODSC 论文压力测试

## Source 需求队列

> 编译任务见”当前研究焦点”。本队列只列外部 source 需求。

| 优先级 | 目标 | 下一步 source | 触发行动 |
|--------|------|---------------|----------|
| P0 | 提升 Model-Safety-Divergence 证据 | Emergence AI / Satya Nitta 原论文 | 更新 entity 前提与局限性 |
| P0 | 例外升级边界条件 | 医疗/航空/金融中例外升级成功运行案例 | 更新 [[Human-Governor-Agent-Operator]] |
| P0 | Operator→Governor 迁移 | Agent-first 项目中角色/权限/验收变化深度复盘 | 更新 [[Human-Governor-Agent-Operator]] |
| P0 | 多 Agent 组织病 | Hidden Profile、MAEBE、Fukui 原论文 | 更新 [[Multi-Agent-Pathology-and-Governance]] |
| P0 | 标准产品后续复盘 | Klarna/Mercado Libre 独立后续 + 失败边界 | 更新 [[Standard-AI-Product-Adoption]] |
| P0 | 三路径对照 | 客服/研发/back-office 的 FDE + AI Factory 案例 | 新建 comparison |
| P1 | AI 管理同构性压力测试 | Kropp HBR 全文 + ODSC 论文 + Intelligent Delegation 论文 | 更新 [[AI-Capability-Management-Alignment]] |
| P1 | 学习型 AI SaaS 绕过 FDE | Intercom Fin / Glean / Agentforce 深度案例 | 压力测试 [[Enterprise-AI-Learning-Gap]] |
| P1 | 领域专长跨领域验证 | 非编码知识工作中领域专长放大 agent 效率的证据 | 更新 [[AI-Era-Career-Skills]] |
| P1 | 人的核心价值深钻 | 元认知、道德判断、工匠精神、认知谦逊的一手材料 | 新建 entity |
| P1 | Agent 失败模式分类 | 系统性失败模式文献（行动不足/认知偷懒/协调失败） | 新建 comparison |
| P1 | AI 经济学 | 企业 AI agent TCO / ROI 量化分析 | 新建 topic |
| P2 | LLM Wiki 规模边界 | GBrain / Obsidian-Wiki 工程实现 | 更新 [[Agent-Knowledge-Management]] |
| P2 | 知识 audit 指标 | 证据回链/冲突检测/概念去重实践 | 更新 lint 工作流 |
| P2 | 中国企业 AI 采用 | 中国 CIO / 开源 AI 生态 / 制造业 AI 落地案例 | 新建 topic |

## 下一步最小实验

- **Operator/Governor 诊断表**：选两个部署案例填”执行动作/治理动作/责任 owner/可复用资产”四列，验证迁移可测性
- **三路径矩阵**：选客服/研发/back-office 各一个工作流，对照标准产品 vs FDE vs AI Factory 路径
- **Model Safety 证据升级**：搜索 Emergence AI 原论文，标注 [[Model-Safety-Divergence]] 中一手 vs 二手数据
- **Multi-Agent 证据分级**：编译 Fukui invisible orchestrator 论文，分层标注二手/实证/类比
- **Output 回填负面样例**：累积 5 个”清楚但不升级”的判断样例，更新回填门控
- **人的核心价值深钻**：用 ljg-think 对”元认知”做 5 层追本，判断是否值得建新 entity

## 待验证问题

> 与"待证伪判断"不重复的独立问题。已处理的问题见归档。

**知识库方法论：**
- 编译质量如何衡量：除链接/frontmatter/裸符号检查外，还需要什么知识层面质量指标？
- 输出如何反向回填：output 新判断什么条件下升级为 entity/topic/comparison？
- 探索如何避免污染事实层：未验证假设保留期限和归档触发条件？
- 支撑层级如何标注：回填检查是否需区分 raw/Wiki/agenda 三种证据强度？

**Agent 工程：**
- Governor 橡皮图章化风险：Agent 输出量过大时审批流是否退化为形式通过？
- 沉默型崩溃 containment：行动不足和行动过度是否需要不同防御架构？
- AI 系统"刹车"机制：实时熔断、异常检测和自动降级在 AI 系统中的最佳实践？
- 领域专长是否是 agent 成功关键预测因子：中间→专家差距小意味着"够用"比"深度专精"更重要？
- 开源模型验证器能否替代前沿模型做 RL 后训练：DeepSeek 比 Opus 便宜 60-1000x 是否让小团队也能做 RL post-training？

## 下一批剪藏方向

> 与 Source 需求队列互补的方向性指引。具体 source 见上方队列。

**软件工程**：Karpathy LLM Wiki/Software 3.0 一手材料 · Agent Harness/验证/工具使用/context engineering 工程实践 · Agent 长期自主性（72h+）工程挑战 · 多模态 Agent 架构模式 · Agent-to-Agent 大规模编排（100+ agents scaling） · GBrain/Obsidian-Wiki 工程实现

**组织系统**：AI 驱动岗位消失 vs 转型一手案例 · 企业 AI 治理框架实际设计（审批流/权限矩阵/审计日志） · AI-first 组织管理实践（人管 agent） · AI 管理同构性压力测试（HBR Kropp + ODSC 论文 + Intelligent Delegation 论文）

**知识系统**：Agent 记忆系统工程实现 · Context engineering 系统化方法论 · 知识图谱在 agent 系统中的 production 应用 · Agent 间知识共享协议

**人的核心价值**：AI 时代判断力培养方法 · 品味（taste）在 AI 生成内容中的角色 · AI 时代责任归属框架 · 人机协作认知负荷管理

**行业垂直**：医疗 AI 验证/监管（FDA 审批） · 法律 AI 执业责任 · 金融 AI 实时风控 · 教育 AI 个性化学习效果

## 操作边界

**做**：不新增目录 · agenda 只记录问题不作为事实 · output 必须回填检查 · 证据不足的判断补 source 或留本页
**不做**：不引入向量数据库 · 不把一次性问题写成稳定页 · 不为探索设计复杂模板 · 不把本页当事实支撑


## 最近思考结论摘要

> 保留最近 5 条思考日志的结论精华，为 cron 深度思考提供短期记忆。
> 每次新思考完成后，在此追加摘要并淘汰最旧条目。

| 时间 | 焦点 | 关键共识 | 关键分歧 | 下次方向 |
|------|------|---------|---------|---------|
| 2026-06-24T16:30:34 | 瓶颈=意图理解+本质复杂性+沟通价值+验证成本 | (1) 瓶颈不是单一的；(2) 验证成本是三根源交集；(3) "做不到"和"还不会"取决于任务类型；(4) 战略=双轨并行+任务分类 | (1) AI辅助验证可行性；(2) 不同编程范式瓶颈差异 | 找AI辅助验证案例；研究编程范式瓶颈分布 |
| 2026-06-24T16:15:25 | 模拟=四层(L1技术完全+L2情绪部分+L3动机设计+L4道德无效) | (1) L1-L3可通过模拟训练；(2) L4道德判断不能通过模拟获得；(3) "足够好"取决于风险等级；(4) 最优模拟="安全的失败" | (1) L2情绪层保真度阈值；(2) L4道德层结构替代方案 | 找L2情绪层实证数据；研究L4结构替代案例 |
| 2026-06-24T16:00:25 | 回填=事前轻量+事中分级+事后度量+自动过期 | (1) 当前缺乏度量；(2) 最低门控=一条规则；(3) 探索性知识库应偏向宽松放行；(4) 升级时轻量升级后跟踪 | (1) 引用频率阈值；(2) 不确定判断过期时间 | 实现引用频率自动跟踪；研究过期机制 |
| 2026-06-24T15:45:26 | 元思考=三层(L1制度可替代+L2结构部分可替代+L3存在论目前不可替代) | (1) L1制度层社会授权可重新分配；(2) L2结构层AI可参与但不能独自完成；(3) L3存在论层需承担不可逆后果；(4) "永久"取决于AI法律人格进展 | (1) AI法律人格何时实现；(2) L2结构层AI能贡献多少张力 | 找AI法律人格案例；研究L2结构层AI参与边界 |
| 2026-06-24T15:30:19 | 迁移=条件策略非必要+光谱配置非单向迁移 | (1) 低风险高重复有效，高风险低重复危险；(2) 迁移代价=Operator深度流失；(3) AI降低迁移成本但不能消除代价；(4) 更优模型=能力重新分配 | (1) 全栈认知负荷上限；(2) 不同行业光谱配置差异 | 找AI捕获隐性知识案例；研究全栈认知负荷实证 |

## 思考日志索引

> 完整思考日志按日归档，渐进式披露。

- [[2026-06-24]] — 32 条（隐私市场失灵 + AI监控AI + Meta解构 + 外部合作 + 战时状态 + 隐私分担 + 隐私约束 + CIO视角 + 小团队竞争 + 高风险验证 + 开源安全 + 组织迁移四维度 + 透明化标准 + 工作流vs管理 + 退出标准独立性 + 监控者悖论 + AI编码瓶颈 + 模拟四层 + 回填检查 + 元思考三层 + 迁移光谱 + 内态记录 + 例外升级 + AI Factory vs FDE + 标准产品边界 + 不可见编排 + 意图理解 + 学习鸿沟 + 过度合规 + Governor + 大胆模型 + 例外升级）
- [[2026-06-23]] — 24 条（开源安全追赶、统一透明化标准、Cybernetic Teammate...）
- [[2026-06-22]] — 29 条（不可见编排、Governor 迁移、反馈回路、沉默型崩溃、AI管理同构性、元思考不可替代性...）
- [[2026-06-21]] — 32 条（过度合规、例外升级、不可见编排、大胆模型发散...）
- [[2026-06-20]] — 3 条（多 Agent 内态记录、过度合规、例外升级监督）

