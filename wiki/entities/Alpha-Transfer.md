---
type: entity
title: Alpha Transfer
aliases:
  - Alpha Transfer
  - Alpha 转移
  - Alpha 泄露
  - AI 主权流失
definition: "企业使用托管模型服务时，其 prompts、responses 与使用模式所承载的机构独特知识（alpha）经条款许可的通道转移给提供商，并可能以权重或服务形式被转售给市场（含竞争对手）"
created: 2026-07-30
updated: 2026-08-03
tags:
  - enterprise-ai
  - ai-sovereignty
related_entities:
  - "[[Reverse-Information-Paradox]]"
  - "[[Moats-in-AI-Era]]"
  - "[[Exit-Sovereignty]]"
  - "[[Hardware-Sovereignty]]"
  - "[[Zero-PHI-Policy]]"
  - "[[Policy-as-Code-for-Agent-Governance]]"
source_raw:
  - "[[20260727-palantir-ai-sovereignty-alpha-playbook]]"
evidence_level: low
claim_type: mixed
---

# Alpha Transfer（Alpha 转移）

> [!definition] 定义
> **Alpha Transfer（Alpha 转移）** 是企业使用托管模型服务（Hosted Model Providers：AI Labs 与 Hyperscalers）时，其暴露给模型的数据——prompts、responses、使用模式——所承载的独特机构知识与技艺（tradecraft）经条款许可的通道转移给提供商的过程。转移后的 alpha 可能以权重或服务形式被转售给更广泛的市场，包括竞争对手。它是 [[Reverse-Information-Paradox|反向信息悖论]] 的条款级机制描述：悖论说明买方为使用智能必然泄露，alpha transfer 说明泄露沿哪些合同通道流出、又如何被堵住。

## 概念边界锐化（08-03 圆桌，synthesized/medium，待升级）

> [!abstract] 锐化定义（待升级）
> **alpha = 你的实践中不可被市场遗骸复活的不对称部分**（带公共成分修饰语：不对称中有多少来自公共基础，决定"保护"的正当性可争议程度）。证据基础未变（单一 vendor 来源），本节为概念分析非事实断言。

- **转移机制精炼**：转移的不是 alpha 而是**公约数遗骸**——prompts = 被编码的问题、使用模式 = 工作流的遗骸化痕迹（接遗骸化定理结构〔08-03 agenda〕：实践→遗骸转化不完全、残差永在）；vendor 从千万客户遗骸中**统计聚合**复活出市场实践的公约形态——聚合按定义消灭偏差（偏离公约数的不对称分子不可被复活）。故**归零的是公约数租金**（你的实践公约数从"只服务你"稀释为"市场可购买服务"，基线变成别人的产品），**保留的是不对称分子**（alpha 按定义不可复活）。
- **威胁形态**：不是 alpha 直接流失，而是**alpha 更新成本的红皇后加速**（市场平均成为可购买服务 → 维持相对独特性的成本上升——接剪刀定理的红皇后结构：保持奔跑才能留在原地）。
- **半真叙事裁决**（本条来源性质）：Palantir playbook 的机制层为真（提取通道/ZDR 稀释路径有行业文档佐证，可作采购清单），框架层是剥削性叙事（"你有 alpha 待保护"的恐惧服务其主权产品销售），且掩盖一层：alpha 相当部分由公共基础（公共资助研究/开放数据/互联网语料）共同创造——"保护 alpha"叙事把公共价值私有化两次（组织结晶公共知识为私有 alpha 是一次，vendor 提取是二次）。处理规范：**提取机制 + 质问框架 + 追问"谁的价值"**。
- **实践推论**：① 值得保护的不是数据而是**实践模式**（使用模式是实践形态的遗骸，比数据本身更危险——ZDR 防御优先级应防模式先于防数据）；② 真正的 alpha 战略不是防泄露而是**不对称产生速度 > 遗骸聚合速度**（持续生产新不对称）；③ 不对称中公共成分越多，"保护"的正当性越可争议。
- **概念缺口**：alpha 的公共价值成分未进入企业主权讨论——这是本条来源（vendor playbook）结构性缺失的维度，待公共政策视角的来源补充。

## 提取通道（不止"训练"一条）

1. **直接训练**：prompts/responses 进入模型训练数据——多数提供商承诺不做，但承诺主体常有缺口（Hyperscaler 只约束 AI Lab 不约束自己）。
2. **辅助服务改进**：元数据与使用模式被用于改进"辅助服务与工具"；触发安全分类器的 prompt 被用于改进分类器本身；使用模式被用于改进模型 harness。
3. **例外路径留存**：ZDR 的八类例外（见下）使数据在"承诺不留存"的前提下仍被落盘、人审或长期缓存。
4. **诉讼与攻击面**：留存的数据可能被卷入提供商自身的法律战，或成为网络攻击的标的面。

## ZDR 与其八类稀释路径

严格 ZDR（Zero Data Retention）的四条定义：不落盘存储或记录、不交人工审查、不用于训练或服务改进、仅在内存暂存至请求完成。常见稀释路径：

| 路径 | 机制 |
|------|------|
| Beta/preview 服务 | beta 服务及 beta API 配置（模型 A + beta 工具）整体排除出 ZDR 范围，且"什么是 beta"只写在随时变动的产品文档里 |
| 安全分类器触发 | 分类器命中即存储+人审，误报使合法 prompt 同样被留存（部分高优先级分类器即使关闭 abuse monitoring 仍触发） |
| 图像/文件输入 | 多模态 prompt 不适用或仅适用弱化版 ZDR |
| Prompt 缓存 | 扩展缓存功能将 prompts 落盘、TTL 过长 |
| 条款叠加 | Hyperscaler 在 AI Lab 条款上叠加自有条款；Lab A 的定制保护需主动同步给云商 B |
| DPA 免责声明 | 超链接在线条款对特定服务免除全部数据处理条款 |
| 静默启用 | 服务/模型被自动启用或升级到无保护版本，无显式通知 |
| 认证边界 | 提供商或其特定服务不满足工作流所需认证（SOC2 ≠ FedRAMP ≠ IL2/4/5） |

## 四层防御

1. **合同层**：严格 ZDR 四条 + 正向枚举唯一许可用途（而非负面清单）+ 同时绑定提供商与 AI Lab + 责任上限高到条款能"咬合"。
2. **服务边界层**：活体 allow-list（模型/工具/特性/端点），IT-法务联动审查新服务，beta header 自动阻断，区域路由 fail-safe。
3. **变更锁定层**：超链接条款冻结于签约日文本、设定严格优先顺序、web.archive 变更监控告警；面向非法务员工的 click-through 条款合同约定无效。
4. **连续性层**：停用/终止前通知 + investigation & cure 期（且调查期不得获取 alpha）+ 迁移缓冲期；用例前置许可 + 关闭相关分类器——迁移缓冲是 [[Exit-Sovereignty|退出主权]] 的时间维度设计。

## 关键数据点

- **严格 ZDR 的四条定义**（原文）：提供商不 (1) 将 prompts/responses 落盘存储或记录，(2) 交人工审查，(3) 用于训练模型或改进服务，(4) 仅在内存暂存至完成请求所需时间。
- **提取不止训练一条**（原文列举）：触发安全分类器的 prompt 可被用于改进分类器本身；使用模式可被用于改进模型 harness；Hyperscaler 常只承诺"创建模型的 AI Lab 不训练"而不以同等方式约束自己。
- **八类 ZDR 稀释路径**（见上表）：beta 服务/配置、安全分类器触发存储+人审（含误报）、图像/文件 prompt、prompt 缓存长 TTL 落盘、条款叠加、DPA 免责、静默启用、认证边界。
- **防御四层**（见下节）：合同（ZDR + 正向枚举唯一许可用途 + 责任上限咬合）→ 服务边界（活体 allow-list + beta header 阻断）→ 变更锁定（超链接条款冻结 + click-through 无效）→ 连续性（通知 + investigation & cure + 迁移缓冲）。
- **来源性质**：单一 vendor（Palantir 销售主权 AI 产品），全文无案例引用、附法律免责声明；机制断言未经独立验证。

## 前提与局限性

- **证据层级 low**：机制清单来自单一 vendor（Palantir 销售主权 AI，论点与其商业模式直接自利），全部为"提供商通常如此"式断言，无公开案例引用；部分机制（beta 排除、分类器存储）有行业文档佐证，部分（元数据改进 harness）属推断。
- **谈判地位门槛**：定制主条款、冻结超链接条款、click-through 无效等大客户手段对只能接受标准条款的组织不可用；其可执行部分只剩 allow-list 与技术阻断门。
- **清单会过时**：条款形态随提供商与时间持续变化（文章自身承认）；防御必须包含变更监控，而非一次性审查。
- **硬约束不可消除**：模型必须消费输入才能产生输出——alpha 泄露只能压缩（ZDR + 边界 + 本地化），不能归零；主权控制是颗粒化控制，不是绝对控制。

## 关联概念

- [[Reverse-Information-Paradox]] — 本条是反向信息悖论"解决方案"一栏的条款级答案：堵漏工程。
- [[Moats-in-AI-Era]] — alpha = 独占资源护城河的数据形态；转移 = 护城河向供应商及其客户的单向倾倒。
- [[Exit-Sovereignty]] — 迁移缓冲期与区域专属容量是退出权的时间与空间设计。
- [[Hardware-Sovereignty]] — 彻底路径：neocloud + 开源自托管，把数据留在自己控制的栈内。
- [[Zero-PHI-Policy]] — 同构模式：PHI 是合规驱动的硬数据边界，alpha 是竞争驱动的软数据边界。
- [[Policy-as-Code-for-Agent-Governance]] — allow-list、beta header 阻断、路由 fail-safe 是法务条款的运行时执行形态。
