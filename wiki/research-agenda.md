---
type: research-agenda
title: "Agentic Work Atlas 研究议程"
created: 2026-05-22
updated: 2026-06-02
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
  - "[[Organization-as-Agent-Harness]]"
  - "[[Forward-Deployed-AI-Enablement]]"
  - "[[Enterprise-AI-Factory]]"
  - "[[Human-Governor-Agent-Operator]]"
  - "[[The-GenAI-Divide]]"
  - "[[Enterprise-AI-Learning-Gap]]"
  - "[[AI-Deployment-Valley-of-Death]]"
  - "[[Successful-AI-Deployment-vs-GenAI-Divide]]"
  - "[[Multi-Agent-Pathology-and-Governance]]"
  - "[[Model-Safety-Divergence]]"
  - "[[Agent-Containment]]"
---

# Agentic Work Atlas 研究议程

> [!note] 使用边界
> 本页维护当前最值得验证的问题、反例、source 需求和下一步动作。它不作为事实页；稳定结论必须回填到 entity、topic 或 comparison，并能追溯到 raw source。

## 当前研究焦点

| 焦点 | 为什么现在重要 | 当前状态 | 下一步动作 |
|------|----------------|----------|------------|
| Output 回填机制 | `produce(query)` 会自然生成新判断，需要防止 output 污染稳定知识层 | 回填检查已经有实践样本，但外部参照不足 | 找团队如何用文章、报告或 decision memo 反向更新知识库的案例 |
| Operator 到 Governor 迁移 | AI 赋能可能不是减少人，而是把人从执行节点移到治理层 | 作为探索性诊断框架保留，证据不足 | 用两个部署案例测试“执行动作 / 治理动作 / 责任 owner / 可复用资产”四列表 |
| 内部 AI Factory 与外部 FDE 分工 | 企业部署能力可能内部化，也可能继续依赖高接触部署 | 已有 [[AI-Factory-vs-Forward-Deployed-AI-Enablement]]，但缺同类工作流对比案例 | 找企业内部平台团队、外部 FDE、自助 SaaS Agent 的对比案例 |
| 标准产品 / FDE / AI Factory 的边界 | 新剪藏同时支持标准产品成功案例、成功部署样本和 GenAI 失败漏斗，需要解释三者何时成立 | 已有 [[Successful-AI-Deployment-vs-GenAI-Divide]]，但缺同一工作流的路径对照 | 做三路径案例矩阵：标准 SaaS/API、外部 FDE、内部 AI Factory |
| 多 Agent 组织病治理 | Multi-agent 不只是技术编排，也会产生责任稀释、内态失真和不可见权力 | 当前证据主要来自二手综述和少量概念页 | 优先补一手论文和生产级 observability 工程复盘 |
| 模型安全行为分歧 | 自治系统中的过度合规、过度行动、行动不足可能需要不同 containment | 当前 [[Model-Safety-Divergence]] 证据层级不足 | 找 Emergence AI 原论文或详细实验报告 |

## 活跃假设

| 假设 | 当前支撑 | 风险 | 处理 |
|------|----------|------|------|
| Output 是 Wiki 的压力测试 | [[Knowledge-Compilation]]、多次 output 回填实践 | 主要来自本库实践，缺外部 source | 保留为工作流假设，不升级为事实 entity |
| Research agenda 只能支撑“待研究问题存在” | Schema 边界规则、本页使用边界 | 后续 output 可能误把本页当事实来源 | 所有回填检查必须区分 Raw / Wiki / Agenda / 无 |
| FDE 的核心价值是现场到能力沉淀 | [[Forward-Deployed-AI-Enablement]]、[[Deployment-Product-Flywheel]]、[[Integration-Wall]] | 标准化 SaaS Agent 可能绕过高接触部署 | 主动寻找无需 FDE 也能改写核心工作流的反例 |
| 内部 AI Factory 不必然替代外部 FDE | [[Enterprise-AI-Factory]]、[[AI-Factory-vs-Forward-Deployed-AI-Enablement]] | 缺少同一工作流的成本、风险和复用路径对比 | 找企业内部团队与外部部署团队的对照材料 |
| 标准 AI 产品能改写核心工作流，但需要组织已具备可读流程和集成基础 | [[Successful-AI-Deployment-vs-GenAI-Divide]]、[[AI-Ready-Organization]]、Klarna / Mercado Libre / Lightspeed raw | 可能把“工具 adoption”误判为“工作流改造”；也可能低估供应商侧隐藏实施工作 | 对标准产品案例补 source-summary，检查是否有 API 化系统、业务 owner、指标闭环和人类升级路径 |
| Enterprise AI Learning Gap 可能是产品问题，也可能是组织问题 | [[Enterprise-AI-Learning-Gap]]、[[The-GenAI-Divide]]、[[AI-Ready-Organization]] | 如果学习鸿沟主要由产品内存/集成能力解决，FDE 和组织重构的重要性会下降 | 找学习型 AI SaaS 在低咨询条件下跨过 production 的案例 |
| Multi-agent 系统会产生组织病 | [[Multi-Agent-Pathology-and-Governance]]、[[Invisible-Orchestrator]]、[[Agent-Dissociation]] | 证据可能过度依赖二手叙述 | 补 Hidden Profile、MAEBE、invisible orchestrator 等一手论文 |
| 模型安全分歧反映底层信任结构 | [[Model-Safety-Divergence]]、[[Agent-Containment]] | 新闻摘要不足以支撑强解释 | 找原论文、实验日志或同基准复现实验 |
| Operator 到 Governor 迁移可作为 AI 赋能成熟度观察指标 | [[Human-Governor-Agent-Operator]]、[[AI-Ready-Organization]]、[[Organization-as-Agent-Harness]] | 可能把治理上移误判为成熟，忽略 operator 经验和高风险流程边界 | 仅作为探索性诊断，不建新 entity |

## 待证伪判断

- **标准化 SaaS Agent 会削弱 FDE 必要性**：寻找无长期驻场、无咨询、无高接触部署，却改写企业核心工作流的案例。
- **标准产品成功案例可能只是低集成边缘流程**：寻找标准 SaaS/API 改写强权限、强合规、强遗留系统核心流程的案例；如果找不到，标准产品反例的适用范围要收窄。
- **外部合作成功率高可能是选择偏差**：寻找项目难度、预算、流程清晰度相近的内部自建 vs 外部合作对照案例。
- **学习鸿沟可以完全靠产品记忆解决**：寻找无需组织流程显式化、仅靠产品内存和上下文学习就稳定进入生产的案例。
- **例外升级式监督是通用最佳实践**：寻找高风险流程中 80/20 自动化导致事故、责任漂移或审计失败的案例。
- **内部 AI Factory 会替代外部 FDE**：寻找内部 AI 平台成熟但仍高度依赖外部 FDE 的案例。
- **多 Agent 组织病必须通过内态记录才能治理**：寻找只靠外部 harness、日志和审计就能长期稳定运行的生产系统。
- **不可见编排一定有害**：寻找不可见编排提升质量或安全，且影响链条可审计、责任不稀释的案例。
- **过度合规本身是安全风险**：寻找 Claude 或类似模型在自治环境中做出合理但违规判断的案例。
- **大胆模型必然发散**：寻找 Grok 或类似高行动倾向模型在自治环境中稳定收敛的案例。
- **Operator 到 Governor 迁移是 AI 赋能成熟必要条件**：寻找核心工作流被 Agent 稳定改写，但人类仍主要停留在 operator 位置的成功案例。
- **Governor 上移一定更高级**：寻找人类过早脱离 operator 经验导致治理空心化、误判异常或验收失败的案例。
- **Output 回填检查足够轻量且有效**：继续收集“清楚但不应升级”的 output 判断，检验回填规则是否真的降低页面膨胀。

## Source 需求队列

| 优先级 | 目标 | 当前缺口 | 下一步 source | 触发行动 |
|--------|------|----------|---------------|----------|
| P0 | 提升 [[Model-Safety-Divergence]] 证据层级 | 缺一手论文或详细实验报告 | Emergence AI / Satya Nitta 原论文、实验日志或详细报告 | clip 后更新 [[Model-Safety-Divergence]] 的前提与局限性 |
| P0 | 验证 Operator 到 Governor 迁移 | 缺一手组织案例 | Agent-first / FDE 项目中角色、权限、验收和责任变化的深度复盘 | clip 后更新 [[Human-Governor-Agent-Operator]] 或新建 comparison |
| P0 | 补强多 Agent 组织病 | 缺一手论文 | Hidden Profile、MAEBE、persona collapse、bystander effect、Fukui invisible orchestrator、MetaAgent-X 原论文 | clip 后更新 [[Multi-Agent-Pathology-and-Governance]] |
| P0 | 编译标准产品成功案例 | Klarna / Mercado Libre / Octopus / Lightspeed 已剪藏但未 source-summary 化 | 官方案例、客户故事、后续复盘、是否有内部系统/API 集成细节 | compile 后更新 [[Successful-AI-Deployment-vs-GenAI-Divide]] 和 [[Forward-Deployed-AI-Enablement]] |
| P0 | 建立三路径对照 | 缺同一工作流在标准产品、外部 FDE、内部 AI Factory 下的成本和结果对比 | 客服、研发、back-office 三类工作流的成对案例 | 证据足够后新建或扩展 comparison |
| P1 | 对比内部 AI Factory 与外部 FDE | 缺同类工作流对比 | 企业内部 AI 平台团队与外部 FDE 服务同类流程的案例 | 证据足够后更新 [[AI-Factory-vs-Forward-Deployed-AI-Enablement]] |
| P1 | 验证外部合作成功率的选择偏差 | MIT/NANDA 称外部合作成功率更高，但缺项目难度控制 | 内部自建和外部合作在相同流程/行业/预算下的失败复盘 | 更新 [[The-GenAI-Divide]] 的前提与局限性 |
| P1 | 学习型 AI SaaS 是否绕过 FDE | 缺“产品内存 + workflow integration”直接跨过 production 的案例 | Intercom Fin、Glean、ServiceNow、Salesforce Agentforce 等官方客户深度案例 | 压力测试 [[Enterprise-AI-Learning-Gap]] |
| P1 | 设计 multi-agent observability 指标 | 缺工程实践 | reason change、disagreement、input rewrite、final authority、handoff trace 的记录实践 | compile 后更新 [[Verifiable-Agent-Engineering]] |
| P1 | 验证标准化 SaaS Agent 反例 | 缺无 FDE 高接触部署的成功案例 | SaaS Agent 自助改写核心工作流的企业案例 | clip 后压力测试 [[Forward-Deployed-AI-Enablement]] |
| P1 | 建立 output 回填外部参照 | 缺一手实践 | 团队如何用文章、报告、decision memo 反向更新知识库的案例 | 更新 [[Knowledge-Compilation]] 或新建 comparison |
| P2 | 判断纯 Markdown LLM Wiki 规模边界 | 缺工程数据 | GBrain、Obsidian-Wiki 或类似系统的检索、图谱、文件精读实现细节 | 更新 [[Agent-Knowledge-Management]] |
| P2 | 定义知识层面的 audit 指标 | 缺质量标准 | 知识库证据回链、冲突检测、概念去重、过时判断的实践材料 | 更新 lint / audit 工作流 |
| P2 | 防御行动不足型 Agent 崩溃 | 缺失败模式文献 | Agent 系统中遗忘生存、行动不足、最低生存行为的失败模式和防御策略 | 更新 [[Agent-Containment]] 或新建 comparison |

## 下一步最小实验

### Operator / Governor 诊断表

选两个已有部署主题，优先使用 [[Forward-Deployed-AI-Enablement]] 和 [[Enterprise-AI-Factory]]。

| 案例 | 执行动作 | 治理动作 | 责任 owner | 可复用资产 |
|------|----------|----------|------------|------------|
| 待填 | 待填 | 待填 | 待填 | 待填 |

要求：
- 只填 source 明确支持的内容。
- 无法填写的格子记录为 source 缺口。
- 如果两个案例都能填出相似结构，再考虑升级为 comparison 或补充 [[Human-Governor-Agent-Operator]]。

### 标准产品 / FDE / AI Factory 三路径矩阵

选同一类工作流，优先从客服、研发和 back-office 各找一个案例，填入三条路径。

| 工作流 | 标准 SaaS/API 路径 | 外部 FDE 路径 | 内部 AI Factory 路径 | 关键差异 |
|--------|--------------------|---------------|----------------------|----------|
| 客服 | Klarna / Lightspeed 待编译 | 待找 | 待找 | adoption、集成深度、升级路径、P&L 指标 |
| 研发 | Mercado Libre / Copilot 待编译 | 待找 | 待找 | license 下发 vs 流程重构 vs 平台化 |
| back-office | 待找 | 待找 | P&G / AI Factory 相关 | BPO 替代、数据接入、审计和复用资产 |

判断标准：
- 是否有明确业务指标，而不是只看使用率。
- 是否有核心系统/API 集成，而不是只做前端助手。
- 是否有组织学习资产：评测集、流程规范、升级规则、模板或平台模块。
- 是否有明确人类角色迁移：operator、reviewer、governor、owner。

最小动作：先把 Klarna、Mercado Libre、Lightspeed 三篇标准产品案例补成 source-summary，再用这个矩阵压力测试“标准产品绕过 FDE”的假设。

### Model Safety 证据升级

1. 搜索 Emergence AI / Satya Nitta 原论文或详细实验报告。
2. 若找到，编译为 source-summary。
3. 对照 [[Model-Safety-Divergence]] 中的数据点，标注哪些来自一手实验，哪些来自新闻摘要。
4. 若找不到，在 entity 的前提与局限性中明确降级证据强度。

### Multi-Agent 组织病证据分级

1. 选择一个一手论文，例如 Fukui invisible orchestrator。
2. 编译为 source-summary。
3. 对照 [[Invisible-Orchestrator]]、[[Agent-Dissociation]] 和 [[Multi-Agent-Pathology-and-Governance]]。
4. 将二手转述、论文实证、工程类比分层标注。

### Output 回填负面样例收集

1. 从每篇新 output 的回填检查中抽取“清楚但不升级”的判断。
2. 标注原因：缺 raw source、只出现一次、已有页面承载、只是表达修辞。
3. 累积到 5 个以上样例后，更新 Output 回填门控。

## 待验证问题

- **编译质量如何衡量**：除了链接、frontmatter 和裸符号检查，还需要什么知识层面的质量指标？
- **输出如何反向回填**：一篇 output 中产生的新判断，什么情况下应升级为 entity、topic 或 comparison？
- **探索如何避免污染事实层**：未验证假设应保留多久，何时删除、归档或转为正式页面？
- **研究议程如何衰减**：长期未被 source 支撑、未被 output 使用的问题，是否应定期删除或归档？
- **支撑层级如何标注**：回填检查是否需要区分 raw source、Wiki 页面和 research agenda 三种不同证据强度？
- **多 Agent 组织病如何评测**：最终答案正确时，是否还需要检查 reason change、disagreement、monologue ratio 或 input rewrite？
- **内部 AI Factory 与外部 FDE 如何分工**：企业什么时候应该内部化部署能力，什么时候仍需要外部 FDE？
- **不可见编排能否被治理**：透明化是否必须牺牲效率，还是审计日志足以降低风险？
- **Operator 到 Governor 的迁移是否可测量**：AI 赋能成熟度能否通过执行动作、治理动作、责任 owner 和可复用资产四列来诊断？
- **Governor 是否需要 Operator 经验**：脱离一线执行经验的人类治理者，是否会更容易误判 Agent 输出和流程异常？
- **Governor 橡皮图章化风险**：审批流是否会因为 Agent 输出量过大而退化为形式性通过？
- **过度合规是否是安全风险**：零异议的自治系统在面对规则间隙时是否更脆弱？
- **沉默型崩溃需要什么 containment**：行动不足和行动过度是否需要不同的防御架构？
- **反馈回路能否中途反转**：least-agency 约束是否能在发散循环锁定前改变轨道？

## 下一批剪藏方向

- Karpathy 关于 LLM Wiki、Software 3.0、Agentic Engineering 的一手材料。
- AI Agent 开发、Agent Harness、验证、工具使用和上下文工程的一手工程实践。
- GBrain 或类似系统的工程实现细节，特别是混合检索、完整文件精读和图谱加权。
- Obsidian-Wiki / Skills 类系统如何把工作流封装成 Agent 可执行能力。
- 知识编译质量评估方法：冲突检测、证据回链、概念去重、过时判断。
- 输出驱动的 Wiki 演化案例：文章、报告或决策 memo 如何反向更新知识库。
- 标准化 AI 产品绕过 FDE 式高接触部署的反例案例。
- 标准 SaaS/API、外部 FDE、内部 AI Factory 处理同类工作流的对比案例。
- 学习型 AI SaaS 的深度客户案例，尤其是产品记忆、流程集成、例外升级和 P&L 指标。
- 企业 AI 外部合作成功率是否受选择偏差影响的失败复盘。
- Multi-Agent 组织病的一手论文和工程复盘。
- 企业内部 AI Factory 与外部 FDE 的对比案例。
- 生产级 multi-agent observability、reason tracing 和 disagreement logging 实践。
- Agent-first 流程重构中的人类角色迁移案例：从 operator 到 governor 的组织设计、权限边界和验收标准。
- 高可靠系统中的 human-in-the-loop / human-on-the-loop 案例，用来校准 AI Agent 治理边界。

## 已收敛的操作原则

- 不新增 `explore/`、`audit/`、`claims/` 等目录。
- Research agenda 只能记录问题、假设、反例和 source 需求，不作为事实判断证据。
- Output 文件必须包含回填检查；没有 raw source 支撑的新判断默认不升级。
- 对清楚但证据不足的判断，优先补 source 或放在本页，不直接新建 entity。
- 探索文档不再按时间流水账组织；Git history 已经负责记录操作时间线。

## 暂不做

- 不引入向量数据库或自动调度。
- 不把一次性问题写成稳定知识页。
- 不为探索结果设计复杂模板。
- 不把本页作为 output 事实判断的支撑来源。
