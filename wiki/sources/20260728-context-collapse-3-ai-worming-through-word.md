---
type: source-summary
title: "Context Collapse, Part 3 - AI Worming through Word"
source_raw:
  - "[[20260728-context-collapse-3-ai-worming-through-word]]"
created: 2026-07-30
updated: 2026-11-28
tags:
  - source-summary
  - agent-security
  - prompt-injection
evidence_level: medium
claim_type: mixed
---

# Context Collapse, Part 3 - AI Worming through Word

> 来源：En Klype Salt（2026-07-28），Håkon Måløy；MSRC 协调披露（144 天协调期），**作者报告披露时仍能复现相关类别**，作者选择类级（class-level）披露。三部曲终篇，系列的理论核心。

## 编译摘要

### 1. 浓缩
- **核心结论1**：作者的受控Word演示显示不可信内容可能随文档生成及后续复用传播；特定修复未覆盖作者后续复现的全部类别
  - 关键证据: 原文Stage 1/2、Impact及Mitigating报告内容完整性受损和下游文档继续承载不可信内容的两阶段PoC；后续复用有条件，并非所有文档必然传播，也没有真实跨组织感染统计。Timeline和Mitigating记载原始PoC措辞已被缓解，后续变体仍复现，作者认可修复降低暴露；2026-07-28时的报告不能当作当前产品状态。作者在144天协调期后选择类别级披露，而非公布完整载荷。
- **核心结论2**：作者提出架构层风险论证：被检查内容参与语义判断
  - 关键证据: Closing thoughts讨论模型同时处理可信请求和不可信数据时的语义判断风险，并用解释器和多层检测器作类比。这是作者架构论证，不是数学不可解证明，也未证明不同能力检测器必然失败、只能用LLM检测或所有系统均无可执行防御。模型外身份、来源、动作合同和资源权限能约束后果而不依赖对任意语义的完美识别。
- **核心结论3**：作者建议按存在剩余风险设计控制并保留文档来源与编辑溯源
  - 关键证据: 作者建议对可能的非零失败风险做好准备，生成文档保留来源和模型编辑信息以辅助追溯。未给出通用失败率，元数据可缺失、受篡改或泄露敏感信息；可信记录、访问控制、版本、撤销和恢复需另行设计。

### 2. 质疑
- **关于"结论1"的质疑**: 传播取决于实际检索、素材选择、编辑权限、审批及再次使用；原文展示可行性而非命中率、传播速度或真实DLP效果。其他可比产品的缓解状态是作者认知，不是系统综述。
- **关于"结论2"的质疑**: 架构论证是原则性命题而非不可能性证明——"无干净解"针对的是纯上下文内检测；系统级设计（意图在上下文之外表达、写权限门禁、双路径验证）可以压缩沦陷率，作者自己也承认微软修复"meaningfully reduce exposure"。论证支持避免仅依赖模型检测，不能确立任何具体系统必然有非零失败率的定理；系统层可移除或约束实际副作用路径。
- **关于数据可靠性的质疑**: 一手研究者报告与披露时间线，未独立复跑或查验实际租户和厂商私有日志。单一生态下的PoC不能证明跨生态传播率或当前状态。

### 3. 对标
- **与 [[Prompt-Injection-Risk]] 的关联**：原文支持共享语义处理风险及部分模型检测的局限；本库此前Gödel类比不是形式证明，不因PoC与作者论证相似便升级为已验证不可解定理。
- **[[Agent-Traps]] 分类对应**：案例涉及不可信输入、编辑副作用及后续复用；六类视角有助于检查不同控制，但不证明六环完整连锁、全部实证成熟度或实际跨组织事故。
- **Morris-II先例**：核对[Cohen等论文v2摘要](https://arxiv.org/abs/2403.02817v2)（v1 2024-03-05，v2 2025-01-30），研究在GenAI邮件助手生态中评估传播风险，并报告特定检测防护的效果；与Word PoC属于不同环境，未作首创判断或普适检测保证。
- **"侵蚀组织决策的信息地基"**: 若篡改经合法工作流静默扩散，受损的是组织赖以决策的信息基础——这是 [[Organization-as-Agent-Harness]] 的攻击面镜像：组织把信息流编译成 AI 运行时，攻击者就通过同一编译过程注入。
- **约束分析（3c）**: 来源与授权可在语义处理之外实施强制控制；provenance有助溯源但非单独安全保证；特定模型升级与产品修复降低风险并不证明覆盖整个类别。

### 证据边界与可迁移实践（2026-11-28）

回核[研究者原文](https://enklypesalt.com/posts/context-collapse-part3-ai-worming-through-word/)及本地Raw的Disclosure status、Timeline、Impact、Mitigating与Closing thoughts。原网页2026-07-30修订时间线；未独立核验后续Word修复。Microsoft 2026-10-12 [Trust-Aware Controls](https://techcommunity.microsoft.com/blog/microsoft-copilot-blog/building-trust-aware-controls-for-ai-differentiated-handling-of-untrusted-conten/4562160)介绍初期外部通信等来源的受限处理架构，不据此推断Word类别已全面解决或仍未缓解。

**本库综合**：生成物和检索材料默认保留其来源属性，不因内部账号生成而自动获更高指令权限；对外部副作用使用独立授权，跨轮持久写入与文档推广分级验收；用合成测试材料检验重复复用、拒绝越权、正常文档编辑效用、来源追踪及撤销恢复。未重跑PoC、未核用户租户或实际传播数据。

### 关联概念
- [[AI-Worm]]
- [[Context-Collapse]]
- [[Prompt-Injection-Risk]]
- [[Agent-Traps]]
- [[Shared-Memory-Contamination]]
