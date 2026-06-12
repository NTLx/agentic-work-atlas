---
type: source-summary
title: "Code designs Harness 还是 Model drives Harnesses？"
source_raw:
  - "[[20260613-NLAH-natural-language-agent-harnesses]]"
created: 2026-06-13
updated: 2026-06-13
tags:
  - source-summary
  - agent-harness
  - NLAH
  - research-paper
---

# Code designs Harness 还是 Model drives Harnesses？

## 编译摘要

### 1. 浓缩

- **核心结论1**: Agent 驾驭层（Harness）可以被表示为可执行的自然语言对象（NLAH），从而将偶然的胶水代码转变为可检视、可移植、可消融的科学表示对象
  - 关键证据: 在 SWE-bench Verified、Terminal-Bench 2.0、OSWorld 三类基准上，IHR 执行的 NLAH 取得与代码驾驭层相当的成绩
  - 关键证据: Live-SWE 从 6.01 万 token 代码降到 2.9k token 的 NLAH；MHTBA 从 1.05 万降到 0.8k

- **核心结论2**: Harness 模块"不是越多越好"——消融实验首次把"该保留哪些 harness 设计"变成可用实验数据回答的问题
  - 关键证据: 文件持久化状态是最稳的正贡献（Δ 约 +2.6/+13.9）；多候选搜索反而损害性能；上下文压缩在两个任务上都有害
  - 关键证据: 自我进化模块带来最高绝对性能但 token 消耗大幅上升

- **核心结论3**: NLAH 的驾驭机制遵循度"有好有坏"——契约式、可即时验证的机制遵循度高，跨阶段/跨子 agent 协调的机制遵循度低
  - 关键证据: 8 类可观测驾驭机制的逐条遵循率对比

### 2. 质疑

- **关于"NLAH 等效代码驾驭"的质疑**: 基准测试（SWE-bench、Terminal-Bench、OSWorld）是否覆盖了真实生产环境的复杂性？论文的原型运行时 token/调用开销更高，规模化时成本差距可能放大
- **关于"消融实验"的质疑**: leave-one-out 消融假设模块间独立，但驾驭模块之间可能存在非线性交互——关闭一个模块的效果可能依赖于其他模块是否存在
- **关于自然语言不精确性的质疑**: 论文承认 NLAH 的语义约束可能被不同模型不同解读，但依赖"实际运行检验"来兜底，这在高风险场景下是否足够？

### 3. 对标

- **跨域关联1**: NLAH 类似软件工程的 Infrastructure as Code（IaC）—— 把原本硬编码的基础设施配置外置为声明式文档。区别在于 IaC 是确定性的，NLAH 的解释执行依赖 LLM
- **跨域关联2**: 消融实验的发现（上下文压缩有害、文件外化状态有益）与 [[Context-Rot]] 和 [[Multi-Layer-Memory]] 的研究方向一致
- **跨域关联3**: NLAH 四层架构（基础 Agent → 运行时策略 → NLAH 文档 → 脚本适配器）与 [[Thin-Harness-Fat-Skills]] 的设计哲学有相似之处，都强调关注点分离

### 关联概念

- [[NLAH]]
- [[Agent-Harness]]
- [[Harness-Engineering]]
- [[Context-Rot]]
- [[Multi-Layer-Memory]]
