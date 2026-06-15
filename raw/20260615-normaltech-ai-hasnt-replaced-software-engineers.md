---
type: raw
source: "https://www.normaltech.ai/p/why-ai-hasnt-replaced-software-engineers"
author:
  - "[[NormalTech]]"
published: "2026-06-11"
created: "2026-06-15"
tags:
  - clippings
  - ai-replacement
  - software-engineering
  - labor-market
  - agentic-engineering
  - vibe-coding
  - decide-execute-deliver
---

# Why AI hasn't replaced software engineers, and won't

**来源**: https://www.normaltech.ai/p/why-ai-hasnt-replaced-software-engineers  
**发布时间**: 2026-06-11  
**作者**: NormalTech (Princeton SAGE Lab)

---

There is great anxiety and uncertainty about AI replacing jobs. How can we move past vague warnings and bombastic predictions and bring data to bear on this question? One good way is to look at the profession where AI capabilities are furthest along and adoption has been exceptionally rapid: software engineering.

In this essay, we argue that there is enough evidence to reject the narrative that once AI capabilities reach a certain threshold, it will cause mass layoffs. Given that this is true even in a sector with very few regulatory barriers, most other professions are likely to be even more cushioned.

We also have a good understanding of why this is the case. We can think of many kinds of knowledge work, including software development, as a "decide-execute-deliver sandwich". AI compresses the "execute" layer — the middle of the sandwich — but the other two layers resist automation in a way that will not be overcome by capability improvements alone.

We conclude on a note of cautious optimism about the future trajectory of demand for software engineering. This essay is the first in a series, and the next one will look at reasons why individual software engineers' careers might be rocky even if overall demand is healthy.

## The AI-Washing of Job Cuts

Consider three stories that made the headlines and how they contrasted with reality:

### Block (Cash App)
In February, fintech company Block announced layoffs of 4,000 employees because, according to founder Jack Dorsey, AI is "enabling a new way of working" with "smaller and flatter teams", specifically citing late-2025 improvements in model capabilities.

But subsequent reporting revealed a radically different picture. After growing headcount more than threefold during the pandemic, the company was under massive financial pressure. A data scientist on the Cash App team, Naoko Takeda posted that Block "shoved AI down everyone's throats" yet she saw "very limited gains in productivity." She refused a 75% retention raise and quit. Other employees interviewed had a sharply different understanding of what AI was capable of at Block and whether Dorsey had a competent understanding of the issues.

As Aaron Levie has pointed out, CEOs are uniquely prone to delusions about AI's usefulness because they can build quick prototypes but can't see the 90% of work it takes to turn it into a finished product. Dorsey's public statements about AI seem to fit exactly this pattern.

### Snap
In April, Snap laid off about 1,000 people, with CEO Evan Spiegel primarily citing AI as the reason in his layoff memo. He also said that AI generated 65% of new code. In reality, the layoffs followed a campaign by an activist investor demanding cost cuts. (Snap has posted a net loss every full year since its 2017 IPO and shares were down over 30% in 2026). Tellingly, the nature of the cuts, such as 150 jobs spanning various roles in the augmented reality division, don't correlate with the cuts we would expect to see if they were driven by AI (i.e. programming and other "AI-exposed" jobs across the board, not concentrated in any unit).

### Intuit
In May, Intuit announced 3,000 cuts, alongside deals with Anthropic and OpenAI. The press connected the two, framing the layoffs as AI-driven restructuring. For once, the CEO actually pushed back on this easy narrative, saying that "none of it had to do with AI" and that the cuts targeted "coordination-heavy roles" and too many management layers.

## The Data on AI-Driven Layoffs

We did not cherry-pick these examples. In every story about AI-driven software engineering layoffs that we examined, the same narrative violation emerged. It turns out that "AI washing" of job cuts is an economy-wide phenomenon, evidenced by many surveys:

- 59% of U.S. hiring managers admitted they emphasize AI when explaining hiring freezes or layoffs because it plays better with stakeholders than citing financial constraints.
- Forrester principal analyst J. P. Gownder says of companies preparing supposedly AI-driven layoffs: "When we ask if they have a mature, vetted AI app ready to fill in those jobs, nine out of 10 times, the answer is no—and they haven't even started."
- In a HBR survey of over 1,000 global executives, 21% had made large headcount reductions "in anticipation of" AI, with another 39% having made low or moderate anticipatory headcount reductions. In contrast, only 2% had already made large reductions in headcount related to actual AI implementation. The 10x gap suggests that executives, like everyone else, are highly prone to succumbing to the misleading narratives about AI replacing jobs.

## The WARN Act Data

Another interesting data point comes from the WARN Act, which requires certain disclosures of plant closings and mass layoffs affecting over 100 workers. In March 2025, New York became the first U.S. state to add an AI disclosure checkbox to WARN Act filings. In the full first year, more than 160 companies filed WARN notices. Not a single one checked the AI box. We reached out to the NY Department of Labor who confirmed that as of late May, only one company, Nespresso, checked the box. If these filings are accurate, only 46 out of about 25,000 laid off workers in New York State in the relevant period, or about two-tenths of a percent, were affected by AI.

## The Wrong Signal

Even more damning for the AI-driven-mass-layoffs narrative: layoffs are the wrong signal of AI's potential productivity benefits in the first place! The research is clear that the effect operates through "slower hiring rather than increased separations". Firing existing workers results in the loss of precisely the tacit knowledge and organizational capital that allows workers to operate AI effectively. Besides, it is expensive in terms of severance, damage to morale, and rehiring risk. Given these costs, it is largely unnecessary given that natural turnover achieves the same result in a few years.

## Overall Employment Trends

So what does the data tell us when we look beyond layoffs to overall employment trends? An important paper from Federal Reserve economists compiles the evidence in the U.S. context. Software engineer employment is still growing, but they find that it is growing slower post-ChatGPT compared to a no-AI counterfactual, by about 3 percentage points per year. One important limitation of this study is that the methodology can't capture self-employment, so it is possible that some of the slowdown in growth is being absorbed by entrepreneurship instead. We do have evidence from other studies that AI makes entrepreneurship easier. So the real picture is probably even healthier than the Federal Reserve study suggests.

## The Decide-Execute-Deliver Sandwich

Many tech leaders, like the Snap CEO above, report the percentage of code written by AI alongside reports of layoffs or predictions of future job losses. This feeds into the simplistic mental model that once AI writes all the code, there is no need for coders. Fortunately, this mental model is wrong. This AI-written-code metric is almost completely disconnected from what matters for labor displacement.

Writing code isn't, and never was, the bottleneck. For example, a 2019 paper summarized existing studies with the conclusion that "developers spend surprisingly little time with coding, 9% to 61% depending on the study". This finding was consistent with the paper's own data from 6,000 developers at Microsoft. As coding agents began to be taken up, there was an explosion of blog posts in late 2025 pointing out that writing code isn't the bottleneck, as developers realized that using agents to write most of the code led to little impact on overall productivity.

If writing code isn't the bottleneck, what is? The task-breakdown surveys point at things like meetings or debugging. This just leads to more questions: what are developers doing in those meetings and why can't it be done by AI? Won't debugging get automated as capabilities improve? To understand the real bottlenecks, we have to get qualitative, and dig into software engineers' own understanding of what it is they do that resists automation.

When we did this analysis, it revealed three things as the real bottlenecks:
1. Deciding and specifying what to build
2. Verifying and being accountable for what is delivered
3. The deep human understanding — of the codebase, the business, and the environment — required to carry out both of these.

In other words, software engineers' work consists of a "decide-execute-deliver" sandwich (with understanding being a prerequisite for all three). AI has compressed the middle of the sandwich, but has left the two ends largely unchanged. As long as software development teams are in charge of decision making and accountable for what they deliver, engineers still need to spend time building up a deep understanding of the system. These are the three bottlenecks.

### The Evidence

Evidence for the sandwich model of AI's productivity effects comes from a recent paper on "Writing Code vs. Shipping Code". Across 100,000 developers on GitHub, the researchers found that AI agents led to an eight-fold increase in the number of lines of code written, consistent with the idea that AI almost completely compresses the Execute layer of the sandwich. But this led to only 30% more releases, strongly suggesting that human bottlenecks (the Decide and Deliver layers) remain in place.

### Can the Sandwich Be Further Compressed?

We don't think so. At one end of the pipeline, development teams need to decide what to build. One of the most important lessons junior software engineers learn is that requirements specification (the profession's lingo for this layer) takes surprisingly long, and if it is compressed, it leads to much more pain down the line. This layer is hard to automate because it requires thinking about user needs, market signals, organizational priorities, and in some cases regulatory constraints.

As AI capabilities improve, the kinds of decisions that can be delegated to AI increase over time. But this does not make the "decide" layer thinner — once a decision can be delegated to AI, it is no longer a source of competitive advantage, and the value of human decision-making migrates upward. Software increases in complexity over time, so there is no ceiling to this process.

At the other end of the sandwich, human teams need to be accountable for what they deliver. It is possible that some day in the future teams will ship mission-critical code without fully testing and understanding it, but today's AI is so unreliable that such haphazard practices would represent an existential threat to software teams and their customers.

Even if the technical barriers go away in the future, we don't have to cede control to AI. A central insight of AI as Normal Technology is that we can collectively choose to keep humans accountable through shared norms, law, and policy. This is a much more resilient way to control the speed of AI impacts and improve safety than trying to slow the development of technical capabilities. These speed barriers are already largely in place due to liability laws and sector-specific regulation, but can be further strengthened.

In this vision, as more and more of the execution layer gets delegated to AI, the software engineer's role in the future becomes analogous to that of a crane operator. AI agents will do most of the cognitive heavy lifting; supervising the agent and keeping it in control becomes most of the human's job.

## The Programmer vs Software Engineer Distinction

By the way, the sandwich getting squished is a new trend and it is not uniquely due to AI. Over two decades ago, the Bureau of Labor Statistics started tracking programming separately from software engineering. Roughly speaking, programmers are responsible only for execution while software engineers manage a bigger part of the sandwich. Not only has programming been shrinking, it is also pays much less because it is seen as grunt work. AI merely accelerates this long-existing trend, further devaluing purely technical skills.

## Broad Applicability

This pattern — where humans remain heavily involved at both ends of the decide-execute-deliver sandwich, even as AI increasingly automates the middle layer — seems to be broadly applicable to most knowledge work, though it is farthest along in software. After all, complex decision making and accountability are common to most fields. A lack of recognition of this phenomenon has led to many overconfident claims about imminent job losses, such predictions about AI replacing radiologists.

## Vibe Coding vs Agentic Engineering

One reason for confusion about the extent to which software engineering is changing is the sloppy use of the term "vibe coding" to refer to a wide spectrum of practices, the ends of which are conceptually distinct and more dissimilar than similar.

In true vibe coding the user simply tells the agent what to do, doesn't supervise it when it's running, doesn't review the code — might not even have the skills to do so — and doesn't evaluate the output, beyond perhaps noticing when things are visibly broken.

This is in contrast to how most software engineers are actually using agents — as a tool, with the human remaining in control and accountable for the output. Fortunately, the term agentic engineering is gaining currency as a descriptor of this practice.

As agentic engineering has become the norm, engineers are discovering that supervising coding agents is surprisingly time consuming. For example, Simon Willison, a prominent developer and chronicler of the AI transition, has noted how he is mentally exhausted by 11am from supervising agents. This is consistent with our experience as well.

More quantitative evidence comes from SWE-chat, a dataset of coding agent interactions from open-source developers who opted into a logging tool. The study found that only 44% of agent-produced code survives into user commits, that vibe-coded commits introduce vulnerabilities at nine times the human-only rate, and that the most common user intent is understanding existing code, not generating new code (19% vs 13%).

## The Jevons' Paradox for Software

AI boosters might claim that mass layoffs are coming; they just haven't happened yet because human-level software engineering abilities are very recent (or haven't been achieved yet). But if the sandwich model is correct, these predictions won't come true. AI has already largely compressed the middle of the sandwich (and the compression actually started decades ago). So even making the execution layer instant and perfect will only be a small change from the status quo. The reasons why the other two layers have resisted AI is not because of capability limitations.

In fact, not only are software engineering jobs not going away due to AI, there might even be an increase in demand for software engineers. When software (or anything else) gets cheaper to create due to technological productivity improvements, people will buy a lot more software (in econ jargon, software is highly "price elastic"). And as we have argued, AI doesn't replace software engineers (the "elasticity of substitution" is low), so the demand for more software results in a derived demand for more software engineers. A loosely related but flashier economics term, "Jevons' paradox", is often thrown around in the AI discourse to describe this concept.

Historically, this has been the pattern — programmer employment in the U.S. has grown from near-zero around 1950 to millions today. This is sharply different from occupations such as agriculture in which labor demand was famously decimated due to mechanization and automation. The difference is that the amount of calories people consume is relatively fixed — even a 25% increase led to the obesity epidemic — whereas the amount of software produced has grown a millionfold. Modern cars have something like a hundred million lines of code running on their various on-board computers.

If there is a ceiling to the demand for code, we are nowhere near it. Virtually all cognitive work benefits from software. As AI makes coding cheaper, people are creating all kinds of one-off utilities — whether for work or personal use — that it never made sense to create until now.

## The Future of Software Engineering

To be clear, while we think there will be a lot more software in the future, and likely more software engineers, this doesn't mean big tech companies will get even bigger. The majority of software engineers today already work in-house in non-software firms, and that share might grow in the future. Then there's the idea of "AI rollups", which refers to venture capital or private equity firms buying "Main street" businesses — dentistry practices, accounting firms, and whatnot — and rebuild them from the ground up to be "AI-native" by embedding software engineers or AI engineers into those businesses.

Some people predict that demand for software engineering skills will fall because of democratization. They acknowledge that there will be more software produced than ever before, and also that more human time will be spent producing software than ever before, but that this work will be done by people who are not software engineers. The idea is that AI will democratize software engineering to the extent that legal software, for instance, can be more easily created by those with training in law than in software engineering.

Maybe. But we'll bet against it. In our view, this falls into the same trap of conflating vibe coding with agentic engineering, and the execution layer with the whole decide-execute-deliver sandwich. In fact, when we look at the history of programming, there have always been claims that we are at the threshold of democratization — old languages such as FORTRAN, COBOL, and SQL were all accompanied by such prominent hopes at the time of their introduction. It never happened. The barrier isn't actually learning the syntax. It's having enough skilled judgment to make good decisions while maintaining accountability.

Ultimately the distinction may be semantic. It seems clear that the amount of time people spend on getting computers to do new things will increase over time. This might take the form of building software, or managing complex workflows using agents, or something else. It will require a mix of software skills, AI skills, and domain expertise. Whether it is today's software engineers who will best adapt to fill these new roles remains to be seen.

## Further Reading

In a remarkable essay called No Silver Bullet 40 years ago, Fred Brooks distinguished between the "essential complexity" and "accidental complexity" of software. He argued that some of the complexity of software is accidental, arising from limitations of present technology such as the clunkiness of programming languages, and can be alleviated over time as tooling improves. But some of it is essential, because specifying the correct behavior of software is itself hard. He presents a forceful articulation of why the "decide" layer of the sandwich is thick and resists automation. Interestingly, hopes of boosting programmer productivity through AI were already prominent back then! Brooks argues that because AI or any other technology only reduces accidental complexity, it won't result in an order-of-magnitude productivity improvement.

---

**相关概念**: [[Decide-Execute-Deliver-Sandwich]], [[Agentic-Engineering]], [[Vibe-Coding]], [[Jevons-Paradox-for-Knowledge-Work]], [[AI-Replacement]], [[Software-Engineering]]
