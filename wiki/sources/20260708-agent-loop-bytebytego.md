---
type: source-summary
title: "The Agent Loop: How AI Goes From Answering Questions to Doing Things"
source_raw:
  - "[[20260708-agent-loop-bytebytego.md]]"
created: 2026-07-13
updated: 2026-07-13
tags:
  - source-summary
  - agentic-engineering
evidence_level: medium
claim_type: extracted
---

# The Agent Loop: How AI Goes From Answering Questions to Doing Things

## 编译摘要

### 1. 浓缩
- **核心结论1**: Agent 的本质是将流程控制权交给模型——"agent 就是被放进循环里、由模型自己决定何时停下来的 LLM"。系统从 Text → Augmented → Pipeline → Loop 四阶段演化，Loop 阶段模型在 Review → Evaluate → Execute → Record 的四相循环中动态决策终止条件，而非依赖硬编码限制。
  - 关键证据: 每次迭代模型选择四条路径之一（直接回复、tool call、委派、内部推理）；连续反馈使系统适应实时结果而非依赖预设假设。
- **核心结论2**: 自主循环的代价是可预测性崩塌——95% 单步成功率经 20 次迭代后降至约 36%（0.95^20），同时成本高于确定性 pipeline。基础设施（进度追踪、git 历史、预执行规划）的投入往往比升级模型本身更关键。
  - 关键证据: 复合错误数学；社区洞察"更便宜的验证步骤比更强的基础模型带来更大收益"。
- **核心结论3**: 三层护栏是 Agent 安全运行的必要条件：输入筛查（轻量模型拦截违规）、中间件检查（监督每次外部请求及返回）、输出审查（在用户接收前拦截敏感泄露）。
  - 关键证据: 三层过滤分别作用于循环与外部环境之间的边界。

### 2. 质疑
- **关于"95% → 36%"的质疑**: 该数字假设各步独立且错误率恒定，实际 agent 可通过自我修正、上下文累积、检查点回滚缓解复合错误；真实衰减曲线取决于任务结构和纠错机制强度，36% 是悲观上界而非普遍规律。
- **关于"基础设施比模型更重要"的质疑**: 该判断可能反映当前模型能力已接近瓶颈的特定阶段，而非普遍真理；当模型推理能力出现代际跃迁时，基础设施投入的相对重要性会下降。
- **关于 Pipeline vs Loop 的选择**: 文章暗示"先试 pipeline，不够再上 loop"，但未给出判断阈值——何时 task 的不确定性高到必须用 loop 承担复合错误成本？这取决于任务空间的可枚举性，而非单纯复杂度。
- **ReAct 的"推理"成分**: 文章将 chain-of-thought 归为 prompt engineering 的涌现而非独立代码路径，这模糊了"真推理"与"伪推理"的边界——推理阶段是否真正功能性的，取决于每一步是否依赖前一步的环境反馈，而非是否产生了文本。

### 3. 对标
- **跨域关联1**: 复合错误衰减（0.95^n）与软件工程中的可靠性链（series reliability model）同构——串联系统的整体可靠度等于各组件可靠度之积。可迁移到：任何多步自动化流程（CI/CD、微服务调用链、人工审批链）的设计都必须面对"步骤越多、整体越脆弱"的约束。
- **跨域关联2**: 三层护栏（输入/中间件/输出）与网络安全的纵深防御（defense in depth）结构一致——不依赖单一检查点，而是在每个边界设防。可迁移到：Agent 安全设计应复用安全工程数十年的分层策略，而非重新发明。
- **跨域关联3**: "更便宜的验证步骤比更强的模型更有效"与软件测试的 property-based testing 思想呼应——与其追求更强的生成器（模型），不如投入更强的不变量检查器（验证），用低成本断言捕获高成本错误。

### 关联概念
- [[Agent-Loops]]
- [[Agent-Harness]]
