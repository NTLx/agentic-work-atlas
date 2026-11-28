---
type: entity
title: Software-Factory
aliases:
  - Software Factory
  - 软件工厂
definition: "Agent 驱动的软件生产系统：把可程序化、可验证的软件任务组织为可持续运行的 Agent 流水线，覆盖从问题输入到构建、测试、部署与维护的多个环节；人类角色从逐步操作转向目标定义、验证、风险决策与例外处理。"
created: 2026-08-13
updated: 2026-11-28
evidence_level: medium
claim_type: mixed
tags:
  - agentic-engineering
  - organization
  - automation
related_entities:
  - "[[Agent-Development-Lifecycle]]"
  - "[[Agent-Orchestration]]"
  - "[[Agent-Verification]]"
  - "[[Agent-Unit-of-Work]]"
  - "[[Machine-Readable-Processes]]"
  - "[[Agent-Legibility]]"
source_raw:
  - "[[20260804-agent-development-lifecycle-adlc]]"
  - "[[20260804-astro-software-factory-issue-triage]]"
  - "[[20260805-how-we-use-ai-cloudflare-os]]"
  - "[[20260828-uber-software-factory]]"
  - "[[20260914-anthropic-test-impact-analysis-ci]]"
  - "[[20260915-openai-software-factory]]"
---

# Software-Factory（软件工厂）

> [!definition] 定义
> **Software Factory** 是 agent 驱动的软件生产系统：把可程序化、可验证的软件任务组织成持续运行的流水线，可覆盖从问题输入到构建、测试、部署与维护的多个环节。人类通常从逐步操作迁移到目标与边界定义、验证、风险决策和例外处理；实际自动化范围取决于任务可复现性、验证能力与组织基础设施。与 [[Agent-Development-Lifecycle|ADLC]] 互为表里——ADLC 是生命周期范式，Software Factory 是建立在该范式之上的生产架构。

## 关键机制

### 输入输出全链委托
- 输入：production error / customer bug report / feature idea
- 输出：已修复、已预览、已部署、已维护的软件
- 关键：围绕可验证的工作单元扩展委派范围，而非预设全流程无需人工；明确可达权限、停机、结果验收和例外责任。

### 平台七项设计目标（Cloudflare, 2026-08-04）
1. **Programmatic**——ClickOps 对 agent 是 non-starter，一切操作要有 API
2. **Horizontally scalable**——每个 agent 有与生产一致的独立 preview
3. **Reproducible**——4G 模拟 / 地理 IP 类 bug 需能复现
4. **Real-time, push-based**——事件触发 agent 而非等人盯 dashboard
5. **Atomic**——每个变更独立可测/可发布/可观察/可回滚
6. **Permissioned**——agent 能 escalte 获得更多权限以完成工作
7. **Self-improving**——agent 从经验中学习（像人从 on-call 中学习）

### 案例：Astro 的 issue triage 工厂（2026-08-04）
- 分阶段子代理串行（reproduce → diagnose → verify → fix），通过 `report.md` 传递发现；隔离是降低强行修复偏见的设计，不证明错误独立
- 状态外置在 issue labels 和 comments（`triage needed` → `fix verified`）；无本地持久状态不等于无状态系统
- 作者报告 open issues 200+ → ~30（约85%下降）；5+ 年首次达到零是当时的预测而非结果；存量下降不能单独识别解决率、漏诊或新问题流入
- 失败诊断：不透明抽象、缺文档和测试不足是维护者提出的候选原因；另需检验模型、权限、上下文和环境差异。补丁预览经 reporter 确认才开关联 PR，不等于已合并或生产部署

### 案例：Uber 的托管 Agent 车队与成本控制（2026-08-28）
- **规模化对象**：超过 70% 的 pull requests 归因于本地或云 Agent；已构建 3,600 多个 Agent skills，每日执行超过 30,000 次；2026 年 2 月至 8 月，周活跃用户增长 7 倍、周 Agent 请求增长 9.4 倍，而总 AI 支出自 4 月起相对稳定。
- **管理方式**：把 code review、自愈 CI、E2E PR 视觉验证、on-call 分诊、bug 调试和代码维护等工作迁入 managed agents；每个 Agent 用真实工作构建 benchmark，在统一 harness 中比较模型，并按完成任务成本、输出质量和可靠性选择 Pareto 最优模型。
- **成本控制面**：统一 MCP gateway、按需工具搜索、CLI tool resolution、code-mode、prompt cache TTL、实时花费计数和 session anti-pattern dashboard 共同减少 schema、轮询、上下文重传和错误循环。
- **重要判断**：当 Agent 从“工程师交互式助手”变成“托管车队”后，软件工厂的核心能力从生成代码转向管理任务分配、验证基准、上下文供给和单位完成成本。
  - **证据**：[[20260828-uber-software-factory]]（“Introduction”“Benchmark-Driven Model Selection”“Conclusion”）。
  - **边界**：规模、成本与质量数据均为 Uber 自报；这套收益依赖其代码库、MCP gateway、数据图谱和内部 harness，不能直接外推到一般团队。

## OpenAI/Anthropic：软件工厂的两个新瓶颈（2026-09）

**判断**：软件工厂的扩大不是“多生成代码”，而是把长程 Agent、风险分层、CI/测试新鲜度、部署观察和生产反馈连成可回退闭环。

- **证据**：[[20260915-openai-software-factory]]、[[20260914-anthropic-test-impact-analysis-ci]]。
- **边界**：OpenAI 材料是付费外部报告且只呈现部分内容；Anthropic 数据来自内部自报；两者都不能直接代表一般团队的收益。

## 关键数据点

- Astro：200+ → ~30 open issues；Cloudflare OS：25 万问题 / 1.6 万 merges / 4000 apps（[[20260805-how-we-use-ai-cloudflare-os]]）
- Cloudflare：SDLC 七阶段全映射到自家栈（Vite/Rolldown → Browser Run/Vitest → Flagship/Gradual Deployments → Logs/Agent Traces/MCP/Analytics）
- Uber：固定模型后，每 1,000 次模型请求成本较峰值下降近34%，每 session 成本较2026年6月峰值下降52%；这两个分母不是成功完成任务。5次相同SQL查询的同session路径比较支持特定场景 token 开销下降超过50%，批量超过90%为作者报告；不等于总货币成本或正确率同比下降
- Uber AI Context Graph：2,400 万节点、8,000 万条边，覆盖 86 类节点与 117 类边；一个有 grounding 的案例 38 秒完成，未 grounding 的 Agent 用时 20 分钟后仍错误判断数据集不可查询

## 前提与局限性

- **可复现性前提**：自动修复应具备足够可信的复现或其他独立证据；依赖真实环境的 bug 可能需环境模拟、观测、人工补证或受控诊断，而非必然不可自动化
- **vendor 叙事**：Cloudflare 的七项需求与栈映射来自平台发布文，自家狗粮=自家卖点，复制需剥离
- **可靠性边界**：没有从某个通用成功率到全流程自治的已证实阈值；应区分成功概率、失败代价、可检测性与外部影响
- **社区副作用**：客服式 bot 回复可能制造"维护者与用户的新隔阂"，Astro 自评"更多但更有用的对话"未经独立验证
- **企业规模边界**：Uber 的收益同时依赖统一 gateway、内部数据图谱、托管 Agent 和真实工作 benchmark；缺少这些基础设施时，单独复制某一个 CLI、缓存或模型路由技巧不一定产生同等效果

## 关联概念

- [[Agent-Development-Lifecycle]] — 工厂的生命周期范式（SDLC 的 agent 版）
- [[Agent-Orchestration]] — 工厂的编排层（Workflow / Flue 状态机 / 隔离子代理）
- [[Agent-Verification]] — 工厂的验证环节（isolated subagents 反 LLM 偏见）
- [[Agent-Unit-of-Work]] — 工厂的任务粒度控制参数
- [[Machine-Readable-Processes]] — 标签驱动状态机是流程显式化的最小实现
- [[Agent-Legibility]] — Agent 失败可触发可读性诊断，而非证明代码库不可读
- [[Agentic-Workflow-Token-Efficiency]] — 工厂的单位任务成本与 token/工具/上下文优化
- [[Agent-Harness]] — 托管 Agent 车队依赖统一的执行、工具和状态运行时
