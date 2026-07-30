---
type: source-summary
title: "AI Sovereignty is Your Alpha: How to Avoid Transferring Your Alpha to a Hosted Model Provider"
source_raw:
  - "[[20260727-palantir-ai-sovereignty-alpha-playbook]]"
created: 2026-07-30
updated: 2026-07-30
tags:
  - source-summary
  - enterprise-ai
  - ai-sovereignty
evidence_level: low
claim_type: mixed
---

# AI Sovereignty is Your Alpha — Palantir AI 采购合同 Playbook

> 来源：Palantir Blog（2026-07-27），厂商官方（法务/安全团队口吻）。**证据定级 low**：vendor 立场（Palantir 销售主权 AI 产品，论点与商业模式直接自利）；全部机制为"提供商通常这样做"式断言，无案例引用、无证据链接；附法律免责声明。机制颗粒度高，可作采购检查清单引用，不可单独支撑新判断升级。

## 编译摘要

### 1. 浓缩
- **核心结论1**：alpha 是你使用 AI 时暴露的数据所承载的机构独特知识与技艺；托管模型提供商（AI Labs + Hyperscalers）有动机也有条款空间提取它，并以权重或服务形式转售
  - 关键证据: 提取通道不止"训练"一条——元数据与使用模式可改进"辅助服务与工具"，触发安全分类器的 prompt 可改进分类器本身，使用模式可改进模型 harness；超大规模云商常只承诺"AI Lab 不训练"而不约束自己。数据留存还扩大攻击面、并可能被卷入提供商自身的存续性诉讼。
- **核心结论2**：严格 ZDR（四条定义：不落盘、不人审、不训练/改进、仅内存暂存至请求完成）是必要不充分条件——至少八条例外路径可稀释它
  - 关键证据: beta/preview 服务及 beta API 配置（模型 A + beta 工具即出保护范围）；安全分类器触发即存储+人审（含误报）；图像/文件 prompt 不适用 ZDR；prompt 缓存长 TTL 落盘；Hyperscaler 在 AI Lab 条款上叠加自有条款（Lab A 的定制条款需主动同步给云商 B）；DPA/BAA 被超链接条款免责声明；服务被自动启用/升级到无保护版本且不通知；合规认证边界（SOC2 ≠ FedRAMP ≠ IL2/4/5）。
- **核心结论3**：主权 = 颗粒化控制，需要四层纵深：合同条款 + 活体 allow-list（IT-法务联动审查，beta header 自动阻断）+ 锁死单方变更（超链接条款冻结于签约日/优先顺序/web.archive 监控；click-through 条款约定无效）+ 运营连续性（停用前通知 + investigation & cure 期 + 迁移缓冲期；全球推理区域限定）

### 2. 质疑
- **关于"结论1"的质疑**: "提供商会提取并转售你的 alpha"是全文论点，但无一起公开案例被引用；部分机制（分类器触发存储、beta 排除 ZDR）属行业有文档记录的做法，部分（元数据改进 harness）属推断；厂商立场使论点强度需要打折——同一机制清单由非利益相关方陈述时可信度更高。
- **关于"结论2"的质疑**: 例外清单的覆盖面是"常见的"而非"全部的"；条款形态随提供商与时间变化，清单会过时（文章自身承认超链接条款持续变动）。
- **关于"结论3"的质疑**: 全部最佳实践预设大客户谈判地位（定制主条款、冻结超链接条款、约定 click-through 无效）；对只能接受标准条款的中小组织，可执行的只剩 allow-list 与阻断类技术门——playbook 的适用域比标题暗示的窄。
- **数据可靠性**: 无外部验证、无引用、有法律免责声明；当作"有结构的行业经验主张"使用，不当作事实库。

### 3. 对标
- **[[Reverse-Information-Paradox]] 的"?"有了第一个具体答案**: Nadella 悖论（买方为使用智能必须泄露专有知识）的比较表里，"解决方案"一栏原本只有问号（信任边界 + 自主 learning loop）。本 playbook 是泄露侧的堵漏工程：ZDR = 把 exhaust 留在内存里；限制使用条款 = 切断"泄露 → 转售"通道；迁移缓冲 = 保留退出权。两者合成企业 AI 采购的完整图景——悖论说明为什么必然泄露，playbook 说明泄露的边界可以谈判。
- **[[Moats-in-AI-Era]] 的微观机制**: Boris Cherny 框架中 AI 不削弱的"独占资源"护城河，其侵蚀机制在此有了条款级描述——alpha 经 ZDR 例外、元数据使用、分类器语料逐条渗漏，等于把 cornered resource 以数据形态单向转移给供应商及其全部客户。
- **采购层的 [[Policy-as-Code-for-Agent-Governance]]**: 活体 allow-list、beta header 自动阻断、区域路由 fail-safe、条款变更自动告警——法务条款的可执行化，与 agent 治理中"把权限从 prompt 移到运行时"同构。合同条款若无技术门执行，等于超链接条款。
- **[[Zero-PHI-Policy]] 的镜像**: PHI 边界是合规驱动的硬数据隔离（医疗），alpha 边界是竞争驱动的软数据隔离（全行业）；两者共享同一工程模式：按数据类别划定"什么绝不能进入外部模型上下文"。
- **约束分析（3c）**: 硬约束——模型必须消费输入才能产生输出（与反向信息悖论同一硬约束，泄露不可消除只可压缩）；软约束——ZDR 条款、责任上限、区域限定（可谈判、可技术执行）；自设约束——"标准条款只能接受"被 click-through 无效条款与条款冻结实践反例（但受谈判地位约束）。

### 关联概念
- [[Alpha-Transfer]]
- [[Reverse-Information-Paradox]]
- [[Moats-in-AI-Era]]
- [[Zero-PHI-Policy]]
- [[Policy-as-Code-for-Agent-Governance]]
- [[Exit-Sovereignty]]
- [[Hardware-Sovereignty]]
