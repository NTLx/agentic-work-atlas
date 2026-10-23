---
type: source-summary
title: "Why AI Compute Comes in Rectangles — Erik Bernhardsson, Modal CEO"
canonical_url: "https://www.latent.space/p/modal-d"
raw_state: index
original_raw_file: "20261022-latentspace-modal-d.md"
original_body_sha256: "73131d31855fcf6138f5f510ca67ee28ebffc251f9c19853aee8f32d9576c4f7"
indexed_at: "2026-10-23T11:12:57+08:00"
created: 2026-10-23
updated: 2026-10-23
tags:
  - source-summary
  - agent-infra
  - gpu-compute
  - sandboxes
  - inference
  - forward-deployed-engineering
  - ai-native-organization
evidence_level: medium
claim_type: mixed
source_locator:
  - "Transcript 0:00–13:30：Modal 产品定位、Functions 起源、从旧云组件重建 filesystem/snapshot/autoscaler/scheduler、全球容量池"
  - "Transcript 31:30–39:00：非矩形需求、capacity aggregation、sandboxes 成为约三分之一收入、training / building-block 产品战略"
  - "Transcript 40:30–48:00：sandbox ephemerality、snapshot/fork、agent-harness 与 sandbox 解耦、极端并行 CI/test workload"
  - "Transcript 54:00–57:00：Agent-first SDK/API、旧语法进入模型训练数据导致 deprecation 变难、Agent recommendation benchmark"
  - "Transcript 57:00–61:30：FDE 从约 4 人扩至约 24 人、LLM/GPU performance tuning、现场工作产品化"
  - "Transcript 61:30–66:00：manager/IC、人人写代码、code review 与 CI/CD accountability 的组织观点"
  - "Transcript 1:09:00–1:24:00：capacity prepayment、BYOC、三年矩形 GPU 合同与 bursty demand mismatch、独立 inference provider 的结构性理由"
---

# Why AI Compute Comes in Rectangles — Erik Bernhardsson, Modal CEO

> Latent.Space 于 2026-10-22 发布的 Erik Bernhardsson（Modal CEO）长访谈，完整 revised transcript 从 0:00 到 1:24:00。访谈覆盖 Modal 的基础设施演化、GPU 容量采购、serverless Functions、Agent sandboxes、training、FDE、Agent-first API 与工程组织。公司规模、收入结构、可靠性和团队人数等数字主要来自 CEO 自述，因此适合支持产品架构和经营机制判断，不应作为独立市场份额或性能审计。

## 编译摘要

### 1. AI workload 的核心供需错配不是“有没有 GPU”，而是 **capacity shape mismatch**

Bernhardsson 把 GPU 市场最实际的问题描述为：大量容量按未来 3–6 个月起租、持续三年的固定“rectangle”出售，但多数真实 workload 并不是平坦矩形。推理、Agent、batch 和训练任务会随日内流量、产品增长和突发事件上下波动。

Modal 的答案是把跨云、跨地域容量视为一个全球 pool，再把许多客户的波动需求聚合成更平滑的 aggregate demand。由此，基础设施提供商创造的价值不只是“拥有 GPU”，而是把上游固定、长期、粗粒度的容量合同重新包装为下游即时、弹性、细粒度的计算供给。

更准确的抽象是：

```text
upstream supply
long-lived rectangular GPU commitments
        ↓ capacity aggregation / scheduling
shared global pool
        ↓ temporal multiplexing
bursty customer workloads
(inference / agent / batch / training)
```

**判断**：AI compute provider 的一项核心经济功能是 **capacity-shape transformation**。它类似云计算早期把服务器资本支出变成按需实例，但 Agent workload 又进一步把需求推向更短寿命、更高 burst、更大并行度。

### 2. Agent sandbox 正从“隔离环境”变成一种可编排 compute primitive

Modal 最初的核心是 Functions；Bernhardsson 称 2023 后随着 LLM 从代码补全走向生成完整应用，vibe-coding 公司、background agents 和使用 sandbox 做 RL 的模型团队带来快速增长，sandboxes 当前约占 Modal 收入三分之一。

访谈对下一阶段的描述更重要：

- agent / harness 不必与一个长期 sandbox 一一绑定；
- 一个 Agent 可以控制多个 sandbox；
- sandbox 可以 fork、snapshot、快速恢复；
- 极端情况下甚至可以做到“一条 command 一个短命 sandbox”；
- 测试 setup 做一次 snapshot 后，可以把同一状态克隆到上千 sandbox，并行运行 test suite。

因此 sandbox 不只是一层安全 containment。对 Agent workload 来说，它同时是 **stateful-but-disposable execution unit**：状态可复制，执行环境可销毁，并行度可以快速扩张。

### 3. Snapshot 的价值是降低 parallelism overhead，而不只是加快启动

传统 CI 即使可以分 shard，每个 shard 仍要重复 dependency install、test setup 和环境构建，导致 Amdahl-style overhead。Modal 的构想是：

```text
prepare environment once
      ↓ snapshot
clone N identical execution states
      ↓
run each test / branch / agent action independently
      ↓
discard or preserve selected states
```

这把 snapshot 从“恢复机器”转成了**并行执行的复制原语**。如果 clone/start/stop 成本足够低，很多原本因为 orchestration overhead 不值得并行的任务会进入“massively parallel by default”区域。

### 4. Agent 成为软件消费者后，API 的兼容性约束发生变化

Modal 会运行内部 Agent benchmark，例如让 Agent 自己选择工具部署 Stable Diffusion、启动 sandbox，观察是否能自然选中并正确使用 Modal。Bernhardsson 还描述了一个新问题：模型训练数据中大量存在旧版本 Modal 示例，Agent 因此反复生成旧 syntax，使 feature deprecation 比只服务人类开发者时更困难。

**判断**：当 Agent 变成主要 API consumer，`docs + examples + public code` 不再只是文档资产，而成为未来模型行为的间接训练接口。API lifecycle 因而多出一层 **model-memory compatibility**：已经进入训练语料的旧调用方式不会随着官方文档更新立即消失。

这也解释了为什么 Agent-first developer experience 需要同时管理：

- machine-readable SDK/API；
- examples / skills / docs 的一致性；
- legacy syntax 的兼容期；
- 用真实 Agent 做 tool-selection / task-success benchmark，而不只做人类 DX 测试。

### 5. FDE 的正确终点是把现场优化压回可复用产品

Modal 称其 FDE 团队从年初约 4 人扩到约 24 人。工作包括与客户一起优化 LLM serving、训练 draft model、调 vLLM / SGLang 参数、处理性能问题，并与 research / platform 团队协作。

但 Bernhardsson 同时明确说，这不能长期变成“每个客户优化一次都要人工陪跑”；FDE 与 research 早期需要深入客户，随后必须把重复模式转成 internal tooling 和 self-serve products。

因此该案例强化了 [[Deployment-Product-Flywheel]] 的判据：

```text
customer-specific pain
   → FDE diagnosis / tuning
   → recurring pattern
   → reusable platform primitive
   → self-serve product
```

如果最后一步长期没有发生，FDE 只是高成本服务团队，不是平台学习机制。

### 6. AI-native 工程组织的另一个版本：减少协调 gate，增加自动化正确性基础设施

Bernhardsson 描述 Modal 内部 manager / IC prestige 尽量对等，很多前 manager 回到 IC；包括 CEO 在内的技术团队成员持续写代码，一些非技术成员也开始提交代码。他对 code review 的观点较激进：review 在很多场景可能被用来分散 merge accountability，因此与其把所有变更都堆给人工 reviewer，不如把更多投资放到 CI / CD 和自动验证。

这与 [[AI-Native-Engineering-Org]] 中“生成变便宜后 verification 成为瓶颈”的主线一致，但给出了不同组织选择：不是单纯增加 reviewer，而是尝试让 owner 对 merge 负责，并把低层正确性更多交给自动化系统。

**边界**：这是 Modal 自己的工程文化观点，不应推广为“code review 应取消”。架构变更、安全边界、高风险基础设施与跨团队接口仍需要独立审查；自动 CI 也无法证明 specification 本身正确。

### 7. 独立 inference provider 的结构性理由来自模型 churn + workload pooling

访谈末尾提出：model builder 与 inference provider 长期可能保持分工。模型排名和需求会快速切换，但跨很多模型和客户聚合后的总推理需求相对平滑；独立 provider 可以在模型之间重新分配底层资源，而单一模型实验室容易把容量与自己的模型需求绑定。

这不是已经证明的产业终局，但给 [[Token-Supply-Chain]] 增加了一个 supply-side 解释：网关/路由解决“请求去哪”，而 compute provider 解决“物理容量怎样在模型与时间之间重新分配”。

## 关键事实与自报数据

- Modal 提供 compute + storage，workload 包括 inference、sandboxes、training/fine-tuning、batch 等。
- Bernhardsson 称公司相比约两年前 revenue/users 至少增长约 50×；这是 CEO 粗略自述。
- 2023 年初一个 Stable Diffusion 客户一度贡献约 80–90% revenue，随后客户结构多元化。
- Modal 称近期达到约 four/five nines；没有独立 SLA 数据在本来源中核验。
- Sandboxes 当前约占收入三分之一；属于公司自报业务结构。
- FDE 团队从年初约 4 人扩至约 24 人。
- 公司约 200 employees，约 150 engineers；均为访谈时点自报。

## 前提与局限性

- 自动 Transcript 明确提示 names / wording may contain errors；数字与术语应优先按语义使用，不把疑似转写词当精确专名。
- 访谈主体是 Modal CEO，关于 Modal 性能、可靠性、收入、产品增长和市场结构的判断具有供应商激励。
- “三年 rectangle”描述的是当前 GPU procurement 市场常见结构，不意味着所有云/算力合同都如此。
- Sandbox 约三分之一收入说明需求强，但不能直接证明 Agent sandbox 已成为全行业独立品类。
- Agent benchmark / agent optimization 主要是 Modal 内部实践，没有公开成功率曲线。
- “code review optional”是组织文化选择，不是一般安全建议。
- “独立 inference provider 与 model builder 分离”属于结构性行业判断，未来可能因垂直整合、芯片绑定或资本结构而变化。

## 跨来源综合

- 与 [[Agent-Infra]]：补充 Agent workload 的物理计算层——global capacity pool、ephemeral sandbox、snapshot/fork 和 massively parallel execution。
- 与 [[Agent-Ergonomics]]：Agent-first 工具设计从输出格式扩展到 API lifecycle；训练数据中的旧 syntax 会形成长期 model-memory debt。
- 与 [[Forward-Deployed-Engineer]] / [[Deployment-Product-Flywheel]]：Modal 提供了 infrastructure vendor 的 FDE→self-serve product 回流案例。
- 与 [[AI-Native-Engineering-Org]]：人人可写代码后，review capacity 不能线性扩张；一种组织响应是把更多 correctness 约束编码进 CI/CD，同时保持明确 owner。
- 与 [[Token-Supply-Chain]]：从 token 路由进一步下沉到 compute capacity pooling；模型 churn 越快，资源重分配能力越有价值。

## 编译决策

不新增 `Modal`、`Agent Cloud` 或 `Elastic Agent Compute` Entity。本文的稳定价值已可由 [[Agent-Infra]]、[[Agent-Ergonomics]]、[[Forward-Deployed-Engineer]]、[[AI-Native-Engineering-Org]] 与 [[Token-Supply-Chain]] 承载；单独造新实体会与既有基础设施主线高度重叠。