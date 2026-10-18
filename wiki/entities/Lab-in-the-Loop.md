---
type: entity
title: Lab-in-the-Loop
aliases:
  - Lab in the Loop
  - 实验室闭环
  - 实验闭环
  - Replayable Physical Experience
definition: "把真实实验或实验派生的可验证证据组织成 Agent 可连续提出假设、选择实验、接收反馈并修正策略的科学环境；既包括实时自动实验，也包括由预先测量数据构成的可重放物理经验。"
created: 2026-10-18
updated: 2026-10-18
evidence_level: high
claim_type: mixed
tags:
  - ai-for-science
  - scientific-discovery
  - agent-learning
related_entities:
  - "[[Scientific-Discovery-AI]]"
  - "[[Evaluation-Set]]"
  - "[[Agent-Verification]]"
  - "[[Continual-Learning]]"
source_raw:
  - "[[20261014-latentspace-leash-bio-lab-in-the-loop]]"
  - "[[20261009-latentspace-periodic-synthesis-superintelligence]]"
---

# Lab-in-the-Loop（实验室闭环）

> [!definition] 定义
> **Lab-in-the-Loop** 是把科学 Agent 的决策与现实实验反馈闭成循环：模型提出 hypothesis 或下一步实验，环境返回可验证 observation，模型据此更新判断并继续行动。这个概念不要求每一次 rollout 都即时驱动机器人；只要反馈来自可追溯的真实实验，并能保持 action → evidence 的对应关系，预先采集的数据也可以被包装成可重放的物理经验环境。

## 关键数据点

- Periodic Labs 的路线是 **live physical loop**：`hypothesis / simulation → synthesis → characterization → evidence update → next experiment`。每次新知识都要重新经过真实实验，反馈昂贵、延迟高、有噪声，但可以探索此前未测量的现实空间。
- Leash Bio 的路线是 **replayable physical loop**：先通过 DEL 等高吞吐 assay 预先测量数百万 protein × molecule interaction，再让 Agent 从数据库中选择“下一次实验”；结果近实时返回，但仍来自之前真实发生过的物理测量。
- Leash 描述的一个 Agent task 是从约 650 万候选中，在 100 molecule budget 内通过多轮选择寻找最强 binder；每轮结果都用于更新下一轮 SAR hypothesis。
- 两条路线共同要求 provenance、negative / counterfactual evidence、measurement QC 和明确的 observation boundary；否则实验反馈本身也可能被 shortcut、batch effect 或 measurement artifact 污染。

## 两种时间结构

| 形态 | Reality cost 何时支付 | Rollout 速度 | 能否探索未测空间 | 主要瓶颈 |
|---|---|---|---|---|
| **Live Lab-in-the-Loop** | 每轮决策后 | 慢，受物理实验限制 | 可以 | synthesis、仪器、自动化、噪声、sample efficiency |
| **Replayable Lab-in-the-Loop** | 预先批量支付 | 接近软件/数据库速度 | 不可以，除非重新回到实验室 | measurement coverage、dataset bias、counterfactual density |

Periodic Labs 更接近第一种：现实实验本身就是训练环境。Leash Bio 则展示第二种：如果一个实验技术能一次性生成极高密度的组合 measurement landscape，就可以把物理经验“缓存”为 Agent 可大量重放的 sequential environment。

**判断**：两者不是竞争方案，而是可以组合的两级结构：

~~~text
large replayable physical corpus
        ↓
cheap/high-volume agent rollouts
        ↓
identify uncertain or high-value regions
        ↓
live physical experiments
        ↓
expand the corpus
        ↺
~~~

- **证据**：[[20261014-latentspace-leash-bio-lab-in-the-loop]]；[[20261009-latentspace-periodic-synthesis-superintelligence]]。
- **边界**：当前两篇都主要是一手团队访谈。Leash 的 Agent rollout 发生在其已测量 chemical/protein landscape 内；Periodic 的 end-to-end scientific discovery 也尚未提供统一独立 benchmark。不能把“闭环架构存在”外推成“自主科学家已成立”。

## 关键设计条件

### 1. 环境必须返回 Reality Evidence，而不只是 Model Reward

纯 learned simulator 可以高吞吐，但它会继承自身 model error。Lab-in-the-Loop 的核心价值是让 reward / observation 能追溯到现实测量：实验数据、仪器读数、物理 assay 或经过校准的 characterization。

这不意味着实验天然正确。真实实验仍可能受到 batch effect、仪器漂移、蛋白错误折叠、样本污染和观测不完备影响。因此现实反馈需要 QC 与 provenance 才能成为 oracle。

### 2. Counterfactual Density 决定 Agent 能学到什么

只保存“成功实验”会让环境缺少 decision boundary。Leash 的 activity cliffs、binding-pocket mutations、competitive assay，以及 Periodic 强调的 negative/null results，都在增加同一局部邻域中的反事实密度：输入只发生很小变化，但 observation 大幅改变。

**判断**：对 scientific RL，最有价值的数据未必是更多 IID samples，而是更多能区分相邻 hypothesis 的 controlled contrasts。

### 3. Agent Interface 必须保留序贯决策结构

如果把实验 corpus 压成一个静态 supervised dataset，模型只学习 `x → y`；Lab-in-the-Loop 则保留：

~~~text
state
→ choose experiment
→ observe result
→ update belief
→ choose next experiment
~~~

这使同一批现实数据可以训练实验选择、信息增益、hypothesis revision 和预算约束下的探索策略，而不只是单次预测。

### 4. Replay 不能替代 Frontier Expansion

预计算环境再大，也只覆盖已经测过的区域。Leash 的 DEL 数据受 chemical library geometry、building-block availability、DNA conjugation 与 protein panel 限制；Periodic 的 live lab 则受材料、设备和物理时间限制。

因此更完整的系统需要在 replay 与 live experiment 之间切换：先在已知现实数据上便宜探索，再把最有价值、最不确定的候选送回真实实验，扩张 measurement frontier。

## 与 Scientific Discovery AI 的关系

[[Scientific-Discovery-AI]] 描述的是更广义的系统目标；Lab-in-the-Loop 是其中一种 **environment architecture**。它解决的不是“模型是否会科学知识”，而是“模型如何获得足够多、足够真实、可迭代的科学反馈”。

与纯计算 Agent 相比，最大的区别是 oracle 来自现实；与单次 wet-lab validation 相比，最大的区别是实验不只在最后验收，而是进入训练与决策循环。

## 与 Evaluation Set 的关系

[[Evaluation-Set]] 冻结 case 来比较系统版本；Lab-in-the-Loop 则允许 Agent 主动选择下一条 evidence。两者都依赖独立、可信的 oracle，但用途不同：

- Evaluation Set：**测系统**，追求可比性；
- Lab-in-the-Loop：**让系统学会探索**，追求信息增益与策略改进。

同一现实 measurement corpus 可以同时支持两者，但必须划清 held-out eval 与 agent 可探索训练环境，避免 measurement contamination。

## 前提与局限性

- **现实来源不等于无噪声**：measurement protocol、batch、instrument 和 sample quality 仍可能制造系统偏差。
- **可重放环境有 coverage ceiling**：数据库查询只能返回已测量事实，不能自动产生真正新 observation。
- **高吞吐可能放大错误 oracle**：如果实验 pipeline 本身存在系统 artifact，Agent 会更快地优化错误信号。
- **自然语言 reasoning 不是必要条件**：Leash 当前用 language model 构造可审查 SAR reasoning，但 Lab-in-the-Loop 也可以由非语言 policy / planner 驱动。
- **闭环速度不是唯一指标**：科学价值取决于 experiment informativeness、measurement fidelity、成本和能否扩展到真正未知区域，而不是 rollout 数量本身。

## 关联概念

- [[Scientific-Discovery-AI]] — 更上位的科学 Agent 系统范式
- [[Evaluation-Set]] — 与闭环环境共享 oracle / provenance，但目标是版本比较而非主动探索
- [[Agent-Verification]] — 外部 evidence 仍是科学 Agent 结论的主要可信门槛
- [[Continual-Learning]] — 多轮实验经验只有在保留 state/action/evidence lineage 后，才可能安全回流到模型能力
