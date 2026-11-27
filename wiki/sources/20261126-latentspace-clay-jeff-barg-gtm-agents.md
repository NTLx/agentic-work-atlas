---
type: source-summary
title: "How Clay Builds GTM Agents — Jeff Barg, Head of AI"
source_raw:
  - "[[20261126-latentspace-clay-jeff-barg-gtm-agents]]"
canonical_url: "https://lspace.beehiiv.com/podcast/s/latent_space_the_ai_engineer_podcast/how_clay_builds_gtm_agents_jeff_barg_head_of_ai"
raw_state: full
created: 2026-11-27
updated: 2026-11-27
tags:
  - source-summary
  - agentic-engineering
  - harness-engineering
  - agent-evaluation
  - product-management
evidence_level: medium
claim_type: mixed
source_locator:
  - "03:27–06:46 GTM Engineer：Agent、数据与软件工程的结合"
  - "11:14–17:25 Persona focus；Signals 从静态名单到事件驱动与状态聚合"
  - "17:34–27:43 Claygents、Sculptor、工具循环的局限、CLI 与 Audiences"
  - "27:50–36:59 Post-training 经济性、Jev 成本估算、前沿模型与自动路由"
  - "37:11–41:09 轨迹、工作流属性、下游业务成果三层评测"
  - "42:17–48:22 BullMQ、数据库、可观察性、突发推理、限流与公平性"
  - "48:22–54:28 内外 Harness 能力平权、CLI/MCP、Pi 与 Vercel AI SDK"
  - "54:28–59:13 ChatGPT Apps 合作风险及组织应对"
  - "1:00:25–1:06:42 Workflows、YC 分析与上下文层权限边界"
  - "1:07:01–1:11:16 反复失败的 CLI 调用、trace diagnosis、手写 Skills"
---

# Clay：从单元格 Agent 到可被任何 Harness 使用的 GTM 基础设施

> 一手来源：[Latent Space 官方节目（2026-11-26）](https://lspace.beehiiv.com/podcast/s/latent_space_the_ai_engineer_podcast/how_clay_builds_gtm_agents_jeff_barg_head_of_ai)。Jeff Barg（Clay Head of AI）访谈。主要证据为用户提交的完整 SRT：111,983 bytes、524 个连续字幕块、00:00:00.560–01:12:23.372、正文约 17,263 空格分隔词；原附件 SHA-256 `5e6d2453e61c09e3c9ee343a717ab7a6f83221c1dec441fb0c460151cf3e466d`。已核对官方节目标题、时长及章节导读。Raw 保存原始字幕时间与文字，加来源元数据，Registry 正文哈希由脚本计算，区别于原始 SRT 字节哈希。自动字幕存在 Jeff Bard/CloudCode 等专名误识，本摘要按官网 Jeff Barg、Claude Code 等校正，不改 Raw。产品与经营信息是受访者及发布方在访谈时的自述；未独立重跑 Clay 评测、取得财务审计或验证所有功能的 GA 状态。

## 编译摘要

### 1. 浓缩

#### 一、GTM Engineering 不是用 LLM 批量写销售邮件，而是构建可运行、可维护的收入系统

- **来源（03:27–06:46）**：GTM Engineer 结合 Agent 工程（资格筛选和判断）、数据工程（构建、转换、富集、过滤名单）以及软件工程（网站表单触发调查、交给销售或外联流程）。原本多分散在 RevOps、Growth Engineering 与销售操作中。Clay 从横向低代码工具聚焦一个核心 persona；Avenue 的经验则是把工程可观察性带到运营。
- **来源（11:14–16:06）**：Signals 解决静态名单之外的问题：监控职位变动、晋升、新闻等市场事件，结合已积累的状态决定何时响应。例如同一家公司的三人迁至另一家公司才触发动作。Barg 明言大量可用信号会让用户不堪重负。
- **综合判断**：`source event → canonical entity → dedup / state aggregation → qualification → authorized play → receipt / feedback`。信号覆盖不等于行动价值；事件、资格判断、外联动作和结果需分开计量。持续运行的 GTM 系统应使用持久状态和受限触发规则，而不是让 LLM 维持所有任务状态。
- **边界**：这些例子并未提供销售增量的独立对照，监控联系人与客户数据也必须满足授权、隐私、数据保留及营销合规要求。

#### 二、Claygents 与 Sculptor 是不同抽象层：执行单个任务与生成任务系统

- **来源（17:34–24:45）**：早期 Claygents 在表格中进行 Web 研究、分类、提取、评分和文案生成，返回单元格结构化结果。Sculptor 则负责搭建和配置这些工作流。2025 年 9 月上线的早期 Sculptor 主要是工具循环及精调 Prompt，能添加列，却不能可靠完成端到端获客目标。上线后发现用户需要表格分析、企业表包含数百万条记录等情境未被原评测覆盖。
- **来源（24:54–27:43、37:20–38:22、53:46–54:28）**：重构基于三项认识：模型更擅长通过 Bash/Python 编写脚本并组合工具；单一细粒度工具表达力不足；CRM、活动反馈等关键上下文原本缺失。新 Sculptor 基于 Pi Harness、Vercel AI SDK 和云沙箱中的 Clay CLI；Audiences 将 CRM、Gong 等第一方信息实体解析为可查询上下文。原文称 Audiences 为单租户，而 Clay 另有共享公司与联系人基础数据。
- **综合判断**：将 `semantic planner / workflow compiler` 与 `bounded task executor` 分开；共用可组合的领域 API/CLI、身份和数据语义。构建计划应可检查，执行由确定性运行时接管；编码式 Harness 解决工具表达力问题，不天然解决权限、资源和事务。
- **边界**：新 Sculptor 在部分产品表面已可用、广泛上线仍是访谈时计划（1:04:10–1:04:41）；不是证明 CLI 在所有任务优于 MCP 或结构化工具。单租户描述限于访谈所谈数据层，不能推断整个 Clay 基础设施完全物理隔离。

#### 三、前沿智能的边际价值向编排和深度研究上移；固定分布中的任务应独立优化单位成本

- **来源（27:50–34:16）**：Barg 区分直接使用较小开放权重模型与针对自身工具和输入分布做后训练；目标是保持任务质量同时降低成本、延迟。他认为很多企业太早做后训练，尚无足够推理支出使节省覆盖研发投入；提到数千万至上亿美元量级的推理支出作为经验性讨论，不是通用门槛。常规资格判断的内部评测据称约一年处于饱和状态，深度调查和复杂 GTM play 编排仍受益于前沿模型。
- **来源（31:07–32:34）**：以 Jev 分类器说明低成本全量市场扫描的可能性：Clay 公司数据集约 4000 万条，每条公司描述约 1000 tokens 加 ICP 约 500 tokens。访谈估算总成本约 1500 美元，并提及每十亿 tokens 42 美元，但按该输入数和单价直算为 60 billion tokens × 42 USD/billion = 2520 USD；字幕口算与估计不一致，且 Jev 尚未用于生产。该数字不能当作实际报价或已完成实验。
- **综合判断**：模型路由按任务复杂度、证据敏感度、质量下限和真实成本进行，而非统一切换最低价模型。训练决策应比较 `baseline spend × achievable saving` 与训练、数据、托管、回归、运维及机会成本。低价筛选仍需召回率、校准、数据覆盖、误判代价和候选复核。
- **边界**：所谓评测饱和仅指 Clay 当前内部任务集；没有公开样本或独立结果。4000 万公司是其数据集，不等于全球公司全覆盖；成本未含获取/清洗资料、上下文、失败重试、人工复核和业务动作费用。

#### 四、Model Selector 是成本与效果决策的用户负担，自动路由必须赚取信任

- **来源（34:16–36:59）**：Barg 称大多数客户不愿面对模型选择，不应要求每个客户追踪每次新模型在各用例上的评测。计划推出 Auto Mode，按任务挑选模型；查 Apple CEO 与查不知名公司的 CEO 需要不同能力。仍保留手选模型，尤其面向 agency 等熟练用户。主持人提出自动模式的 token 消耗信任问题。
- **综合判断**：将模型能力、价格、限流、数据边界和质量回归封装到路由控制面；给用户简单默认、成本上限、可追踪账单和必要的手动覆盖，而不是暴露不断变化的模型清单。自动路由必须记录实际选择、fallback 与结果，以便验证其不劣于基线。
- **边界**：没有已上线 Auto Mode 的效果、满意度、成本或对照结果；“多数客户讨厌选择器”是定性自述，不是统计问卷。主持人举的 5% 不是 Clay 实测用户比例。

#### 五、Eval 应分层：工具轨迹、实际产物、业务成果；三者不能互相替代

- **来源（23:24–24:45、37:52–40:09）**：早期用 LLM 判断工具调用是否符合预期，遗漏真实工作负载。新评测按用例检查预期轨迹（第一方数据应查询上下文层），并检查工作流是否真的创建、是否包含期望属性。团队希望进一步衡量活动是否收到回复等二阶结果，但这还不是已完成的评测能力。商业成功受客户产品、邮件内容、市场条件等多变量影响。
- **综合判断**：`trajectory / policy compliance → artifact state and properties → downstream outcomes`。第一层检查执行是否合法合理，第二层以真实系统状态和约束为验收，第三层通过实验评估增量价值；不能只用 LLM 评价文本或工具调用数量，也不能只凭收入给单个 Agent 动作归因。产品可提供用户自定义测试和受控对照，让各客户定义其成功条件。
- **边界**：预期轨迹不应变成唯一正确路径；不同可行流程需按约束和最终效果判断。Barg 提及产品内 Eval 类能力与二阶效果是探索，不是已经落地的 GA 功能。

#### 六、生产 Agent 的可靠性问题主要是突发负载、可观测性和租户公平性，不在选哪个 Agent Framework

- **来源（42:17–48:22）**：Clay 自建大部分运行架构，部分耐久执行依靠 BullMQ；没有使用 Temporal 或 LangGraph。产品使用 Postgres、ClickHouse，分析使用 Snowflake；Barg 对未来再增长十倍时 BullMQ 是否够用没有把握。Claygent 一行一 Agent，五万行表可形成瞬时推理负载；引入 LangSmith 观察轨迹，实现节流、供应商失败或限流时暂停/恢复。访谈时还没有全面双供应商 fallback；强调百万条记录的企业任务不能挤占十人小任务。
- **综合判断**：数据平面可并行，但控制面要提供 `per-tenant quotas / fair scheduling / backpressure / retry budget / checkpoint / provider health / idempotent receipts`。把业务任务规模、LLM 调用并发和租户公平分别测量；在实测瓶颈之前不因为框架流行而迁移。
- **边界**：没有公开吞吐、p99、资源配置、调度算法或故障恢复实验；队列存在不等于 Exactly-once，暂停恢复不等于有无缝双供应商切换。

#### 七、Agent-native SaaS 可以把护城河放在领域基础设施，而不是强迫客户使用自家 Harness

- **来源（48:22–54:28）**：Clay 明确希望原生 Agent 和 Claude Code 等外部 Harness 使用 Clay 时获得相近效果，主要通过 CLI，也保留 MCP。API、SDK、CLI、MCP 是消费形态。Barg 回忆内部与外部 Harness 使用比例比预期更接近 50/50，但不记得精确数字和分母；用户已在 Cursor、Codex 等界面做 GTM 与 deal prep，内部需求推动 CLI。产品内仍有原生 Agent，因为用户在 Clay UI 工作时需要它。
- **来源（1:00:25–1:05:27）**：Workflows 起初遭用户反对（想要 spreadsheet），后来据称增长，很多流程由 CLI 或 Agent 建造。以查询使用 Clay 的 YC 公司为例，Agent 约一分钟整合名单与内部上下文，而此前需 CSV、Snowflake/CRM 等多系统操作。实际 YC 渗透率未披露。
- **综合判断**：共享领域原语、数据语义与授权是基础；原生 Agent 负责集成便利，外部 Agent 保留用户熟悉环境。衡量跨 Harness 相同任务的成功率、权限一致性、成本、可审计回执。对照 [[20261119-latentspace-linear-cristina-cordova-gtm-100m-arr]]：Linear 更重视人类回到产品协作，Clay 更愿意让入口外移；两者都需要领域上下文与可执行能力，不应把界面所有权等同于商业价值。
- **边界**：近 50/50 未提供时间窗口或精确分母；不证明内外 Harness 达到质量平权。YC 分析为单次自述而非测试集；只引入 GTM 所需第一方数据并不免除字段/行级授权。访谈中对 MCP 的玩笑不是技术淘汰结论。

#### 八、真实 trace 是改进输入，但 Agent 仍不可靠地识别其他 Agent 的失败根因

- **来源（1:07:01–1:11:16）**：Barg 从大量 trace 发现基础失败仍存在，如相同 CLI 输入重复执行而不纠正。团队尝试让 Agent 找出长轨迹中何处困惑，却发现其往往把合理耗时当错误，诊断直觉不可靠；直接把坏 trace 交给 Agent 分析再改进性能的闭环仍不好用，许多 Skills 仍由人编写。主持人建议清理历史 bug reports、去除 PII 并形成 benchmark；Barg 称尚未开展公开 benchmark。
- **综合判断**：`observed trace → reproducible failure → independently confirmed root cause → bounded candidate change → frozen eval and regression → acceptance`。自动反思的结论是待验证假说，不是自进化准入证据；重复相同失败应由 Harness 的限次、状态和错误反馈约束，而非仅靠 Prompt 自觉。领域人员与工程师共同构建失败分类和测试。
- **边界**：这是实践反例，不证明 trace 自动诊断在所有任务不可行；缺少错误分类准确率及人机对照。公开 benchmark 是建议，不是 Clay 已发布产物。

#### 九、平台合作有不确定性；组织需要可逆的投入，而不是把外部平台路线图当事实

- **来源（54:28–59:13）**：Barg 回忆，为 ChatGPT Apps 首批合作，约四分之一工程团队投入一个月，两天前被告知无限期推迟；其团队仍继续，数天后对方改变决定。他不知道取消原因。受访者用此说明组织勇气与适应。
- **综合判断**：将外部合作依赖拆成复用性高的通用领域 API/能力与平台专用适配，给后者明确资源预算、里程碑、取消与回滚条件。不要将合作方口头预期当生产发布保证。
- **边界**：仅 Clay 一方口述；不推断 OpenAI 决策动机，不把继续投入后碰巧恢复合作当无条件坚持的证明。

### 2. 质疑

1. **估算不一致**：全量分类估计中数量、token 与价格的乘积和口述总价不一致；不得转述为可复现的 1500 美元服务承诺。即便推理便宜，准确性、实体匹配、时效和数据获取仍是成本。
2. **评测饱和不是现实任务解决**：必须检验测试分布、标签和未知样本，区分通用分类与深度调查。不能仅凭旧 Eval 选择廉价模型。
3. **表达力与安全正交**：CLI、脚本和云沙箱提供组合能力，却可能增加权限面、批量副作用和资源开销。统一 API 必须执行权限，不能只依赖沙箱或模型说明。
4. **第一方数据层不是完整真相**：CRM/Gong 的记录可能冲突、过时或无权共享；entity resolution 需要误合并/漏合并的质量控制与来源追踪。
5. **实际成果与归因**：活动回复率、合格会议数、成交受用户、渠道、市场等变量影响，不能直接当单 Agent 的因果指标；不能由业务十倍增长推断特定技术的贡献。
6. **运行时工程需要独立验收**：BullMQ 能支撑当前规模的自述不足以证明每个副作用幂等、无租户饥饿、停机后全恢复。新模型路由的上线和性能仍待验证。
7. **内外 Harness 平权是设计原则而非已实现测量**：相近使用量不证明相同质量、安全和成本；应使用相同任务、相同数据、相同权限比较。
8. **Trace 自评可能循环放大错误**：不能只因 LLM 指出耗时就改变流程；需要复现、专业人员确认、冻结准入评测与新任务验证。
9. **数据使用和外联责任**：扩大市场信号、联系人信息处理和外联规模不等于更好结果，必须按合法用途、授权、退订、敏感信息最小化与人工监督划定边界。

### 3. 对标

| 来源机制 | 现有知识 | 可验证迁移 |
|---|---|---|
| Claygents vs Sculptor | [[Agent-Harness]]、[[Agent-Workflow-Patterns]] | 编排/生成工作流与执行单任务分离；从真实终态验收 |
| CLI/领域原语与跨 Harness 平权 | [[Agent-Ergonomics]]、[[AI-Native-Product-Operating-System]] | 相同授权与任务集对照原生和外部执行，不复制平台能力 |
| Signals、节流、公平与暂停恢复 | [[Agent-First-Process-Redesign]]、[[Organization-as-Agent-Harness]] | 在现有 Broker 测试并发重复、租约与小工单饥饿，不重造队列 |
| 轨迹、产物、二阶结果 | [[Evaluation-Integrity]] | 区分调用成功、实际完成、用户收益；后者用对照而非模型评分 |
| Trace 自动诊断不可靠 | [[Meta-Harness-Optimization]]、[[Recursive-Self-Improvement]] | 以实际失败复现、根因验证、独立回归约束候选更新 |
| 低成本分类 vs 前沿编排 | [[Agent-Harness]] | 按任务分层设置质量、成本及延迟门槛，不能只按模型价格切换 |

对现有 LLM WiKi/n8n：Broker 继续持有任务状态、权限、回执和调度；AI 负责语义执行与判断；将失败 trace 转为可复现问题，不允许自评直接触发生产变更。与 [[20261113-oreilly-what-makes-agent-self-evolving]] 的模块化改进及独立评测形成直接对照：理论上的闭环可行性不能替代工程实测的根因诊断可靠性。

## 前提与局限性

本篇 medium / mixed 表示一手访谈支撑有限的架构事实和经验描述，不为销售效果、推理价格、模型性能或组织战略赋予独立因果证据。附带的完整 SRT 保存精确时间范围，属于本次用户提供的证据；不将自动字幕视作嘉宾审订稿。全文存为 Raw，保留原有字句及时间轴，不向正文追加分析。以上迁移为综合建议，未在 n8n 或生产系统实施。

## 关联概念

- [[Agent-Harness]]
- [[Agent-Workflow-Patterns]]
- [[Agent-Ergonomics]]
- [[AI-Native-Product-Operating-System]]
- [[Agent-First-Process-Redesign]]
- [[Organization-as-Agent-Harness]]
- [[Evaluation-Integrity]]
- [[Meta-Harness-Optimization]]
- [[Recursive-Self-Improvement]]
