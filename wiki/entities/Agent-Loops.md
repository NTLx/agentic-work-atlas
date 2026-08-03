---
type: entity
title: Agent Loops
aliases:
  - Agent Loops
  - Agent 循环调度
  - 时间驱动 Agent
definition: "让 Agent 按时间或事件持续运行、检查状态、修复问题和汇总反馈的自动化编排模式"
created: 2026-05-08
updated: 2026-08-03
tags:
  - AI-agent
  - claude-code
  - automation
evidence_level: medium
claim_type: mixed
related_entities:
  - "[[Boris-Cherny]]"
  - "[[Claude-Code-CLI]]"
  - "[[Product-Overhang]]"
  - "[[Agent-Swarm]]"
  - "[[Agent-Workflow-Patterns]]"
  - "[[Claude-Code-Automation]]"
  - "[[Agent-Harness]]"
  - "[[Context-Advantage]]"
  - "[[Loss-Function-Development]]"
  - "[[Agent-Verification]]"
  - "[[Human-Governor-Agent-Operator]]"
source_raw:
  - "[[Anthropic's Boris Cherny: Why Coding Is Solved, and What Comes Next]]"
  - "[[20260630-loop-engineering-andrew-ng]]"
  - "[[20260617-langchain-art-of-loop-engineering]]"
  - "[[20260706-getting-started-with-loops-claude-code]]"
  - "[[20260624-loops-rediscovering-cybernetics]]"
  - "[[20260611-loss-function-development]]"
  - "[[20260708-bun-in-rust]]"
  - "[[20260708-agent-loop-bytebytego]]"
  - "[[20260708-vercel-agent]]"
---

# Agent Loops（Agent 循环调度）

> [!definition] 定义
> **Agent Loops** 是一种时间驱动的 Agent 自动化模式：让 Agent 以固定频率或持续监听方式运行，反复检查状态、执行修复、整理反馈、推进后台任务，并把结果交给人类或上层系统验收。

## 为什么重要

单次 Agent 调用解决的是“这个任务怎么做”。Agent Loops 解决的是“这个系统如何持续被照看”。当 coding agent 可以读代码、跑测试、修 CI、看 PR、聚类反馈时，最小可行自动化不再是复杂多 Agent 架构，而可能只是一个定时循环。

Boris Cherny 把 loops 描述为极简但有效的范式：让 Agent 每隔一段时间检查某个状态，并在发现问题时行动。这个模式把 Agent 从一次性助手变成持续运行的后台工作者。

## 关键数据点

- Boris 的使用场景包括 PR 看护、自动修 CI、auto rebase、flaky test 维护，以及定期抓取用户反馈并聚类。
- Loop 与 sub-agent 不同：sub-agent 是任务分派，loop 是时间或状态驱动的持续运行。
- Anthropic 后续将这一方向产品化为 Routines：即使本地电脑关闭，后台循环仍可继续运行。
- 当模型开始主动建议“我可以每 30 分钟检查一次并报告”时，说明 loop 正从人类手写 cron 变成模型可理解的工作模式。
- 这一模式是 [[Product-Overhang|产品能力溢出]] 的例子：模型已经能完成持续照看类任务，产品界面和权限模型才开始追上。

## 与自动化层的关系

| 层级 | 关注点 | Agent Loops 的位置 |
|------|--------|--------------------|
| 单次 prompt | 完成一次请求 | 不够，状态不会持续被检查 |
| Sub-agent | 并行拆分任务 | 可作为 loop 内部执行者 |
| Loop / Routine | 定期检查、修复、汇总 | 时间驱动的持续自动化 |
| Harness | 权限、状态、验证、日志和失败恢复 | 管理 loop 的边界和后果 |

因此，Agent Loops 不是替代 [[Agent-Harness|harness]]，而是 harness 内的一种调度形态。真正生产化时，loop 必须被权限、预算、日志、幂等性、回滚和外部验证包住。

## Andrew Ng 的三层循环模型（2026-06）

Andrew Ng 将 Loop Engineering 分解为三个不同时间尺度的循环：

| 循环 | 时间尺度 | 驱动者 | 核心活动 |
|------|---------|--------|---------|
| **Agentic Coding Loop** | 分钟级 | AI Agent | 写代码 → 测试 → 迭代直到无 bug |
| **Developer Feedback Loop** | 几十分钟到小时级 | 人类开发者 | 审查产品 → 引导 Agent → 做高层产品决策 |
| **External Feedback Loop** | 小时到周级 | 用户/市场 | 用户反馈 → A/B 测试 → 驱动产品愿景演化 |

关键洞察：随着 Agentic Coding Loop 的成熟（Agent 能自我测试），开发者角色从 QA 升级为产品决策者。Ng 的 coding agent 可以独立工作约 1 小时，多次用浏览器检查构建结果后才回来。

Ng 将人类在 Developer Feedback Loop 中的不可替代性归因于 **[[Context-Advantage]]**——人类比 AI 知道更多关于用户和产品运行上下文的信息，这不是"品味"而是信息不对称问题。只要人类知道 AI 不知道的东西，Human-in-the-loop 就是必需的。

## Claude Code 官方四种循环分类法（2026-07）

Anthropic Claude Code 团队（delba_oliveira）按**触发机制和停止条件**将 Loop 分为四种类型，与 Andrew Ng 按时间尺度的分类互补：

| Loop 类型 | 触发方式 | 停止条件 | Claude Code Primitive | 适用场景 |
|-----------|---------|---------|----------------------|---------|
| **Turn-based** | 用户 prompt | Claude 判断任务完成 | 手动 prompt | 探索性或一次性短任务 |
| **Goal-based** | 实时 prompt | 目标达成 OR 最大 turn 数 | `/goal` | 有可验证退出标准的任务 |
| **Time-based** | 时间间隔 | 用户取消 OR 工作完成 | `/loop`, `/schedule` | 周期性工作、对接外部系统 |
| **Proactive** | 事件或计划 | 每次任务目标达成 | `/schedule` + `/goal` + auto mode + dynamic workflows | 持续的、定义明确的工作流 |

**关键设计原则**：

- **Loop 输出质量取决于围绕 loop 的系统**：保持代码库整洁、编码验证步骤为 SKILL.md（让 Agent 自验证）、文档易达、独立 agent 做代码审查（fresh context 避免自我偏见）
- **Token 管理分层策略**：选择正确的 primitive 和模型、定义清晰成功/停止条件、pilot before large run、脚本化确定性工作、匹配 routine 频率与被监控对象变化频率
- **编码异常为系统改进**：当单个结果不达标时，不只修复单个问题，而是编码为系统改进，惠及所有未来迭代

**与 Andrew Ng 三层模型的关系**：Ng 按角色和时间尺度划分（coding / developer feedback / external feedback），ClaudeDevs 按操作原语划分。Turn-based 和 Goal-based 对应 Ng 的 Agentic Coding Loop，Time-based 对应 Developer Feedback Loop 的自动化版本，Proactive 对应 External Feedback Loop 的持续运行版本。

## 控制论视角：Loop Engineering 即 Cybernetics（2026-06）

PeyMonee 指出 Loop Engineering 并非新学科，而是 Norbert Wiener 1948 年**控制论（Cybernetics）** 在 AI Agent 时代的重新发现。词源是希腊语 steersman（舵手）——Agent 就是需要被驾驭的决策者。

从控制论提取的五条结构原则：

| 原则 | 控制论对应 | Agent 工程映射 |
|------|-----------|---------------|
| Loop 是工作单元，不是任务 | 系统视角 | 人从 loop 内执行者升级为 loop 作者，模型是子程序 |
| Permission ≠ Correctness | 独立观测器 | guardrails（是否被允许）和 verification（是否正确）是不同问题 |
| 无停止条件 = 无限回归 | Governor / 调速器 | 设上限、检测停滞、超出包络时升级到人类 |
| Skills 复合，prompts 蒸发 | 模块化设计 | 命名良好的 skills 持续增值，每次重新推导只消耗 token |
| Encode the what not the how | 目标导向控制 | 指定目标、边界和完成定义，让模型选择路径 |

**核心洞察**：Agent 自动化（编码、合规、客户运营）始终是同一个动作——**定义目标、画包络线、检查结果、命名负责人**（"Define the goal, draw the envelope, check the result, name the owner"）。这与 [[Human-Governor-Agent-Operator]] 和 [[Escalation-Based-Human-Oversight]] 中的升级机制形成理论呼应。

## 分层验证模式（07-10 深度思考）

Agent Loop 的验证不是二选一（"要不要对抗性审查"），而是四层分级体系，每层覆盖不同可判定性的错误：

| 层级 | 验证方式 | 触发条件 | 成本 | 覆盖范围 |
|------|---------|---------|------|---------|
| L1 | 编译器/测试/lint | 始终（每次代码变更） | ~0 | 语法/类型/基本行为（完全可判定） |
| L2 | Property-based testing + 变异分析 | 始终（每次功能变更） | 低 | 不变量保持/边界条件（大部分可判定） |
| L3 | 对抗性审查（独立 reviewer agents） | T×S > θ 时（条件触发） | 3x | 语义一致性（半可判定） |
| L4 | 人类审查 | L3 标记异常时（升级触发） | 极高 | 架构意图/业务逻辑/品味（不可判定但可直觉） |

**升级规则**：当前层的三前提（SNR/变异分析/延迟）不再全部满足时 → 升级到下一层。

**密度公式**：d* = f(T × S / M)，T = 尾部成本（出错最大影响），S = 语义复杂度（行为等价性难度），M = 过程成熟度（已有验证基础设施）。T×S/M 高 → 全密度 L3；中等 → 关键路径 L3；低 → L1+L2 足够。

**触发式审计**（非定期式）：SPC 为底 → 变异指标超阈值时启用 L3 → 审计正常后回退 SPC。定期审计假设错误线性累积，但 AI 错误是相变的（自组织临界性）——触发式更匹配实际错误分布。

**案例验证**：Bun 百万行 Zig→Rust 重写（2026-07）使用 64 并发 AI 实例 + 1:2 对抗审查比，11 天完成，\$165K，仅 19 个语义回归逃逸。实际做法是触发式——关键路径（跨 crate 接口/内存管理/编译密集区）用 L3，胶水代码仅过 L1。来源：07-10 深度思考（roundtable+think+qa）

**理论基础**：AI agent 的错误分布是分形的——可判定区域（编译/类型）近似正态分布（Deming SPC 足够），不可判定边界（语义等价性，Rice 定理）肥尾涌现（需要 Taleb 式尾部对冲）。对抗性审查的本质是**肥尾截断器**，通过视角多样性 × 错误模式丰富性 × 独立 reviewer 数量截断肥尾指数，但有不可逾越下界（所有参与者共享同一不可判定性）。

## Loop 设计空间四宪法（07-10 深度思考）

Agent Loop 的设计不是 one-size-fits-all——不同任务类型需要根本不同的 loop 参数。以下四条约束构成 loop 设计的"宪法"：

### 1. 外部终止定理

> [!important] 终止悖论
> 最需要停止时最不能判断应该停止。退化的 agent 无法检测自己的退化（自指必然）。这是 Gödel 不完备定理的工程推论——足够复杂的系统包含不可自检测的失败模式。

**设计推论**：终止判断必须来自外部——fresh context reviewer（Bun 案例）、编译器/测试（客观信号锚）、人类（最外层）。完全自主的 loop 是逻辑不可能。来源：07-10 深度思考（roundtable+think+qa）

### 2. 人类介入凸性定理

人类介入频率是**凸函数**——平时极低（保护认知、防增强陷阱），复杂度突变时急剧上升（algedonic signal 触发）。

- **Algedonic signal**（VSM 术语）：客观信号锚检测到异常时自动升级人类介入。例：编译错误激增、测试失败模式变化、性能退化
- **20-30% 最低不确定性密度**集中在复杂度突变点——这些点是默会知识获得最大密度的时刻
- 均匀介入既不经济（浪费注意力）又有害（增强陷阱）

来源：07-10 深度思考（roundtable+think+qa）

### 3. 嵌套终止架构（VSM 映射）

Beer 的可行系统模型（VSM）定义了五层嵌套 loop，每层由上层终止：

| 系统 | 功能 | Loop 频率 | 可否完全自主 | 人类角色 |
|------|------|-----------|-------------|---------|
| S1 | 执行（做事） | 秒~分钟 | ✅ 可以 | 旁观者 |
| S2 | 协调（解决冲突） | 分钟~小时 | ✅ 大部分 | 异常裁决 |
| S3 | 控制（资源分配） | 小时~天 | ⚠️ 部分 | 优先级设定 |
| S4 | 智能（感知变化） | 天~周 | ❌ 不可以 | 共同感知 |
| S5 | 政策（定义身份） | 月~年 | ❌ 不可以 | 主导 |

**关键**：S4-S5（感知变化 + 定义身份）= 框架判断力 = 永远需要人类。这与"框架判断力不退化——前提是保留判断权"精确对应。来源：07-10 深度思考（roundtable+think+qa）

### 4. 反脆弱替代

在隔离容器中，让失败自己说话——替代多层审批延迟。

- **脆弱系统**（失败不可隔离）→ 需要多层预防审批（高延迟但安全）
- **反脆弱系统**（失败可隔离，如 Bun 的 64 worktree）→ 让失败自己终止（低延迟，失败即信号）
- **选择标准**：失败可隔离性决定位置。安全关键系统用多层审批，代码生成用反脆弱隔离

来源：07-10 深度思考（roundtable+think+qa）

## Loop 定理观察性析因与权重裁决（08-03 深度思考）

外部终止定理（四宪法 #1）的 2³ 验证设计已完成首次观察性析因：库内 5 篇 loop 工程文献 + HF/ExploitGym/Ralph/恒温器共 16 行实践，按 A（变差函数来源）× B（反馈耦合）× C（参照层监控）编码为 6-cell 分布，裁决三竞争理论（Dijkstra A 主效应 / Wiener A×B 交互 / Boyd C 条件效应）。

### Cell 分布实测

| cell | A × B × C | 落点 | 性质 |
|------|-----------|------|------|
| 1 | 外×耦合×高 | 控制论规范 loop、Ng 开发者反馈 loop、Claude Code Turn-based（LangChain hill climbing 触及） | 全人类载体 |
| 2 | 外×耦合×低 | 验证 loop（tests/rubric/确定性标准）、Ng coding loop、/goal、/loop | **最密：工程共识区** |
| 3 | 外×脱钩×高 | 库内空（学科分区，见下） | 空白 |
| 4 | 外×脱钩×低 | HF 入侵案、ExploitGym、Ralph 状态文件脱钩侧 | **失败案例区** |
| 5 | 内×耦合×低 | ByteByteGo agent loop（模型自判停止）、LangChain L1 裸 loop、恒温器 | 原始 loop |
| 6 | 内×脱钩×低 | 不可运行（完全自主定义本身），但病理描述反复出现（"删掉失败测试宣布 shipped"） | 定理实物化 |

### 权重裁决 = 三剖面分治

三预测非互斥竞争者，而是同一结构的三个剖面：**A 主效应 = 投资剖面**（cell 2 密度 + "更便宜的验证步骤比更强的基础模型带来更大性能提升"社区洞察）；**A×B 交互 = 失败剖面**（HF/ExploitGym 都是 A=外——最昂贵的失败都在 A 在场但 B 脱钩处，A 的投入不能免疫 B 脱钩）；**C 条件效应 = 边界剖面**（cell 1 全人类，C 骑在 A 上出现，从不替代 A）。

### 本体论改写：三时间尺度与 C 分裂

- **A/B/C = 设计时/运行时/演化时**：A（谓词声明）已制度化，B（通道耦合）已例行化，C（标准修改）**定义性不可制度化**——制度化 = 固定标准，而 C 的行为恰是修改标准。三条件合取形式保持，但 C 应从状态读法（"参照层被监控"）改为通道读法（"现实与异源解读的通道不被堵塞"）。
- **C 分裂为二**：可见规格守卫（可制度化）+ 不可见定向携带（不可自动化，mētis 残差决定人审形态：CI 门禁=小残差，产品判断=大残差）。
- **经验边界精确化**：不是"参照层需要外部来源"，而是**实现/规格界限需要外部守卫**——任何机制一旦能修改充当规格之物，必须被外部终止。LangChain hill climbing loop"harness 改进应经人类审查后部署"是现成判据实例（harness 充当规格）。
- **cell 3 空白 = 学科分区**：loop 工程文献占据 cell 2（预设参照层可信），评测安全/审计文献占据 cell 3/4（专处理脱钩与定向污染）。meta-evaluation 学科（Scriven 1969 命名、Stufflebeam 2001《The Metaevaluation Imperative》）确证 cell 3 在组织实践中存在（评估之评估），同时确证"审计者后退"结构（MEC 清单显式承认自身需被评估）。
- **判据的判据 = 赌注方向**（08-03 追本）：审查是对地图的质疑还是地图内运算，看审查者的生存押在地图正确性上（→ 地图内运算）还是领地状态上（→ 质疑地图）；制度化审查 = 过去赌注的遗骸。接 [[Over-Compliance]] 与遗骸化定理。

**自指警告**：本裁决的 cell 表格本身正在成为新参照层——引用它声称"我们的 loop 在 cell 2 所以安全"，恰是 cell 4 的开始。

来源：08-03 深度思考（roundtable 戴克斯特拉/维纳/博伊德/斯特拉森/斯科特 + think + qa + 联网）；synthesized/medium，16 行 cell 编码 extracted 支撑，待更多案例校准。详见 [[2026-08-03]] 09:33 区块。

## 前提与局限性

- **错误累积**：Agent 每 30 分钟犯一次小错，几天后可能变成系统性污染。
- **权限膨胀**：后台 agent 若拥有写权限、生产权限或自动合并权限，必须有更强审计。
- **上下文漂移**：长期运行的 loop 会遇到需求、代码和环境变化，需要重新加载真实状态。
- **成本不可见**：定时循环会持续消耗 token 和工具调用，必须有预算上限和效果指标。
- **验收外置**：修 CI、改 PR、聚类反馈都需要测试、review、日志或人工确认作为完成标准。
- **增强陷阱（Augmentation Trap）**：Loop 的人类监督者面临技能退化风险。Caosun & Aral (2026) 证明即使完全预见退化，决策者仍理性选择 AI（短期收益 > 长期代价）。Liu et al. (2026, N=1222) 发现仅 ~10 分钟 AI 辅助后人类独立表现显著下降。人类参与线（Loop 自我改进的天花板）本身是一个需要持续维护的耗散结构。来源：07-09 深度思考（roundtable+think+qa+联网）

## 技术分类：四维框架（07-17 扩展）

Loop Engineering 涉及约 17 种技术。单维度"核心 vs 外围"分类不够。四维框架（Beck/Fowler/Kim/Wardley 圆桌）：

| 维度 | 提出者 | 含义 | 示例值 |
|------|--------|------|--------|
| 失效模式 | Beck | 技术对抗哪种 loop 失效 | 做错/做不完/做太慢/没人管 |
| 依赖层次 | Fowler | 技术间的依赖关系 | L0基础→L1增强→L2治理 |
| 组织成熟度 | Kim | 谁在运行和维护 loop | 个人→小团队→平台 |
| 演化阶段 | Wardley | 技术处于哪个商品化阶段 | Genesis→Custom→Product→Commodity |

**关键洞察**：
- "核心"不是固定的——沿演化轴向下移。Genesis 期 L0=核心；Commodity 期 L1/L2=核心（L0 已被平台内置）。
- 不存在抽象分类——分类 = f(任务类型)。代码生成和自动驾驶所需的"核心"技术不同。
- 迁移路径由组织成熟度决定起点——个人从 L0 开始，平台团队从 L2（配置）开始。

## 关联概念

- [[Claude-Code-Automation]] - Agent Loops 是 Claude Code 自动化的时间驱动层
- [[Product-Overhang]] - 模型能力已经能承担后台照看，产品正在补足界面
- [[Agent-Harness]] - 生产 loop 需要 harness 管理权限、状态和验证
- [[Agent-Swarm]] - 大量 loop 可能形成持续运行的 Agent 群
- [[Agent-Workflow-Patterns]] - Loop 是 agent workflow 的一种调度模式
- [[Loss-Function-Development]] - LFD 将 /goal loop 推向外层梯度下降，超越 spec-driven development
- [[Agent-Verification]] - 控制论视角下 verification 是独立于 permission 的必要检查
- [[Human-Governor-Agent-Operator]] - Governor 概念：设上限、检测停滞、超出包络时升级
