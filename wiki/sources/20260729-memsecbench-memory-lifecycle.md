---
type: source-summary
title: "MemSecBench: Tracking Agent Memory Poisoning from Persistence to Consequence and Repair"
source_raw:
  - "[[20260729-memsecbench-memory-lifecycle]]"
canonical_url: "https://arxiv.org/abs/2607.27080"
raw_state: full
source_locator:
  - "310 cases / 48 contexts / 24 stack configurations"
  - "Write–Execute–Forget lifecycle and seven checkpoint adjudication"
  - "§Evaluation Metrics / Fig. 4: configuration macro-average MPSR 84.2%, E2E-ASR 50.3%, SRSR 56.1% conditional on successful poisoning"
created: 2026-09-19
updated: 2026-11-28
tags:
  - source-summary
  - agent-security
  - verification
evidence_level: high
claim_type: mixed
---

# MemSecBench: Tracking Agent Memory Poisoning from Persistence to Consequence and Repair

## 编译摘要

### 1. 浓缩

- **核心结论 1：memory 安全必须按生命周期测，而不能只测是否“写进去了”。**
  - 关键证据：310案例×24配置（OpenClaw/Hermes，Native/Mem0/Mem0-Graph/A-MEM，3 LLM），每配置-案例只运行一次；Write通过后，从同一已验证污染状态分别进入Execute与Forget分支，而非先完成外部动作再修复。七检查点W1写入、W2持久化、E1召回、E2采纳、E3外部化、F1修复、F2正常记忆保留。
- **核心结论 2：memory backend / harness / model 的组合会显著改变传播与修复。**
  - 关键证据：Table 2/Fig. 4报告配置宏平均MPSR 84.2%、E2E-ASR 50.3%（全案例）；MESR 59.6%、SRSR 56.1%（各配置成功污染案例为分母）。OpenClaw/DeepSeek-V4-Pro替换Native为A-MEM时E2E 59.0→56.5%、SRSR 46.3→87.6%；Hermes/MiniMax-M3换Mem0时E2E 34.8→48.7%、SRSR 47.3→60.0%。描述性对照、条件分母及样本组成不同，非后端通用排名或独立因果效应。
- **核心结论 3：删除恶意 memory 与恢复所有后果是不同问题。**
  - 关键证据：Fig. 4：成功污染案例中F1为86.3%、F2为62.5%、两者同时满足56.1%（配置宏平均）；30.2个百分点差距代表去除目标语义但未保留所需正常记忆。删除/中和、正常记忆保留、外部效果补偿是三个不同验收目标。

### 2. 质疑

- isolated runtime 与现实 SaaS/API 的 provider-authoritative post-state 仍有距离。
- Appendix E：W1为确定性检查；其余含按检查点的judge及程序门禁，500条分层抽样与两位人工标注者分别一致453/500（90.6%）、459/500（91.8%），非100%正确oracle。缺证据与判定失败分开，不将缺失自动计失败。
- Forget 成功并不意味着已经发出的消息、已提交交易或传播工件被撤销。

### 3. 对标

- 对 EX-006：提供 carrier lifecycle 的 Write→Execute→Forget 联动证据。
- 对 EX-005：本库综合：修复后应继续核对既有外部效果及必要补偿；论文Forget分支不包含Execute后补偿，不能声称论文已测量外部恢复。
- 对 [[Agent-Security]]：恢复链需要区分 state repair、effect compensation 和 canonical post-state verification。

## 证据边界（2026-11-28）

直接回核[arXiv v1](https://arxiv.org/html/2607.27080v1) Methodology、Evaluation Metrics、Table 2、Fig. 4/5、Appendix A.1/E.6。每配置310个case槽，24×310为配置-案例组合而非独立真人用户；隔离服务记录/工作区证据为任务定义的外部化，非真实生产API效果。作者强调后端比较是匹配配置下描述性对照，未来仍需受控消融；条件分母不同，不直接比较所有被污染案例的选择性修复。未复跑实验或检查全部数据工件。

**本库综合**：对LLM WiKi的纠错验收必须同时检查错误主张确已纠正、仍正确知识未丢失、受影响下游页已复核。不能以删除条目、lint通过或模型自报替代独立语义及真实终态验收。

## 关联概念

- [[Agent-Security]]
- [[Agent-Attack-Surface]]
- [[Shared-Memory-Contamination]]
- [[Alert-Closed-Loop]]
