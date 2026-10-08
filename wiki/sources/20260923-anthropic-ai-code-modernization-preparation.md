---
type: source-summary
title: "How to prepare for AI-driven code modernization projects"
canonical_url: "https://claude.com/resources/articles/how-to-prepare-for-ai-driven-code-modernization-projects"
original_raw_file: "20260923-anthropic-ai-code-modernization-preparation.md"
body_sha256: "74af78546ff51243cf4a749844fd9b95cc50b2a79c044e0eb4195b0417ff4e40"
indexed_at: "2026-10-08T10:22:18+08:00"
raw_state: index
created: 2026-10-08
updated: 2026-10-08
tags:
  - source-summary
  - agentic-engineering
  - software-modernization
  - verification
  - enterprise-ai
evidence_level: medium
claim_type: mixed
source_locator:
  - "Opening + six-step overview — bottleneck shifts from producing changes to mobilizing the organization"
  - "Step 1: Define the target — uplift / transform / reimagine and behavioral-spec boundary"
  - "Step 2: Define the certificate — cumulative machine-checkable evidence and modernization-type-specific oracle"
  - "Step 3: Set the promotion policy — risk-tiered human review, SME allocation, shared responsibility"
  - "Step 4: Put the prerequisites in place — environment, CI/CD, review capacity, security/compliance"
  - "Step 5: Build and refine the agentic workflow — modify the workflow rather than repairing every change"
  - "Step 6: Run the modernization — end-to-end pilot before scale; partition/freeze/gate for in-place uplift"
  - "A note on cost + Beyond the modernization — verification as major cost driver and reusable playbook outputs"
---

# How to prepare for AI-driven code modernization projects

## 编译摘要

### 1. 浓缩

- **核心结论 1：AI 把大规模代码现代化的主要瓶颈从“生成变更”推向“先定义正确性，再让组织能够按生成速度吸收已验证变更”。**
  - Anthropic 将项目拆成六步：target → certificate → promotion policy → prerequisites → agentic workflow → pilot/scale。值得注意的是，真正的 Agent workflow 被放在第五步；前四步先解决目标、证据、上线治理和组织容量。
  - 作者明确指出，关键系统既有 change management / review / approval 流程原本建立在人类写、人类逐 diff 审的吞吐假设上；当 Agent 加速变更生产后，瓶颈转为 mobilizing the organization。
  - **判断**：Agentic modernization 的控制面不是“让更多 Agent 并行改代码”，而是先建立一个能承受高生成吞吐的 **target–evidence–promotion contract**。

- **核心结论 2：certificate 是现代化项目的 correctness contract；不同 modernization type 对应不同 oracle，不能用同一套测试模板。**
  - Uplift 以原系统/原测试为主要 parity oracle；Transform 因跨栈后旧测试往往不能直接复用，更依赖 production replay、differential testing 与 prod-parallel；Reimagine 改变行为，必须锚定 behavioral spec，因 reference 更主观而需要更多模型判断和独立 adversarial review。
  - certificate 的条件应尽量机器可检查，使 Agent 能自动迭代到通过，或在无法通过时升级给人。作者列出的证据包括原/新测试、coverage、performance bound、fresh-context adversarial review、computer use、old/new differential output、state/wire-format round trip、staging telemetry、static/security analysis、build/type checks。
  - **判断**：certificate 的本质不是“测试清单”，而是把“什么算正确”变成可累计、可自动判定的证据合同；reference 越弱，自动化验证上限越低。

- **核心结论 3：promotion policy 把 human review 从逐 diff 审批改成风险分层的稀缺 SME 资源配置。**
  - Anthropic 建议按 blast radius 与 Agent confidence 分级，关键路径保留完整人审；反复出现的 flag 应回到 workflow/certificate 修根因，而不是无限增加人工复核；输出格式应与 reviewer 共设计，使 SME 直接看到高风险变更和被 flag 的 Agent 决策。
  - 对强监管环境，作者强调 promotion policy 要提前由组织层达成，避免某个最终 approver 独自承担系统性风险。
  - **判断**：当生成吞吐远超 review throughput 时，治理重点从“每个变更都由人批准”迁到 **风险分类、证据充分性、升级路径与责任分配**。

- **核心结论 4：大规模现代化是组织/基础设施项目，不是单纯 coding-agent 项目；最有效的修复单元应是 workflow，而非单个 change。**
  - prerequisites 覆盖 remote host、测试容量、生产 telemetry/replay、依赖图、CI compatibility gate、code freeze、跨团队 review capacity、模型访问批准、least privilege、PII/secrets 处理、PR↔Agent transcript↔certificate evidence traceability。
  - Step 5 的关键原则是：小范围 pilot 暴露问题后，应修改 workflow/certificate，使同类错误在规模化阶段系统性消失，而不是让人逐个修每个 Agent change。
  - **判断**：这把“从经验中学习”从 Agent memory 提升为 **workflow-level error correction**：重复失败必须转化为 harness/证书/规则变化。

- **核心结论 5：在受监管现代化中，verification 可能比生成代码更昂贵；成本优化应围绕证据门的排序和模型路由，而不是只压低生成 token。**
  - 作者把 certificate 复杂度、补测试/修测试、并行开发 reconciliation 列为主要成本驱动，并明确指出在 regulated environment 中 verification 往往比 writing the change 占更大份额。
  - pilot 应实测 token usage，重验证信号放到便宜 gate 之后；机械、高吞吐且 certificate 能完全检查的任务可用较便宜模型，复杂 transformation / adversarial review 留给更强模型。
  - **判断**：Agentic modernization 的成本模型应以 **verified change** 而非 generated change 为单位。

### 2. 质疑

- **一手实践但缺少可审计样本**：文章来自 Anthropic Forward Deployed Engineers，声称方法源于客户部署经验，但没有给出项目数量、行业分布、失败项目、前后对照或统计口径；适合支持工程框架，不足以证明六步法具有普遍最优性。
- **“months/weeks” 不是本篇的独立结果**：开头关于多年项目缩短到月/周来自其相关案例链接，本篇没有提供对应基线、代码规模、质量/事故结果，不能把速度提升当作本文自身实证。
- **certificate 仍可能共源失败**：Claude-authored tests、Claude adversarial reviews、Claude computer use 都可能共享模型家族与上下文假设；“fresh context”提高过程独立性，但不等同于 verifier independence。生产 replay、旧系统 differential、静态分析和人类 domain knowledge 仍是重要异质证据。
- **Agent confidence 不是天然可校准风险信号**：promotion policy 建议结合 blast radius 与 Agent confidence，但文章没有给出 confidence 的定义、校准方法或误校准数据；高风险分级不能依赖自报置信度单轴。
- **旧系统不是可靠 ground truth 的同义词**：Transform 中把旧系统行为作为 parity oracle 可以降低迁移风险，但遗留 bug、未文档化例外和错误业务逻辑也会被复制；因此“behavior held constant”是工程选择，不等于旧行为本身正确。
- **组织责任仍不能被 policy 消解**：提前共享 promotion policy 能减少末端 approver 的孤立责任，但监管/法律责任是否能真正共享由组织和制度决定，不能由 workflow 设计自动解决。

### 3. 对标与约束

- **与 [[Verifiable-Agent-Engineering]] 对标**：certificate 提供了一个生产级的“可验证边界”实现：target/reference 决定 oracle，异质检查累积 evidence，不能自动证明时进入 escalation。它进一步说明可验证性必须在 Agent 开始批量生成前设计，而不是生成后的 QA 附件。
- **与 [[AI-Labor-Bottleneck-Shift]] 对标**：本文直接给出企业关键系统的瓶颈迁移：coding throughput 上升后，change management、review capacity、test infrastructure、approval、跨团队 consensus 和 production promotion 成为 binding constraints。
- **与 [[Escalation-Based-Human-Oversight]] 对标**：promotion policy 将人工审查按 blast radius / confidence / flags 分层，本质是软件现代化场景中的例外升级式监督；但 confidence 需要独立校准，receiver/packet/timing 等既有 handoff 边界仍成立。
- **与 [[Agent-Verification]] 对标**：原测试、新测试、differential replay、prod-parallel、telemetry、static/security scans 与 adversarial model review 组成多信号 evidence stack；其中最强价值来自证据异质性，而不是“检查层数”本身。
- **与 [[Skill-Internalization]] / harness learning 对标**：文章要求重复 flag 回到 agentic workflow 或 certificate 修根因，以及 pilot 后优先修改 workflow 而不是每个 change，说明规模化 Agent 系统的学习单元应是可版本化的工作流约束。
- **安全边界**：文章明确要求 modernization workflow 仅写 modernization branches、无 production credentials、敏感数据 scrub/mask，并把每个 PR 链接到 Agent transcript 与 certificate evidence。这意味着大规模代码自治并不要求扩大生产权限。

## 证据边界

- 来源为 Anthropic / Claude 官方 2026-09-23 的 Notes from the Field 实践文章，作者 Jonah Ezekiel、Lexie Tonelli；属于供应商第一方经验总结，且 Anthropic 同时销售 Claude Code 与相关现代化服务，因此 evidence_level 取 medium。
- 可稳定支持：六步工程框架、三类 modernization 与 oracle 差异、certificate/promotion policy 的设计逻辑、prerequisites、安全约束、pilot-first 与 workflow-level correction。
- 不足以独立支持：现代化普遍能从多年降到数周、特定生产率倍数、Claude 相对其他工具的优越性、该流程对所有行业/监管环境均最优。
- canonical URL 当前公开稳定可恢复；Source Summary 已保留 section-level evidence locator，编译完成后 Raw 可按 schema 结算为 `index`。

## 关联概念

- [[Verifiable-Agent-Engineering]]
- [[AI-Labor-Bottleneck-Shift]]
- [[Agent-Verification]]
- [[Escalation-Based-Human-Oversight]]
- [[Agent-Harness]]
- [[Skill-Internalization]]
