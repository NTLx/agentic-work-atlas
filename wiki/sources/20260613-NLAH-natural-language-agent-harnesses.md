---
type: source-summary
title: "Code designs Harness 还是 Model drives Harnesses？"
source_raw:
  - "[[20260613-NLAH-natural-language-agent-harnesses]]"
created: 2026-06-13
updated: 2026-11-28
tags:
  - source-summary
  - agent-harness
---

# Code designs Harness 还是 Model drives Harnesses？

## 编译摘要

> 本地Raw为二手解读。本轮核对Pan et al. [arXiv:2603.25723v2](https://arxiv.org/html/2603.25723v2)（2026-05-18）§4–5及Tables 1–5，勘误不改Raw。

### 1. 浓缩

- **核心结论1**: Agent 驾驭层（Harness）可以被表示为可执行的自然语言对象（NLAH），从而将偶然的胶水代码转变为可检视、可移植、可消融的科学表示对象
  - 关键证据: Table 1原代码/普通Prompt/IHR分别为SWE Verified 67.0/77.0/73.0、TB2 36.0/57.3/53.9、OSWorld 47.1/47.9/46.3。IHR未超过普通Prompt；特定实现可行，非统计等效证明。
  - 关键证据: Table 2静态材料token：Live-SWE 60.1k→2.9k、MHTBA 10.5k→0.8k、SeeAct 47.5k→1.4k；不含运行时prompt/log，非实际推理成本缩减

- **核心结论2**: Harness 模块"不是越多越好"——模块干预让特定设计的贡献可实测，不主张研究首创
  - 关键证据: Table 5是在Basic条件逐项添加（不是二手解读所说leave-one-out）。SWE/OSWorld文件状态+2.6/+13.9，证据回答+2.8/+2.8，多候选−1.6/+2.8，压缩−1.0/−8.3，Markdown记忆−2.8/+5.6个百分点；不能将多候选概括为普遍负效应
  - 关键证据: 自我进化模块在SWE为78.8（+5.8），OSWorld为52.8（+8.4），后者低于文件状态58.3；Table 5报告agent calls而非完整token成本，不称两个任务最高或普遍高成本

- **核心结论3**: NLAH 的驾驭机制遵循度"有好有坏"——契约式、可即时验证的机制遵循度高，跨阶段/跨子 agent 协调的机制遵循度低
  - 关键证据: Tables 3–4分别报告模式保留及机制指标；IHR artifact contract约1.00/0.96、handoff recall约0.32/0.55（Live-SWE/MHTBA），直接上下文与父子交接指标口径不同

### 2. 质疑

- **关于"NLAH 等效代码驾驭"的质疑**: 基准测试（SWE-bench、Terminal-Bench、OSWorld）是否覆盖了真实生产环境的复杂性？论文的原型运行时 token/调用开销更高，规模化时成本差距可能放大
- **关于"消融实验"的质疑**: 逐项添加测得条件增量，不识别模块交互；组合效果须另测
- **关于自然语言不精确性的质疑**: 论文承认 NLAH 的语义约束可能被不同模型不同解读，但依赖"实际运行检验"来兜底，这在高风险场景下是否足够？

### 3. 对标

- **跨域关联1**: NLAH 类似软件工程的 Infrastructure as Code（IaC）—— 把原本硬编码的基础设施配置外置为声明式文档。区别在于 IaC 是确定性的，NLAH 的解释执行依赖 LLM
- **跨域关联2**: 消融实验的发现（特定压缩配置在两基准负增益、文件状态配置为正；不外推所有压缩与记忆方式）与 [[Context-Rot]] 和 [[Multi-Layer-Memory]] 的研究方向一致
- **跨域关联3**: NLAH 四层架构（基础 Agent → 运行时策略 → NLAH 文档 → 脚本适配器）与 [[Thin-Harness-Fat-Skills]] 的设计哲学有相似之处，都强调关注点分离

### 关联概念

- [[NLAH]]
- [[Agent-Harness]]
- [[Harness-Engineering]]
- [[Context-Rot]]
- [[Multi-Layer-Memory]]
