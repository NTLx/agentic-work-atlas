---
type: raw
source: "https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents"
author:
  - "Justin Young (Anthropic)"
published: "2026-06-01"
created: "2026-07-02"
tags:
  - clippings
  - agent-harness
  - long-running-agents
  - agent-engineering
  - AI-Agent
---

# Effective harnesses for long-running agents

**Source**: Anthropic Engineering Blog
**Author**: Justin Young

---

As AI agents become more capable, developers are increasingly asking them to take on complex tasks requiring work that spans hours, or even days. However, getting agents to make consistent progress across multiple context windows remains an open problem.

The core challenge of long-running agents is that they must work in discrete sessions, and each new session begins with no memory of what came before. Imagine a software project staffed by engineers working in shifts, where each new engineer arrives with no memory of what happened on the previous shift.

We developed a two-fold solution to enable the Claude Agent SDK to work effectively across many context windows: an **initializer agent** that sets up the environment on the first run, and a **coding agent** that is tasked with making incremental progress in every session, while leaving clear artifacts for the next session.

## The long-running agent problem

The Claude Agent SDK has context management capabilities such as compaction, which enables an agent to work on a task without exhausting the context window. However, compaction isn't sufficient. Out of the box, even Opus 4.5 running on the Claude Agent SDK in a loop across multiple context windows will fall short if only given a high-level prompt like "build a clone of claude.ai."

Two failure patterns emerged:

1. **One-shotting**: The agent tries to do too much at once, runs out of context mid-implementation, leaving the next session with a half-implemented, undocumented feature. The next agent has to guess what happened.
2. **Premature declaration of victory**: After some features are built, a later agent instance sees progress and declares the job done.

This decomposes into two parts: set up an initial environment that lays the foundation for ALL features, and prompt each agent to make incremental progress while leaving the environment in a clean state.

## Environment management

The solution uses two agent types with different initial prompts:

### Initializer agent
The very first agent session uses a specialized prompt to set up the environment:
- An `init.sh` script
- A `claude-progress.txt` file that keeps a log of what agents have done
- An initial git commit showing what files were added

### Feature list
To address one-shotting and premature completion, the initializer agent writes a comprehensive file of feature requirements expanding on the user's prompt. In the claude.ai clone example, this meant over 200 features, all initially marked as "failing." The feature list uses JSON format — the model is less likely to inappropriately change or overwrite JSON files compared to Markdown.

```
{
    "category": "functional",
    "description": "New chat button creates a fresh conversation",
    "steps": [
      "Navigate to main interface",
      "Click the 'New Chat' button",
      "Verify a new conversation is created"
    ],
    "passes": false
  }
```

Coding agents are prompted to edit this file only by changing the `passes` field, with strongly-worded instructions: "It is unacceptable to remove or edit tests because this could lead to missing or buggy functionality."

### Incremental progress
The coding agent is asked to work on only ONE feature at a time. This incremental approach was critical to addressing the tendency to do too much at once.

The agent must leave the environment in a clean state: commit progress to git with descriptive commit messages, write summaries in a progress file. This allows the model to use git to revert bad changes and recover working states.

### Testing
Absent explicit prompting, Claude tended to mark features as complete without proper testing. Claude mostly did well at verifying features end-to-end once explicitly prompted to use browser automation tools (Puppeteer MCP) and do all testing as a human user would.

Some issues remain: Claude can't see browser-native alert modals through Puppeteer MCP, and features relying on these modals tended to be buggier.

## Getting up to speed

Every coding agent is prompted to run through steps to get its bearings:

1. Run `pwd` to see the working directory
2. Read the git logs and progress files to understand recent work
3. Read the features list file and choose the highest-priority undone feature

A typical session starts with the assistant reading git logs, checking `init.sh`, starting the dev server, testing basic functionality, then choosing a new feature to work on.

## Agent failure modes and solutions

| Problem | Initializer Agent | Coding Agent |
|---------|------------------|--------------|
| Premature victory declaration | Set up feature list file with end-to-end descriptions | Read feature list, choose single feature |
| Environment left with bugs | Initial git repo and progress notes | Start by reading progress and git, run basic test; end with commit and progress update |
| Features marked done prematurely | Set up feature list | Self-verify all features; only mark passing after careful testing |
| Agent wastes time figuring out how to run app | Write `init.sh` script | Start by reading `init.sh` |

## Future work

Open questions remain:
- Whether a single general-purpose coding agent performs best, or if better performance comes from a multi-agent architecture (specialized testing agent, QA agent, code cleanup agent)
- Generalizing these findings beyond full-stack web app development to scientific research or financial modeling
