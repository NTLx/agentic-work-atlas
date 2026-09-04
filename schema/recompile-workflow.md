---

title: "Recompile 持续重编译工作流"
type: schema-subdoc

---

«本文档是 Agentic Work Atlas Schema 子文档，由持续重编译任务按需加载。
本文件是 "recompile" 的唯一运行协议；入口 Prompt 不重复维护这里的工作流规则。»

Recompile 持续重编译工作流

定位

"recompile" 用于消化已有研究债务。

它不负责主动扩张研究空间，也不负责持续生成更多观点。

与 "explore" 的边界：

- "explore"：打开问题，产生新问题、证伪方向、Source 需求和下一步实验。
- "recompile"：选择一个已经存在的判断或问题，用最小动作使我们的认识发生变化。

每轮只有一个目标：

«One Claim · One Gap · One Action · One Delta»

“想得更多”不是完成条件。

“知道得更清楚一点”才是。

---

核心对象

Claim

一个能够独立改变真伪判断或适用边界的命题。

好的 Claim：

«Agent 自治程度提高会增加 verification 成本。»

过大的 Claim：

«Agent 自治会增加 verification 成本、改变组织结构并最终使管理岗位消失。»

如果一个命题中的不同部分可能分别被支持或推翻，应拆开研究。

---

Gap

本轮阻止 Claim 前进的一个最重要知识缺口。

只使用四类：

- "Evidence"：缺事实、数据、一手案例或现实验证。
- "Counterexample"：现有材料主要支持一个方向，需要主动寻找反例或失败条件。
- "Boundary"：概念、适用对象、场景、时间或前提条件不清。
- "Mechanism"：现象已有一定证据，但为什么发生、通过什么机制发生仍不清楚。

一次只处理一个 Gap。

---

Evidence

Evidence 是能够约束 Claim 的来源材料，例如：

- "raw/" 原始材料；
- 可回溯到 raw 的 source；
- 一手外部来源；
- 必要时的高可信二手来源。

已有 Wiki 页面可以帮助定位 Evidence 和理解上下文，但不能因为 Wiki 自己重复了一次判断，就被当成新的独立证据。

同一 raw 及其 source summary 只算同一份来源依据。

Source-Class Gate

如果当前 Evidence goal 明确要求特定来源类别，例如官方文件、一手来源、原始数据、正式决定或直接实验结果，则在取得该来源类别之前，不得仅凭二手报道、转载、聚合页或搜索摘要把 Claim 判为 `strengthened` 或 `falsified`。

低一级来源可以用于定位 Evidence、暴露矛盾、收窄边界或形成后续检索方向，但不能替代 Evidence goal 指定的来源类别。

在目标 source class 尚未取得时，应根据实际结果使用 `refined`、`blocked` 或 `no_delta`。

多个页面如果来自同一原始报道链、互相转载或共享同一个未核实源，不视为多个独立 Evidence。

---

Reasoning

Reasoning 是对 Evidence 的解释、比较和推导，包括：

- Agent 自己的综合分析；
- 当前按动态协议激活的 Skill 输出；
- 类比、机制模型和概念推演。

Reasoning 不是 Evidence。

增加推理深度可以改变理解方式，但不能自行增加证据强度。

多个 Persona 达成共识也不是多个独立证据。

---

Delta

一次运行结束时，只选择一个主要 Delta：

- "strengthened"：新证据使 Claim 更可信。
- "weakened"：反例或新证据使 Claim 变弱或适用范围缩小。
- "falsified"：关键 Claim 被明确推翻。
- "refined"：定义、边界、条件或机制得到实质澄清。
- "blocked"：已经明确当前为什么无法继续，以及缺什么才能继续。
- "no_delta"：完成了一次有效检查，但当前认识没有发生变化。

新增名称、比喻、术语、公式、“定理”或更多解释文字，本身不构成 Delta。

---

工作流

0. Preflight

生成一次统一时间戳：

python3 -c "from datetime import datetime; print(datetime.now().isoformat(timespec='seconds'))"

保存为 "TIMESTAMP"（本轮运行变量，只在日志与 commit 中引用；不创建 TIMESTAMP 文件，不写入仓库）。

本轮所有日志和提交统一引用该值。

检查工作区：

git status --short

如果存在与本任务无关的未提交修改，停止执行：

工作区非 clean，本次 recompile 未执行

不要修改或覆盖用户已有工作。

---

1. SELECT — Main Agent 选择一个 Claim

1.1 最小读取

先读取：

"wiki/research/research-agenda.md"

但只读取选题真正需要的操作内容。

优先级：

1. 如果存在 "## Recompile Queue"，只从该节选择。
2. 如果尚未迁移到 Recompile Queue，则从当前活跃研究焦点、活跃假设、待验证或待证伪内容中选择。
3. 读取“最近思考结论摘要”最近 5 条，避免立即重复刚完成的方向。

不要为了寻找任务而：

- 通读全部 research logs；
- 通读整个 Wiki；
- 扫描所有 low-evidence 页面；
- 主动创造一个新的研究主题。

发现新研究问题属于 "explore"。

1.2 可行动条件

优先选择同时满足以下条件的 Claim：

- 已经有明确问题或缺口；
- 当前存在可以执行的下一动作；
- 有合理可能通过一次小动作改变我们的认识。

跳过：

- 只有“值得继续想想”，但没有明确 Gap；
- 已明确缺失当前不存在的 source；
- 最近刚检查，且没有任何新信息；
- 需要用户价值判断或权威决定才能继续；
- 本轮需要先完成另一个大型研究问题才能推进。

如果没有可行动 Claim：

本次无可行动 Claim，退出

直接结束。

不创建空日志，不制造 commit。

---

2. DIAGNOSE — Main Agent 找到当前 Gap

读取当前 Claim 直接引用的材料。

初始上下文保持小：

- Claim 本身；
- 最近相关摘要；
- 最多几个直接相关的 entity/topic/source/raw。

优先使用搜索和局部读取定位内容，不默认打开完整长文档。

只回答一个问题：

«当前最可能阻止这个 Claim 改变认识状态的缺口是什么？»

从以下四类中选一个：

Evidence
Counterexample
Boundary
Mechanism

记录：

Claim: ...
Gap: Evidence | Counterexample | Boundary | Mechanism

如果无法确定 Gap，说明 Claim 本身还不够清楚。

本轮以 "refined" 或 "blocked" 收束，而不是调用多个工具寻找灵感。

---

3. ACT — Main dispatch，Worker 执行一个最小动作

每轮只选择一个主要 Action；Action 属于 worker execution，不能由 Main Agent
在主回路中自行完成：

evidence_search
reasoning_operator

不要把它们串成固定流水线。

Main Agent 根据 Claim、Gap 和 side-effect budget 规划一个 bounded worker task，
然后派发给唯一的 active worker。Worker 不得 spawn 另一个 agent；若执行中发现
需要第二个认知 operator，返回 `New bottleneck`，本轮停止，交给 Main 在后续
re-select。若 worker spawn 因瞬时 Runtime/gateway 问题失败，Main 最多做一次
bounded retry；仍失败则停止 execution slice 并以 `blocked` 或 `failed` 结束，
不得把失败改成 `Skill: none`，也不得由 Main 接管实际 Action。

一旦一个 Action 已足以产生 Delta，就进入 "SETTLE"。

如果 Action 暴露出新的不同 Gap，把它记入 "Next"，交给后续运行。

---

3.1 "evidence_search"

适用于：

- "Evidence"
- 大多数 "Counterexample"
- 需要检查 source 是否真的定义了某个边界的 "Boundary"

Main Agent 先确定 Evidence goal，然后 dispatch evidence_search worker。Main 不
自行执行本轮 substantive search。Worker 先搜索仓库已有材料：

优先顺序：

1. 当前 Claim 已链接的 raw/source；
2. 相关 "wiki/sources/"；
3. 精确关键词搜索 "raw/"；
4. 仓库材料确实不足时再联网。

使用搜索结果先定位相关片段。

不要因为文件相关就默认阅读全文。

外部搜索

联网只在仓库 Evidence 不足时使用。

Worker 执行联网前先写一句：

Evidence goal: [我要寻找什么，以及什么结果可能改变当前 Claim]

如果 Evidence goal 指定了 source class，搜索与结算必须先通过 Source-Class Gate；二手结果只能作为线索，不能替代目标来源类别。

如果需要联网，worker 按仓库路由加载：

"schema/web-tools.md"

默认预算：

- 最多 2 次搜索 query；
- 最多打开 3 个真正相关的外部来源；
- 优先一手来源、原始数据、官方材料和实际案例；
- 找到足够改变或卡住 Claim 的材料后立即停止。

第二次 query 应是第一次搜索的定向修正，而不是无边界扩张主题。

找不到关键 Evidence 时：

Delta: blocked

明确记录：

Missing: [需要什么材料]

搜索失败不会让内部推理获得更高可信度。

本轮选择 "evidence_search" 后，不再选择 reasoning operator。Worker 返回
Evidence package；Main 只观察、审查和结算，不把搜索交回自己执行。

如果搜索结果暴露了新的解释问题，把它写入 "Next"。

---

3.2 "reasoning_operator"

reasoning operator 不是默认步骤，只在 Evidence 已足够支持一次局部分析、而当前
Gap 主要是竞争解释、Mechanism 或 Boundary 时考虑。若真正缺的是事实、案例或
反例，应先执行 `evidence_search`；只是觉得“还能再深入一点”也不足以触发它。

由 Main Agent 加载 `schema/skill-mapping.md`，查看 Runtime 当前发现的 Skill 描述。
只可选择明确支持 headless、无人值守且输入契约适配当前 Gap 的 Skill；不得把
交互式 Skill 自行模拟成无人值守 operator。选择 `none` 也是有效结果。若选择
Skill，Main 必须完整读取实际 `SKILL.md`、必要 references，完成 compatibility
check，并把 exact locator/path 传给 worker；worker 执行前必须再次读取同一个
实际 `SKILL.md`。

如果当前 Gap 确实需要 reasoning operator，但 Runtime catalog 中没有安全、headless、
输入契约匹配的候选，记录 `Skill: none` 后直接进入 "SETTLE"。此时不得自行模拟
某个 Skill，不得把 Action 改成联网搜索或其他未经选择的动作：若缺少 operator 使
Gap 无法推进，使用 `Delta: blocked` 并记录
`Missing: eligible headless reasoning operator`；若已有材料已足以确认本轮没有
进一步变化，使用 `Delta: no_delta`。

Main 发给 reasoning worker 的输入只包含：

- Claim；
- Gap；
- 已知的、可回溯的关键 Evidence；
- 当前需要区分的竞争解释、机制或边界问题。

在 worker brief 中附加：

【无人值守模式】本次任务无人值守。请自主完成本次分析并自然收束，不询问用户、不等待用户输入。只聚焦当前 Claim 和指定 Gap；输出属于 reasoning，不判断证据等级，不写入 Wiki，不创建文件或外部笔记。

如果 worker 加载的 Skill 返回需要用户选择的菜单或问题：

- 不询问用户；
- 不重复调用以推进交互；
- 使用已经返回的有效材料；
- 在 Reasoning 中注明“Skill 提前停在交互边界”；
- 进入 "SETTLE"。

不要为了达到某个轮数继续分析。当下钻只会产生无法被 Evidence 区分的故事时
停止；发现新的 Gap 时由 worker 返回 `New bottleneck` 并写入 "Next"。本轮完成
reasoning operator 后，不再调用另一个 reasoning operator，也不联网扩展研究。

---

4. SETTLE — Main Agent 判断知识是否发生变化

Worker 完成唯一 Action 并返回后，Main Agent 立即判断 Delta。Worker 不拥有
最终 Delta 裁决权，也不能把自己的 reasoning 直接升级为 Evidence。

只允许：

strengthened
weakened
falsified
refined
blocked
no_delta

使用以下检查：

«如果删除本轮所有新增的解释性文字，只看 Evidence、Claim 和它的适用边界，我们对它知道的东西是否发生了变化？»

如果 Evidence goal 指定了 source class，先检查本轮是否取得该来源类别；未取得时，`strengthened` 或 `falsified` 不得仅由低一级来源支撑。

如果没有：

Delta: no_delta

以下情况不能被包装成知识增量：

- reasoning operator 达成了共识或产生了更抽象的解释；
- 创建了一个新术语；
- 给旧观点取了“定理”名称；
- 生成了一段更有说服力的 prose；
- 同一个 Evidence 被不同 Wiki 页面重复引用。

---

沉淀

Research Log

SETTLE 后的写入与验证仍由 worker 完成。Main Agent 先根据 worker result、Evidence、
Reasoning、diff 和 validation 决定唯一 Delta，再向**同一个 worker**发送一次
settlement/persistence follow-up，要求它只持久化 Main 已决定的结果、运行 lint，
并按既有规范 commit / push。该 follow-up 不是第二个 epistemic Action；不得在其中
新搜索、新选 Skill、新做 reasoning operator 或重新分析 Gap。Main 只做控制面检查、
观察验证结果和最终验收。

只要实际选中并检查了 Claim，就记录一次紧凑日志。

按照 "schema/research-module.md" 的目录和 frontmatter 规则写入：

wiki/research/research-logs/YYYY-MM-DD.md

追加：

## Recompile [TIMESTAMP] · [Claim 简称]

- Claim: [一个命题]
- Gap: [Evidence | Counterexample | Boundary | Mechanism]
- Action: [evidence_search | reasoning_operator]
- Skill: [none | 实际 worker 加载的 Skill 与 locator]

### Evidence
- [supports | challenges | bounds] [raw/source/URL] — [具体约束 Claim 的内容]

### Reasoning
- [只写真正影响结论的 1–3 条推理；没有则写“无额外推理”]

### Result
- Delta: [strengthened | weakened | falsified | refined | blocked | no_delta]
- Conclusion: [1–3 句]
- Next: [下一步最小动作 | none]

Evidence 与 Reasoning 必须分开。

日志只保存 decision-grade trace。

不要保存：

- 完整 Skill transcript；
- Skill 的长篇原始输出；
- 与最终 Delta 无关的思维旁支。

第三方 Skill 在仓库外产生的笔记或副作用文件不是 Wiki Evidence，不加入 Git。

---

Research Agenda

Research Agenda 是操作索引，不是完整研究正文。

写入前加载：

"schema/research-module.md"

只做与本轮 Claim 有关的最小修改。

包括：

- 更新 Claim 当前 Gap 或下一动作；
- 更新最近检查时间；
- "blocked" 且缺材料时更新 "## Source 需求队列"；
- 已被 falsified 或已无下一动作的条目，从活跃操作区收敛或移除；
- “最近思考结论摘要”只保留最近 5 条；
- 更新“思考日志索引”。

不要把完整 Evidence、完整推导或长篇结论复制到 agenda。

Recompile Queue

如果 agenda 已存在：

## Recompile Queue

优先使用以下紧凑格式：

| ID | Claim | Gap | Refs | Last |
|----|-------|-----|------|------|
| C017 | 一个可独立判断的命题 | Evidence / Counterexample / Boundary / Mechanism | [[直接相关页面]] | YYYY-MM-DD |

如果当前 agenda 尚未迁移到该格式：

- 本轮仍可使用现有活跃研究节；
- 不要为了执行一次 recompile 而批量重构 agenda；
- Queue 迁移作为独立维护任务处理。

---

Stable Wiki 边界

默认：

Stable Wiki changes: 0

Synthesized 判断只留 Research。

包括：

- LLM 跨来源综合产生的新判断；
- 新因果模型；
- 新规律；
- 新机制理论；
- reasoning operator 的共识或推导；
- 新“定理”；
- 尚需反例或现实验证的解释。

即使这些内容非常有启发，也不由 daily recompile 自动晋升。

如果一个 synthesized 判断已经明显成熟，只记录：

promotion candidate

本任务到此为止。

---

允许修改 Stable Wiki 的唯一例外

只有同时满足以下条件，才允许修改最多 1 个已有 entity/topic：

1. 本轮发现的是 raw/source 直接明确支持的 extracted 事实；
2. 不需要跨来源推理才能成立；
3. 与已有稳定页面直接相关；
4. 修改只是补充或纠正现有事实；
5. 不需要创建新的 entity/topic。

不满足任一条件：

«留在 Research。»

"recompile" 不创建新的稳定知识页面。

---

上下文与预算

预算是上限，不是目标。

正常运行应尽早结束。

上下文原则

默认只加载：

- 当前 Claim；
- 最近 5 条思考摘要；
- 当前 Claim 的少量直接引用；
- 当前 Action 真正需要的 source/raw 片段。

不要预加载：

- 全部 Wiki；
- 全部 research logs；
- 全部 Schema；
- 与当前 Gap 无关的资料。

Schema 也按分支加载：

- 管理 research → "schema/research-module.md"
- 联网 → "schema/web-tools.md"
- 使用 Skill → "schema/skill-mapping.md"
- commit → "schema/git-commit-spec.md"

没有进入对应分支就不要读取。

---

单轮硬上限

每轮：

- Claim：1 个；
- Gap：1 个；
- 主要 Action：1 个；
- reasoning operator：最多 1 个；
- 不因 Skill 数量增加而增加 Action；
- 外部搜索 query：最多 2 次；
- 实际打开外部来源：最多 3 个；
- Stable Wiki：最多修改 1 个已有页面，默认 0；
- 不创建新 stable page。

Token 使用目标：

- 普通 evidence run：尽量约 10–20k；
- 需要较多检索：尽量约 20–30k；
- 使用一次重型 reasoning Skill：仍应尽早结束；
- 若运行环境可观察 token，约 50k 视为硬上限。

如果无法直接观察 token，以以上 Action 和 Tool 上限为准。

不得因为“还有预算”继续研究。

---

退出条件

满足任一条件立即进入沉淀或结束：

- 没有可行动 Claim；
- 一个 Action 已经产生 Delta；
- 已明确 "blocked"；
- 当前剩余动作只会产生更多解释，而不会改变知识状态；
- 已完成本轮唯一 reasoning operator；
- 外部搜索预算耗尽；
- 继续工作需要切换到另一个主要 Gap；
- 接近运行预算或外部调度器时间限制。

发现下一步有价值，不意味着必须本轮执行。

记录到：

Next

即可。

---

完成门

如果没有选中任何 Claim：

- 不修改仓库；
- 不创建日志；
- 不 commit；
- 直接输出摘要并结束。

如果已经检查一个 Claim：

1. 确认 Research Log 已记录：

   - Claim
   - Gap
   - Action
   - Evidence
   - Reasoning
   - Delta
   - Conclusion
   - Next

2. 确认 Research Agenda 已做最小同步。

3. 检查 diff，删除：

   - 无关改动；
   - 完整 Skill transcript；
   - 仓库外笔记的复制；
   - 为了“丰富内容”产生的额外页面。

4. 由 settlement worker 运行：

uv run python tools/wiki-lint.py --fix-index --write-report

5. Main Agent 观察 lint 结果；若 lint 报错，worker 只修复本轮导致的问题并重新
   运行。无法安全修复则将结果报告为 `failed`，不由 Main Agent 接管写入：

   - 只修复本轮导致的问题；
   - 修复后重新运行；
   - 无法安全修复则恢复本轮修改并结束为 "failed"。

6. settlement worker 提交前加载：

schema/git-commit-spec.md

遵守仓库 commit 规范。

"recompile" 的 commit 应表达本轮知识变化，而不是“又思考了一次”。

建议语义：

recompile: [Claim 简称] — [Delta]

正文只保留：

- gap: [Gap]
- action: [Action]
- delta: [Delta]
- next: [Next | none]

7. settlement worker 提交并推送；Main Agent 检查 commit、diff 和 validation 后
   完成验收。

push 失败：

- 保留本地 commit；
- 输出 commit hash；
- 明确说明 push 失败原因。

"no_delta" 仍应保留紧凑日志和最近检查信息，以避免调度器立即重复同一 Claim。

---

stdout

结束时只输出紧凑摘要：

=== Recompile ===
时间：[TIMESTAMP]
Claim：[Claim | none]
Gap：[Gap | none]
Action：[evidence_search | reasoning_operator | none]
Delta：[strengthened | weakened | falsified | refined | blocked | no_delta | none]
Evidence：[N]
Skill：[none | worker 实际加载的 headless Skill 与 locator]
Stable Wiki：[0 | 1]
Next：[下一步 | none]
Commit：[hash | none]
Status：[success | blocked | no_delta | skipped | failed]

不要在 stdout 重复完整研究日志。
