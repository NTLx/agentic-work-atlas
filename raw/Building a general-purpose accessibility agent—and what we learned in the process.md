---
title: "Building a general-purpose accessibility agent—and what we learned in the process"
source: "https://github.blog/ai-and-ml/github-copilot/building-a-general-purpose-accessibility-agent-and-what-we-learned-in-the-process/"
author:
  - "[[Eric Bailey]]"
published: 2026-05-16
created: 2026-05-16
description: "Learn about the experimental general-purpose accessibility agent that GitHub is piloting."
tags:
  - "clippings"
---
It is an understatement to say agents have become a popular way of working with code. GitHub has adopted agent-based code creation and editing for many of its initiatives, including **piloting an agent to help with** [**our commitment to accessibility**](https://github.blog/news-insights/company-news/github-accessibility-and-the-disability-divide/).

GitHub is currently piloting an experimental general-purpose accessibility agent to achieve two main goals:

1. Providing engineers with **reliable, just-in-time answers to accessibility questions** in the GitHub Copilot CLI and the Copilot VS Code integration.
2. Catching and **automatically remediating simple, objective accessibility issues** before they go to production.

For purpose number two, the accessibility agent is set to automatically evaluate changes that modify our front-end code.

To date, the agent has **reviewed 3,535 pull requests, with a 68% resolution rate**. In order of occurrence, the top five issue types center around:

1. [Making structure and relationships clear to assistive technologies](https://www.w3.org/WAI/WCAG22/Understanding/info-and-relationships.html)
2. [Providing clear and concise names for interactive controls](https://www.w3.org/WAI/WCAG22/Understanding/name-role-value.html)
3. [Ensuring users are aware of important announcements](https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html)
4. [Ensuring there are text alternatives for non-text content](https://www.w3.org/WAI/WCAG22/Understanding/non-text-content.html)
5. [Moving keyboard focus through pages and views in a logical order](https://www.w3.org/WAI/WCAG22/Understanding/focus-order.html)

Each of these issue types represents friction and barriers automatically removed that would have otherwise inhibited use of GitHub for people who use and rely on assistive technology. Here’s a screenshot of it in action:

![A GitHub Actions bot comment on a line of code in a Pull Request that suggests a fix to a content order accessibility issue. The comment reads, 'WCAG 1.3.2 Meaningful Sequence: The .header CSS class uses flex-direction: row-reverse, which causes the close button to appear first in the DOM (and screen reader reading order) but visually renders after the heading. This creates a mismatch between the programmatic reading sequence and the visual layout. A simpler approach is to swap the element order in the DOM and use regular flex-direction: row in the CSS, so the reading order matches what sighted users see:' Following that is a code suggestion that re-orderes the heading and side panel toolbar, with the option to commit the suggestion to code. After that is a final comment that reads, ''This also requires updating •header in agent-task-content.module.css to change flex-direction: row-reverse → flex-direction: row." Cropped screenshot.](https://github.blog/wp-content/uploads/2026/05/image1.png?w=1620)

A GitHub Actions bot comment on a line of code in a Pull Request that suggests a fix to a content order accessibility issue. The comment reads, 'WCAG 1.3.2 Meaningful Sequence: The.header CSS class uses flex-direction: row-reverse, which causes the close button to appear first in the DOM (and screen reader reading order) but visually renders after the heading. This creates a mismatch between the programmatic reading sequence and the visual layout. A simpler approach is to swap the element order in the DOM and use regular flex-direction: row in the CSS, so the reading order matches what sighted users see:' Following that is a code suggestion that re-orderes the heading and side panel toolbar, with the option to commit the suggestion to code. After that is a final comment that reads, ''This also requires updating •header in agent-task-content.module.css to change flex-direction: row-reverse → flex-direction: row." Cropped screenshot.

Interested? We’ll be **outlining successes and lessons learned** with this experiment, with the hopes that it can help with other teams’ accessibility journeys.

## Mindset

[The social model of disability](https://en.wikipedia.org/wiki/Social_model_of_disability) teaches us that access barriers—and consequently impairment—can be created because of how an environment is built. The same thinking applies to digital experiences.

With the accessibility agent, **we are not attempting to “solve” accessibility** in isolation. We are instead attempting to **augment our peers’ efforts**, to better help them remove the barriers that may be created as a result of how we construct GitHub’s user interfaces.

**The accessibility agent is not a “silver bullet”** that can automatically address every hypothetical scenario. Understanding, honoring, and socializing this better helps set the agent’s scope of responsibility. This sped up the experiment’s launch, leading to more buy-in for the effort.

## Past efforts

[The European Accessibility Act](https://commission.europa.eu/strategy-and-policy/policies/justice-and-fundamental-rights/disability/european-accessibility-act-eaa_en) is now in effect. [Title II of the Americans with Disabilities Act](https://www.ada.gov/law-and-regs/regulations/title-ii-2010-regulations/) is set to establish meeting WCAG 2.1 AA as the legal definition of done in April of 2027. LLM agents can read and take action on [the accessibility tree](https://www.nngroup.com/articles/ai-agents-as-users/#:~:text=Accessibility%2DTree%20Parsing).

To say it plainly: **Organizations will be at a disadvantage if they have not already invested in manually identifying and remediating accessibility issues**. There are many reasons for this, including building an accessibility agent.

To that point, GitHub has a mature system in place for logging accessibility issues, as well as verifying fixes to issues are working as intended. This includes:

- A structured template for reporting problems
- Steps to reproduce the issue
- A rich layer of metadata about the issue’s severity level, service area, and applicable [WCAG success criterion](https://www.w3.org/TR/WCAG22/)
- Crosslinks to the Pull Request that addressed the issue
- Acceptance criteria

In addition, all the issues are centralized to a single repository. While this issue-logging effort predated the explosion in popularity of LLM tooling, its highly consistent and structured nature made it **an ideal corpus of content** for the accessibility agent to reference.

Because of this, we instructed the agent to investigate these issues to see if there are related code and language snippets it can extrapolate from. This is one area where the non-deterministic “fuzzy matching” behavior of LLMs acts as an asset rather than a possible liability.

### Old gold

Much like with any other specialized domain area, vague instructions in a skill file won’t cut it. Telling an LLM to “use accessibility best practices” with a short list of examples won’t work well.

When generating code, [**LLMs have an unfortunate bias towards producing accessibility antipatterns**](https://microsoft.github.io/a11y-llm-eval-report/) since every major LLM currently available is trained on decades of inaccessible code.

To counteract this, the agent needs better content to draw from.

So, **I enthusiastically recommend investing in manually cataloging and remediating accessibility issues**. After some progress, this data can be incorporated into the agent.

The issues and their corresponding pull requests provide highly contextual examples for the LMM to reference, written using the conventions set up by the organization it is deployed in. This collection of issues and code is by far one of the strongest assets the agent draws from.

## Efficient token consumption

**Accessibility is a holistic concern**, intersecting with code, design, copywriting, and numerous other disciplines involved with creating user interfaces.

A lot of accessibility work is also **highly contextual**, meaning that someone typically needs the full working picture of a problem before they’re able to give the appropriate advice for what to do.

Because of these two factors, a general-purpose accessibility agent can consume a ton of tokens when it performs work. This has three negative outcomes:

1. An increased amount of unreliable output
2. Slower response times
3. Increased operational costs

It’s important to be diligent when structuring the agent. Here’s how we went about doing just that.

### Use sub-agents

The accessibility agent started as a single monolithic agent, but quickly grew past the limitations of this approach. Because of this, we evolved it to use a [sub-agent architecture](https://dev.to/goose_oss/agents-subagents-and-multi-agents-what-they-are-and-when-to-use-them-39na#:~:text=The%20Subagent%20Setup%3A%20Orchestrator%20With%20a%20Crew).

A lot of guides recommend creating a large suite of sub-agents, each with its own specific area of responsibility. Here, the sub-agents are executed in parallel, with the main agent reconciling their output.

Surprisingly, **this approach worked against us** for the accessibility agent. Instead, we wound up using two dedicated sub-agents:

1. The first sub-agent acts as a **passive reviewer and researcher.**
2. The second sub-agent acts as an **active implementer.**

The two sub-agents are sandboxed and cannot directly pass content to each other. Instead, they generate a structured, templatized output. This output is then served to the parent orchestrating accessibility agent to consume, validate, and route.

![A diagram demonstrating how the parent accessibility agent passes work sequentially from itself to a read-only reviewer sub-agent, then back to the parent agent, to a write and read-capable implementer sub-agent, then back again to the parent agent. The parent agent is contained in a column labeled, 'Tier 1 - Orchestration', and the two sub-agents are contained in a column labeled, 'Tier 2 - Specialists'. The first connecting line that shows the parent agent passing work off to the reviewer sub-agent is labeled, 'run sub-agent'. The second line that passes work back to the parent agent is labeled, 'structured findings'. The third line has the parent agent passing work to the implementer sub-agent, and is labeled 'Run sub-agent with structured findings'. The fourth and final line passes work from the implementer sub-agent back to the parent agent and is labeled, 'Changes or guidance generated'. The parent and sub-agents also have lists of responsibilities. The parent accessibility agent routes requests, locates code and skills, runs complexity scoring, validates outputs, manages escalation gates, manages re-audit loops, and answers research questions. The reviewer sub-agent  performs code audits, WCAG research, detects escalation triggers, and produces structured findings. The implementer sub-agent has two modes: a default code-change mode and a fallback guidance-only mode. The code-change mode fixes critical issues first, then addresses the rest. The guidance-only mode generates guidance docs. Both modes validates changes.](https://github.blog/wp-content/uploads/2026/05/image2.png?w=3000)

A diagram demonstrating how the parent accessibility agent passes work sequentially from itself to a read-only reviewer sub-agent, then back to the parent agent, to a write and read-capable implementer sub-agent, then back again to the parent agent. The parent agent is contained in a column labeled, 'Tier 1 - Orchestration', and the two sub-agents are contained in a column labeled, 'Tier 2 - Specialists'. The first connecting line that shows the parent agent passing work off to the reviewer sub-agent is labeled, 'run sub-agent'. The second line that passes work back to the parent agent is labeled, 'structured findings'. The third line has the parent agent passing work to the implementer sub-agent, and is labeled 'Run sub-agent with structured findings'. The fourth and final line passes work from the implementer sub-agent back to the parent agent and is labeled, 'Changes or guidance generated'. The parent and sub-agents also have lists of responsibilities. The parent accessibility agent routes requests, locates code and skills, runs complexity scoring, validates outputs, manages escalation gates, manages re-audit loops, and answers research questions. The reviewer sub-agent performs code audits, WCAG research, detects escalation triggers, and produces structured findings. The implementer sub-agent has two modes: a default code-change mode and a fallback guidance-only mode. The code-change mode fixes critical issues first, then addresses the rest. The guidance-only mode generates guidance docs. Both modes validates changes.

There are a few reasons for this approach:

- **Escalation checkpoints**. The reviewer checks for areas where human intervention will likely be needed. This includes multiple high-severity WCAG failures, as well as a list of patterns that are known to be difficult to make accessible.
- **Complexity-based behavior**. The agent is instructed to operate in a specialized guidance-only mode if the underlying code is deemed too complicated. Here, the parent accessibility agent acts as an arbiter, while the reviewer agent is “opinionless” and just reports the findings as instructed.
- **Filtering**. The reviewer presents everything it finds. The parent accessibility agent then utilizes resources and skills to determine what is relevant to the request. The reviewer passing all its findings to the implementer would be costly and potentially set it on irrelevant and counter-productive tasks.
- **Traceability**. Direct communication between sub-agents would remove the ability to create and review an audit trail of user and agent decisions. This is important given the agent’s instruction around complex patterns, as well as the highly contextual nature of accessibility work.

### Execute instructions in a linear order

In addition to being a holistic concern, effective digital accessibility work also demands a methodical, detail-oriented approach.

The concern of using sub-agents to increase the speed of the LLM’s reply is counterbalanced by our need for its results to be accurate. We found that **compelling the agent to execute its sub-agent instructions in a fixed order** was key.

We first establish a parent set of ordered phases. Each phase itself contains child ordered steps of instructions, which are accompanied by relevant resources and skills:

![A diagram demonstrating how the research sub-agent uses ordered phases and ordered steps within each phase to produce structured output. The first phase is labeled, 'Phase 1 - Research', and contains 5 steps. The first step is labeled, 'WCAG SCs' and uses a skill called 'wcag-2.2-level-a-aa-success-criteria'. The second step is labeled, 'GitHub’s SC interpretation' and uses a skill called 'accessibility-check-wcag-sc-interpretation'. The third step is labeled, 'Assistive technology support' and uses a skill called 'accessibility-check-at-support'. The fourth step is labeled, 'Prior accessibility audits' and uses a skill called 'accessibility-search-prior-audits-general'. The fifth and final step for this phase is labeled, 'External W3C references' and is governed by a rule called 'Only if local searching is insufficient'. An arrow connects the first phase to the second phase, which is labeled, 'Phase 2 - Code audit'. The first step of phase 2 is labeled, 'Read source files on demand'. The second step is labeled, 'Incorporate user-provided URLs' and has a role called that compels it to always fetch. The third step is labeled, 'Investigate provided URLs’ links' and is governed by a rule called 'search 1 level deep'. The fourth step is labeled, 'Run validation skills' and uses a resource called 'decision table'. The fifth step is labeled, 'Cross-reference findings' and uses a skill called 'use phase 1 research'. The sixth and final step of this phase is labeled, 'Re-review all content interacted with'. An arrow connects the second phase to the third phase, which is labeled, 'Phase 3 - Structured output'. The third phase contains a single step labeled, 'Findings report, output-schema-reviewer'. It has three subsections, 'Summary', 'Finding severity scoring', and 'Each finding includes'. The summary subsection contains an ordered list that reads, '1. total findings', '2. prior audits', '3. escalation needed', '4. escalation scope', and '5. Escalated findings'. Finding and severity scoring has three levels, 'critical', 'warning', and 'info'. Each finding includes applicable WCAG SCs, applicable files and line numbers, current human-facing experience, expected human-facing experience, suggestion for remediation, and an escalation summary (if present).](https://github.blog/wp-content/uploads/2026/05/image3.png?w=3000)

A diagram demonstrating how the research sub-agent uses ordered phases and ordered steps within each phase to produce structured output. The first phase is labeled, 'Phase 1 - Research', and contains 5 steps. The first step is labeled, 'WCAG SCs' and uses a skill called 'wcag-2.2-level-a-aa-success-criteria'. The second step is labeled, 'GitHub’s SC interpretation' and uses a skill called 'accessibility-check-wcag-sc-interpretation'. The third step is labeled, 'Assistive technology support' and uses a skill called 'accessibility-check-at-support'. The fourth step is labeled, 'Prior accessibility audits' and uses a skill called 'accessibility-search-prior-audits-general'. The fifth and final step for this phase is labeled, 'External W3C references' and is governed by a rule called 'Only if local searching is insufficient'. An arrow connects the first phase to the second phase, which is labeled, 'Phase 2 - Code audit'. The first step of phase 2 is labeled, 'Read source files on demand'. The second step is labeled, 'Incorporate user-provided URLs' and has a role called that compels it to always fetch. The third step is labeled, 'Investigate provided URLs’ links' and is governed by a rule called 'search 1 level deep'. The fourth step is labeled, 'Run validation skills' and uses a resource called 'decision table'. The fifth step is labeled, 'Cross-reference findings' and uses a skill called 'use phase 1 research'. The sixth and final step of this phase is labeled, 'Re-review all content interacted with'. An arrow connects the second phase to the third phase, which is labeled, 'Phase 3 - Structured output'. The third phase contains a single step labeled, 'Findings report, output-schema-reviewer'. It has three subsections, 'Summary', 'Finding severity scoring', and 'Each finding includes'. The summary subsection contains an ordered list that reads, '1. total findings', '2. prior audits', '3. escalation needed', '4. escalation scope', and '5. Escalated findings'. Finding and severity scoring has three levels, 'critical', 'warning', and 'info'. Each finding includes applicable WCAG SCs, applicable files and line numbers, current human-facing experience, expected human-facing experience, suggestion for remediation, and an escalation summary (if present).

The interesting bit about this linear order is that it mirrors how I would personally approach performing auditing, remediating, and reporting duties.

### Use a template schema pass around sub-agent content

The entire operation of the sandboxed sub-agents is built around template schema files. These files **create consistency** that is vital to keeping the agent focused and on track.

The two schema templates are:

1. **Reviewer template schema:** This focuses on what to audit, and how to find applicable information about it.
2. **Implementer template schema:** This focuses on what to fix and how to fix it.

Without the schema files in place, the agents would all attempt to arbitrarily communicate with each other. This would create increased token expenditure, undesirable hallucinations, unnecessary code changes, and difficult-to-impossible behavior for agent auditing purposes.

## Acknowledging limitations

Another vital aspect of creating the accessibility agent is **understanding areas where agents can fall short**.

As the agent is not a turnkey “solution” for accessibility, we want to avoid situations where the agent’s output in error may not be sufficiently interrogated by the human using it. This is especially relevant when someone is not well-versed in digital accessibility considerations and practices.

Here’s what we did to accommodate the agent’s limitations:

### Evaluate code complexity

We want to avoid scenarios where we would need to perform costly and time-intensive work to revisit an inaccessible solution that the agent “thinks” is accessible.

To aid with this problem, the accessibility agent uses a small shell script to analyze the code it is set to work on. The script itself is simple, using a small set of basic heuristics to evaluate the relative complexity and distill it down into a score.

This score is then ingested by the agent. If the score passes a set threshold, the agent is instructed to **not** execute code changes. Instead, it will inform the person using the LLM that they should reach out to the accessibility team to consult on what they are attempting to do.

### Identify high-risk patterns

It is a subtle thing to understand, but know that **it is entirely possible to have code that passes automated accessibility checks, yet is functionally unusable**.

As a companion to code complexity, the accessibility agent is instructed to avoid attempting code generation for patterns the accessibility team has identified as high-risk. This includes, but is not limited to: drag and drop, [toasts](https://primer.style/accessibility/patterns/accessible-notifications-and-messages/#toasts), rich text editors, [tree views](https://github.blog/engineering/user-experience/considerations-for-making-a-tree-view-component-accessible/), and [data grids](https://www.w3.org/WAI/ARIA/apg/patterns/grid/).

These patterns require a ton of focused attention and detail and currently sit outside of an LLM’s current capabilities to produce in a way that actually works with assistive technology.

Not prohibiting high-risk patterns and high-complexity code environments would lead to unnecessary demands of everyone’s time to readdress, and also represents reputational risk for the accessibility team. We avoid this by shutting off the LLMs capability to go down this pathway.

### Reduce bias to action

I am loathe to anthropomorphize LLMs, but one quality they all seem to share is **desperately wanting to produce content**. For Copilot, that often means generating code.

We had to create [anti-gaming](https://en.wiktionary.org/wiki/game_the_system) instructions to prevent the LLM from creating sneaky ways to get around its instructions to not generate code when human expertise is needed. This prevented it from violating its own intervention instructions.

### Know that programmatically determinable issues don’t cover everything

Agent success metrics live within a larger context.

Of the 55 total WCAG level A and AA Success Criterion, only [35 of them can be detected via deterministic automated code checkers](https://www.w3.org/WAI/standards-guidelines/act/rules/?requirements=a%2Caa&status=approved&implement=auto&display=no-rules). This means that **~36% of level A and AA Success Criterion cannot be discovered automatically**.

![A pie chart titled, 'WCAG A and AA Success Criterion'. The first of two slices is labeled, '36% require manual evaluation'. The second of two slices is labeled, '64% can be detected automatically'.](https://github.blog/wp-content/uploads/2026/05/image4.png?w=729)

A pie chart titled, 'WCAG A and AA Success Criterion'. The first of two slices is labeled, '36% require manual evaluation'. The second of two slices is labeled, '64% can be detected automatically'.

LLM-powered agent operation is making inroads on this ~36% gap, but it is not a perfect science. Because of this, it becomes important to **manually identify accessibility barriers earlier during design and prototyping efforts** — [the area where the majority of accessibility issues originate](https://www.deque.com/blog/auditing-design-systems-for-accessibility/#design-should-consider-accessibility).

This thinking is also reflected in the agent’s escalation logic, in that members of the Accessibility team can pair with designers to help consider alternate approaches and brainstorm solutions that achieve business goals without compromising on accessibility.

This intervention and assistance is done to thwart potential downstream issues—and costly and time-consuming redesigns—are stopped before they ever have a chance to get off the ground.

### Manually evaluate agent output and adjust things that aren’t working as expected

We periodically perform manual review of agent output to determine its accuracy and efficacy. In addition, we have tooling in place to capture pull request reviewer sentiment. Both serve as **strong signals for areas where the agent needs better instruction**, as well as new resources and skills.

## Learning in the open

To recap, we learned that the agent is:

- Used to aid and augment existing accessibility efforts, not to replace them.
- Significantly more effective when trained on manually audited and remediated accessibility issues for your specific experience.
- Far more efficient with token consumption when utilizing sub-agents.
- More accurate and effective when executing instructions in a methodical, linear fashion.
- More consistent when set to use preformatted templates to pass information around.
- Set to understand its limitations and route people to alternative support systems.
- Improved when its output is periodically reviewed to identify areas it needs better instruction.

This journey is also not yet complete. The accessibility agent continues to be iterated upon in the hopes of **helping ensure GitHub is an accessible and inclusive platform for all developers**.

We hope that we can eventually open source the agent as part of [our pledge to help improve the accessibility of open source software at scale](https://github.blog/open-source/social-impact/our-pledge-to-help-improve-the-accessibility-of-open-source-software-at-scale/). Until then, we hope that in sharing our learnings with this undertaking that other teams can have a resource to reference for their own accessibility efforts.

---

## 编译摘要

### 1. 浓缩
- **核心结论1**: GitHub 的无障碍 Agent 不是“自动解决无障碍”的银弹，而是一个增强现有无障碍流程的生产级辅助系统。
  - 关键证据: 官方明确把目标限定为即时回答无障碍问题，以及在上线前自动发现并修复简单、客观的问题；并反复强调它只是 augment peers’ efforts。
- **核心结论2**: 这类专业 Agent 的效果高度依赖组织自己积累的高质量历史语料、结构化模板和线性工作流。
  - 关键证据: GitHub 把集中维护的无障碍 issue、PR、acceptance criteria 和 WCAG 元数据作为核心知识语料；同时采用 reviewer/implementer 两个顺序子 Agent、固定 phase 顺序和 template schema 传递信息。
- **核心结论3**: 生产级 Agent 的关键不只是“能不能修”，而是“知道什么时候不该修、什么时候该升级到人工”。
  - 关键证据: 文中给出复杂度评分、高风险模式禁改、anti-gaming 指令、人工复核和 escalation logic；并指出 55 个 WCAG A/AA 标准里只有 35 个可自动检测，约 `36%` 仍需人工评估。

### 2. 质疑
- **关于“68% resolution rate”的质疑**: 解决率说明问题被关闭或修复，但不直接等同于真实辅助技术体验改善，也不说明长尾复杂问题是否被覆盖。
- **关于“子 Agent + 模板 + 顺序执行”的质疑**: 这套设计依赖 GitHub 已有的无障碍团队、历史问题库和内部 skill 体系，其他团队未必能低成本复制。
- **关于“自动化边界”的质疑**: 即使 LLM 缩小了自动检测覆盖不到的 `36%` 缺口，它仍然无法替代设计阶段、原型阶段的人工无障碍判断。

### 3. 对标
- **跨域关联1**: 这篇文章是 [[Verifiable-Agent-Engineering|可验证 Agent 工程]] 的高质量案例：Agent 被设计成可升级、可审计、可拒绝，而不是一味自动执行。
- **跨域关联2**: 它也把 [[Agent-Harness|Agent Harness]] 的几个组件压得很实：顺序子 Agent 编排、结构化 schema 传递、复杂度门控和人工升级回路都不是 prompt 小技巧，而是 harness 设计。
- **跨域关联3**: 文中的 anti-gaming 指令和“拼命想生成代码”的观察，为 [[Bias-to-Action-LLM|LLM 的行动偏差]] 提供了具体工程场景。

### 关联概念
- [[Accessibility-Agent]]
- [[Verifiable-Agent-Engineering]]
- [[Agent-Harness]]
- [[Bias-to-Action-LLM]]
