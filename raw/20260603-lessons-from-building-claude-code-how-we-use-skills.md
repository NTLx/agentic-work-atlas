---
type: raw
source: "https://claude.com/blog/lessons-from-building-claude-code-how-we-use-skills"
author:
  - "Thariq Shihipar"
published: "2026-06-03"
created: "2026-06-10"
tags:
  - clippings
  - claude-code
  - skills
  - progressive-disclosure
---

# Lessons from building Claude Code: How we use skills

Skills have become one of the most used extension points in Claude Code. They're folders of instructions, scripts, and resources that agents can discover and use to do things more accurately and efficiently.

**Types of skills we use:**
1.  **Library and API reference:** Explaining how to use internal or complex libraries.
2.  **Product verification:** Describing how to test or verify code (e.g., using Playwright).
3.  **Data fetching and analysis:** Connecting to data and monitoring stacks.
4.  **Business process automation:** Automating repetitive workflows like standup posts.
5.  **Code scaffolding:** Generating framework boilerplates.
6.  **Code quality and review:** Enforcing style and performing adversarial reviews.
7.  **CI/CD and deployment:** Helping fetch, push, and deploy code.
8.  **Runbooks:** Mapping symptoms to investigation steps.
9.  **Infrastructure operations:** Routine maintenance and cleanup.

**Best practices for making skills:**
*   Don't state the obvious; focus on "taste" and non-default patterns.
*   Build a "Gotchas" section based on common failure points.
*   Use the file system for progressive disclosure.
*   Write descriptions for the model (triggers), not just for humans.
