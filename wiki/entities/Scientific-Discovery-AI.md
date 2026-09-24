---
type: entity
title: Scientific Discovery AI
aliases:
  - Scientific Discovery AI
  - 科学发现 AI
definition: "把巨大组合搜索空间、明确目标函数、数据或模拟器和工具调用结合起来，用 AI 寻找科学突破方案的系统形态"
created: 2026-05-08
updated: 2026-09-24
tags:
  - AI
  - science
  - deepmind
evidence_level: high
claim_type: mixed
related_entities:
  - "[[Demis-Hassabis]]"
  - "[[Einstein-Test]]"
  - "[[Continual-Learning]]"
  - "[[World-Model]]"
  - "[[Tool-Use-Architecture]]"
  - "[[Open-Source-Operational-AI-Framework]]"
  - "[[Deterministic-Retrieval]]"
source_raw:
  - "[[Demis Hassabis: Agents, AGI & The Next Big Scientific Breakthrough]]"
  - "[[20260608-paving-the-way-for-agents-in-biology]]"
  - "[[20260826-latent-space-anima-physical-world-models]]"
  - "[[20260922-latentspace-john-platt]]"
  - "[[20260923-latentspace-eric-biosecurity]]"
---

# Scientific Discovery AI（科学发现 AI）

> [!definition] 定义
> **Scientific Discovery AI** 是用 AI 在科学问题空间中寻找突破的系统形态。它通常需要四个条件：巨大组合搜索空间、明确目标函数、足够数据或模拟器，以及能通过工具调用和实验反馈不断校验假设。

## 为什么重要

科学发现是检验 AI 是否能超越文本生成的重要场景。它要求系统不只是复述论文或给出方案，而是在庞大搜索空间中找到人类难以穷举的结构，并把结果变成可验证的理论、实验或工具。

Hassabis 从 AlphaGo 和 AlphaFold 总结出一个模式：当问题可以被描述为海量组合搜索，并且有可优化目标函数时，AI 能找到 needle in a haystack 式的解。围棋中的惊人落子和蛋白质折叠中的结构预测，都是这个模式的不同实例。

## 关键数据点

- AlphaFold 被全球数百万研究者使用，说明科学发现 AI 的价值不只是论文指标，而是能成为科研基础设施。
- Hassabis 提出的通用条件是：组合搜索空间足够大、目标函数清晰、有足够数据或模拟器生成分布内数据。
- 药物发现可被表述为搜索问题：如果物理规律允许某种化合物存在，难点就是如何高效找到它。
- **确定性检索层（[[Deterministic-Retrieval]]）** 的缺失是科学智能体的核心瓶颈。Anthropic 研究显示，在引入 gget-virus 后，Agent 在病毒序列检索上的准确率从 16.9% 提升至 99.7%（2026）。
- 虚拟细胞路线需要更强的观测和模拟能力，可能依赖无损活细胞纳米级成像，也可能依赖更好的学习型模拟器。
- 通用模型不应把所有专业科学知识塞进一个巨大脑袋；更可行的是通过 [[Tool-Use-Architecture|工具使用架构]] 调用 AlphaFold 这类专用系统。
- Google Research 的新水文模型相对旧版本，在有测站流域延长六天可靠预测窗口，在无测站流域延长一天；更重要的是，团队把模型架构、训练管线、文档和教程开放给运营机构。

## 两种层级

| 层级 | 任务 | 代表问题 |
|------|------|----------|
| 搜索型发现 | 在已有规则和目标函数下找到极优解 | 围棋走法、蛋白质折叠、候选分子搜索 |
| 框架型发现 | 提出新的问题、理论或解释结构 | [[Einstein-Test|Einstein Test]] 所关心的新理论生成 |

当前方法在第一层更有把握。第二层需要更强的类比推理、世界模型、持续学习和对“什么问题重要”的判断。

## 第二条路线：连续物理系统的结构先验（08-27 补充）

Hassabis 叙事的"组合搜索 + 目标函数"是一种科学发现路线；[[20260826-latent-space-anima-physical-world-models|Anima Anandkumar（2026-08）]]补上了第二种——**连续物理系统（天气/聚变/流体）用结构归纳偏置建模**。两者共享"用 AI 找科学方案"的目标，但搜索空间与先验来源不同：

| 维度 | 组合搜索路线（Hassabis） | 连续系统路线（Anima） |
|------|------------------------|----------------------|
| 问题空间 | 离散组合（蛋白质折叠、分子、围棋） | 连续演化（大气、等离子体、流体） |
| 核心机制 | 海量搜索 + 目标函数 | Neural Operators（函数映射）+ 物理先验 |
| 先验来源 | 规则、仿真器、策略网络 | PDE 结构、球谐/Fourier 基底、物理直觉 |
| 规模假设 | 可扩充（锦上添花的 scale 故事） | 反抗 token scaling（数据稀缺 + 百亿级 context） |
| 代表系统 | AlphaGo / AlphaFold | FourCastNet / Spherical FNO / TorchLean |

**关键机制（值得沉淀）**：
- **Neural Operators**：把"网格建模"改为"任意分辨率输入输出间的函数映射"——不再建模 grid，而是建模跨尺度演化的函数；Fourier Neural Operator 在频域学习，球谐变体把"地球是球"的先验 baked in，模型可稳定滚动数月而非数天
- **物理世界比预期宽容**：聚变数百个样例即可预测 plasma disruptions，AI 仿真比传统仿真快 ~100 万倍——结构先验大幅降低数据需求，与语言模型的 scale 依赖形成对照
- **context 的物理上限**："网格 1000³ ≈ 数百亿到万亿 context length，所以别想用 transformer 做这个规模"——这是 token scaling 的科学域边界证据

**长期愿景**：`物理基础模型`（跨多现象、模拟 + 设计）；但与语言模型不同——"把深度学习有效成分变得更有原则（principled）"，而非等价 scale 故事。

> [!warning] 边界
> "数千样例即可"依赖特定领域（低维去歧义问题）；"百万倍快"为受访者主张需检原论文。两条路线的划分是机制性对照，不是 Either/Or——真实科学发现系统可能二者结合（结构先验 + 组合搜索）

## 第三条路线：Scorable Task + LLM Tree Search

John Platt 对 Google ERA（Empirical Research Assistance）的描述补出第三条机制路线：科学家先把问题转译为可执行的 scoring contract，LLM 在 specialized harness 中生成和变异 notebook，再用 Monte Carlo Tree Search / UCB 在候选树中做非贪婪搜索；共享试验历史让后续分支吸收此前失败与成功的信息（[[20260922-latentspace-john-platt]]，00:04:16–00:14:42）。

**判断**：在可评分的计算型科研问题中，Agent 的关键杠杆不是直接替代科学判断，而是把“可尝试的实验软件空间”扩大几个数量级，从而把人的瓶颈上推到目标函数定义、科学解释和结果验证。
- **证据**：[[20260922-latentspace-john-platt]]（00:15:01–00:18:13；00:22:27–00:34:26）。Platt 明确说 scoring function 会被 Agent 找到漏洞，需要反复重写；对 descriptive science 还必须处理 multiple-hypothesis testing、false discovery 和隐藏 holdout。
- **边界**：scoreable task 天然偏向有可执行 objective 的问题。Platt 同时明确表示，当前系统还不能独立发现 completely new physics / completely new science；predictive fit 也不能直接升级为对现实机制的 descriptive truth。

这一路线和已有两条路线形成互补：

| 路线 | 核心可计算结构 | Agent/模型的主要作用 | 主要硬边界 |
|---|---|---|---|
| 组合搜索（Hassabis） | 巨大搜索空间 + 明确 objective | 在组合空间中找极优解 | objective 是否代表真正问题 |
| 连续物理（Anima） | PDE / operator / 结构先验 | 学习跨尺度动力学 | 数据稀缺、物理先验与超长 context |
| Scorable Task（ERA） | scoring contract + executable notebook | LLM 引导 tree search、代码变异与重组 | score gaming、holdout 污染、科学解释 |

### 计算闭环仍不是实验闭环

**判断**：ERA 目前证明的是“计算研究环节可以被高吞吐 Agent 化”，而不是端到端 autonomous science；真实实验、传感与数据采集仍是闭环中的外部硬边界。
- **证据**：[[20260922-latentspace-john-platt]]（02:00:21–02:00:49）。Platt 把最想消除的瓶颈描述为一个可接收 JSON 并自动执行任意实验的 “everything lab”，并强调当前 ERA “it's all computational”。
- **边界**：不同科学领域的实验成本差异极大；纯计算数学、仿真或已有数据集任务可以更接近闭环，而湿实验、材料、机器人和大科学装置仍受物理执行层限制。

## Domain-native Foundation Model：直接学习科学对象

[[20260923-latentspace-eric-biosecurity]] 用完整访谈补出一个与外层 Agent orchestration 不同的 scientific AI 层次：Genome Language Model 直接把 biological sequence 当作基础建模对象。HyenaDNA 的出发点是 biological sequence 的极长 context；Evo 把能力从 read 推到 write；Omni 则进一步把 base model 通过 task structure、mid/post-training 和 supervised alignment 映射到科学家真正使用的预测与设计任务（Transcript L34-L58、L96-L144、L196-L230）。

**判断**：Scientific Discovery AI 至少需要区分三层能力：
1. **domain representation**：模型是否直接学习科学对象的原生表示；
2. **task alignment**：是否能把 base representation 映射到实际科学问题和输出格式；
3. **agent orchestration**：是否能在更高层规划、调用工具和闭环验证。

在生物域，domain-native model 不只是被 Agent 调用的“一个工具”，它本身会成为可搜索、可条件化和可生成的科学空间。
- **证据**：[[20260923-latentspace-eric-biosecurity]]（Transcript L34-L58、L96-L144、L196-L230）。
- **边界**：Omni 的 benchmark、alignment recipe 和 generalization 主要来自厂商自述；长 context 和统一模型并不自动等价于 general biological intelligence。

### Score-conditioned generation 不是已证明的 biological CoT

访谈把一项实验称为 biological “chain-of-thought”：给模型一系列按 fitness score 递增的 biological sequences，隐藏表现最好的部分，再让模型继续这一 progression。模型在 in-silico 结果中能够恢复部分更高分候选（Transcript L248-L270）。

**判断**：当前更稳妥的抽象是 **score-conditioned in-context optimization / extrapolation**，而不是已证实与自然语言 CoT 同构的内部推理链。
- **证据**：[[20260923-latentspace-eric-biosecurity]]（Transcript L248-L270）。
- **边界**：Nguyen 明确说 wet-lab validation 当时仍在进行；因此该结果只能证明计算层行为，不能把 in-silico score 直接升级为真实 biological function。

### 验证链从 benchmark 延伸到真实世界

全文还把 scientific AI 的验证边界拆成三层：训练/benchmark 层防 data leakage（Transcript L232-L238）、representation 层用 mechanistic interpretability 检查 embeddings/activations 中是否出现可解释 biological structure（L450-L490）、最终 design claim 回到 wet-lab / real-world measurement（L266-L270）。

**判断**：domain-native model 越接近真实科学对象，verification 越不能停在 benchmark；可信链需要从数据划分一直延伸到独立物理反馈。
- **证据**：[[20260923-latentspace-eric-biosecurity]]（Transcript L232-L238、L266-L270、L450-L490）。
- **边界**：访谈中的 leakage QC 与 mech-interp 仍是团队自述，未提供足够细节用于独立复现。

### Capability 与 Defense 的耦合

同一 biological model frontier 同时推动 design 与 defense。Nguyen 明确提出“dual mandate”：生成能力更强的模型也可以用于 discrimination / risk prediction，并把 design/defense 描述成持续的 arms race（Transcript L506-L516、L594-L620）。

**判断**：当同一 model frontier 同时服务 discovery 与 defense 时，“提升能力”和“降低风险”不再是可独立优化的两个轴；治理必须把模型能力、访问权、domain-level checking、物理执行接口与环境级检测分层控制。
- **证据**：[[20260923-latentspace-eric-biosecurity]]（Transcript L506-L586、L594-L620）。
- **边界**：这是 Radical Numerics 的战略框架，尚缺独立跨模型 benchmark 与长期 field evidence；不能直接推出“更强生成模型必然带来更安全结果”。

## 从科学突破到运营基础设施

科学 AI 的价值不只取决于模型能否达到更高 benchmark，还取决于发现能否进入研究和运营机构的标准工作流。

Google 水文框架提供了一个完整转换链：

```text
研究模型
  -> 可复现架构与训练管线
  -> 本地数据和知识进入模型
  -> 伙伴机构验证
  -> 适配既有运营平台
  -> 本地机构持续运行和改进
```

[[Open-Source-Operational-AI-Framework|开源运营型 AI 框架]]因此是 Scientific Discovery AI 的下游基础设施。它把科学能力从发布方的研究成果，变成其他机构可拥有、可修改、可集成的工作能力。

## 与 Agent 架构的关系

科学发现 AI 很可能不是一个单体模型，而是一个 agentic tool-use system：

- 通用模型负责拆问题、规划实验、调用工具和整合结果。
- 专用模型负责蛋白质、材料、药物、数学或模拟器中的特定能力。
- [[World-Model]] 负责把实验结果和理论假设连接起来。
- [[Continual-Learning]] 负责让多轮实验经验不被遗忘，也不被错误经验污染。
- **确定性感知层与约束闭环**: 对于生物学等敏感领域，基础设施必须从“步行者”模式转型为提供 Agent-native 数据访问路径。通义实验室（2026）进一步指出，质量不是生成的，而是通过注入硬约束和自动化判据（[[Automated-Criteria]]）收敛出来的。这对于需要极高精度的科学交付至关重要。

这与企业 Agent 的结构类似：通用 orchestrator 不替代所有专家系统，而是协调专用工具、检索、验证和人类判断。

## 前提与局限性

- 清晰目标函数不是所有科学领域都有；“什么是好猜想”比“怎样赢棋”更难定义。
- 数据和模拟器可能是瓶颈，尤其是生命科学中无法直接观测的动态过程。
- 搜索型突破不等于真正原创；系统可能会解已有问题，却不会提出新问题。
- 科学发现结果必须经过实验或形式化验证，不能只靠语言说服。
- 开放模型和训练管线不会自动产生运营采用；本地数据质量、集成能力、责任链和长期维护仍可能成为瓶颈。
- **VirBench 基准测试** 揭示了当前模型在原生检索任务中的高随机性和不稳定性。

## 关联概念

- [[Einstein-Test]] - 检验系统能否提出新问题和新理论
- [[Continual-Learning]] - 多轮实验需要累积经验并避免遗忘
- [[World-Model]] - 科学探索需要可更新的环境和理论表示
- [[Tool-Use-Architecture]] - 通用模型应协调专用科学工具
- [[Demis-Hassabis]] - AlphaGo / AlphaFold 路线背后的关键人物
- [[Open-Source-Operational-AI-Framework]] - 把科学模型转成可被本地机构运营和改进的基础设施
- [[Deterministic-Retrieval]] - 通过结构化工具与领域规则提高科学数据检索的可重复性和可靠性
- Biological-Data-Infrastructure - 为 Agent 设计的科研数据底座
- Laura-Luebbert - 科学智能体基础设施的研究者
- VirBench - 衡量科学检索准确性的基准
