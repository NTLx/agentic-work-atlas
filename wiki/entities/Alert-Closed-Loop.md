---
type: entity
title: Alert Closed Loop
aliases:
  - Alert Closed Loop
  - 告警闭环
  - 风险告警闭环
definition: "AI 发出风险信号后，经由通知、责任人接收、人类评估、干预到复盘的完整责任链；闭环之外，模型输出不产生结局价值"
created: 2026-07-30
updated: 2026-07-30
tags:
  - ai-deployment
  - organizational-change
  - healthcare-ai
related_entities:
  - "[[Escalation-Based-Human-Oversight]]"
  - "[[AI-Deployment-Valley-of-Death]]"
  - "[[Integration-Wall]]"
  - "[[Input-Output-Outcome]]"
  - "[[Agent-Observability]]"
source_raw:
  - "[[20260729-nejm-ai-triggered-rapid-response-mortality]]"
evidence_level: medium
claim_type: mixed
---

# Alert Closed Loop（告警闭环）

> [!definition] 定义
> **Alert Closed Loop（告警闭环）** 是 AI 系统发出风险信号之后的完整责任链：风险识别 → 通知 → 责任人接收 → 人类评估 → 干预 → 复盘。模型输出只是闭环的入口；结局价值在闭环内部产生。预警系统的真正产品不是一个风险分数，而是这条闭环。

## 核心逻辑

大量 AI 部署失败不是模型性能（AUC、准确率）不够，而是信号停在"发出"这一步。闭环的每个节点都是潜在断点：

1. **识别**：模型持续计算风险（如 Epic Deterioration Index 每 15 分钟用 EHR 数据重算）。
2. **通知**：达到阈值时自动通知预设责任方；通知的时机与频率本身是设计变量。
3. **接收**：有明确的人类 owner，且他真的看到、有权处置。
4. **评估**：专家判断——信号是判断的输入，不是判断的替代。
5. **干预**：行动发生，且下游资源（如 ICU 容量）能吸收增量。
6. **复盘**：结局与工作量监控回流，调整阈值、通知规则与流程。

## 关键数据点

- NEJM AI（2026）RWJBarnabas 研究：闭环建立（EDI + EHR 集成 + 自动 RRT 通知 + 培训 + 持续监控）后，高风险患者院内死亡率 23.1% → 18.6%，风险校正优势比下降约 18%，RRT 激活率 25.3% → 37.5%，而 ICU 转入率未显著上升——闭环运转没有压垮下游容量。
- 研究高级作者归因："The mortality benefit was not produced by an algorithm but by the partnership around the algorithm"（死亡率获益不是算法生产的，而是算法周围的协作生产的）。
- 闭环的典型失败模式：告警无明确责任人、告警时机不当、告警疲劳（alert fatigue，告警过多导致人类忽略）、未嵌入既有系统与排班、缺乏跨站点标准化、无结局与工作量监控。

## 前提与局限性

- **闭环各环节不可单独拆解归因**：RWJBarnabas 研究是观察性的，闭环各环节的贡献未被单独测量（无消融实验）；"组合起效"是作者归因，不是分解测量。
- **闭环节点的基建是组织投资**：RRT 建制、EHR 集成、培训、监控构成部署成本的主体；"只开通模型"的边际成本很低，但单独不产生效果。
- **六节点结构的一般化是综合判断**：从单一临床案例外推到一般 AI 部署；与软件 Agent 部署的失败模式结构同构（见来源摘要的对标分析），但尚无跨域测量证据。
- **复盘节点最容易被裁掉**：许多部署止步于"干预"，不监控告警假阳性率与工作量增长；告警疲劳会从通知节点开始腐蚀整条闭环。
- **责任主体清晰度决定闭环强度**：临床场景责任主体明确（RRT）、时间性强，闭环较完整；责任主体模糊的办公场景中，"接收"节点会首先失效。

## 关联概念

- [[Escalation-Based-Human-Oversight]] — 闭环是例外升级式监督的运行形态：AI 处理常规，人类接手例外。
- [[AI-Deployment-Valley-of-Death]] — 死亡谷里死掉的项目，多数死在闭环的某个节点，而不是死在模型。
- [[Integration-Wall]] — 通知与接收节点必须嵌入既有系统（EHR、排班、CI/on-call）才能存在。
- [[Input-Output-Outcome]] — 闭环是把输入（风险分数/生成量）转换为结局（死亡率/业务结果）的转换装置。
- [[Agent-Observability]] — 复盘节点依赖对系统行为与结局的可观测性。
