---
type: source-summary
title: "Your AI isn't stupid. It's blind."
canonical_url: "https://tessl.io/blog/your-ai-isnt-stupid-its-blind"
raw_state: index
original_raw_file: "20261020-tessl-claim-based-agent-memory.md"
original_body_sha256: "46b2bd03cac56002ab13d2f77944129a20f05205bfc1cbf606a4e9e6e7feeb9a"
indexed_at: "2026-11-06T00:57:55.293Z"
created: 2026-11-06
updated: 2026-11-28
tags:
  - source-summary
  - knowledge-management
evidence_level: low
claim_type: mixed
source_locator:
  - "Original article section: Why agent memory matters now"
  - "Original article section: 1. Store claims, not chunks"
  - "Original article section: 2. Make time and absence explicit"
  - "Original article section: 3. Decide permissions before the model runs"
  - "Original article section: Where memory fits in a software factory"
  - "Original article section: TL;DR"
---

# Your AI isn't stupid. It's blind.

> 证据来源：https://tessl.io/blog/your-ai-isnt-stupid-its-blind（2026-10-20，Ran Aroussi）。2026-11-06 读取官方网站公开正文并逐节核对。原文以 canonical URL 为权威；本 Wiki 保存自撰释义、章节定位和推理边界，不存储网页逐字全文；original_body_sha256 仅记录临时来源索引记录的哈希，**不是**网页全文校验值。**本文数据若未注明独立验证，均为该来源的报道/作者陈述。**

## 编译摘要

### 1. 浓缩

- **核心结论 1：组织 Agent 记忆的单位应尽量是有来源、时间区间与可见性的 Claim，而非未治理的相似文本块。**
  - **原文证据**：作者称其 VarOps 系统为每个 Claim 保留说话人、事实、有效时间与原文 span；报告LongMemEval-S 500问的Hit@10为99.8%，严格Recall@10为95.8%，非答案准确率；同表LoCoMo为93.06%/82.64%，BEAM 1M为44.0%/16.16%。不同任务及语料，不能认为蒸馏普遍无损。约3500万Token摄入成本来自另一个BEAM 1M实验，非LongMemEval的同次运行。

- **核心结论 2：记忆应区分事实变化与知识空白，避免把缺失内容自动补全成想象。**
  - **原文证据**：作者保留新旧事实及 supersedes 关系，让系统区分 answered、searched but absent、out of scope；在一项消融中，技术报告Appendix A.11表：同500题、相同检索与judge，原配置与禁止拒答探针总准确率88.0→87.2%；30不可答题中正确拒答29→0，470可答题准确率87.4→92.8%。文章称30次原有诚实拒答不符合表中29次；不重复该说法。

- **核心结论 3：访问控制应在检索前按用户身份执行，而不是让模型负责事后隐去敏感信息。**
  - **原文证据**：作者描述写入时计算披露等级、查询前按授权选择数据，示例里不同角色看到精确营收或区间；Appendix A.13报告五对隔离记忆存储、每对九项测试共45项拒绝或限制成功；还报告18项分级披露集成测试。权限机制需覆盖组合推导、撤销、实际提交及可观测性，非生产安全证明。

## 本轮原始证据复核（2026-11-28）

Tessl canonical再次超时；通过作者本人[VarOps同题文章](https://varops.com/your-ai-isnt-stupid-its-blind/)（2026-10-08，章节和关键数字一致）与[技术报告v1.1 Markdown](https://raw.githubusercontent.com/varops/acropolis-research/main/paper/README.md)、[Appendix A reference v1.3](https://raw.githubusercontent.com/varops/acropolis-research/main/paper/methodology.md)交叉核验。保留Tessl索引及原哈希，不声称逐字一致。报告为厂商自评，Markdown可演化，未打开冻结PDF、逐条复验报告工件或运行实验。

- **检索与成本**：报告Retrieval表的LongMemEval-S Hit@10 99.8%不是完整证据召回或答案正确；不同数据集表现差异大。§6的BEAM 1M历史运行（2026-08-20）约3500万Token、17,745 accepted claims、37,387 LLM calls、总摄入`$8.24`，本地CPU嵌入报告无外部API费，不等于零计算成本。文内每claim `$0.0021` 与所列总额及数量不一致；若相同分母，直接除得约`$0.000464`。未核费用原始明细，不选定哪项为真。local是自主运营模型，不是物理本地；Appendix A.1称相关本地模型测试使用租用H200，不能把CPU嵌入条件套到所有提炼、回答与硬件成本。
- **拒答与评测合同**：Appendix A.11报告88.0→87.2%及不可答、可答分组结果；禁止拒答是探针而非发布配置。整体、可答子集、拒答正确率必须分别报告。作者正文的30次转变与表中原29次正确拒答存在差异，保留表值，未核逐题结果。
- **模型席位与证据边界**：报告及[Acropolis产品说明](https://varops.com/acropolis/)将提炼、检索与回答分离；三项会话记忆基准按所述严格口径全本地保留全frontier参考得分84–96%、仅租用回答席位约96–99%，是相对参考得分而非绝对正确率。BEAM 100K全本地在共享GPU并发下中位12–15分钟/问，frontier行不到1分钟；不等于单用户延迟。报告Table 3/4的再评分更换回答/判分规则及部分题目注释，分数大幅变化；比较协议下并非全本地回答，不能把不同协议得分直接排名。数据集均非真实企业工作负载，规模化目录、真实组织决策与生产结果尚未验证。
- **权限与来源**：作者的claim来源、有效时间、supersedes与预检索授权是候选合同；预生成披露层级仍需验证组合推导和撤销生效。文章主张丢弃原始transcript，但有损提炼可能损害恢复、复核及后续任务；Wiki应按来源权限、保留策略和实际依赖选择保存范围，而非直接照搬。

### 2. 质疑与证据边界

- 文章与关联报告均由系统作者撰写，公开报告、方法与逐题工件提高可检查性，不构成独立复现；LongMemEval检索命中率不能等同端到端答案正确率。
- Claim 蒸馏有信息损失；多人权限、来源组合派生信息和时间冲突需要明确定义。
- 所谓 45/45 防御只是所述攻击集内结果，不能证明普遍抗越权。

### 3. 对标与应用约束

- **跨域迁移（综合判断，非原文证实）**：对 [[Agent-Knowledge-Management]]：与现有 provenance、Evidence/Reasoning 区分以及 Schema 的 source locator 有直接结构同构；但不应据此把全文 Source 自动丢弃，须由恢复性与活跃 Claim 依赖决定。
- **使用前提**：任何架构类比只能用于提出评测与工程变更候选；生产推广需真实权限、失败恢复、成本与回归实测。

## 重要判断（Claim / Evidence / Boundary）

- **判断**：组织 Agent 记忆的单位应尽量是有来源、时间区间与可见性的 Claim，而非未治理的相似文本块。
  - **证据**：一手来源 [Your AI isn't stupid. It's blind.](https://tessl.io/blog/your-ai-isnt-stupid-its-blind)，定位至「Why agent memory matters now / 1. Store claims, not chunks / 2. Make time and absence explicit / 3. Decide permissions before the model runs」及上方事实摘要。
  - **边界**：文章与关联报告均由系统作者撰写，公开报告、方法与逐题工件提高可检查性，不构成独立复现；LongMemEval检索命中率不能等同端到端答案正确率。

### 关联概念

- [[Agent-Knowledge-Management]]
- [[Structured-Agent-Memory]]
- [[Memory-Architecture]]
