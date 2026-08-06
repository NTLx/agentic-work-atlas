---
type: raw
source: "https://blog.cloudflare.com/how-we-use-ai-with-cloudflare-os/"
author:
  - "Sam Rhea"
published: "2026-08-05"
created: "2026-08-06"
tags:
  - clippings
  - cloudflare
  - agents-week
  - cloudflare-os
  - fde
  - context-layer
  - permissions
  - ai-rollout
---

# How we're rethinking work at Cloudflare with Cloudflare OS

> Source: [blog.cloudflare.com/how-we-use-ai-with-cloudflare-os/](https://blog.cloudflare.com/how-we-use-ai-with-cloudflare-os/)
> Author: Sam Rhea
> Date: 2026-08-05

*Sam Rhea is Cloudflare's Chief Information Officer.*

## 正文

I knew we had a problem about six months ago when a member of our sales organization reached out to me asking for API keys. Keys plural. They used AI to build what they described as a SuperApp that would transform our go-to-market teams. All they needed was production access to about a dozen systems of record at Cloudflare and admin permissions to a deployment pipeline to make it work.

We had taken a fairly cautious approach to rolling out AI at Cloudflare during 2025. We deployed informational chat applications and tinkered with using AI to help write some boilerplate code, but we felt that the technology was not ready to change how we work.

And then, over the course of a few days at the end of last year, better models and more powerful harnesses changed that calculus. AI agents could **do** things, and they could do them well. Hundreds of team members across Cloudflare, in technical and non-technical roles, spent the quieter weeks around the New Year experimenting with new tools that made it easier than ever to build.

That sales team member building their SuperApp was just the first in an avalanche of people raising their hands to use these tools to transform how they get things done. We had an obligation to equip and enable them to do so. But we also had an obligation to keep our systems, internal data, and customer data safe.

We have spent the last several months building a platform to do exactly that inside of Cloudflare. We call it Cloudflare OS. We started by stitching together off-the-shelf components from our Developer and Zero Trust platforms like Cloudflare [Workers](https://www.cloudflare.com/products/workers/) and [Access](https://www.cloudflare.com/sase/products/access/). As we learned more about the challenge, we also created custom services tailored to this new way of working.

As with many of Cloudflare's products, we set out to solve a problem we had internally. As it turns out, many of you had the same problem. That's why today we are excited to share Cloudflare OS, the sum of what we have launched internally to give our own team members the ability to safely and productively use AI and deploy agents. You can read more about what is available right now in [Phillip's post here](http://blog.cloudflare.com/cloudflare-os).

In this post, I want to walk through our own internal journey that led to this release, both what has gone well and where we have fumbled. There are five sections: the principles we put in place to begin; how we piloted to figure out what the jobs were to be done; what we built for engineers, and for non-engineers; and how we created champions across the organization to help drive change.

During the last few months, I have felt like the luckiest CIO in the world as the team I support had access to these emerging technologies. Today's goal is to share that platform and its lessons with every team.

## Set the ground rules

We started by defining a set of principles around how this should work. Cloudflare's CTO and I sat down in our office in Austin, Texas, and began to sketch out what needed to be true in how we adopted AI. We invited leaders from across the organization to give us feedback on the draft. The result became the guidelines below.

**1) We use AI to spend more time with our customers and build technology to solve more of their problems.**

We do not want to use AI just for the sake of using AI. We push teams to start by defining their "jobs to be done" first, the pain points, bottlenecks, or missed opportunities that can improve how we serve our customers. Then we find the right tool.

**2) Everyone deserves superpowers.**

AI is very, very good at writing code. By extension, the first wave of AI tools that could take actions consisted of interfaces that developers already used: command lines, code editors, terminals, Git repositories.

These formats could leave behind large parts of our team. While we have a very technical and curious workforce, not every member of our team spends their day in developer tools. And we do not think they need to! We want our employees to bring their subject matter expertise and we would provide them with an intuitive platform they could use to rethink how we do work.

**3) The human owns the output.**

We view AI as a tool and toolmaker, not a team member. We expect humans to take responsibility for defining the quality, testing, and workflows that rely on AI output.

The rule extends to deploying agents, as well. The users and teams that ship agents are responsible for the output of those agents. Someone leaves? Their manager inherits the responsibility of their agents in the same way they inherit their other workflows.

**4) The context from the organization matters more than the model.**

The workflows and agents that we deploy at Cloudflare need to know about Cloudflare. The time we spent on the technology had to be paired with time invested in a curated, canonical context layer.

**5) You should never have more permission with systems of record when using AI.**

Everyone at Cloudflare has a scoped view into the underlying data at Cloudflare for good reason. We use our own products to segment data access by factors ranging from device to role to region. We also configure and monitor the controls inside our third party applications.

Those controls need to apply when I manage an AI agent that interacts with the same data. I should never have "more" access to data when using an AI tool and my AI agents should only have access to exactly what they need, nothing more. And if I deploy an agent and share it with someone, the access the agent provides to them should reflect their permissions, not mine.

## Meet your users where they are

With those rules in place, we got to work. We ran two parallel programs: the first for our engineering teams, and the second for every other type of work.

### Provide your engineers with guardrails

AI tools took the work our engineers already did and made it faster — faster than our review process could keep up with. Anyone at Cloudflare could now write bad code, faster, thanks to AI. We needed better guardrails.

So we built a context layer for engineering. We call it the Cloudflare Engineering Codex. A Codex is an authoritative guide. Ours sets out the principles and practices we work by. Policies tell you what you can't do, whereas a Codex tells you what you should do. It is opinionated by design. Every part of our codebase has a domain owner accountable for what good looks like there.

We surfaced that context layer across the software development lifecycle. Agents use the Codex to help engineers plan work. One agent reviews every Merge Request against Codex requirements. Another reviews technical designs before implementation starts. A third reviews incident reports. In the past four months, those agents have flagged nearly a quarter of a million potential problems and blocked 16,000 merges. They have caught architectural issues in close to 600 designs before a line of code was written.

You can read in much greater detail about how we built this code review workflow in [Timo's blog post on AI Code Review](http://blog.cloudflare.com/engineering-standards-enforcement). We are now shifting focus to giving engineers the tools to define the loops that evaluate the work their agents produce.

### Offer everyone a magic email alias

An early mistake we made was giving everyone outside of engineering the same tools with slightly friendlier user interfaces. Engineers could clone a code repository to their laptop, add a context file like [AGENTS.md](http://AGENTS.md), and point their harness at the work. However, the harnesses in the market map poorly to other types of knowledge work where users create one-off outputs and work on projects that involve dozens of systems of record.

If you give everyone a harness workspace that is great at writing code, you'll wind up with way more code than you need. The result became a flood of vibe coded apps looking for a problem to solve. So we worked backwards.

We told everyone at Cloudflare that they could send the work they did not want to do to a "magic AI email bot" that would respond with the output they needed. Behind the scenes, a small team of people staffed this email alias using AI tools to do the work.

For some reason, people are less willing to send their vibe coding ideas to what they think is an automated system, but very willing to send the work they do not want to do. Over the course of hundreds and then thousands of sessions managing the email alias, we identified the mundane work that team members would like to automate.

We triaged these manually and over time we observed patterns. We created the skill and context files, mapped out the data connections, and defined the kinds of outputs users needed. With those in hand, we could automate some of the responses to this email alias.

We were very motivated to stop staffing this service. It was miserable. The long-term goal was to take these materials we had collated and create skills to address them, so that our users could solve their own problems. The manual work behind this email alias continued until we felt we had captured enough of the common "jobs to be done" at Cloudflare to give our teams a headstart on automation. Now we just needed to give them a platform where they could easily and safely run those workflows.

## Give team members a platform to solve problems

The first version of that platform, which we call Cloudflare OS, consisted of a simple harness running in a container on Cloudflare's infrastructure. Users access it in a web browser and, once authenticated through [Cloudflare Zero Trust](https://www.cloudflare.com/products/access/), they can run the skill files and workflows we started collecting during the magic email phase.

All of this happens inside of their browser, no local configuration required. Users could open their laptop and immediately be productive. We heard from new members of our sales team who, within days of starting, felt like they could automate work that would have taken them weeks to complete in their last workplace.

Users could also close their computer and get a coffee or use the bathroom while work happened. No more walking around the office with a laptop cracked open.

We think that cloud-based workspaces benefit more than just the user. An ephemeral cloud-based environment only has access to the data a user introduces into the session, rather than potentially everything on the laptop in front of you when you use a local harness. Our Security team has audit visibility and network control over the environment, including the ability to filter where on the Internet it can connect.

When a user needs to get work done, they begin by running skill files defined by common workflows we identified across departments. The company's accumulated context and skills we gathered during the magic email phase become executable with a single click.

A panel on the right-hand side would render the output of a given skill file, like a technical architecture document or a slide deck. Users could share the outputs with teammates.

We gave Cloudflare OS access to data by connecting systems of record through our [Model Context Protocol (MCP) Portal](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/). The MCP standard is a framework that defines how to connect your AI tools to systems of record in a way that tells the AI tool what data and operations are available. Following our rule around permissions, the access a user session has in Cloudflare OS is scoped to their existing permission set in a given system of record.

In most cases, we build and deploy our own implementation of an MCP server for each system of record, even when the system of record provides a native version. By building our own, we can add additional layers of controls like rate limits by role or region. Cloudflare Workers gives us a simple place to build them and, as a serverless platform, the ongoing maintenance burden is practically zero.

When Cloudflare OS uses AI inference, we route that through our [AI Gateway](https://www.cloudflare.com/products/ai-gateway/). That allows us to filter, log, and audit all interactions between users and those AI systems. For example, we can reuse the [Data Loss Prevention](https://www.cloudflare.com/products/dlp/) (DLP) rules from our [Secure Web Gateway](https://www.cloudflare.com/products/gateway/) to block certain datasets from ever being sent to a provider.

AI Gateway also gives us the ability to [control model usage](https://blog.cloudflare.com/ai-gateway-spend-limits/). Not every user needs access to the max thinking mode of the latest frontier lab model. And we do not need team members spending $20 to summarize their email inbox every hour. We can use AI Gateway to gate models by role or steer use cases, especially more autonomous ones like scheduled skill file runs, to more efficient models.

## Now make it more deterministic with agents for everyone

Cloudflare OS gave our team an AI workspace where users could run skill files and their own workflows. However, each skill file a user ran kicked off a token-hungry inference session. Much of the work we do is mostly deterministic; a sequence of steps with some inference (or human judgment) in the right places. We don't need AI to always be a tool as much as we need AI to be a toolmaker.

We set out to address that in an update to Cloudflare OS, which is the version we are sharing with you today. This version lets users describe a workflow in natural language, have an AI agent create the code to power that workflow, and then run agents on demand, on a schedule, or triggered from an event. Rather than trying to build one-size-fits-all agents that we share with the organization, we give every team member the ability to create secure applications, isolated by default.

For example, one of the teams I work with is our IT help desk. We support the team members at Cloudflare with the hardware and software they need to do their work, from provisioning to debugging to offboarding. We manage that work through a classic ticket queue.

Each morning, I want to review our open ticket queues and metrics around our ability to serve these internal customers. Before Cloudflare OS, I would do this manually. Our ticketing system has built-in dashboards, but they are pretty basic. I would download CSVs and import them to Google Sheets where I would create charts. I would then manually click into each ticket that had come in overnight. That was both time-intensive and created redundant data outside our system of record.

In Cloudflare OS v1, I ran this as a skill file connected to the MCP server for our ticketing software. While safer (and less manual), this meant I was burning thousands of tokens each morning recreating a report that was mostly the same. I was also lighting tokens on fire triaging and drafting responses to the overnight tickets.

Cloudflare OS v2 handles that for me and anyone else with similar kinds of problems to solve. I described the charts I want to view, and it uses an AI agent to write the code that powers them alongside a secure connection to the dataset that [uses a service](http://blog.cloudflare.com/cloudflare-os) we call a gatekeeper. That gatekeeper handles the consistent queries my agent makes to the dataset, scoping down the context for the app without any API key management.

When I do need AI inference, I can embed it into the application. I built options to draft responses with AI to tickets that arrive. I can review the responses and send them. All within a secured workspace that did not require me to create and manage any integrations or deployment pipelines.

When I share the agent I built with others, they authenticate the agent using their own permissions through the same gatekeepers, so we do not cross data boundaries. And I burn exactly zero tokens each time I load the initial report.

## Send out champions and share your wins

Cloudflare OS provided us with the platform we needed, but we still needed to enable our team. To do that, we did not hire a dedicated AI team. Instead, we found early adopters in various roles and made them into champions who could help their peers use this new platform. We tapped a sales leader in London, a solutions engineer in Texas, and an investor relations leader in Portugal, a business development team member in Japan, a Sales Ops leader in the US among others, and asked them to partner with their teams to rethink their work.

We also had success embedding interns into established teams. We announced our goal of bringing on 1,111 interns this year, and many of those who have joined us are working within departments with the simple goal of "make this team into all-stars by equipping them with our AI tools."

The results continue to amaze us. Thousands of Cloudflare team members use the platform every week and the active users per day have grown every single workday. In the last month alone, we estimate that our sales team members have saved more than 10,000 hours of time spent on previously manual tasks like territory planning and proposal creation. In those 30 days, users have created over 4,000 apps and tools to solve specific challenges.

## What's next?

We are not close to done, but every day I see a little more progress as we obsess over how to rethink the work we need to do to solve problems. Someone sent me the link to a report in Cloudflare OS last night that helps us diagnose a procurement bottleneck that would have previously required days of manual spreadsheet crawling. This morning, a member of the IT team shared a workflow agent to track laptop replacements built on the platform with someone on the finance team sitting near them in the Lisbon office. Small acts of automation and knowledge sharing that add up.

Just like we are committed to giving everyone at Cloudflare superpowers, we think every team outside of Cloudflare should have them too. We are excited to share Cloudflare OS with you today, and we expect it to continue to evolve, quickly, as we learn more together. If anyone wants to sit down and trade notes on what is working and not working with internal AI rollouts, just [let us know](http://www.cloudflare.com/resource/cloudflare-os-interest-landing-page/). I'd love to chat, human to human.
