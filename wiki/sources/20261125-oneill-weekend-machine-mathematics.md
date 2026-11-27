---
type: source-summary
title: "A weekend of machine mathematics — Charlie O’Neill"
canonical_url: "https://charlesponeill.com/posts/a-weekend-of-machine-mathematics/"
original_raw_file: "raw/20261125-oneill-weekend-machine-mathematics.md"
original_body_sha256: "64e0b8636042b753fef8e5b108662694194e3ad27a0b1ad174d9a9f7b4fe30c3"
indexed_at: "2026-11-26T12:42:03+08:00"
raw_state: index
created: 2026-11-26
updated: 2026-11-26
tags:
  - source-summary
  - mathematics
  - AI-capabilities
  - verification
evidence_level: medium
claim_type: mixed
source_locator:
  - "Opening: weekend scope, undergraduate mathematics background, self-reported API expense and compulsive feedback"
  - "How I began: RH/GRH as changed premise; selection of conditional research opportunities"
  - "The six results: six claimed quantitative improvements, code/PDF release link, certificates, Lean"
  - "I was quite miscalibrated: multiple obstacles, method ceilings, local search versus conceptual shift"
  - "I wasn’t bitter-lesson pilled enough: intervention frequency and alternating optimization/exploration"
  - "Open-weight models did it too: rederivation with DeepSeek and Kimi, some hints, writeup pending"
  - "QED: authorship, recognition and human contribution"
  - "leanprover-community/riemann-hypothesis README: Theorem Statements / Cache / purpose and branch history"
---

# A weekend of machine mathematics：可磨性、研究判断与证明的独立验收

> 来源：[Charlie O’Neill，2026-11-25](https://charlesponeill.com/posts/a-weekend-of-machine-mathematics/)。个人实践回顾而非同行评议论文。已读取官方文章全部正文；[六项成果发布页](https://charlesponeill.com/maths-releases/) 未能访问，故未核验原始证明、计算证书、基准或文献优先权。另阅读 [RH/GRH 社区 Lean 仓库](https://github.com/leanprover-community/riemann-hypothesis) README，未执行构建、Lean kernel 或 nanoda 验证。以下成果均按作者报告记载，而不是本库独立证明。

## 编译摘要

### 1. 浓缩

#### 1. 外部知识突破改变问题空间，但不自动消除所有障碍

作者借 RH/GRH 证明发布寻找以往受条件限制的研究方向，发现原先预估的跃迁并未发生。RH 对某些既有条件性定理足够，却不意味着能推出 Legendre 猜想或 ζ 函数六阶矩的预测精确常数。**综合判断**：新前提应触发依赖图重算，把直接推论、仍缺关键引理、仅受启发的探索分开；不能把旧路线的主要障碍误认作唯一障碍。

#### 2. 六项自报成果是边界改善，不是六个猜想全部解决

定位：The six results。下列是作者声称的结果，未独立复算；百分比及常数沿用其归一化与统计口径。

| 方向 | 文章报告 |
|---|---|
| ζ 函数六阶矩 | 归一化下界 41.008 → 41.6406，预测值 42 仍未达到 |
| 二次 L 函数中心值 | 非零比例 94.27% → 超过 94.53%，不等于 Chowla 猜想 |
| 连续幂之间素数 | 指数 11/5 的全范围结论；另报告 Legendre 猜想仅核查至 n=10¹⁴，不能外推全域 |
| 算术级数最小素数 | 超过 58.7% 的模数满足作者陈述的界 |
| Hadwiger–Nelson | 6-可染色保证扩大到 10,689 顶点或 245,510 边；不决定平面色数 |
| 七循环强积 | 四次、五次强积独立数上界分别 115 → 112、401 → 392；称使用 Lean |

第三项报告约 59 万亿次区间检查、51.69 TB 证书；这是作者披露的计算规模，不是本库核验的覆盖率、完整性或资源账单。

#### 3. 分清内层求解与外层路线搜索

作者在六阶矩工作中发现路径存在低于预测目标的上限；模型能够帮助改进技术细节，也能在请求反思时给出上限判断，但经常持续沿既定方向探索。作者观察长时间少干预的线程有较多进展，仍认为切换深入求解与整体审视有价值。其提出明确目标加 checker 的循环，是回顾性的改进建议，并非本次已完成的控制实验。

**综合判断**：内层在固定证明框架、算法或目标下搜索；外层评估方法的可达域、边际成本及下一条候选路径。若出现理论上限、重复失败、可验证增益趋零或预算耗尽，应先停止或改题，不以 token、运行时长和试验次数替代进展。

#### 4. 成果正确性、证明理解与科研信用不能合并

原文承认自身对数学成果理解有限，并披露强反馈造成持续工作冲动；开放权重 DeepSeek、Kimi 的重推导也有部分提示，详细报告尚待发布。

**综合判断**：区分形式化定理是否准确陈述、允许依赖、公理/证明检查、数值计算覆盖与可重放、既有文献比对、专家解释、贡献归属。证明检查可以降低验证成本，却无法自动证明新颖性、研究意义或全套系统安全。重推导可能复用已知解题线索，不等价于独立从零发现。研究任务还应设置总成本、停机与人工升级约束，避免即时反馈把搜索变成不受控资源消耗。

### 2. 质疑

- **样本与归因**：一次个人周末实践缺少失败任务总数、模型配置、完整调用轨迹、各线程成本和对照策略，不能建立少干预、长运行或模型代际造成数学突破的因果关系；作者提到数千美元 API credits 的语境并不是完整核算。
- **范围与数学语义**：必须回查六篇原始定理、参数范围、归一化、严格不等式、边界条件及既有最佳结果。Legendre 的有限范围计算与指数 11/5 的全域命题应保持独立；六阶矩界改善不能称为解决猜想。
- **证书独立性**：51.69 TB 数据量不等于完整证明；要核对分片覆盖、区间端点、重复与缺失、检查器及其版本和证书重放结果。Lean 也需要实际定理陈述与依赖清单，而非仅记录“通过”。
- **背景定理**：RH/GRH 社区仓库 README 表示维护形式化成果，并说明 comparator 与 Lean、nanoda 的检查设计。其存在不代替本轮重跑，也不证明 O’Neill 的所有结果均依赖或使用该证明。
- **开放权重重推导**：作者未公开本轮模型精确版本、提示量、总算力、失败轨迹与盲测条件；不能外推为开放模型已匹配前沿模型的原创研究能力。
- **方向与人类责任**：概念创新与既有工具的重新组合之间没有简单判界。单例观察既不足以宣布模型缺少创造力，也不足以认为专家不再必要。
- **当前核验缺口**：六项成果链接未能访问；结果为待查的一手主张。本页 evidence_level=medium 支撑实践观察，不提升未验证数学结果的证据等级。

### 3. 对标

| 关联知识 | 可迁移判断 | 候选验证 |
|---|---|---|
| [[AI-in-Mathematics]] | 开放研究的局部改进不等于解决原猜想 | 明确原问题、改进命题、范围及独立检查结果 |
| [[Grindability-vs-Verifiability]] | 搜索可并行与验收可自动化之外，还需识别方法上限 | 固定成本预算，对照继续搜索与换路线的真实收益 |
| [[Research-Taste]] | 问题选择与退出策略是不同于执行吞吐量的能力 | 记录候选路径、失败原因、预计上限、停止决策与后续结果 |
| [[Conceptual-Breakthroughs]] | 重新组合已有工具不必等同于发明新概念 | 文献比对、独立专家审查、概念层和证明层分开 |
| [[Verifiable-Agent-Engineering]] | 形式证明及大规模计算结果仍需要独立 Oracle、边界和可重放证据 | 检查定理陈述、公理与依赖、覆盖、checker 版本、独立复核 |
| [[Meta-Harness-Optimization]] | 内层任务推进和外层方法选择分离，不等于已经实现递归自改进 | 在固定资源下比较路线评估/切换策略，保留基线和独立评测 |

对 LLM WiKi：外部突破应推动证据依赖复查，而不是无差别重编译。对研究 Worker：将可验证的候选结论、路线失败记录及停止原因作为输出；只有独立验证通过的知识才能升级。任务预算和终止状态由确定性控制面管理。本次仅为知识对标，不代表已修改生产系统或执行独立实验。

## 前提与局限性

本页是个人回顾的证据地图；原文章可从 canonical URL 回查，公开数学成果的发布页本次读取失败，待有独立验证再升级。未保存版权全文。`original_body_sha256` 对应临时来源登记摘录正文，不是原网页全文哈希。

## 关联概念

- [[AI-in-Mathematics]]
- [[Grindability-vs-Verifiability]]
- [[Research-Taste]]
- [[Conceptual-Breakthroughs]]
- [[Verifiable-Agent-Engineering]]
- [[Meta-Harness-Optimization]]
