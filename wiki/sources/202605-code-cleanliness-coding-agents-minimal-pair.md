---
type: source-summary
title: "Does Code Cleanliness Affect Coding Agents? A Controlled Minimal-Pair Study"
source_raw:
  - "[[202605-code-cleanliness-coding-agents-minimal-pair.pdf]]"
created: 2026-07-08
updated: 2026-07-08
tags:
  - source-summary
  - agentic-engineering
  - code-quality
  - evaluation-methodology
  - token-efficiency
evidence_level: high
claim_type: extracted
---

# Does Code Cleanliness Affect Coding Agents? A Controlled Minimal-Pair Study

> SonarSource 论文（2026-05, arXiv:2605.20049v1），首次用最小对比对方法隔离代码整洁度对 coding agent 的独立影响。

**作者**: Priyansh Trivedi, Olivier Schmitt (SonarSource)

**实验设计**: 6 个 minimal pair 仓库（3 个 Slopify 方向：将干净仓库变脏；3 个 Vibeclean 方向：将脏仓库变干净），33 个编码任务，660 次 Claude Code (Sonnet 4.6) 试验。通过 hidden test 评估正确率，同时记录 10 个 footprint 指标。

## 编译摘要

### 1. 浓缩

- **核心结论 1**：代码整洁度**不影响** agent 的任务通过率（cleaner 0.913 vs messier 0.921，差距 −0.9pp 可忽略），但**显著降低** agent 的操作足迹：input tokens −7.1%、output tokens −8.5%、reasoning characters −11.1%。
  - 关键证据：660 次试验的聚合数据；6 个仓库对方向一致。
- **核心结论 2**：**文件回访率（file revisitation）下降 34%** 是最大单一效应，且在所有 6 个仓库上方向一致（范围 −7% 到 −69%）。Agent 在干净代码上"读一次就定稿"，在脏代码上反复回去验证之前的修改。
  - 关键证据：commons-bcel 上回访率下降 69%，ckan 上下降 7%，但方向始终一致。
- **核心结论 3**：跨模块任务（boundary-crossing track）受益最大（input tokens −11.0%），认知热点任务（cognitive-hotspot track）token 几乎不变但读更多文件。两条轨道拉扯方向相反，聚合后仍呈现 −7.1% 的净效应。
  - 关键证据：per-track 分析揭示 boundary-crossing 和 cognitive-hotspot 两个轨道的相反行为模式。

### 2. 质疑

- **关于"通过率不变"的质疑**：任务难度可能不够高——33 个任务在两个版本上都达到 ~92% 通过率，天花板效应可能掩盖了整洁度在更困难任务上的差异。作者在 Sec 4.2 也承认 calibration track 的高通过率印证了这一点。
- **关于"单一配置"的质疑**：所有试验只在 Claude Sonnet 4.6 + Claude Code 上运行。Haiku 4.5 试验噪声过大无法提取信号；GPT 和 Gemini 家族完全未测试。机制（file revisitation 反应局部代码结构）可能跨模型迁移，但这是推测。
- **关于"评论混淆"的质疑**：dirty/clean pair 之间评论行数差异可达 8000+ 行，可能 token 差异不是因为代码结构而是因为评论量。论文做了评论归一化实验（Table 4），sonar-caas-poc 归一化后 input token 差距从 +1.2% 翻到 −18.0%，说明效应真实，但 genie 归一化后方向翻转（从 +5.2% 到 +3.0%），结论不完全稳定。
- **关于 trial-to-trial variance 的质疑**：同一任务同一侧的 10 次试验中，最贵试验通常是最便宜的 2.5 倍；ckan/organization-list-exclude-empty 试验跨度从 1.4M 到 10.6M input tokens。单个 ~10% 的任务级 delta 可能是噪声；数据集级数字可靠是因为汇集了数百次试验。
- **关于外部效度的质疑**：仓库和任务均由作者策划，非 SWE-bench 式来自真实 GitHub issue。作者自认任务选择可能存在系统偏差。且只检测 hidden test 通过率，不检查 agent 是否破坏了仓库中的既有测试。

### 3. 对标与旁逸

#### 3a. 跨域对标

- **[[Agentic-Workflow-Token-Efficiency]]**：本文发现代码质量是继模型选择（9x）、工具裁剪、上下文管理之后的**第四类 token 效率杠杆**——虽然 7-8% 的幅度远小于模型选择，但它是少数不需要改 harness 就能生效的杠杆。
- **[[Agent-Harness]]**：论文的发现为 harness 设计增加了一个新维度——harness 不需要"理解"代码质量，但代码质量决定了 harness 运行的"地形复杂度"。类比城市规划：同样的交通系统（harness），在整洁的网格城市 vs 混乱的有机生长城市中，通行效率差异显著。
- **SWE-bench 系列**：SWE-bench 的每个 instance 是单个仓库单个版本，无法隔离代码质量的影响。本文的 minimal pair 方法填补了这个方法论缺口。
- **Bai et al. (2026)**：论文复现了 Bai 的两个发现——input token 主导总消费、per-task variance 极大（2.5x 在最贵/最便宜试验间）。

#### 3b. 旁逸（跨域联想）

- **认知科学中的 "processing fluency"**：心理学研究表明，文本排版清晰度不影响理解正确率，但显著影响阅读速度和重读频率。代码整洁度对 agent 的效应结构高度同构——不影响"做对"，但影响"做的成本"。
- **制造业中的 5S / Lean**：5S 运动的核心论点不是"脏乱车间造不出产品"，而是"脏乱车间增加寻找工具的时间、增加返工率"。本文的 file revisitation 指标恰好对应 "寻找工具的时间"。

#### 3c. 约束分析

- **硬约束**：代码结构决定 agent 需要处理的上下文量——这是信息论层面的，无法绕过
- **软约束**：当前 coding agent 依赖全文读取而非摘要读取——未来如果有结构感知的上下文管理（如 ACI），这个效应可能减弱
- **自设约束**：SonarQube 规则集是特定静态分析工具的选择，不同工具集可能产生不同的 "clean/messy" 切分

### 关联概念

- [[Code-Cleanliness-Agent-Footprint]] — 本文核心发现的概念化
- [[Minimal-Pair-Evaluation]] — 本文提出的评估方法论
- [[Agentic-Workflow-Token-Efficiency]] — 代码质量作为第四类 token 效率杠杆
- [[Agent-Harness]] — harness 的"地形复杂度"维度

### 速读卡

| 维度 | 内容 |
|------|------|
| **论文回答的问题** | 代码整洁度是否独立影响 coding agent 的行为？ |
| **它反对的常见信念** | "好模型不在乎代码脏不脏" / "AI 时代代码质量不重要了" |
| **它提出的新主张** | 整洁度不影响正确率，但深刻影响操作成本（token −7-8%，revisitation −34%） |
| **主张可信度** | 中高：660 次试验、双向 minimal pair、评论归一化，但仅单一模型+harness |
| **对读者判断的更新** | 代码质量在 AI 时代没有贬值，反而成为 agent 运营成本的关键变量 |
| **主张失效的边界** | 更弱模型（Haiku 噪声大）、非 Java/Python 代码库、超长程任务未测试 |
| **可执行项** | 在 agent-heavy 团队中，代码整洁度投资回报率应从"人的可读性"翻成"agent 的 token 成本"重新计算 |
