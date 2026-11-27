---
type: raw
title: "How Clay Builds GTM Agents — Jeff Barg, Head of AI"
source: "https://lspace.beehiiv.com/podcast/s/latent_space_the_ai_engineer_podcast/how_clay_builds_gtm_agents_jeff_barg_head_of_ai"
published: 2026-11-26
created: 2026-11-27
language: en
tags:
  - agentic-engineering
  - product-management
  - clippings
---

# How Clay Builds GTM Agents — Jeff Barg, Head of AI

用户提供的完整 SRT 字幕；原始附件 SHA-256: 5e6d2453e61c09e3c9ee343a717ab7a6f83221c1dec441fb0c460151cf3e466d，111983 字节，524 个字幕块，00:00:00.560–01:12:23.372。以下保留原始字幕编号、时间轴与转写文字（未纠正自动转写专名）；标题和来源日期以官方节目页为准。

1
00:00:00,560 --> 00:00:07,800
We have a, a company data set of 40 million companies. You can imagine just asking a question like, "Is this customer a good fit for my product or service?"

2
00:00:08,039 --> 00:00:17,680
And you could run that across every company in the world, and it comes out to, I think, around 1,500 bucks. Our users hate our model selector. I think most, most customers, like, don't wanna see it.

3
00:00:17,820 --> 00:00:27,340
Like, they're upset when they see it. We explicitly don't want our agent to be markedly better than just using Clay and CloudCode. We were doing some analysis on just how many YC companies are using Clay.

4
00:00:27,620 --> 00:00:34,160
We just asked our agent for this, and it found it in, like, 60 seconds. I was just thinking, like, a year ago, this would've taken so much time.

5
00:00:34,440 --> 00:00:42,740
From looking through so many agent traces, one, like, the models are still kind of dumb. Trying CLI commands with the same inputs over and over again and just not correcting them.

6
00:00:43,040 --> 00:00:51,900
We were one of the launch partners for ChatGPT apps, probably 25% of the engineering team for a month. I think two days before we were supposed to launch, they were like, "We're gonna postpone this indefinitely."

7
00:00:51,900 --> 00:01:06,280
[upbeat music] We have Jeff Bard here from Clay. Um, you are the head of AI. Could you maybe introduce yourself and the business? Yeah, absolutely. Well, first, thanks- thanks for having me. So yeah, I'm, I'm Jeff.

8
00:01:06,580 --> 00:01:12,140
Uh, I've been at Clay for about two years, and Clay, we like to think of ourselves as a creative tool for growth.

9
00:01:12,680 --> 00:01:22,660
And so really what that means is we help people build lists of companies and contacts, [graphics beeping] um, for the purpose of prospecting or getting customers or finding, you know, new and great customers for their business.

10
00:01:23,220 --> 00:01:37,680
Um, so we help qualify those lists using agents and other data providers to basically, you know, add data points like the amount of revenue or funding they've gotten, or who their CEO is, or different locations that they have, and use that to basically filter down to figure out who their best customers, um- Yeah...

11
00:01:37,720 --> 00:01:43,040
who their best customers are. Uh, for those watching on YouTube, you are actually really identified with this spreadsheet for some reason. [chuckles] Yes.

12
00:01:43,080 --> 00:01:52,120
When I talk about, when I talk about, like, the spreadsheet form factor with other AI builders, they usually point to Clay as the, the, the success example. Yes. Uh, and yeah, it's, it's funny.

13
00:01:52,160 --> 00:02:00,920
I mean, Clay started seven years ago, really as a low-code tool in the spreadsheet, so it makes a lot of sense. Uh, you know, we've been around for a while and really have built up on, on that spreadsheet. Yeah.

14
00:02:01,240 --> 00:02:07,780
Uh, and then I- I'll also identify, you said you was, it's a creative something. Yeah. There's nothing, nothing creative here. It says, "Build systems to grow revenue."

15
00:02:07,800 --> 00:02:11,680
[chuckles] That, that sounds a lot more like, yeah, like, "Let's make money, guys." No, your guys are just so creative.

16
00:02:12,000 --> 00:02:20,860
Yeah, actually, like, let's give us, give us a set two, uh, seconds on, like, why, why are you guys always so cheery and, uh, no- noticeable? Like- Yeah... like, Clay's branding is, like, really on point.

17
00:02:21,280 --> 00:02:32,560
Well, I do think it's, it's a core part of the thesis, um, that go-to-market really is a creative endeavor, and I- I don't know. I think, like, actually none of our competitors really seem to believe that- Try. Yeah...

18
00:02:32,580 --> 00:02:36,560
or, or try to do that, and I think it just, um, you know, adds to the ethos.

19
00:02:36,620 --> 00:02:45,360
It's like, I think it, it helps us build, you know, this community of people who, I don't know, try really cool and creative stuff to grow their companies. So. Did you guys- Yeah... start that way, by the way?

20
00:02:45,500 --> 00:02:55,800
Like, the business was always this? I think we've always spent a lot of time thinking about brand and how, you know, we, we present. Um, but no, like, we, we, we really narrowed in on go-to-market.

21
00:02:55,860 --> 00:03:04,780
Um, this is before I joined the company, but I think around three years ago, we really focused in on... We were deciding, like, "Oh, should we focus on recruiting or should we focus on go-to-market?"

22
00:03:05,300 --> 00:03:14,720
Focused on go-to-market, and then, you know, really doubled down there. Yeah. What was the reason for that? Just like a thesis? Um- There's this, like, little nice history chart. Uh, I don't know what this place, but...

23
00:03:15,200 --> 00:03:24,380
Yeah. [laughs] Yeah. Yeah, I mean, I, I don't know. I mean, there was probably a, a lot of evolution in the, in the five years that, that this started. But- Yeah...

24
00:03:24,720 --> 00:03:36,820
um, you know, we really started with a bunch of different kind of ways to think about the company or think about the business, but it started very horizontal, and then I think we just really l- wanted to focus in on kind of a singular persona.

25
00:03:37,400 --> 00:03:41,380
Um, and that helped us sort of build the things that ended up, you know, really making Clay successful. Cool.

26
00:03:41,860 --> 00:03:49,420
I think, you know, the thing that a lot of people tell me about Clay, uh, is that there's a lot of parallels with how I grew LaneSpace and AIE- Mm...

27
00:03:49,480 --> 00:03:59,720
because I identified this sort of segment of the market called, that I called the AI engineer, and I really focused on serving them, and you guys are basically synonymous with the GTM engineer now.

28
00:04:00,140 --> 00:04:09,680
Can you describe what that is? You know, I think this is one of the reasons why it's interesting for Basil and I to be on this pod because Basil is f- focusing on the FDE. You guys are on the GTME, and I'm on the AIE.

29
00:04:10,380 --> 00:04:24,220
You know, we really branded this term the good market engineer, and the idea was just, um, companies in, let's say, the 2010s really spent a lot of time trying to build pipeline or trying to, you know, grow their companies through just throwing more people at the problem.

30
00:04:24,760 --> 00:04:26,680
You can probably just engineer a lot of these problems.

31
00:04:26,720 --> 00:04:44,700
Like, you can probably actually build systems to find customers for you, and I think this kind of coincided with LLMs and, you know, the post-Cha- ChatGPT era where you could actually have agents go and crawl the web or, you know, qualify customers and basically exert judgment, um, for finding potential customers in a scale that way.

32
00:04:44,920 --> 00:04:57,140
And so, you know, you kinda have this confluence of things where you had these new systems that could effectively qualify or, you know, score accounts for you and just kind of a continued trend towards automation in the space.

33
00:04:57,160 --> 00:05:06,300
And we were seeing more people basically engineering go-to-market systems and tried to, you know, brand that term around it. And what was the role of a person doing that before?

34
00:05:06,740 --> 00:05:10,700
I'm sure people have tried to do this for a long time. Yeah. But I, I think it's sort of...

35
00:05:10,900 --> 00:05:19,760
You know, if you were to think about the different disciplines that go into go-to-market engineering, it's probably some agent engineering to figure out how to write the best prompts to actually qualify something, right?

36
00:05:19,800 --> 00:05:26,600
So it's actually, you know, understanding LLM systems. There's probably some data engineering in there, right? Like, you're actually building a bunch of lists.

37
00:05:26,680 --> 00:05:34,540
You're transforming them, you're enriching them, you're filtering down and building different views on top of that, and there's sort of just regular software engineering built in there too, right?

38
00:05:34,580 --> 00:05:45,820
Like, you're, I don't know, actually orchestrating systems that when someone fills out a get in touch form on your website, probably research that company and then maybe, like, send it to a rep or send it to an outbound campaign, right?

39
00:05:45,880 --> 00:05:55,720
All these sort of things that are kind of just traditional software engineering. Yeah, I think the old school name for this might be marketing engineer ops person. I may even heard of it.

40
00:05:55,840 --> 00:06:03,980
Software engineer might be a part of it, but a, a growth engineer might as well be a part of it, but growth maybe is more focused on marketing and yours is more sales, right? Yeah.

41
00:06:04,400 --> 00:06:13,496
I, I think probably, like- This function would have fallen into revenue operations. Like, that's probably the bucket of things, and still today we sell into reven-revenue operations teams.

42
00:06:13,996 --> 00:06:21,616
But yeah, I think it's, it's somewhat distinct as a discipline. Like, I'd say it's, it's pretty new. What kinds of backgrounds do successful go-to-market engineers tend to have?

43
00:06:22,276 --> 00:06:32,476
Oh, man, it's pretty, uh, it's pretty across the board. Uh, I think we've seen a lot of actually, a lot of traditional software engineers move into the role, and so that's been pretty interesting to see.

44
00:06:32,536 --> 00:06:43,156
It's, like, actually just people approaching the problem from, like, very kind of first principle software engineering, uh, standpoints. Um, definitely, like, ambitious rev ops folks have grown into the role as well.

45
00:06:43,376 --> 00:06:46,016
So we've kind of seen, like, all different directions of people move into it.

46
00:06:46,376 --> 00:07:03,936
Yeah, I think, uh, you know, one of the things that people who have never done this job before don't really appreciate is that basically there is a lot of data mining and entity resolution and a little bit of knowledge graphs, maybe you can talk about that, uh, just to get all this kind of lists for people just for prospecting.

47
00:07:04,256 --> 00:07:10,556
Yeah. Um, I'm not sure, like, uh, I think there's probably other use case other than prospecting. Obviously, a list is a very powerful thing.

48
00:07:11,156 --> 00:07:19,376
That actually combines a lot of information, like multiple tens of billions of dollar companies are created just as a database that feeds into Clay, right?

49
00:07:19,576 --> 00:07:28,636
Uh, so like, m-my canonical example is like ZoomInfo, like, or RocketReach. Like, you've, you've heard of all these things where you need enrichment from, like, I have an email. That's all I have.

50
00:07:29,076 --> 00:07:36,776
To, like, okay, what company do they work at? What size, what size is that company? Like, are they the buyer? Did they just move companies? Like, I don't know what other details are relevant there.

51
00:07:36,796 --> 00:07:45,376
[laughs] You know, definitely Clay, where, where Clay sits in the market, we work with a bunch of different data providers and, and partners, so- How many? Um, I, I don't have the latest number- Hundreds of them?...

52
00:07:45,396 --> 00:07:50,596
but, you know, in, in the hundreds- Yeah... uh, in, in the hundreds for sure. And it's really flexible as a platform.

53
00:07:50,656 --> 00:08:01,536
Like, if I think about kind of, again, back to, like, other competitors or different people tr- who have tried to build sales tools in the past, um, I think a lot of people try to build point solutions, and Clay is, like, really generic, right?

54
00:08:01,596 --> 00:08:10,656
Like, to your point, you can build a lot of stuff with lists, and we've seen people build crazy things in Clay, and that's intentional, right? And it comes with a bunch of trade-offs.

55
00:08:10,956 --> 00:08:15,976
I think it's being very flexible means there's a lot of ways that you can make mistakes. Mm.

56
00:08:15,976 --> 00:08:21,316
There's a lot of different ways [laughs] that you can, you know, build systems that, that don't work as you'd expect, but it, it becomes really powerful.

57
00:08:21,956 --> 00:08:30,976
Can we take a step back to when you started Avenue, and then maybe, like, how that led you to joining Clay? So yeah, could you describe Avenue a little bit?

58
00:08:31,456 --> 00:08:40,636
So I, I joined Clay through the acquisition of my previous company, uh, Avenue- Yeah... um, which is a company I co-founded with a friend of mine from high school in- We'll have it up on screen. Yeah.

59
00:08:40,916 --> 00:08:50,656
The, the website's still up. Yeah, so, so Avenue was a company, uh, we started in, uh, I think early 2020. And Avenue, we... Yeah, so I, I built this with a friend of mine from high school.

60
00:08:50,696 --> 00:08:59,956
We actually had been building apps together back in middle school and high school, so we had one of the first 500 iPad apps on the iPad store back in the day, and- Nice... so we'd always been kinda tinkering on ideas.

61
00:09:00,456 --> 00:09:20,896
And we, my co-founder had worked at Uber, I worked at Amazon out of school, and we'd both wanted to start something together, and both kind of had the idea of, hey, we're kind of working on different types of ops problems in very different domains, um, but kinda makes sense that actually these marketplace operations teams actually need observability solutions like engineering would.

62
00:09:21,296 --> 00:09:29,156
So almost like I'd say the through line even to Clay is there were a lot of kind of, you know, engineering best principles that we were trying to build to oper- uh, bring to operations teams.

63
00:09:29,616 --> 00:09:40,416
And, um, but yeah, so we, we worked on this for about four and a half years. We went through YC, we raised from Accel. Um, we sold to a bunch of really cool companies like Ramp, AngelList, Valin, DoorDash.

64
00:09:40,616 --> 00:09:51,536
Um, yeah, so some really cool and interesting customers to work with. And yeah, so, you know, in late '24, we ended up, uh, you know... So the business was growing pretty well.

65
00:09:52,016 --> 00:09:57,596
We ended up meeting Kareem and Varun, uh, through, I think, a mutual connection.

66
00:09:58,056 --> 00:10:09,156
Um, but at the time, we had been approached by some other players in the space, so some other, um, I'd say, like, data engineering companies and who'd always been interested in acquiring the business.

67
00:10:09,676 --> 00:10:16,416
And so, uh, we were kind of in that mindset of like, hey, we could raise a Series A. Um, we were pretty excited about the business growth, but weren't- Yeah...

68
00:10:16,756 --> 00:10:25,255
necessarily, like, we didn't know if, like, this was gonna be then, you know, the billion-dollar outcome that, you know, we were trying to, to get to when we set out to, to start the business.

69
00:10:25,716 --> 00:10:32,396
Um, and so then it was like, well, we should probably join up with a bigger company that already has more traction. Ended up, ended up just really connecting with Kareem and Varun.

70
00:10:32,936 --> 00:10:42,876
So they already had a lot of traction at that point? Yeah. I mean, I, I, you know, the- How big was the company, by the way, sorry? It was, I think we joined right as they were 50 people. It was- And you were how many?

71
00:10:43,656 --> 00:10:52,476
We were five. Okay. Yes. So you were, like, 10% of the company. Yeah. I think, I think we underappreciated how much of a bet they were taking on us. Yeah. [laughs] Um, like, to bring in 10% of the company- [laughs]...

72
00:10:52,476 --> 00:11:02,656
in just, like, one, in one day is, is kind of a, yeah, it's, it's a pretty big bet. [laughs] Yeah. Yeah. I think it's nice to bring in a skilled team and also perhaps, like, you guys were more on the automation side.

73
00:11:02,716 --> 00:11:14,116
Like, what do you s- what do you think you spiked more versus the original Clay team? Yeah, I mean, I, I think, one, just we were really deep in, in building, I don't know, just, like, very robust systems.

74
00:11:14,196 --> 00:11:20,516
I think, like, maybe the, the story I like to tell is, like, Clay was really focused on PLG, and they had really nailed the PLG motion.

75
00:11:20,596 --> 00:11:28,576
So, like, we joined the company when it was maybe, like, 15 to 20 million in, in revenue, but the biggest contract was, was really small.

76
00:11:28,776 --> 00:11:34,916
Like, we, it was just, like, so many companies who had found Clay and had just, you know, signed up and, you know, ended up getting value out of the platform.

77
00:11:35,316 --> 00:11:47,896
Um, but they hadn't really moved into mid-market or enterprise sales yet, and I think that was something that we, we really knew how to do, uh, at, at Avenue, was, hey, build systems that could go into DoorDash and, and AngelList and Valin, and all these kind of more scaled outcome companies.

78
00:11:48,476 --> 00:11:53,996
Would you say that was the, I guess, biggest learning that you took from Avenue and then applied it to Clay?

79
00:11:54,536 --> 00:12:04,876
One of the things that I think Clay has done really well is focus really deeply on one customer p-persona, right? Like the go-to-market engineer, and I, I feel like everything we do is for the go-to-market engineer.

80
00:12:05,536 --> 00:12:12,116
And I think at Avenue, we, you know, we had some commercial traction, but we never really figured out who our core customer was, right? Like, we were kind of...

81
00:12:12,480 --> 00:12:20,800
Across a couple of different personas, like different company types. And so I think one of the things that is just really impressive about Clay is the amount of focus on the single customer persona.

82
00:12:21,300 --> 00:12:29,940
Okay, so you guys join. Like, what was... Like, what was your 90-day plan? Like, what, what [laughs]... Like, like, can you maybe, like, paint a picture of the business at that point? Yeah.

83
00:12:29,960 --> 00:12:33,300
And you're like, "Okay, well, what's the plan for the next six months?" So yeah.

84
00:12:33,340 --> 00:12:41,660
So, so we joined, uh, Clay, and I think the main thing that we were trying to do at Clay when we joined was Clay had a really good business on sort of static lists, right?

85
00:12:41,740 --> 00:12:47,640
So I don't know, you throw a dinner, you want to figure out if any of the people who came to the dinner, like, are- Yeah...

86
00:12:47,680 --> 00:12:52,360
are good customers for you, and you could, you can do that in Clay, and, like, that was a good business for them at the time.

87
00:12:52,700 --> 00:12:57,320
But if you're trying to build revenue systems, which I guess now it's, you know, uh, now our new, new tagline.

88
00:12:57,360 --> 00:13:13,000
But if you wanted to build these sort of online systems of someone changes jobs and, like, you know, they had bought Clay at their previous company, but then maybe they would buy Clay at their, their next company, or like, you know, you kind of wanted to build these online systems for revenue, we didn't really have a great system in place to do that.

89
00:13:13,020 --> 00:13:17,340
And so we helped build out the original Signals product, which was effectively that.

90
00:13:17,420 --> 00:13:25,720
So monitor for new hires, monitor for things like promotions, like, any of these events that we could see in the market that you might wanna act on and build plays off of.

91
00:13:26,420 --> 00:13:32,820
So yeah, so we spent actually the first couple of months doing that, and there was a lot of tech overlap with what we had built at Avenue. Like, we're- Yeah...

92
00:13:32,840 --> 00:13:42,580
like very different domains, very different product spaces, but, uh, it just ended up being a pretty similar problem, uh, 'cause it was kind of market observability. It wasn't operational observability.

93
00:13:42,600 --> 00:13:52,420
It was just like, hey, like, look at all of these events that we can see in the market and be able to, you know, build plays off to, off of that. What was the hardest part about building the Signals product?

94
00:13:52,920 --> 00:14:01,600
There's a lot of things that were, were difficult about it, and I think one of the things that we didn't appreciate kind of building this was just the diversity of customers that would use it, right?

95
00:14:01,720 --> 00:14:10,180
Like, I think we've been used to really building things alongside a core set of design partners, but Clay has a lot of different customers, and they just have a lot of different- [laughs]... needs and different...

96
00:14:10,460 --> 00:14:18,780
And to the point about go-to-market engineers, like, they're really creative, and so, uh, people were building just kind of crazy stuff on top of this. Like, what are some examples, if you can share?

97
00:14:19,440 --> 00:14:24,500
I mean- Like surprising use cases maybe. I, I think it was just, like, s- some of the scale was just crazy and like- Oh, okay...

98
00:14:24,520 --> 00:14:36,380
I don't, I don't remember the exact numbers, but, you know, some people were, like, really trying to track every customer that they'd ever talked to, like, where they were, like, like their career progressions, like, different things that they were posting, so, like, news articles.

99
00:14:36,420 --> 00:14:50,900
Like, it was just, like, a very scaled-out, um, scaled-out thing. Okay. Yeah. Social mentions, product reviews, gong calls. Yeah. Okay. [laughs] Website visitors. There's just a lot.

100
00:14:51,260 --> 00:14:56,620
I mean, I think it's one of those things where it's easy to get really lost if you...

101
00:14:56,880 --> 00:15:06,020
It's easy to just, like, on day one of Clay, just go like, "Oh my God, I can, I can, like, react to all these things," and then you just stop reacting 'cause you're just drown under all these things. Yeah.

102
00:15:06,520 --> 00:15:16,540
I mean, that, that's the kind of the, the beauty and the, the scary part about Clay [laughs] is just like there's a ton you can do and, like, it's a really powerful platform, but, um, yeah, it's, it can be a little overwhelming.

103
00:15:17,020 --> 00:15:25,700
So did you join as, uh, like an engineering manager, and now you're head of AI? Like, w- like, when did that transition happen? Yeah, yeah. So actually, the, I...

104
00:15:25,900 --> 00:15:33,640
You know, so I, I joined to build out, uh, the Signals product, which is almost not, not really AI, right? It's just sort of, you know- Pipelines... pipelines, yeah.

105
00:15:33,740 --> 00:15:41,080
It was just sort of a regular system that y- you might build at kind of any company. I would say a lot of people used to use Zapier for this kind of stuff, right? Yeah, yeah.

106
00:15:41,200 --> 00:15:45,960
Um, and but, like, Zapier kind of, let's just call it politely, didn't evolve [laughs] with the times.

107
00:15:46,520 --> 00:15:55,900
There's all sorts of advantages of kind of building the system with all of the other stuff that you, you can do with Clay, right? Like, I don't know. If I think of Zapier as just, like, A to B data movement, right?

108
00:15:55,960 --> 00:16:06,740
Like, if you have all of this data piped into the same place, you can kind of do all these interesting things where it's like, hey, I only wanna react when there's, like, three people from this company that move to the same, same company or something like that, right?

109
00:16:06,760 --> 00:16:14,900
Like, um, you kind of have the statefulness as well. It's kind of nice. Yeah. Back to the transition, uh, to, like, head of AI. So, like, so you built the Signals product. What now?

110
00:16:15,200 --> 00:16:21,240
Well, yeah, so at, at the time, I mean, you know, we joined when the company was 50 people. Engineering team was ab- about 20, 20 folks.

111
00:16:21,900 --> 00:16:34,399
Um, I think Clay at the time, yeah, I mean, to this day, there was a huge part of the business was using agents to qualify and enrich stuff, like search the web, find data points about companies, like actually use those data points to do things.

112
00:16:34,860 --> 00:16:45,220
And at the time, there was one person working on that, and so I think he was maybe 24. So, you know, like, pretty fresh out of school, and he actually ended up leaving to go start a company of his own.

113
00:16:45,340 --> 00:16:54,560
So, you know, super excited for him. But, you know, we were this, you know, really AI-forward company that had zero people working on AI, so it was kind of scary. Yeah, yeah.

114
00:16:54,820 --> 00:17:04,780
Um, and so, like, we were basically like, "Hey, like, we, we really need to reprioritize, like, make sure that we're actually investing in this," and there was all this other stuff that we wanted to do in AI at the time.

115
00:17:04,820 --> 00:17:13,860
Like, we, we really just had AI as part of our workflows but not, I don't know, building workflows or sort of all the things that ended up becoming really important in the last year and a half. Um, so yeah.

116
00:17:13,940 --> 00:17:25,740
So basically, I shifted my attention over to, one, just kind of trying to get that into a good place and help build out that team, help build out the roadmap, and figure out kind of what we wanted to do as AI and agents- Yeah...

117
00:17:25,800 --> 00:17:34,280
and kind of build out the strategy. You said at that point in time, like, AI was, like, part of workflows. It wasn't really a big part of it. What were those things? And then, like- Yeah...

118
00:17:34,320 --> 00:17:41,780
what was on your roadmap that you were like, "Oh, we're gonna, like, totally overhaul this"? You know, we, we had an agent product in Clay actually really early.

119
00:17:42,060 --> 00:17:54,940
So I think, like, November of 2023, so, like, a year after ChatGPT, we had an agent product that would search the web, like actually structure data, like do structure data extraction from that, and you could use that in your Clay workflow.

120
00:17:54,980 --> 00:18:03,100
So you could imagine building a column that's like, "Hey, who's the CEO of this company?" And it would go off and search the web and kind of structure this data into a, a cell output.

121
00:18:03,600 --> 00:18:14,180
And I think, I mean, this is a, a huge part of the Clay business to this day, but it's not super inspiring as like, hey, AI's gonna change go to market. You know, I'm an engineer by background. I used Cursor.

122
00:18:14,580 --> 00:18:21,360
CloudCode came out in February of '25, and I was like, you know, this is a pretty different thing than what engineers had been doing. Um, and so-

123
00:18:22,296 --> 00:18:29,896
We were like, "Hey, this is clearly the direction that engineering is going, and, you know, there's probably something in go-to-market as well that we're gonna see as well."

124
00:18:30,075 --> 00:18:36,396
So basically trying to bring the same shift, um, you know, that Cursor brought to engineering actually to go-to-market in that domain.

125
00:18:37,096 --> 00:18:44,836
That was m- the majority of our roadmap, I would say, was actually just building agents into the product, letting people build and configure go-to-market plays with agents.

126
00:18:45,016 --> 00:18:50,816
What, what's the first thing after Signals that you start with that was- Yeah... like a real hit? Yeah. So we launched...

127
00:18:51,036 --> 00:18:59,196
Um, so, like, that was the direction that we were trying to go into was just agents building more of your go-to-market plays and, you know, improving them over time. But w- that, that came a bit later.

128
00:18:59,236 --> 00:19:06,596
But we launched Sculptor and- Oh, Sculptor first. Okay. Yes. I, I had Claygents pulled up. Yes, yes. So Claygents, Claygents is what we had in- The general form... in workflows. Yeah.

129
00:19:06,616 --> 00:19:15,316
Yeah, so it was just, like, Claygents were basically you would have an agent that would crawl the web, like, structure data, and put it in a table. And it's again, like, it's a huge part of the Clay platform.

130
00:19:15,396 --> 00:19:25,216
I think actually most people think of Clay as Claygents. Claygents. And yeah, we, we did a ton more work on Claygents, so I, I don't know. I mean, I, I... we basically rebuilt the entire Claygents stack.

131
00:19:25,316 --> 00:19:33,456
We, like, did a ton of work to just make this scale to the level that it is today. I mean, again, like, the business is basically 10X since we joined, and, like- Yeah...

132
00:19:34,116 --> 00:19:41,136
you can imagine that more people are actually using Claygents even than the business growth. And so, uh, there was just a ton of work to get that into a good place.

133
00:19:41,476 --> 00:19:47,196
I was gonna say, uh, you know, you made the statement about the business is 10X since you joined. You could dra- draw a nice chart here. Yeah.

134
00:19:47,196 --> 00:19:55,016
[laughs] Uh, where it's like, you know, uh, Jeff joins here, and- [laughs] That's right. Yeah... look at, look at the shareholder value that we've added. [laughs] That's right. Uh, where is it? Yeah. Whoop.

135
00:19:55,016 --> 00:20:07,476
[laughs] That's right. Yeah. Yeah. Have a new acquisition. Uh, I mean, you know. So we're here, right? [laughs] I, I, yeah. It was... I, I, uh- [laughs] L- late, late '24, so. [laughs] Just, uh, very, uh... Yeah. Yeah.

136
00:20:07,516 --> 00:20:15,756
[laughs] Okay. Uh, yeah. So, so, I mean, okay, so a- and again, uh, just for people who, again, uh, many of whom they are engineers- Yeah... uh, they...

137
00:20:15,856 --> 00:20:28,116
or they are new to the overall, uh, GTME ecosystem, Claygents are just basically the same Clay interface, but everything is exposed to the agent. Agent can do everything that a human could do. Yeah.

138
00:20:28,256 --> 00:20:33,636
I, I, I would almost think of Claygents as, like, what sales reps would've been doing, like, a few years ago, right?

139
00:20:33,676 --> 00:20:43,356
Which is like, "Hey, like, for all of my leads, I'm gonna go figure out, like, I don't know, like, are they a plumbing company or a news company?" Right, like, they'll do some categorization.

140
00:20:43,496 --> 00:20:52,896
They might research, like, oh, do they have the number of employees that I would expect to be able to sell to this company? You, you can imagine they have access to all of the things you can do in Clay.

141
00:20:53,016 --> 00:20:59,736
They're just natively in your table, and they have access to the web as well. Um- Doesn't that data come from, like, ZoomInfo, like, all these other data providers?

142
00:21:00,216 --> 00:21:08,516
I would almost think of Claygents as, one, an agentic way to, to get some of this data. Um, but primarily it's the public web. Okay. So yeah. And then, so Sculptor? Yes.

143
00:21:08,856 --> 00:21:12,416
So Sculptor we launched, I think, almost, uh, just about a year ago.

144
00:21:12,856 --> 00:21:21,696
Um, and the idea with Sculptor was like, hey, we, we can go, like, one level of abstraction up, which is like, you know, if Claygents are sort of the, the things doing each of the tasks in your workflow, right?

145
00:21:21,736 --> 00:21:31,956
Like, they're, they're qualifying, they're scoring, enriching, like, I don't know, doing copywriting. Sculptor is the thing that's actually building those workflows to, you know, coordinate these Claygents together.

146
00:21:32,376 --> 00:21:40,976
Okay. You can think of it al- almost like- Orchestrator? Yeah, yeah. Like, so Sculptor's, like, building the table structure, and then, like, Claygents are filling in the table, table cells.

147
00:21:41,516 --> 00:21:49,236
Can you talk about, like, what the stack is you used to build it? I think we... Uh, I'll, I'll describe it. I, I think we, we've just learned so much since then. Yeah.

148
00:21:49,256 --> 00:21:54,216
I, I can describe sort of what we've, what we've changed. Yeah, maybe, like, talk about the evolution- Yeah... and how it'd be really interesting. Yeah, yeah.

149
00:21:54,316 --> 00:22:05,636
So, so we, we, we launched Sculptor in September of last year, so we, we basically were building it through the summer of last year. And I think at the time, you know, it was, like, Sonnet 3, 3.5, like- Oh... or maybe...

150
00:22:05,916 --> 00:22:16,056
I... It was around then, I think. You know, so, uh, the models were way less advanced, I think. Like, people just knew less about how to build agents properly. It was just, like, really figuring things out.

151
00:22:16,756 --> 00:22:25,936
Sculptor ended up being, you know... We had a bunch of different tool interfaces to, you know, access, read, update the Clay platform, and we basically gave it to a model in a loop.

152
00:22:26,396 --> 00:22:39,836
And, you know, we spent a lot of time on sort of system prompt optimization and tool definition optimization, and, you know, I think it, it, it came out well, but it was way less expressive than I think even CloudCode was at the time and definitely, like, the agents that people are building now.

153
00:22:39,996 --> 00:22:44,596
I think we just had way less ability to sort of do these, I don't know, long horizon things.

154
00:22:44,636 --> 00:22:51,356
So the way I'd describe it is, like, Sculptor was really good at doing things like, "Hey, add this column that does, you know, does, does this."

155
00:22:51,876 --> 00:22:57,936
It was not good at doing things like, "Build me an outbound campaign that's gonna deliver 10 qualified meetings on, on my calendar." Mm.

156
00:22:58,476 --> 00:23:07,156
Well, what does that look like when you say, "Hey, go build me an outbound campaign"? Like, is it connected to your systems? Yeah. I mean, yeah, I think that, like, it wasn't. [laughs] Okay.

157
00:23:07,156 --> 00:23:14,416
I'd say, like, I think that was, that was the other thing. It, it just lacked a lot of the context that- Okay... you know, your sales reps would have. Okay, so that's how it started.

158
00:23:14,476 --> 00:23:24,156
Like, what would you say were the biggest learnings that got it to, um, improve over time? Again, it, it was pretty good. Like, I think it, it accomplished a lot of the things that people were trying to do with it.

159
00:23:24,376 --> 00:23:31,996
And you guys were running evals at that point? Yes, yes. Uh, we were running, writing, writing evals, but I don't think we were measuring the right things. Yeah.

160
00:23:31,996 --> 00:23:38,396
And so, like, we launched it, and immediately we saw a ton of people trying to just do analysis on their tables, and we were like, "Oh, we didn't plan for that."

161
00:23:38,616 --> 00:23:47,736
And I, I don't know, like, a bunch of the evals were good for small companies, but then we had enterprise customers who had, like, millions of records in their tables, and, like, things would break down.

162
00:23:48,096 --> 00:23:54,376
So, like, all these sorts of things that were probably predictable in advance, but, you know, we... I don't know, we, we observed them in production, so. Yeah.

163
00:23:54,616 --> 00:23:57,816
Like, what do evals even look like for, for something like that?

164
00:23:58,216 --> 00:24:09,956
We were doing pretty standard stuff, I'd say, of, like, just looking at the, the outputs, like, judging the quality of whether the suggestions were correct. Um, so, like, LLM is a judge- Yeah... basically, you know.

165
00:24:10,196 --> 00:24:16,216
But, like, what are the outputs that you're, that you're measuring? It's basically the, the actual tools that it rec- it was calling. Okay.

166
00:24:16,356 --> 00:24:23,096
So it's like, hey, like, if it's, if the prompt is build a table to do these things, it would be like, did it actually add these columns?

167
00:24:23,464 --> 00:24:33,164
'Cause I was gonna say, it might be like in, in this context, right, like, the ultimate objective is to, you know, "Hey, go build me an outbound campaign to get me customers," might be hard to get that data. Yeah.

168
00:24:33,204 --> 00:24:39,944
Yeah, so it's, like, very unique use case of evals, I guess. This is probably a very different shift to where we are now. Yeah. I think, like, now we're doing...

169
00:24:40,024 --> 00:24:45,684
Uh, I don't think we're at that point where, like, uh, we're actually measuring some of the, like, downstream effects of these things.

170
00:24:45,744 --> 00:24:53,904
But we're, we're definitely, I think, doing, doing a much better job of, I think, measuring actual quality. So you're building this harness. Um, why not just use something off the shelf?

171
00:24:54,284 --> 00:25:02,124
Yeah, so I would say, like, the... If I were to summarize the learnings, one, it turns out coding agents are really good. Like, the models are really good at, you know, operating and coding agents.

172
00:25:02,504 --> 00:25:12,484
Coding agents are really good at using things like Bash or using things like Python to actually write scripts and do things. Two is, like, hey, the expressivity of some of the tools that we had was just too small.

173
00:25:12,764 --> 00:25:20,764
Like, we kind of needed actually ways for the agents to chain these tools together or, like, I don't know, build five columns at once or kind of do a bunch of stuff.

174
00:25:21,204 --> 00:25:33,544
And then I'd say the last thing is, um, uh, I, I think it was just too constrained in terms of the primitives it had access to. To your point about data, like, we didn't have CRM data, and we didn't have, you know...

175
00:25:34,344 --> 00:25:38,984
If someone was gonna send a campaign, we didn't have access to the actual results of that campaign. And so that...

176
00:25:39,004 --> 00:25:47,564
This was, like, a platform-wide effort where we rebuilt a ton of parts of the system where, like, we now have a core data context layer where it's like this is called Audiences.

177
00:25:47,604 --> 00:25:56,924
Like, we bring in CRM data, we bring in Gong data. You can entity resolve it all together. Like, you can imagine it's, like, the authoritative canonical spreadsheet of, like, your customers and contacts.

178
00:25:57,404 --> 00:26:08,264
Can I ask a cheeky question there? Yeah. A lot of this is duplicate work across, uh, customers. Yeah. Do you multi-tenant it, or do you have, like, single-tenant guarantees? It is single-tenant, so, uh- Ah. Yes.

179
00:26:08,544 --> 00:26:13,184
For everyone. The... Yes. There's, there's a ton of downsides to that, but, but yes, uh, we, we effectively have.

180
00:26:13,284 --> 00:26:23,624
Because, y- you know, and for the audience, you can save a ton of costs because you just onboard one person once. In- instead, everyone who's scraping google.com has to... Or, uh, what- whatever.

181
00:26:23,704 --> 00:26:29,444
Or, like, you know, you scrape OpenAI as a customer. Well, you have to go scrape them again. Yes. Yes. Okay. Uh, yeah.

182
00:26:29,764 --> 00:26:37,724
Uh, and, like, there's a lot of downsides of doing that, but I, I think it, it ends up being both simpler, and then I think also... I think there's less duplicative work than you would think.

183
00:26:37,984 --> 00:26:44,584
Like, people are doing kind of- Very custom things. Ver- yeah, like w- I wanna find out their- More custom than I would expect... I wanna find out their employee size.

184
00:26:44,624 --> 00:26:52,444
I wanna find out, like, their phone number- Totally... or name of their firstborn. Like [laughs] Yeah. Yeah, yeah. [laughs] Yeah. As soon as you get to that part, then, you know, then it, then it devolves a bit. Uh,

185
00:26:53,464 --> 00:26:59,444
we do have our, our own data sets of companies and contacts, and, like, those are out of the box, right? Like, you can just bring them in.

186
00:26:59,524 --> 00:27:05,924
So, like, if I, if I just wanna start with a list of companies, like, we'll help you build that, and, like, that, that just comes from our database and, like- Okay... you know.

187
00:27:06,264 --> 00:27:14,064
There is not, there's not, like, a specific branding behind that. I can't- Uh, I- I can't see it on the- I think we brand- There's a data marketplace... we would brand it as search if we brand it as anything.

188
00:27:14,104 --> 00:27:24,304
But the, the idea is, like, you, um- There's data marketplace, there's, there's, like, other things in products, but it's not really like- Yes... like, Clay itself has data. Instead it is the...

189
00:27:24,404 --> 00:27:32,004
The messaging is, like, "We have all these integrations." That's right. Yeah, we, we, we do have a, a data set that you can start with. And so if I'm just like, "Hey, I want," you know.

190
00:27:32,264 --> 00:27:36,864
I mean, you know, maybe, maybe the framing is, like, well, this is what you'd have to do if you built it in-house. Mm-hmm. Right?

191
00:27:37,024 --> 00:27:43,704
Like, so Clay is simply, like, the, the software as a service that you install, and it does- Yeah... the thing that you would normally do in-house anyway. Yeah, the...

192
00:27:43,744 --> 00:27:50,744
I mean, you, you can think of it as, like, just an infrastructure provider, like, go to market flavored. Yeah, I guess back, back to the, the agency that you're building.

193
00:27:50,844 --> 00:27:59,164
Okay, um, you said you started with whatever it was, like, Sonnet. Yes. Sonnet 3.5. [laughs] It was not, not great. Obviously, like, models are getting insanely good now.

194
00:27:59,644 --> 00:28:07,724
Also, open source models are getting really good now. Yeah. So are you guys, you know, thinking about that? Are you guys, you know, fine-tuning them? Starting to think about this way more.

195
00:28:08,064 --> 00:28:24,884
I think, um, since, since I've been at Clay, I think we've flirted with the idea of doing post-training, like, I don't know, training our own models, and I think, you know, it just realistically hasn't been viable for a number of reasons for I'd say the past or, like, the first 18 months, uh, of, of when I joined Clay.

196
00:28:25,424 --> 00:28:32,024
I'd say in the past couple of months, like, it's started to be more potentially viable in some areas. Like, what areas?

197
00:28:32,504 --> 00:28:39,564
The main thing, I'd say this is true for both open weight models and post-training, but I, I think just cost savings once you're at a certain level of inference.

198
00:28:39,623 --> 00:28:44,844
Like, you can get pretty good performance and just go a model class smaller.

199
00:28:45,204 --> 00:28:56,544
And if you're post-training on, like, just that model set of tools or, like, just that model's, you know, the input distribution of what you think, like, what queries that you want that mo- uh, model or agent to be optimized for, I think you can get pretty good results.

200
00:28:57,024 --> 00:29:06,544
Um, we're pretty early here, I'd say, on the post-training front. Like, we're starting to explore. I think we'll launch something pretty soon in, like, in this area. Um- Ooh. Yeah. Yeah, yeah.

201
00:29:06,544 --> 00:29:14,204
[laughs] Um- The general goal is to keep the capabilities constant but reduce cost and- That's right... reduce speed. Uh, increase speed. That's right, yeah. Yeah. Yeah.

202
00:29:14,244 --> 00:29:23,764
And, like, what do you think is reasonable for other heads of AI, let's say, exploring this process? What is a good goal? Yeah. So 50%, 75%? There's kind of two things that, uh, you can do.

203
00:29:23,844 --> 00:29:30,704
So one is just, like, off-the-shelf open weight models are, are pretty good now. Like, I, I don't know, like, you can get K3 at, like, decent prices.

204
00:29:30,724 --> 00:29:36,864
Like, K3 is still pretty expensive even, and, like, but it's pretty good, um, and still cheaper than Opus by a good margin.

205
00:29:37,284 --> 00:29:45,364
Uh, and then, like, beyond that, it's like, hey, you could probably get actually, like, a maybe not GLM-53 Flash but, like, a smaller weight, weight class of model to perform at, like, Opus level.

206
00:29:45,744 --> 00:29:51,004
And so, uh, there's kind of two jumps in cost reduction that I think you can, you can achieve. I don't know.

207
00:29:51,104 --> 00:29:59,884
I think, like, still maybe the, the pitfalls are, like, what I see people doing prematurely is, one, I, I still think training a frontier model is really hard.

208
00:30:00,164 --> 00:30:08,004
So, like, if you're trying to get post-frontier performance, like you're trying to exceed fable- like, achieve or exceed fable lev- level for, like, a domain even, it's pretty hard.

209
00:30:08,584 --> 00:30:18,004
And then I think the other thing is, like, hey, cost savings are great, but you have to kind of do that on a substantial enough base where the cost savings are gonna actually matter for, for that. And so I don't know.

210
00:30:18,064 --> 00:30:25,784
I think a lot of companies are jumping into this just too early, right? Like, they don't have enough of it, enough inference spend where the savings are gonna, you know, be material to the business.

211
00:30:26,104 --> 00:30:35,708
Um- So what would that be? Hun- 10 million? 100 million? It's, uh, you know, somewhere in the 10 to 100, like, is where you, like... That, that starts to be I don't know. Chunky. Chunky. [laughs] Yeah, yeah.

212
00:30:35,708 --> 00:30:46,668
Yeah, I think that is in line with expectations. I think, you know, maybe, uh, this is, like, very timely 'cause, uh, you know, a week ago we did the Jev podcast- Yeah... and Jev is all, all, uh, talk of the town. Yeah.

213
00:30:46,728 --> 00:30:52,748
But you as a head of AI are no strangers to classifiers. Yeah. Um- A lot of... There, there's a lot of- What's going on? Yeah. [laughs] Yeah, yeah. How...

214
00:30:52,768 --> 00:30:58,168
There, there's a lot of stuff, uh, there's a lot of overlap with what, what we're doing and, uh- Yeah... what, uh, you know, the goals of Jev.

215
00:30:58,448 --> 00:31:07,408
Is it actually additive or were you al- I mean, you're already doing classification, right? Yeah, yeah. In, like, spades. Yeah. And, like, you know. We haven't done anything yet with Jev in production.

216
00:31:07,548 --> 00:31:17,968
I, I think, um, I do think the name is really accurate, where I could- [laughs]... imagine people just use Jev way more. And so, like, I, I don't know.

217
00:31:18,068 --> 00:31:25,388
People, people do use Claygent to qualify, but people are still restricting their lists to, like, oh, maybe I'll, like, take 10,000 companies and just qualify across them.

218
00:31:25,988 --> 00:31:36,548
But the thought experiment I can think of with Jev is, like, we have a, a company data set of 40 million companies, right? And you can imagine that, I don't know, every company's LinkedIn is maybe, like, 1,000 tokens.

219
00:31:37,108 --> 00:31:47,088
And maybe your company's ICP, like, ideal customer profile, is, like, 500 tokens. And so it's 1,500 tokens across your ICP and their, um, you know, and their LinkedIn.

220
00:31:47,728 --> 00:31:58,808
You can imagine just asking a question like, "Is this customer a good fit for my product or service?" And you could run that across every company in the world, and it comes out to, I think, around 1,500 bucks, right?

221
00:31:58,868 --> 00:32:07,048
You just multiply 1,500 tokens times 42 billion, you know, $42 per billion tokens. It's like, that's crazy. You just kind of, like, across...

222
00:32:07,288 --> 00:32:16,408
A- and you get a probability of, like, is this a good customer for you across every company in the world. Um, pretty, like, a pretty cool starting point in Clay. What's a budget for enrichment?

223
00:32:16,468 --> 00:32:23,388
Or maybe you have a target for that. It varies a lot, but I would say, like, you know, 1 to $10 per qualified lead is, like, a pretty good range.

224
00:32:23,768 --> 00:32:34,268
You know, if you're booking a co- um, a call with someone that's, like, you know, on the order of 10 to 100 is not crazy. Yeah. So. Wow. 10 to 100. [laughs] Yeah. It just depends on the type of business, right?

225
00:32:34,308 --> 00:32:39,808
It, it totally depends on, yeah, the type of business, like, the expected value of, like, each customer for, for someone. But, uh...

226
00:32:40,428 --> 00:32:48,868
Maybe one thing we can talk about is just, like, where do you, like, in your agents need frontier intelligence, and where do you not need frontier intelligence?

227
00:32:49,868 --> 00:33:03,248
There are definitely examples of, um, to the point about go-to-market engineering being engineering, I think there's a huge variance in terms of how you orchestrate some of these go-to-market plays and the kind of intelligence or reasoning that are required there.

228
00:33:03,788 --> 00:33:06,948
And so, like, I don't know, something sculptor-like or

229
00:33:07,868 --> 00:33:19,948
having an agent that actually builds end-to-end plays for you is something we're still, I think, like, the difference between the best and the average is, you know, a 10X, 100X in output, like variation, right?

230
00:33:20,028 --> 00:33:30,088
So, like, I think, like, kind of the higher level of extraction you are, frontier intelligence still matters. The stuff on, like, task agents or, you know, the qualification step, I don't know.

231
00:33:30,168 --> 00:33:36,668
I think, like, our evals have probably been saturated there for about a year, right? Like, new models come out, and, like, they might be better for some of the harder tasks.

232
00:33:36,948 --> 00:33:46,928
I actually think this is where model routing is pretty helpful for stuff like Claygent, where people are still doing deep research tasks and trying to prospect into companies really deeply, and they're...

233
00:33:46,948 --> 00:33:51,808
Like, Fable is much better at than something like, I don't know, GLM 5.3 Flash.

234
00:33:52,268 --> 00:34:02,848
But, you know, if you're just trying to get, I don't know, the most recent funding announcement for a company, I mean, any model that's come out in the last year can do this quite effectively for, for any company.

235
00:34:03,128 --> 00:34:06,048
And so, yeah, it's just started to move higher up the stack, I think, right?

236
00:34:06,088 --> 00:34:15,888
Like, the more orchestration level things or the more kind of creative, like, trying to break into very specific types of companies where, like, you're still seeing benefits from frontier level intelligence. But yeah.

237
00:34:16,288 --> 00:34:24,008
Yeah. You said model routing is important. Uh, do you have your own router or is there... What's the state-of-the-art there? We will, we will launch a model router, uh, quite soon. Yeah. Ooh. I think. Scooped it.

238
00:34:24,128 --> 00:34:31,148
[laughs] Yeah. [laughs] Yeah. I, I think, uh, that's one of those things where, um, so I have this theory, thesis about what I call the agent labs, right? Which is where- Yeah...

239
00:34:31,448 --> 00:34:41,148
you know, look, like, your customers are not necessarily in there all day, like, clicking the mo- model toggle and picking models, and, like, some of them want to, like, maybe 5% of them want to.

240
00:34:41,208 --> 00:34:50,068
The rest of them just wanna get on with their jobs. And they trust you as the technology provider to choose for us, right? Yeah. I, I would say, like, our, our, our users hate our model selector. Really?

241
00:34:50,088 --> 00:34:55,608
Like, they hate it. [laughs] Like- Are you gonna get rid of it? Or are you- No. We'll, we'll keep it, but- Yeah. That's the aggressive position, right? [laughs] Yeah. I, I like...

242
00:34:55,648 --> 00:35:01,828
I, I think most, most customers, like, don't wanna see it. Like, they're upset when they see it. Yeah, yeah, yeah. And we get a bunch of complaints about that. Yeah.

243
00:35:02,148 --> 00:35:12,708
The, the analogy I've had recently is, um, you got Tesla self-driving, right? Uh, and then, like, you just wanna put it in self-driving most of the time, but some people want to steer, some people want, uh, stick shift.

244
00:35:13,088 --> 00:35:18,148
All... More power to them. Yeah. Most people are just gonna self-drive. Yeah. [laughs] No, I, I think it, it makes sense.

245
00:35:18,208 --> 00:35:28,828
Like, I, I, I, um, I think customers are not in the position to, like, look at the evals for the specific use case for every new model that comes out. Like, it just doesn't make sense for them to be, you know...

246
00:35:28,848 --> 00:35:34,588
A- and for, I mean, for some, for the customers who want to do that, great. Like, you know, we'll keep the, our model selector. Like, it makes sense, but... Yeah, yeah.

247
00:35:34,928 --> 00:35:41,228
So, like, I think, uh, the way that, for example, Commission is doing it is they, they have some branding around it. They call it, like, Devin Fusion or whatever.

248
00:35:41,568 --> 00:35:49,808
Is there, like, Clay Fusion or, like, Clay One Model or whatever you wanna do? No. I think we'll, we'll, we'll just do auto mode. Yeah. Yeah, so. [laughs] Yeah. Be humble. We're not trying to get fancy with it. Yeah.

249
00:35:49,808 --> 00:35:57,028
[laughs] Like, we just wanna help people out, I think, uh, yeah. The one downfall, which I don't think is a huge one, but you wanna watch it, is, uh, people do get suspicious.

250
00:35:57,068 --> 00:36:04,788
They're like, "Well, how do I know you're spending my tokens well, you know?" Like, it's... This is basically, like, a trust us mode. Then you just have to provide analytics, I guess. Yeah.

251
00:36:04,888 --> 00:36:12,428
I mean, like, I, it's totally a hard problem. I think, you know, hopefully we, uh, you know, we build enough trust with people that they, that they want to use auto mode, actually.

252
00:36:12,468 --> 00:36:27,528
Like, um, and the idea is actually it should be better than, you know, selecting your own model for, for different things because, like, hey, it can actually do it on the task level, where it's like, hey, like, I don't know, finding the CEO of Apple is very different than finding the CEO of, like, a random company in, you know, somewhere that is not so well known.

253
00:36:27,888 --> 00:36:38,068
It's actually interesting 'cause your users are, I would think, like, power users kind of, right? Um, they're, like, go-to-market engineers. A lot of your customers are agencies, right? Yes.

254
00:36:38,168 --> 00:36:44,288
I would assume that they would want that level of control. Yes. I don't think the agency owners, uh, will stop selecting their own models. Okay. [laughs] So, yes. Uh, yeah.

255
00:36:44,688 --> 00:36:49,648
Uh, I think this is actually just for kind of everyone else, right? Mm. Like, just, like, um, we have, we have a ton of customers at Clay.

256
00:36:49,708 --> 00:36:58,800
We have a ton of people who come to Clay with some idea of go-to-market engineering, but they're still- New to a lot of this stuff What percentage would you say is, like, agency customers versus everyone else?

257
00:36:59,220 --> 00:37:04,620
Now I think it's, there's a lot of just the everyone else category. Yeah. Like, there's a lot of people who just come to Clay and find Clay.

258
00:37:04,660 --> 00:37:11,360
You know, we have a lot of brand and marketing, and I think, like, a lot of people just, uh, find us, you know, through word of mouth. Yeah. Can we go back to evals a little bit? Yeah.

259
00:37:11,360 --> 00:37:20,660
So maybe we can talk specifically about Sculptor. Yeah. So for Sculptor, like I'm assuming you have buckets of, like, the types of evals that you're doing. Like, what are those buckets? So yeah.

260
00:37:20,720 --> 00:37:28,800
So, so one, like, we, uh, we've done a ton of work since we launched Sculptor. I think now we're, uh... Well, one, we, we basically rebuilt the entire agent ar- architecture.

261
00:37:29,020 --> 00:37:40,900
So, like, it is no longer just a tool loop, tool loop model. It is, like, a proper coding agent. It has, uh... We launched our CLI, um, publicly, and the new version of our agent, uh, just uses a CLI.

262
00:37:41,260 --> 00:37:46,740
It uses it in a cloud sandbox, and it's just way more expressive. It can use, like, all different parts of the Clay platform.

263
00:37:46,940 --> 00:37:52,160
So that's, uh, that's one thing is just, like, we completely rebuilt it from the ground up to leverage all the Clay primitives.

264
00:37:52,540 --> 00:37:57,360
In terms of the categories of things that we're looking at, I think it's largely use case based still.

265
00:37:57,620 --> 00:38:08,100
So it's, like, the types of things customers do in Clay or try to use our agent for, and then trying to describe both the trajectories that we think should get there. It's like, hey, like, it should probably use...

266
00:38:08,140 --> 00:38:15,960
You know, if it's asking about first party data, it should probably query the data context layer that we have. And then also just the actual quality of the response and things that happen, right?

267
00:38:16,000 --> 00:38:22,520
So we measure, like, hey, if it, the user asked to build a workflow, did it actually build that workflow, and did the workflow actually have these, these properties about it?

268
00:38:22,840 --> 00:38:28,060
Maybe how do you see that evolving over the next, I don't know, six months? It's hard to know. [laughs] Yeah. I think, yeah. Um,

269
00:38:29,000 --> 00:38:39,400
I, I, I mean, I, I really would love to get, um, just actually synthetic, like, output generation. Like, measuring the second order effects of some of these things would be really cool. Like- Second order effects?

270
00:38:39,800 --> 00:38:48,260
Second order effects as in, like, if it, if the user asked to build an outbound campaign to reach out to, you know, this list of people, it's like, could we measure if it, if those people actually respond?

271
00:38:48,880 --> 00:38:54,980
So not only did they build the list and not only did they build the workflow to engage with those people, but, like, did that actually work? You know, did that...

272
00:38:55,020 --> 00:39:03,700
You know, and, and ideally, that's the metric that we want to improve over time, is the measured output for people. I see. But you can't really own all of that because some of it is my skill issue, right?

273
00:39:03,780 --> 00:39:13,060
Like, of, like- Yes, yes... well, you know, maybe I don't work at a good enough company. My, my cold email wasn't good enough, whatever. That's kind of the trouble with some of these evals broadly. [laughs] Okay.

274
00:39:13,060 --> 00:39:19,860
[laughs] Like, you know? This is my problem with, like, people saying, like, real money is the real eval. Yeah. And I'm like, yeah, well, that's, you know, that's everybody's real eval.

275
00:39:20,100 --> 00:39:25,540
There's part of me that always wants to build an eval platform into the, into the product too, or something that's eval-like.

276
00:39:25,940 --> 00:39:32,100
Either own the outcome for people or kind of build something into the product where they can start to build these tests and, like- Yeah... build that assurance. Yeah.

277
00:39:32,300 --> 00:39:42,900
Um, it's- That's actually holding you back almost as, as a company because you can, you can never own the outcome- Yeah... 'cause you're, you are a tool for people to do, like, mass volume basically. Yeah.

278
00:39:43,300 --> 00:39:47,420
Well, I, I mean- Which is fine. Like, you're a great- Yeah. For now... you're, like, you're, you're, like, state-of-the-art in your category. Yeah.

279
00:39:47,460 --> 00:39:52,100
But, like, like a Sierra will be like, "No, you just pay us for outcomes." That's it. Yes, yes. Right? That, that's true.

280
00:39:52,180 --> 00:40:01,020
No, I, I, I, I don't think we're, we're trying to do the, you know, full outcome based type of thing. But even Sierra, I think, you know, Sierra has an eval platform built into, into Sierra.

281
00:40:01,440 --> 00:40:09,000
So I think, uh, you know, there's something there where, like, you know, if something can't be expressed in our internal evals, it's probably, like, a product feature to be built around it.

282
00:40:09,580 --> 00:40:14,000
But I mean, it's, it's a bit tricky. I don't know. So what does your, like, team composition look like?

283
00:40:14,300 --> 00:40:24,340
Maybe, like, do you have specific people working on evals only, and do they happen to be, like, go-to-market engineers? Like, yeah, what does that look like? No, they're, they're mostly, mostly just engineer profile.

284
00:40:24,380 --> 00:40:32,500
Like, I think, uh, just in terms of the team breakdown, I'd say it's probably a pretty even split. We have people who spike in kind of traditional machine learning.

285
00:40:32,880 --> 00:40:40,560
We have people who you'd probably consider, like, applied AI engineers, so, like, people who've built evals and, like, kind of like like to do that type of work.

286
00:40:41,060 --> 00:40:48,500
And then you have just the sort of standard software engineering profile. It's like, hey, like, I don't know, this is an engineering system, and you can, like, build a bunch of stuff around that.

287
00:40:48,900 --> 00:40:58,600
Do you have different titles for those different people, or are they all engineers? I think everyone's just a software engineer. Yeah, yeah. Nice. AI engineer now. Yes. Yeah, yeah, yeah. [laughs] Yeah.

288
00:40:58,960 --> 00:41:08,780
What is the hardest capability to hire for? Like, let's say you're, you would like to add, uh, one more additional person. What do you wish they had? I mean, it's, it's really hard to get people...

289
00:41:09,360 --> 00:41:17,200
You know, I, I don't know how much of this... Clay's in New York, and so, like, there's, there's a sort of- You wish they weren't in the Bay Area. [laughs] No, no, I... But there's just a different set of pro-...

290
00:41:17,560 --> 00:41:28,300
So I, the thing that's really hard to find is people who have, like, hands-on experience building production agents. And New York doesn't have it? Uh, it's just- I'm so sad... it's not as common. Yeah. I, I, I- [laughs]

291
00:41:28,380 --> 00:41:34,260
I, I think it's, it's, it's harder to find in New York. Um- No, no, no, no, no. Okay. Well, we will, we will strive to prove you wrong. Yeah.

292
00:41:34,280 --> 00:41:42,560
[laughs] You know, like, uh, you know, my second largest conference is AI in New York. Okay. Like, like, we are gathering all these people, like, uh... No, it's very sad. Like, like- Yeah...

293
00:41:42,580 --> 00:41:51,420
you know how many people, N- New Yorkers tell me, like, "Oh, there's just no AI scene here." Yeah, yeah, yeah. I mean, the, the- It's just you and Modo and, like, Runway and that's it. Yeah. R- like Ram- [laughs]...

294
00:41:51,460 --> 00:41:59,420
Ramstill has a pretty big presence. Ram, Ram, yeah. Yeah, yeah. But yeah. No, I, I grew up in New York, so I, I'm, I, I love New York. Uh- Silicon Alley is supposed to be a thing. I know.

295
00:41:59,500 --> 00:42:07,840
I, well, it's hard, it's just hard to find people who have built production agent... You know, one, it's just there's a time element of it, right? Like, ChatGPT is, you know, still only four years old.

296
00:42:08,100 --> 00:42:17,000
So, like, I don't know. If you've spent a year working in agent engineering, like, there's still got a lot of... You know, that's- Yeah, yeah... this kind of limits the pool. Yeah. I, I, I mean, the more the stack...

297
00:42:17,020 --> 00:42:26,560
And you know, I think something that I'm closer to that maybe, maybe Basil didn't pick up on but I did, which was kind of like, let's call it workflows and pipelines, batching.

298
00:42:26,900 --> 00:42:33,900
Um, uh, so I come from the temporal background. Yeah. I used to work at Temporal. Uh, do you use that? Do you use something else as an, like a backend orchestrator?

299
00:42:34,340 --> 00:42:43,580
Anything in the reliability orchestration stack that you want to go into? Uh, I feel bad. We obviously- LangGraph? Uh, [laughs] uh- No LangGraph? None of the above, un- unfortunately, yeah. Hand rolled?

300
00:42:43,780 --> 00:42:56,780
No, hand, hand rolled. Yeah. Wow. Um, yeah. There's a couple different parts of the system. For some of the agent durability, um, we have still gotten away to the large, for the most part, building on top of BullMQ.

301
00:42:57,256 --> 00:43:07,216
The Java. Ooh, woo-hoo. [laughs] JavaScript? Yep. Very brave. Yep. Uh- Any, any pain points, or all good? Uh, for the most part, all good. What? Yeah. I, I don't know if- Amazing...

302
00:43:07,336 --> 00:43:17,096
I don't know if we'll survive another 10X on BullMQ, but so far so- What's the most likely choke point if it, if you don't survive? By the way, I'm, I'm like a huge data stack guy, right?

303
00:43:17,156 --> 00:43:26,756
Like, there's this whole- Yeah... like, you, like, you- Yeah... embedded inside of you, there's a whole data warehouse and a ETL, reverse ETL pipeline. Yeah. Right? Yes. You had to basically subsume all of these guys.

304
00:43:27,036 --> 00:43:34,896
Yes. [laughs] So, there's, uh, there's- So I used to work for some of these, you know, and they're all dead basically. Yeah. 'Cause, like, you can just vibe code your own. I mean, I would say, like, we- [laughs]...

305
00:43:34,916 --> 00:43:40,736
you know, Ave- Avenue was, like, probably, like... We, we, we sort of thought of ourselves as kind of in this data monitoring, like, you know, like MetaPlane.

306
00:43:40,796 --> 00:43:50,116
Like, th- this is, like, sort of adjacent to what we were doing. Um- Yeah, Kevin. I used to, I used to hang out with those guys. Yeah, yeah. I mean, like, I- Yeah... you know, it's a, it's a very interesting market.

307
00:43:50,396 --> 00:43:59,316
I really like the, the data space. Um- Okay. Wow. All right. Yeah. Yeah, that was a very short answer. [laughs] Oh, no. Yeah. Uh-huh. No, that's what I think...

308
00:43:59,356 --> 00:44:08,796
Okay, like, uh, I do think, like, uh, basically the da- the former data guys, th- that's, that's- Yeah... I'll, I'll put, like, myself, I'll give myself maybe, like, one third credit as a data guy.

309
00:44:09,476 --> 00:44:13,756
You are basically subsumed inside the AI engineering ins- Yeah... subsumed inside the app.

310
00:44:13,816 --> 00:44:22,896
It is assumed to just work, but you know that you have to build a whole context layer and a knowledge graph and, like, do all these pipelines. And, like, sometimes they break, guys. They don't just magically work. Yes.

311
00:44:22,916 --> 00:44:32,516
Uh, and, like, you don't... You, you do all this in-house? We use ClickHouse a, a bunch, both in-product and then for, for our own stuff. Uh, we're Snowflake users, uh, for, like, analytics. But new...

312
00:44:32,576 --> 00:44:44,016
I mean, like, most of the stuff in product is hand roll, so it's on top of Postgres. Um, on top of- Man, m- modern data stack is cooked, man. [laughs] That's all I can say. Uh, look at this. Yeah, yeah.

313
00:44:44,036 --> 00:44:54,336
[laughs] Um, no, I mean, like, I... You know, for, for some of, for some of our internal data sets, we were using Dagster, and I think, like, we're, we're reworking some of that, some of that, but, um, yeah, it's, uh...

314
00:44:55,396 --> 00:45:05,236
Wow. [laughs] Impressed, impressed. Yeah. No, yeah, because, like, you know, I've been, uh, maintaining some of these things, right, all the connectors. It used to be a huge business- Yeah...

315
00:45:05,316 --> 00:45:12,856
just maintaining all of that, and I guess, like, now you don't need to, or they all have SCPs or whatever. I don't know. Yeah. I mean, you know, I, I, I don't know.

316
00:45:12,876 --> 00:45:20,216
I mean, the- there, there are a lot of people at Clay who work, who work, who work quite hard at, at, at, like, maintaining and, and building these, but, but yes, I, I... It's definitely... Like, I think they...

317
00:45:20,256 --> 00:45:24,096
The team's much smaller than I think you would expect. Yeah. And, like, I, I don't know.

318
00:45:24,136 --> 00:45:32,616
Like, we just launched, I think, like, 25 or 30 new integrations and, like, uh, the, the bottleneck was not engineering work, right? It was just, like, all of the contracting and- Yeah... and the stuff around it.

319
00:45:32,656 --> 00:45:38,496
Well, also q- uh, quality control, right? Like, it's good to- Totally... it's easy to get a basic integration working, but, like, did you really test it? Totally.

320
00:45:38,596 --> 00:45:44,616
Um, and, uh, yeah, you know, I'll, I'll shout out my former employer, Airbyte, and there's, there's much, like Fivetran, all those guys. Yes. Yeah.

321
00:45:44,876 --> 00:45:53,816
I have a couple questions on, like, what broke with your agents as you scaled. Mm-hmm. Yeah, so yeah. What broke? [laughs] Oh, man. Nothing. Just vibe code all day. Yeah.

322
00:45:54,676 --> 00:46:02,816
Yeah, so when I joined Clay, like, the, the immediate work that we were working on was Claygent, and Claygent, I think, is just... There was so much stuff breaking.

323
00:46:03,496 --> 00:46:11,656
One, like, we didn't have great observability for what was happening, so I don't know. We, we onboarded LangSmith. Like, very helpful, I think, just to understand what was...

324
00:46:11,716 --> 00:46:18,816
like, what the agent was doing, like what, what tools was it calling. I don't know, like, what wasn't working. Um, kind of all the things that you, you'd expect.

325
00:46:19,476 --> 00:46:24,736
I think also at our scale, because people are running stuff in a table, like, our inference workloads tend to be quite spiky.

326
00:46:25,136 --> 00:46:33,116
So it's like, you can imagine someone has a table of 50,000 companies that they're trying to s- research over, and you run an agent for each of those companies.

327
00:46:33,376 --> 00:46:41,816
So there's just, like, a ton of inference going to an inference provider, like, I don't know, uh, uh, like, quite quickly. Um, so I don't know.

328
00:46:41,856 --> 00:46:48,076
A lot of the work was around throttling, making sure that we were actually could fall over to, like, if, you know...

329
00:46:48,676 --> 00:46:56,276
If an inference provider went down or it was rate limiting us, we could kind of pause execution and resume. Uh, all of that work, I think, was... We spent a lot of time on. Across...

330
00:46:56,356 --> 00:47:04,116
Uh, so do you have, like, a sort of, like, a dual sourcing policy for all, all inference? Uh, dual sourcing meaning, like, you always have a fallback. We don't. Okay. All right. Um, and yeah.

331
00:47:04,216 --> 00:47:12,556
Like, for, for, for a variety of reasons, we'll, we'll probably do this now, is more just, like, because of our customer distribution, we care a lot about fairness.

332
00:47:12,856 --> 00:47:27,276
So, like, I- I'm trying to think of a, a customer example I can name, but, you know, if one of our large enterprise customers runs a million things that they want to, uh, enrich, we don't want that to, you know, crowd out, like, the person who just signs up for Clay and just wants to do, like, a 10-person workflow or something like that.

333
00:47:27,836 --> 00:47:32,576
That's called a noisy neighbor- Yes... I don't know if that's the right analogy, but- I think that's... Uh, yes. Yeah. Yeah.

334
00:47:33,056 --> 00:47:41,816
Uh, and a shout-out to your, uh, previous talks at the LangSmith conferences if you wanna check into those things. Uh, we won't cover those in detail, but- Yeah... uh, you know, they're our downstairs neighbors for now.

335
00:47:42,256 --> 00:47:49,176
Yeah. [laughs] Um, it's interesting also this, this whole, like, dual sourcing thing. Like, I, I basically... I'm trying to basically distill your...

336
00:47:49,216 --> 00:47:55,316
You know, you're ahead of a, a AI at, at, at, uh, at a notable, um, AI vertical company, and, like, there...

337
00:47:55,376 --> 00:48:04,876
I meet, like, a lot of you, and we cover a lot of you and, and your peers on our, on the podcast, and I see the same patterns. Mm. Right? I see, like, yes, actually smaller teams can do a lot.

338
00:48:05,256 --> 00:48:15,176
I see, yes, you wanna do a router, but you don't wanna take away the model picker. Yes, I see that you eventually want to dual source everything. Yes, I see that you wanna go from closed to open model, uh, open models.

339
00:48:15,656 --> 00:48:22,436
You know, the... Basically, I, like, probably we can build out this handbook of, like, what every head of AI needs to know. I, I don't... Is there, is there anything else in there?

340
00:48:22,436 --> 00:48:29,436
[laughs] Those are all good starting points. Yeah. [laughs] I'm, uh- I do think that a lot of people are exploring, uh, let's call it their, let's...

341
00:48:29,476 --> 00:48:37,456
in their agent infrastructure, how much power they want to give the agent. Yeah. What kind of sandbox do they wanna give the agent? Um, how much autonomy.

342
00:48:37,856 --> 00:48:45,876
Yours seems more pipeline-y, so maybe there's sort of more limited autonomy. But other people are exploring, like, effectively complete ChatGPT clones.

343
00:48:46,236 --> 00:48:56,376
Like, everything ChatGPT can do or Codex can do, uh, or Cloud Code can do, like, we will just basically ship a version of that for our users. This is, like, a very interesting one, so, like, we will effectively do this.

344
00:48:56,516 --> 00:49:02,276
So, like, we- Yeah, 'cause you started off saying file systems are, like, good, right? Yes. So, like, you know- Like, so that's the talk track for everyone saying the same thing. Yeah, no, they'll...

345
00:49:02,596 --> 00:49:11,776
We, we will effectively do this, where we have, we'll have an agent in the, in the product that does have a sandbox, is, like, quite unconstrained in terms of what you can do, and, you know, has access to all of the Clay primitives.

346
00:49:12,156 --> 00:49:15,096
But I'd say, like, almost our, our ethos and... I don't know.

347
00:49:15,136 --> 00:49:23,820
We spent a lot of time thinking about the right way to engage with this, but we want the Clay platform to be- Great for all agents, like, whether it's our agent or external agents.

348
00:49:24,180 --> 00:49:34,100
So, like, we explicitly don't want our agent to be markedly better than just using Clay and Claude Code. Like, if you use Clay and Claude Code, that's great. Like- And is that Clay MCP or Clay- Clay CLI primarily.

349
00:49:34,240 --> 00:49:43,980
Clay CLI? Yes. Okay. Yeah. And most- MCP's dead? I, I don't know [laughs] Yeah, yeah. Uh, MCP, uh, it's- It's making a comeback. It's making a comeback, yeah. I, I, uh... It's really funny. The, uh, the team who...

350
00:49:44,160 --> 00:49:53,720
We, we have an MCP as well, um, and but that team basically re- like, shifted their focus to, to build out the CLI. I mean, it's just integrations, right? It's just like, here's y- consume it however- Form...

351
00:49:53,780 --> 00:50:01,160
like API, uh, C- SDK, CLI, MCP. Yeah. Right? That's the four things. It's sort... Like, it's, it's just a form factor, and it shouldn't matter that much, but n- yeah.

352
00:50:01,340 --> 00:50:06,740
Now, now we're like, "Oh, we should probably build that." Like, people get really religious about this stuff. Yeah [laughs] Um, yeah. Yeah. Okay. No, I mean, it's just cool.

353
00:50:06,880 --> 00:50:08,960
I think it's, it's, like, good to check biases. Yeah.

354
00:50:09,020 --> 00:50:20,240
Um, but, like, I, I do think, like, uh, maybe, maybe one thing to check is what's the market share, I guess, of, like, Clay in Claude Code or, you know, Clay in external harness versus your har- your stuff. Yeah.

355
00:50:20,600 --> 00:50:28,900
I would have assumed it would be more the Clay harness, and I think... I forget the exact breakdown, but it, it's much closer to 50/50 than I would've thought. Yeah.

356
00:50:28,920 --> 00:50:40,700
Because I find, like, um, you know, I'm, I'm, I'm dating a GTM, uh, person, and she loves GroqBot. Yeah. And, like, you're never gonna gri- ply- pry GroqBot from her cold, dead hands. Totally, yeah. And so why not?

357
00:50:40,780 --> 00:50:47,720
Like- Yeah. And, and, and we're not trying to. Yeah, yeah. I think that's the, that's the thing that, like, I, I mean, we spend a lot of time just thinking about, like, do we, do we need to own the surface area here?

358
00:50:47,760 --> 00:50:55,800
And, uh, it's really okay. Yeah, yeah. Like, people can do go-to-marketing GroqBot, and- Yeah... we want them to have all the s- the- I will say, I don't know if you have, you have any, like, thoughts on this.

359
00:50:55,840 --> 00:51:02,120
Like, this is another thing that maybe Marc Benioff at Salesforce had also come to sort of that religion on, on that side of the fence.

360
00:51:02,420 --> 00:51:12,040
Because as a source of true for as, like, a SaaS provider, you can just be like, "No," like, "I want you all to pay my $20 a month, $200 a month, and use my thing."

361
00:51:12,420 --> 00:51:21,820
But, uh, exposing yourself as an API basically means you lose the first-touch interface, but then you just make your API really good. Yeah, I, I mean, I, I think, like, you know, I, I...

362
00:51:22,100 --> 00:51:27,400
We, we spent a lot of time on our agent harness, and, like, I hope people use it. Uh, that's actually not the point.

363
00:51:27,400 --> 00:51:34,180
[laughs] You know, like, I think we just want Clay to be this agentic go-to-market infrastructure, and, like, I think it'll be valuable in a lot of different places.

364
00:51:34,480 --> 00:51:40,700
So I guess, would you say you guys are trying to automate go-to-market, essentially? No. I mean, I would, I would frame it differently.

365
00:51:40,760 --> 00:51:50,100
I, I think we're trying to do the same thing, you know, bring the same shift that Claude Code brought to engineering. So it's like, I think, you know, go-to-market will... You'll still have go-to-market engineers.

366
00:51:50,280 --> 00:51:53,580
They'll just do way more. Mm. They will, I don't know, build a bunch of plays.

367
00:51:53,620 --> 00:52:02,660
And, like, I think about this from the perspective of Clay, where, like, you know, Clay has a really great go-to-market team, uh, maybe, maybe intuitively, but there's so much stuff we're not doing.

368
00:52:02,840 --> 00:52:11,980
Like, I, I don't know. Uh, we're not running a bunch of different go-to-market plays that... Like, I could probably think of 10 different go-to-market ideas that we're not doing right now. And I don't know.

369
00:52:12,100 --> 00:52:16,060
I think the, the goal of Clay is, like, we'll do all of that. [laughs] We'll just- Yeah, yeah. Yeah.

370
00:52:16,440 --> 00:52:23,460
One thing I like about go-to-market businesses is that your, basically, your, your GTM team can just tell your s- sales team what, uh, your engineering team what you need. Yeah.

371
00:52:23,700 --> 00:52:32,980
Uh, what's an example that's come from your internal needs that, like, you guys were like, "Oh, yeah, that really makes sense"? [laughs] Yeah. [laughs] I mean, probably the CLI was, like, a, a big part- Really?...

372
00:52:33,180 --> 00:52:41,960
of that, yeah. They asked you for it? Yes. Say more. I, I think a lot of people were just in Cursor, and it was, you know, similar to GroqBot, like, really hard to pry it out of their hands. Wow. Yeah.

373
00:52:42,480 --> 00:52:50,800
And they were like, "We g- we can't..." Yeah. Yeah, yeah. And your go-to-market team is mostly engineers? Our sales team is, is in Codex doing a bunch of stuff on, like, deal prep.

374
00:52:51,020 --> 00:52:59,380
But no, I mean, like, we do have a go-to-market ops team that is probably, like, our... I don't know. The, the naming's a bit confusing, but they're probably, like, what we would call a go-to-market engineering team.

375
00:52:59,760 --> 00:53:04,360
Yeah. Just cracked- [laughs] Cracked-... go-to-market people. Yeah. That's, like, the profile of, like, former engineers doing- Yeah...

376
00:53:04,380 --> 00:53:11,900
go-to-market work, like, building out a bunch of internal tools, like, built on top of Clay, um, for our sales team. Yeah, that makes sense. Yeah. I, I see it's still...

377
00:53:12,000 --> 00:53:20,540
Like, I'm still not over this whole, like, it's 50/50. Like, you, y- it's not the point of your, the Clay harness- Yeah... to beat Claude Code harness. Then, like, why do it at all?

378
00:53:20,800 --> 00:53:29,660
Like, why not just go all in on, on, like, just being the best, uh, CLI MCP for agents? Yeah. Uh, I think people, like, want something in Clay.

379
00:53:29,720 --> 00:53:34,220
Like, people are in, in the Clay UI building stuff and would want to use an agent there. Yeah.

380
00:53:34,400 --> 00:53:41,140
Um, so it, it's somewhat just following the customer demand, where, like, they're- You could ship Claude Code in a container, you know? Like- Totally. I mean, uh, yeah. [laughs] All right.

381
00:53:41,540 --> 00:53:46,640
I, I- O- Pi or OpenCode, whatever the open source one is, yeah. Yeah. I feel like that's effectively what a lot of these agents are. Okay. All right. Yeah. [laughs] All right.

382
00:53:46,920 --> 00:53:57,360
That's another weird thing of, like, well, where, you know, where are the sources of alpha in harness building, agent building? Yeah. A lot of people are saying there's not that much on top of what everyone already has.

383
00:53:57,480 --> 00:54:04,060
Yeah. And, like, wow. [laughs] Yeah. Our agent harness is built on top of Pi, and so, you know, we're, we're, we're starting with Pi, and, you know- Yeah...

384
00:54:04,340 --> 00:54:13,840
it's, it's, it's somewhat more, you know, built out and customized on top of it, but- Yeah. Did it start that way? Yeah. Wow. Well, like, in, in a post-Sculptr world, so, like, after we- Oh, okay, okay. Yeah, yeah. Yeah.

385
00:54:13,960 --> 00:54:23,840
It seems like, uh, it... And by the way, Pi is Python. You seem to have a JavaScript stack. Yes. You just merge languages. Yeah. [laughs] You just rewrite the whole thing. We use the Vercel AI SDK. Yeah.

386
00:54:23,900 --> 00:54:27,780
We use, uh, you know, their, their, their integration there. Yeah, yeah. Yeah, very cool.

387
00:54:28,640 --> 00:54:34,900
I think one of those things where, uh, we, we come across in the research is that you always talk about courage and e- emotional metabolism.

388
00:54:35,260 --> 00:54:39,120
Can you talk about, like, what that looks like, especially with, with something that didn't really work?

389
00:54:39,640 --> 00:54:49,380
I feel very strongly that, you know, institutional courage is, uh, probably the most important thing right now at companies. Uh, and it's really hard. I, I don't know. Like, I joined Clay at 50 people.

390
00:54:49,940 --> 00:55:00,720
We're now probably around 600. It changes a lot. Like, the momentum is just for things to calcify, and I don't know, just to do things requires more and more courage. So I, I don't know.

391
00:55:00,840 --> 00:55:10,660
One is just as a, as a principle, I think it is, it's quite important. Two, I, I don't know. I think there's a lot of uncertainty as things change a lot, and so, um, I, I can think of a couple examples.

392
00:55:10,720 --> 00:55:20,060
So one, like, we, um, uh... I think I've posted about this before, but we were one of the launch partners for ChatGPT apps. We're, like, the kind of the first wave of, of business apps in ChatGPT.

393
00:55:20,560 --> 00:55:28,540
And, you know, we had loosely been working with the team, uh, on, like, on supporting this. Uh, and then I think maybe, you know, so we basically reprioritized.

394
00:55:28,700 --> 00:55:34,028
I mean- Probably 25% of the engineering team for a month, like mid-quarter to, to get this done.

395
00:55:34,088 --> 00:55:42,468
It was like a huge sprint to like, you know, integrate with ChatGPT, and you know, ChatGPT is, has a ton of demand like so there's a lot of, you know, incentive for us to do it.

396
00:55:42,748 --> 00:55:50,288
But basically, the team was giving us kind of no indication of whether this was gonna work or not. M- they were just like, "Hey, maybe, maybe if it's cool, like we'll, we'll launch with that."

397
00:55:50,628 --> 00:55:57,888
And, uh, so we reprioritized like a quarter of the company basically to work on this. I think two days before we were supposed to launch, they were like, "We're gonna cancel it.

398
00:55:58,028 --> 00:56:07,368
We're gonna just, uh, we're, we're gonna postpone this indefinitely. We'll let you know if we, we do this again." So I think it was like- Sorry, who made that decision? OpenAI. Oh, wow. Yes. So we were like, "Oh, man."

399
00:56:07,388 --> 00:56:10,308
[laughs] That's a big, that's a- Yeah... you know, TLDR, it's a big move, right? Yes.

400
00:56:10,308 --> 00:56:19,008
[laughs] 'Cause but like I, I assume they didn't make that decision lightly, and like, you know, they have other b- balancing priorities. One would hope. Um. [laughs] No, I, I think, I think that's right.

401
00:56:19,088 --> 00:56:28,708
I, I, I don't actually exactly know what happened, but you know, like we, uh, we were just, uh, of course a little bummed out. But I think we were just like, "Hey, like this bet still makes sense.

402
00:56:28,808 --> 00:56:37,768
Like we, we just needed to do it," and actually just kept working on it with the assumption like, "Well, they'll probably change their minds." And I think like three or four days later, they, they changed their minds.

403
00:56:37,768 --> 00:56:46,368
[laughs] So- Ah, nice... like we actually like needed to keep working. They changed their minds in three days? Yeah. After a very public cancellation? Like what? Uh, well, they- [laughs]...

404
00:56:46,388 --> 00:56:53,768
they just told us they were canceling, so I don't know, you know, the, the reasoning. I mean, no, even making a decision to tell you they were canceling is like- Yeah, yeah... a very intentional thing.

405
00:56:54,168 --> 00:57:00,688
Do you have a hypothesis for like why they changed their minds? [laughs] Maybe- Uh... enough people were like, "Fuck you," like [laughs]... I already engineered all this stuff.

406
00:57:00,728 --> 00:57:04,648
[laughs] I think it's just like everything... I mean, I don't know.

407
00:57:04,768 --> 00:57:14,308
I, it's hard for me to speculate, but it's like I think things are just very dynamic right now, and so the decision-making processes around that are very dynamic as well, and that, that has- Yeah... permeated through.

408
00:57:14,308 --> 00:57:23,388
I'm just curious. I've, you know, like a- anyone who has deal- dealt with the labs, they're like- [laughs] Yeah... they have a lot of stuff going on. Mm. Yeah. It's, it's chaotic inside. We have sympathy for them. Yeah.

409
00:57:23,408 --> 00:57:29,328
They're trying, they're trying to do their best. Which totally makes sense. Yeah. Like, um- Could be better, but look, we're in, we're in AI times. Like things are moving quickly.

410
00:57:29,328 --> 00:57:32,608
Yeah, it was probably one of 20 priorities for us, and it was like one of our top priorities.

411
00:57:32,628 --> 00:57:39,088
[laughs] It was, uh- But like, okay, uh, actually, I question, uh, if I w- had been you, I would've questioned why m- you made it the top priority. Yeah.

412
00:57:39,267 --> 00:57:48,008
You know, let's call it every single dev day, you know, recording this on the eve of, uh, the, the fourth dev day, they've always tried to launch some kind of marketplace thing. It's always flopped.

413
00:57:48,408 --> 00:57:56,588
And like wh- why make this top priority? [laughs] This is probably at the beginning of when we were figuring out like the, the same surface area questions about the CLI.

414
00:57:56,728 --> 00:57:58,808
It's like where, where do we want to play with this?

415
00:57:58,868 --> 00:58:06,388
Like, do we want to have a full ChatGPT clone in Clay, and like that pr- that might make sense, but like it probably makes sense to leverage the things that exist as well.

416
00:58:07,008 --> 00:58:12,568
So I, I think one, it was just like, I don't know, it felt like the right bet to try. [laughs] And- It's like a game theory thing, right?

417
00:58:12,608 --> 00:58:20,068
It's like, oh, if you have a competitor that does it, and this time it actually ends up- You don't want to... Yeah, yeah. Yeah. I will say- Yeah... each year it does get better. Yeah. It does.

418
00:58:20,128 --> 00:58:27,688
The, the, it's more polished. It just, no, it's not gonna take over- [laughs]... the world by storm. Like- I- But it is very valuable to be page one. Yeah. I will say that.

419
00:58:27,808 --> 00:58:31,508
I, I mean, I think, you know, I, this is like back to the iPad development days.

420
00:58:31,548 --> 00:58:39,808
It's like, you know, I was one of the first 500 iPad apps on the store, and it's like a s- feels like a similar moment, where like AI's clearly a platform shift in some ways and like- Yeah...

421
00:58:39,868 --> 00:58:46,088
but I, I don't know if like people have figured out the platform part yet. Like, people have figured out the sort of the like AI sh- shift, but, uh, yeah.

422
00:58:46,608 --> 00:58:54,668
I mean, in, in some ways, you know, I think everyone has their sort of single pane of glass that they wanna be the platform. You are the platform for a lot other people. Like, a lot of people prioritize you- Yeah...

423
00:58:54,688 --> 00:59:03,168
as like we will make it big by demoing our integrations. Uh, you have your event coming up. Presumably peop- a bunch of your partners are gonna make that same announcement. Yeah. Don't cancel on them.

424
00:59:03,228 --> 00:59:13,268
[laughs] But no, I, I think, I think that's, uh, that's great. That's it, like emotional metabolism. Basically, just like take hits as they come, I guess. Yeah. [laughs] Having courage. Yeah. Yeah.

425
00:59:13,368 --> 00:59:18,968
I think, I think you need it. Like I, I don't know. Like it's, uh, just very easy to make wrong decisions right now. Yeah. That's the reality.

426
00:59:19,188 --> 00:59:23,848
And like you just have to keep moving and like- So first of all, there, there is a version of founder mode as well. Like, you know- Mm...

427
00:59:24,108 --> 00:59:34,588
one of the reasons to acquire a company when, you know, you have 50 people and you've got five, is they just like n- they need to keep injecting the founder mode energy of like look, I didn't come here as a regular employee.

428
00:59:34,708 --> 00:59:42,468
I can like shake things up. I was hired with the mandate to shake things up, and I can go do that. Yeah. Presumably Clay has done other acquisitions where they've, this has happened. Yes. Yeah, yeah. Right? Yeah.

429
00:59:42,568 --> 00:59:52,988
Um, yeah, this is a very standard reason to acquire, which is like well, like the people that get into the regular door just want things to stay the same, and I don't as a founder. [laughs] Yeah.

430
00:59:53,028 --> 01:00:02,468
I think the other thing that I think is really interesting in my, let's call it five years, uh, doing latent space and whatever, is like I see the, let's call it the courage of your convictions.

431
01:00:02,528 --> 01:00:11,048
Like, like sometimes you think a thing is right on first principles- Mm... and it doesn't work, doesn't work, doesn't work, doesn't work. Just hang on. It, it works eventually.

432
01:00:11,508 --> 01:00:17,848
Yeah, I mean, like one, just like the whole history of Clay, I mean, Kareem was building this company for five years with basically nothing working.

433
01:00:18,148 --> 01:00:25,588
So like I think just deep in his soul he kind of feels that, you know, things will work if you just keep pushing long enough. And I don't know.

434
01:00:25,648 --> 01:00:30,188
I think we have plenty of examples of products that like when, when we first launched them, it just didn't make sense.

435
01:00:30,228 --> 01:00:38,088
We just launched our workflows product, and, uh, I think a lot of agency owners are really, you know, really liking it. There's just a organic excitement about the feature.

436
01:00:38,508 --> 01:00:47,708
But when we first showed it to people, people did not understand it. They were confused. They were, in some cases, just upset. They were like, they, they were like, "Why are you doing this?" Just give me a list. Yeah.

437
01:00:47,768 --> 01:00:52,628
I want a spreadsheet. We were like, "We like the spreadsheet. Why are you doing workflows?" Um- This is, I mean, this is Zapier, right? Yes. I, I would say, yeah.

438
01:00:52,708 --> 01:01:00,368
I mean, the- they're probably things that, you know, I'd say we, we do differently, and, and, you know, if Z- if Zapier was built today, there's, you know, probably things that would, would be incorporated like this.

439
01:01:00,568 --> 01:01:08,908
Uh, you know, this is also sort of, you know, it's agent first, the CLI first. That's the major- like majority of workflows are built with the CLI or our agent. But yeah.

440
01:01:09,008 --> 01:01:15,168
Yeah, I would say, you know, like a- and, and for workflows, a- again, something I've, I've worked in quite a bit, this is always the dream.

441
01:01:15,228 --> 01:01:20,728
Like, you know, uh, one of the statements of Clay is like to give everybody the u- the ability to program and like- Yeah...

442
01:01:20,868 --> 01:01:30,368
do that stuff, including GTM engineers, and maybe they're not Python gods, maybe they are not, cannot be trusted in Cursor, right? Because like they s- should not have access to all the infra. Yeah.

443
01:01:30,388 --> 01:01:41,228
But here, here's like a, a blessed place where you can do all your tools, all your data, all in one place, and it's made for you to just go nuts. I think it's changing how we do stuff internally at Clay too.

444
01:01:41,608 --> 01:01:51,492
We were doing some analysis on just- How many YC companies are using Clay? Um Ooh, how many? [laughs] It must be really high. Soon all of them. It, uh, it is, it is high. A good ballpark is, like, let's, let's call it...

445
01:01:51,532 --> 01:02:01,492
I think Superbase has a number of, like, 70% of each batch is Superbase. Yeah. All right. I, I, I won't disclose the number. [laughs] But, uh, uh, but it, but, uh, you know, it, it, it's a healthy number.

446
01:02:01,572 --> 01:02:12,072
But I, I was just like, we just asked our agent for this, and it found it in, like, 60 seconds. Hmm. It's like, oh man, this... I was just thinking, like, a year ago, this would've taken so much time. Yeah.

447
01:02:12,112 --> 01:02:22,232
I would need to find and scrape the YC batch into some CSV on my computer. Then I would need to get Snowflake access somehow, and, you know, cross-reference there to be like, "Are they a customer?"

448
01:02:22,672 --> 01:02:29,152
Or like maybe Salesforce ac- you know, it's just like all these different systems, and you don't need any of that. Yeah. You can just, like, ask Clay, it'll, like, you know- Yeah...

449
01:02:29,172 --> 01:02:31,692
pull the list, it'll, you know, cross-reference everything. It won't be long. That's it.

450
01:02:31,732 --> 01:02:38,012
The beautiful thing about the domain that you're in that other people don't have [laughs] the privilege of is that most of your stuff is public-ish. Yeah.

451
01:02:38,032 --> 01:02:49,332
Like, there's no sensitivity if one em- pa- one employee sees another thing that they don't necessarily have access to. Yeah. It's all public-ish, right? Yeah. Um, whereas other people, they're like, "No, absolutely not.

452
01:02:49,392 --> 01:02:56,112
What do you mean you have, like, free rein to my s- my Snowflake?" Yeah. Like [laughs] Yeah, yeah. This is somewhat relevant to us. Like, it's not like...

453
01:02:56,232 --> 01:02:59,452
There, there are definitely companies where they want, you know, more fine-grained permissions.

454
01:02:59,532 --> 01:03:07,772
But yeah, just for the most part, I mean, I think that's the, the advantage also of having the data context layer is, like, you can bring in just the information that's relevant for, for good market.

455
01:03:08,152 --> 01:03:18,252
You don't need everything. Yeah. When did you launch the Workflows product? Uh, this was earlier this summer. So we, we did 12 launches in 12 weeks. I don't know why we did this in the summer instead of... I don't know.

456
01:03:18,252 --> 01:03:27,152
[laughs] But, uh, so, so, uh, yes, we did 12 launches in 12 weeks. Uh, this was, this was one of the launches. And how is it going? [laughs] Uh, it's, it's going great. Yeah.

457
01:03:27,192 --> 01:03:31,592
Uh, yeah, no- What metrics do you guys look at for this? Yeah, I mean, the, there's, there's a bunch of things that we're tracking.

458
01:03:31,812 --> 01:03:41,532
Um, one of the things that's cool is just the percentage of things people are doing in Workflows versus Tables. So like, you know, again, like people think of Clay as th- the spreadsheet tool, and- Yeah...

459
01:03:41,632 --> 01:03:48,012
that's, like, the core of the product. And we're seeing a lot of people just sw- switch to Workflows basically as their primary mode.

460
01:03:48,432 --> 01:03:57,272
Um, so both on a per customer basis, but just, like, as a percentage of, like, Tables versus Workflows, we're seeing that, like, grow pretty quickly. So there's a potential this could become the, like, main interface?

461
01:03:57,912 --> 01:04:07,112
I think there's... Yes. I mean, like, there, there's, there's for sure potential there. Yeah. Yeah. Are there any product launches or things that you're working on right now that you're, like, particularly excited about?

462
01:04:07,712 --> 01:04:10,292
Yes. That you can talk about? [laughs] Yes, yes.

463
01:04:10,332 --> 01:04:22,652
[laughs] Um, so one, uh, our rearchitecture of Sculptor, uh, this is live in some limited forms in our product now, but we are going to launch that broadly for everyone across every surface in Clay.

464
01:04:22,752 --> 01:04:31,352
This is, like, our first party agent. Um, that's probably what I'm most excited about. That's, uh... Yes. We'll, we'll launch this very soon. Um- Why does it have to be rearchitected?

465
01:04:31,692 --> 01:04:40,872
Uh, this is the, the, you know, the, the f- all of the rearchitecture work that we've done to rebuild it around a coding agent and, um, you know, all- I see. Yeah, yeah. Just more powerful.

466
01:04:41,272 --> 01:04:48,532
This is the, this is the agent that, uh, told us how many people were... How many, how much of the YC batch was using Clay, and, you know, you could do analysis of that. Yeah, yeah.

467
01:04:48,812 --> 01:04:58,252
What do you expect the outcomes of the, like, rearchitecture to be? Oh, I mean, just anecdotally, it's, it's- Just more usage, right? Okay... it's unbelievably more expressive and, and useful. More extensible. Yeah.

468
01:04:58,372 --> 01:05:06,732
Higher NRR. [laughs] Yeah, yeah. No, I, I think, like, one, one of the things, like, uh, that it could be interesting to analyze, which I don't know if you, you probably have enough data- Yeah...

469
01:05:06,792 --> 01:05:17,712
is how it changes the type of questions people ask, right? Like, o- one of my, I guess, biggest regrets is, like, let's call it I had the chance to invest in Perplexity very early on, and I didn't really get it. Yeah.

470
01:05:17,732 --> 01:05:27,232
I was like, "I'm gonna stick to my Google. I don't need an LLM call for my every search." But then, like, when you have an LLM call for every search, you ask different questions. Yeah. [laughs] Totally. Yeah.

471
01:05:27,872 --> 01:05:37,832
I'm most excited for just the, like, kind of weird, weird go-to-market ideas that people start building. Uh, 'cause I feel like that's, again, like, just there's stuff at Clay where we're not, you know...

472
01:05:38,872 --> 01:05:46,392
Uh, so I did this YC, this, like, YC analysis, and I was like, "Hey, for everyone that's not, you know, that's not currently a Clay customer- Yeah, what are they doing? Yeah... like, what, yeah, what are they doing?

473
01:05:46,432 --> 01:05:52,672
Like, why, why are they not using Clay? And it's like we're not really systematically doing that right now. And, like, we should just have the agent do that.

474
01:05:52,872 --> 01:06:01,232
Like, just tell it, like, "Hey, every week," like, "check in with Alex." [laughs] Just, "Are you not using Clay?" Do you guys have data on, like, the growth of the YC companies that use Clay versus don't use Clay?

475
01:06:01,272 --> 01:06:06,712
Oh, we should do that. [laughs] That's... I mean, yeah, we're, I mean, yeah. To try to get the ones that don't. Yeah, yeah. I'm just... [laughs] Oh, man. Yeah, that's true. That's true.

476
01:06:06,732 --> 01:06:16,172
[laughs] This is a thing that Stripe does, and I think even at Cognition we, we did this. But it's definitely self-selecting for, like, people that are more- Yeah... you know, tech native, which are going to grow faster.

477
01:06:16,552 --> 01:06:24,732
Totally, yeah. Like, it's like the... You're basically, you're basically confusing correlation with causation, right? Yeah. That's a way to get the c- [laughs]... the companies that are not on it on it, right? Yeah.

478
01:06:24,812 --> 01:06:32,272
But, like, okay, anyway. [laughs] It's, it's not just, just because you're adopt Clay doesn't mean, like- [laughs]... you will become a Clay model customer. But it, yes- Yeah... it is a step toward it.

479
01:06:32,312 --> 01:06:42,452
There is a potential. Yes, it is. [laughs] Yeah. Totally. Uh, yeah, I mean, it's almost like, I... There's probably a reason why we don't, like, really focus in on, on YC, but it's like, I don't know, why, why not?

480
01:06:42,592 --> 01:06:50,392
You know? [laughs] Like, that, that's kind of where, that's where I'm excited for, you know, the agent to just take some of these things- Yeah... and just do. Is there a, um, model capability?

481
01:06:50,452 --> 01:07:00,832
Let's say, you know, we have GPT-6 now and, you know, the, the 5.5 series sort of for Claude. Uh, let's say the next gen. Is there something that you're holding back on that you would love to build and it's not ready?

482
01:07:01,372 --> 01:07:10,872
Oh, it's a great question. You know, I, I mean, one of the things that I, just from looking through so many agent traces is, one, like, the, the models are still kind of dumb. Like, there- Yeah...

483
01:07:10,972 --> 01:07:12,972
like, so [laughs] Yeah, what's, what's an example that comes to mind?

484
01:07:13,032 --> 01:07:20,012
I can, I can obviously- And just, like, you know, like, trying CLI commands with the same inputs over and over again and just not correcting them every time. Yeah. You know, it's like things that aren't...

485
01:07:20,532 --> 01:07:27,472
It's not rocket science, but I'm like, "Oh, there's still room just even on the, the kind of basic kind of what you would think is solved." Do you have that partnerships...

486
01:07:27,572 --> 01:07:30,012
Like, I, I assume you have a shared Slack with all these guys, right? Yes.

487
01:07:30,132 --> 01:07:37,472
Can you just give them, like, a Legsmith, like, thread ID and just go like, "Hey- Yeah, I, I, s- I mean, there's, there's always an interesting relationship. Uh, yeah, we, we probably could do that.

488
01:07:37,512 --> 01:07:42,912
I think there's- Yeah. Yeah. It's a-- this is how, like, they ask for feedback, right? Yeah. They just go, like- Yeah... give me the, the feedback ID.

489
01:07:43,352 --> 01:07:54,512
But I, I do think, like, you guys as agent builders basically need your own version of that to share back with the labs, and then the more, the more powerful version of this is you wrap all your bug reports up and call it a benchmark.

490
01:07:54,612 --> 01:07:59,272
Yes. [laughs] Yeah. And then just be like- That's right... "Look, you, you guys are bad on this." Yeah, what do you, what do you think about that? I think it's good. It...

491
01:07:59,312 --> 01:08:06,452
Look, it takes a bit more work, but you could probably have, like, a grad student work on it with you- Yeah... and just go like, "Hey," like, "these are my past, like, 500 bug reports."

492
01:08:06,511 --> 01:08:13,112
Like, categorize them up, group them up- Yeah... clean them up, remove PII, and that's a benchmark, and that's a paper for you. Yeah. Yeah. Yeah.

493
01:08:13,552 --> 01:08:19,472
Uh, th- this is, like, an area where, I mean, we're, we're thinking about this. Uh, I think it's a great area to partner with companies. Like, I feel like there are companies- Yeah...

494
01:08:19,612 --> 01:08:26,732
who do this all day, and, like- Like, Sierra was super early to this- Yeah... 'cause obviously Karthik was GPT-3, and, like, they were like, "Okay," like, "these are my main verticals.

495
01:08:26,772 --> 01:08:35,472
We'll do a tail bench, uh, airline retail telecom- Yeah... and, like, please optimize for this." And, like, l- it's basically the- [laughs]... please make my business better for me. Thanks. Yeah, I mean, the...

496
01:08:35,852 --> 01:08:45,052
we, we, we do spend some time thinking about, like, what does performance in go-to-market or performance in sales look like? Like, kind of what is, you know... what would a sales optimized model look like?

497
01:08:45,552 --> 01:08:52,312
But yeah, I mean, we're, we're, we're early on. Like, we haven't looked into doing a public benchmark, but I think it could make sense. Yeah. No, I think the grad students would love to work with you.

498
01:08:52,592 --> 01:08:55,872
And look, New York has tons of them. Like, yeah, you- Okay... you'll find, you'll find somebody.

499
01:08:56,312 --> 01:09:01,092
I just think, like, this is one of those things where, like, uh, as a marketing guy, and you know, I'm primarily a marketing guy, and maybe- Yeah...

500
01:09:01,192 --> 01:09:09,212
a bit of community, maybe a bit of, like, content and, and all, all, all that, um, this achieves your goals- Mm... and it achieves the, the lab's goals.

501
01:09:09,252 --> 01:09:17,732
This is, like, a very much a win-win, uh, win in terms of community understanding of your problems too. So this is one of those things that if I can encourage you to publish those- Okay...

502
01:09:17,752 --> 01:09:24,332
kind of things, you know, it's... it, it can be high leverage. You'll get all the, uh, engineers in New York to, like, come out of their dens- [laughs]... to do that. [laughs] Yeah. Yeah. Yeah. Yeah.

503
01:09:24,752 --> 01:09:31,752
I mean, it's, it's... it is just another way of, like, forcing them to look at data and, like, do evals and label them and- Yeah... uh, which they don't wanna do.

504
01:09:31,852 --> 01:09:38,452
So you have to come up with creative ways to make them enjoy their work that they actually normally wouldn't do. [laughs] Yeah. Yeah. Uh, yeah.

505
01:09:38,572 --> 01:09:44,752
I, I do think we have a good flywheel of this internally, where, like, we have real good market engineers who- Yeah. Yeah...

506
01:09:44,852 --> 01:09:50,712
you know, spend a lot of time thinking about, like, oh, like, like how would we find pockets of customers that we should reach out to? Or like, hey, who...

507
01:09:50,812 --> 01:09:58,292
like, how would I build scoring for my customers or whatever, like, all of these things. And so have some in-house talent there, but we probably haven't connected that flywheel as much as we should.

508
01:09:58,832 --> 01:10:09,392
Um, actually, you talked about coding agents a lot. Do you have any, you know, things you want coding agents to get a lot better at over the next, you know, six months, 12 months, that would help the Clay CLI?

509
01:10:09,932 --> 01:10:16,792
Uh, y- yes, and may- maybe this connects to the question, but, like, model capability is being able to look at an agent trace and figure out what's wrong with it.

510
01:10:16,952 --> 01:10:20,612
I mean, maybe it's just, like, too self-reflective, but it still really doesn't work.

511
01:10:20,832 --> 01:10:29,352
So, like, we're, we're trying to build, you know, the, the loose forms of continual improvement, but it's not even continual improvement, but like, "Hey, here's a trace. It was really long.

512
01:10:29,972 --> 01:10:37,912
The agent probably got confused. Can you tell me where it got confused?" And I think agents are still not good at this. Like, they just are... they have the wrong intuition about what's wrong.

513
01:10:37,952 --> 01:10:43,992
They're like, "Oh, well, like, this took a long time," but just like, "No, no, that, that makes sense." They're just, like, completely wrong, I think, most of the time.

514
01:10:44,492 --> 01:10:54,912
Um, and so if, like, you try to connect it the whole way, where it's like, "Hey, just download the bad, bad traces," like, have agents look at those, and then, you know, improve those over time, uh, that just, like, doesn't work.

515
01:10:54,972 --> 01:10:59,112
I think it... You know, it is similar to, like, you know, agents writing their own prompts.

516
01:10:59,732 --> 01:11:08,892
Maybe works in some sense, but, like, if you're just like, "Hey, fix the agent performance based on this thing," that doesn't really work. So, like, I don't know, we're still handwriting a lot of skills.

517
01:11:08,932 --> 01:11:16,412
Like, we're doing a lot of stuff there, and, like, that, that feels a good tractable, solvable problem too. Uh, you guys have, uh, Sculpt, I think- Sculpt... coming up. Yes.

518
01:11:16,732 --> 01:11:26,192
Is there anything that you are going to be launching that you could potentially tease? C- clearly Sculptor. [laughs] Uh- In 10 days. Yes.

519
01:11:26,332 --> 01:11:38,412
So, uh, I do think we, uh, will launch a wh- a whole host of new features for our bet on the go-to-market engineer, and so giving them, I would say, new, new tools in their toolbox. All right. Do you have anything?

520
01:11:39,392 --> 01:11:48,652
I think... No, I, I think it's really... you've been really open about your journey. Um, I'm... I, I think, like, people sh- who, who haven't tried Clay, and honestly, I conceptually understood Clay. Yeah.

521
01:11:48,692 --> 01:11:56,692
I didn't understand the depth. I didn't understand the work that you've done. I have use cases now for, uh, my two businesses. And you know, what, what is, like...

522
01:11:56,972 --> 01:12:01,432
when you explain Clay to an engineer friend, what do you usually tell them to try? I don't know.

523
01:12:01,492 --> 01:12:11,212
I, I think it's, like, kind of the stuff that you're trying to do in go-to-market, like, I would just try asking Clay, like, try asking the agent to build that- Yeah... and, and see what happens. Yeah. See what happens.

524
01:12:11,312 --> 01:12:23,372
All right. Yes. Well, thank you so much for spending some time with us, and good luck for your, uh, big conference. Thank you so much. Yeah. Thank you. Yeah. Thanks. [upbeat music]

