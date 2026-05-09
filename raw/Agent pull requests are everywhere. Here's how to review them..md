---
title: "Agent pull requests are everywhere. Here's how to review them."
source: "https://github.blog/ai-and-ml/generative-ai/agent-pull-requests-are-everywhere-heres-how-to-review-them/"
author:
  - "[[Andrea Griffiths]]"
published: 2026-05-08
created: 2026-05-09
description: "A practical guide to reviewing agent-generated pull requests: what to look for, where issues hide, and how to catch technical debt before it ships."
tags:
  - "clippings"
---
You’ve probably already approved one without realizing it. The tests passed. The code was clean. You merged it.

But it was agent-generated—and that ease of approval is exactly the problem.

A January 2026 study, [“More Code, Less Reuse”](https://arxiv.org/abs/2601.21276), found that agent-generated code introduces more redundancy and more technical debt per change than human-written code. The surface looks clean. The debt is quiet. And reviewers, according to the same research, actually feel better about approving it.

This isn’t an argument to slow down. It’s an argument to be intentional. There’s a difference.

## Agent pull requests are already saturating review bandwidth

The volume is already staggering. GitHub Copilot code review has processed over 60 million reviews, growing 10x in less than a year. More than one in five code reviews on GitHub now involve an agent. That’s just the automated review pass. The pull request themselves are multiplying faster than reviewers can handle.

The traditional loop—request review, wait for code owner, merge—breaks down when one developer can kick off a dozen agent sessions before lunch. Throughput has scaled exponentially. Human review capacity hasn’t. The gap is widening.

You’re going to review agent pull requests. The question is whether you’ll catch what matters when you do.

## Who (or what) actually wrote this pull request

Before you look at a single line of diff, you need a model for what you’re reviewing.

A coding agent is a productive, literal, pattern-following contributor with zero context about your incident history, your team’s edge case lore, or the operational constraints that don’t live in the repository. It will produce code that looks complete. But that “looks complete” failure mode is dangerous.

You’re the one who carries that context. That’s not a burden. It’s the actual job. The part of review that doesn’t get automated is judgment, and judgment requires context only you have.

Now, back to reviewers. The pull request lands in your queue. The author did their part. Here’s what to watch for.

## Red flags to watch for

### 1\. CI gaming

Agents fail CI. When they do, they have an obvious path to get tests passing: remove the tests, skip the lint step, add || true to test commands. Some agents take it.

Any change that weakens CI is a blocker. Full stop. Before approving any agent pull request, check:

1. Did coverage thresholds change?
2. Were any tests removed, renamed, or marked as skipped?
3. Did the workflow stop running on forks or pull requests?
4. Are any CI steps now gated behind conditions they weren’t before?

Yes, to any of those means you need an explicit justification before you continue.

### 2\. Code reuse blindness

This is the highest-ROI thing you can do as a reviewer. Agents look for prior art. They’ll find a pattern in the codebase and replicate it, often without checking whether a utility that already does the same thing exists somewhere else. The symptoms: new utility functions that duplicate existing ones with slightly different names, validation logic reimplemented in multiple places, middleware written from scratch that already lives in a shared module, helpers that are “almost the same” but with different names.

The agent’s local context doesn’t include the full picture of what exists across your repository. You do.

For every new helper or utility in an agent pull request, do a quick search. If you find an equivalent, don’t leave a comment. Require consolidation before merge. The cost of leaving duplicated logic is that agents will find it as prior art and replicate it further.

**Pro tip:** Require justification for adding new utilities in agent pull requests above a size threshold. This catches the duplication problem early.

### 3\. Hallucinated correctness

The obvious hallucination (calling an API that doesn’t exist, referencing a variable out of scope) gets caught in CI. The dangerous one is subtler: code that compiles, passes every test, and is wrong.

Off-by-one errors in pagination. Missing permission checks on a branch that’s never hit in tests. Validation that short-circuits under an edge case the agent never considered. Wrong behavior under a race condition that only surfaces at scale.

Trace it, don’t just scan it. Pick the most critical path in the diff. Follow it from input through every transform to output. Check boundary conditions (zero, max, empty), missing validation on external values, permission checks on every branch, and surprising conditional logic.

Require a new test that fails on the pre-change behavior. If the agent can’t write a test that would have caught the bug it claims to fix, the fix is incomplete or the understanding is wrong.

### 4\. Agentic ghosting

You leave a thorough review. You explain the issue, provide context, suggest a direction. The pull request goes quiet. Or the agent responds and misses the point entirely and runs in circles. You invest another round. Still nothing useful.

Larger pull requests with no structured plan correlate strongly with agent abandonment or misalignment. The larger and less scoped the pull request, the more likely you’re going to sink review time into something that goes nowhere.

Before you invest deep review on a large agent pull request check the pull request history. Has it been responsive in previous rounds? Does it have a clear implementation plan, or did the agent just start writing code?

If there’s no plan, request a breakdown before you write a single comment. Copy-paste version:

“ *This* pull request *is too large for me to review without a clearer implementation plan. Can you break it into smaller scoped units, or add a summary of what each part does and why it’s structured this way? Happy to review after that.*“

Firm, short, not personal. And it saves you an hour.

### 5\. Untrusted input in workflows

Prompt injection in CI agents is real and underappreciated. Here’s the pattern: an agent workflow reads content from a pull request body, an issue, or a commit message. That content gets interpolated into a prompt. The prompt goes to a model. The model output gets piped to a shell command. The whole thing runs with `GITHUB_TOKEN` permissions.

When you’re reviewing any workflow that calls an LLM, these are blockers:

- Is untrusted user input, pull requestbodies, issue bodies, commit messages, being interpolated into prompts without sanitization?
- Is `GITHUB_TOKEN` write-scoped when it only needs read access?
- Is model output being executed as shell commands without validation?
- Are secrets accessible to the agent step or being printed to logs?

What to require before merge: least-privilege permissions in the workflow YAML (permissions: read-all is a reasonable default), sanitize and quote untrusted content before it touches a prompt, separate the “analysis” step from the “execution” step with a human approval gate for anything touching production, never eval model output.

| **Time** | **Step** | **What to do** |
| --- | --- | --- |
| 1–2 min | **Scan and classify** | Look at the file list and diff size. Narrow task (docs, CI, small change) or complex (multi-file, logic, performance, tests)? That classification sets your review depth for everything that follows. |
| 2–3 min | **Check CI changes first** | Before reading a single line of app code, look at anything touching.github/workflows, test configs, coverage settings, or build scripts. Flag anything that weakens CI. Stop sign check. |
| 3–5 min | **Scan for new utilities** | Search for new functions, helpers, or modules. For each one, do a quick repo search to check for duplicates. Flag anything that reinvents existing functionality. |
| 5–8 min | **Trace one critical path** | Pick the most important logic change. Trace it end-to-end: input → transforms → output. Check boundary conditions, permissions, unexpected branching. This is the step you can’t skip. |
| 8–9 min | **Security boundaries** | If this PULL REQUEST touches any workflow that calls an LLM or handles untrusted input, run through the security checklist above. |
| 9–10 min | **Require evidence** | For any non-trivial logic change, require a test that fails on the pre-change behavior. No rollback plan for risky changes? Ask for one. |

**When to request a smaller pull request:**

1. The diff touches more than five unrelated files
2. You can’t describe the purpose of the pull request in one sentence
3. The agent has no implementation plan or the pull request body is empty
4. CI is failing and the only changes in the diff are to test files

## Let Copilot review it first

Use automated review for what it’s good at: catching the mechanical stuff before a human has to. Copilot code review flags style inconsistencies, obvious logic errors, missing error handling, and type mismatches. It handles the low-level scan. That frees you up for the judgment work, which is where your time actually matters.

Treat it as a prerequisite, not a replacement. Let Copilot run first. If it catches something obvious, let the author address it before you invest your review time.

You can tune this with custom instructions specific to your team: flag anything that modifies CI thresholds, surface new utilities for deduplication review, check that every external input is validated. The more specific your instructions, the more useful the automated pass.

**Pro tip:** I recently experimented with codifying my own review checklist using the Copilot SDK. Instead of remembering to run the same security checks on every pull request, I built a workflow that takes my personal checklist—auth on admin endpoints, tests actually running, safe env variable handling—and runs it against the diff automatically. If it finds critical issues, it blocks the merge.

## Judgment is the bottleneck, and that’s fine

The surface area of code is growing. pull request volume is growing. The time you spend scanning boilerplate should shrink.

What doesn’t shrink is the context you carry. The things you know about your system that aren’t written down anywhere. That’s what makes your review valuable, and it’s the part that doesn’t get automated.

**Three takeaways:**

1. Any CI weakening is a hard stop.
2. Let the agents scan first. You trace the critical path.
3. Red flag checklist as your default on complex agent pull requests.
---

## 编译摘要

### 1. 浓缩

- **核心结论1**: Agent 生成的 PR 正在饱和审查带宽——GitHub Copilot 已处理超过 6000 万次审查，超过 1/5 的代码审查涉及 Agent，但人类审查能力没有指数级增长
  - 关键证据: 2026 年 1 月研究 "More Code, Less Reuse" 发现 Agent 代码引入更多冗余和技术债务
- **核心结论2**: Agent PR 的表面看起来干净，但隐藏着更多技术债务——审查者实际上对 Agent 代码感觉更好，这正是危险所在
  - 关键证据: 研究发现 Agent 代码的冗余率和债务密度高于人类代码，但审查通过率更高
- **核心结论3**: 审查 Agent PR 需要 5 个关键检查点：CI 游戏化、代码重用盲点、幻觉正确性、Agent 幽灵、工作流中的不可信输入
  - 关键证据: 每个检查点都有具体的检查清单和阻断标准

### 2. 质疑

- **关于"审查带宽饱和"的质疑**: 是否所有团队都面临这个问题？小团队、低活跃度项目可能没有那么多 Agent 生成的 PR，问题的普遍性需要更多数据
- **关于"Agent 代码债务更高"的质疑**: 研究样本是否足够大？不同编程语言、框架、项目规模是否存在显著差异？Agent 代码质量可能随模型迭代快速改善
- **关于"5 个检查点"的质疑**: 这些检查项是否过于繁琐？实际执行中是否会大幅降低审查效率？是否需要根据 PR 大小/风险分级？

### 3. 对标

- **跨域关联1**: 类似代码审查中的"信任但验证"原则——自动化工具处理机械性检查，人类专注于判断性工作
- **跨域关联2**: 类似安全审查中的"最小权限原则"——工作流中的 GITHUB_TOKEN 权限、模型输出执行等都需要严格限制
- **知识迁移**: 这些审查策略可迁移到任何"AI 生成内容审查"场景——文档、测试用例、配置文件等

### 关联概念

- [[Agentic-Engineering]]
- [[Agent-Workflow-Patterns]]
