---
type: raw
title: "Introducing a new design for Microsoft 365 Copilot"
source: "https://www.microsoft.com/en-us/copilot/blog/2026/05/28/introducing-a-new-design-for-microsoft-365-copilot/"
author:
  - "Jon Friedman"
published: "2026-05-28"
created: "2026-09-19"
description: "Microsoft 365 Chief Design Officer Jon Friedman 对 Copilot redesign 的当前产品复盘：从静态 prompt box 转向 task-aware workspace，把 output quality 作为核心设计对象，并披露 load time、response latency 与 app usage 的真实 rollout 指标。"
tags:
  - clippings
  - design
  - ai-era
---

# Introducing a new design for Microsoft 365 Copilot

> Canonical source: https://www.microsoft.com/en-us/copilot/blog/2026/05/28/introducing-a-new-design-for-microsoft-365-copilot/

## Source locator

- Author: Jon Friedman, Chief Design Officer, Microsoft 365.
- Published 2026-05-28.
- Describes the redesign of Microsoft 365 Copilot across the standalone app and Word, Excel, PowerPoint and Outlook.
- Explicitly reframes the design target:
  - not only interface;
  - but also the quality of AI output, including tone, structure, readability, usefulness and trustworthiness.
- Converts the prompt line into a larger task-aware workspace and introduces shared interaction patterns across apps.
- Work IQ is presented as a visible and controllable intelligence layer drawing on emails, files, chats and meetings.
- Agentic modes in Word, Excel and PowerPoint can take action inside the working context rather than only answer prompts.
- Reported product metrics:
  - app load more than twice as fast, with load time reduced over 50%;
  - first-token response time for complex prompts improved about 10% at p95;
  - Copilot usage after rollout increased 27% in Word, 33% in Excel, 43% in PowerPoint and 30% in Outlook.
- Qualitative user feedback cited is based on 8 interviews and 79 survey responses.

## Evidence boundary

This is an official product/design post by Microsoft leadership. Performance and usage figures are backed by internal product telemetry, but the source does not publish raw experiment tables or long-term retention. Short-window usage lifts do not prove durable user value. The redesign shows that model output and task flow are design objects, but does not expose internal RACI for model behavior, eval ownership or incident accountability.
