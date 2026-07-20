---
title: "AI Mania Is Eviscerating Global Decision-Making"
source: "https://ludic.mataroa.blog/blog/ai-mania-is-eviscerating-global-decision-making/"
author: "Ludicity"
date: "2026-07-18"
added: "2026-07-20"
tags:
  - ai-hype
  - organizational-decision-making
  - ai-failure
  - institutional-capture
  - ai-governance
---

# AI Mania Is Eviscerating Global Decision-Making

Published on July 18, 2026

Note: This has been cross-posted to my company's blog, in case you think there is some use in sharing with someone in a format that looks more authoritative. Link here.

I strongly believe there are entire companies right now under heavy AI psychosis and it's impossible to have rational conversations with them about it. I can't name any specific people because they include personal friends I deeply respect, but I worry about how this plays out.

– Mitchell Hashimoto, of HashiCorp and Ghostty fame

Over the past year, I've run point on all of our company's sales, led the technical components of all but two of our engagements, and over the lifetime of this blog have had something like 300 catchups with professionals from around the world. This has ranged from people on the ground in niche service industries to executives at Fortune 500 companies. Because of this, I've had a front-row view to our collective institutions across both the private and public sector undergoing breath-taking mass psychosis. This essay is an attempt to describe the bizarre dynamics that are currently at play, as I am in the rare position where my wellbeing is not contingent on paying lip service to madness, and to reassure the people trying to survive amidst all of this that they are not crazy.

The reality is thus: the people in charge either have no plan, or see no path forwards other than keeping their heads down. Not at banks, not at hospitals, not in our government institutions. The world's organisations have been captured by people in the throes of frothing excitement, and saner people who now live in a state of constant commingled fear and frustration.

## I. AI Investments Are Generally Total Failures

Are companies actually seeing massive productivity gains from their AI adoption? Does any of this sordid affair make sense?

This should be an easy question, but it is surprisingly hard to get a straight answer to it. Executives that tell the press that their company has gone insane will quickly find themselves removed from their positions. Employees who are honest will find themselves fired in short-order, or "randomly" selected for a round of layoffs. In fact, it is in the interests of almost every actor in the space – boards, executives, employees, vendors, consultants – to obfuscate and misrepresent the success rate of AI projects. Many publicly traded companies are putting out announcements about their AI productivity gains when I know for a fact that the businesses have done nothing other than purchase Copilot licenses and declare victory.

Yet we need to know if these projects are panning out – if the total focus on AI as a core tenet of business strategy is succeeding at a reasonable rate, then a discussion about the relative risk and reward is warranted.

Unfortunately, we live in a dark timeline. All of the AI projects we have observed as a team are failing. Every single one – we have seen 0% success in a year and a half, not only amongst projects we have been asked to participate in, but even within projects that we have observed in passing while doing totally unrelated work. Even if you grant that AI tooling accelerates specific workloads, the method and scale of the current investments is senseless. Frequently the failure is not related to AI itself, but rather that companies are terminally bad at running software projects effectively, and as I have remarked previously, AI projects are subject to all the failure modes of normal projects plus you can get everything right and then still fail because of the method's novelty. Very few companies are so good at shipping software that they can afford the extra risk profile.

Often enough, though, it's an actual failure in what LLMs can accomplish. The most common version of this, being rolled out across businesses around the world, is the internally-facing chatbot, or for the more daring company, the customer-facing chatbot. The story is always the same. For the former, I've never seen substantial internal uptake from inside a business. Employees don't use internal chatbots because companies tend to have low-quality documentation and an LLM is not psychic – it can only know things that have been written down and made accessible. For the latter customer-facing applications, I have rarely had a pleasant experience as a consumer, with perhaps the exception of live transcription during medical appointments – hardly something worth pivoting an entire organisation around. In both cases, project leaders are very careful to avoid tracking basic metrics, such as whether the tools are being used at all, or they track metrics that are easily gamed.

For example, my last consumer interaction was attempting to get help from Mitsubishi following an automotive failure, where a very polite robot asked me to describe the problem and that I'd receive a call back as soon as someone was available. This was the single most competent implementation of such a project I've seen in the wild, in that the voice was natural sounding, responded quickly, was clearly "live" in production, and promised a swift resolution.

That was six months ago, and I did not, in fact, get a call back.

When Mitsubishi did not call me back, what happened? Did that request just go into the void, showing one less incident for the year? Does it appear that the phone bot resolved my query without the need for human intervention? All we know is that it didn't show up as an error, or I'd have received a call. I'm sure it looks great in all sorts of ways except the one that matters, which is that I was planning to buy a car and decided not to buy another one of theirs.

## II. Heretics Will Be Shot

It has become outright dangerous to even raise the possibility that AI might not be the solution to a problem, let alone be the sole focus of a company's entire strategy.

In every sufficiently large business we have observed (say, with 500+ employees), we have noted that continued advancement, and increasingly continued employment, has started to require repeated professions of belief in the transformative power of AI for said business. I am not talking about providing ideas about how to use AI in the business – I mean religious profession, declarations of faith. Overwhelmingly these statements are made by non-technicians, though it is not uncommon for technicians to emit deranged statements to curry favour.

There have been several occasions where I have seen someone, apropos of nothing, blurt out almost word-for-word "AI is changing everything", only to concede moments later that their organisation does not currently use LLMs for anything, and indeed, that they cannot name a single thing that has changed other than they get some use out of ChatGPT (frequently the free-tier). In one extreme case, I have seen an executive confess that they had never even used ChatGPT or any AI tool in their life, immediately after producing a technical strategy for an organisation with $2B+ in revenue which was entirely centered around AI.

Initially these statements were so absurd on their face that I thought it was some cynical ploy to achieve thought leader status, and there are certainly some people doing this – I have had it admitted to me. But the broader reality is so much worse: people who have no background in the technology at all actually believe what they are saying. As a general rule you should avoid getting into business with a liar, but if you must, you can at least reason with them even if only in private. A true believer is much more threatening because they are impervious to even inducement by self-interest.

The turning point in my belief was watching someone with a spectacular amount of money on the line fire their highest performers because they were achieving that performance without LLMs. When an employer publicly talks about AI innovation, we have to ask ourselves if they're simply trying to manipulate the market or customers. When they privately commit to strategies like this with their own money at stake, with no attempt to communicate that strategy to external clients, I can only assume they really mean what they're saying.

Several of my peers now "AI-wash" their work, meaning that even when they can perfectly competently execute on their jobs to the satisfaction of their management teams, said managers are unhappy if the engineers haven't used AI in the work… so now they're lying about using LLMs even in contexts where their professional judgement is that they aren't the appropriate tool. They just do the work, the same way they have for decades, and say Claude did it. Others are being measured on their AI bills with "token leaderboards", where higher is better… so the people hired for their freakish ability to perform system optimisation do the obvious thing. They set the LLMs prompting themselves in a semi-plausible loop in case someone inspects the token consumption and then they watch Netflix. Not a single one has been caught, even when their own assessment of the output is that it isn't suitable for deployment.

In fact, the only people I know of to be fired over this whole thing are people that have expressed visible doubt about this organisational strategy, which again, even Ptacek thinks is transparently dumb. The net result is that everyone has learned very quickly to praise executives on their visionary AI prowess, or they will be gunned down in the proverbial streets.

## III. AI Demos Are The Mind-Killer

One of the main pieces of infrastructure we deploy at our clients is an analytics-focused database called Snowflake. One of the features in Snowflake that we don't use is called Cortex – their AI chatbot layer, with the ability to plug into metadata and query a company's database autonomously. In theory, you can ask a question like "What was our revenue for last week?" and it will spit out an answer.

It is not really suitable for production usage. From memory, the last time I was given a presentation on it, by actual Snowflake staff, they reported that ideal configuration results in something like ~92% accuracy due to the complexity of data at a large business and there were serious issues with managing deployments. Nonetheless, it can be used to produce some very flashy demonstrations.

On several occasions, we've been exposed to folks that have been sort of lukewarm on our main offerings, but they really, really wanted to use AI to perform a natural language query on their data. And we thought "Okay, if you really want to see it, maybe we can caveat this appropriately and show you what it might look like."

This was a terrible mistake. It backfired in the most predictable way imaginable – every lukewarm client that saw the chatbot in action, even with us telling them that it was not going to accomplish what they wanted, wanted to buy it immediately. Every other consideration, including millions of dollars that we could plausibly help them achieve by non-AI means, was swept aside. It was like a dark and terrible force seized control of their limbs, plunged their hands into their own chests, and presented their still-beating credit cards to us in grim supplication. We were so mortified by the inexplicable shift in energy that we (wisely) declined to take the money and ended the sales process, and soon thereafter removed Cortex from our list of demonstrations.

It took our team two hours to produce something that was frankly not that good – basically just typing text descriptions of data into a web browser – and it was still better than anything the leads had seen because they had nothing to show for all the investment.

In fact, we have been forced to opt out of every sale where the lead has expressed anything beyond the most fleeting curiosity in the use of AI in their business. I don't mean that we've heard that they're interested in AI and elected to drop the contract on moral grounds. I mean that, over the course of the engagement, these people have exhibited a pattern of behavior that has made it near-impossible to sell to them without incurring reputational and legal risk, and are furthermore crafting management environments that I can only describe as cultish, ineffective, and "please dear God, do not let it be on earth as it is on LinkedIn".

## IV. Executives, Game Theory, and The Emperor's Clothes

Despite the substantial prevalence of true believers, many of the people running large AI initiatives, or making public statements about them, do not believe what they are saying. There are "heads of AI" who read this blog, at companies with $1B+ in annually recurring revenue, who have written in to say they believe their job is totally fraudulent but it was the only promotion pathway remaining at the organisation.

On a trip overseas, I had the privilege of a meeting with one of the Fortune 500 executives mentioned at the beginning of the post, who will remain anonymous so that they are not executed by firing squad by their board. As we were chatting, it became clear that they were very switched-on and technically competent, and they also happened to be at a company that had committed to the usual battery of exorbitant claims about their recent innovations. But since I had them there without any microphones around, I asked why this was being repeated without opposition. Was it just sales fluff?

The answer was a lot more interesting. It was partially ridiculous sales material being delivered to an easily excitable audience, but this was not the dominant factor constraining honesty. Executives at their customers were saying absurd things about achieving 100x productivity, and this meant that if any executive at the vendor said that these gains were not plausible, it would undermine the credibility of the customer's executive, be perceived as an attack (or heresy), and possibly result in an enterprise contract cancellation. And getting enterprise contracts cancelled because you wanted to opine on something that doesn't really matter to your organisation's mission is a great way to get fired.

But the best part of the explanation was that the entire thing was an elaborate round-robin: the customer's executive also didn't believe the claims, and was making them because hesitancy would be seen by the vendor's account managers and reported to investors. So the vendor says we've hit 100x productivity, the client says "wow, we're also hitting 100x productivity with you", everyone goes back to their respective boards with reports that business is booming, and no one actually knows whether anything is happening – they just know the game theory says no one can stop.

The end result is not to kill AI, which would still be helpful if we could stop trying to fix everything with it, but just to make people very confused in a world where there is already massive institutional failure. A well-intentioned manager learns of the claims from the market and begins their own initiative, entirely unaware that the claims were baseless. This can only end in tears.

## V. Collective Survival In An Insane World

At the beginning of this post, I mentioned that the bar to prevent this madness is very high – the function of boards and regulators is supposed to be to prevent panics like this from getting out of control. But this is extremely hard to do when the people in charge have no plan, or see no path forwards other than keeping their heads down, which is where we started this post. This is not my voice being dramatic – this is directly quoting the words of the participants. They are terrified of the consequences of speaking up, and in many cases I get the impression that heads of departments who are trying to keep their staff employed have bet on the hype to avoid their department being defunded.

There is a very deep revulsion to the narrative that AI is going to save us all from our burning platform, which I think is rooted in a lot of dormant technology resentment from the pandemic era. In 2020 we said "Zoom calls are amazing!" despite how they isolated and atomised us. We were told AI was going to fix the NHS, when staff are still using pagers and being told they're breaking policy by using WhatsApp groups – AI is not the bottleneck. We're told to be excited about the AI like we were told to make sourdough, like everything that matters can be fixed with a nice little ritual. It is completely understandable that people are sick of it. 

I received a note from a risk analyst, whose entire job is evaluating risks for a living: "I don't feel like people have factored in the reputational risk of making 5% of your work force redundant over AI when you have an AI project that's failing or will fail." This is exactly right. They're risking everything on something that isn't working.

What do we actually do? At scale, I don't know. There's a lot of money flowing into people who have learned to speak the shibboleths, and most of the people I speak to have more immediate concerns than fixing institutions. But on the individual level, it is very simple: stop lying. I don't know what course of action will save your department, nor your job, but it is absolutely clear that lying about what is happening will not work. The AI hype is a collective fiction built on the complicity of a vast network of people who know better.

As always, the most radical act is to tell the truth. If you can do nothing else, at least refuse to add one more brick to the edifice of lies. And if your leadership fires you for it – you were going to be fired anyway when the project inevitably failed. At least this way you get to keep your soul.
