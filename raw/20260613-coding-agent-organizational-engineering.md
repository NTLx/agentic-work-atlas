---
type: raw
source: "https://mp.weixin.qq.com/s/LA1AFSjb5ffTHDA2xkv0wQ"
author:
  - "AgentScope 社区"
published: "2026-06-13"
created: "2026-06-13"
tags:
  - clippings
  - coding-agent
  - agent-harness
  - organizational-engineering
---
# Coding Agent 下半场：从个人提效到组织级研发体系

当下还在古法手搓代码的开发者都是在奔着非遗传承人的目标去了，绝大多数都已经用上了 Claude Code、Cursor 这类 Coding Agent。方向对了，但场景不同，解法也不同 —— 开发者自己在本地装个 AI 助手提效，和在组织内部搭起一套 AI 驱动的研发协作体系，是完全两个维度的事情。前者已经有成熟的产品了，后者才刚刚开始。本文聊的就是后者。

## 什么是组织级 Coding Agent

2025 年底到 2026 年初，一件有意思的事情发生了：Stripe、Ramp、Coinbase 这三家公司几乎同时公开了各自的内部 Coding Agent —— Stripe 叫 Minions，Ramp 叫 Inspect，Coinbase 叫 Cloudbot。三家公司独立开发，没有互相参考，最终却不约而同地收敛到了几乎相同的架构上。

这不是巧合。当你把 Coding Agent 从"一个人在终端里用"升级成"整个团队通过 Slack / GitHub Issue 随时触发"，你就会被同一组工程问题逼到同一条路上去——你需要沙箱隔离执行环境，需要让 Agent 在中断后能续上之前的工作，需要让它接得住 Slack、GitHub、飞书各种入口，需要防止一个用户的失控循环把全公司的模型额度烧光。

LangChain 团队看到了这个规律。2026 年 3 月，他们发布了 Open SWE —— 一个把 Stripe/Ramp/Coinbase 的共同模式提炼成开源框架的项目。Open SWE 的 README 开头写得很直接：

> Elite engineering orgs like Stripe, Ramp, and Coinbase are building their own internal coding agents — Slackbots, CLIs, and web apps that meet engineers where they already work.

"Meet engineers where they already work" —— 这句话点出了组织级 Coding Agent 的核心设计理念：不是让工程师学一个新工具，而是让 Agent 钻进工程师已经在用的 Slack 频道、GitHub Issue、IM 对话里，变成团队工作流的一部分。

AgentScope Java 2.0 的 AgentScope Harness 模块走的是同一条路。本文以官方示例 agentscope-examples/agents/agentscope-codingagent 为线索，讲清楚一个生产级 Coding Agent 是怎么用 Harness 拼出来的 —— 每一行配置解决了什么问题，怎么从本地 CLI 一路演进到挂在 GitHub Webhook 后面的企业服务。

## 先把定位说清楚

在往下走之前，必须把"我们要做的"和"Claude Code / Cursor 这类本地工具"区分清楚。

Claude Code 优化的是"我一个人写代码更快" —— 你打字、它干活、你看着它干活、你随时打断纠正。状态在你本机，触发者就是你自己，信任边界就是你信你自己的机器。

本文要搭的东西解决的是另一个问题："团队里某个小任务我都不用自己看，扔给 Agent 跑完开 PR 我 review 一下就行"。触发者可能是任何一个 Issue 评论者，Agent 在远端跑十几分钟到一小时，没人盯着。Stripe 的工程师在 Slack 里 @Minions 说句"帮我修这个 bug"，回头收到一个 draft PR —— 这就是组织级 Coding Agent 该有的样子。

Open SWE 把这个哲学总结成一句话：**"Isolate first, then give full permissions inside the boundary."** 先隔离，再放权。AgentScope Harness 的设计一模一样。

### 那厂商的 Cloud Agent 呢？

事实上很多厂商也在提供 SaaS 的产品服务，比如 GitHub Copilot Coding Agent 已经可以在 Issue 上 assign 触发，在云端跑完自动开 draft PR；Claude Code 也有 headless 模式，能在 CI 里被程序化调用。

理念上没有本质区别 —— 沙箱隔离、异步触发、PR 驱动产出 —— 厂商是把头部公司验证过的模式产品化了，做成了开箱即用的 SaaS 服务。而 Stripe、Ramp、Coinbase 这些公司选择自建，更多是出于自身工程体系的特殊性。

## 真正的难题：从"能跑一次"到"7×24 服务一个团队"

### 沙箱：让 Agent 可以放心 rm -rf

Coding Agent 最大的工程矛盾是：你要让模型有真正的执行能力——git clone、npm install、mvn test、任意 shell 命令 —— 但又不能让它误伤宿主。

AgentScope Harness 做了和 Open SWE 同样的抽象 —— FilesystemSpec 是统一接口，Docker 容器、远端 KV、本机文件系统都是可插拔的实现。IsolationScope.SESSION 保证每个 GitHub Issue / PR / IM 对话各跑各的。

### 跨调用恢复：第二轮 call() 才是真考验

用户在 PR 上评了一条"再补个测试"。Agent 必须能接着上一轮的环境继续干。AgentScope Harness 的方案：沙箱在每次 call() 结束时把工作区状态打包成快照存起来，下次按需恢复。快照后端可选 LocalSnapshotSpec、OssSnapshotSpec、RedisSnapshotSpec。

### 长会话记忆：上下文窗口不是无限的

AgentScope Harness 的解法是四套独立可组合的机制：对话摘要压缩、大工具结果卸载（超 80K 字符写到工作区文件）、参数截断、溢出兜底。同时 MEMORY.md 会从每天的对话流水账里周期性合并出长期事实。

### 会话持久化：节点挂了对话不能断

默认模式下用本地文件存储状态。多副本生产切 Redis，一行配置。切到 Redis 之后：节点崩了会话漂到另一个节点，滚动发布时旧 pod 自动保存、新 pod 自动恢复。

## 组织级特有的工程问题

### 多通道接入：同一个 Agent 接得住所有入口

Stripe 的 Minions 走 Slack，Coinbase 的 Cloudbot 也走 Slack，Open SWE 同时接 Slack + Linear + GitHub。组织级 Coding Agent 的一个共识是：不要让用户换到一个新的界面去找 Agent，让 Agent 出现在用户已经在用的地方。

Coding Agent 通过通道适配器把不同入口的事件统一映射到 (threadId, message)：github:issue:owner/repo#42 → SHA-256 → UUID → coding agent thread。确定性映射保证同一个 Issue 的所有评论都路由到同一个 Agent session。

### 多租户隔离：谁和谁不能串

AgentScope Harness 用 IsolationScope 控制隔离粒度。SESSION（默认）让每个 sessionId 独立一个沙箱。USER 让同一用户的多个对话共享同一份仓库克隆。隔离不只是沙箱层面的 —— 会话状态、记忆、子 Agent 任务也都按同样的粒度隔离。

### 并发控制：一个 thread 同一时间只跑一个推理

Coding Agent 用 RunDispatcher + MessageQueueHook 强制保证。ThreadBudgetHook 管住每个 thread 的模型调用上限，ModelCallLimitHook 管住全局。

### 工作区：人格、记忆、技能都是文件

AgentScope Harness 把所有跨调用、跨重启需要保留的东西组织成一个目录 —— workspace。行业里现在把这类设计叫"Context Engineering"。几乎所有主流 Coding Agent 都独立走到了同一个模式：Claude Code 有 CLAUDE.md，GitHub Copilot 有 .github/copilot-instructions.md，Open SWE 有 AGENTS.md。

### 子 agent：把独立任务委派出去

在 workspace 里写一个 markdown 文件即可声明子 Agent。主 Agent 调用 agent_spawn，子 Agent 在隔离上下文里跑完返回结果。

### Plan Mode：大改之前先想清楚

开启后 Agent 进入只读阶段，只能调用读取工具和 plan 相关的白名单工具，退出 plan 需要人类确认。和 Coinbase Cloudbot 的"Agent Councils"理念类似。

### 工具精选与确定性兜底

Stripe 的 Agent 有约 500 个工具，但强调"tool curation matters more than tool quantity"。Open SWE 只暴露约 15 个核心工具。

关键步骤要用确定性逻辑保证：GitHub Copilot Coding Agent 跑完后走 CI pipeline 验证；Open SWE 有 open_pr_if_needed middleware 兜底。Draft PR 作为输出契约——Agent 不直接改生产代码。

## 从单机到企业：一条演进路线

**Stage 1：本机 CLI。** 什么都不配。execute 在宿主 sh -c 跑，状态存本地文件。
**Stage 2：本机 + Docker 沙箱。** 加一行 .filesystem(new DockerFilesystemSpec()...)，所有执行进容器。
**Stage 3：多副本 + 分布式。** stateStore 换 Redis，沙箱快照存 OSS，加 executionGuard 做并发控制。
**Stage 4：可观测与限流。** Spring Boot Actuator 暴露健康探针和 Prometheus 指标，ThreadBudgetHook 和 ModelCallLimitHook 守住模型预算。

回顾一下 —— Stripe Minions、Ramp Inspect、Coinbase Cloudbot、LangChain Open SWE、GitHub Copilot Coding Agent、Claude Code、AgentScope Harness —— 在核心架构决策上高度一致：per-session 隔离沙箱、确定性的 thread ID 路由、middleware 拦截链、Agent 运行时的 message queue 注入、repo 级指令文件、draft PR 作为输出契约。

Coding Agent 的上半场是个人提效，下半场的战场转到了工程：怎么把"能跑一次 demo"变成"7×24 稳定服务一整个团队"。
