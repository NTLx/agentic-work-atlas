---
title: "The Return of the Deployment Company"
source: "https://medium.com/@caffein.chen/the-return-of-the-deployment-company-b1e41c615ed1"
author:
  - "Caffein Chen (陳穎漢)"
published: 2026-05-20
created: 2026-05-23
description: "In May 2026, three consecutive events shook the AI industry:"
tags:
  - "clippings"
---
## Why AI Vendors Are Sending FDE Into Your Office — and What Enterprises Are Really Giving Up

## Preface

- **May 4**: Anthropic announced a joint venture with Blackstone, Hellman & Friedman, and Goldman Sachs. Anthropic, Blackstone, and Hellman & Friedman each committed roughly `$300M`; Goldman Sachs committed around `$150M`. The JV is valued at approximately **`$1.5 billion`**.
- **May 11**: OpenAI announced the launch of a wholly-owned subsidiary, the **OpenAI Deployment Company** (DeployCo), with initial investment exceeding **`$4 billion`**, simultaneously acquiring UK-based AI consultancy Tomoro and gaining roughly 150 Forward Deployed Engineers (FDEs).
- **May 12**: Google Cloud CEO Thomas Kurian announced via LinkedIn the formation of an FDE team within Google Cloud, with plans to hire hundreds of forward-deployed engineers.

Three of the world’s leading AI companies, **within the same week**, placed bets in the same direction.

If you sit on the buy-side of enterprise AI — CIO, CTO, IT leader, procurement lead — you should be asking one serious question:

> ***“What are they betting on? And what does that mean for me?”***

This article aims to do four things:

1. **Explain why this is happening now** — how the economic logic of AI products diverges fundamentally from traditional SaaS
2. **Decode what each of the three vendors is actually betting on** — OpenAI, Anthropic, and Google have meaningfully different playbooks
3. **Identify four structural risks that enterprise buyers should be wary of** — a perspective that the broader analyst conversation has largely overlooked
4. **Argue why the economics of on-premise AI deployment have re-emerged in 2026** — and offer concrete guidance

By the end, you should walk away with two things: a framework for evaluating FDE proposals, and a decision-making logic for on-premise deployment.

If your company is going to face AI procurement decisions in the next 12 months, this article may help you avoid several structural long-term risks — or more importantly, help you see what this trade is actually about.

> ***Disclosure****: The factual core of this article is based on public announcements and industry reports from May 2026. Some strategic analysis reflects the author’s interpretation and should be read as such.*

## Part I: How AI Product Economics Differ from Traditional SaaS

To understand why the major vendors are suddenly piling into FDE, you first need to understand this: **the three preconditions that made SaaS the most profitable business model of the past 15 years are simultaneously being weakened by AI products.**

## 1.1 Why SaaS Worked

Recall the economic model of classic SaaS — Salesforce, Workday, Slack, Notion. They reached 70–80% gross margins, scaled through Product-Led Growth, and earned eye-watering valuation multiples because three conditions held simultaneously:

**Precondition 1: Zero marginal cost of replication** Write the code once. Serving 100 customers vs. 1,000 customers makes virtually no difference on the backend. One more user adds almost no compute cost.

**Precondition 2: Durable product value** The underlying logic of SaaS products — how CRM manages customers, how HR calculates payroll, how Slack delivers messages — only **changes meaningfully every few years**. Long product lifespan = long R&D amortization horizon.

**Precondition 3: High switching cost** Once users move their data, workflows, and habits into a SaaS, the cost of switching to a competitor is enormous. Customers are “locked in,” which sustains high subscription pricing.

These three together support an elegant equation: **low marginal cost + long product life + high switching cost = high margin + high retention + high valuation.**

For 15 years, this formula was how Silicon Valley valued the entire SaaS industry.

## 1.2 AI Products Are Eroding All Three Preconditions

AI products operate under different economic constraints. Let me unpack each:

**Precondition 1 weakens: Inference is a real compute expense**

Every ChatGPT response, every Claude completion, every Midjourney generation — each one burns real GPU cycles.

This isn’t the linear “use a bit more, pay a bit more” you see in SaaS. For complex reasoning tasks, long-context processing, and multi-step agentic workflows, the per-call cost can be **hundreds of times higher than a traditional SaaS query**.

According to multiple 2026 industry reports, **AI product gross margins now sit around 50–60%**, compared to 70–80% for traditional SaaS — a 20–30 point gap. And this gap **cannot easily be closed through pricing alone** — customers can defect to cheaper alternatives like OpenRouter, deploy open-source models themselves, or switch to competitors with comparable functionality at lower prices.

**Precondition 2 weakens: Tool turnover has compressed product lifespans**

In 2024, the dominant coding agent was GitHub Copilot. By 2025, it was Cursor. In 2026, attention has shifted to Claude Code and Windsurf. The category leader changes roughly every 12–18 months.

When an AI tool’s lifecycle from launch to obsolescence compresses to under 12 months, **the “invest heavily in R&D and amortize over 5 years” math starts breaking down.**

More directly: **the models themselves keep getting stronger.** A customer service agent your team built three months ago may be matched by a new frontier model six months later using only basic prompt engineering — **the product moat gets eroded by capability inflation.**

**Precondition 3 weakens: Lock-in based on human UI habits is eroding**

The historical switching cost in SaaS came from “humans learning the interface.” If your employees spent three months learning Salesforce, asking them to switch to HubSpot meant making them re-learn everything.

But when the “user” becomes an AI agent — something that can read documentation, call APIs, and operate across multiple tools — **it has no inherent preference for any particular SaaS interface.**

This means: **lock-in built on human UI familiarity is weakening.**

That said, the trend of “agents lowering switching costs” still faces three layers of real-world resistance:

- **Data migration layer**: A company’s actual switching cost lies in data model coupling and historical data migration — these don’t disappear just because the API works.
- **Organizational inertia**: Even if technically feasible, process ossification, departmental politics, and compliance habits inside companies are massive real-world barriers.
- **Standardization**: For agents to operate seamlessly across platforms, you need highly standardized API and semantic layers — far from reality in today’s complex enterprise software stack.

So the precise statement is: **Agents are weakening UI-based lock-in, but deeper switching barriers remain — and as we’ll see in Part III, FDE is starting to build an entirely new kind of switching cost: lock-in by tacit knowledge.**

> ***Scope note****: The economic analysis in this article applies primarily to AI-native companies. For companies like Salesforce or Adobe — traditional SaaS at the core with AI bolted on — the trajectory differs. They face the question of “how to integrate AI into an existing subscription model,” not “whether the SaaS math still holds.”*

## 1.3 Conclusion: The Economic Model of AI-Native Products Is Being Restructured

With all three preconditions weakened:

- **You can no longer rely on zero marginal cost** (inference is real)
- **You can no longer rely on long product lifecycles** (tooling churns fast)
- **You can no longer rely on UI-based human lock-in** (agents reduce operational stickiness)

AI companies’ answer is to do what traditional SaaS cannot: **send people into the customer’s office and perform highly customized, high-value, hard-to-replicate work.**

**This is why FDE has been pulled back into the spotlight.**

## Part II: Why Now? What Each Vendor Is Actually Betting On

FDE isn’t new. Palantir has been running this model for nearly 20 years — embedding engineers at the customer site, deeply learning the workflow, building software that serves that one customer, and charging enormous contract fees.

So why are OpenAI, Anthropic, and Google all going big on the model in May 2026?

## 2.1 What Changed the Game: AI Coding Tools Themselves

Historically, only Palantir could make FDE work, because **the unit economics didn’t pencil**. A single FDE could typically serve only 1–2 large customers per year — the cycle from understanding requirements to writing a prototype, iterating with business stakeholders, and delivering production code was simply too long.

AI coding tools changed that.

Cursor, Claude Code, and Windsurf have compressed the “from requirements to working prototype” cycle **from weeks to hours**.

Which means a modern FDE can:

- **Vibe-code v1 live in the customer’s conference room** (used to take two weeks; now 30 minutes)
- **Feed in real cases and iterate live with business users** (used to take a month; now same-day)
- **Serve multiple customers simultaneously** (used to be 1–2; now depends on project complexity)

**The unit economics of FDE are shifting from “doesn’t scale” to “scales sustainably.”** The model has gone from “only Palantir can afford it” to “potentially viable across hundreds of mid-market enterprises.”

That’s why now is 2026 — **the maturation of AI coding tools has made FDE a scalable business model.**

## 2.2 Three Vendors, Three Different Bets

All three are doing FDE — but their strategic logics differ substantively:

## OpenAI’s bet: Capability gap arbitrage

OpenAI created DeployCo and acquired Tomoro. The core assumption underlying this bet:

> ***“The capability gap between frontier models and everything else will persist and possibly widen. If we put engineers inside customer organizations and let them experience that capability gap firsthand, customers will pay a premium for it.”***

OpenAI is betting on **“frontier model rent”** — FDE is the conduit that converts technical leadership into commercial value.

## Anthropic’s bet: Industry know-how matters more than raw model power

Anthropic’s JV partners are remarkable for their strategic fit:

- **Blackstone** is the world’s largest PE firm, with hundreds of mid-market portfolio companies
- **Hellman & Friedman** is a top PE shop with deep industry penetration
- **Goldman Sachs** is a top investment bank that understands the operational logic of finance, manufacturing, retail, and adjacent industries

The core assumption:

> ***“A meaningful share of future customers don’t actually want ‘the strongest model’ — they want ‘someone who deeply understands my industry’s deployment.’ So we partner with the people who understand the industries best, and embed FDEs into their portfolio companies.”***

Anthropic is betting on **“industry know-how + mid-market enterprises”** — not competing head-on with OpenAI on frontier capability, but capturing the segment where “model is good enough, but deep customization is hard.”

## Google’s bet: Distribution beats everything

Google didn’t spin out a separate company or launch a major JV. It simply absorbed FDE into the existing Google Cloud go-to-market team.

The core assumption:

> ***“Customers are already on GCP, Workspace, BigQuery. We have the data, the customer relationships, the SRE infrastructure. Just make FDE part of the Cloud sales motion. We don’t need to ‘win’ customers — we need to ‘deepen’ the ones we already have.”***

Google is betting on **“existing distribution + customer relationship depth”** — no new business model required, just bolting FDE onto the existing sales engine.

## 2.3 The Shared Underlying Assumption — and a Larger Backdrop

The strategies differ, but one shared judgment underlies all three:

> ***“AI commercialization cannot be powered by SaaS-style low CAC, low marginal cost, PLG self-onboarding. You need people inside the customer’s site, encoding the customer’s tacit knowledge into an evaluation set.”***

What is tacit knowledge?

Take an example. A customer says: “I want an agent that automatically processes insurance claims.”

The information content of that sentence is almost zero. The real logic of claims processing — “ **Who signs off on this kind of case? How do you handle disputes? Does this customer get fast-tracked because they’re big?**” — **all lives in the heads of senior employees, never written into any SOP.**

To build an agent that actually works, **someone has to sit in the customer’s office, watch the AI’s output alongside the business users, and get told repeatedly: “No, that’s wrong, because our company’s unwritten rule is XX.”**

That layer of tacit knowledge **can only be extracted by people on the ground.**

**Here’s a larger backdrop worth holding in mind:**

For the past decade, the hyperscaler business model has been “ **selling tools** ” — selling compute, storage, APIs, and letting the enterprise decide what to do with them.

But FDE represents a fundamental shift: **hyperscalers are starting to directly take over the enterprise’s operational workflows themselves.**

This shift doesn’t just affect IT budgets — it affects enterprise **governance sovereignty**. Who designs the workflows? Who defines the business logic? Who accumulates operational intelligence?

This is why the four impacts in the next section aren’t just “IT risks” — they are “ **governance risks.**”

Up to this point, if you’re a hyperscaler investor or employee, FDE is a beautiful story.

**But if you’re sitting on the enterprise side of this trade, the story is just beginning.**

The next section — rarely discussed systematically in any depth — walks through **four real impacts that enterprise buyers should be wary of.**

## Part III: Four Structural Impacts Enterprise Buyers Should Watch For

Let me state my position clearly up front: **FDE is not evil.** For some enterprises, in some scenarios, accepting FDE is a reasonable choice.

But if you only see FDE’s upside — technical leadership, customization, faster deployment — and miss the power-structure shift underneath, then **the moment you sign the contract, you’ve planted a 3–5 year long-term risk.**

Let me break the four impacts apart.

## 3.1 Impact 1: Where Is Your Tacit Knowledge Flowing?

Back to FDE’s core logic: **“Encode the customer’s tacit knowledge into an evaluation set.”**

Read that sentence again, slowly.

When an OpenAI / Anthropic / Google FDE sits in your conference room, listens to your senior business person say “ **This case needs to be handled this way, because our company’s unwritten rule is…** ” —

**Those unwritten rules are entering that AI company’s systems in some form.**

- Contractually, who owns this evaluation set?
- If that FDE leaves the company in three years, who owns the “understanding of your workflow” they’re carrying in their head?
- If that AI company also has customers in your adjacent industry, will the “best practices for processing claims” they extracted from you somehow “inform” their work for your competitor?

This isn’t a villain narrative. This is a **structural problem that high-end consulting has always faced** — McKinsey, BCG, and Palantir have all been managing it for decades.

But FDE has one new element that traditional consulting didn’t: **the extracted knowledge gets encoded into AI systems, and may be reused in some form.**

Traditional consulting

FDE model

Post-engagement

Consultant walks away with the knowledge in their head

Your know-how sits in the AI company’s system as an evaluation set

Portability

Highly dependent on individuals

Systematically stored, potentially reusable across engagements

The legal, commercial, and competitive implications of these two are **fundamentally different**.

## Questions you should be asking:

1. **Who owns the IP of the evaluation set?** (Default answer is usually the AI company; what you should push for is “customer co-owned” or “customer-exclusive”)
2. **Will the AI company commit to “not using what they learn from you for other customers in your industry”?** (Default answer is usually no commitment)
3. **What happens to the evaluation set if the contract terminates?** (Default is the AI company keeps it; push for forced deletion or transfer to customer)

## 3.2 Impact 2: Data Boundaries Are Being Redrawn Under FDE

Under traditional SaaS, data contracts followed this logic: “ **Your data sits on my cloud, but I won’t look at it, won’t use it, won’t share it.**”

Anyone who’s signed enterprise contracts with Workday, Salesforce, or Slack knows the playbook — data sovereignty stays with the customer; the SaaS vendor is just the “custodian.”

FDE is breaking that boundary.

When the FDE “ **sits in your office**,” “ **looks at your real cases**,” and “ **debugs the model alongside your employees** ” — your data, your workflows, your business logic are **leaving the enterprise perimeter in a way that traditional SaaS never enabled.**

Even more subtle: **none of this triggers your traditional “data leakage detection” radar.**

- Your DLP system can’t detect “what’s in the FDE’s head”
- Your ISO 27001 audit doesn’t ask “what business logic is embedded in the FDE’s prompts”
- Your privacy compliance checks don’t cover “whether the AI evaluation set indirectly contains sensitive information”

**This is a brand-new data-boundary problem, with no mature regulatory framework yet to govern it.**

And in Taiwan specifically, this problem hits hard in 2026:

- **Financial services**: FSC (Financial Supervisory Commission) and FSI security regulations impose strict data-handling requirements
- **Healthcare**: companies serving US clients face HIPAA, alongside Taiwan’s domestic privacy law
- **Government customers**: national security and classified-information rules add another layer
- **Multinational subsidiaries**: often bound by parent-company global compliance policy

Interestingly, in Taiwan, this regulatory reality can actually become a **negotiating asset** for enterprises. Many Taiwanese companies are simultaneously subject to FSC regulations, national-security rules, or multinational parent-company compliance — which provide an internally easy-to-defend reason to say no to FDE. In other words: **“It’s not that we don’t want to — it’s that compliance won’t allow it.”** That sentence carries more weight in FDE negotiations than any commercial argument.

**If your company serves clients across these regulated industries, FDE’s data-boundary problem may put you in unintentional breach of multiple customer contracts.**

## Questions you should be asking:

1. How does the data the FDE accesses get classified under your DLP / privacy law / ISO 27001 framework?
2. Are the FDE’s prompts, evaluation sets, and saved interactions fully retained within your company’s control?
3. If your customer requires “all data processing must remain within Taiwan,” how does FDE comply? (Note: where does the AI company actually run inference? Does the data really stay onshore?)

## 3.3 Impact 3: Once Your Business Logic Is Encoded in the Evaluation Set, Do You Still Have Negotiating Power?

This is the most subtle of the four impacts, and the one most people miss.

Bargaining power in any commercial relationship comes from “ **the credibility of your walk-away option.**” If you can switch vendors at will, you have leverage. If you’re locked into a system you can’t replace for years, your leverage evaporates.

FDE systematically erodes the credibility of your walk-away option, **starting on day one.**

Walk through the timeline:

**Month 1**: FDE arrives, builds v1 of the agent, gets the core workflow running. Your reaction: “OK, but still some distance from what we actually need.”

**Month 3**: FDE deeply understands your business, has written hundreds of evaluation cases, customized the prompt chain. Your reaction: “This agent is starting to get us, but still struggles with edge cases.”

**Month 6**: Edge cases are getting handled. AI now manages most standard cases. Senior staff time is freed up. The company starts treating the AI as infrastructure. Your reaction: “It’s genuinely useful. We’re starting to depend on it.”

**Month 12**: Your business workflow has been redesigned around the AI. New hires are trained to “ask the AI first.” Process documents have been rewritten. KPIs reset. Your reaction: “This is now part of our operations.”

**Month 18**: A competitor pitches you, willing to come in at 30% lower price. You open the calculator on switching cost:

- Rebuilding the evaluation set takes months
- Workflows need to be realigned
- Employees need to be retrained
- Service quality may drop during the transition

**Conclusion: Unless the discount is substantial, the cost of switching is prohibitive.**

This is **“vendor lock-in by tacit knowledge”** — more implicit, deeper, and harder to unwind than classic SaaS lock-in.

And many enterprises will discover: **as their dependence deepens, the vendor begins to adjust contract pricing.**

## Questions you should be asking:

1. **Is the evaluation set exportable?** Is the export format compatible with other AI models or platforms?
2. **Are there pricing-protection clauses?** (E.g., renewal price caps, annual cost-increase limits, transition terms?)
3. **Are there transition-of-service clauses?** (If the contract ends, must the vendor help you migrate to another vendor?)

## 3.4 Impact 4: When the FDE Eventually Leaves, Do You Walk Away with a System — or an Empty Shell?

The final impact is temporal: **the FDE will not be at your company forever.**

The contract may end. The AI company may pivot strategically. The specific FDE assigned to you may quit. The AI company may be acquired, broken up, or restructured.

When the FDE walks out, what is left at your company?

Scenario A (ideal)

Scenario B (the default)

Evaluation set

In your hands

In the AI company’s hands

Prompt configuration

In your hands

Possibly part of a cloud service

Internal capability

Your team runs / tunes / extends

Only knows how to use the front-end UI

Post-departure impact

System keeps running; you switch vendors

Operational capability regresses months

**In the absence of explicit negotiation, the default outcome of most FDE contracts is Scenario B.**

Not because AI companies are “evil.” This is rational commercial strategy. Any service provider, given the choice, prefers contract structures where **the customer can’t take the work product with them.**

But as the customer, you must understand: **you’re signing a contract whose short-term value is certain and whose long-term risk is undefined.**

## Questions you should be asking:

1. **At contract termination, what exactly can you take with you?** (Listed in writing.)
2. **Does your company have an “internal handover” capability plan?** (Training your own people, not perpetually relying on FDE.)
3. **If the FDE suddenly leaves, how long would it take your company to resume independent operations?** (This number should be in the contract.)

## Part IV: Why the Economics of On-Premise AI Have Re-Emerged in 2026

After reading the four impacts above, you might ask: “ **So can we just not sign an FDE deal? Can we just do this ourselves?**”

## Get Caffein Chen (陳穎漢)’s stories in your inbox

Join Medium for free to get updates from this writer.

Two years ago I would have answered: “Hard. The technical barrier is too high, the open-source model gap too wide, and the total cost doesn’t necessarily pencil.”

But in 2026, **the answer has changed.**

## 4.1 The Capability Gap on Open-Source Models Has Narrowed Dramatically

Tracking the past 24 months of open-source LLM evolution:

- **Early 2024**: GPT-4 vs. Llama 2 70B — a clear capability gap
- **Late 2024**: Llama 3.1 405B and Qwen2.5–72B emerge, reaching GPT-4 tier
- **2025**: DeepSeek V3, Llama 3.3, Mistral Large 2 — multiple benchmarks reach GPT-4o tier
- **Early 2026**: Llama 4 Scout and Maverick (Behemoth flagship still in training, release date TBD), Qwen 3, DeepSeek V3.2, Mistral Large 3, Gemma 4 all released — **on many benchmarks, approaching closed-source frontier models**

The real situation in May 2026: **for the majority of enterprise tasks (RAG, document processing, coding assistance, customer service automation, RCA report generation), open-source models are now genuinely usable.**

The remaining capability gap — frontier reasoning, cutting-edge multimodal, top-tier agentic — **is not a hard requirement for most enterprise use cases.**

## 4.2 The Hardware and Software Ecosystem Has Matured

Two years ago, self-hosting an LLM was an R&D project. In 2026, it’s increasingly an IT procurement project.

**Hardware layer**:

- HPE Private Cloud AI, Dell AI Factory, Lenovo Neptune all ship turnkey solutions
- NVIDIA RTX Pro 6000 Blackwell, L40S, H200 enterprise GPUs are in stable supply
- From procurement to live deployment can be compressed to 4–8 weeks

**Software layer**:

- vLLM, TGI, Ollama and other inference frameworks have stabilized
- LangChain, LlamaIndex and other RAG frameworks are widely adopted
- Open WebUI, AnythingLLM and other open-source interfaces are production-ready

**Operations layer**:

- Quantization techniques (GGUF, AWQ, GPTQ) let large models run on mid-tier hardware
- LoRA, QLoRA make fine-tuning affordable
- vLLM tensor parallelism makes multi-GPU deployment straightforward

**The on-ramp difficulty of the entire technical stack is now within reach of a typical enterprise IT team that’s willing to invest.**

## 4.3 Cost Comparison: Illustrative Estimates

Let’s run an **illustrative** TCO comparison, for a mid-sized SI/MSP company serving 80 engineers, over a 3-year horizon:

> ***Important note****: These are illustrative estimates for the sake of reasoning, not a rigorous financial model based on a specific configuration. Real costs vary significantly with scale, availability requirements, and compliance needs. Actual enterprise decisions should rely on detailed assessments.*

**Option A: Cloud AI API + FDE service**

- Cloud API cost (illustrative): 80 users × `$200/mo` × 36 mo ≈ `$576,000` USD
- FDE service cost: mid-to-large enterprise contracts ≈ `$300K-500K` USD/year × 3 years ≈ `$1,200,000` USD
- **Estimated total: ≈ `$1,776,000` USD**

**Option B: On-premise + open-source models (illustrative)**

- Hardware + software + colo: ranges from low six-figures to low seven-figures depending on scale
- 1–2 AI operations architects: salary range varies with seniority and market
- Open-source model licensing: typically no licensing fee, but real training and maintenance costs

> ***What matters isn’t the absolute number — it’s the structural difference in cost shape****: as usage grows, the marginal-cost curve of on-prem deployment is flatter.* ***That’s the structural advantage of scale.***

## 4.4 Four Structural Advantages of On-Premise Deployment

Beyond cost, on-prem has four characteristics FDE cannot easily match:

## Advantage 1: Complete data sovereignty

All data, prompts, evaluation sets, and inference logs **stay within your company’s control.**

No need to worry about:

- Whether the AI company can see your data
- Whether your data is used to train other models
- Whether cross-border transfer violates regulations
- What happens to your data when the contract ends

For regulated industries (finance, healthcare, government, telecom), this is often **a contractual requirement.**

## Advantage 2: Vendor independence

The beauty of open-source models is: **you can evaluate and switch at any time.**

Using Mistral Large 3 today? When a better model arrives next year, you can evaluate migration (as long as your evaluation set is in your hands).

Compared to “locked to one AI vendor” under FDE, this is a **structural difference in bargaining power.**

## Advantage 3: Knowledge internalization

When you have a dedicated AI operations team, they develop deep understanding of:

- How prompts are designed
- How evaluation sets are constructed
- How models are tuned
- How errors are debugged

**That knowledge stays in your company.** It becomes a transferable organizational capability.

Compared to “FDE leaves and so does the understanding,” this is **a fundamental long-term difference in capability building.**

## Advantage 4: A more stable long-term cost structure

On-prem cost curve: **high up-front investment, then marginal cost stabilizes.**

Once the infrastructure is in place and the team is built, **incremental usage doesn’t necessarily mean linear cost increase.**

Compared to FDE / cloud API’s “more usage, more pay” linear cost curve, at scale this becomes **a qualitative difference.**

## 4.5 The Real Costs of On-Premise Deployment

Let me be honest: **on-prem is not a silver bullet. It has real costs.**

**Cost 1: You need to develop internal talent** You need dedicated AI operations engineers. In Taiwan’s 2026 labor market, this role has **limited supply and high salaries** — both hiring and retention are challenging.

**Cost 2: Capability ceilings exist** Open-source models still trail current closed-source flagship models on some dimensions. For applications that demand absolute frontier capability (deep reasoning, complex agentic, cutting-edge multimodal), on-prem will face real limits.

**Cost 3: You must own model maintenance** New models emerge. Old models age. Decisions about when to upgrade fall on you. For traditional enterprises without an R&D culture, **this is a fundamental shift in operating model.**

**Cost 4: Year 1 ROI doesn’t look great** On-prem value typically shows in Year 2 and Year 3. Year 1 is usually “ **build the base, break even or take a small loss.**” For management focused on short-term returns, **this is a real persuasion challenge.**

## 4.6 Conclusion: Not “FDE vs. On-Prem” — That’s the Wrong Question

Let me state this part’s core point bluntly:

**“FDE or on-prem?” is the wrong question.**

The right question is:

> ***“In my company’s specific context, which AI capabilities should be on-prem, and which should come via FDE or cloud API?”***

This is a **layered sourcing strategy** problem, not a single-choice problem.

Reasonable allocation might look like:

- **Core, high-frequency, high-sensitivity applications** → On-prem (data sovereignty + bargaining power + long-term cost control)
- **Frontier, low-frequency, cutting-edge-required applications** → FDE or cloud API (acquire frontier capability)
- **Transition / learning phase** → Use FDE to accelerate onboarding, while building on-prem capability in parallel, **internalize over the next few years**

This hybrid strategy is **the pragmatic answer for mature enterprises in 2026.**

Two real challenges in executing this hybrid: the line between “core” and “frontier” is **dynamic** — today’s frontier may be tomorrow’s core. And your internal team’s capability growth must keep pace with model iteration and business demand, which places real demands on your organization’s learning capacity. Neither has a standard answer; every enterprise needs to evaluate and adjust continuously based on its own context.

## Part V: Concrete Guidance for Enterprise Buyers

## 5.1 If You’re Evaluating an FDE Proposal Right Now

If OpenAI, Anthropic, Google, or their partners are pitching FDE services to you, **don’t sign yet. Ask these five questions first:**

**Question 1**: **Who owns the IP of the evaluation set?**

- Default answer is usually the AI company. What you should push for: **“customer co-owned”** or **“customer-exclusive”**

**Question 2**: **At contract termination, what can I take with me?**

- Listed in writing as a takeaway inventory
- Including: prompt configuration, evaluation set, training data, model weights (if fine-tuned), operational documentation

**Question 3**: **Will you commit that “knowledge learned from us will not be used for other customers in our industry”?**

- Default is usually no commitment. **This clause is worth fighting for — possibly worth paying a premium for.**

**Question 4**: **What is the price-protection mechanism?**

- Renewal price ceilings, annual increase caps, transition terms

**Question 5**: **What is the transition-of-service clause?**

- If the contract ends, must the vendor help you transition to another vendor? For how long? At what cost?

**These five questions still have negotiating room in the early-2026 FDE market.**

By 2028, when the market matures, **these may all become “standard terms — take it or leave it,” and you’ll have no choice.**

## 5.2 If You Want to Build Internally But Don’t Know Where to Start

If your company hasn’t deployed any AI yet but is **willing to build in-house**, suggested sequencing:

**Step 1: Pick a low-risk, high-frequency, easily measurable use case for the MVP**

- Don’t start with high-risk autonomous-agent scenarios
- Start with “ **document review**,” “ **RCA draft generation**,” “ **vulnerability matching** ” — i.e., “AI advises, humans decide”

**Step 2: Evaluate on-prem infrastructure feasibility**

- Look at HPE Private Cloud AI or comparable solutions
- Understand the characteristics of Mistral, Llama, Qwen
- Assess the cost and feasibility of hiring 1–2 AI operations architects

**Step 3: Use 16–24 weeks for the MVP, evaluate honestly**

- Don’t promise unrealistic numbers like “6-month payback”
- Use a “Y1 build base, Y2 validate value, Y3+ accelerate” three-year frame
- Be transparent: adoption typically follows a “ **curiosity → skepticism → adaptation → habit** ” curve

**Step 4: After MVP, evaluate whether FDE is needed to fill gaps**

- If you only lack frontier capability → cloud API
- If you lack deep industry customization → short-term FDE
- If neither → keep going on-prem

## 5.3 If You’re Already Locked Into an FDE Contract but Now Worried

If you’re already in an FDE contract but reading this article is making you uneasy, **it’s not too late.** Three actions:

**First, start a parallel “internal capability buildout” track**

- Don’t terminate the FDE contract immediately
- Stand up 1–2 internal AI engineers working alongside the FDE
- Goal: have the internal team capable of **“taking over”** within 12–18 months

**Second, secure an internal backup of the evaluation set**

- Even if the contract doesn’t explicitly require it, you can ask the FDE to “ **sync a copy of the evaluation set to the internal team** ”
- During the contract, FDEs usually won’t refuse — they may interpret it as “the customer wants to participate more deeply”
- In reality, this is your **portable asset.**

**Third, renegotiate at renewal**

- Add the five questions from 5.1 as renewal conditions
- If they won’t budge, **at least you know where the negotiating space is.**
- If they do budge, **you’ve secured what you wouldn’t have gotten by default.**

## Part VI: Limitations of This Article

Before the conclusion, I want to be explicit about this article’s limits:

1. **Core facts are based on public information**: This analysis draws on publicly available announcements and industry reports from May 2026. It does not cover internal vendor strategy or non-public information.
2. **Cost estimates are illustrative**: The cost comparisons in Part IV are illustrative examples for the sake of reasoning, not rigorous financial models based on specific configurations. Real enterprise decisions require detailed assessment.
3. **Applicability varies by industry and company size**: The analytical framework is general, but specific conclusions should be adapted to your own context — not applied verbatim.
4. **Strategic interpretation reflects a point-in-time view**: Sections on “why now” and “how enterprises should respond” reflect analysis at the current moment; as the market evolves, reassessment will be needed.

## Conclusion: This Isn’t Anti-AI — It’s About Embracing AI More Wisely

Let me be clear:

**This article isn’t against FDE. It isn’t against cloud AI. It isn’t against AI deployment.**

I am a heavy AI user myself. In writing this article, I used multiple AI models to assist with research and drafting, with cross-validation. My own company is planning on-prem AI deployment. I deeply believe AI is one of the most important enterprise topics of 2026.

What I am against: **embracing any direction blindly, without understanding the structural shift in power dynamics underneath.**

The hyperscalers are betting on FDE for their own commercial reasons and their own interest calculations. As people working in the enterprise AI deployment field, **we cannot only see FDE’s short-to-medium-term capability uplift and miss the power structure forming underneath.**

Three sentences capture this article’s core view:

1. **AI product economics differ fundamentally from traditional SaaS — this is restructuring the path of AI commercialization, and FDE is a product of that restructuring.**
2. **FDE introduces four structural impacts: tacit knowledge flow, redrawn data boundaries, eroded negotiating power, and hollowed-out exits.**
3. **By 2026, the conditions for on-premise deployment have matured. Enterprises should adopt a “layered sourcing” strategy — not outsource all AI capability to a single source.**

If this article has been useful, I hope it serves as **one additional angle** when you’re negotiating with AI vendors, making AI investment decisions, or planning your company’s AI roadmap.

It’s not the answer. It’s **one overlooked angle.**

The decision is still yours.

If you’re currently working through an AI procurement decision, or have signed (or declined) an FDE proposal recently, I’d love to hear what you’ve seen — what have you noticed that I missed?

## Postscript: On How This Article Was Written

This article used AI assistance throughout the drafting process — research aggregation, initial drafts, and multi-round cross-validation.

The core viewpoints, case selection, and risk framework reflect the author’s interpretation. Corrections and counter-arguments are welcome.

I think the writing process itself is a small practical demonstration of the article’s theme: **in the AI era, learn to use AI wisely — rather than be used by it.**

## References

## Category 1: Primary Announcements of the Three Events

1. OpenAI. (2026). *OpenAI Launches the Deployment Company*. OpenAI. [https://openai.com/index/openai-launches-the-deployment-company/](https://openai.com/index/openai-launches-the-deployment-company/)
2. Krupp, L. (2026, May 11). OpenAI DeployCo Private Equity. *Axios*. [https://axios.com/2026/05/11/openai-deployco-private-equity](https://axios.com/2026/05/11/openai-deployco-private-equity)
3. de la Mare, A. (2026). OpenAI Deployment Company: Tomoro Acquisition. *The Next Web*. [https://thenextweb.com/news/tomoro-openai-deployment-company-consulting](https://thenextweb.com/news/tomoro-openai-deployment-company-consulting)
4. PYMNTS. (2026). OpenAI Launches `$4 Billion` Company to Accelerate Enterprise AI Adoption. [https://pymnts.com/news/artificial-intelligence/2026/openai-launches-4-billion-dollar-company-accelerate-enterprise-ai-adoption/](https://pymnts.com/news/artificial-intelligence/2026/openai-launches-4-billion-dollar-company-accelerate-enterprise-ai-adoption/)
5. Yeh, S. (2026, May 4). Anthropic Takes Shot at Consulting Industry in Joint Venture with Wall Street Giants. *Fortune*. [https://fortune.com/2026/05/04/anthropic-claude-consulting-industry-joint-venture-blackstone-goldman-sachs/](https://fortune.com/2026/05/04/anthropic-claude-consulting-industry-joint-venture-blackstone-goldman-sachs/)
6. Yeh, S. (2026, May 5). Anthropic Deepens Push into Wall Street with New AI Agents. *Fortune*. [https://fortune.com/2026/05/05/anthropic-wall-street-financial-services-agents-jamie-dimon/](https://fortune.com/2026/05/05/anthropic-wall-street-financial-services-agents-jamie-dimon/)
7. Yahoo Finance. (2026). Anthropic Forms `$1.5B` Joint Venture with Blackstone, Goldman Sachs. [https://finance.yahoo.com/sectors/technology/articles/anthropic-forms-1-5b-joint-123147935.html](https://finance.yahoo.com/sectors/technology/articles/anthropic-forms-1-5b-joint-123147935.html)
8. The Information. (2026, May 12). Google to Hire Hundreds of Engineers to Help Customers Adopt Its AI. [https://www.theinformation.com/briefings/google-hire-hundreds-engineers-help-customers-adopt-ai](https://www.theinformation.com/briefings/google-hire-hundreds-engineers-help-customers-adopt-ai)
9. Tech Startups. (2026, May 13). The Human Side of Agentic AI Adoption. [https://techstartups.com/2026/05/13/the-human-side-of-agentic-ai-adoption-hundreds-of-forward-deployed-engineers/](https://techstartups.com/2026/05/13/the-human-side-of-agentic-ai-adoption-hundreds-of-forward-deployed-engineers/)
10. Channel Dive. (2026). Google Cloud Is Hiring an Army of AI Deployment Engineers. [https://channeldive.com/news/google-cloud-forward-deployed-engineering-jobs/820176/](https://channeldive.com/news/google-cloud-forward-deployed-engineering-jobs/820176/)
11. Schnitzler, J. (2026). Google, Box CEOs Say This Is the Most In-Demand Job in Tech. *Fast Company*. [https://www.fastcompany.com/91541878/google-box-ceos-say-this-is-the-most-in-demand-job-in-tech](https://www.fastcompany.com/91541878/google-box-ceos-say-this-is-the-most-in-demand-job-in-tech)
12. OfficeChai. (2026). Google Is Hiring Forward Deployed Engineers to Help Organizations Adopt AI. [https://officechai.com/ai/google-is-hiring-forward-deployed-engineers-to-help-organizations-adopt-ai](https://officechai.com/ai/google-is-hiring-forward-deployed-engineers-to-help-organizations-adopt-ai)

## Category 2: Historical Context of the FDE Model

1. Orosz, G. (2025). What Are Forward Deployed Engineers, and Why Are They So in Demand? *The Pragmatic Engineer Newsletter*. [https://newsletter.pragmaticengineer.com/p/forward-deployed-engineers](https://newsletter.pragmaticengineer.com/p/forward-deployed-engineers)
2. Cagan, M. (2025). Forward Deployed Engineers. *Silicon Valley Product Group*. [https://svpg.com/forward-deployed-engineers/](https://svpg.com/forward-deployed-engineers/)

## Category 3: Research on AI Product Gross Margins

1. Lemkin, J. (2026). The Execution Era of AI: 5 Key Takeaways from ICONIQ’s State of AI Report. *SaaStr*. [https://www.saastr.com/the-execution-era-of-ai-5-key-takeaways-from-iconiqs-state-of-ai-report/](https://www.saastr.com/the-execution-era-of-ai-5-key-takeaways-from-iconiqs-state-of-ai-report/)
2. SaaStr. (2026). Top 10 Learnings from Sapphire Ventures’ 2026 Software x AI Report. [https://www.saastr.com/top-10-learnings-from-sapphire-ventures-2026-software-x-ai-report-80-100m-arr-ai-startups-the-ultra-round-is-the-new-normal-and-enterprise-is-50-of-vc-now/](https://www.saastr.com/top-10-learnings-from-sapphire-ventures-2026-software-x-ai-report-80-100m-arr-ai-startups-the-ultra-round-is-the-new-normal-and-enterprise-is-50-of-vc-now/)
3. SFAI Labs. The AI Project Gross-Margin Reset Every SaaS Company Is About to Face. [https://sfailabs.com/guides/the-ai-project-gross-margin-reset-every-saas-company-is-about-to-face](https://sfailabs.com/guides/the-ai-project-gross-margin-reset-every-saas-company-is-about-to-face)
4. Monetizely. (2025, October). The Economics of AI-First B2B SaaS in 2026. [https://getmonetizely.com/blogs/the-economics-of-ai-first-b2b-saas-in-2026](https://getmonetizely.com/blogs/the-economics-of-ai-first-b2b-saas-in-2026)
5. Trending Topics EU. (2026, May). AI Is Eating Software Margins. [https://trendingtopics.eu/ai-software-margins/](https://trendingtopics.eu/ai-software-margins/)
6. ICONIQ Capital. (2026, January). *State of AI Report 2026*. (Paid report. The primary original source for this article’s references to AI product gross margins (~52%) and inference cost as a share of revenue (~23%).)

## Category 4: Open-Source LLM Maturity

1. Hugging Face Blog. (2026, April). DeepSeek-V4: A Million-Token Context That Agents Can Actually Use. [https://huggingface.co/blog/deepseek-v4](https://huggingface.co/blog/deepseek-v4)
2. Hugging Face Blog. (2026, April). Granite 4.1 LLMs: How They’re Built. [https://huggingface.co/blog/granite-4-1-llms](https://huggingface.co/blog/granite-4-1-llms)
3. Hugging Face Blog. (2026, May). Granite Embedding Multilingual R2. [https://huggingface.co/blog](https://huggingface.co/blog)

## Category 5: Enterprise On-Premise AI Platforms

1. Hewlett Packard Enterprise. (2026, March). HPE Accelerates Secure, Scalable Production-Ready AI Through New Innovations with NVIDIA. *HPE Newsroom*. [https://www.hpe.com/us/en/newsroom/press-release/2026/03/hpe-accelerates-secure-scalable-production-ready-ai-through-new-innovations-with-nvidia.html](https://www.hpe.com/us/en/newsroom/press-release/2026/03/hpe-accelerates-secure-scalable-production-ready-ai-through-new-innovations-with-nvidia.html)
2. WEI. How HPE GreenLake Intelligence Powers On-Prem AI Infrastructure and Secure Edge Deployment. [https://www.wei.com/blog/how-hpe-greenlake-intelligence-powers-on-prem-ai-infrastructure-and-secure-edge-deployment/](https://www.wei.com/blog/how-hpe-greenlake-intelligence-powers-on-prem-ai-infrastructure-and-secure-edge-deployment/)

## Category 6: FDE Role Debates and Critiques

1. Lemkin, J. (2026). Who Gets an FDE, and Who Doesn’t: The Great B2B + AI Debate Right Now. *SaaStr*. [https://www.saastr.com/who-gets-an-fde-and-who-doesnt-the-great-b2b-ai-debate-right-now/](https://www.saastr.com/who-gets-an-fde-and-who-doesnt-the-great-b2b-ai-debate-right-now/)
2. Flybridge. Why 95%+ of Startups Get the Forward Deployed Engineer Role Completely Wrong. [https://www.flybridge.com/ideas/the-bow/why-95-of-startups-get-the-forward-deployed-engineer-role-completely-wrong](https://www.flybridge.com/ideas/the-bow/why-95-of-startups-get-the-forward-deployed-engineer-role-completely-wrong)
3. Parekh, M. AI’s “FDEs” Go from Forward Deployed Engineers to Entities. *Substack*. [https://michaelparekh.substack.com/p/ais-forward-deployment-fdes-go-from](https://michaelparekh.substack.com/p/ais-forward-deployment-fdes-go-from)

## Further Reading: Alternative Perspectives

There are a few worthwhile English-language pieces on this topic. If you want to see different angles:

**【Mainstream Investor View】** ► a16z — *Trading Margin for Moat: Why the FDE Is the Hottest Job in Startups* (June 2025) [https://a16z.com/services-led-growth/](https://a16z.com/services-led-growth/) (From the AI-vendor investor perspective, arguing FDE is the right strategy of “trading margin for moat.” Position is the opposite of this article — worth reading in contrast.)

**【Structural Analysis】** ► Stratechery / Ben Thompson — *The Deployment Company, Back to the 70s* (May 13, 2026) [https://stratechery.com/2026/the-deployment-company-back-to-the-70s-apple-and-intel/](https://stratechery.com/2026/the-deployment-company-back-to-the-70s-apple-and-intel/) (One of the English-language world’s most respected tech analysts. Places the FDE trend in the historical context of 1970s mainframe-era computing. Complementary to this article’s angle.)

**【Critical Voices】** ► Thomas Otter — *On the Forward Deployed Engineer, PLG and Genuine Adoption* (December 2025) [https://thomasotter.substack.com/p/on-the-forward-deployed-engineer](https://thomasotter.substack.com/p/on-the-forward-deployed-engineer) (A former SAP executive’s sharp critique: “Many roles labeled ‘FDE’ are just implementation engineers with a cooler title — not real product work.”)

► Flybridge — *Why 95%+ of Startups Get the FDE Role Completely Wrong* (December 2025) [https://www.flybridge.com/ideas/the-bow/why-95-of-startups-get-the-forward-deployed-engineer-role-completely-wrong](https://www.flybridge.com/ideas/the-bow/why-95-of-startups-get-the-forward-deployed-engineer-role-completely-wrong) (VC critique: “The FDE model is widely misunderstood — and only works under very specific conditions.”)

⚠️ **Honest framing**: The angles of these pieces differ from this article. a16z is the seller-side view (what AI companies should do); Stratechery is macro tech-industry analysis; this article focuses on what enterprises in the deployment field need to watch out for. To my knowledge, the English-language conversation lacks a systematic risk analysis from this angle. This article is an attempt to fill that gap.
