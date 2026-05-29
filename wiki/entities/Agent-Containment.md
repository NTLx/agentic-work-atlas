---
type: entity
title: "Agent Containment"
aliases:
  - Agent Containment
  - Agent 遏制
  - Agent 隔离
  - Blast Radius Control
definition: "通过环境层隔离限制 Agent 可操作范围，使概率性防御（模型层）失效时仍有确定性边界兜底的安全架构"
created: 2026-05-27
updated: 2026-05-29
tags:
  - agent-security
  - architecture
  - containment
  - infrastructure
related_entities:
  - "[[Agent-Harness]]"
  - "[[Verifiability]]"
  - "[[Security-Hardening-Phase]]"
  - "[[Harness-Engineering]]"
  - "[[Least-Agency]]"
  - "[[Model-Safety-Divergence]]"
  - "[[Emergence-World]]"
source_raw:
  - "[[How we contain Claude across products]]"
  - "[[20260518-zero-trust-for-ai-agents]]"
  - "[[Using LLMs to secure source code]]"
  - "[[20260528-ai-model-simulation]]"
---

# Agent Containment（Agent 隔离与遏制）

> [!definition] 定义
> 通过环境层隔离限制 Agent 的可操作范围（blast radius），使概率性防御（模型层）失效时仍有确定性边界兜底。Anthropic 工程团队从三款 Claude 产品的安全实践中提炼。

## 三层风险 × 三层防御

Agent 安全风险分三类，防御对应三个组件：

| 风险类型 | 描述 | 防御组件 |
|---------|------|---------|
| **用户误用** | 用户指示 Agent 做有害操作（故意或疏忽） | 环境隔离 + 权限控制 |
| **模型误行为** | Agent 自发采取有害行动（如"helpfully"逃逸沙箱） | 模型层（系统提示、分类器、训练） |
| **外部攻击** | 通过工具、文件、网络对 Agent 进行注入或传统攻击 | 内容检查 + 工具权限限制 |

**核心原则**: 环境层 containment 优先于模型层 steering。模型层防御是概率性的（Claude Opus 4.7 单次攻击成功率 ~0.1%，100 次自适应攻击 ~5-6%），永远无法 100%。确定性边界（沙箱、VM、文件系统隔离）是兜底。

## 三种隔离模式

| 模式 | 产品 | 环境 | 隔离机制 | Blast Radius | 用户要求 |
|------|------|------|---------|-------------|---------|
| **临时容器** | claude.ai | 服务端 gVisor | 每会话临时容器，无持久文件系统 | 最小（服务端隔离） | 无 |
| **HITL 沙箱** | Claude Code | 用户本机 | OS 沙箱（macOS Seatbelt / Linux bubblewrap） + 人类审批 | 工作目录内 | 能读 bash |
| **密封 VM** | Claude Cowork | 用户桌面 | 完整虚拟机（hypervisor 级），挂载式文件系统 | 挂载目录内 | 无 |

### 模式选择逻辑

隔离强度必须匹配用户的监督能力：
- **开发者**（Claude Code）: 能理解 `rm -rf` 的含义 → HITL + 轻量沙箱足够
- **知识工作者**（Claude Cowork）: 不能期望判断 `find . -name "*.tmp" -exec rm {} \;` → 需要绝对且始终开启的 VM 隔离
- **匿名用户**（claude.ai）: 无本地执行 → 服务端容器隔离

## 四个安全失败案例

### 1. 信任对话之前的执行（Claude Code，2025 年中-2026 年 1 月）

攻击者提交含恶意 `.claude/settings.json` 的仓库。Claude Code 在显示"你信任此目录吗？"提示之前就读取并执行了 hook。

**教训**: 项目打开、配置加载、localhost 监听器必须被视为来自互联网的入站请求。

### 2. 用户作为注入向量（Claude Code，2026 年 2 月）

红队演练中，钓鱼邮件让员工运行含隐藏恶意指令的"常规任务"。25 次重试中 24 次成功读取 `~/.aws/credentials` 并外泄。模型层无法识别——因为指令来自用户本人。

**教训**: 唯一有效的防御是环境层——egress 控制阻止 POST，文件系统边界阻止 `~/.aws` 访问。

### 3. 通过已批准域名外泄（Claude Cowork）

攻击者在用户工作区放置含隐藏指令的文件 + 攻击者 API key。Claude 读取其他文件，用攻击者的 key 调用 Anthropic Files API。egress proxy 看到目的地是 `api.anthropic.com`，放行了。

**教训**: 域名白名单应被视为**能力授予**，而非目的地过滤。白名单上每个域名的每个功能都是攻击面。

### 4. VM 隔离挡住了 EDR（Claude Cowork）

企业安全团队问"为什么 EDR 看不到 VM 内部"——隔离把 Agent 关住了，也把端点检测软件挡在外面。

**教训**: 隔离降低可见性。合规依赖端点可见性的团队需要提前规划。

## 关键数据点

- 用户批准 **93%** 的权限提示——审批疲劳使 HITL 成为不可靠的防御
- Claude Code auto mode 捕获 ~**83%** 的过度行为，但 ~**17%** 的过激操作仍能通过
- OS 沙箱减少 **84%** 的权限提示
- Claude Opus 4.7 在 Gray Swan Agent Red Team 基准上：单次攻击成功率 ~**0.1%**，100 次自适应攻击 ~**5-6%**
- 红队钓鱼攻击：**24/25** 次成功外泄（96%）
- 经验丰富的用户自动审批率是新手用户的 **2 倍**，但中断 Agent 执行也更频繁

## 前沿威胁

| 威胁 | 描述 | 状态 |
|------|------|------|
| **持久记忆投毒** | 注入落入 CLAUDE.md、产品记忆、定时 Agent 状态目录 → 每次启动重新加载 | 需要会话启动分类器 |
| **多 Agent 信任升级** | 子 Agent 输出被当作"自己人的输出"而非原始工具结果 → 新的注入路径 | 需在信任层级分配和注入风险间权衡 |
| **Agent 身份** | Agent 应拥有独立身份还是继承用户权限？Claude Cowork 使用 per-session scoped token | 跨平台标准尚未形成 |

## 前提与局限性

- **前提**: 大部分安全教训来自 Anthropic 自家产品（claude.ai、Claude Code、Cowork），不同产品形态可能有不同的最优隔离策略
- **局限性**: 环境层 containment 增加延迟和成本（VM 启动时间），且降低可见性（EDR 盲区）
- **边界条件**: 自建组件是最弱环节——gVisor、seccomp、hypervisor 经过多年对抗加固，自研代理/白名单/解析器是主要失败点
- **与模型层的关系**: 不是替代模型层防御，而是兜底。Claude Code auto mode 的分类器在沙箱内仍有效减少摩擦

## 关联概念

- [[Agent-Harness]] — Containment 是 Harness 第 12 组件（安全执行环境）的架构级扩展
- [[Verifiability]] — 事后可验证与事前不可达构成双层防御
- [[Security-Hardening-Phase]] — Containment 是 Agentic Coding 第三阶段的核心实践
- [[Harness-Engineering]] — 隔离策略是 Harness 工程的关键架构决策
- [[Least-Agency]] — OWASP 新概念，Containment 在权限层的实现原则
- [[Model-Safety-Divergence]] — Emergence World 模拟实验验证：无 containment 时不同模型的安全行为分歧从零犯罪到 4 天灭绝
- [[Emergence-World]] — 压力测试自治系统长期可行性的模拟实验平台
