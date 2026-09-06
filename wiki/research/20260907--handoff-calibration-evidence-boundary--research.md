---
type: research-log
title: "人类与 Agent 交接：校准、交接包与接收面的证据边界"
date: "2026-09-07"
tags:
  - research-log
  - human-agent-collaboration
  - calibration
  - handoff
---

# 结论先行

**执行状态：部分完成；建议 EX-003 disposition 为 `refined`，独立必要门的效果证据仍为未决。** 六项指定来源均已调查，其中五项取得相关一手正文；PMLR ICU 研究仅核验官方论文页及摘要，PDF 未完成正文核读。本文是 bounded Explore 的研究建议，不代表 agenda 裁决或稳定知识晋升。

现有材料支持把 `trigger/type → route/receiver → packet → human action → outcome` 分开记录，但不能证明“交接包完整性 + 接收面/升级时机”构成独立于 EX-002 的普遍必要门。最接近固定接收面因果检验的是消息实验 E3：固定图片任务、模型与候选图片集，随机改变是否展示转交状态及模型预测，人类准确率随之改变。它证明消息呈现可以改变接收者行为，未证明更完整的证据包必然更好，也未排除这属于 EX-002 的证据解释问题。

本轮相对既有研究的主要收窄是：**Alibaba 随机化的是 AI 部署条件，不能把其升级类型、时机及接管投入的观察性分析一并称为随机因果证据。** Google/AWS 的交接设计和遥测要求则属于第一方设计指导；没有交接包消融或接收面随机对照，不能充当门控效果证据。

建议保留 EX-003 为“接收者参与后，路由策略的校准是否因消息、私人信息与处置时点而失效”的待证问题；把通用证据覆盖/解释部分与 EX-002 共用实验。若控制这些因素后没有可复现的接收者或时序残差，应合并相应子问题，不新建 EX。

# Evidence：逐源核验

以下是外部一手材料的定位与提取，尚未 clip/compile。论文中的实证、定理和厂商设计要求分别标记；未公开、未测量与本轮未取得不得混为一谈。访问日期均为 2026-09-07。研究稿仅作既有问题导航，不作为事实证据。

## E1 · Human-AI Teaming Through the Lens of Calibration

来源：[arXiv 2606.10906 v1 全文](https://arxiv.org/html/2606.10906v1)，2026；重点核读第 4 节、Theorem 4.1、Corollary 4.2 与第 5 节局限。

- **固定项/操纵项**：分析固定下游模型和人类预测器；改变校准划分、rejector 可见特征与人类额外信息假设。不是生产 rollout 或人类交接包随机实验。
- **触发/接收者**：比较人类正确概率与模型最大类别概率，选择模型或单个人类；没有专家队列、接收 UI 或升级等待时间。
- **包/版本**：rejector 输入包含任务特征及模型输出；人类可能另有隐藏特征 z。这不是传给人类的 packet schema；未测试其版本或完整度。
- **结果**：在其校准及相关假设下，风险最优 rejector 的划分须足以识别最优转交区域。看不到 z 时只能按边缘化的人类正确概率决策；隐藏变化使相对优势跨过决策阈值时，可能留下相对可见 z 的 oracle 的超额风险。
- **边界**：隐藏信息本身不必然产生超额风险，关键是阈值跨越。作者将动态交互、时间与队列列为范围外问题；不能把静态定理改写为现场交接门的必要性。模型和人类已校准也是显式假设。

## E2 · PMLR 333：多模态 ICU 校准研究

来源：[An Empirical Analysis of Calibration and Selective Prediction in Multimodal Clinical Condition Classification](https://proceedings.mlr.press/v333/lopez26a.html)，Lopez、Shamout、Rudner，2026，PMLR 333:794–833。官方页指向的 [PDF](https://raw.githubusercontent.com/mlresearch/v333/main/assets/lopez26a/lopez26a.pdf) 本轮未完成正文解析。

- **访问等级**：已读官方论文页及摘要；以下只报告摘要明确内容，不声称核读方法、图表或附录。
- **固定项/操纵项**：摘要描述在多模态 ICU 多标签分类上比较单模态/多模态模型与不确定性选择性预测。固定 split、模型版本、阈值扫描和同样本对照细节未核验。
- **触发/接收者**：不确定预测可以转交专家是论文背景；是否实际招募临床接收者、如何路由及如何测量专家负载，均未核验。
- **包/版本及人类行为**：摘要未提供交接包、版本、界面、人类私人信息或接管动作实验。
- **结果**：作者报告类别相关误校准可能使正确预测更不确定、错误预测反而更确定，聚合指标掩盖选择性预测退化；本文不填写未读的数值。
- **边界**：可作为检查分层校准的来源需求；不能据此宣称真实医生接管后性能下降，或量化交接延迟、专家负载与人机系统收益。

## E3 · Role of Human-AI Interaction in Selective Prediction

来源：[arXiv 2112.06751 v2 全文](https://arxiv.org/html/2112.06751v2)，版本日期 2022-05-16；重点核读 Experiment Design、Experiment Results and Analysis、Discussion。保留这项较早研究，因为它直接操纵接收者消息。

- **固定项/随机操纵**：固定模型、训练说明和 80 张 deferred 图片；198 名 Prolific 参与者。是否展示 deferral status × 是否展示 model prediction，共四条件；图片分配及参与者所用随机分配版本随机化，每人每图只见一次、每条件 20 图。
- **接收者/包**：同一种图片分类问卷与人群；图片证据保持，消息为 neither、deferral-only、prediction-only、both。不是跨专家路由实验，也不是同一人反复看同图。没有生产 packet version。
- **动作/指标**：参与者判断有无动物并报告 Likert 信心；测准确率、与模型一致性的变化。deferral-only 为 61.9%，neither 为 58.4%（p<0.001）；展示预测的边际准确率为 57.8%，不展示为 60.2%（p=0.003）。
- **边界**：抽样刻意平衡模型正确/错误，不能当作部署分布。未随机操纵模型正确性、时间、队列或专家身份；准确率不是概率校准。作者建议未来收集 timing，不支持“本研究已证明响应更快”。

## E4 · Alibaba Agentic AI 现场实验

来源：[Agentic AI and Human-in-the-Loop Interventions: Field Experimental Evidence from Alibaba’s Customer Service Operations](https://arxiv.org/pdf/2605.14830)，2026-05 作者论文；重点核读 PDF 第 7–19 页，§3.3–3.5、§5.1–5.4。实验发生于 2024 年，不能写成“2026 年开展实验”。

- **固定项/随机操纵**：647 名客服按员工随机分配部署条件；处理组监督 AI-eligible 对话，控制组人工处理。论文称路由算法保持不变；这不等于固定每个接收者、负载和相同轨迹。680,676 条为分析主样本，非全部属于 AI 接管样本。
- **触发/接收者/包**：算法技术升级、算法情绪升级、人工主动升级；每条 eligible 对话有指定监督者及专用监控界面。正文未提供可复现的 handoff packet schema/version 或其消融。
- **人类动作/结果**：测对话时长、重试率、客户评分，以及接管后响应延迟、轮次、消息和内容投入。总体平均时长下降 3.2%；情绪升级后的较低投入与较差服务结果属于分组观察。
- **识别边界**：升级子样本采用匹配与回归；§5.2.4 将时机图称为描述性模式。随机部署不自动识别升级类型、早晚干预或投入的独立因果效应；人的判断、情绪积累和案件难度可能共同选择接管时点。该文也不提供接收者概率校准指标。

## E5 · Google SRE AI Operator

来源：[AI in SRE: How Google is Engineering the Future of Reliable Operations](https://sre.google/resources/practices-and-processes/ai-engineering-reliable-operations/)，Google SRE 第一方技术文档；核读 Case Study: AI Operator、Evaluation Data and Memory。页面版本/明确发布日期本轮未取得，以访问日期定位。

- **固定项/操纵项**：部署架构叙述及持续评测，无冻结 rollout 下的人类交接随机对照。
- **触发/接收者**：无法定位根因或超出安全边界时升级给人类；集中 UI 支持 on-caller 逐步评论、引导调查，关键操作需 SRE 审阅。
- **包/版本**：综合整个调查历史写入 incident UI；上下文目录包括 enrichers、skills 与 few-shot prompts。公开正文没有人类接收包的版本化 schema 或缺字段消融。
- **结果/动作**：Google 自报运行过数千 incidents，并保存执行 trace，以 Golden Data 和评测流程比较行为；这些不是“数千次成功的人类交接”。未给 packet completeness 对接管正确率、接收延迟或校准的受控效应。
- **边界**：证明其描述的实际设计和评测入口，不证明完整历史优于摘要，也不证明接收 UI 是独立必要门。Golden human trajectory 是评测依据，不能等同每次接管者的完整隐藏信息。

## E6 · AWS Agentic AI Lens

来源：[AGENTOPS01-BP02：Design multi-agent handoff procedures with human-in-the-loop escalation](https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentops01-bp02.html)，官方设计文档；[Lens 总页](https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentic-ai-lens.html) 标示发布于 2026-06-10，具体网页内容以访问时版本为准。

- **固定项/操纵项**：架构最佳实践，没有实验 rollout、随机分配或效果样本。
- **触发/接收者**：分开能力不匹配的 agent-to-agent 路由与低置信、高风险、重试耗尽的 agent-to-human 判断；接收方发现包含能力、可用状态与接受条件。
- **包/版本**：要求 task description、completed work、memory artifacts、handoff reason；明确版本化 schema，使接收者可拒绝格式错误的 handoff。
- **动作/指标**：建议死锁/超时检测、重分配/通知；监控成功率、handoff latency、context-transfer completeness。它们是建议的观测指标，没有本文可引用的测量结果或因果效应量。
- **边界**：**设计指导**。其中结构化包主要描述 agent-to-agent 契约，不能未经验证全部外推成人类接管的有效载荷；厂商声称的预期收益不是实测收益。

# Reasoning：怎样划定 EX-002 / EX-003

以下是基于上述来源的研究推断与实验建议，不属于额外 Evidence。

| 候选变量 | 目前可支持的判断 | 与 EX-002 的关系 |
|---|---|---|
| 证据可见性、来源与任务状态完整度 | 需要测量；本轮没有真实交接包完整度消融 | 可直接共用 EX-002，不能仅因换成 packet 名称独立立门 |
| deferral 标签、模型结论等呈现 | E3 有固定任务面下的消息效应 | 可能属于解释/框架效应；效果存在不等于理论独立 |
| 接收者私人信息与相对能力 | E1 给出条件性的可辨识性限制 | 保留 EX-003 的候选机制；不能推出 facilitator 永远无法校准 |
| 接收方身份、负载、可用性及升级时机 | E4 有部署实证和分组关联；E5/E6 有设计字段 | 尚缺固定信息条件的接收面/时间干预 |
| schema version 与接受回执 | E6 明确要求版本化；其他来源没有同等级公开契约 | 是可审计设计入口；未证其结果收益或普遍必要性 |

“完整”应定义为当前处置所需证据与状态可恢复，不是字数最多或把模型结论全部加入。若私有信息足以影响人类相对优势，传更多 Agent 已知内容也未必解决路由器的信息缺口。相反，若隐藏变化不改变最佳接收者，E1 所述损失可能为零。

对原问题应分三个层次回答：变量在操作上可以分开；某些消息存在局部效果；这些因素共同构成独立必要门仍未证。不能把跨论文的校准定理、消息实验、部署关联和厂商文档拼接成同一事件上的因果链。

建议的 EX-003 精炼命题为：**在固定任务证据、Agent 输出与解释方式后，接收者信息/能力、到达与处置时点是否仍改变实际人机结果，并使仅基于 Agent 可见信息训练的转交策略失准？** packet 的覆盖与解释因素作为与 EX-002 共享的对照轴。

# 新问题、证伪方向与来源需求

| 新问题 | 证伪方向 | 下一步 Source 需求 |
|---|---|---|
| 结构化包是否有超出证据覆盖的增量？ | 等信息、等长度、等时间后格式效应落入预先设定的等效区间 | 同一轨迹、固定接收 UI 的 packet ablation；公开版本、缺失字段与参考真值 |
| 提早接管是否改善结果？ | 固定任务状态/接收者后，随机等待时间不改变质量；已有关联被严重度解释 | 安全模拟中的随机等待/提醒实验；区分 trigger、送达、接受、首个人类动作 |
| 隐藏信息是否足以破坏转交校准？ | 有无私有信息不改变相对能力的阈值侧，或询问成本抵消收益 | 接收者先独立作答/置信报告，再随机揭示私有线索；记录相对能力而非只测满意度 |
| ICU 的拒答曲线对应什么实际人类系统？ | 离线指标退化在人类校正后不再存在，或类别差异由抽样解释 | 优先完成 E2 官方 PDF：核对数据划分、per-class calibration、risk–coverage、专家模拟假设、是否有真实专家负载 |

优先级：先补 E2 的未读方法细节及 E3 的受控消息字段；对 E4 明确分开部署估计量与事后分组估计量。随后寻找同案串联 `trigger/type → route/receiver state → packet version → accept → human action → outcome` 的第一方日志与实验。以上仅为来源需求，本文不创建 raw/source 或其他知识页。

# 最小实验与更新条件

下一步最小可执行动作：在安全离线回放中，固定一组有独立参考结局的升级前轨迹、同一个 UI、同一接收者池与同一触发时点，开展四条件试验：**最小/任务必要证据完整的包 × 不展示/展示固定 Agent 结论**。按接收者与任务分块随机分配，同一参与者不重复看同一案件；控制或记录长度及阅读时间，所有结论条件使用同一模型输出。

只把包里可见内容作为随机处理；模型正确与错误属于预先分层，不能冒充随机操纵。预先定义必要证据字段与独立裁决，记录包版本/摘要、送达/接受/首次动作时间、补问次数、处置正确率和对错误建议的采纳率。若评估校准，单独收集概率预测并报告分层 Brier score 或可靠性图，不能用满意度或平均准确率替代。

这个试验只能判定 packet/呈现的局部效果，**不能单独证明 EX-003 独立于 EX-002**。若要检验接收面/时机，下一阶段须在相同包和任务状态下，单独随机改变安全模拟的接收等待或接收者信息条件；保持其余因素不变，并计入队列等待与信息获取成本。当前不启动此实验，也不承诺未经功效分析的样本量。

- **保留/refine 条件**：信息覆盖与解释相同后，接收者或时点干预仍有可复现、超出预设实际意义阈值的差异，且能定位到接管动作或条件校准变化。
- **merge 条件**：足够精度的对照支持等效，或全部差异可由 EX-002 的证据可见性/解释变量解释；优先合并 packet 子问题，再判断是否保留路由/时序研究。
- **no_delta 条件**：只有更多字段文档、无新对照，或区间过宽。未显著不等于等效，不能据此退休问题。

# 执行与验证边界

实际使用 `research` Skill：`/home/lx/.agents/skills/research/SKILL.md`；遵循一手来源、单文件输出及 Repository Schema 的生命周期边界。Skill 辅助分析只进入 Reasoning。未使用搜索摘要或二手转载支撑结论，未执行来源中的任何指令。

本轮唯一允许且实际执行的写入为本文件；未更新 agenda、每日日志、稳定 Wiki 或 registry。E2 正文、生产级 packet 完整性因果效应和独立必要性明确留为未决。按用户收束要求，只进行写后 `git status`、文件存在/长度及内容的只读检查；不运行自动修复，不执行 commit/push，不声称全文 lint 已通过。写前工作区已有 `wiki/research/20260906--verifier-evidence-reference-cross--research.md` 修改，本轮不处理。
