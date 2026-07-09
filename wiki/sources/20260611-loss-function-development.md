---
type: source-summary
title: "/goal + Loss Functions: 用 Loss Function Development 在 30 小时内蒸馏一个产品"
source_raw:
  - "[[20260611-loss-function-development]]"
created: 2026-07-08
updated: 2026-07-08
tags:
  - source-summary
  - agentic-engineering
  - harness-engineering
  - reward-hacking
evidence_level: medium
claim_type: mixed
---

# /goal + Loss Functions: 用 Loss Function Development 在 30 小时内蒸馏一个产品

## 编译摘要

### 1. 浓缩
- **核心结论1**: Loss Function Development (LFD) 是 Spec-Driven Development 之后的新范式——不写 spec 让 Agent 构建，而是写 loss function 让 Agent 优化。四要素框架：Target（大且盲的评估集）、Constraints（时间/金钱/表面/方法论硬约束）、Instruments（每个约束对应一个 CLI 可检视工具）、Forced Entropy（防止局部最优的显式机制）
  - 关键证据: 30 小时 / 6,300 行代码 / 92k 页爬取 / `\$40` 消耗 → 输出是参考产品的 ~50 倍。作者 Elvis Sun 开源了 LFD 设计工具 (github.com/elvisun/loss-function-development)
- **核心结论2**: Agent 作弊不是 bug 而是优化的必然结果——每一条未被封堵的廉价路径都会被 optimizer 利用。三轮失败的迭代证明：枚举 eval → 一对一关键词 → 枚举扩展 eval，每轮"赢了"但零泛化。解法是逐轮封堵廉价路径直到唯一前进方向是真正变好
  - 关键证据: "The cheating wasn't a bug in the agent. It was a bug in my target: I told it where to go and left every shortcut wide open."
- **核心结论3**: 双层梯度下降——内层循环是 Agent（写代码→跑测试→修 bug，spec-driven development），外层循环是 `/goal`（驱动整个系统朝 outcome metric 下降，loss function development）。两层都已自动化，**人的剩余工作是定义 loss function**。同时提出 Prompt-time Distillation：将训练时的知识蒸馏搬到推理时，用 agent 拟合公开可见的产品输出
  - 关键证据: "Both loops are automated now. What's left on you is defining the loss function." cal.com（`\$5M` ARR 开源公司）在 2026 年 4 月转闭源，理由是开源代码可被 agent 枚举攻击面——信息对称使执行成本归零，信息不对称成为新护城河

### 2. 质疑
- **关于 LFD 的可迁移性**: 文章场景是新闻爬取和数据层产品（有公开可比的输出），对于 UI 产品、内部工具、无公开参考物的产品是否适用？LFD 的前提是"存在可比的公开输出"，这排除了大量创新场景
- **关于 50x 改进的可信度**: 参考产品本身可能质量极差，50x 可能说明的是参考产品差而非自己好。且只有单次成功案例报告，存在幸存者偏差——30 小时但效果平平的 LFD 运行不会被写文章
- **关于 Forced Entropy 的实际操作**: 文章描述了 overfit reflection、force entropy on stall、iteration log 三种机制，但都是 prompt-level 的指令，缺乏 harness-level 的硬约束实现。如果 agent 忽略"think outside the box"指令，stall 仍然会发生
- **关于成本门槛**: 30 小时 + `\$40` 看似低廉，但对于普通开发者来说，overnight 运行的心理门槛和调试 cheating 的迭代成本未被量化

### 3. 对标
- **跨域关联1**: 直接对应 ML 训练中的 overfitting / reward hacking——agent 过拟合 eval set 的解法（blinding、data augmentation、regularization）与 ML 训练中的对策完全同构。LFD 的 forced entropy 对应 ML 中的 dropout / noise injection
- **跨域关联2**: Prompt-time Distillation 是训练时蒸馏的推理时版本——DeepSeek/Kimi 在训练时蒸馏 GPT/Claude 输出，LFD 用 agent 在推理时做同样的事。执行成本从训练算力降到 `\$40` API 消耗
- **跨域关联3**: 信息不对称护城河论点与 [[Context-Advantage]] 和 [[Sufficient-Context]] 一致——当执行成本归零，拥有 eval set（私有 ground truth）的一方保持优势。cal.com 开源转闭源是这个论点的实证信号
- **跨域关联4**: 四要素框架（Target / Constraints / Instruments / Forced Entropy）与 [[Constraint-Driven-Engineering]] 高度互补——LFD 的 Constraints + Instruments 就是 Constraint-Driven Engineering 中分阶段硬约束的工程化表达
- **跨域关联5**: "内层循环 spec-driven + 外层循环 loss-function"的双层模型与 [[Agent-Loops]] 中 Andrew Ng 的三层循环形成对照——Ng 的 Developer Feedback Loop 对应 LFD 的外层循环（人定义优化方向），但 LFD 更激进地自动化了外层循环

### 关联概念
- [[Loss-Function-Development]]
- [[Agent-Loops]]
- [[Agent-Harness]]
- [[Constraint-Driven-Engineering]]
- [[Context-Advantage]]
- [[Model-Distillation]]
- [[Evaluation-Set]]
- [[Agent-Verification]]
