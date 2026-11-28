---
type: entity
title: Agent Loops
aliases:
  - Agent Loops
  - Agent 循环调度
  - 时间驱动 Agent
definition: "让 Agent 按时间或事件持续运行、检查状态、修复问题和汇总反馈的自动化编排模式"
created: 2026-05-08
updated: 2026-11-28
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
  - "[[20260906-lenny-companies-series-loops]]"
  - "[[20260924-github-security-lab-ai-fuzzing-taskflow]]"
  - "[[20261014-lovable-growth-tools]]"
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

因此，Agent Loops 不是替代 [[Agent-Harness|harness]]，而是 harness 内的一种调度形态。生产化时按风险约束权限、预算、日志和完成判据；有外部副作用时另核幂等、对账与适用的恢复能力。

## Andrew Ng 的三层循环模型（2026-06）

Andrew Ng 将 Loop Engineering 分解为三个不同时间尺度的循环：

| 循环 | 时间尺度 | 驱动者 | 核心活动 |
|------|---------|--------|---------|
| **Agentic Coding Loop** | 分钟级 | AI Agent | 写代码 → 测试 → 迭代直到无 bug |
| **Developer Feedback Loop** | 几十分钟到小时级 | 人类开发者 | 审查产品 → 引导 Agent → 做高层产品决策 |
| **External Feedback Loop** | 小时到周级 | 用户/市场 | 用户反馈 → A/B 测试 → 驱动产品愿景演化 |

关键洞察：随着 Agentic Coding Loop 的成熟（Agent 能自我测试），开发者角色从 QA 升级为产品决策者。Ng 的 coding agent 可以独立工作约 1 小时，多次用浏览器检查构建结果后才回来。

Ng 将人类在 Developer Feedback Loop 中的不可替代性归因于 **[[Context-Advantage]]**——人类比 AI 知道更多关于用户和产品运行上下文的信息，这不是"品味"而是信息不对称问题。若缺失信息影响任务决策，可通过授权获取、澄清、专家接管等方式补足；信息差本身不证明每一轮都需要人工介入。

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

## Coverage-Driven Loop：把停止条件放到模型外（2026-09）

GitHub Security Lab 的 fuzzing Taskflow 是 Agent Loop 的一个很硬的工程实例。Loop 不是简单反复调用模型，而是：

**运行 fuzzing → 测量真实 coverage → 识别 gap → 修改 harness/input → 再运行**。

其中最值得迁移的是终止语义：系统不让模型凭主观感觉宣布“完成”，而是用 coverage plateau 检测 diminishing returns；当连续迭代收益低于阈值时退出该目标。

**判断**：Loop 的自治程度取决于反馈信号是否客观、廉价且外部于模型。越接近编译、测试、coverage 这类机器可测信号，越适合让 Agent 长时间自动 hill-climb；越接近 exploitability / architecture intent 等语义判断，越需要升级给人。

这提供了外部 stop predicate 作为计算预算控制器的工程实例，并不证明终止谓词可充分保证安全或任务正确。

- **证据**：[[20260924-github-security-lab-ai-fuzzing-taskflow]]，“The coverage-feedback loop”；文章还把持久 corpus 跨 iteration/campaign 保存，使每轮反馈能累积而不是重复探索。
- **边界**：coverage 上升不等于漏洞价值上升；最终安全 verdict 仍需人类复核。

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

## 分层验证与终止条件（2026-11-28 校准）

按任务风险、反馈质量和可检验性选择验证手段，不要求所有循环使用同一层级或固定审查比例。

| 手段 | 可验收对象 | 边界 |
|---|---|---|
| 编译、lint、确定性测试 | 指定语言规则与已编码断言 | 测试通过不代表所有行为正确，成本亦不为零 |
| 属性测试、变异分析 | 指定属性及测试对选定变异的敏感性 | 不穷尽输入空间或语义缺陷 |
| 独立实现、模型复核 | 指定错误类别、不同证据或实现的交叉检查 | fresh context / 不同家族不保证错误独立 |
| 业务专家及用户验收 | 需求、实际后果、风险与取舍 | 人审同样可能漏检，应有明确输入、判据与责任 |

分开定义三类停止：

- **资源停止**：步数、时间、预算、取消或执行边界限制；避免无界消耗，但不能证明任务正确完成。
- **目标停止**：任务成功谓词、覆盖率平台期、无可执行剩余任务等；判据须与任务目标相符，必要时独立复核。
- **风险停止**：超授权、异常、状态冲突、危险动作及无法核验的外部效果；按风险阻断、升级或对账，停止调用不撤销已发生的效果。

内置且有界的循环可以终止，不需要每次由人或独立 Agent 决定。例如对有限列表逐项处理、每轮减少剩余项数且禁止新增项，在每步返回的假设下自然终止。形式化程序可用良基变差函数证明终止，但终止性质不等于目标达成或安全；模型生成判据也不因此获得任意改变授权和验收标准的权力。对于可改写自身判据、有外部副作用或高风险的 Agent Loop，宜把关键资源/授权门置于不受该运行任意修改的执行点。

**证据边界**：[[20260924-github-security-lab-ai-fuzzing-taskflow]] 展示 coverage feedback 与 plateau stop；作者仍有执行风险提示及人审需求，不证明外部停止普遍必要或安全充分。[[20260617-langchain-art-of-loop-engineering]] 描述多类循环与部署前复核；[[20260706-getting-started-with-loops-claude-code]] 是产品分类及实践建议，而非控制理论证明。Bun 重写自报的审查、测试与回归数据见 [[20260708-bun-in-rust]]，本轮未回核原文或复算，不能从单案推导固定审查比例、正态/肥尾分布或错误率。

## 观察性分类与实验设计边界

[[2026-08-02]] 与 [[2026-08-03]] 中的 A（判据来源）、B（反馈耦合）、C（参照层监控）保留为诊断维度，而非四宪法或必要充分的终止定理。历史 16 行案例编码未随机化、未匹配任务与风险，未提供效应估计，故 cell 密度、空白与自然案例的差异不识别 A/B/C 主效应或交互；因定义或安全约束不实施的 cell 也不是不可能性证据。Gödel 不完备性不直接推出通用 Agent 自主终止不可能，VSM 层级也不规定永久人类专属或固定频率。

候选实验：在无真实外部副作用的可复位环境固定任务、模型、预算、初始状态和裁决；独立操纵判据来源、反馈与监控机制（若部分组合定义上不可行，则明确比较范围）。测量任务正确性、越界、提前停止、未停止/超时、成本和人工介入，单列未知终态；不以不显著判定等效。高风险生产动作不为填满设计格而放开权限；隔离与审批均按任务风险验收。此合同尚未执行。历史原文可回溯，不新增研究编号或复活旧工单。

## 从个人 Loop 到公司 Loop（2026-09）

Anish Acharya 把 Loop 从个人自动化模式推进到组织设计假设：公司可能由一组嵌套的 Loop 组成，层级从个人、岗位职能、业务单元一路上升到覆盖大部分公司的业务 Loop。每个 Loop 都应把输入转成行动、测量结果、收敛到当前最优解，再把反馈送入下一轮。

| 层级 | 典型输入 | Loop 输出 | 主要人类职责 |
|------|----------|-----------|--------------|
| 个人 | 任务、资料、请求 | 可交付结果与反馈 | 目标、上下文、验收 |
| 职能 | bug、客户反馈、实验机会 | 代码、实验、销售/支持动作 | 处理例外与跨域判断 |
| 业务 | 多职能结果、市场信号 | 业务模型、产品或战略调整 | 选择下一座山、承担结果 |

访谈中的 growth 例子是一个可观察的职能 Loop：生成实验变体 → 测量 → 达到统计标准后发布 → 设置长期 holdout → 进入下一实验。coding 的 bug-fix 也有类似结构：复现 → 修复 → review → 按风险决定是否进入生产。关键不在“每个环节都由 Agent 完成”，而在输入、完成标准、反馈与升级路径被显式化。

**局部最优是 Loop 的边界**。Loop 可以在既定指标空间里 hill-climb，却可能停在 local maxima；当需要跳到下一座山时，仍要有人提出出分布的新问题、识别指标之外的价值或改变业务约束。人类的销售、支持、战略和例外判断因此不是残余岗位，而是把 Loop 从一个局部优化器重新定向到更大目标的控制层。

**教练式升级是学习回路**。Kavak 的案例是：Agent 卡住时调用人类，人类补上缺失的知识或数据；Agent 保存这次交互的 traces，下一次减少同类求助。这个模式只有在 traces 可审查、可归因、可回归时才会产生组织学习，否则只是把一次人工救火误称为“模型变聪明”。

这把 [[Agent-Unit-of-Work|Agent 工作单元]] 与组织层的 [[Organization-as-Agent-Harness|组织 Harness]] 接起来：组织要做的不是给每个 Loop 无限权限，而是为每个 Loop 定义目标、可测量空间、预算、停止条件、owner 和向上升级路径。

### Lovable：从生成应用到经营 Growth Loop（2026-10）

[[20261014-lovable-growth-tools]] 把本页已有的 growth loop 从组织抽象落成一个端到端产品实例。用户先给 business outcome（如 first 100 signups / more bookings），Lovable 复用 app、audience、traffic 与 brand context 生成计划，再执行 SEO、landing page、Google/Meta Ads、creative assets 与 analytics；campaign 运行后，结果重新进入 chat，用户可以要求 pause、改 budget、换 audience 或 copy。

~~~text
app context + goal
      ↓
growth plan
      ↓
SEO / ads / content / distribution
      ↓
conversion telemetry
      ↓
analysis + suggested adjustment
      ↓
human approval / instruction
      ↓
next action
~~~

这里最重要的不是“AI 也会做营销”，而是 **build 与 grow 被接成同一条 context-preserving loop**：构建阶段积累的产品语义不必在每个下游 SaaS 中重新解释，而可以继续驱动增长动作。

同时，这个案例保留了很清楚的控制边界：广告花钱前必须确认 budget、地域、语言、goal 与 tracking；系统不会自行启动或修改 campaign；站外帖子也由用户自己的账号发布。因此它更准确地属于 **approval-gated execution loop**，而不是完全自治的 growth agent。

- **证据**：[[20261014-lovable-growth-tools]]；目标→计划、Google/Meta 广告、Analytics 回流、approval-before-spend 与 SEO/creative sections。
- **边界**：来源是 Lovable 产品公告，没有 CAC、conversion uplift、retention 或对照实验，支持的是 loop 结构与权限边界，不支持“增长效果已经改善”的结论。

## 前提与局限性

- **错误累积**：Agent 每 30 分钟犯一次小错，几天后可能变成系统性污染。
- **权限膨胀**：后台 agent 若拥有写权限、生产权限或自动合并权限，必须有更强审计。
- **上下文漂移**：长期运行的 loop 会遇到需求、代码和环境变化，需要重新加载真实状态。
- **成本不可见**：定时循环会持续消耗 token 和工具调用，必须有预算上限和效果指标。
- **验收外置**：修 CI、改 PR、聚类反馈都需要测试、review、日志或人工确认作为完成标准。
- **增强陷阱（Augmentation Trap）**：监督者的独立判断与技能再生可能受工作方式影响，需在真实任务与适当对照下测量，而非由使用 AI 的时间直接推定永久退化。参见 [[Augmentation-Trap]]、[[Skill-Atrophy-and-Knowledge-Debt]]；旧 07-09 推演及未经本轮回核的数字不作本页事实。

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
