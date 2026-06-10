---
type: raw
source: "https://claude.com/blog/whats-new-in-claude-managed-agents"
author:
  - "Anthropic"
published: "2026-06-09"
created: "2026-06-10"
tags:
  - clippings
  - managed-agents
  - deployment
  - vault
---

# New in Claude Managed Agents: run agents on a schedule and store environment variables in vaults

Starting today, Claude Managed Agents can run on a schedule and securely access CLI tools and other authenticated services. Both features are now available in public beta on the Claude Platform.

**Run agents on a schedule**
Agents can now run on a schedule, completing routine work automatically. A scheduled deployment gives an agent a cron schedule. Each time the schedule fires, the agent starts a new session and completes its task, with no scheduler for you to build or host. Use it for recurring work like a nightly data sync, a weekly compliance scan, or a daily digest. Once a deployment is live, you can pause, resume, or archive it at any time, or trigger additional runs on demand.

**Store environment variables in vaults to authenticate CLIs and other tools**
Agents connect to external systems through direct API calls, CLIs, and MCP. Now we're extending vaults to support environment variables, so CLIs and other tools can make authenticated requests. CLIs let agents drive existing command-line tools directly through a shell, making them a fast, lightweight integration path. Register an API key with an environment variable name and the domains it can reach, and the CLIs installed in an agent's sandbox can use it to make authenticated API calls.

The agent never sees your key because the sandbox only holds a placeholder. The real key is attached at the network boundary, and only on requests to domains you allow, so it only goes where you've approved. To change a key, update it in the vault, and running sessions will pick up the new value on their next call. Most CLIs that send their key in an HTTP request work this way, including the Browserbase, KERNEL, Notion, Ramp, and Sentry CLIs.
