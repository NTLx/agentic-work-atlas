---
type: source-summary
title: "Validating agentic behavior when 'correct' isn’t deterministic"
source_raw:
  - "[[Validating agentic behavior when “correct” isn’t deterministic]]"
created: 2026-05-24
updated: 2026-05-24
tags:
  - source-summary
---

# Validating agentic behavior when 'correct' isn’t deterministic

## 编译摘要

### 1. 浓缩
- **核心结论1**: 传统测试工具（断言测试、录制回放、视觉回归、ML oracles）的共同缺陷是假设"正确=可重复的步骤序列"。对于 agentic 系统，正确性应该定义为"可靠达成关键结果"而非"遵循固定路径"。
  - 关键证据: GitHub Copilot Coding Agent 在相同任务中，loading screen 出现与否、快捷键 vs 菜单操作等不同路径都能成功完成任务，但传统 CI 管线会报 false negative。
- **核心结论2**: Dominator analysis（支配者分析）从编译器理论移植到 agent 验证，能自动区分「essential states」（必须达成的里程碑）和「optional variations」（环境噪音如 loading spinner），数学上无需黑盒模型。
  - 关键证据: 在 VS Code 实验中，Dominator Tree 达到 100% 准确率（F1=100%），而 Agent 自评只有 69.8% F1。Agent 完全无法识别 "Not a Bug" 场景（0% F1），Trust Layer 达到 52.2%。
- **核心结论3**: 仅需 2-10 次成功执行记录即可构建 ground truth 模型，通过三层次等价性检测（视觉哈希 → LLM 语义分析 → 保守合并）和前缀树接受器（PTA）实现可解释的结构化验证。
  - 关键证据: 算法输出 coverage metric 和具体失败原因（如 "State 'Search Results' never reached after 'Search Dialog'"），不是黑盒 pass/fail。

### 2. 质疑
- **关于"Dominator analysis 通用性"的质疑**: 假设 agent 执行的 state space 可以被有限观察覆盖。对于 open-ended 探索型任务（如"研究 X 主题"），没有明确的 essential states，dominator 方法可能不适用。
- **关于"LLM 依赖"的质疑**: 三层次等价性检测依赖多模态 LLM 来做语义判断，这意味着 Trust Layer 的可扩展性直接受 LLM API 延迟和成本制约——本质上是用一个非确定性组件去验证另一个非确定性系统。
- **关于数据可靠性**: 实验在"VS Code extension test suite"这一特定场景中进行，样本量和场景多样性未披露。100% 准确率在小规模受控实验中需谨慎解读。

### 3. 对标
- **跨域关联1**: Dominator analysis 本质上是一种 **结构不变性提取**——与 [[Ontology|Ontology]] 中 TBox（概念规则层）与 ABox（实例数据层）的分离逻辑一致：提取不变的骨架结构，容忍实例层的变异。
- **跨域关联2**: 这个验证框架与 [[Agentic-Engineering|Agentic Engineering]] 的测试环节直接对接——使 Agent 从 "demo 级" 迈入 "production 级" 的最后一块拼图。
- **跨域关联3**: "Essential states" 的概念与 [[Decision-Quality|Decision Quality]] 中的"清晰"维度类似——正确性不取决于路径细节，而取决于是否穿过关键决策节点。

### 关联概念
- [[Dominator-Analysis]]
- [[Agentic-Engineering]]
- [[Ontology]]
- [[Decision-Quality]]
