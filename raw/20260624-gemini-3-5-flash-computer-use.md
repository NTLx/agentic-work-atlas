---
source: "https://deepmind.google/blog/introducing-computer-use-in-gemini-3-5-flash"
title: "Introducing computer use in Gemini 3.5 Flash"
author: "Mateo Quiros, Google DeepMind"
date: 2026-06-24
tags:
  - computer-use
  - gemini
  - agentic-ai
  - enterprise-automation
  - safety
---

# Introducing computer use in Gemini 3.5 Flash

Computer use is now a built-in tool supported in Gemini 3.5 Flash, delivering our best performance yet for agentic computer use tasks. Previously only available as a standalone Gemini 2.5 computer use model, computer use is now integrated natively in the main Gemini Flash model. Gemini already excels at function calling and using built-in tools like Search and Maps grounding. With built-in computer use capability, developers can now use 3.5 Flash to reliably build custom agents that can see, reason and take action across browser, mobile and desktop environments. This unlocks improved performance for long-horizon and enterprise automation tasks like continuous software testing and knowledge work across professional applications.

## Key points

- Computer use is now a **built-in tool** in Gemini 3.5 Flash (previously a standalone model)
- Supports browser, mobile, and desktop environments
- Accessible via Gemini API and Gemini Enterprise Agent Platform
- Targets long-horizon and enterprise automation tasks

## Safety measures

- Targeted adversarial training for computer use in Gemini 3.5 Flash
- Two optional enterprise safeguard systems:
  - Require explicit user confirmation for sensitive or irreversible actions
  - Automatically stop tasks if an indirect prompt injection is identified
- "Defense-in-depth" approach: combine with secure sandboxing, human-in-the-loop verification, and strict access controls

## Industry adoption

- Browserbase: demo environment for testing
- Browser Use: CEO Magnus Muller endorses
- UiPath: Senior Director Alvin Stanescu endorses

## Significance

This represents a major step in computer use becoming a first-class capability in frontier models. The integration of computer use as a built-in tool (rather than a separate model) signals that **agentic UI interaction is becoming a standard model capability**, not a niche add-on. The safety measures (prompt injection detection, user confirmation) preview the emerging **Agent Control Plane** product category.
