---
type: source-summary
title: "How Warp Builds Self-Improving Agents on Claude"
canonical_url: "https://claude.com/blog/how-warp-builds-self-improving-agents-on-claude"
raw_state: index
original_raw_file: "20260826-warp-self-improving-agents-on-claude.md"
original_body_sha256: "13d351d8fbeb81bb399811f06be48ac671a857cd6fc8b12d524001fe895d7c14"
indexed_at: "2026-08-27T11:56:37+08:00"
created: 2026-08-26
updated: 2026-08-27
tags:
  - source-summary
  - self-improving-agent
  - agent-skills
  - feedback-loop
  - agentic-engineering
evidence_level: medium
claim_type: mixed
---
> Raw 生命周期：Anthropic 原文已降级为可恢复索引；精确引用时从 canonical URL 回到原文核验。


# How Warp Builds Self-Improving Agents on Claude

> Anthropic 企业案例（2026-08）：Warp（AI 终端，800K 月度开发者，56% 财富 500，累计 1000 万次 Claude Code 会话）用**双 skill 框架**构建自我改进 agent——base skill 承载领域知识，improver skill 作为观察者 agent 周期性聚合人类反馈并微调 base skill。核心洞见：反馈到 agent 通常随会话结束消失，而文件化的 skill 让改进可沉淀、可评审、可回滚。来源：Anthropic 官方博客。证据等级：medium（一手企业案例 + 已投产规模数据；但为宣传性质，自改进循环的定量收益未给指标）。

## 编译摘要

### 1. 浓缩

- **核心结论1**: 反馈会随会话结束消失——这是 agent 改进无法累积的根本障碍；解决方式是把改进载体从"对话上下文"移到"文件化 skill"
  - 关键证据: 工程师抱怨内部 code review agent 输出低质；手工改写 prompt 与改进 AGENTS.md 都是临时解，不 scale
  - 关键证据: "feedback to an agent, no matter what its purpose, typically disappears when the session ends, removing critical context from the agentic loop"
- **核心结论2**: 双 skill 架构——base skill（领域知识）+ improver skill（观察者 agent）在人类反馈中闭合自改进循环
  - 关键证据: inner/base skill 持有功能领域知识与指令（如 PR 打开时 code agent 执行审查）；outer/improver skill 定时运行（非每任务），拉取累积反馈、对比"agent 建议 vs 人类如何回应"、提出 base skill 的小聚焦编辑
  - 关键证据: skill 是纯文件（plain files），agent 极擅更新；更新可评审、可批准、可合并，走正常 PR/代码审查流——合并后 inner skill 下次运行即继承改进
- **核心结论3**: 反馈质量 > 数量，但数量有帮助；低摩擦捕获 + 具体解释"为什么"的反馈最有价值
  - 关键证据: "detailed, domain-specific feedback from a senior engineer 可抵大量草率反馈"；binary thumbs up/down 不解释 why
  - 关键证据: 低摩擦关键——在人们已工作的地方捕获（PR/issue 评论直标），自动化无额外提交步骤；"Low friction is what keeps signal flowing"
- **核心结论4**: improver skill 是高度可复用的机制——跨用例的 improver skill 差异很小，值得投入重写
  - 关键证据: "the improver skill for a code review agent is not that different from the improver skill for any other agent"——domain-specific 部分外是通用机制

### 2. 质疑

- **关于"skills 用于自改进"与 [[Lessons-MD-Self-Improvement]] 的关系**: 两者同构（反馈沉淀到文件 + agent 用文件改进），但载体与触发不同——lessons.md 是事故后自动 append + "promote 到 investigation skill"的**两级蒸馏**；Warp 是 improver 观察者定期拉取反馈后**主动编辑 base skill**。Warp 没有"何时 promote"的模糊性（improver 直接改），成本是每 agent 需要一条 improver
- **关于"改进走 PR 流程"的局限**: 手动 PR 评审让"改进"受制于人类 reviewer 吞吐；对规模化（Warp 全开源 repo，数百贡献者上千评审）该瓶颈可承受，但对更大组织是扩展性疑问。且"反馈是错的"场景——文章自己提醒"assume it will be"，但未给滤波器病防错的具体机制（只提"context to sanity-check + human in loop"）
- **关于证据密度**: 数据点（10M sessions、400K/周、40M conversations）是营销性规模展示，自改进循环本身的量化收益（skill 更新后 review 质量提升多少）未给指标——这是宣传案例的普遍证缺
- **关于适用边界**: 双 skill 循环假设"领域知识可文件化 + 反馈可显式表达"。对无法言明的隐性知识（审美判断、风格品味）、或反馈频率过低的低频任务，循环可能空转；"domain verifiable"与否的处理建议（verification harness first vs evals vs restricted human）区分了这一点但未深入

### 3. 对标

- **与 [[Meta-Harness-Optimization]] 的载体对照**: 两者都是"外层反馈环改进系统"——Meta-Harness 改 harness **代码**（有 acceptance gate 防过拟合）；Warp 改 agent skill **文件**（人类 PR 评审当 gate）。Warp 的 gate 是人类 reviewer（软 gate），Meta-Harness 是 J_train ∧ J_dev（硬 gate）——**改进载体 + 门禁机制的两端**
- **与 [[Lessons-MD-Self-Improvement]] 的最直接对照**: 同是"反馈→文件→改进"，但 Lessons-MD 是 incident 驱动的**promote 两级蒸馏**（短期 lessons.md → 长期 skill），Warp 是 improver 主动的**skill 单级编辑**（评价后直接改 base skill）——前者累积后 promote，后者持续直接改
- **与 [[Skills-as-Products]] 的治理对接**: skill 文件走 PR 评审流 = skill 变更被当作 artifact 治理；"写原则不写规则"（"instructing a smart person, not programming a computer"）+ 渐进披露（small file + 引用资源文件）正是 skill 工程的最佳实践，与库内 skill 治理同源
- **跨域类比：双 skill 循环 ≈ 制造中的 PDCA**: base skill（标准作业程序）+ improver（质量审核员定期抽样、提出工序改进、变更走审批）——这是质量管理的 PDCA 环在 agent 技能层的重演（跨域联想，综合判断）
- **"反馈消失"问题 ≈ 软件工程的 issue 搁置**: 会话结束后反馈消失，类比 bug report 不被记录成 issue 就随对话丢失——把反馈固化为文件（skill PR）是把"口头教训"变成"可追溯变更"的 agent 版

### 关联概念

- [[Lessons-MD-Self-Improvement]] — 同族机制：反馈→文件→改进，载体与触发不同
- [[Meta-Harness-Optimization]] — 外层反馈环改系统，载体是 harness 代码（vs skill 文件）
- [[Skills-as-Products]] — skill 治理框架，Warp 是 file-based skill 的实例
- [[Recursive-Self-Improvement]] — 模型层 RSI vs harness/skill 层的系统层改进
- [[Agent-Loops]] — 内层执行 + 外层改进的双环结构