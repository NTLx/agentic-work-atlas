---
type: raw
title: "Agents Prompt People: Using Agents for Long-Horizon Financial Work"
source: "https://latent.space/p/arca/"
author:
  - "Richard MacManus"
published: 2026-10-31
created: 2026-11-05
description: "Latent Space interview with Aman Singh at Arca. User-provided full English timestamped WEBVTT transcript; original attachment sha256 04660196005ff748cd166eed1ef0bba081f2c78a1d0d6f1d94ebe8e166c60dc1."
language: en
tags:
  - clippings
  - agent-harness
  - long-horizon-agents
---

# Agents Prompt People: Using Agents for Long-Horizon Financial Work

Full interview transcript (WEBVTT; user-supplied, preserved with original timestamps and wording). Transcript may contain ASR errors. The canonical article and transcript were cross-checked for topic and identity.

```vtt
WEBVTT

1
00:00:00.100 --> 00:00:10.400
We're actually not a SaaS company. We are, um, we are the firm ourselves. Agents prompt people more than people prompt agents- Mm... and it is a proactive kind of, um, service that is running for them twenty-four seven.

2
00:00:10.420 --> 00:00:20.780
[on-hold music] We're here at the, uh, AI Engineer New York conference, twenty twenty-six. Um, and I'm here with Aman Singh, uh, from Arca.

3
00:00:21.320 --> 00:00:27.520
Um, and, uh, Arca's, uh, recently raised sixty-four million for an AI-native wealth management firm.

4
00:00:28.200 --> 00:00:40.820
Uh, so first of all, Aman, can you tell us a bit about your role at Arca and, um, the financial services you provide and, um, how you're using AI agents to run them? Yeah, for sure. Um, thanks for having me.

5
00:00:41.660 --> 00:00:52.060
Um, my role at Arca is I lead the AI platform team, so we're building the underlying sort of, um, harness and our capabilities to kind of run the business with AI, which is our ultimate goal.

6
00:00:52.760 --> 00:00:59.900
Um, in terms of the services that we provide to our clients, um, we-- This is a broad spectrum of financial services.

7
00:00:59.940 --> 00:01:12.900
So that includes, um, sort of financial advice, financial planning for, um, for their assets, um, and sort of, um, uh, tax planning and insurance and estate planning as, as people get wealthier.

8
00:01:13.360 --> 00:01:22.960
Um, maybe you are, um, someone who just sold a business, for example. Mm-hmm. Um, and there's lots of complexities with all the different partners, et cetera, right? So, uh, we can help you think through that.

9
00:01:23.440 --> 00:01:33.780
Um, we also have clients that are, you know, uh, really large technology executives that, uh- Mm... have, uh, are trying to figure out a real plan for retiring, retiring early, right? Mm-hmm.

10
00:01:33.880 --> 00:01:40.300
Um, and also sm-small families that, um, uh, that are trying to buy their first home, for example. Yeah. Um, yeah.

11
00:01:40.780 --> 00:01:51.380
So the, um, the clients that you have so far, are they, um, do you have to kind of talk them through using agents and, and why you're using agents and tell them a little bit about the technology behind it? Yeah.

12
00:01:51.440 --> 00:02:02.980
So, um, the role of AI at Arca is not to replace the advisor. It is to replace all of the work around the advisor. Mm. So our clients don't really interface with AI directly. Mm.

13
00:02:03.320 --> 00:02:14.040
All they experience is a level of service that has not been, been, um, been possible in this industry before- Mm... delivered through the empathy and care of a human advisor.

14
00:02:14.660 --> 00:02:24.220
Um, so we're building the machinery behind, um, every client- Mm... that's constantly thinking about, um, you know, um, what's, what is the market doing, and how does it impact Richard? Mm.

15
00:02:24.280 --> 00:02:30.360
You know, um, what are, what, what else is going on in your life? Like, what are you-- what are the s-the, the textures of your life that impact your finances?

16
00:02:30.860 --> 00:02:41.600
Um, and, uh, we're able to be way, way more proactive, way more responsive, um, and just deliver a better, um, kind of, uh, level of client service using AI that does all of the, the back office stuff. Okay.

17
00:02:42.040 --> 00:02:52.160
So let's get into the, some of the technical aspects of it. Wh-which models are you using to power your agents and, um, how do you decide which model is best for, for which action? Yeah.

18
00:02:52.480 --> 00:03:05.640
Um, so today we're using, uh, the Frontier, uh, models from, um, from, uh, the Frontier Labs, like Anthropic and, uh, and OpenAI. Mm. Um, Claude is kind of our primary, um, um, model, has been, but- Mm-hmm...

19
00:03:06.380 --> 00:03:11.460
um, we've gone through several iterations of models over the years. Um, we used to be in Gemini way back when- Mm...

20
00:03:11.560 --> 00:03:27.660
um, and then OpenAI and then, and then Anthropic, and what's guiding all of our decisions are, um, our benchmarks that we have internally for, um, all of the various, um, capabilities of our general harness, uh, that it has to express in, in running our business.

21
00:03:28.220 --> 00:03:40.180
Um, and so, uh, just recently, for example, um, despite the external benchmarks claiming, um, great things for Luna, it didn't really quite work out for us as, as well as we had expected. It was way too slow or, um...

22
00:03:40.520 --> 00:03:50.760
And it was costing a lot. Mm. And so, um, our internal benchmarks kind of guide our model decisions, and, uh, as a principle, we, we want to be, um, model-agnostic- Mm...

23
00:03:50.860 --> 00:04:02.080
um, and, and sort of not, um, uh, you know, um, take a dependency on, on a, a certain provider or a certain harness from one of these labs and kind of keep that, that optionality open for us. Okay.

24
00:04:02.500 --> 00:04:13.100
So, uh, you just mentioned, uh, harnesses, so you're using different harnesses depending on which model you're using? No. We have, uh, we have our, our own- Okay... uh, kind of built internally that is mo-model-agnostic.

25
00:04:13.420 --> 00:04:26.480
Okay. Um, so, um, you know, when, when your, when a financial advisor is doing something like a taxation report or something like that, how does the harness decide which model to use? Is that automated? Well, yes.

26
00:04:26.540 --> 00:04:39.620
So we have, um, certain tiers of models based on different complexities of, of tasks. Mm-hmm. So a task like assisting with a tax plan or doing a tax analysis would get our, like, heaviest tier of models. Right.

27
00:04:39.680 --> 00:04:48.440
Inside of that tier, it is a little bit flexible, so you could use, um, so like an Opus tier model or a Sonnet tier model, um, or a, a, a heavy GPT model. Mm.

28
00:04:48.560 --> 00:04:59.720
Um, but, um, based on, uh, there's a lot of, like, background activity that our agents are participating in, right? That is using the, a lower tier of model- Mm... um, based on the complexity of the task.

29
00:05:00.060 --> 00:05:04.900
So that's kind of how we, how we make decisions- Yeah... uh, on, on which model serves which task. Okay.

30
00:05:04.960 --> 00:05:15.620
So is it the, um, uh, the financial advisor that's actually making that decision while they're using the pro-product or- Not really. Mm. Um, they, they're, they're not aware of- Okay... uh, of that happening.

31
00:05:15.680 --> 00:05:25.020
We've abstracted this away- Okay... uh, from them entirely. They kind of just interact with our product, um, as they would. Mm. Um, and those decisions are made in-internally, uh, by us. Okay.

32
00:05:25.800 --> 00:05:31.660
So, um, in your presentation at, at the conference earlier today, you talked about a tax bill, uh, example.

33
00:05:32.280 --> 00:05:45.180
Uh, I just wondered if you could maybe walk us through, uh, an example of adjusting a client's, uh, portfolio, investment portfolio, um, you know, from identifying a need to maybe rebalance the portfolio to executing trades.

34
00:05:45.500 --> 00:05:58.220
Can you talk us through, you know, what, what parts of that process the agent does and, and what parts the human advisor does? Right. Um, so just like in the talk, this is a thing that will span ten days.

35
00:05:58.900 --> 00:06:07.420
Um, and so agents are ultimately, um, responsible for delivering that outcome. But there are, are, are certain parts that they do and certain parts that they do not. Mm.

36
00:06:07.460 --> 00:06:21.680
So in this example, um, when, uh, when the client emails us, uh, with this whole tax bill, th-there's a, there's a piece of the analysis of like, where is this client's money allocated today, and what is the most optimal way, um, to liquidate some of that to, to produce a hundred thousand dollars?

37
00:06:21.820 --> 00:06:32.496
Mm. That is best suited for agents. Right To take on as an analysis task Yeah So that they do exactly that Do they have certain limits though? That they can't, you know, they can't execute a trade at- Correct...

38
00:06:32.636 --> 00:06:41.936
X amount? Yeah. So the analysis part is fully automated, but, um, they're unable to actually execute, uh, any sort of money movement or liquidation automatically. Mm-hmm.

39
00:06:41.976 --> 00:06:47.816
We have a very deep integration with our custodian, uh, that actually gives us APIs to be able to do that. Mm.

40
00:06:47.916 --> 00:06:58.596
Um, but we have strict guardrails around human in the loop for things that would either move money or liquidate assets, or even directly communicate with our, with our end clients, uh- Mm...

41
00:06:58.636 --> 00:07:08.096
because there's a level of service that, that, uh, service, service, and quality that we expect. Um, so all of the like internal analysis will be done by agents, but the, the...

42
00:07:08.416 --> 00:07:13.256
They will also pull in the right person to be able to execute the trade when needed. Mm.

43
00:07:13.396 --> 00:07:20.116
And they'll pr- give a, give the person a plan that they, they're able to review and kind of like adjust, um, and yeah, go from there. Yeah.

44
00:07:21.096 --> 00:07:30.376
Yeah, so you mentioned that, um, uh, these processes tend to be, you know, 10 days or at least l- longer sort of, uh, running time than most sort of agent stuff these days. Mm.

45
00:07:30.836 --> 00:07:42.656
So, um, when an agent kind of resumes a task, maybe days later than they, you know, than they started it, how do you restore, how do you check that the plan still fits the client's, uh- Mm-hmm... you know, uh, needs?

46
00:07:42.896 --> 00:07:50.536
Yeah. Um, so this is an interesting, interesting one to think about, is we have tons of these signals like I described in the talk. Mm.

47
00:07:50.676 --> 00:07:57.936
Um, some are, for example, you can imagine there's an email thread that is receiving responses, and there's chatter happening, right? Mm.

48
00:07:57.976 --> 00:08:06.636
You can imagine that, that any ad- ad- additional response to that goes to the same agent that's kind of like reading that, that email thread and reacting to it, right? Mm-hmm. Mm.

49
00:08:06.676 --> 00:08:16.276
But a, a fresh signal of, like a, like a phone call that was made in the middle, um, that is a brand-new signal that isn't attached with any other ongoing process. Yes.

50
00:08:16.296 --> 00:08:25.656
And so there's like a fresh agent that wakes up to figure out what this means, right? Mm. And the way they, way they understand what is happening right now is our internal memory systems. Mm.

51
00:08:25.756 --> 00:08:38.516
So we have, um, we have this, this persistence of, for every client, um, what is happening right now? What are we trying to service? Who owns what? Mm. What has happened so far? Mm. What are we tracking for next, right?

52
00:08:38.556 --> 00:08:45.956
What, what needs to happen immediately in the next couple of days? Mm. What are we tracking for the long term, right? Mm. Which individual is responsible for which action?

53
00:08:46.336 --> 00:08:51.336
All of this is being tracked by our memory systems- Mm-hmm... that our agents contribute to.

54
00:08:51.836 --> 00:08:59.096
But also, there is a, a kind of really sort of dreaming process that reflects on the state of the world as it relates to Richard, the client- Mm-hmm...

55
00:08:59.596 --> 00:09:04.596
um, and is able to kind of like update these memory systems to, to persist long-horizon kinda tasks. Mm.

56
00:09:04.656 --> 00:09:15.216
So that agent that received a new signal quickly ramps up on what, uh, the situation is with the client, and it'll know, "Okay, we're, we're actually executing a big tax bill." Um- Mm...

57
00:09:15.256 --> 00:09:21.796
and we'll be able to see, okay, my signal relates to that tax bill- Mm... so let me kind of contribute to the, to, to the state of that world. Mm.

58
00:09:22.556 --> 00:09:32.536
Can you talk a little bit about the, the safety sort of aspects that you've maybe built into your product or harness to, to, to make sure obviously that, uh, no money is lost along the way? Yeah.

59
00:09:33.036 --> 00:09:40.596
Um, so all of our safety restrictions are, are fully deterministic, and they, they take the decision-making off the, the agent's hands.

60
00:09:41.036 --> 00:09:49.936
So for example, um, certain tools let the, let the agent kind of execute the tool itself. So if it's like a simple record-keeping kind of tool- Mm... um, it will execute it.

61
00:09:50.316 --> 00:10:05.176
We also, with every time a tool is called that writes data, we have, um, a LLM-based verification running on, uh, on that action. Um, these like fast, uh, LLM calls that, that analyze every single write to our database.

62
00:10:05.656 --> 00:10:15.756
Um- Mm... so that's another layer of verification we're running. And then, uh, we also ingest a lot of like external information, so there's emails coming in, documents coming in, phone calls being made- Mm...

63
00:10:15.816 --> 00:10:26.416
which are targets for prompt injection. So we run, um, sort of verifications at the, at, at the edges that detect presence of certain, um, you know, flavors of prompt injection. Mm.

64
00:10:26.436 --> 00:10:38.296
And then anytime there is a, um, there is a case where, uh, data leaves our system, for example, in like a, a web search in, in the most obvious case, but also if we're sending a calendar invite to Richard, right? Mm.

65
00:10:38.316 --> 00:10:46.096
That's an external kind of, uh, data where we have both deterministic checks on presence of certain information that we know is PII- Mm...

66
00:10:46.176 --> 00:10:52.556
uh, but also a consensus of small models that, that ensure that there isn't any kind of data exfil being attempted. Mm.

67
00:10:52.676 --> 00:11:02.396
Um, so we have tons of different, different kind of guardrails built into the harness, uh, with the principle that we wanna kind of contain them at the edges of capability- Right... uh, and not earlier than that. Yes.

68
00:11:02.996 --> 00:11:17.996
And, and because you're in the financial, uh, you know, industry, are there certain kind of regulations that, uh, are required that you have to sort of keep to in terms of the technology that you're using, or is that, is it just more about outcomes and, and the way you sort of deal with clients?

69
00:11:18.176 --> 00:11:31.936
Yeah. The, the industry cares about outcomes, but, um, compliance cares about auditability. Right. Right? Um, and so, um, our, um, our system is, is, is such that auditability is by default. Mm-hmm. Um, we have

70
00:11:32.936 --> 00:11:45.796
every single action that, that an agent takes produces a change log of what changed- Mm... um, who changed it, from which part of the system, and when. Mm. And this applies not just to agents, by the way.

71
00:11:45.836 --> 00:11:52.476
It applies to human actors as well. Mm. So if you change something in the UI that affects a client, uh, we'll log that action.

72
00:11:52.856 --> 00:12:02.136
So it lets us both get auditability by default, but also power some of our agentic capabilities, where the same thing that, that would tracks like a UI change- Mm...

73
00:12:02.256 --> 00:12:05.756
also could be used to, like, inform the agent that that happened. Right.

74
00:12:05.876 --> 00:12:14.936
Um, so auditability has been a big part of our, um, our story, both for obviously compliance and regulation, uh, but also for our, um, a- agentic loop. Yes.

75
00:12:15.716 --> 00:12:26.276
In your, uh, presentation, uh, you had a nice line, "Agents prompt people more than people prompt agents." Um, so how do the agents decide who to involve and, um, you know-

76
00:12:27.216 --> 00:12:35.616
What sort of, how much of the context that they need to provide that person in order to do what they need to do? Yeah. Um, another int- interesting one.

77
00:12:35.676 --> 00:12:45.876
So, um, this is similar to how humans work in, in, in, uh, in our industry- Mm... is there is a process that we're tracking over 10 days. There's multiple actors involved.

78
00:12:46.476 --> 00:12:52.856
The, the actor at step seven may not need to know about this just yet, right? They're pulled in at the right time. Mm.

79
00:12:53.176 --> 00:13:08.456
And so our agents with our kind of like long memory persistence plus the daily reflection on what is happening, um, reflect on where the, the state of the world is at the moment, and they're able to pull in the right person at that time- Mm...

80
00:13:08.476 --> 00:13:13.476
when it is, when, when there's a signal that, that implies that, that person must be pulled in. Mm.

81
00:13:13.516 --> 00:13:26.476
And all of this is, um, work that we have done to operationalize the context of how this industry works, but not just that, but how does Arca want it to work, and what are our principles of, of how work happens in this industry.

82
00:13:26.836 --> 00:13:36.996
Mm. Um, and that is another advantage of us being sort of a- a, um, a not just a SaaS company. We're actually not a SaaS company. We are, um, we are the firm ourselves. Mm.

83
00:13:37.036 --> 00:13:45.096
So we can standardize the way this work even happens- Mm... um, so that our agents can participate in standard ways that, um, that work must happen. Mm.

84
00:13:45.976 --> 00:13:57.056
So, um, early in the conference, uh, Anthropic, uh, did a workshop about their managed agents', uh, infrastructure, and a lot of it, uh, even the orchestration is becoming more automated now.

85
00:13:57.576 --> 00:14:05.196
So do you foresee kind of using that type of functionality? 'Cause o- obviously it presents a danger in that the human is not necessarily always in the loop anymore.

86
00:14:05.636 --> 00:14:17.616
So, uh, d- have you had any thoughts about using that technology to automate even more of the process? Um, I think we are very bullish on the models from, uh, from Anthropic and, and labs like OpenAI- Mm...

87
00:14:17.896 --> 00:14:31.496
um, but less so on, on taking a dependency on a product like managed agents. Mm. Um, because managed agents, one of their, their key things is how the models kind of persist and, and contribute memory- Mm...

88
00:14:31.636 --> 00:14:38.196
as to what is happening in the world, um, and all the operational knowledge that they need to be, uh, need to use to, to be successful. Yes.

89
00:14:38.296 --> 00:14:53.016
Um, and so letting them own that part of the business is kind of like, um, a, a risk because, um, owning that is... Owning your intelligence is kind of, uh, gives you the ability to impact the business. Mm.

90
00:14:53.136 --> 00:15:06.336
If you, if you hand off, uh, the intelligence to, to another provider, you lose some of that control that you need to kind of, like, build something that is unique and tailored to your business to such a deg- great degree, um, that it can actually impact your business.

91
00:15:06.576 --> 00:15:15.116
Mm. And just on Anthropic, they'll, they've also recently released, uh, financial services, so they're partnering with a whole bunch of different firms. Mm-hmm.

92
00:15:15.156 --> 00:15:20.396
Do you think what they're doing is kind of competitive to what you're trying to do, or do you see them as different things? Yeah.

93
00:15:20.476 --> 00:15:26.016
I think, uh, I think Anthropic getting into our kind of industry is, is very validating for, for our industry.

94
00:15:26.516 --> 00:15:37.476
Uh, but the way I think about it is that it is very different to be an, um, a, a services firm that has access to AI tools- Mm... versus a firm that was built to be AI native. Mm-hmm.

95
00:15:37.836 --> 00:15:46.336
The firm with AI tools requires their users to prompt the us- the, the agents kind of to, to produce work or to do work. Mm.

96
00:15:46.436 --> 00:15:51.976
Um, but here, like I said, in, at Arca, agents prompt people more than people prompt agents- Mm...

97
00:15:52.016 --> 00:16:04.176
and it is a proactive kind of, um, service that is running for them twenty-four/seven, and it's kind of like running the business in the most standard way that we, that we expect at the level of service that we, that we, uh, that we aspire to- Mm...

98
00:16:04.456 --> 00:16:14.176
uh, which looks very different if you're, if you're, um, a, an AI, AI... Sorry, uh, a company with AI tools. Yes. Yes. Okay. Um, so a little bit more about on the security side.

99
00:16:14.236 --> 00:16:27.576
So can you explain, like, what, uh, in your processes runs inside a sandbox, and, um, how do you verify, like, a change to a financial plan, uh, you know, before anyone acts on it? Um... Mm. Yeah.

100
00:16:27.596 --> 00:16:41.936
[clears throat] So, um, the s- the, the way we use sandboxes is that the, the sandbox is one component of our harness. Mm. Our agent isn't actually inside of the sandbox. Mm. It uses the sandbox to offload computation.

101
00:16:42.116 --> 00:16:50.096
Mm. Um, and, uh, we've, we've built systems to make it safe for code inside of that sandbox to access our data. Mm.

102
00:16:50.536 --> 00:17:02.096
Um, so we kind of like have this thing which translates the code it wrote into a strict format that we expect, throw away the code, and you, um, kinda instill guardrails on that format before it reaches your back end.

103
00:17:02.336 --> 00:17:14.056
Right. Um, so we allow the agents kind of to use, uh, code to query our data, which means that they can, like, aggregate it, they can munge it, they can kind of like work with it as they, as they see fit- Mm...

104
00:17:14.116 --> 00:17:26.656
to produce such a thing like a, like a financial plan. Um, inside of the same sandbox, they produce this, you know, beautiful artifact that we, we can share with clients that has like... it's a PDF of like- Mm...

105
00:17:26.656 --> 00:17:36.236
"Here's your financial plan, and here's how we're do- planning to kind of like approach your life financially." Um, and once that is produced is where we run our verifiers.

106
00:17:36.676 --> 00:17:41.156
So, um, it's a certain type of artifact that is produced from the sandbox. Yep.

107
00:17:41.196 --> 00:17:51.096
The moment that it's produced, we run bunch of different, different verifications on it, um, some deterministic that check for presence of like, "Hey, did you just put like a raw account number in there?

108
00:17:51.456 --> 00:18:00.396
You should not do that." Mm. Mm. Um, so deterministically we can check that, um, but also, um, fast models like, um, like the, the smaller models or JEV- Mm...

109
00:18:00.596 --> 00:18:12.276
um, to analyze for presence of things that might make this artifact non-compliant. Like for example, you really should not be like, um, promising returns, uh, in, in that artifact. Mm.

110
00:18:12.316 --> 00:18:17.136
So that's another thing that we will check before it is, um, it is kind of publishable. Mm.

111
00:18:17.236 --> 00:18:34.276
Um, and the last thing I'll say on that is that, um, doing this is actually, um, makes our kind of compliance, uh, better than if humans were doing it because AI is- tireless at, at, at finding even the smallest mention of a non-compliant, um, uh, piece of writing in there.

112
00:18:34.476 --> 00:18:42.456
Yeah. Um, so yeah, we'll continue to invest in, in, in more of that and kind of like- Mm... constrain at the capability edges. Yes. Yeah, you, uh, mentioned Jev there.

113
00:18:42.536 --> 00:18:51.296
Um, so y- you've started to use decision models, uh, as part- Mm-hmm... of your process. Uh, uh, what other, um, products, other than Jev, are you sort of looking at? Yeah.

114
00:18:51.376 --> 00:19:00.276
So what we've noticed is, um, when, when models are, um, working with financial data, right? When they're answering questions that require financial knowledge- Mm...

115
00:19:00.456 --> 00:19:11.396
they are-- they're very confident in, in, uh, in the knowledge that they have. So a small example is that, uh, models will very happily use the tax brackets from twenty twenty-five- Mm...

116
00:19:11.676 --> 00:19:16.956
um, to, to come up with an analysis and be like, "All right, that is it." Um, but that is, that is obviously incorrect.

117
00:19:16.976 --> 00:19:30.356
And so, um, that is one of the ways in which we're using decision models in, in our harness is to, to check when the, the model is about to make a financial recommendation or, or anything, any action that requires financial rigor- Mm...

118
00:19:30.456 --> 00:19:41.036
will detect and will nudge the model to kind of use our knowledge base of verified facts about the world that is true today. Mm. And/or use their kind of web search. Yes. So it kind of makes it, um...

119
00:19:41.396 --> 00:19:51.196
This is kind of a, a, a point about the, the harness and, and owning the harness that lets you do things like this that, that help your, um, your models be, be accurate where it matters.

120
00:19:51.896 --> 00:20:02.796
And do you use, um, decision models in, for example, recovery if, like, a trade fails to execute? Is there a decision model involved there, or is there another path to, to get the agent back on track? No, not today.

121
00:20:02.836 --> 00:20:13.196
That is not a use case that we're exploring today. Okay. Um, so, um, you know, if, if a step, a trade does fail, for example, how does the agent recover at, at the moment in your process?

122
00:20:13.236 --> 00:20:24.976
So, um, so at the moment, we are not doing autonomous trading with, with agents. Okay. It is very much a, um... The agents will propose that we, we make trades. I see. Um- Yep...

123
00:20:25.516 --> 00:20:31.896
and it is fully up to kind of our, our experts to figure out if that is the right trade to be making- Right... and to execute the trade. Okay.

124
00:20:33.156 --> 00:20:43.296
So, uh, on the, on the same sort of, uh, line of that, um, your slides, um, say that every staff edit or cancellation comes with a why and come-- it becomes an eval.

125
00:20:43.856 --> 00:20:56.916
So, um, how does that feedback, uh, get turned back into, uh, the system as a measurable improvement? Yeah. Um, that is another one of the advantages of us, um, being the business and not a SaaS company- Mm-hmm...

126
00:20:56.996 --> 00:21:01.676
um, is that we have, um, we have the ability to have to require them to give us feedback.

127
00:21:02.256 --> 00:21:12.556
Um, and yeah, the way that we loop the feedback back into improvements is something that you would, um, you would expect is all of that feedback gets piped into, um, a data store- Mm-hmm...

128
00:21:12.676 --> 00:21:18.016
that, um, that couples that feedback with the trace of the agent that produced it. Yeah.

129
00:21:18.116 --> 00:21:30.576
Um, and so we're able to kind of like take that, take, take that trace, um, put it, put it next to the, the feedback, and every night, we run this process where we take-- collect traces from, uh, the real world- Mm...

130
00:21:30.596 --> 00:21:36.776
from our agents in the wild, and run, run a meta agent on top that suggests changes to our harness. Mm.

131
00:21:36.956 --> 00:21:44.436
So maybe tools that were mis-misleading or, um, things that were, were errored, or there's missing knowledge in our knowledge base. Mm-hmm.

132
00:21:44.536 --> 00:21:48.336
Um, and they'll surface this information to us, and then we'll, we'll be able to kind of, uh, improve it.

133
00:21:48.816 --> 00:21:56.036
Um, today, we still have a, a human in, in, like a human engineer in the loop before we actually ship a prompt change. Yes.

134
00:21:56.136 --> 00:22:06.176
Um, I've noticed that, uh, that agents will, will make really nasty prompt changes if you leave them, leave them to it. Um- Mm... every little fix becomes the whole prompt. Mm.

135
00:22:06.276 --> 00:22:12.516
Uh, and they're, they're unable to stay meta and kind of generalize, uh, the fix into, into a prompt that generalizes. Mm-hmm.

136
00:22:12.616 --> 00:22:22.036
Um, so but yeah, we have, we have, uh, feedback loops from our product that we collect directly as first-class product features- Yep... to collect evals into, into improvements. Hmm. Okay.

137
00:22:22.596 --> 00:22:40.176
Um, and you also mentioned in your presentation about, uh, turning knowledge of how a firm works into agent context, which is actually something a lot of, uh, forward deployed engineers, uh, do- try to do is, is turn an organization's kind of internal knowledge into, uh, actionable things for agents.

138
00:22:40.216 --> 00:22:46.895
Mm-hmm. Um, what does that look like, uh, for your company technically, and, and how do you sort of keep it up to date? Yeah.

139
00:22:47.335 --> 00:23:02.096
So we have, um, a knowledge base of, um, of files that rep-- is represented as, as, um, as files. And, um, the way we keep that up to date is we- we've handed it to our experts to curate and update. Mm.

140
00:23:02.236 --> 00:23:12.376
So it is a, a first-class, um, feature in our product. Uh, so on the left-hand side, there's a tab called Knowledge- Mm... which has the full, uh, operational context that our agents are using.

141
00:23:12.956 --> 00:23:25.016
Um, and as they, they work on, um, uh, work on things, uh, they're able to cite knowledge, and so it kind of like creates this, this loop of like, "Oh, we noticed that the knowledge is incorrect."

142
00:23:25.656 --> 00:23:38.236
Um, and, um, we-- that gets surfaced to us in our trace analyses. Mm-hmm. And because it is a, a part of the product itself, uh, people are able to go in and, like, edit the, edit the scale, um, uh, directly. Okay.

143
00:23:38.276 --> 00:23:40.496
Um, that's how it kind of works. All right. Okay.

144
00:23:41.276 --> 00:23:52.936
So, um, you know, you mentioned you're, um, uh, uh, you're actually offering these services to, to clients through, you know, uh, I presume you have a staff of, um, financial advisors in your firm.

145
00:23:53.236 --> 00:24:12.356
So, um, can you maybe give us an example of, uh, uh, some, you know, a client that you've had that's had a measurable improvement in their investments or taxation or whatever through the agent system and, and maybe some sort of details about what in the agent architecture kind of helped that client, you know, get such a good return?

146
00:24:12.856 --> 00:24:22.516
Yeah. I'll give you a recent example. Um, this is, um, this person wasn't a client yet. Mm. Um, but they were, they were at the, the point of becoming a client.

147
00:24:22.596 --> 00:24:33.816
So we had all of their, uh, their documents, their statements, their current investments, et cetera. Mm. And this person was already working with an advisor. Um, and so, um, they meet with us.

148
00:24:33.996 --> 00:24:45.616
They tell us that, "Hey, I have this advisor already. They're charging me fifteen hundred dollars, um, uh, for, for their services." Mm. Um, "And, uh, they're not very responsive to me, so I'm, I'm chatting with you."

149
00:24:46.076 --> 00:24:55.516
And so, um, our agents have kind of like, um, you know, read through all of those documents. They've analyzed them. They've analyzed what the person's goals are that they state, right? Yep.

150
00:24:55.596 --> 00:25:00.636
Um, they've also analyzed the statement of, like, who this current advisor is, uh, right? And how much they're, they're charging them.

151
00:25:01.176 --> 00:25:19.676
And, um, they discover that, that there is-- there are fees that this person was charging them that they weren't aware of, uh, and surfaces it, it to them, um, and kind of like makes them not only aware of, um, of the fact that they're being overcharged, but also aware that that person wasn't even fiduciary.

152
00:25:20.056 --> 00:25:33.116
Mm. Um, so they're not fu-- um, obligated to act in their interests. Mm. So it is-- this is the sort of, like, attention to detail that our agents bring about in, in-- when they're analyzing a financial picture- Mm...

153
00:25:33.276 --> 00:25:38.816
um, that, that sort of, um, would not have been possi-possible if we didn't have, um, have these.

154
00:25:39.236 --> 00:25:51.056
There's several examples of, um, proactivity, uh, that our agents kind of like produce of, like, someone has a deadline coming up. Mm. Or they're at risk of missing their RMD or, um, that kind of thing.

155
00:25:51.076 --> 00:26:02.596
And so, um, this is difficult at scale for humans to keep track of, but it is the, the default behavior of, uh, of our agents at, at Orka. Yeah. Wonderful. Well, that's probably a good, uh, uh, point to stop it.

156
00:26:02.656 --> 00:26:05.356
So thank you very much, Iman, for joining us- Thank you for having me... on Out in Space.
```