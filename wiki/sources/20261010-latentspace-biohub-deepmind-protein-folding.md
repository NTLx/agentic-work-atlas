---
type: source-summary
title: "Why AlphaFold Didn't Solve Protein Folding — Pushmeet Kohli, Google DeepMind & Sal Candido, Biohub"
canonical_url: "https://www.latent.space/p/biohub-deepmind"
raw_state: index
original_raw_file: "20261010-latentspace-biohub-deepmind-protein-folding.md"
original_body_sha256: "e670ed95a95f08ef79312510327f744ed52b182bdd7369cb3c570000abea3483"
indexed_at: "2026-10-10T09:04:36+08:00"
created: 2026-10-10
updated: 2026-10-10
tags:
  - source-summary
  - ai-for-science
  - protein-modeling
  - model-evaluation
evidence_level: medium
claim_type: mixed
source_locator:
  - "Transcript L14-L74：data scaling、找到 scaling law 而非假定 scaling law、problem-first 与多学科方法"
  - "Transcript L76-L106：科学归纳偏置、数据规模、data curation 与 architecture 的共同作用"
  - "Transcript L108-L146：AlphaFold 的实际问题边界、PDB structure、protein dynamics 与从局部模型走向系统上下文"
  - "Transcript L148-L190：design vs understanding、模型内部科学信息、pLDDT calibration 与 behavioral characterization"
  - "Transcript L192-L216：临床/药物发现中的 AI、10x acceleration 与基础研究边界"
---

# Why AlphaFold Didn't Solve Protein Folding

> Latent Space 生物建模圆桌，嘉宾为 Google DeepMind 的 Pushmeet Kohli 与 Biohub 的 Sal Candido。用户提供了完整 216 行 Transcript。本文适合支持两位一线研究者对 AlphaFold 问题边界、AI-for-Science 数据策略、归纳偏置和可信使用方式的判断；但它是会议对谈而非系统实验，许多路线判断、未来预测和经验性例子未在现场给出可独立复核的定量结果，因此按 medium / mixed evidence 处理。

## 编译摘要

### 1. 浓缩

- **核心结论 1：科学 AI 的“bitter lesson”不是盲目 scale，而是先找到一个真正存在 scaling law 的问题表述。**
  - Candido 明确区分“scaling law 到处都天然存在”和“研究工作本身就是找到那个可扩展区间”：只有数据包含解决目标问题所需的 information statistics，继续增加 data / compute 才会稳定转化成能力（Transcript L20-L44）。
  - Kohli 将这一点进一步抽象成 problem-first：不要先把自己定义成“modeler”或“data-generation person”，而应先问要解决什么问题，再决定资源应该投到 modeling、compute、data generation 还是 domain expertise（L48-L74）。
  - **综合判断**：Scientific Discovery AI 的第一层设计变量不是模型架构，而是 `problem specification → information requirement → feasible data/measurement → model/compute`。Scaling 是这个链条成立后的放大器，不是替代问题定义的万能策略。

- **核心结论 2：科学先验与 scale 不是二选一；数据稀缺时 inductive bias 提高样本效率，数据扩大后错误先验反而可能成为上限。**
  - Kohli 以 AlphaFold 为例说明，biophysics / biochemistry 中已知的 residue interaction 应被显式利用，因为这让模型不必重新从有限数据中学习全部结构；同时他强调 data curation 本身也是“art”，重复更多同质数据不会产生新信息（L76-L90）。
  - Candido 则给出条件性边界：小数据下更多 inductive bias 往往必要；数据增大后，模型可能发现人类此前未知的结构，而不准确的先验可能限制模型。即使进入大规模阶段，architecture、infra、inference efficiency 和“下一批真正提供新信息的数据”仍需要大量工程与研究 craft（L94-L106）。
  - **综合判断**：更准确的资源分配问题不是 `craft vs scale`，而是每一规模下重新判断 **新增一单位先验、数据、算力或架构工作，哪一个带来的信息增益最大**。

- **核心结论 3：“AlphaFold 解决了 protein folding”是一个过宽的传播压缩；AlphaFold 解决的是更窄、但非常有用的结构预测任务。**
  - Kohli 明确说，团队并不知道蛋白真正的 ground-state distribution；他们实际优化的问题是：已有研究者获得并存入 PDB 的 structure，模型能否重现同类 structure。这个目标非常有用，但不等于理解 protein dynamics、context-dependent conformations、disorder、function 或完整 folding distribution（L108-L124）。
  - Candido 用“spoke → wheel → bicycle”的类比说明，当前模型可能把一个局部对象建得越来越好，但真正的生物问题常要求把蛋白放回更大的细胞/系统上下文；单一结构模型并不自动扩展成对整个 biological system 的理解（L138-L146）。
  - **综合判断**：科学模型的成功必须绑定其 **measurement target / reference distribution / operating scope**。把 benchmark contract 的成功升级成“领域问题已解决”，会把模型最重要的未覆盖变量从研究议程里抹掉。

- **核心结论 4：更接近原始测量的数据可能保留被人工结构标签压缩掉的科学信息。**
  - Kohli 以 cryo-EM micrographs 为例：与其只训练 PDB 中已经推断出的结构，是否可以直接在更接近观测源头的 micrographs 上建模，从中恢复结构的 distributional / dynamic information；他明确说自己尝试过，但模型和数据规模仍需要更多工作（L126-L136）。
  - **综合判断**：在 AI-for-Science 中，derived labels 往往是高价值但有损的 projection。模型越接近 raw measurement，理论上越可能学习到标注流程没有保留的 latent structure；代价是数据规模、噪声、计算量和识别问题显著增加。

- **核心结论 5：科学模型“可理解”的最低要求首先是 behavioral characterization 与 uncertainty calibration，而不是人类能够逐神经元解释机制。**
  - Kohli 用 AlphaFold 的 pLDDT 做反例：即使结构精度很高，如果 confidence / uncertainty 完全失准，研究者可能在错误预测上投入一年，因此模型给出什么、在哪些条件下可靠、哪里不可靠，是使用模型前必须知道的行为契约（L172-L186）。
  - 他区分两类 interpretability：一类是人类能否理解模型为什么这样算；另一类是用户是否理解模型的 strengths / limitations。前者可能受人类认知和计算能力限制，后者则是安全、可行动使用的必要条件；他甚至提出未来更强模型可能比人类更能解释另一个模型的内部行为，但这只是开放猜想（L176-L190）。
  - **综合判断**：对于科学 world model / predictor，可信使用的最小合同是 `capability boundary + calibrated uncertainty + known failure modes + external validation`。Mechanistic interpretability 有价值，但不能替代这套操作性合同。

- **核心结论 6：AI 的临床价值不应被压缩成“是否已有全 AI 药物”，而应按研发链条上的实际 outcome acceleration 来测量。**
  - Kohli 指出 AI 已进入药物发现多个阶段，但“什么时候 10x/100x 加速”取决于问的是 target discovery、lead optimization、preclinical、tox 还是别的环节；真正的大幅提速仍需要解决基础生物学难题（L192-L200）。
  - Candido 同样反对只追逐一个象征性终点，主张从 first principles 反问“怎样做到 10x 而不是 10%”，以迫使团队扩大解空间，同时保留增量路径的价值（L204-L214）。

### 2. 质疑与证据边界

- **“AlphaFold 没解决 protein folding”本身也是传播标题，不应反向过度纠正。** Kohli 的核心是任务边界：AlphaFold 对 PDB-style structure prediction 做出了重大突破，但不能推出对 dynamics / function / distribution 的完整理解。本文不能据此否定 AlphaFold 在结构生物学中的真实效用。
- **problem-first / scaling-law 论述主要是方法论。** Transcript 没有提供跨项目实验去证明这种资源配置总是优于 model-first 或 data-first；它更适合作为研究设计原则。
- **metagenomic “低质量数据仍提升 protein LM”是 Candido 的经验例子。** 现场没有给模型、数据版本、指标和 effect size，因此只支持“非 pristine 数据也可能含有有用 information statistics”，不能量化收益。
- **cryo-EM raw-data route 是研究方向，不是已完成系统。** Kohli 明确说自己尝试过且仍需更多工作；不能把“原始测量保留更多信息”直接推出“端到端 raw model 已优于 PDB-based model”。
- **pLDDT calibration 的原则性例子很强，但本文没有给 calibration curve。** 若要写具体 ECE、coverage 或版本间比较，必须回到 AlphaFold 原论文/技术资料核验。
- **“更大模型可以解释较小模型”是推测。** 它没有在本对谈中被实验证明，更不能当作 mechanistic interpretability 的替代方案。
- **临床时间线刻意保持不确定。** 两位嘉宾都拒绝给出“纯 AI 药物何时出现”的确定时间，因此不应从本文生成具体临床落地预测。

### 3. 对标与知识连接

- **与 [[Scientific-Discovery-AI]] 对标**：本文把库内已有“搜索 / objective / simulation / experiment”框架再向前推一步：先判断问题真正缺的是模型、数据、测量还是 domain knowledge。它也修正了“AlphaFold = protein folding 已解决”的宽泛表达，把成功重新绑定到 PDB-like structure prediction 的 reference contract。
- **与 [[World-Model]] 对标**：protein language model / structure model 可能压缩出 structure、function、motion 等内部表示，但“内部含信息”不等于“可安全行动”。行为边界和 uncertainty calibration 是 world model 对外成为科学工具前的最小使用合同。
- **与 [[20260826-latent-space-anima-physical-world-models]] 对标**：Anima 强调物理域必须利用结构先验；本访谈给出更动态的边界——小数据时先验提高 sample efficiency，数据增大后错误先验可能限制 discovery。两者共同反对把 generic transformer scaling 当成无条件默认。
- **与 [[20261009-latentspace-periodic-synthesis-superintelligence]] 对标**：Periodic 强调现实实验是 ultimate truth；本访谈进一步说明输入 reality evidence 也有层级：PDB 是科学流程产生的 derived representation，cryo-EM micrograph 更接近 raw measurement。验证链不仅要“回到现实”，还要知道现实是经过什么观测/压缩过程进入模型的。
- **与 [[20260923-latentspace-eric-biosecurity]] 对标**：Radical Numerics 强调 domain-native biological representation；本访谈补充 representation 的评价标准：不仅看 task score，还要问数据是否包含目标问题所需的信息、模型 confidence 是否校准、行为边界是否已知。

## 结论

这场对谈最重要的修正不是“AlphaFold 成功还是失败”，而是把 Scientific Discovery AI 的设计顺序重新排列：

```text
problem / desired outcome
  → what information would resolve it?
  → what measurement / data actually contains that information?
  → what scientific priors remain reliable at this data scale?
  → what architecture / compute extracts it efficiently?
  → how is uncertainty calibrated and failure behavior characterized?
  → does the result change the real scientific / translational outcome?
```

**Scale 只有在这条链条成立后才是杠杆。** 对科学 AI 来说，最大风险之一恰恰是把一个清晰、可测、可扩展的代理问题做得极好，然后把代理问题的胜利误写成原始科学问题已经被解决。

## 关联概念

- [[Scientific-Discovery-AI]]
- [[World-Model]]
- [[Tool-Use-Architecture]]
- [[Agent-Verification]]
- [[20260826-latent-space-anima-physical-world-models]]
- [[20260923-latentspace-eric-biosecurity]]
- [[20261009-latentspace-periodic-synthesis-superintelligence]]
