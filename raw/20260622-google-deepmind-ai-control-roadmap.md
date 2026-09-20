---
type: raw
title: "GDM AI Control Roadmap v0.1"
source: "https://storage.googleapis.com/deepmind-media/DeepMind.com/Blog/securing-the-future-of-ai-agents/gdm-ai-control-roadmap.pdf"
author:
  - "Mary Phuong"
  - "Erik Jenner"
  - "Laurent Simon"
  - "Lewis Ho"
  - "Rohin Shah"
  - "Sebastian Farquhar"
  - "Scott Coull"
published: "2026-06-22"
created: "2026-09-19"
description: "Google DeepMind AI Control Roadmap v0.1：定义 asynchronous/synchronous coverage、recall、time-to-response，并给出 R1–R3 的目标要求；这些是 roadmap assurance requirements，不是已实现的部署实测。"
tags:
  - clippings
  - observability
  - agent-security
---

# GDM AI Control Roadmap v0.1

> Canonical source: https://storage.googleapis.com/deepmind-media/DeepMind.com/Blog/securing-the-future-of-ai-agents/gdm-ai-control-roadmap.pdf

## Source locator

- Version: v0.1, dated 2026-06-22.
- Defines asynchronous assurance metrics:
  - monitoring coverage = fraction of internal agentic traffic monitored;
  - monitoring recall = fraction of trajectories showing misaligned behaviour correctly flagged;
  - time-to-response = time from flag to investigation.
- Defines synchronous assurance metrics:
  - response coverage = fraction of internal agentic traffic where harmful action is automatically blocked, resampled, escalated or otherwise prevented;
  - response recall = fraction of attack rollouts correctly blocked.
- Proposes red-team exercises with proxy untrusted models to measure recall.
- R1 gradually increases monitoring coverage from representative sampling toward about 99% and accelerates response from about one week toward 24 hours or less as harm potential rises.
- R2 mitigation requirements propose:
  - asynchronous monitoring coverage greater than 99%;
  - time-to-response less than 24 hours;
  - synchronous response coverage greater than 99%;
  - recall targets/assurance following the detection track.
- Roadmap distinguishes D1–D4 detection capability as visible chain-of-thought becomes less reliable, moving toward behavior-based and potentially internal-activation monitoring.

## Evidence boundary

The thresholds are roadmap requirements/targets, not published deployment achievements. The paper explicitly describes AI control as nascent and several higher-tier measures as future or speculative. Coverage of instrumented traffic is also not identical to coverage of every effective action path.
