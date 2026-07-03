---
type: research-agenda
title: "Agentic Work Atlas 研究议程"
created: 2026-05-22
updated: 2026-07-03
tags:
  - agentic-work-atlas
  - llm-wiki
  - knowledge-management
related_entities:
  - "[[LLM-Wiki]]"
  - "[[Agentic-Engineering]]"
  - "[[Agent-Harness]]"
  - "[[Human-Governor-Agent-Operator]]"
  - "[[Judgment]]"
---

# Agentic Work Atlas 研究议程

> [!note] 使用边界
> 本页只保留当前最值得推进的方向、待证伪判断、source 需求和最小动作。已收敛判断见 [[resolved-judgments]]；已收敛操作原则见 [[resolved-principles]]；图谱健康度历史快照与成簇分析见 [[research-snapshot-20260703]]；方向库与长问题库见 [[exploration-archive-20260628]]。

## 图谱健康度（07-03 实测）

| 指标 | 当前值 | 动作 |
|------|--------|------|
| Entity / Topic / Comparison / Output | 301 / 31 / 19 / 5 | **建 8-10 topic**（六簇零承载） |
| Entity:Topic 比 | 9.7:1 | 中层断层持续 |
| lint 分数 | 100/100 PASS | evidence_level 阻断已清零 |
| 待编译 raw | 18 | 07-03 已编译 3 轮但未回填 entity |
| 完全孤儿 entity | 2 | `Digital-Life-Kazke` / `Shared-Memory-Contamination` |
| 零入链 topic（死 topic） | 7 | **新发现**，见下方死 topic 清理 |
| 零被引 output | 5/5 | output 层彻底孤岛 |
| Output 转化率 | 5/67+ ≈ 7% | 目标 ≥20% |

> 完整历史快照、成簇明细与缺失领域清单见 [[research-snapshot-20260703]]。

## 当前研究焦点

| 焦点 | 为什么重要 | 当前状态 | 下一步 |
|------|-----------|---------|--------|
| **图谱整合与 topic 建设** | 301 entity / 31 topic = 9.7:1，六簇零承载（记忆13/AGI经济15/安全16/Skill5/Distillation7/Harness6） | 26+3 轮思考产出 52 条新判断但未建 topic 承载 | 建 8-10 topic skeleton；优先记忆/AGI经济/安全三簇 |
| **Output 断层修复** | 5 output 无法验证新判断；零被引；已 32 天无新产出 | 07-01/02/03 日志有丰富原料 | 转 ≥2 output：1) Agent Observability 产业分析；2) 26 轮元合成 rank 文章 |
| **07-03 三轮回填** | 07-03 完成 3 轮 roundtable 但产出未落 entity/topic/comparison | 待回填 | 建 AI-Native-Testing topic / AI-Governance-Regimes comparison / Open-Source-Agent-Ecosystem comparison |
| **Token FinOps 与 AI 计量** | 企业 AI 采用的隐性瓶颈 | ✅ raw 到齐 + 07-02 已立定理 | compile → 建 Token FinOps entity + topic |
| **AI-native 测试与验证方法论** | 评测治理四部曲完成后，下一层是工程实践 | ✅ 07-03 roundtable 完成 | 回填 → 建 AI-Native-Testing topic |
| **跨境 AI 治理差异** | EU/US/CN 三范式对 Agent 部署的实质影响 | ✅ 07-03 roundtable 完成 | 回填 → 建 AI-Governance-Regimes comparison |
| **Agent 经济协议与互操作** | 多 Agent 编排的经济协议和互操作标准 | ✅ raw 到齐 + 07-02 立收敛假说 | compile → 建 Agent Economic Protocols entity |

## 活跃假设

| 假设 | 验证方向 |
|------|---------|
| Agent Control Plane 壁垒转移定理：壁垒从模型→运行时治理。独立窗口 = f(多模型采用 × 监管) | 追踪独立厂商融资；测量多模型采用率 |
| 治理不可委托定理：因果责任可委托，道德责任不可委托。锚点价值 = 可问责性 ≠ 更好的判断 | 找模型被接受"最终负责"的法律案例 |
| 认知分工终态定理：发散 = 1 人 + AI，收敛 = 多独立视角（防共同锚点） | 对照实验：共享 AI vs 不同 AI vs 无 AI |
| AI 认知关系五模式：情境工具箱，Exit-Sovereignty = 元模式 | 测量五模式在不同职业中的分布 |
| 全球南方 AI 跃迁双速定理：AI 可跳过技术层，不可跳过制度层 | 找同时加速个体 + 组织的成功案例 |
| 中国 AI 双速瓶颈：高政策推动 × 低组织准备度。瓶颈 = 科层碎片 + FinOps 缺失 | 找 Token FinOps 实际建立案例 |
| 判断力维护 = 扰动优先于校准：扰动边际收益递增，校准递减。六可操作机制。需外部+市场约束 | 测量六机制在不同 AI 团队的实施效果 |
| 后果真实性不可消除定理：模拟可逼近参数更新(知识)，不可逼近结构更新(存在)。硬边界=时间不可逆 | 找"模拟中的不可逆性"成功案例 |
| Headless Agent 范式三条件：结构化 I/O × 不可变 artifact × Simple 单一职责 | 找满足三条件的实现 |
| AGI 经济学四阶段周期：Token 通胀 → Token 治理 → 结构转型 → 新均衡 | 追踪 Token 成本曲线与企业采购行为时滞 |
| Agent 记忆统一框架假设：编码/巩固/检索/遗忘四阶段映射 Agent 记忆。Context-Rot = 检索干扰 > 存储衰退 | 测量不同记忆架构在四阶段衰减曲线 |
| 合规即代码定理：法规效力=f(可自动化,惩罚痛度,检测概率,配置保鲜度)。终极=自动化问责 | 追踪 EU AI Act 首年自动合规覆盖率 |
| **🆕 Agent 框架分化定理**：终局=后端模式分化（按语言+用例，非前端单一赢家）。差异化=可观测性+状态管理+人机协作（非编排模型）。协议标准化后编排 commodity 化 | 追踪 LangGraph/CrewAI 在三维度功能对比；MCP/A2A 后编排层 commodity 化实证 |
| **🆕 Agent 测试三支柱框架**：正向(LLM-Judge×多模型×人类校准) + 负向(Property 不变量×Adversarial) + 反馈(快速循环×阈值断言)。测试金字塔=沙漏形。粒度=f(失败成本) | 测量 Agent Quality Pipeline 开源实现；LLM-as-Judge 6/12/24 月漂移 |
| **🆕 AI 治理三范式比较框架**：EU(事前/权利/程序俘获)×US(事后/行业/盲区)×CN(集中/安全/风暴执法)。全球标准=多维度碎片化拼图 | 测量"多国最严格交集"统一设计采用率；CN 制度化进程 |
| **🆕 AI 编程范式收敛假说**：Software-2.0→3.0→Vibe-Coding 不是线性升级，而是向"代码作为 agent 记忆/协调介质"的范式收敛 | 找代码仍主要是人-人沟通媒介且 agent 未介入的稳定场景 |
| **🆕 组织形态谱系定理**：AI-Factory/FDE/Agent-First-Enterprise 是同谱系不同成熟度阶段，选型=f(组织规模 × AI 成熟度 × 隐性知识比例) | 找不可归约为谱系的组织形态 |
| **🆕 Benchmark 加速贬值定理**：benchmark 有效寿命 ∝ 1/(agent 能力增长速度 × 优化器迭代速度)，SWE-Bench 饱和是信号 | 找 benchmark 寿命不随 agent 能力缩短的案例 |
| **🆕 认知背离双循环修正模型**：六步反馈环——注意↓→AI降委托成本→AI兜底预期效应→推理动机↓→练习↓→技能退化→委托需求↑。关键变量：AI兜底预期(Mark)×推理动机×练习频率×时间间隙(Wolf)×失败可习得性。断裂点三层因果层级：微观(摩擦性设计)⊂中观(组织激励)⊂宏观(教育评估转向) | 测量六步反馈环各环节的量化系数；追踪教育评估转向的早期实践案例 |
| **🆕 Agent记忆编码优先设计原则**：多维索引(语义+位置+因果+层级)+工具调用自动标记+差异化编码(高价值=多维,低价值=浅)+层次化context(先建概览→按需放大)。核心原则：编码策略>存储容量 | Agent多维编码vs平铺编码A/B对照实验；层次化context工程实现 |

## 待证伪判断（精选最高优先级）

| 判断 | 证据强度 | 证伪路径 |
|------|---------|---------|
| 代理-现实差距是一切失真/博弈/退化/漂移的根源，可由单一生成器反推 | extracted（26 轮降秩元合成） | 找到"度量完美代表现实、零差距、不可博弈"的 AI 评测系统 |
| 时间不对称（后果不可预体验）决定判断力/责任/记忆恢复不可被模拟或加速替代 | extracted | 找到模拟训练在后果真实性敏感任务中达到与真实遭遇同等效果的对照实验 |
| 可博弈性结构必然：Goodhart + Soros 反射性 + Gödel 投影 → 不存在不可博弈的"静态/自我验证"显式仲裁标准。有效评测=制度化纠错=速度×独立性×成本不对称 | synthesized | 找到无需制度约束力而长期有效的纯技术 benchmark |
| Gödel 不完备递归六层定理：博弈从规则→惩罚→独立→道德→信任→共享脆弱性逐层上升，递归终点=共享脆弱性 | synthesized | 找到博弈在某制度层终止且无需共享脆弱性的案例 |
| AI 评测制度化已启动：US AI Incident Reporting Act(2026-06-26)=强制7天报告+`$2M`/天罚款 | extracted | 追踪首次执法行动的时间、力度和效果 |
| 治理内生性六变量定理：可内生=f(验证独立性,退出自由度,受益对称性,参与通道,知识接口化)-不可内化底线。多中心前提=共享脆弱性 | synthesized | 找到满足六变量全部正向且多中心有效的 AI 治理案例 |
| 记忆双重衰减修正——Agent版：检索干扰 > 存储衰退。机制=长context中attention权重被摊薄→关键信息注意力份额↓→检索失败率↑。"Lost in the Middle"=典型表现。encoding specificity(Tulving)+attention dilution(Wei)+有限焦点(Cowan)→三源收敛 | extracted | 找到context长度增长但检索准确率不降反升的Agent系统（需排除RAG/分块等预过滤） |
| **🆕 Context衰减三层修正模型**：L1(关联检查不可压缩性O(N²),最根本不可消除)⊃L2(attention稀疏化+无循环再处理,可工程缓解)⊃L3(编码-检索不匹配+位置效应,最便宜改善最大)。修正：L1不是"信噪比递减"而是"潜在关联检查的不可压缩性"——即使完美信号也受O(N²)约束 | extracted | 找到不依赖预知结构而在O(N)复杂度下维持检索准确率的注意力机制 |
| **🆕 编码策略杠杆定理**：检索准确率=f(编码结构质量×信噪比)/attention稀释因子。编码时1单位投入≈检索时10单位节省。平铺式context=最低效编码。最佳实践：工具调用返回→高优先级编码区→多维索引 | synthesized | Agent多维编码vs平铺编码A/B对照实验（相同context长度，结构化索引 vs 平铺，测量工具使用准确率差异） |
| **🆕 完美信号不可达定理**：严格"完美信号context"不可达成——因为"知道信息已完美"需无限处理预算。softmax attention权重总和=1硬约束→更多token=每token平均注意力↓。即便是纯信号，关联检查的O(N²)不可压缩性导致有限注意力预算下必然牺牲某些信号的处理精度。更大context永远有代价 | extracted | 找到在所有信息精确相关+无冗余+结构预知+长context条件下检索准确率不衰减的案例 |
| Reward Hacking 三层防御定理：评测有效性=主锚(延迟不可伪造信号)×哨兵(短周期博弈可见)×后盾(偏离触发惩罚) | synthesized | 测量主锚延迟缩短极限；哨兵偏离阈值(20%)实证校准 |
| 评测治理三要素缺一不可：制度 × 技术 × 锚定 | synthesized | 找到缺任一要素但仍有效治理的 AI 评测体系 |
| 多 Agent 编排倒 U 型：层级峰顶 ≈5-15。Team of Teams 可推高。瓶颈 = orchestrator context 带宽 | synthesized | 找到层级编排下 15+ Agent 仍无性能退化的案例 |
| 重组双向制度阶段加权：保护^α × 演化^(1-α)。单α不可维持——裂解为多α后，公式价值≠参数计算=结构知识+叙事工具 | synthesized | 找到成功将"移动α"叙事引入实际政策辩论的案例 |
| Agent 互操作协议收敛假说（修正）：3-5 年多协议共存+适配器层崛起。Transport 不收敛到 1 胜者。前提=中性治理组织出现 | hypothesis | 追踪 CNCF 式 AI 协议治理组织出现 |
| Token FinOps 品类窗口定理：独立窗口=归因层(语义级成本归因)。终局=被可观测性平台收购非独立上市。中国延后 2-3 年 | hypothesis | 追踪推理链 API 开放度和可观测性平台收购动作 |
| Context Advantage 解释力边界定理：在可类型化任务中有效；在独一性任务中漏失——"谁在做"对行为意义有构成性影响 | synthesized | 测量独一性任务中 AI 输出质量=人类但位格替换后关系意义改变的实证案例 |
| Context 工具使用衰减定律：Agent 工具使用准确率随 context 长度呈对数-线性衰减，~67K token 后跌破 0.80 | extracted | 在 >128K context 场景中找到工具使用准确率不降反升的反例 |
| 认知背离双循环修正模型：六步反馈环——注意↓→AI降委托成本→AI兜底预期效应→推理动机↓→练习↓→技能退化→委托需求↑。AI是加速器非触发器。关键变量：AI兜底预期×推理动机×练习频率×时间间隙×失败可习得性 | extracted | 找到长期高频使用 AI 但注意力和判断力未退化的对照群体；或找到注意力下降在 AI 采用前已停止的纵向数据 |
| **🆕 判断力退化隐蔽性定理**：判断力最易被委托侵蚀——退化比操作技能更隐蔽(无客观"坠机"信号)，练习需求比知识更高，退化信号被AI"看起来合理"的输出掩盖。Macnamara et al. (2024) 直接验证：AI辅助使用者常意识不到技能退化 | extracted | 找到判断力在长期高频AI使用后经客观测试无退化且自我评估准确的群体 |
| **🆕 失败空间迁移不等价定理**：失败的学习价值=f(反馈硬度,因果透明度,自我距离⁻¹,时间窗口)。AI引入的新失败类型"可习得性"结构性地低于被替代的旧失败类型——不是因为失败不够多，而是因为穿过高熵中介 | hypothesis | 新旧失败类型可习得性直接对照实验(反馈清晰度×延迟×可重复性)；找到新失败类型学习效率≥旧失败的案例 |
| **🆕 高熵中介学习衰减定理**：AI作为认知中介，内部状态不透明(不可归因)+不会因失败改变(不可更新)+替你错替你修(自我距离远)→信号穿过中介后"可归因性"和"可更新性"丢失→学习效率系统性下降。类比热力学：高熵中介不可逆地衰减学习信号 | synthesized | 找到AI中介不降低学习效率的案例(如可解释AI+持久记忆+用户主动纠错反馈回路) |

## Source 需求队列

| 优先级 | 目标 | 当前缺口 | 下一步 source | 触发行动 |
|--------|------|----------|---------------|----------|
| P0 | AGI Economics topic | 15 entity 零承载 | 经济学框架性论文（Autor/Acemoglu 最新） | 建 topic skeleton + clip |
| P0 | Output 断层 | 5 output 无法验证 52 新判断 | 07-01/02/03 日志原料充足 | 写 2 个 output |
| P0 | Memory Systems topic | 13 entity 零承载 | 认知心理学记忆模型文献 | 建 topic skeleton |
| P0 | Security & Privacy topic | 16 entity 零承载 | 安全/隐私对标 OWASP | 建 topic skeleton |
| P1 | Token FinOps entity + topic | 3 raw 待编译 | ✅ raw 已到齐 | compile → 建 entity |
| P1 | AI-Native Testing topic | 07-03 roundtable 完成 | ✅ raw 已到齐 | 回填 → 建 topic |
| P1 | AI Governance Regimes comparison | 07-03 roundtable 完成 | ✅ raw 已到齐 | 回填 → 建 comparison |
| P1 | Agent Economic Protocols entity | 2 raw 待编译 | ✅ raw 已到齐 | compile → 建 entity + comparison |
| P1 | Agent Observability topic | 4 entity 零承载 | Datadog/New Relic APM 演化史对标 | 建 topic skeleton |
| P1 | Skill Engineering topic | 5 entity + 07-03 新剪藏 | ✅ Anthropic Skill Engineering 实践 raw | compile → 建 topic |
| P2 | 死 topic 清理（7 个零入链） | 见下方死 topic 清理 | — | 补内容 or 归档 |
| P2 | 长期自主 Agent 权利/责任 | 缺法律/伦理 topic | long-running postmortem 判例 | 追踪法律案例 |
| P2 | Compliance-as-Code for AI | 概念阶段 | EU AI Act 合规自动化工具/案例 | clip + 建 entity |
| P2 | 编译 18 pending raw | 编译速度远落后于剪藏 | 已有 raw | 批量 compile |

## 高杠杆待验证问题

### 从思考未穷尽处

- Token FinOps 能否成为独立的企业软件品类（类似 CloudHealth 之于云成本）？
- Agent Control Plane 独立厂商能否在模型厂商内化之前建立护城河？
- 多模型策略在企业中的实际采用速度——2026/2027 年能否超过 50%？
- 判断力退化的"净退化期"能否被量化——不同判断力类型的时间曲线？
- 模拟训练的"后果真实化"（赌注/公开承诺）能否部分克服大脑的情景/语义分离？
- Exit-Sovereignty 能否被设计为 AI 工具的强制性 affordance（而非可选功能）？
- 中国 AI 采用中"科层碎片化"的结构性根源——是暂时过渡还是体制性永久特征？

### 从盘点新缺口

- Agent 记忆系统能否统一为"编码→巩固→检索→遗忘"四阶段框架？Context-Rot 对应哪一阶段？
- AGI 经济学的核心生成器是什么——Token 成本、劳动力替代率、还是组织学习速度？
- Agent Observability 能否成为独立的 `$10B+` 市场？它的"Datadog 时刻"何时到来？
- 开源 Agent 框架的竞争终局——收敛到协议标准还是产品整合？
- Compliance-as-Code 能否将 AI 治理从"文档合规"升级为"运行时合规"？
- 知识库的 Output 转化率从 7% 提升到 20% 的最小可行动作是什么？
- **🆕 Agent Quality Pipeline 的开源参考实现——类似传统 CI/CD 的 Jenkins/GitHub Actions 等价物？**
- **🆕 Property 不变量库的标准化——常见 Agent 不变量的可复用目录（类似 OWASP Top 10 之于安全）？**
- **🆕 LLM-as-Judge 的长期漂移——6/12/24 月尺度上 judge bias 是否增长？**
- **🆕 CN AI 治理何时从"风暴式执法"过渡到"常规化独立审计"？**
- **🆕 Skill Engineering 能否成为 Agent 时代的"软件工程"——Thin Harness/Fat Skills 的边界在哪？**
- **🆕 新旧失败类型可习得性对照实验**——反馈清晰度×延迟×可重复性，新失败(编排失败/验证遗漏) vs 旧失败(拼写/计算/事实)，学习效率差多少？
- **🆕 AI兜底预期的量化阈值**——"有AI可用"的预期在多大程度上降低推理动机？是否存在递减边界？
- **🆕 摩擦性设计的市场可行性**——主动参与UX能否在效率竞争压力下成为差异化优势而非竞争劣势？
- **🆕 发育关键期不可逆性实证**——AI辅助下未充分构建深度推理回路的儿童，成年后可否通过密集训练重建？
- **🆕 教育评估转向最小可行动作**——从"答案正确性"到"推理过程质量"，哪个教育系统最接近实现？

## 新方向库（07-03 探索扩充）

> 按主题宪法四层面系统盘点可深挖方向。每条含内部锚点、证伪方向、可能落点。优先级 P0=直接服务主问题且有成簇 entity，P1=有锚点待深化，P2=需补 source。

### 软件工程层

| 方向 | 为什么该做 | 内部锚点 | 证伪方向 | 落点 | 优先级 |
|------|-----------|---------|---------|------|--------|
| AI 编程范式下一站 | Software-2.0→3.0→Vibe-Coding→Code-as-Conceptual-Infrastructure 是线性升级还是范式收敛？下一站是 agent 写 agent / 代码作记忆介质？ | Software-2.0/Software-3.0/Vibe-Coding/Code-as-Conceptual-Infrastructure/Git-Fluent-Agents/Agent-Optimized-CLI | 若代码仍主要是人-人沟通媒介、agent 写 agent 不构成独立阶段 | topic | P1 |
| Distillation 与模型经济终局 | 小模型 vs 大模型分工边界；API 蒸馏的合规/商业边界（DeepSeek vs OpenAI） | Adversarial-Distillation/API-Distillation-Catch-Up/Model-Distillation/Specialized-Small-Models/Unified-Model-Strategy/Closed-Frontier-Models-vs-Open-Model-Economy | 若蒸馏被法律封堵或小模型分工不成立 | comparison+topic | P1 |
| Headless Agent 作为新范式 | 无头 vs 有头 agent 分工；HaaS 商业模式；07-02 已有三条件 | Headless-Automation/Headless-Mode/HaaS-Harness-as-a-Service/Thin-Harness-Fat-Skills/Agent-Logic | 若无头只是 CLI 升级非范式 | topic | P1 |
| Benchmark 生命周期与博弈 | benchmark 从发布到被博弈到失效的周期；SWE-Bench 已饱和 | SWE-Bench/CORE-Bench/ITBench/Evaluation-Set/Grindability-vs-Verifiability | 若 benchmark 寿命不随 agent 能力增长而缩短 | topic | P1 |
| 长期自主 Agent 生命周期 | 维护/退化/退役；long-running drift；Agent Logic 已五阶段 | Agent-Logic/Ralph-Loops/Continual-Learning/Recursive-Self-Improvement/Staleness-Problem | 若维护阶段不构成独立工程阶段 | topic | P0 |

### 组织系统层

| 方向 | 为什么该做 | 内部锚点 | 证伪方向 | 落点 | 优先级 |
|------|-----------|---------|---------|------|--------|
| AI 时代组织形态谱系 | AI-Factory/FDE/AI-Ready-Org/Agent-First-Enterprise/Company-Brain 是否同一谱系不同阶段？什么决定选型？ | AI-Factory/Forward-Deployed-AI-Enablement/AI-Ready-Organization/Agent-First-Enterprise/Company-Brain/Organizational-Shape-Moat/Organization-as-Agent-Harness | 若这些不可统一为谱系、选型不可归约 | topic | P0 |
| 多 Agent 系统病态学 | 协调失败模式分类学；Shared-Memory-Contamination 等已立题 | Multi-Agent-System-Pathology/Shared-Memory-Contamination/Coordination-Cost-Three-Layer-Decomposition/Multi-Agent-Pathology-and-Governance | 若病态不可分类为有限模式 | topic | P1 |
| Computer Use 治理与 screen gate | action surface 从 API 扩张到跨界面操作，是否催生独立于 API gate 的 screen gate 新品类 | ACI-Agent-Computer-Interface/Agent-Computer-Interface/Agent-Containment/Agent-Harness | 若 computer use 只是更强工具调用非新治理层 | topic/comparison | P1 |
| 责任架构创新 | 责任在人机间如何分配；H-G-O 已立但责任架构演进未系统化 | Human-Governor-Agent-Operator/Escalation-Based-Human-Oversight/Policy-as-Code-for-Agent-Governance/Custom-Policy-Guardrails | 若责任架构创新无法跟上 agent 自主性增长 | topic | P1 |

### 知识系统层

| 方向 | 为什么该做 | 内部锚点 | 证伪方向 | 落点 | 优先级 |
|------|-----------|---------|---------|------|--------|
| 知识库自身元方法论 | LLM Wiki 四动作模型的有效性反思；output 转化率 7% 的根因 | LLM-Wiki/Knowledge-Compilation/Context-Engineering-vs-Knowledge-Compilation/Obsidian-Wiki/Progressive-Disclosure | 若 wiki 模式不可复用到其他领域 | output | P0 |
| 数据/语料作为基础设施 | 数据层工程化缺失；agent 时代数据层是否独立 | Latent-Knowledge-Demand/Latent-Space-vs-Deterministic/Human-Curation/Deterministic-Retrieval/Corrective-RAG | 若数据工程不构成 agent 时代独立层 | topic | P2 |
| Skill Engineering 工程化 | Thin-Harness-Fat-Skills 边界；skill 作为 agent 时代的"软件工程" | Skill-Chains/Skill-Internalization/Thin-Harness-Fat-Skills/AGENTS-md/CLAUDE-md | 若 skill 不可组合/复用、只是 prompt 模板 | topic | P0 |

### 人的核心价值层

| 方向 | 为什么该做 | 内部锚点 | 证伪方向 | 落点 | 优先级 |
|------|-----------|---------|---------|------|--------|
| AI 社会抵抗与拒绝者 | AI Amish 作为社会选择；技术采用的社会抵抗面 | AI-Amish/AI-Washing/AI-Psychosis/Societal-Resilience/AI-Restraint | 若 AI 拒绝者不构成稳定社会群体 | topic | P2 |
| 认知债务新型态 | AI 加速产生的新型债务；Cognitive-Surrender 已立 | Cognitive-Debt/Cognitive-Surrender/Technical-Debt-Avoidance/Cognitive-Debt-vs-Technical-Debt | 若认知债务可被技术偿还 | comparison | P1 |
| 工作节奏与采用节律 | cadence 作为 adoption 指标是否优于 ROI | Agent-Adoption-Curve/AI-Use-Rhythm/Anthropic-Institute/Amortized-Intelligence | 若 cadence 不能稳定预测 adoption 成败 | topic/output | P1 |
| 智慧工作与剩余价值 | 持续深化——判断力/品味/智慧工作的边界随 AI 能力增长如何移动 | Wisdom-Work/Judgment/Taste/Discernment/Chosen-vs-Seen/Positionality | 若人的剩余价值随 AI 能力增长而消失 | topic | P0 |

## 下一步目标建议与最小实验

> explore-workflow 要求：下一轮最应该推进什么 + 最小可执行动作。

1. **回填 07-03 三轮产出** → 最小实验：用 07-03 日志的"新判断"直接建 AI-Native-Testing topic skeleton + AI-Governance-Regimes comparison skeleton + Open-Source-Agent-Ecosystem comparison skeleton（3 个文件，各 ≤30 行 frontmatter+大纲）
2. **Output 断层破冰** → 最小实验：把 07-02 元合成 rank（四根柱子）转成 1 篇 output，验证 49 条判断能否被四根柱子反生成
3. **记忆系统簇建 topic** → 最小实验：13 个记忆 entity 归入"编码→巩固→检索→遗忘"四阶段框架，建 Agent-Memory-Lifecycle topic skeleton
4. **死 topic 处置** → 最小实验：7 个零入链 topic 逐个判定——补内容承载 / 合并 / 归档，先做 `模型安全分歧`（可整合 16 安全簇 entity）
5. **新方向库 P0 启动** → 最小实验：从 P0 方向（长期自主 Agent 生命周期 / 组织形态谱系 / Skill Engineering / 智慧工作剩余价值）选 1 个启动 ljg-rank 降秩，找不可再少生成器

## 死 topic 清理（07-03 新发现）

> 7 个 topic 零入链（`grep -rl` 全库无引用）。需补内容承载 entity、或归档、或合并。

| Topic | 状态建议 |
|-------|---------|
| `模型安全分歧` | 补承载（安全簇 16 entity 待建 topic，可整合） |
| `Lean-Indie-Engineering` | 补承载 or 归档 |
| `Karpathy-AI-Thought` | 补承载（有 Karpathy/Software-2.0/Software-3.0 entity） |
| `CEO-Hands-On-AI` | 补承载 or 归档 |
| `AI-Mathematics-Future` | 补承载（有 AI-in-Mathematics entity） |
| `AI-Management-Mindset-Transfer` | 补承载（有 AI-Capability-Management-Alignment entity） |
| `Agentic-AI-Ecosystem` | 补承载（可整合 Agent 互操作协议簇） |

## 最近思考结论摘要

> 只保留最近 5 条；更早见 [[exploration-archive-20260628]]。

| 时间 | 焦点 | 临界发现 |
|------|------|---------|
| 2026-07-03 | 记忆双重衰减修正与Context扩展悖论 | 检索干扰>存储衰退在Agent中成立；Context衰减三层修正模型(L1=O(N²)不可压缩⊃L2=attention稀疏化⊃L3=编码-检索不匹配)；完美信号不可达定理(softmax权重总和=1硬约束)；编码策略杠杆(编码1单位=检索10单位节省)；差异化编码=最小成本最高杠杆 |
| 2026-07-03 | 认知背离双循环 | 六步反馈环(注意↓→降委托成本→AI兜底预期→推理动机↓→练习↓→退化→依赖↑)；AI=加速器非触发器；高熵中介不可逆衰减学习信号；断裂点三层因果层级：微观⊂中观⊂宏观(教育评估转向)；成人退化可逆，儿童窗口关闭可能不可逆 |
| 2026-07-03 | AI-native 测试三支柱框架 | 正向(LLM-Judge×多模型×人类校准)+负向(Property×Adversarial)+反馈(快速循环×阈值断言)；金字塔=沙漏形；粒度=f(失败成本)；Agent Quality Pipeline 与 CI/CD 并行 |
| 2026-07-03 | AI 治理三范式比较 | EU(事前/程序俘获)×US(事后/盲区)×CN(集中/风暴执法)；全球标准=多维度碎片化拼图；布鲁塞尔效应在 AI=多中心化 |
| 2026-07-03 | Agent 框架分化定理 | 终局=后端模式分化非前端收敛；差异化=可观测性+状态管理+人机协作；协议标准化后编排 commodity 化 |

## 思考日志索引

- [[2026-07-03]] — 5 轮：记忆双重衰减修正(roundtable+think+联网) / 认知背离双循环(roundtable+think+qa+联网) / AI-native 测试三支柱 / AI 治理三范式 / Agent 框架分化定理
- [[2026-07-02]] — 31 轮含元合成：评测/记忆/灵活性/治理/认知/全球南方/控制平面/AI 认知/Headless/Harness/多 Agent 倒 U/AGI 经济学/中国 AI/元合成 rank/Context Advantage/Goodhart Soros Gödel/重组制度/治理内生性/判断力扰动/后果真实性/Token FinOps
- [[2026-07-01]] — 12 轮：协调/记忆/评测/治理/判断力/经济学/组织/Agent/CU/Reward/动态环境
- [[2026-06-30]] — 全库盘点 + 多轮探索
- [[exploration-archive-20260628]] — 06-28 全库快照 + 方向库 + 长问题库
- [[research-snapshot-20260703]] — 07-03 图谱健康度快照 + 成簇分析 + 缺失领域
- [[resolved-judgments]] — 已收敛判断（06-24 批次 15 条 + 07-02 批次 2 条）
- [[resolved-principles]] — 已收敛操作原则（9 条）
