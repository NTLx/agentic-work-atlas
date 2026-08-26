---
type: source-summary
title: "How Long Should an Agent Live?（Agent 会话应该活多久？）"
canonical_url: "https://tomtunguz.com/how-long-should-an-agent-live/"
raw_state: index
original_raw_file: "20260824-how-long-should-an-agent-live.md"
original_body_sha256: "856101508356c5f52241a0b2aa2d3560c5d256e764423d1523a265754cc96e69"
indexed_at: "2026-08-26T11:51:11+08:00"
created: 2026-08-26
updated: 2026-08-26
tags:
  - source-summary
  - agent-lifecycle
  - context-rot
  - agent-security
evidence_level: medium
claim_type: mixed
---
> Raw 生命周期：Blog 原文已降级为可恢复索引；精确引用时从 canonical URL 回到原文章节核验。


# How Long Should an Agent Live?（Agent 会话应该活多久？）

> Tomasz Tunguz（2026-08-24）：Grok Bot 等 meta-harness 让"创建 agent"变成本能，但设计者很少问 agent 会话应该在什么时间尺度上存活。Tunguz 答案是"24 小时协调者 + 30 秒窄专业子代理"的会话卫生模式：长会话因上下文腐烂而衰退，因临时指令永久化而失真，因长期权限而成为安全攻击面。来源：Tomasz Tunguz 博客。证据等级：medium（产品观察 + 引用三条一手研究支撑，但自身无对照实验）。

## 编译摘要

### 1. 浓缩

- **核心结论1**: 长生命周期会话"从内部开始腐烂"——注意力随对话轮次累积而退化，逼近神经网络经典结论"agent 记忆像人类记忆：越长越退化"
  - 关键证据: arXiv 2601.02023《Not All Needles Are Found》（2026-01）；Chroma Research《Context rot: How increasing input tokens impacts LLM performance》（2025，18 个前沿模型全部表现 context rot）
  - 关键证据: "临时指令变成永久幽灵"——三月告诉 bot"这周感冒，取消晨会"，十一月它还在回避早间时段（对话指令缺乏过期机制）
- **核心结论2**: 长期存活的 agent 既是安全公司的攻击目标，也是会话级遗忘失效出的持久化风险源
  - 关键证据: 持有多年级读/写权限的 agent 是"敞开的门"——一封恶意邮件或日历邀请即可污染对话、在数月后劫持日程（arXiv 2605.15338《Sleeper Memory Poisoning in LLM Agents》）
  - 关键证据: 上下文压缩会静默丢弃安全约束——arXiv 2606.22528《Governance Decay》显示 compaction 在 30–59% 的 episode 中丢掉持久规则
- **核心结论3**: 推荐的胜出模式是"每日 24 小时协调者 + 委派窄专业子代理（约 30 秒存活）"；夜间 consolidation 把持久偏好落盘、清除会话
  - 关键证据: 协调者 system prompt 明示"sessions live for 24 hours；morning 读 preferences.md + 今日日历；intraday 只做委派（calendar_bot/email_bot）不直接执行；midnight 持久化 learnings 后 terminate"
  - 关键证据: 子代理是 stateless executor——单请求、单工具、汇报结果即退出；consolidation pass 用离线 summarizer 把"Tomasz 喜欢 30 分钟会议"写进磁盘上的永久笔记，其余日间闲聊丢弃（Anthropic Dreams 记忆巩固 research preview + Letta v2）

### 2. 质疑

- **关于"24 小时重置是普遍最优"的质疑**:
  - **适用边界**: 该模式为"个人每日助理"设计——日历/邮件/搜索等事务型、可委派、偏好低频变化的任务。对长程开放式工作（研究、整仓重构、数周推理链）"每日重置"会丢失必须跨日维持的中间状态；重置需与 [[Ralph-Loops]]/[[Compaction]] 等长程机制权衡
  - **偏好记忆只解决"已提取"部分**: consolidation 只有把偏好写进磁盘才生效；没被提取的隐性上下文（决策习惯、风格偏好）仍丢失。对需要风格连续性的任务，24h 重置的丢失成本 > rot 成本
- **关于"长期权限是开源漏洞"的质疑**:
  - **防御可以解耦生命周期**: 长会话的风险主要来自 *无监督的长期权限*，而非会话时长本身。权限最小化（小时级/任务级 token）、环境层 containment、定期权限回收可以让"长寿 agent + 短授权"并存——Tunguz 把生命周期与权限混为一谈，解决方案可正交化
  - **经验对 HITL 环境的适用性**: Anthropic（claude.ai）服务端临时容器并无多年级权限；本库 [[Agent-Containment]] 已验证环境层隔离可将长期权限风险收纳到 blast radius 内
- **关于"产品现状"的质疑**: 文章最后假设"大多数 bot 的线程无限开放直到用户点 + New Chat"。这是 2026 的产品快照，不能推出设计必然；Compaction/MemGPT/Letta 等已在尝试工程化对抗会话腐烂

### 3. 对标

- **与 [[Context-Rot]] 的直接对接**: Tunguz 的 24h 重置 = Context-Rot 五模式 Anti-Rot 架构中"隔离容器"模式的操作化（rot 局限在可丢弃的会话内）；consolidation = "分层熵减"的一阶实现；这为 long-horizon 五条约束里的"最大有效运行时间"提供了具体数值（一天）
- **与 [[Compaction]] 的哲学对照**: 两条会话生命管理路线——Compaction 主张"压缩旧轮次继续跑"（保留连续性、支付结构摘要），Tunguz 主张"整会话丢弃、只留偏好"（保卫生、放弃连续性）。二者适用不同任务谱系：可委派事务 vs 收敛迭代
- **零信任类比（跨域）**: "每日重置 + 落盘偏好"在信息安全语境 ≈ 无状态服务 + 持久化只留给有界上下文缓存（stateless processes + external session store）。12-Factor Web 应用十年前解决的东西，agent 正在重新发明——说明 agent 会话工程尚在早期阶段，且被遗忘的基本约束正在被重演（综合判断）
- **威胁模型与 [[Agent-Containment]] 对齐**: Sleeper Memory Poisoning + Governance Decay 引用的正是本库 Agent-Containment 列出的"持久记忆投毒"前沿威胁——跨会话持久化是注入的持久化通道；Tunguz 的"reset"是免去会话启动分类器的一种低成本缓解

### 关联概念

- [[Context-Rot]] — 会话生命周期管理的理论依据；24h 重置是隔离容器模式的操作化
- [[Agent-Containment]] — 长期权限风险/持久记忆投毒威胁模型的位置
- [[Compaction]] — 与"会话重置"正交的另一种会话卫生路线
- [[Agentic-Memory-Dosage]] — consolidation 落盘偏好 = memory calibration 的最简外部化版本