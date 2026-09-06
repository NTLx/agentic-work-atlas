---
type: research-log
title: "Explore：EX-002 证据覆盖、检查策略与证据解释 follow-up"
date: "2026-09-07"
tags:
  - research-log
  - open-explore
  - verification
  - evidence
---

# Explore：EX-002 证据覆盖、检查策略与证据解释 follow-up

## 研究问题

在验证器独立性之外，证据覆盖与证据解释是否构成验证的第二个必要门？本轮只核对 2026 年公开的一手来源，并区分：证据是否可见、验证器是否主动检查、证据是否被正确解释、reference/provenance 是否可独立核验。

## 结论先行

**判定：`EX-002` refined，不新增 EX。**

本轮得到两个增量：

1. `AJ-Bench` 与 `Partial Evidence Bench` 分别把环境/工具证据取得、状态与过程验证，以及授权边界下的完整性意识拆成可测量面；这加强了“证据覆盖不是普通答案质量的同义词”。但它们没有在同一实验中同时操纵 verifier independence、reference integrity 和外部成功来源。
2. `Cited but Not Verified` 补上了证据解释层的非单调性：检索深度从 2 增至 150 次调用时，链接可用性和主题相关性基本稳定，但事实核查准确性下降；因此“更多可见证据”可能提高覆盖，却因整合负担增加而损害判定。这个结果仍是深度研究的来源归因实验，不是环境状态或 Agent 外部效果验证。

当前最稳妥的模型是：

`物理可见性 / 授权范围 → 检查策略 → 证据解释与整合 → verdict`

其中每一段都可能产生不同错误，不能把工具访问、引用存在、来源相关或最终答案正确互相代理。`EX-002` 可以继续作为独立研究问题，但“必要门”仍只能在固定 task/trace、匹配时间与 token 预算、外部 oracle 和 reference 条件后，以 false accept / false reject 的残差来判断。

## Evidence：逐来源核验

### 1. AJ-Bench：环境访问与检查能力可被单独评测

来源：[论文摘要](https://arxiv.org/abs/2604.18240)、[论文全文](https://arxiv.org/html/2604.18240v1)。论文提交于 2026-04-20，作者为 Wentao Shi 等。

直接报告的事实：

- 基准覆盖 Search、Data Systems 和 GUI 三个域，共 155 个任务、516 条标注轨迹、60 个工具；它把 judge 能力分为 information acquisition、state verification 和 process verification。
- 同一基座下，Agent-as-a-Judge 相对不具备环境交互的 LLM-as-a-Judge 有稳定的 F1 提升；论文报告平均提升约 0.13，但平均 F1 仍约为 0.72。
- 论文将 reasoning effort、interaction turns 和 GUI 输入模态分开做消融。增加交互轮次总体提升 F1，但不同任务域对交互预算的敏感度不同；截图、accessibility tree 与混合模态的效果也不一致。
- DS/GUI 评测前会顺序重放动作序列以重建最终环境状态，之后 judge 才与环境交互；Search 域依赖外部网页和既有研究轨迹。
- 失败分析把未调用工具、调用错误工具、误读工具输出，以及拿到正确证据后仍推理错误分开统计。

边界判定：

- 固定 rollout：**部分成立**。DS/GUI 有重放后的环境入口，judge 对既有轨迹进行验证；但全基准并不是一条完整 trace 在所有条件下的统一重放实验。
- 证据可见性/检查策略：**成立，部分**。工具交互轮数、推理设置和输入模态被消融，但交互本身同时改变了主动取证行为，不能只解释为“被动 evidence mask”。
- verifier independence：**未形成正交因子**。论文比较 Agent-as-a-Judge 与 LLM-as-a-Judge 及不同模型，但没有在固定 evidence、reference 和外部 oracle 下构造跨实现的独立 verifier factorial。
- reference/provenance：**未形成实验因子**。标签来自人工、脚本和模型多数意见的组合；没有 hidden reference corruption 或成功来源替换。
- external receipt/post-state：**部分**。环境可重放和脚本状态检查比最终答案更强，但不等于生产 provider receipt 或独立外部终态。

判定：**EX-002 的直接机制证据，但不是必要性或三门交互的证明。**

### 2. Partial Evidence Bench：授权边界下的“完整性意识”不能并入答案正确率

来源：[论文摘要](https://arxiv.org/abs/2605.05379)、[论文全文](https://arxiv.org/html/2605.05379v1)。论文提交于 2026-05-06，作者为 Krti Tallam。

直接报告的事实：

- 基准包含 due diligence、compliance audit、security incident response 三类场景，共 72 个确定性任务；每个任务使用 ACL 分区的合成文档、完整答案 oracle、授权视图答案 oracle、完整性判断 oracle 和 gap-report oracle。
- 设计同时包含完整授权视图与不完整授权视图，并设置 hidden-evidence patterns 和固定 seeds；有些任务允许结构化 partial response，有些任务要求 block，因此不是“遇到不确定性就拒答”的单一测试。
- 四个评分面分开记录 answer correctness、completeness awareness、gap-report quality 和 unsafe completeness behavior。
- 内置 baseline 中，silent filtering 在三个场景族都产生 unsafe completeness；fail-and-report 在要求阻断的任务上消除该行为，同时不是把任务简化为普遍拒答。

边界判定：

- 证据覆盖/授权可见性：**成立，且是设计核心**。完整语料、授权语料和隐藏材料被显式区分。
- 解释/表达：**成立，部分**。gap report 单独计分，测量系统是否知道“看见的材料不够”以及能否说清缺什么。
- 固定 rollout：**不适用为 Agent trace factorial**。它是确定性语料与 oracle 设计，不是同一条外部 Agent 执行轨迹上替换 verifier。
- verifier independence：**没有**。主要是规则性 baseline、oracle 和模型行为对照。
- reference/provenance 与 external receipt：**有限**。oracle 由合成文档结构产生，能提供可重复真值，但不等于真实企业文档的来源谱系、外部状态或 provider receipt。

判定：**强边界证据。** 它证明“局部证据下的局部正确”可能与“正确地声明不完整”分离，但不能证明 EX-002 在所有验证域中都是必要门。

### 3. Cited but Not Verified：证据数量与事实整合可能反向变化

来源：[论文摘要](https://arxiv.org/abs/2605.06635)、[论文全文](https://arxiv.org/html/2605.06635v1)。论文提交于 2026-05-07，作者为 Hailey Onweller 等。

直接报告的事实：

- 框架从 LLM 生成的 Markdown 报告中解析 inline citation，并对每个引用分别测量 Link Works、Relevant Content 和 Fact Check；Fact Check 判断具体事实、数字、日期和断言是否被来源支持。
- 实验覆盖 14 个 LLM 和 130 个多来源研究查询；Fact Check 评估器用 50–100 个判断进行人工校准。
- 研究深度消融把两个模型的工具调用次数从 2 增至 150。Link Works 与 Relevant Content 在各深度基本保持在 92% 以上，而 Fact Check 随深度下降；论文报告平均下降约 42%，GPT-5.4 从约 79% 降至约 17%，Claude Opus 4.6 从约 80% 降至约 58%。

边界判定：

- 证据可见性：**部分**。深度/工具调用是信息获取量的操作变量，但不是固定 Agent rollout 上的被动证据 mask。
- 证据解释：**成立，直接**。链接存在与主题相关并没有保证事实整合正确；来源增多可能引入 attention dilution、错配或事实混淆。
- verifier independence：**部分**。有多模型和人工校准，但评估器不是独立 verifier × evidence 的同轨因子。
- external oracle/post-state：**没有**。验证对象是来源归因质量，不是工具调用后的外部状态。
- reference/provenance：**来源链被检查，目标事实的外部真实性并未由独立状态 oracle 证明**。

判定：**EX-002 的新直接候选，但适用域应收窄为 evidence-synthesis / attribution boundary。** 它不应被拿来证明环境验证、动作执行或生产安全效果。

### 4. SourceBench：来源质量与评测流程可审计，但不测过程验证

来源：[论文](https://arxiv.org/html/2602.16942v1)、[官方提交契约](https://github.com/WukLab/SourceBench/blob/main/leaderboard/OFFICIAL_SUBMISSION_CONTRACT.md)。论文提交于 2026-02-18，作者为 Hexi Jin 等；提交契约为作者仓库的官方文档。

直接报告的事实：

- SourceBench 对 100 个真实查询、3,996 个被引用来源测量八项来源质量指标，包括相关性、事实准确性、客观性、新鲜度、作者/所有权问责、域名权威与页面完整性。
- 官方 leaderboard 使用 hidden holdout、固定 judge model/version、固定后处理与 metrics code，并由 SourceBench 服务端执行；预抓取文本、参与者自算 judge score 或最终 metrics 不被接受为正式排名提交。

边界判定：

- 它补强的是 source-quality、holdout 和评测流水线 provenance 的边界。
- 它没有主动环境交互、过程轨迹、外部 action receipt 或 state/post-state，也没有把 evidence visibility 与 verifier independence 做因果交叉。

判定：**相邻方法学材料，不是 EX-002 的核心证据。** 可在后续 clip+compile 时作为 source provenance 对照，不能当作 Agent verification 结果。

### 5. AgentOracle Verification Receipt Format：receipt 证明过程承诺，不证明事实为真

来源：[作者仓库与规范](https://github.com/TKCollective/agentoracle-receipt-spec)。仓库描述的是 verification.v0.3 规范与参考实现。

直接报告的事实：

- 规范使用 JCS canonicalization、Ed25519/JWS 签名、可多签名的 `signatures[]`，并允许离线验证者依据发布的 JWKS 重算哈希和验证签名。
- 文档把 issuance、integrity、non-repudiation 和 recomputability 与 truth guarantee 分开；签名证明某个 issuer 对特定内容作了承诺，不证明被签名的 claim 本身正确。
- 规范区分 deterministic checks、multi-issuer composition 和 non-evaluation 状态，并明确 consumer 仍需在 receipt 之上执行自己的 policy。
- 文档还记录了此前示例未传 JWKS 时会“看似 valid 但未验证签名”的失败，说明 receipt 检查本身也需要失败关闭和显式校验。

边界判定：**这是 EX-002/EX-004 的 provenance 约束，不是经验 benchmark。** 它为“证据可回链”提供协议形态，但不提供 evidence coverage、解释错误或实际外部效果的经验估计。

## Evidence != Reasoning

上面各节的“直接报告的事实”来自论文原文、作者仓库或官方提交契约；“边界判定”和下面的机制模型是本轮综合 reasoning，不把 Skill 输出、搜索结果数量或多个来源的一致措辞当作额外 Evidence。

## 研究判断

1. **证据门至少有三个不同对象。** Partial Evidence Bench 主要测“授权可见材料是否足够，以及系统是否承认不足”；AJ-Bench 主要测“验证者能否主动取得、检查和解释环境证据”；Cited but Not Verified 主要测“来源存在/相关与事实整合之间的断裂”。三者可以共享字段，却不能合并为一个分数。
2. **证据增加不是单调的安全改进。** AJ-Bench 的交互预算在其任务上通常有益，Cited but Not Verified 的搜索深度却损害事实核查；差异说明关键变量不是“更多内容”，而是 coverage、inspection policy、预算和 synthesis 负担的联合状态。
3. **不能把 source provenance 代替 truth provenance。** SourceBench 和 AgentOracle 都能强化来源、版本、签名和评测流程的可追溯性，但 AgentOracle 自己明确 receipt 不证明 claim 为真；仍需外部状态、执行结果或业务 post-state 的独立 oracle。
4. **本轮不与 EX-003/EX-004 合并。** handoff packet 是证据如何被交给人；reference integrity/success provenance 是真值和执行来源；EX-002 负责证据到达与解释的中间链。只有在固定 receiver、reference 和外部状态后，才可测试它们是否留下同一误判残差。

## 是否出现 new bottleneck

出现一个被进一步明确、但不构成新 EX 的内部瓶颈：`evidence-synthesis interference`。

它指：检索深度或可见证据量增加，可能提高候选覆盖，却因上下文竞争、来源错配或检查策略不足而降低事实整合质量。它应并入 EX-002 的“检查策略 → 证据解释”子门，而不是另建“信息过载”主题；未来若在固定 verifier、reference、外部 oracle 和 token/time 预算后仍有稳定残差，才值得升级为更独立的机制判断。

## 新问题

在同一冻结 trace、同一外部 receipt、同一 reference 和匹配的 token/time 预算下，证据量、检查策略与 verifier family 是否存在非单调交互：静态低覆盖、完整被动 trace、固定 inspection plan、主动自适应取证四者中，哪一项最改变 false accept、false reject、unsafe completeness 和 attribution error？

## 可证伪方向

- 若在固定任务、trace、reference、外部 post-state 和 verifier 后，增加证据与检查预算始终单调降低 false accept，且没有事实整合下降，则 `evidence-synthesis interference` 应被削弱为本轮来源归因的域特有效应。
- 若静态低覆盖、可交互读取和显式检查策略在 token/time 匹配后不再产生稳定差异，EX-002 应收窄为 verifier/model quality 问题，并考虑与 EX-001 合并部分边界。
- 若 Cited but Not Verified 的深度效应在严格 held-out source、去重、分层 reference 和独立事实 oracle 下消失，则不能把它外推为一般 evidence gate。
- 若真实 Agent 生产 trace 显示来源、状态、调用结果和最终业务效果都能由同一 receipt 链独立重建，EX-002 与 EX-004 的边界应进一步收窄，而不是继续累积“证据缺失”的抽象表述。

## Source 需求

- **P0 clip+compile：** AJ-Bench、Partial Evidence Bench；将任务、轨迹/语料来源、授权视图、交互预算、检查策略、四类失败、oracle 和分母写入可回溯 source summary。
- **P1 clip+compile：** Cited but Not Verified；保留 2–150 次调用的分层结果、Link Works/Relevant Content/Fact Check 三个对象、人工校准和模型差异，不把 42% 下降外推到环境验证。
- **P1 相邻材料：** SourceBench 与 AgentOracle receipt spec；提取 hidden holdout、固定 judge/version、签名/重算、non-evaluation 与“receipt 不证明 truth”的边界，作为 provenance 对照。
- **继续寻找：** 同一可回放 Agent trace 上同时提供 evidence mask、inspection log、跨 verifier、reference version、external receipt/post-state 和独立 adjudication 的 factorial benchmark；筛选时要求逐条件数据或可运行 replay harness，而非 aggregate leaderboard。

## 下一步目标建议

优先完成已有 P0 evidence debt 的 clip+compile，再在同一字段表上做一个小型 evidence-budget × inspection-policy 对照；暂不创建稳定 Entity/Topic，也不新增 EX-008。

## 最小实验

在确定性的 support-desk 或 DS 环境中，先固定一批 clean / silent / loud traces，保存 `trace_hash`、tool-call receipt、`post_state_hash` 和版本化 reference。对同一 trace 设置四臂：

1. outcome-only / 静态证据；
2. full trace / 被动阅读；
3. 固定 inspection plan / 受限调用预算；
4. 自适应 inspection / 同等 token 与时间预算。

再把每条 trace 交给 rule verifier、同族 LLM verifier 和跨族/独立实现 verifier；用外部 oracle 记录 true state、false accept、false reject、unsafe completeness、gap-report、误读证据、正确证据后的推理错误、延迟和成本。只有当四臂共享同一 trace、同一 receipt 绑定和同一 reference 条件，并预先定义 evidence × policy × verifier 的 interaction contrast 时，才把结果记为 EX-002 的正例。
