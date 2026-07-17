---
type: entity
title: Delegative-UI
aliases:
  - Delegative UI
  - 委派式交互
  - Slow Dialogue
  - 慢速对话
definition: "Delegative UI 不是 Conversational UI 的对立面，而是同一对话光谱上回合粒度更大、反馈带宽更低的区域——人一次性陈述目标与约束后放手，agent 自主执行，人在循环外定期验收。本质 = 慢速对话，核心代价 = 错误心理模型复利增长。"
created: 2026-07-17
updated: 2026-07-17
evidence_level: medium
claim_type: synthesized
tags:
  - interaction-design
  - AI-Agent
  - human-agent-interaction
  - delegation
  - organization
related_entities:
  - "[[Flattening-as-Governance-Consequence]]"
  - "[[Judgment-Degradation-Cascade]]"
  - "[[Permission-Ratchet-Mechanism]]"
  - "[[Carbon-Silicon-Division]]"
  - "[[ACI-Agent-Computer-Interface]]"
source_raw: []
---

# Delegative UI（委派式交互）

> [!definition] 定义
> **Delegative UI** 不是 Conversational UI 的对立面——两者共享"对话"这一基本结构。Delegative UI = **慢速对话**（slow dialogue）：回合粒度从秒/分钟级变为小时/天级，反馈带宽从全带宽（过程体感）变为窄带（结构化结果摘要），意图密度从低（渐进式澄清）变为高（一次性打包目标+约束+验收标准+异常升级规则）。

## Suchman 穿透：对话光谱而非类别二分

Delegative 和 Conversational 的根区别不在"是否对话"——在对话的**回合粒度**和**反馈频率**。Suchman（圆桌，2026-07-17）指出：Delegative 中的"元操作"（阅读 agent 输出→发现偏差→修正前提→agent 再产出）本身就是一种对话——只是对话对象从人变成了 agent，回合粒度加大了。

`交互范式 = f(回合粒度, 反馈带宽, 意图密度)`

| 维度 | Conversational UI | Delegative UI |
|------|-------------------|---------------|
| 回合粒度 | 秒~分钟 | 小时~天 |
| 反馈带宽 | 全带宽（过程体感/阻尼/犹豫） | 窄带（结构化摘要/结果报告） |
| 意图密度 | 低（渐进式澄清，每轮携带少量意图） | 高（一次性打包全部前提） |
| 代价结构 | 交互成本（多轮对话的时间） | 歧义修正成本（前提不精确的修正轮次）+ 错误模型复利 |

## Norman 2×2 任务边界模型

Delegative UI 的适用域由两个维度决定：

- **目标稳定性**：目标是已知的还是在使用中涌现的？
- **路径可预见性**：执行路径是可预判的还是需要探索的？

```
            目标已知              目标涌现
          ┌──────────────┬──────────────────┐
路径可预判 │ Delegative ✓ │ 不适合 Delegative │
          │ (发送邮件报表) │  (先Conversational找目标) │
          ├──────────────┼──────────────────┤
路径不可预判│ Delegative + │ Conversational ✓  │
          │ 异常升级     │ (探索+创作)        │
          └──────────────┴──────────────────┘
```

**形式化**：`Delegative 可行 ⇔ (目标已知 ∧ 路径可预判)`。`需要 Conversational ⇐ (目标涌现 ∨ 路径不可预判)`。

混合模式：同一人在同一工作日内的切换——上午 Conversational 探索目标，下午 Delegative 执行已知目标。

## 错误心理模型复利增长定理（Simon 级联）

慢速对话的致命代价不是"一次性歧义修正成本"——而是**错误心理模型的复利增长**。

```
反馈延迟(f↓)
  → 错误心理模型存活时间↑
  → 用错误模型评估 agent 输出 → 产生次优前提修正
  → 次优修正产生更多输出偏差 → 更多错误模型
  → 正反馈环：认知级联
```

**形式化**：`认知代价 = 错误模型存量 × 存活时间 × 传播因子(k>1)`。存活时间 ∝ 1/f（反馈频率）。传播因子 k > 1 的证明：每个错误模型被用来评估下一轮输出，产生更多错误理解 → 错误模型不只是叠加，是**相乘**。

**缓解**（Norman 四策略）：
1. **过程可见性**：agent 持续输出中间状态（Andon 板模式）
2. **解释性中间输出**：关键决策点自动解释"为什么选这条路"
3. **可中断性**：安全介入点（像自动驾驶"随时接管"）
4. **事后溯因**：完整决策 trace，事后复盘

四策略不解决"目标涌现"问题（那需要 Conversational），但显著降低"目标已知"象限内 Delegative 的认知代价。

## 实质权威迁移定理（交互层投射）

Delegative UI 不改变形式权威（组织层级、任命权），但改变了**实质权威**的生产要素——从"占据某个职位"变为"能有效规定 agent 可执行的前提"。

- **Simon 权威二分**：形式权威（有权做决策）vs 实质权威（有能力影响决策结果）
- **旧实质权威来源**：职位 + 信息控制 + 契约化转译能力（中间层靠把上级意图翻译成 KPI/合同）
- **新实质权威来源**：前提规定能力（写 spec/prompt/acceptance criteria）+ agent 编排能力 + 验收判断力
- **推论**：有前提规定能力的人可在任何层级获得实质权威 → 去科层化的交互层机制

这是 [[Flattening-as-Governance-Consequence]]（去科层化治理后果定理）在交互层的精确投射：中间层的契约化转译职能被 agent 替代 → 组织被迫扁平 → 实质权威迁移到"前提规定者"。

## Victor-Karpathy 度量约定定理

元操作（阅读/评估/修正 agent 输出）能否等价替代直接操作以维持判断力？

追本七层（ljg-think, 2026-07-17）发现：争论的表层是经验问题（可做 RCT），中层是信息率问题（I_meta vs I_maintenance），**底层是度量约定的分歧**——什么算"判断力"、什么算"维持"、什么算"足够好"——这些标准本身是**约定**而非**发现**。

**实践含义**：Delegative UI 的安全部署边界 = **约定边界**而非技术边界。解决路径不是"做更多实验找到正确度量"——不存在"正确的"度量。解决路径是建立被广泛接受的度量约定，并让其可操作化、可审计、可争议。这是治理问题。

## 制度化缺口

Delegative UI 安全部署缺乏三个制度化要素：

`安全部署 = 约定标准 × 可审计度量 × 可问责边界`

| 要素 | 自动驾驶类比 | Delegative UI 当前状态 |
|------|------------|---------------------|
| 约定标准 | ISO 26262 / NHTSA 级别 | ✗ 无"判断力维持最低要求"共识 |
| 可审计度量 | 模拟+路测里程+脱离率 | ✗ 无标准化判断力评估工具 |
| 可问责边界 | 监管机构批准/制造商负责 | ✗ 无"谁决定/谁负责"制度安排 |

技术部署在前，治理制度化在后——滞后窗口 = 决策在"直觉过度谨慎"和"直觉过度放权"之间振荡的空间。

## 与既有理论的连接

- [[Flattening-as-Governance-Consequence]]：Delegative UI = 该定理的交互层机制投射（中间层契约化转译被 agent 替代）
- [[Judgment-Degradation-Cascade]]：慢速对话 = 判断力训练频率↓ → 可能加速退化级联
- [[Permission-Ratchet-Mechanism]]：声明性权力（一次性授予不易撤销）vs 关系性权力（持续协商可调整）
- [[Carbon-Silicon-Division]]：Delegative UI = 判断位置跃迁（从操作判断到导航判断）的交互接口
- [[ACI-Agent-Computer-Interface]]：ACI 是 agent→computer 接口；Delegative UI 是 human→agent 接口——互补视角

## 开放问题

1. 元操作 vs 操作的等价性——需要纵向实证（但底层不可解的度量约定分歧意味着实证只能缩小、不能消除分歧）
2. Ambient UI（环境式交互）——agent 在后台持续运行、通过通知/摘要"浮现"到意识中——是第三种范式吗？
3. "前提规定能力"的培养路径——如果实质权威迁移到这种能力，教育/培训如何覆盖？
4. Delegative→Conversational 向下切换的认知代价——上下文重建成本有多高？
