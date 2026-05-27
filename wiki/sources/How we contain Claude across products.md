---
type: source-summary
title: "How we contain Claude across products"
source_raw:
  - "[[How we contain Claude across products]]"
created: 2026-05-27
updated: 2026-05-27
tags:
  - source-summary
  - agent-security
  - containment
  - Anthropic
---

# How we contain Claude across products

## 编译摘要

### 1. 浓缩

- **核心结论1**: Agent 安全的正确策略是"先环境层 containment，再模型层 steering"——确定性边界兜底概率性防御的一切遗漏
  - 关键证据: 员工钓鱼攻击中 Claude 24/25 次成功外泄数据，模型层完全无法识别（因为指令来自用户本人）；api.anthropic.com 白名单外泄中数据通过合法目的地被偷走。两次事件都只有环境层能兜住
- **核心结论2**: 隔离强度必须匹配用户的监督能力——开发者可以读 bash，知识工作者不能
  - 关键证据: Claude Code 面向开发者，依赖 HITL + OS 沙箱（84% 权限提示减少）；Claude Cowork 面向非技术用户，使用完整 VM（hypervisor 级隔离），因为审批需要用户不具备的专业知识
- **核心结论3**: 自建组件是最弱环节——经过对抗加固的标准基础设施（gVisor、seccomp、hypervisor）比自研代理/白名单更可靠
  - 关键证据: 所有产品中 gVisor/seccomp/hypervisor 始终可靠，自研的 allowlist proxy 和 trust dialog 时序是最严重的安全失败点

### 2. 质疑

- **关于"环境层优先"的普适性**: 本文基于 Anthropic 自家三款产品的经验，但大多数企业 Agent 部署无法像 Claude Cowork 那样使用完整 VM——成本和性能约束下，环境层优先是否可行？
- **关于 93% 审批率数据**: 用户批准 93% 的权限提示可能说明 Agent 做得好（不需要频繁打断），也可能说明审批疲劳——两种解读导致相反的设计决策
- **关于 VM 模式的 EDR 盲区**: 文章承认隔离也把端点检测软件挡在外面，这对合规要求高的企业是实质性障碍，文中只提供了 OTLP 日志导出作为降级方案
- **关于"模型改进后风险不缩小"**: 文章指出更强模型犯更少明显错误但能找到更出人意料的绕过路径——这是否意味着 containment 策略永远在追赶？

### 3. 对标

- **跨域关联1**: 类似微服务架构中的"最小权限原则"和"零信任网络"——Agent containment 把网络安全的成熟原则应用于 AI Agent 场景
- **跨域关联2**: 与 [[Agent-Harness]] 的"安全执行环境"组件（第 12 个）互补——Agent-Harness 定义组件，Agent-Containment 定义隔离策略和安全架构
- **跨域关联3**: 与 [[Verifiability]] 形成两层防御——Verifiability 是事后可验证，Containment 是事前不可达。两者共同构成 Agent 安全的"验证+隔离"双保险

### 关联概念

- [[Agent-Containment]]
- [[Agent-Harness]]
- [[Verifiability]]
- [[Security-Hardening-Phase]]
