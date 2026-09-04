---
type: source-summary
title: "An Organizational Second Brain: Building an AI That Learns From Experts"
canonical_url: "https://engineering.fb.com/2026/09/02/ml-applications/organizational-second-brain-ai-learns-from-experts/"
raw_state: index
original_raw_file: "20260902-meta-organizational-second-brain.md"
original_body_sha256: "a19011d04fdf8504ba840bdc1d139f96cdf81ab1ce088e1ee1653a950b82e3d3"
indexed_at: "2026-09-05T01:57:30+08:00"
created: 2026-09-05
updated: 2026-09-05
tags:
  - source-summary
  - knowledge-management
  - organizational-ai
  - agentic-engineering
evidence_level: medium
claim_type: mixed
---

# An Organizational Second Brain: Building an AI That Learns From Experts

> Meta Engineering（Shaurya Sengar、Jason Nawrocki、Jay Shah、Prashant Kommireddi，2026-09-02）。文章以合规领域 agent 为案例，提出把组织知识、专家推理、评估和改进回路拆成可审计文件系统；下述结果与“零回归”等指标均为作者自报。

## 编译摘要

### 1. 浓缩

- **核心结论 1：组织级专家 Agent 的关键不是把更多原文塞进上下文，而是把“组织知道什么”和“组织如何推理”预先编译成可审计结构。**
  - 关键证据：离线过程把专家隐性知识提炼为带约束、边界和路由含义的结构化文件；高密度高频知识进入 wiki，稀疏且情境化的材料继续由 semantic/lexical RAG 按需提供（raw 行 42–71）。
- **核心结论 2：知识层与程序层分离，可以让失败归因和变更范围变得清楚。**
  - 关键证据：position、taxonomy/vocabulary、routing index、gateway 文件分别承载立场、术语、路由和领域入口；recipes 作为命令式程序引用知识但不复制领域事实。新增立场只改知识文件和路由，修正方法论只改 recipe（raw 行 42–87）。
- **核心结论 3：专家纠正只有经过诊断、最小编辑、对抗审查、确定性结构校验、targeted replay、回归测试和专家审核，才会变成可复利的组织记忆。**
  - 关键证据：作者把改进回路列为四步，并进一步描述独立 adversarial review、lint、blind replay、regression test 和将已修复场景加入测试集（raw 行 107–159）。六周三个 sprint 后，作者报告 SME 输出“几乎总是有用”、评估时间从 days 降到 minutes、自动改进、zero regressions 等结果（行 160–190）。

### 2. 质疑

- **关于效果的质疑**：文章没有披露完整基线、测试集规模、错误率、评估 rubric、成本或“zero regressions”的统计定义；“substantial time”“days to minutes”等结果不能脱离原工作量和风险等级解释。
- **关于架构泛化的质疑**：案例来自 Meta 的特定合规域，适用前提是专家判断可以通过可检索文本、结构化立场和程序近似表达；需要持续身体经验、实时感知或高度政治性协商的领域未被证明同构。
- **关于“无需训练”的质疑**：无需修改模型权重不等于系统没有学习成本；知识文件、recipes、路由和评估集都需要维护，且自我改进回路本身依赖专家审核和验证基础设施。
- **关于 80% token 节省的质疑**：这是作者对 recipe-driven stages 相比早期 flat instruction + semantic search 的内部比较，文章没有给出 workload、token 口径或质量保持证据。
- **关于自动编辑的质疑**：多 Agent 并行分析和独立审查降低了共享盲区，但并不自动保证提出者之外的评估器、回归集和专家裁决没有系统性偏差。

### 3. 对标与旁逸

#### 3a. 跨域对标

- **与 [[Knowledge-Compilation|知识编译]] 的关系**：Meta 明确把专家反馈维护称为 compilation；本库的 raw → source summary → stable Wiki 同样把一次性材料转成可版本化中间层，但 Meta 更进一步把回归测试纳入知识生命周期。
- **与 [[Company-Brain|Company Brain]] 的关系**：Company Brain 强调组织共享上下文的 Capture → Curate → Store → Execute → Experience；Meta 案例补上“如何把纠正编译回知识和程序，并用测试防止回退”。
- **与 [[Harness-Engineering|Harness Engineering]] 的关系**：知识文件、recipes、路由和评估套件组成组织级 harness；模型不是独立产品，组织的规则、权限、证据和反馈回路决定其可用边界。
- **跨域类比：软件编译器与持续集成**。知识文件像声明式配置，recipe 像执行程序，lint/replay/regression 像编译与 CI；专家审核是最终 landing gate。这个类比成立的条件是领域规范足够显式且可测试。

#### 3b. 旁逸

文章隐含的组织学习公式是：**专家时间 → 纠正信号 → 可审计编辑 → 回归测试 → 后续少犯同类错误**。它把“专家回答了一次问题”从服务成本变成知识资产，但前提是反馈能被准确归因，且组织允许把判断公开化、版本化（综合判断）。

#### 3c. 约束

- **硬约束**：知识、程序、评估和依赖图必须能被机器读取，否则无法安全做最小编辑和影响分析。
- **软约束**：高风险领域需要 checkpoints、escalations 和专家最终审核；风险越高，自动落地的权限越低。
- **自设约束**：哪些材料进 wiki、哪些留在 RAG，取决于信息密度与使用频率；四层 taxonomy、recipes 和 80% token 目标是该系统的设计选择。

### 关联概念

- [[Knowledge-Compilation]]
- [[Company-Brain]]
- [[Institutional-Knowledge]]
- [[Harness-Engineering]]
- [[Progressive-Disclosure]]
- [[RAG-vs-LLM-Wiki]]
