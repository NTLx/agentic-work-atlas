---
type: research-log
title: "研究日志 2026-09-06：Facilitator handoff calibration"
date: "2026-09-06"
tags:
  - research-log
  - ex-003
  - handoff
  - escalation
  - calibration
---

# 结论先行

本轮结论：**EX-003 refined，尚未解决；不新增 EX，不晋升稳定页。**

现有一手材料支持把三个变量分开记录：

1. **交接上下文（C）**：接收者看到哪些对话、摘要、证据、工具状态和路由理由；
2. **接收面可用性（A）**：目标人/队列是否在线、有容量、能否接收，以及等待和回退；
3. **升级路由（R）**：何时触发、选择哪个目标或队列、是否采用 fallback。

但它们目前只得到“可实现、应分别观测”的设计支持，没有得到同一实验中的因果分解。更重要的是，**完整交接包不等于监督闭包**：路由器可能看不到专家拥有的隐藏信息，接收者也可能看不到工具调用或运行时状态。因而 facilitator 可以被校准为一个受控路由器，却不能仅凭“全量会话已转交”证明没有新的监督盲区。

本轮不重复计入 2026-09-05 已检查的 Google SRE AI Operator、AWS Agentic AI Lens 和 Google Cloud escalation telemetry；新增证据来自当前的转接/编排文档及 2025–2026 作者论文。

# 来源清单

| 来源 | 日期/类型 | 对 EX-003 的作用 | 证据性质 |
|---|---|---|---|
| [Microsoft Agent Framework Handoff](https://learn.microsoft.com/en-us/agent-framework/workflows/orchestrations/handoff) | 2026-08-25 更新；官方编排文档 | 区分动态路由、上下文同步、工具审批和 checkpoint | 实现契约/设计指导 |
| [Microsoft Copilot Studio live-agent handoff](https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced-hand-off) | 2026-08-03 更新；官方产品文档 | 区分完整会话、私有 handoff message、路由变量和可用 agent | 实现契约/设计指导 |
| [Google Cloud virtual-agent transfers](https://docs.cloud.google.com/contact-center/ccai-platform/docs/virtual-agent-to-human-agent-transfers) | 2026-08-26 更新；官方产品文档 | 区分目标 agent、当前/备用队列、失败回退和 escalation reason | 实现契约/设计指导 |
| [AWS Connect chat transfer](https://docs.aws.amazon.com/connect/latest/adminguide/transfer-chats.html)、[agent-to-agent transfer](https://docs.aws.amazon.com/connect/latest/adminguide/setup-agent-to-agent-transfers.html)、[queue management](https://docs.aws.amazon.com/connect/latest/adminguide/queue-to-queue-transfer.html) | 2026-09-06 访问的 current 官方文档；页面未显示发布日期 | 分离 context preserved、目标/队列选择、队列状态、容量和接收完成 | 实现契约/设计指导 |
| [Human-AI Teaming Through the Lens of Calibration](https://arxiv.org/html/2606.10906) | 2026-06-09；作者论文 | 形式化 rejector 校准与人类隐藏信息造成的不可约风险 | 定理、模拟与人类预测实验 |
| [OpenL2D / FiFAR](https://www.nature.com/articles/s41597-025-04664-y) | 2025-04-23；作者 benchmark/data descriptor | 操纵专家工作容量和可用专家，观察分派算法排名变化 | benchmark；专家为合成数据 |
| [AI, Take the Wheel](https://arxiv.org/html/2605.28255) | 2026-05-27；作者论文 | 把“是否让 AI 自主行动”和“接收建议后是否采纳”分成两个决策 | 受控现场式实验；非 handoff/queue 实验 |
| [Alibaba Taobao field experiment](https://arxiv.org/pdf/2605.14830) | 2026-05；随机现场实验 | 把升级类型、时机和接管后人类投入与服务结果分开 | 现场因果证据；不操纵交接包 |

# 逐来源证据与限制

## 1. Microsoft：交接上下文与运行时状态不是同一个包

**Source evidence：** Agent Framework 允许 agent 按上下文动态 handoff，并维护跨 handoff 的对话历史；但参与者不共享同一个 session，只有用户消息和 agent 消息会广播，工具相关内容（包括 handoff tool call）不会广播。工具需要审批时，工作流暂停并发出 `RequestInfoEvent`；长期等待可用 checkpoint 恢复。[Microsoft Agent Framework Handoff](https://learn.microsoft.com/en-us/agent-framework/workflows/orchestrations/handoff)

**Limitation：** 这是框架行为和推荐模式，不是人类正确率、返工、延迟或过度依赖的测量。**Inference：** “full conversation history”不能自动等价于“receiver knows what tools ran, which state was observed, and why the router chose this path”；这给 EX-003 的 supervision blind spot 提供了具体机制候选。

## 2. Microsoft：私有 handoff message、路由字段和可用接收者可分层

**Source evidence：** Copilot Studio 在升级时可把整个会话送入 engagement hub，由其寻找 best available live agent；显式 `Transfer conversation` 还可附加 private message。默认传递的 `va_LastTopic`、`va_Topics`、最近/全部 phrases、language、conversation ID 及用户定义变量，既可用于路由，也可帮助 live agent ramp up；多个 topic 的变量会在转交前合并。[Copilot Studio live-agent handoff](https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced-hand-off)

**Limitation：** 文档说明字段和行为，没有把“变量集合”作为实验条件，也没有报告最佳 agent 的选择准确率或接收后结果。因此它支持 C 与 R 的结构分离，不能证明 C 造成了更好的升级结果。

## 3. Google Cloud：目标、队列可用性和失败回退是不同对象

**Source evidence：** 转接 payload 分别包含 `escalation_reason`、agent extension/ID、fallback menu 和 language；系统可直接转给 agent，或在失败时先回当前 session queue，再回退到指定 queue，最终可能结束通话。文档还区分 `by_virtual_agent`（planned transfer）与 `by_consumer`（escalation），并说明人类可看到会话历史。[Google Cloud virtual-agent transfers](https://docs.cloud.google.com/contact-center/ccai-platform/docs/virtual-agent-to-human-agent-transfers)

**Limitation：** “direct transfer can improve wait times and customer satisfaction”是产品说明中的预期，不是随机对照或现场效应估计。该材料是客服转接，不等于长程 Agent 的专家处置证据；它能证明对象和失败语义被拆开，不能证明 facilitator 已校准。

## 4. AWS Connect：队列状态不是 handoff context 的同义词

**Source evidence：** AWS 文档把 transfer to a specific agent、transfer to a queue、agent-to-agent transfer 分开；chat transfer 可保留全部 context。队列流可以先检查 staffing/agent availability、queue metrics 和 capacity，再执行 `Transfer to queue`；联系人进入队列后仍等待 agent 接收。[chat transfer](https://docs.aws.amazon.com/connect/latest/adminguide/transfer-chats.html)、[agent-to-agent transfer](https://docs.aws.amazon.com/connect/latest/adminguide/setup-agent-to-agent-transfers.html)、[queue management](https://docs.aws.amazon.com/connect/latest/adminguide/queue-to-queue-transfer.html)

**Limitation：** 这是可配置路由和队列语义，不是比较“有/无容量感知”对人类决策的因果实验；没有交接包消融、接收者正确率或 supervision coverage 指标。它支持 A 与 C/R 分离。

## 5. Calibration 论文：隐藏信息使路由器的完美校准不可得

**Source evidence：** Nalisnick 等证明，delegation 的负担转移给决定“谁来预测”的 rejector；rejector 必须足够细致地识别 human 与 model 各自占优的区域。当 human 依赖系统不可见的额外特征时，rejector 会出现不可约的 excess risk。论文还在 ImageNet-16H 与 HAM10000 的人类预测/模拟专家条件下做实验。[作者论文](https://arxiv.org/html/2606.10906)

**Limitation：** 研究对象是分类预测的 delegation，不是客服/incident handoff；没有 queue、等待、交接包或多级路由。它提供的是“何时升级”存在结构性信息边界的理论与受控证据，不是生产 handoff 的效应量。

## 6. OpenL2D / FiFAR：可用专家改变分派表现

**Source evidence：** 2025 benchmark 将合成专家的决策能力与 work-capacity constraints 分开建模，并通过不同 available-expert seeds、批次容量和 deferral rate 测试分派。FiFAR 包含 50 个合成 fraud analysts、约 30K 个实例；作者报告 L2D 算法的相对排名会随可用专家变化。[作者论文与数据描述](https://www.nature.com/articles/s41597-025-04664-y)

**Limitation：** 专家是合成的，容量是 benchmark 设定，不是实际队列 telemetry；没有自然语言 handoff context，也没有人类接收者的返工/依赖行为。因此它支持 A 是独立变量，却不能估计真实队列对升级结果的影响。

## 7. AI, Take the Wheel：路由/委派与接收后的采纳是两个监督点

**Source evidence：** 论文在 23 名有经验的人、16 个 AI agent、24 场比赛中分别记录：是否让 AI 自主回答，以及看到 AI 建议后是否采纳。bonus 阶段先记录人类初始答案，再展示 AI 建议，因而在同一问题上隔离建议暴露对最终决策的影响；论文报告模型 confidence 在人机分歧时接近 chance，并观察到 under-reliance 与 over-reliance。[作者论文](https://arxiv.org/html/2605.28255)

**Limitation：** 这是 trivia 场景、小样本、非队列 handoff；没有操纵交接包、接收者身份或等待状态。它是接收者侧的因果/准因果边界证据，不是三变量 handoff factorial。

## 8. Alibaba：升级类型、时机与接管投入改变结果

**Source evidence：** Wang 等人的 Alibaba Taobao 随机现场实验涉及 647 名客服工作者和 680,676 条服务对话。处理组监督 agent 可自主解决的 AI-eligible 对话，并在算法标记风险或人类判断需要时接管；控制组全程人工处理。AI 部署降低平均对话时长，但 AI-eligible 对话的客户评分下降。技术能力不匹配触发的升级中，人类介入更能保住服务质量；情绪升级通常发生在挫败已经积累后，接管后的消息数、对话轮次占比、主动查找和方案提供都更低；更早的人工介入能部分阻止恶化。[论文 PDF，第 2、7–10 页](https://arxiv.org/pdf/2605.14830)

**Limitation：** 研究使用 worker-level 随机分配和 worker-day 差分设计，能支持部署与升级类型/时机/接管投入之间的效果异质性；但没有把 full transcript、结构化摘要、evidence-only 或带模型结论的交接包作为随机处理变量。因此它不能单独证明哪一种 handoff packet 更好。

# 这如何改变 EX-003

将 EX-003 的内部分析单元从“handoff 是否完整”改为四个可观测门：

| 门 | 要问的问题 | 当前证据 |
|---|---|---|
| C：context sufficiency | 接收者是否拥有完成判断所需的事实、工具状态、路由理由和不确定性？ | 官方文档支持字段化；Microsoft 明确有未广播的 tool content |
| R：routing calibration | trigger 和目标选择是否把任务送到真正占优的 receiver？ | 2026 calibration 论文支持隐藏信息会造成不可约 rejector 风险 |
| A：availability | 目标/队列能否在有效时间内接收并处理？ | Google/AWS 文档分开建模；OpenL2D 说明可用专家改变分派表现 |
| H：handoff reception | 接收者收到后是否正确使用、复核或拒绝 Agent 的结论？ | AI, Take the Wheel 显示 adoption 与 delegation 分离 |

**更新后的判断：** C、R、A 不是同一变量；H 也不能被 C 的“已发送”状态替代。新的 supervision blind spot 可能出现在两处：路由器不知道接收者的隐藏优势，或接收者看到了摘要却看不到执行证据。现有材料支持把两处写进实验设计，但没有证明哪一处在生产中主导。

本轮新增现场证据后，增加一个横切变量：**handoff timing**。研究应把 `trigger/type → route/receiver → handoff packet → human action/outcome` 作为四段事件链；早/晚升级不能被事后“是否接通”这一单一指标替代。

# 新问题

在固定 escalation trigger、升级时机、Agent 输出、目标专家和 queue state 后，**交接包的内容效应是否仍改变人类正确率、补问、处置延迟和过度依赖？** 若差异只在拥塞、错误路由或情绪负载时出现，则应把它并入 A/R/timing 的交互，而不是声称存在一般性的 context effect。

# 证伪方向

- **证伪 C 的独立性：** 固定 trigger、agent output、recipient 和 queue state 后，完整包、结构化摘要、evidence-only、带模型结论的包在人类准确率、补问、处置延迟和过度依赖上无稳定差异；或差异完全由 framing/证据覆盖解释。
- **证伪 A 的独立性：** 在 route 和 context 固定后，available/congested/failed queue 不改变有效处置率、等待、放弃和误升级，或所有差异都能由 route target 解释。
- **证伪 R 的独立性：** 在同一 queue state 与 context 下，facilitator 选路和固定专家目标没有差异，或差异完全由 receiver skill/hidden feature 解释。
- **证伪 timing 的独立性：** 在固定失败类型与交接包后，早/晚接管不改变人类投入、最终结果或恢复率，或所有差异都由情绪/任务难度解释。
- **证伪“新监督盲区”：** 让 router、receiver 和 evaluator 都获得同一份可审计执行证据后，跨任务、跨负载仍能稳定校准且不出现工具状态遗漏；反之，若只让接收者看到摘要仍出现系统性漏判，blind spot 假设获得反例支持。

# Source 需求

1. 一组可重放的生产级 handoff trace，同时含 `trigger`、候选/实际 receiver、queue state/capacity、context version/字段、tool-call visibility、ack/start time、human decision、resolution 和 rework。
2. 固定 Agent 输出的 context ablation 研究：至少比较 full transcript、结构化 packet、evidence-only、evidence + model conclusion，并记录接收者实际看到的字段。
3. 同一任务族中可独立操纵 receiver availability 与 route target 的人类实验或 benchmark；需要 hidden oracle/外部结果，不能只用模型自报成功。
4. 研究“router 是否知道 receiver 的隐藏特征”和“receiver 是否知道 Agent 的隐藏执行状态”的双向可见性矩阵。
5. 生产或 benchmark 记录 `handoff_packet_version`、`route_target`、`queue_state`、`handoff_at`、`first_human_action_at`、`clarification_count`、`approval/reject` 和最终结果，以便把 packet effect 与 timing/receiver effect 分离。

# 最小实验

固定触发条件、初始状态、Agent 输出、专家和队列负载，只随机化四种交接包：

1. 完整历史 + 结构化状态 + 原始工具/证据；
2. 最小摘要 + 结构化状态；
3. 证据-only，不展示模型结论；
4. 证据 + 模型结论，并显式标注其来源。

再按早/晚两个升级时点分层，记录 human correctness、time-to-correct-action、补问次数、重复工作、override/over-reliance、fallback/abandonment、最终结果和队列等待。关键对照是固定 `route_target` 与 `queue_state` 后的 context ablation，而不是把不同路由的总体成功率直接比较。

# 证据边界

- **已知事实：** 官方文档定义了字段、状态、路由图、队列容量/回退和审批暂停；作者研究给出了隐藏信息、专家可用性、接收后采纳，以及升级类型/时机/接管投入的理论或实验边界。
- **本轮推理：** C、A、R、H 与 timing 应作为不同变量进入 EX-003 的实验矩阵；“全量会话转交”不足以证明监督闭包。
- **仍未知：** 没有找到一手来源在同一 handoff 实验中同时操纵 context package、receiver availability、routing 和 timing，并测量人类最终正确率/延迟/依赖；因此当前结论是设计边界与局部因果证据的组合，不是生产级因果结论。

# 来源链接

- [Microsoft Agent Framework Handoff](https://learn.microsoft.com/en-us/agent-framework/workflows/orchestrations/handoff)
- [Microsoft Copilot Studio live-agent handoff](https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced-hand-off)
- [Google Cloud virtual-agent to human-agent transfers](https://docs.cloud.google.com/contact-center/ccai-platform/docs/virtual-agent-to-human-agent-transfers)
- [Google Cloud Chat Platform API Guide](https://docs.cloud.google.com/contact-center/ccai-platform/docs/chat-platform-api-guide?hl=en)
- [Google Cloud Transfers dashboards](https://docs.cloud.google.com/contact-center/ccai-platform/docs/dashboards-transfers)
- [AWS Connect: transfer a chat with context](https://docs.aws.amazon.com/connect/latest/adminguide/transfer-chats.html)
- [AWS Connect: agent-to-agent transfers](https://docs.aws.amazon.com/connect/latest/adminguide/setup-agent-to-agent-transfers.html)
- [AWS Connect: queue status and capacity](https://docs.aws.amazon.com/connect/latest/adminguide/queue-to-queue-transfer.html)
- [Human-AI Teaming Through the Lens of Calibration](https://arxiv.org/html/2606.10906)
- [A benchmarking framework and dataset for learning to defer](https://www.nature.com/articles/s41597-025-04664-y)
- [AI, Take the Wheel](https://arxiv.org/html/2605.28255)
- [Alibaba Taobao field experiment](https://arxiv.org/pdf/2605.14830)
