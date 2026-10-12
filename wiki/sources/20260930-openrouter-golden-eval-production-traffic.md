---
type: source-summary
title: "Building a Golden Eval Dataset from Production Traffic"
canonical_url: "https://openrouter.ai/blog/tutorials/building-a-golden-eval-dataset-from-production-traffic/"
source_raw:
  - "[[20260930-openrouter-golden-eval-production-traffic]]"
raw_state: index
created: 2026-10-12
updated: 2026-10-12
tags:
  - source-summary
  - evaluation
  - production-data
  - regression-testing
evidence_level: medium
claim_type: mixed
source_locator:
  - "What a golden eval dataset is"
  - "Why production data is the better foundation"
  - "Step 1: Pull a sample of production traffic"
  - "Step 2: Deduplicate and cluster"
  - "Step 3: Add expected outputs"
  - "Step 4: Run a first evaluation and fix the rubric"
  - "Step 5: Commit to Git, wire into CI, iterate"
  - "Cross-model benchmarking through one API"
  - "FAQ"
---

# Building a Golden Eval Dataset from Production Traffic

> OpenRouter 面向生产 LLM/Agent 应用的评测教程。稳定价值在于把“从真实流量构造回归集”拆成采样、去重/聚类、风险加权、专家标注、rubric 校准、版本化与 CI 的完整生命周期。具体样本数、刷新频率与平台 API 属于经验性建议或产品实现，不应升级为普适阈值。

## 1. 浓缩

### 1.1 Golden Set 是版本化的 deployment-distribution contract，而不是静态 benchmark

来源把 golden eval set 与 public benchmark、training set、live A/B 明确区分：它由真实产品流量中的输入、经过审查的 expected behavior / rubric，以及运行时配置共同构成；在候选版本进入线上 A/B 前先运行，用来判断行为是否仍在可接受边界内。

更稳定的抽象是：

```text
Golden eval contract
= production-distribution sample
+ risk-weighted tail
+ reviewed expected behavior
+ rubric / evaluator
+ provenance metadata
+ frozen baseline
```

**判断**：golden set 的核心不是“有一批好题”，而是把**当前产品分布中的行为契约**冻结成一个可重放资产。它回答的不是“模型一般有多聪明”，而是“这个候选系统对我们真实用户正在做的事情，是否仍然足够正确”。

### 1.2 纯频率采样不够：部署分布需要与风险尾部共同表示

生产流量的优势是经验分布：真实用户怎么问、哪些 feature 被使用、失败模式如何出现、产品行为如何随时间漂移。相比纯 synthetic set，它更接近系统真正会遇到的输入。

但来源同时强调：去重/聚类后不能只按频率保留样本。低频但代价很高的错误需要被故意加权，否则 head traffic 会吞没 critical tail。

因此评测集抽样目标更接近：

```text
coverage target
= observed frequency distribution
+ deliberately overweighted high-cost / critical tail
```

**判断**：production-derived 不等于“随机抽一批线上请求”。真实分布负责 realism，风险加权负责 safety / business consequence；两者缺一都会产生系统性盲区。

Synthetic data 更适合被标记为 augmentation layer：当真实流量暂时没有覆盖某个已知 failure mode 时补洞，而不是静默混进真实样本后失去 provenance。

### 1.3 第一轮 baseline 不是只测模型，也是在测 oracle

来源要求 domain expert 为 case 写 expected output 或 rubric，并建议对一部分样本做 independent double annotation。两位 reviewer 的分歧不是简单平均掉，而是 rubric ambiguity 的信号。

第一轮跑 eval 后，失败还需要重新分类：

```text
observed failure
  ├─ real model / system failure
  ├─ wrong or ambiguous expected answer
  └─ rubric / evaluator defect
```

**判断**：Evaluation Set 自身也是待验证的软件资产。没有经过 baseline calibration 的 golden set 可能把标注错误、模糊需求或 judge 偏差包装成“模型回归”。

这与 [[Agent-Verification]] 中“验证 harness 自身也是错误来源”的规律完全一致：oracle 不是因为被写进测试文件就天然可信。

### 1.4 Dataset × Rubric × Baseline 必须一起版本化

教程建议把 dataset、rubric 与 baseline 一起提交版本控制，并在 CI 中用较小子集做 PR gate、较大集合做 nightly/release 检查。

这里的关键不是 Git 本身，而是**归因完整性**：

```text
Eval Result
= f(dataset version,
    rubric/evaluator version,
    baseline version,
    system configuration)
```

如果 case、rubric 和 baseline 在不同时间独立漂移，那么分数变化无法回答“候选系统变差了，还是测试定义变了”。

**判断**：golden eval 的最小 provenance unit 不是单个 JSONL 文件，而应至少绑定：

- dataset version；
- rubric / evaluator version；
- baseline result；
- prompt/model/tool/retrieval 等系统版本；
- sample transformation / privacy provenance。

### 1.5 Production traffic 的隐私处理也是可复现性的一部分

真实流量可能包含 PII、敏感业务内容或受服务条款限制的数据。来源要求在进入 eval 前清理，并记录 transformation。

**判断**：privacy scrub 不能只是一次性清洗动作。若一个 case 的原始形态经过脱敏、截断、重写后改变了任务难度，那么这种 transformation 已成为 eval semantics 的一部分，应进入 provenance。

### 1.6 Golden Set 是长期演化资产，但单次比较必须冻结

产品分布会漂移，因此来源建议定期 review、补充新失败模式、保留已经长期通过但仍代表行为契约的 case。

这形成两个时间尺度：

```text
between product epochs:
  refresh / expand the golden set

within one candidate comparison:
  freeze dataset + rubric + baseline
```

**判断**：维护评测集与冻结评测集并不矛盾。前者负责跟随现实变化，后者负责一次实验内部的因果可比性。

## 2. 对现有知识的增量

### 对 [[Evaluation-Set]]

现有页面已强调评测集是业务判断与验收规则的可复用资产。本文补足其**生产分布构造与版本治理**：

- 真实流量提供 empirical distribution；
- risk weighting 补 critical tail；
- expert annotation 构造 oracle；
- first baseline 反过来校准 rubric；
- dataset/rubric/baseline 作为一个 provenance unit；
- product drift 驱动长期 refresh。

### 对 [[Evals-as-PRD]]

Dianne Penn 的案例是从模糊用户抱怨追到具体失败，再凝结成 eval。OpenRouter 这篇则提供了组织规模化后的下一步：**不仅从投诉生成 eval，也从持续生产流量中维护 executable product spec。**

完整链可以扩展为：

```text
production logs
  → privacy scrub + provenance
  → dedup / cluster
  → frequency + risk weighting
  → expert expected behavior / rubric
  → evaluator QA
  → CI regression
  → new production failures
  → refresh next eval epoch
```

## 3. 证据边界

- 这是 OpenRouter 商业平台教程，不是不同 eval 方法的受控比较研究。
- 10、20–50、100–1000 等样本规模属于启发式经验，不能作为通用质量阈值。
- 生产流量会继承历史用户分布、产品偏差与既有系统盲区；“真实”不等于“完整”或“公平”。
- 风险加权需要业务判断，可能被错误风险模型反向扭曲。
- LLM-as-judge 即使经人类样本校准，仍有非确定性、共源偏差和模型更新风险；高后果 case 不应只依赖单次 judge。
- provider routing、模型别名和参数支持会影响复现性，因此跨模型比较只有在 execution envelope 足够明确时才有意义。

## 4. 关联概念

- [[Evaluation-Set]]
- [[Evals-as-PRD]]
- [[Agent-Verification]]
- [[Rubric-Based-Evaluation]]
- [[Evaluator-Miscalibration]]
