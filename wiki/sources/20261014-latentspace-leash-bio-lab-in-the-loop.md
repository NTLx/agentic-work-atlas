---
type: source-summary
title: "Lab-in-the-Loop at Compute Speed — Ian Quigley, Leash Bio"
canonical_url: "https://www.latent.space/p/lab-in-the-loop-at-compute-speed"
raw_state: index
original_raw_file: "20261014-latentspace-leash-bio-lab-in-the-loop.md"
original_body_sha256: "2547e957825403ca538160f0140de91e5d9bf211040c0b485f9dc5c78bcb4867"
indexed_at: "2026-10-18T23:05:23+08:00"
created: 2026-10-18
updated: 2026-10-18
tags:
  - source-summary
  - ai-for-science
  - scientific-discovery
  - drug-discovery
  - evaluation
  - reinforcement-learning
evidence_level: medium
claim_type: mixed
source_locator:
  - "Transcript L40-L190：DEL 原理、barcode controls、实验可重复性与大规模 assay 质量控制"
  - "Transcript L267-L388：4B interaction Kaggle 数据、OOD eval 设计、unseen chemical library 上无人优于随机"
  - "Transcript L398-L448：Hermes、building-block / cluster split、XGBoost baseline 与 memorization 检查"
  - "Transcript L450-L560：Clever Hans / chemist authorship 实验，creator identity 足以预测 activity"
  - "Transcript L562-L590：只在内部实验数据训练、外部数据评测，以及公开模型的训练集污染边界"
  - "Transcript L592-L764：activity cliffs、protein mutations、competitive assay 与用实验反事实约束 shortcut learning"
  - "Transcript L784-L852：自然语言 chemistry representation、Agent 自选实验、database lookup 形成 compute-speed reinforcement rollout"
  - "Transcript L854-L866、L878-L1114：chemical-space 边界、转化/ADMET 约束、数据与实验流程护城河"
---

# Lab-in-the-Loop at Compute Speed — Ian Quigley, Leash Bio

> Latent.Space AI for Science 对 Leash Bio 联合创始人兼 CEO Ian Quigley 的访谈。用户提供了 1122 行完整 Transcript；本次编译以该 Transcript 为主要证据。canonical 页面当前显示发布日期为 **2026-10-14**，而附件 frontmatter 写作 2026-10-15；Raw 已按 canonical 页面日期做最小元数据校正。访谈对 assay 设计、数据质量与训练闭环提供了高密度一手机制材料，但 Leash 自身模型性能、数据规模、药物项目和商业优势仍主要是公司一方陈述，因此整体按 `medium / mixed` 处理。

## 编译摘要

### 1. 浓缩

#### 核心结论 1：科学 AI 的数据优势首先来自“可扩展且可审计的测量系统”，不是简单堆更多样本

Leash 选择 DNA-encoded library（DEL）的核心原因，是它能把数百万到数亿小分子放在同一 pooled assay 中，再通过 DNA sequencing 读取哪些分子与蛋白结合。真正困难的不是 nominal scale，而是如何把 assay artifact 变成可识别、可控制的变量（Transcript L40-L190）。

最典型的设计是：同一个小分子用 32 或 48 个不同 barcode 编码。如果某个蛋白实际上黏的是 DNA 而不是小分子，不同 barcode 会表现出差异；反过来，如果多个 barcode 对同一 chemical 的 enrichment 一致，才更像是真实 chemical signal。团队还用 fresh protein batch、fresh library batch 的重复实验检查长期 reproducibility。

**判断**：在 AI for Science 中，measurement throughput 只有与 artifact controls、metadata、replicate 和 provenance 一起扩展时，才会变成可学习的数据资产；否则 scale 只是在更快地产生 shortcut。

#### 核心结论 2：评测必须主动切断“容易记住的相似性”，否则模型能力可能只是数据结构泄漏

Leash 的 Kaggle competition 释放了约 40 亿次物理 interaction measurement，并设计三档 holdout：共享 building block、仅共享 scaffold/hub、以及来自完全不同 chemical library 的 hardest split（Transcript L267-L388）。约 2,000 支队伍在前两类 split 上能取得不同程度表现，但在完全不同 library 的最难 eval 上没有模型稳定优于 chance。

Hermes 后续进一步用 building-block identity split 和 similarity-cluster split 检查 memorization，并一直保留 XGBoost 这类简单 baseline。XGBoost 随分布距离增加明显下降，而 Hermes 在这些 split 上更稳定；这至少说明“随机拆 train/test”远远不够，必须设计能切断近邻记忆的结构化 OOD eval（L398-L448）。

**判断**：科学模型的 evaluation contract 应围绕“模型是否仍能在刻意移除 shortcut 后成立”设计，而不是围绕随机 holdout 的平均分。

#### 核心结论 3：公开科研数据可能主要编码“谁做了什么”，而不是你以为的自然规律

访谈最强的反例是所谓 Clever Hans / chemist authorship 实验（Transcript L450-L560）。团队从 ChEMBL 收集 1,815 位高产 chemist 的分子，仅看 molecule structure 就能以约 60% top-5 accuracy 猜出 creator。更进一步，他们把 molecule 表示完全替换成一个约 1,800 维的“由谁创造”的概率向量，再预测 activity，表现可以做到与使用 chemical formula 相近；把两者组合也没有显著增益。

Leash 的解释是：药物化学数据包含大量社会过程指纹——chemist 偏好、机构可获得的 building blocks、项目类别、历史成功经验、哪些分子值得继续合成等。模型可以利用这些规律得到预测力，但这不等于理解 protein-ligand physics。

> “train models on the exhaust” 的风险不是数据完全无用，而是**observational exhaust 同时混合了世界规律与人类选择机制**。

**判断**：高预测性能不能自动证明模型学到了目标机制。只要 dataset 的生成过程与标签相关，模型就可能用生成过程的代理信号取代因果机制。

#### 核心结论 4：高价值科学训练数据应包含人为构造的反事实和 activity cliffs，而不是只记录自然发生的成功案例

Leash 不只采集更多 wild-type protein × molecule 数据，还主动制造“近似但行为剧变”的样本（Transcript L592-L764）：

- chemical 侧：设计只差一个很小 substituent 的 molecule pairs / series；
- protein 侧：定点 mutation 改变 binding pocket 的某个 amino acid；
- assay 侧：加入已知 competitor，观察原有 binder 是否被挤出；
- validation 侧：检查 mutation 是否只影响特定 chemical series，而不是把整个 protein 破坏掉。

这种设计把 activity cliff 从“讨厌的例外”变成训练信号：两个输入极相似，但一个微小变化引发巨大 behavior delta。它迫使模型学习哪些局部变化真正重要。

Hermes 的 attention map 曾显示模型主要盯着 protein 中非保守、容易识别的短片段——像给每个 protein 起了“nickname”，而不是理解 binding pocket。加入大量 pocket mutations 后，attention 分布变得更均衡。这里最稳妥的解释不是“attention 已证明物理机制”，而是：**interpretability signal 暴露了一个 plausible shortcut，随后用真实实验反事实去破坏该 shortcut，并重新训练。**

#### 核心结论 5：Lab-in-the-Loop 的关键创新，是把已经发生过的真实实验压成 Agent 可近实时调用的科学环境

访谈后半段描述了一种与传统 robotic lab 不同的闭环（Transcript L784-L852）。Leash 已经预先测过大量 protein × molecule interaction，于是可以给 reasoning Agent 一个初始状态，例如 10 个 binder + 10 个 non-binder，再允许它从数百万候选中选择下一批 5–10 个“实验”。所谓“运行实验”实际上是查询已经由真实世界测量过的结果，因此几乎瞬时返回；Agent 据此更新 hypothesis，再选择下一轮。

~~~text
physically measured assay corpus
        ↓
initial binders / non-binders
        ↓
agent forms SAR hypothesis
        ↓
selects next molecules to test
        ↓
database lookup of real measured outcomes
        ↓
instant grounded feedback
        ↓
update hypothesis / choose next experiment
        ↺
~~~

受访者描述的一个当前任务是：给 Agent 100 个 molecule budget，让它从约 650 万候选里通过多轮选择找到最强 binder。由于每次反馈来自先前真实实验，而不是一个纯 learned simulator，这比普通离线 benchmark 更接近“replayable physical environment”。

**判断**：Lab-in-the-Loop at compute speed 的本质不是“让湿实验突然和 GPU 一样快”，而是**用高密度现实测量预先支付实验成本，再把这些 measurements 重新包装成可进行大量 sequential decision rollouts 的环境。**

#### 核心结论 6：Natural language 在这里承担的不只是交互界面，而是对科学推理的可审查 bottleneck

Leash 从 Hermes 这类 embedding + cross-attention 模型进一步尝试 language model：先教模型把 molecule / protein difference 描述为可读英文，再让 reasoning model 用这些描述提出 SAR hypothesis、选择下一组实验并更新结论（L772-L852）。Quigley 把自然语言称为一种可能的 regularizer：相比参数量不断增大的黑盒模型，语言表示迫使中间 hypothesis 落到更有限、更可审查的语义空间。

这不是“自然语言天然更接近物理”的证明。它更像一种工程权衡：牺牲部分表示自由度，换取 hypothesis 的可读性、序贯推理接口和与 Agent RL 的兼容性。

#### 核心结论 7：真正难复制的护城河可能是实验纠错文化，而不是 assay 或模型本身

访谈最后面对“资金更多的实验室能否直接 scale 过去”的问题时，Quigley 给出的答案主要不是专利算法，而是 process discipline（L1044-L1082）：长期追踪 batch effects 和仪器 metadata；让实验人员低摩擦记录元数据；发现异常后追溯整个历史数据；重建 selection / protein-expression 流程；为 misfolded protein 寻找可自动化 proxy。

Lumacaftor-like molecules 的例子很典型：团队发现一类本应帮助 misfolded protein 的 chemical series 在许多异常 protein screen 中反复出现，于是把它变成“protein 可能没有正确折叠”的 QC signal，并据此剔除或重跑训练数据。

**判断**：当模型的数据来自复杂现实流程时，data moat 往往不是静态 dataset，而是一个会持续发现、解释并修复 measurement failure 的组织能力。

### 2. 质疑与证据边界

- **公司一手陈述不是独立 benchmark。** “约 2,000 protein constructs、约 5,000 screens、每次至少 650 万 molecules”“100 molecule budget 找到最强 binder”“6 个月从 DEL hit 到 mouse PK/PD”等主要来自 Ian Quigley 的访谈陈述；部分数据集和比赛公开可查，但本次 Transcript 本身不能独立验证全部 operational claims。
- **Kaggle hardest split 的失败证明“当时这些方法没有泛化”，不证明 protein-ligand binding 原理上只能靠更多 Leash 数据解决。** 更好的 architecture、结构先验、physics model 或外部数据仍可能改变结论。
- **chemist-authorship 实验揭示强 confounding，但不能推出 ChEMBL“没有 chemistry signal”。** 更准确的结论是：sociology 足以形成极强 shortcut，因此任何 activity model 都必须证明增益不是主要来自 creator / project / molecular-weight 等代理特征。
- **attention map 不是机制证明。** Hermes 盯着非保守序列可以提示“nickname memorization”，但 attention 本身不能证明这是完整因果机制；真正增强可信度的是随后加入真实 protein mutations 后观察 generalization 与 attention behavior 是否共同改变。
- **Lab-in-the-Loop 不是实时发现新自然事实。** lookup 环境只能探索已经被 Leash 实际测量过的 protein × molecule landscape；Agent 无法从数据库中获得尚未测量的 chemical space。真正突破现有 measurement envelope 最终仍要回到 live experiment。
- **预计算实验环境仍有 dataset bias。** 它继承 DEL library geometry、building-block availability、DNA conjugation、protein-production quality 和 assay protocol 的边界；“physically grounded”不等于“覆盖完整现实”。
- **自然语言 regularization 是早期假设。** 访谈没有给出与更大 Hermes、graph model 或其他 policy representation 的系统消融，不能据此认定 language Agent 已是最佳 architecture。
- **binding 只是药物开发早期一层。** ADMET、PK/PD、toxicity、cellular context、clinical efficacy 等高层结果没有同等规模的 oracle；受访者也承认 DEL read count 到 KD 的精确映射仍未解决。

### 3. 对标与约束

- **与 [[Scientific-Discovery-AI]]：从 live physical loop 补出“replayable physical experience”。** Periodic Labs 强调实验现实是昂贵、延迟、带噪声的最终 evidence；Leash 则展示另一种可扩展形态——先用 pooled assay 高吞吐支付 reality cost，再把测量结果做成 Agent 可高速重放的 sequential environment。两者共同说明物理科学 RL 的关键是如何获得大量**可验证、可追溯的现实反馈**。
- **与 [[Evaluation-Set]]：hard split 必须按潜在 shortcut 设计。** 随机 split 会保留 building-block、scaffold、chemist identity 等泄漏；真正的 evaluation 应主动构造 distribution break，并用简单 baseline 测试“便宜策略”还能拿多少分。
- **与 [[Mechanistic-Interpretability]]：science-domain interpretability 最有价值的用法之一是产生可实验检验的 shortcut hypothesis。** 本访谈中的 attention map 本身不是 mech-interp 因果证明，但它触发了对 protein “nickname”策略的怀疑；随后通过物理 mutation 修改数据生成过程，才把解释假设变成更强 evidence。
- **与 [[20261009-latentspace-periodic-synthesis-superintelligence]]：两种 lab loop 的时间结构不同。** Periodic 追求 live `hypothesis → synthesis → characterization → next experiment`；Leash 把大量已经发生的真实 assay 压缩成 lookup environment，以牺牲“立即探索全新空间”换取数量级更高的 rollout throughput。

## 当前稳定判断

**判断**：AI for Science 的下一层 scaling unit 可能不是单纯 `more papers / more parameters / more robots`，而是 **可反复调用的、带反事实结构的现实证据环境**。其质量合同至少包含：

~~~text
high-throughput physical measurement
+ artifact controls
+ structured counterfactuals / activity cliffs
+ provenance & batch metadata
+ shortcut-aware eval splits
+ sequential agent interface
→ grounded scientific rollouts at software-like speed
~~~

这类环境可以显著缩短 Agent 学习“如何做下一步实验”的反馈周期，但它不会消除 reality gap；一旦 Agent 走出已测量空间，最终仍要重新支付真实实验成本。

## 关联概念

- [[Lab-in-the-Loop]]
- [[Scientific-Discovery-AI]]
- [[Evaluation-Set]]
- [[Mechanistic-Interpretability]]
- [[Agent-Verification]]
