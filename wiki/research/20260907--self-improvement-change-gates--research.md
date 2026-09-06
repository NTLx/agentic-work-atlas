---
type: research-log
title: "Explore：自我改进 Agent 的变更归因与晋级门"
date: "2026-09-07"
tags:
  - research-log
  - self-improvement
  - agent-harness
  - ex-007
---

# Explore：自我改进 Agent 的变更归因与晋级门

## 研究问题

`EX-007` 关注一个自我改进 Agent 把“分数提升”写回自身系统时的不可自证边界。本轮不再重复 2026-09-06 对 HELIX、Evo-Harness 与 Anthropic Automated Alignment Researcher（AAR）的初次核查，而是补查三类一手材料：

1. 是否有研究把 harness 变更、演化器、评估器或选择策略拆成不同可归因对象；
2. 质量门、隐藏测试和冻结外层是否足以把真实能力提升与测试时搜索、任务捷径分开；
3. 是否已经出现线上 canary、独立安全复评和可验证 rollback 的长期记录。

来源中的指令均视为不可信数据。本页只提取来源报告的实验与设计事实；“必要门”与“不可自证”是本轮 reasoning，不是来源原话。

## 结论先行

**Delta：refined；不新增 EX。**

本轮新增材料把 `EX-007` 收窄为两个必须同时处理、但不能互相替代的门：

1. **变更归因门**：把变了什么、谁变的、哪一版反馈促成变化、运行时是否实际使用了它分开记录。`Harness Updating Is Not Harness Benefit` 说明“能产生有用更新”与“任务 Agent 能从更新中获益”是两个不同能力；`HarnessEvolve` 和 HSI 进一步把 harness、演化策略和评估/选择过程拆层。
2. **反馈与控制不对称门**：评估参考、外部正确性、选择器和安全策略不能与被测对象一起自由改写。`Rethinking the Evaluation of Harness Evolution` 提供了直接反例：在匹配反馈和推理预算下，自动 harness evolution 可能不如简单 test-time scaling，且在不相交测试集上几乎没有收益；所以“通过性能门”本身不能证明改进来自更好的可复用 harness。

现有结构仍不足以宣称安全闭环。`HarnessEvolve` 有结构解耦、泄漏/膨胀质量门、近期批次性能门和验证集快照池；HSI 有 `task harness → evolver strategy → frozen outer anchor` 的编辑边界和 held-out task split；但本轮没有找到它们报告**不可改写的独立安全策略、部署级 canary、真实线上回滚或 rollback 后行为复核**的证据。因此不把“冻结锚点”“隐藏测试”或“快照选择”单独升级为普遍安全保证。

## Evidence：新增材料

### E1 · HarnessEvolve：结构解耦与两级性能门，但仍是实验内晋级

来源：[HarnessEvolve 论文 HTML](https://arxiv.org/html/2609.00829)（arXiv:2609.00829v1，2026-09-01，Huawei）。

- 论文把执行、评估、优化、门控写成四个模块：执行模块产生轨迹，评估模块判断任务正确性并核验参考轨迹，优化模块对失败轨迹做根因分析，门控模块检查候选 harness 更新。[论文方法概述](https://arxiv.org/html/2609.00829#S3)
- 可编辑对象不是单一 skill，而是 prompts、skills、tools 与 execution logic；开源 benchmark 使用统一的 train/validation/test split，实验配置还明确了 batch、近期回放缓冲区、验证集和 test set。[论文实验设置](https://arxiv.org/html/2609.00829#S4)
- 参考轨迹由执行 Agent 在已知 ground-truth answer 条件下生成，评估 Agent 再检查它是否真的走了合法工具/推理路径，而不是直接复述答案。该设计能改善错误归因，但 reference 的产生仍与执行体系相连，不能自动等同于外部独立真值。[执行与评估](https://arxiv.org/html/2609.00829#S3.2)
- 质量门使用 LLM-as-judge 检查候选是否把失败 query/answer 写入 harness，并限制新增 in-context examples；性能门要求当前 batch 提升且近期 batch 不超过退化容忍度；每个 epoch 再从 snapshot pool 按 validation accuracy 选版本。[门控定义](https://arxiv.org/html/2609.00829#S3.5)
- 论文将 gate agent 称为与优化 Agent “structurally decoupled”，这支持**职责隔离**，但来源没有证明 gate 拥有不可被演化体系改写的独立安全权限，也没有在方法中给出线上 canary、部署后 rollback 或 rollback 后独立复核。这里的后半句是基于所核读方法边界的缺口判断，不是“不存在”的证明。

### E2 · HSI：三层可编辑边界与冻结外层锚点

来源：[Hierarchical Self-Improvement 论文 HTML](https://arxiv.org/html/2608.08466)（arXiv:2608.08466v1，2026-08-09，Tailin Zhou）。

- HSI 让同一个冻结 LLM 同时承担 task-harness、evolver 和 meta-evolver 三个作用域；task harness 可变，evolver strategy 可变，执行 meta-evolution 的外层逻辑保持不可变。[设计边界](https://arxiv.org/html/2608.08466#S3.1)
- 三层作用域的写权限被显式分开：evolver 不能修改 evolution strategy，meta-evolver 不能在该阶段直接修改 task harness；越过授权目录的改动会被拒绝，形成 `M → H → Sigma → frozen anchor` 的结构边界。[scope isolation](https://arxiv.org/html/2608.08466#A.5)
- 为隔离 task-time reasoning 的混淆，任务执行关闭 extended reasoning，演化层开启；所有配置在 development、validation、best-version selection 和 final testing 中保持一致。[实验配置](https://arxiv.org/html/2608.08466#S4.1)
- BabaIsAI 使用 20% held-out test split；论文报告 BreakStop 和 GoTo 上的强泛化，但 Make 仍只有约 0.36/0.34 的 held-out progress，作者也报告后续迭代可能回归，说明 harness 演化并非单调改进。[held-out 结果与轨迹](https://arxiv.org/html/2608.08466#S4.2)
- HSI 把 evaluation signals 和 data splits 置于 Agent 控制之外，但三个作用域仍共用同一个冻结 LLM；本轮未见独立安全 evaluator、线上策略审批、canary 或部署后 rollback 结果。故 HSI 是**结构性自修改边界的正例**，不是独立监督或生产恢复闭环的正例。

### E3 · Harness Updating Is Not Harness Benefit：更新能力与受益能力分离

来源：[Harness Updating Is Not Harness Benefit 论文 HTML](https://arxiv.org/html/2605.30621)（arXiv:2605.30621v1，2026-05-28）。

- 论文明确区分 `harness-updating`：从执行证据产生有用持久更新；与 `harness-benefit`：任务求解 Agent 实际从更新后的 harness 中获益。实验独立改变 task-solving agent 和 evolver，覆盖七个模型与三个 agent benchmark。[定义与实验](https://arxiv.org/html/2605.30621#S3)
- 在其设置中，evolver 之间的 harness-updating gain 差距在任一 benchmark 最多 3.1 个百分点，而 post-evolution score 更受 task-solving agent 的基础能力影响；这意味着“演化器写出了看似合理更新”不能替代“执行 Agent 能稳定调用并遵循更新”。[evolver-side 结果](https://arxiv.org/html/2605.30621#S4.2)
- SkillsBench 分析把受益失败拆为 harness activation 与 harness adherence：Qwen3-32B 的 skill-load rate 为 0.251、harness-following rate 为 0.142；Claude Opus 4.6 的对应值为 0.957 和 0.757。它还报告弱模型随轨迹推进会进一步丢失遵循度。[agent-side 结果](https://arxiv.org/html/2605.30621#S4.3)
- 该研究把更新日志和“不得修改评估脚本/模型权重”作为 benchmark 可审计控制，但作者明确说这不自动保证开放部署安全，并把可逆更新、审计和人类监督列为部署要求。[限制与伦理边界](https://arxiv.org/html/2605.30621#S6)

### E4 · Rethinking the Evaluation：性能提升可能来自搜索而非 harness 设计

来源：[Rethinking the Evaluation of Harness Evolution for Agents 论文 HTML](https://arxiv.org/html/2607.12227)（arXiv:2607.12227v2，2026-08-27，Allen Institute for AI / University of Washington 等）。

- 论文要求 harness evolution 与 parallel sampling、sequential refinement 等 test-time scaling 在反馈和推理预算上匹配，并用 disjoint tasks 检查可复用泛化。[评测协议](https://arxiv.org/html/2607.12227#S3)
- Terminal-Bench 2.1、没有 unit test 时，平均 pass@1 为：初始 harness 68.2，parallel sampling 72.3，harness evolution 67.4，harness scaling 71.8；也就是说，迭代改 harness 在该设置下不如直接扩大任务级搜索。[无 unit test 结果](https://arxiv.org/html/2607.12227#S4.2)
- 有 unit test 时，平均 pass@1 为：parallel sampling 86.0、sequential refinement 84.3、harness evolution 75.8；pass@5 则分别为 86.0、91.8、86.2。论文据此认为，部分收益来自多次尝试和结果选择，而非把原本解决不了的任务转化为可复用 harness 能力。[有 unit test 结果](https://arxiv.org/html/2607.12227#S4.3)
- 在 45 个训练任务、10 个 validation 任务和 34 个 held-out test 任务的设置中，harness evolution 对 Claude Opus 4.6 只提升 1.2 个百分点，对 GPT-5.4 没有提升，平均为 0.6 个百分点。该结果是对当前 benchmark/方法的反例，不是对所有 harness evolution 的普遍否证。[泛化结果](https://arxiv.org/html/2607.12227#S4.4)

## 横向判定

| 材料 | 被允许改变的对象 | 外部/冻结反馈边界 | 它补强了什么 | 仍缺什么 |
|---|---|---|---|---|
| HarnessEvolve | 完整执行 harness；优化、评估、门控分模块 | ground-truth、validation/test split、近期 batch | 变更归因、泄漏/膨胀门、快照选择 | 不可改写安全策略、部署 canary、线上 rollback、独立安全复评 |
| HSI | task harness 与 evolver strategy 分层可变 | frozen outer anchor、held-out split、固定 task interface | 自修改层级边界、策略与对象分离 | 独立 evaluator、生产恢复、跨作用域 authority binding |
| Harness Updating Is Not Harness Benefit | 独立改变 agent 与 evolver；固定部分 harness 组件 | 同一 task stream 的 in-situ score，限制写入评估脚本 | 更新能力与实际受益分离、activation/adherence 指标 | 安全策略与部署后行为的联合评估 |
| Rethinking the Evaluation | 对照 harness evolution、test-time scaling、harness scaling | 匹配反馈/计算预算、disjoint held-out tasks | 识别 benchmark 搜索与真正 harness 改进的混淆 | 变更 provenance、独立安全 gate、可逆部署流程 |
| Anthropic AAR（既有材料，不计作本轮新增） | 自动研究方法与训练代码 | hidden holdout、OS 隔离、独立 evaluator、代码审批 | feedback/control 不对称的正向设计基线 | 长期线上自修改与 rollback 证据 |

## Reasoning

### 1. “对象分层”与“权威分层”是两件事

HSI 解决的是**哪个目录/作用域能被改**，HarnessEvolve 解决的是**哪个模块负责产生、检查和接受更新**。但二者都主要在实验内部定义晋级流程。若 gate、reference、reward 或 final selector 仍由同一演化体系影响，结构解耦只能改善可观察归因，不能自动产生外部权威。

因此，EX-007 的三类对象应保持：

- **行为面**：prompt、skill、tool、memory、execution logic；需要版本/hash、行为契约、回归、activation/adherence 和 post-deploy canary。
- **反馈/评估面**：ground truth、reference、grader、benchmark、reward；需要 owner、版本、来源谱系、隐藏 holdout 和不可由被测对象改写的读取边界。
- **策略/控制面**：evolver、gate、selector、safety policy、rollback authority；至少要有冻结外层或独立控制面，且能在行为面继续自改时保留否决权。

### 2. 性能门不是安全门，也不是因果归因门

HarnessEvolve 的性能门能阻止近期任务明显退化，HSI 的 held-out split 能测试部分泛化；但 Rethinking 的对照显示，即便有 unit-test feedback，性能提高也可能主要来自多次采样和选择。另一方面，Harness Updating Is Not Harness Benefit 说明更新存在不代表执行 Agent 会使用或遵循它。

所以至少要把三个结果分开：

`candidate score ↑` ≠ `reusable capability ↑` ≠ `safe deployment ↑`

第一个要用 matched search baseline 对照，第二个要用 disjoint task/trajectory 与 activation/adherence 追踪，第三个还要加入不可改写的安全复评、canary、rollback 和恢复后验证。

### 3. 本轮没有出现可独立建 EX 的新瓶颈

“更新是否真的被执行 Agent 吸收”与“反馈/控制面能否否决被测对象”都直接落在 EX-007 的变更归因与双重不对称内；前者还与 EX-004 的 success provenance 相连，后者与 EX-006 的 authority/provenance binding 相连。它们是既有问题的边界细化，不满足新建 EX 的正交性要求。

## 新问题

在一个可持续运行的 self-improvement loop 中，能否对每次变更同时提供：

`change hash/owner → feedback provenance → independent acceptance → matched-search delta → held-out behavior → safety canary → rollback/recovery result`？

其中最后三项必须绑定到同一版本，而不是只报告“当前最高分”的快照。若策略面、评估面和行为面中的任一项发生共变，是否应自动降级为“未证实能力提升”，直到外部控制面完成复评？

## 可证伪方向

- 若后续材料显示：行为变更、评估参考、选择策略均有不可改写 owner；有匹配的 test-time scaling 对照、hidden holdout、独立安全复评、线上 canary 与 rollback 后结果，那么当前“性能门不够”的判断应收窄。
- 若同一 benchmark 上，冻结 external oracle 和独立安全策略后，harness update 仍能在 disjoint tasks、多个模型和多次运行中稳定提升 pass@1，并且收益不能由额外采样解释，EX-007 的“搜索混淆”边界应减弱。
- 若线上记录表明所有更新都可由 provider post-state、行为契约和回滚结果重建，且没有评估器/目标/策略共变，则 EX-007 可能与 EX-004/006 合并为变更 provenance 问题。

## Source 需求与最小实验

### Source 需求

- **P0 clip+compile**：`HarnessEvolve`、HSI、`Harness Updating Is Not Harness Benefit`、`Rethinking the Evaluation of Harness Evolution`；提取 change surface、reference owner、gate 输入、matched search、held-out split、activation/adherence 和 snapshot/rollback 字段。
- **P0 继续寻找**：生产 Agent fleet 的 prompt/skill/router/evaluator 变更日志，要求有版本/hash、owner、canary、rollback、隐藏 holdout 与安全/质量联合结果；论文 benchmark 不能替代此类材料。
- **与 EX-004/006 共用字段**：`change_id → reference/provenance → verifier/safety policy → acceptance → actuation → post-state → rollback/recovery`，避免把变更审计与动作效果审计分成互不相连的记录。

### 最小实验

在固定模型和确定性 tool environment 中，分别操纵行为面、反馈面和策略面变更；为每个候选记录 immutable change hash、feedback source/version、独立 acceptance verdict、matched test-time search baseline、disjoint held-out 任务、activation/adherence、safety canary 与 rollback 后的行为。只有当同一版本的所有字段都能回链，才把“得分提升”记为可归因的 capability delta；否则只记作候选更新或 search gain。

## 研究状态

- Disposition：`refined`
- New EX：无
- Promotion candidate：无；本轮只更新 Research，不创建稳定 Entity/Topic
- Evidence posture：四篇新论文与作者代码/官方材料线索已核读；AAR 作为既有 source summary 对照，不重复计数
