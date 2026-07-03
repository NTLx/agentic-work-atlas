---
type: source-summary
title: "千问 C 端 Agent Harness 思考与实践"
source_raw:
  - "[[20260702-qwen-agent-harness-practice]]"
created: 2026-07-03
updated: 2026-07-03
tags:
  - source-summary
  - agent-harness
evidence_level: high
claim_type: extracted
---

# 千问 C 端 Agent Harness 思考与实践

## 编译摘要

### 1. 浓缩
- **核心结论1**: C 端通用 Agent 的产品化方法论是"多快好省"——多（通用任务类型）、快（执行时间对得上交付质量）、好（定义"好"比做到"好"更难）、省（Token 消耗降至海外产品 1/10）。千问月活 3 亿，2026 年 1 月上线通用复杂任务 Agent，历时半年打磨。
  - 关键证据: Token 消耗降至海外产品 1/10；执行时间降至初始 1/3；通过"链路固化"将反复执行的路径编码为代码。
- **核心结论2**: 主动服务（从被动响应到精准预判）需要四大组件——User Memory + Environment + Task System + Assistant，三大核心挑战是环境建模、低成本感知、"情商"。"情商"问题可能需要在基模层面解决。
  - 关键证据: 朱达明确指出"很少训练模型怎么主动发起话题"，认为这需要基模层面的能力。
- **核心结论3**: 从 Harness Engineering 到 AIWare Engineering 的演进框架——借用计算机史类比（1968 年软件危机），提出"AI 的下一步不只是技术问题，是人+AI 的组织方法论"。核心判断：Harness 短期收益高于优化模型，但随基模进步很多脚手架会被淘汰。
  - 关键证据: 引用 Karpathy 的 Harness 七模块框架（O-E-T-C-L-V-G），但延伸到 AIWare Engineering 层面。

### 2. 质疑
- **关于"多快好省"的质疑**: 方法论框架化程度高但细节不足。"链路固化"的具体实现机制（何时触发、如何判断可固化、固化的粒度）未展开。Token 消耗 1/10 的对比基准不明确（对比哪个海外产品？Claude Artifacts? ChatGPT?）。
- **关于"情商需要基模解决"的质疑**: 将主动服务的"情商"归因于基模能力，可能低估了工程手段（如 fine-tuning、RLHF、prompt engineering）在可控场景下的效果。这是务实派工程师常见的"基模决定论"倾向。
- **关于 AIWare Engineering 的质疑**: 1968 年软件危机的类比有启发性，但"软件工程"作为学科花了数十年才成熟。AIWare Engineering 目前更像一个愿景，缺少可操作的方法论框架。

### 3. 对标
- **跨域关联1**: "链路固化"（Agent 首次执行需反思规划，积累后固化为代码）类似软件工程中的"重构"——从探索性代码到稳定抽象的演化。也类似制造业从手工到自动化的路径。
- **跨域关联2**: Harness Engineering 七模块框架（O-E-T-C-L-V-G）与 Agentic Engineering 的系统分类高度重合，但朱达的延伸点在于：Harness 的下一步不是更精细的工程，而是"人+AI 协作"的组织设计。
- **跨域关联3**: "低功耗，够用就行"的进化论类比与 FinOps 中的"成本-效果帕累托前沿"呼应——不是追求最高智能，而是在成本约束下找到最优均衡点。

### 关联概念
- [[Agent-Harness]]
- [[Harness-Engineering]]
- AIWare-Engineering（待建 entity）
- [[Context-Engineering]]
- Active-Service（待建 entity）
- 链路固化（待建 entity）
