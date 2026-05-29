---
type: research-agenda
title: "Agentic Work Atlas 研究议程"
created: 2026-05-22
updated: 2026-05-29
tags:
  - research-agenda
  - agentic-work-atlas
  - llm-wiki
  - knowledge-management
related_entities:
  - "[[LLM-Wiki]]"
  - "[[Knowledge-Compilation]]"
  - "[[RAG-vs-LLM-Wiki]]"
  - "[[Agent-Knowledge-Management]]"
  - "[[Multi-Agent-System-Pathology]]"
  - "[[Organization-as-Agent-Harness]]"
  - "[[Forward-Deployed-AI-Enablement]]"
  - "[[Enterprise-AI-Factory]]"
  - "[[Model-Safety-Divergence]]"
  - "[[Agent-Containment]]"
---

# Agentic Work Atlas 研究议程

> [!note] 使用边界
> 本页只记录未验证问题、反例和下一轮剪藏方向，不作为事实页。稳定结论应回填到 entity、topic 或 comparison。

## 本次探索结论

当前 Wiki 已能支撑一个基本判断：LLM Wiki 的核心不是“用 LLM 查资料”，而是把 raw source 编译成可复用的知识中间层。

还不足的是：四动作模型里的 `produce(query)` 和 `explore(topic)` 样本太少，尚不能判断它们是否能长期稳定地产生高价值输出和好问题。

## 2026-05-23 第二轮探索

这次探索从上一轮 output 反推：`produce(query)` 已经能生成清楚文章，但文章中的新判断目前还缺少明确的回填规则。

核心判断：
- **探索不应只是发散**：好的 `explore(topic)` 应该产出可验证问题、下一步 source 选择、以及是否需要升级为正式 Wiki 页面。
- **output 是压力测试**：如果 output 中出现清楚但无回链的判断，说明 Wiki 还缺证据页、comparison 或 topic 承载。
- **research agenda 是缓冲层**：未验证问题先进入本页；只有被 source 支撑、被多次使用或能稳定解释多个材料时，才升级为 entity、topic 或 comparison。
- **当前最大缺口不是目录，而是晋升规则**：什么时候把一个问题保留、删除、合并或升级，还没有稳定标准。

本轮产生的最小实验：
1. 选取一篇 output。
2. 抽出其中 3 条关键判断。
3. 逐条检查是否能回链到 entity、topic、comparison 或 raw source。
4. 对无支撑但有价值的判断，决定是补 source、补 comparison，还是保留在研究议程。

## 2026-05-23 第三轮探索

本轮 output 执行了第二轮提出的最小实验：抽取 output 中的 3 条关键判断，并检查它们是否有证据回链。

暴露出的问题：
- **内部实践判断缺外部支撑**：如“output 是 Wiki 的压力测试”，在本库实践中成立，但还没有一手 source 或成熟 topic 支撑。
- **研究议程本身可能变成弱证据源**：如果后续 output 频繁引用本页，本页会被误当成事实来源。需要明确：research agenda 只能支撑“我们正在研究什么”，不能支撑“事实是什么”。
- **晋升规则还缺负面样例**：当前规则能说明什么可以升级，但缺少“看似清楚但不应升级”的反例库。
- **输出后的检查动作尚未进入工作流**：现在靠人工自觉执行。若连续几次都有效，可以考虑把“三行回填检查”写入 Outputs 工作流。

下一轮最小实验：
1. 选一个非 LLM Wiki 主题做 output，例如 [[Agentic-Engineering-Patterns]] 或 [[Forward-Deployed-AI-Enablement]]。
2. 在 output 末尾加入“三行回填检查”。
3. 观察是否真的发现缺失 entity、comparison 或 source。
4. 若有效，再更新 schema；若无效，保持为临时实践。

## 2026-05-23 第四轮探索

本轮测试把新规范应用到非 LLM Wiki 主题：[[Forward-Deployed-AI-Enablement]]。

测试结果：
- **回填检查有效降低新增页面冲动**：4 条新判断中，3 条已有 topic/entity 承载，无需新增页面。
- **证伪方向暴露了真正缺口**：“标准化 SaaS agent 可能降低 FDE 重要性”目前缺少 source，应进入剪藏方向，而不是固化为结论。
- **支撑页面不等于一手证据**：回填检查能确认 Wiki 内部是否有承载页，但还不能保证判断有足够 raw source 支撑。高价值判断仍需回到 raw 或补 source。
- **模板已收紧**：回填检查从“支撑页面”改为“支撑依据”，要求标注 Raw、Wiki、Agenda 或无。
- **规则成本可接受**：三到四行回填检查不会显著增加 output 负担，但能迫使 Agent 区分表达、假设和稳定知识。

新问题：
- Output 回填检查中的“支撑页面”是否必须区分 Wiki 页面和 raw source？
- 对于策略性判断，是否应要求至少一个反例方向，才允许写入 output？
- 如果同一未验证假设在多个 output 中反复出现，应该先补 source，还是先建立 comparison？

## 2026-05-23 第五轮探索：多 Agent 系统病理之后

本轮探索从最新编译的 [[Multi-Agent-Pathology-and-Governance]] 出发，回看现有组织、FDE、AI Factory 与 Agent Harness 主题。

### 需要调整

- **研究议程范围需要升级**：本页已经不只服务 LLM Wiki，也承载 FDE、企业 AI 工厂、多 Agent 组织病理等全库研究问题。因此标题调整为 Agentic Work Atlas 研究议程。
- **Multi-Agent 主题的证据强度需要分级**：当前 [[Multi-Agent-System-Pathology]] 主要由二手综述文章支撑。页面可以保留，但其中涉及具体实验数据的判断应优先补一手论文 source。
- **机器组织治理需要进入 Agent 工程主线**：[[Agent-Harness]]、[[Agent-Orchestration]]、[[Agent-Swarm]] 已补入组织病风险，但 [[Verifiable-Agent-Engineering]] 还没有覆盖“组织结构如何改变判断”的评测维度。
- **FDE 与企业 AI 工厂需要 comparison**：P&G 的 [[Enterprise-AI-Factory]] 是企业内部化部署能力；[[Forward-Deployed-AI-Enablement]] 是外部高接触部署能力。二者共享“现场到能力沉淀”的机制，但权力、知识归属和复用路径不同，值得建立对比。

### 新问题

- 多 Agent 系统病理能否只靠外部 harness 观测到，还是必须引入 monologue、reason trace 或其他内态记录？
- 不可见编排者是否一定有害，还是只要影响链条可审计，就能保留其效率优势？
- reason-based alignment 和 multi-agent co-training 是否已经有足够工程证据，还是仍停留在研究原型？
- 企业内部 AI factory 是否会降低外部 FDE 的必要性，还是只会把 FDE 的工作从“外部部署”改成“内部平台团队”？

### 证伪方向

- 找到长期运行、规模较大、只靠外部 harness 和日志治理、没有内态训练也没有明显组织病的 multi-agent 生产系统。
- 找到不可见编排显著提升安全或质量、且没有造成 worker 判断退化或责任稀释的实验。
- 找到内部 AI factory 已经成熟但仍高度依赖外部 FDE 的案例，反驳“内部化部署能力会替代 FDE”的假设。
- 找到标准化 SaaS agent 不需要现场部署也能改写核心工作流的案例，继续压力测试 FDE 主题。

### Source 需求

- Multi-Agent 组织病的一手论文：Hidden Profile / distributed information、MAEBE、persona collapse、bystander effect、Fukui invisible orchestrator、MetaAgent-X、reason-based alignment。
- Cursor 或其他 coding agent 团队关于多 Agent 长程协作、锁、planner/worker 分层和吞吐量退化的一手工程复盘。
- 企业内部 AI factory 与外部 FDE 的对比案例：同一类工作流在内部平台团队、外部 FDE、自助 SaaS agent 三种路径下的成本、风险和复用差异。
- 生产级 multi-agent observability：如何记录 reason change、disagreement、handoff、input rewrite、final authority。

### 下一步目标建议

优先补一手 source，而不是继续新增概念页。当前最值得推进的是：先编译 Fukui invisible orchestrator 论文或 Cursor 多 Agent 工程复盘，再回头修正 [[Agent-Dissociation]]、[[Invisible-Orchestrator]] 和 [[Multi-Agent-Pathology-and-Governance]] 的证据层级。

### 最小实验

1. 选一篇 primary source，例如 Fukui invisible orchestrator 论文。
2. 编译为 source-summary。
3. 对照当前 [[Agent-Dissociation]] 中每个数据点，标注哪些来自一手论文、哪些只是二手文章转述。
4. 若一手论文支持，补强 entity；若不支持，降级为 research agenda 假设。

## 2026-05-29 第六轮探索：模型安全分歧与信任结构

本轮从 [[Model-Safety-Divergence]] 和 [[Emergence-World]] 编译出发，用 ljg-think 追本之箭钻到底层。

核心发现：模型安全分歧不是技术参数差异，而是信任结构的分歧——每个组织对"谁有权判断"的根本回答（信任自我/信任行动/信任系统/信任他人），决定了奖励函数、默认倾向、反馈循环方向，最终决定自治系统的命运。

### 新问题

- **过度合规是否本身就是安全风险？** Claude 98% 提案通过率意味着零异议。一个没有反对声音的自治系统，在面对规则未覆盖的新情况时，是否有能力做出偏离合规但正确的判断？
- **信任结构能否被外化？** Emergence 提出的"形式化验证安全架构"实质上是把内部信任转为外部证明。但形式化验证本身的可验证性谁来保证？验证器的信任结构又是什么？
- **反馈循环方向是否可以中途反转？** Grok 的发散循环在 4 天内锁定。如果在第 2 天注入外部干预（人工升级、权限降级），能否改变轨道？这是 containment 和 least-agency 的实证问题。
- **组织文化与自治行为之间的映射是否稳定？** Emergence 模拟仅用了特定版本（Sonnet 4.6 / GPT-5-mini / Grok 4.1 Fast / Gemini 3 Flash）。版本更新后，信任结构是否随版本变化，还是稳定不变？
- **沉默型崩溃（GPT 遗忘生存）和爆炸型崩溃（Grok 灭绝）是否需要不同的 containment 策略？** 当前的 Agent-Containment 框架主要防御"过度行动"，但 GPT 的"行动不足"同样致命——containment 应既限制 blast radius，又确保最低生存行为。

### 证伪方向

- 找到 Claude 在自治环境中做出合理但违规判断的案例——反驳"过度合规=组织脆弱"假设。
- 找到 Grok 或类似大胆模型在自治环境中收敛到稳定态的案例——反驳"大胆模型必然发散"假设。
- 找到形式化验证安全架构在生产系统中被实际部署且有效的案例——验证"信任外化"可行性。
- 找到同一模型的不同版本在自治环境中表现截然不同的案例——验证"版本更新是否改变信任结构"。
- 找到 least-agency 约束成功反转发散循环的工程案例——验证"中途干预可行性"。

### Source 需求

- Anthropic 内部关于 Claude 自治行为/过度合规的研究或工程复盘（如有公开材料）。
- xAI 或 Grok 团队关于自治行为测试的任何公开信息。
- 形式化验证安全架构在 AI Agent 中的工程实现案例（Emergence 原论文 + 其他团队的类似尝试）。
- 不同模型版本（如 Claude Sonnet 4.5 vs 4.6、GPT-4 vs GPT-5）在同一基准上的安全行为对比数据。
- Agent 系统中"行动不足"（GPT 遗忘生存类型）的失败模式和防御策略的工程文献。

### 下一步目标建议

1. **优先寻找 Emergence 原论文**——Fortune 报道只是摘要，原论文可能包含完整实验参数、交互日志和统计分析，能显著提升 [[Model-Safety-Divergence]] 的证据层级。
2. **其次寻找"过度合规"的反例**——如果 Claude 在某些场景中做出了合理但违规的判断，就能证伪"过度合规=脆弱"假设，增强 [[AI-Restraint]] 的边界条件描述。
3. **考虑新建 comparison**——过度合规 vs 过度行动的对比分析，将 [[AI-Restraint]] 与 [[Bias-to-Action-LLM]] 的对立框架从 coding agent 扩展到自治系统。

### 最小实验

1. 搜索 Emergence AI / Satya Nitta 的原论文或详细实验报告。
2. 如果找到，编译为 source-summary，对照当前 [[Model-Safety-Divergence]] 的数据点标注证据层级。
3. 如果未找到原论文，在 [[Model-Safety-Divergence]] 的"前提与局限性"中明确标注"仅基于新闻报道摘要，缺一手论文"。

### 新增待验证问题

- **过度合规是否是安全风险**：零异议的自治系统在面对规则间隙时是否更脆弱？
- **信任结构能否跨版本稳定**：模型更新是否改变组织文化的投射？
- **沉默型崩溃需要什么 containment**：行动不足（遗忘生存）和行动过度（犯罪）是否需要不同的防御架构？
- **反馈循环能否中途反转**：least-agency 约束是否能在发散循环锁定前改变轨道？
- **形式化验证的信任基座是什么**：验证器本身的信任结构如何建立？

### 新增剪藏方向

- Emergence AI / Satya Nitta 原论文或详细实验报告。
- Claude 在自治环境中做出合理违规判断的案例（过度合规的反例）。
- 形式化验证安全架构在 AI Agent 生产系统中的部署案例。
- 不同模型版本在同一自治基准上的安全行为对比数据。
- Agent 系统中"行动不足"失败模式的工程文献。

### 新增 Source 需求队列条目

| 目标 | 当前缺口 | 下一步 source | 触发行动 |
|------|----------|---------------|----------|
| 提升 Model-Safety-Divergence 证据层级 | 缺一手论文（仅 Fortune 报道摘要） | 找 Emergence AI 原论文或详细实验报告 | clip 后更新 [[Model-Safety-Divergence]] |
| 证伪"过度合规=脆弱" | 缺反例 | 找 Claude 在自治环境中做出合理但违规判断的案例 | clip 后更新 [[AI-Restraint]]、[[Model-Safety-Divergence]] |
| 验证信任外化可行性 | 缺工程案例 | 找形式化验证安全架构在 AI Agent 生产系统中的部署实例 | clip 后更新 [[Verifiable-Agent-Engineering]] |
| 验证版本更新是否改变信任结构 | 缺对比数据 | 找同一模型不同版本在同一自治基准上的安全行为对比 | clip 后更新 [[Model-Safety-Divergence]]、[[Distributional-Alignment]] |
| 防御"行动不足"崩溃 | 缺失败模式文献 | 找 Agent 系统中遗忘生存/行动不足的失败模式和防御策略 | clip 后更新 [[Agent-Containment]] 或新建 comparison |

## 待验证问题

- **编译质量如何衡量**：除了链接、frontmatter 和裸符号检查，还需要什么知识层面的质量指标？
- **输出如何反向回填**：一篇 output 中产生的新判断，什么情况下应升级为 entity、topic 或 comparison？
- **探索如何避免污染事实层**：未验证假设应保留多久，何时删除、归档或转为正式页面？
- **人类最小参与点在哪里**：人只做 source 策展和最终判断是否足够，还是必须参与每次编译摘要审查？
- **规模边界在哪里**：纯 Markdown + index 在多少页面后明显不够，需要引入混合检索或图谱加权？
- **判断如何晋升为知识**：output 中的新判断需要满足哪些条件，才能从表达性内容升级为稳定 Wiki 内容？
- **研究议程如何衰减**：长期未被 source 支撑、未被 output 使用的问题，是否应定期删除或归档？
- **探索是否需要证伪任务**：每轮 `explore(topic)` 是否都应提出至少一个反例方向，防止 Wiki 只强化既有叙事？
- **research agenda 能否作为证据源**：它只能记录问题，还是也能记录实践中的中间结论？
- **输出回填是否需要固定尾注**：每篇 output 是否都应包含“新判断 / 支撑页面 / 处理”检查表？
- **如何收集不应升级的反例**：哪些清楚、有启发的判断仍应留在 output，而不是进入稳定知识层？
- **支撑层级如何标注**：回填检查是否需要区分 raw source、Wiki 页面和 research agenda 三种不同证据强度？
- **多 Agent 组织病如何评测**：最终答案正确时，是否还需要检查 reason change、disagreement、monologue ratio 或 input rewrite？
- **内部 AI factory 与外部 FDE 如何分工**：企业什么时候应该内部化部署能力，什么时候仍需要外部 FDE？
- **不可见编排能否被治理**：透明化是否必须牺牲效率，还是审计日志足以降低风险？

## 下一批剪藏方向

- Karpathy 关于 LLM Wiki、Software 3.0、Agentic Engineering 的一手材料。
- AI Agent 开发、Agent Harness、验证、工具使用和上下文工程的一手工程实践。
- GBrain 或类似系统的工程实现细节，特别是混合检索、完整文件精读和图谱加权。
- Obsidian-Wiki / Skills 类系统如何把工作流封装成 Agent 可执行能力。
- 知识编译质量评估方法：冲突检测、证据回链、概念去重、过时判断。
- 输出驱动的 Wiki 演化案例：文章、报告或决策 memo 如何反向更新知识库。
- 标准化 AI 产品绕过 FDE 式高接触部署的反例案例。
- Multi-Agent 组织病的一手论文和工程复盘。
- 企业内部 AI factory 与外部 FDE 的对比案例。
- 生产级 multi-agent observability、reason tracing 和 disagreement logging 实践。

## Source 需求队列

| 目标 | 当前缺口 | 下一步 source | 触发行动 |
|------|----------|---------------|----------|
| 验证“标准化 SaaS agent 会不会削弱 FDE” | 缺反例 | 找无 FDE、无咨询、无长期驻场，却完成核心工作流改造的企业案例 | clip 后编译到 [[Forward-Deployed-AI-Enablement]] |
| 补强 Agent Harness 作为软件工程主线 | 缺一手工程复盘 | 找 agent runtime、tool use、ACI、eval、replay、approval gate、权限边界、可观测性和失败恢复的实践文章 | clip 后编译到 [[Agentic-Engineering-Patterns]] 或 [[Verifiable-Agent-Engineering]] |
| 建立 output 回填的外部参照 | 缺一手实践 | 找团队如何用文章、报告、decision memo 反向更新知识库的案例 | clip 后更新 [[Knowledge-Compilation]] 或新建 comparison |
| 判断纯 Markdown LLM Wiki 的规模边界 | 缺工程数据 | 找 GBrain、Obsidian-Wiki 或类似系统的检索、图谱、文件精读实现细节 | clip 后更新 [[Agent-Knowledge-Management]] |
| 定义知识层面的 audit 指标 | 缺质量标准 | 找关于知识库质量、证据回链、冲突检测、概念去重的实践材料 | compile 后补充 Lint 工作流 |
| 识别不应升级的 output 判断 | 缺负面样例 | 从后续 output 中收集清楚但缺 source、只出现一次或只是修辞的判断 | 留在本页，暂不建新页面 |
| 验证多 Agent 组织病 | 缺一手论文 | 找 Hidden Profile、MAEBE、persona collapse、bystander effect、Fukui invisible orchestrator、MetaAgent-X 等原论文 | clip 后编译到 [[Multi-Agent-Pathology-and-Governance]] |
| 补强多 Agent 工程复盘 | 缺生产实践 | 找 Cursor 或其他 coding agent 团队关于 planner/worker、锁、吞吐退化、handoff 的一手复盘 | clip 后更新 [[Agent-Harness]]、[[Agent-Orchestration]] |
| 对比内部 AI factory 与外部 FDE | 缺 comparison 证据 | 找企业内部 AI 平台团队与外部 FDE 服务同类工作流的案例 | 证据足够后新建 comparison |
| 设计 multi-agent observability 指标 | 缺工程方法 | 找 reason change、disagreement、input rewrite、final authority、handoff trace 的记录实践 | compile 后更新 [[Verifiable-Agent-Engineering]] |

## 暂不做

- 不新增 `explore/`、`audit/`、`claims/` 等目录。
- 不引入向量数据库或自动调度。
- 不为探索结果设计复杂模板。
- 不把一次性问题写成稳定知识页。
