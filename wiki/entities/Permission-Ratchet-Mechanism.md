---
type: entity
title: Permission-Ratchet-Mechanism
aliases:
  - Permission Ratchet Mechanism
  - 权限蠕变棘轮定理
  - 权限撤销成本不对称
  - Permission Creep Ratchet
definition: "一个 synthesized 权限治理模型：长期授权可能因依赖积累、触发不足、重授成本与责任分配而形成撤销阻力。模型用制度补偿缺失解释部分权限蠕变现象，并提出持久授予、休眠不可观测与补偿不足会增强棘轮效应；各条件的必要性、充分性和量化强度仍待实证。"
created: 2026-07-16
updated: 2026-11-28
evidence_level: medium
claim_type: synthesized
tags:
  - security
  - governance
  - incomplete-contract
  - AI-Agent
related_entities:
  - "[[Plan-is-the-Permission]]"
  - "[[Zero-Friction-Scope-Creep]]"
  - "[[Policy-as-Code-for-Agent-Governance]]"
  - "[[Distinct-Principal-Identity]]"
  - "[[Default-Side-Asymmetry]]"
  - "[[Human-Owns-Output]]"
source_raw:
  - "[[20260708-vercel-agent]]"
  - "[[20260419-agent-harness-engineering]]"
  - "[[20260805-how-we-use-ai-cloudflare-os]]"
---

# Permission-Ratchet-Mechanism（权限蠕变棘轮模型）

> [!warning] 知识身份
> 本页是 `claim_type: synthesized` 的机制模型，不是已证明的“权限棘轮定理”。它把多种理论与工程案例组合成解释链，用于生成可测预测；正文中的必要/充分关系应以“候选机制”理解，直到有独立实证支持。

> [!definition] 当前定义
> 长期授权可能因依赖积累、休眠权限缺少触发信号、重授成本和责任/收益分配不对称而形成撤销阻力。该模型提出“持久授予 + 休眠不可观测 + 补偿不足”会显著增强权限棘轮，但三条件是否严格必要或充分、不同制度中的效应量多大，仍需数据验证。

## 候选因果机制

初始授予/拒绝与撤销的成本可能不同，但并非固定大小关系。撤销可能涉及已积累的依赖、迁移、责任与补偿；初始拒绝也可能造成关键业务中断和高昂论证成本。历史研究曾以 Coase、Hart、Brooks、Taleb 的概念作类比，不是这些作者提出或证明了本模型。

| 层 | 可能的阻力 | 可观察量 |
|---|---|---|
| L1 执行 | 下游依赖、重授或迁移成本 | 撤销耗时、业务中断、恢复成本 |
| L2 触发 | 休眠授权未进入复核议程 | 复核间隔、告警覆盖、owner 缺失 |
| L3 判定 | 对未来需求和误拒代价不确定 | 授权必要性证据、误拒/误保留率 |

未来使用的不确定性并不等于无法决策；有界任务、周期复核、风险判据及失效后的重授机制可减少判定与执行负担。L2/L3 是否比 L1 更重要须实测，不预设成本量级。

## Agent 与人类的比较

人类和 Agent 都可能有长期或临时身份；员工转岗不必然自动撤销，Agent 也可以绑定任务、租约和 owner。日志及社会反馈可用于识别需求，但其完整性和作用依组织设计而定。缺少申诉可能同时减少撤销阻力和需求信号，净效应尚不明确。

## 三条件叠加假说

当前模型把以下三项视为**高风险组合**，而不是已经证明的严格必要充分条件：

1. **持久授予**（无自然过期）——对应 Hart 权力方向不可逆
2. **休眠不可观测**（未来需要不可证伪）——对应 Taleb 风险感知
3. **无补偿**（撤销成本压撤销者、收益归全局）——对应 Coase 制度补偿缺失

现有案例为这些因素提供机制线索，但尚不足以证明“全满足才会出现棘轮”或 agent 必然最重。后续应通过撤销延迟、重授成本和权限利用率等数据估计各条件的独立效应与交互。

## 工程对策与局限

[[Plan-is-the-Permission]] 是降低常驻授权风险的候选工程机制。按 Vercel 产品描述，平台逐次核对短期 capability、token scope、团队权限；并非消灭所有常驻权限。高频任务可采用有界批量授权或自动化策略，适用性取决于实际风险、粒度与审批成本，尚未测出固定阈值。详见 [[Default-Side-Asymmetry]]。

## 预防式对策：Cloudflare 的 never-more-permission（08-06 补充）

Cloudflare Cloudflare OS 提供**预防式**的棘轮对策——侧重预防越界与权限复制，而非解决全部撤销问题（来源 [[20260805-how-we-use-ai-cloudflare-os]]）：

| Cloudflare OS 机制 | 对棘轮的预防机制 |
|-------------------|-----------------|
| 原则 5「用 AI 时权限绝不越界」 | 设计约束层面：agent 权限 ≤ 使用者既有权限，旨在限制授予时超发，依赖实际执行与身份映射 |
| ephemeral 云环境 | agent 只访问会话内引入的数据，不携带本机全部凭据——缩小可蠕变权限的初始面 |
| gatekeeper 分享语义（共享即重新认证） | agent 共享时继承**接收者**权限而非创建者权限——降低共享时继承创建者权限的风险；不等于证明无持久权限副本 |
| MCP Portal + 自建 MCP server | 每个系统记录按角色/地区限流，权限边界下沉到连接层 |
| AI Gateway | 推理全量路由：DLP 阻断敏感数据外发 + 按角色门控模型——运行时约束 |

**对棘轮三条件的针对性**：gatekeeper 的接收者权限语义与 ephemeral 环境可分别缩小共享权限与运行环境暴露面；不能据此保证无持久凭据、外部会话、共享状态或无人认领授权。

**与 Plan-is-the-Permission 的关系**：Plan-is-the-Permission 治"撤销成本高"（临时授权随计划闭合）；never-more-permission 治"越界与复制"（共享即重新认证）。二者互补：前者让权限有自然终点，后者让权限不扩散。**未覆盖盲区**：文章未提 agent 权限的**授予后收缩/过期审计**（棘轮 L2 触发层），"授予后权限漂移"仍缺对策（综合判断，见 source summary 质疑）。

## 棘轮适用域

| 维度组合 | 棘轮强度 |
|---------|---------|
| 持久权限 + 高频使用 + 远期风险 | 候选高风险区；使用频率不等于依赖强度或撤销阻力 |
| 临时权限 + 低频使用 + 近期风险 | 候选较低风险区；自动续期与隐含依赖仍可能产生棘轮 |

证伪路径：预先定义撤销延迟、重授成本和依赖强度，比较不同授权生命周期与可观测性；若控制任务、依赖及风险后长期授权未增加撤销阻力，或补偿机制无预测效果，应收窄或拒绝相应命题。

## 关键数据点

- Vercel Agent 默认只读 + 计划驱动授权 + 即时回退（[[20260708-vercel-agent]]）——Plan-is-the-Permission 作为棘轮对策的厂商实现描述（尚非独立有效性实证）
- 07-14 圆桌共识：agent 活动半径不是设计的，是权限积累的结果；同一 agent 在约束期→生长期→蔓延期漂移
- 企业员工和 Agent 权限都可能累积；尚无可比数据证明 Agent 棘轮普遍更强
- **负案例（07-22 核查）**：PocketOS 删库事件**不在棘轮域内**——权限未蠕变、未休眠、未拒绝撤销，是 agent 在任务中**自主捡拾过度暴露的生产 token**（凭证获取层失效）+ API 权限本身合法（delete-volume）+ 违反明确禁令，9 秒成灾。棘轮定理的适用域需排除"自主捡拾可及凭证"这一新机制：棘轮管"授予后不撤销"，捡拾管"未授予但可及"。详见 [[Agent-Failure-Causal-Chain]] PocketOS 案例节（来源：Jeremy Crane postmortem, X 2026-04-27，二手交叉验证，raw 待剪藏）

## 前提与局限性

- 本模型是 synthesized 判断（Coase 交易成本 + Hart 不完全契约 + Brooks 概念完整性 + Taleb 非对称风险四视角综合），未经独立实证。
- "撤销成本 >> 拒绝成本"的量化比值未测；07-14 下一步明确为"测量权限授予后的撤销延迟分布"，仍待实证。
- lobby 双刃的净效应（消除政治阻力之利 vs 消除触发信号之弊）待实证：追踪"无 owner 休眠 agent 权限"撤销频率 vs"有 owner 活跃权限"撤销频率。
- 三条件的必要性、充分性与交互效应尚未建立；不同系统需要通过观测或实验检验，不能从假说本身推导棘轮必然存在。

## 关联概念

- [[Plan-is-the-Permission]] — 棘轮的工程对策（对称反例局部实现）
- [[Zero-Friction-Scope-Creep]] — 范围蔓延是权限蔓延的近亲，同构
- [[Default-Side-Asymmetry]] — 默认决策与授权生命周期成本的关联假说
- [[Policy-as-Code-for-Agent-Governance]] — 运行时权限约束的治理方法
- [[Distinct-Principal-Identity]] — agent 身份双问题，权限的载体
