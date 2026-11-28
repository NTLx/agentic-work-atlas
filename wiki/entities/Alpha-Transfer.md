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
updated: 2026-11-28
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
> **Alpha Transfer（Alpha 转移）** 是企业使用托管模型服务（Hosted Model Providers：AI Labs 与 Hyperscalers）时，其暴露给模型的数据——prompts、responses、使用模式——所承载的独特机构知识与技艺（tradecraft）经条款许可的通道转移给提供商的过程。转移后的 alpha 可能以权重或服务形式被转售给更广泛的市场，包括竞争对手。它是 [[Reverse-Information-Paradox|反向信息悖论]] 的条款级机制描述：这是供应商提出的商业信息暴露风险；处理、留存、训练、对外披露与实际竞争损失是不同事件，不能把正常处理等同泄露。

## 提取通道（不止"训练"一条）

1. **直接训练**：prompts/responses 进入模型训练数据——多数提供商承诺不做，但承诺主体常有缺口（Hyperscaler 只约束 AI Lab 不约束自己）。
2. **辅助服务改进**：元数据与使用模式被用于改进"辅助服务与工具"；触发安全分类器的 prompt 被用于改进分类器本身；使用模式被用于改进模型 harness。
3. **例外路径留存**：ZDR 的八类例外（见下）使数据在"承诺不留存"的前提下仍被落盘、人审或长期缓存。
4. **诉讼与攻击面**：留存的数据可能被卷入提供商自身的法律战，或成为网络攻击的标的面。

## ZDR 与其八类稀释路径

Palantir建议的严格ZDR四条约束：不落盘、不人审、不训练/改进、仅在请求所需时间内存暂存；非通用法律定义。以下为潜在检查路径，不预设每个服务均存在。

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
4. **连续性层**：停用/终止前通知 + investigation & cure 期（且调查期不得获取 alpha）+ 迁移缓冲期；用例前置合法许可、核对适用安全及合规机制——迁移缓冲是 [[Exit-Sovereignty|退出主权]] 的时间维度设计。

## 关键数据点

- **严格 ZDR 的四条定义**（原文）：提供商不 (1) 将 prompts/responses 落盘存储或记录，(2) 交人工审查，(3) 用于训练模型或改进服务，(4) 仅在内存暂存至完成请求所需时间。
- **提取不止训练一条**（原文列举）：触发安全分类器的 prompt 可被用于改进分类器本身；使用模式可被用于改进模型 harness；Hyperscaler 常只承诺"创建模型的 AI Lab 不训练"而不以同等方式约束自己。
- **八类 ZDR 稀释路径**（见上表）：beta 服务/配置、安全分类器触发存储+人审（含误报）、图像/文件 prompt、prompt 缓存长 TTL 落盘、条款叠加、DPA 免责、静默启用、认证边界。
- **防御四层**（见下节）：合同（ZDR + 正向枚举唯一许可用途 + 责任上限咬合）→ 服务边界（活体 allow-list + beta header 阻断）→ 变更锁定（超链接条款冻结 + click-through 无效）→ 连续性（通知 + investigation & cure + 迁移缓冲）。
- **来源性质**：单一 vendor（Palantir 销售主权 AI 产品），全文无案例引用、附法律免责声明；机制断言未经独立验证。

## 前提与局限性

2026-11-28 [OpenRouter ZDR官方文档](https://openrouter.ai/docs/guides/features/zdr) 将ZDR描述为无例行保留，明确内存隐式缓存可允许、Safety Retention按配置区分、BYOK/私有端点声明并非履约证明，并显示10月27日计划安全筛查及法定保留例外说明。文档仍标为planned，未验证实际生效或合同；不得承诺通用四条，亦不建议绕过安全机制。按端点/工具/区域/协议及实际数据链校验。

- **证据层级 low**：机制清单来自单一 vendor（Palantir 销售主权 AI，论点与其商业模式直接自利），全部为"提供商通常如此"式断言，无公开案例引用；部分机制（beta 排除、分类器存储）有行业文档佐证，部分（元数据改进 harness）属推断。
- **谈判地位门槛**：定制主条款、冻结超链接条款、click-through 无效等大客户手段对只能接受标准条款的组织不可用；其可执行部分只剩 allow-list 与技术阻断门。
- **清单会过时**：条款形态随提供商与时间持续变化（文章自身承认）；防御必须包含变更监控，而非一次性审查。
- **处理与泄露分开**：模型消费输入不等于信息泄露；应验证访问、保留、再利用及披露边界。自托管同样涉及管理员、工具、日志及供应链风险，不能承诺绝对安全。

## 关联概念

- [[Reverse-Information-Paradox]] — 本条是反向信息悖论"解决方案"一栏的条款级答案：堵漏工程。
- [[Moats-in-AI-Era]] — alpha = 独占资源护城河的数据形态；转移 = 护城河向供应商及其客户的单向倾倒。
- [[Exit-Sovereignty]] — 迁移缓冲期与区域专属容量是退出权的时间与空间设计。
- [[Hardware-Sovereignty]] — 自托管可能改善控制权，但非彻底消除风险。
- [[Zero-PHI-Policy]] — 同构模式：PHI 是合规驱动的硬数据边界，alpha 是竞争驱动的软数据边界。
- [[Policy-as-Code-for-Agent-Governance]] — allow-list、beta header 阻断、路由 fail-safe 是法务条款的运行时执行形态。
