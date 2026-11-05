---
type: raw
title: "Why Agents Love Supabase"
source: "https://latent.space/p/supabase/"
author:
  - "Latent Space"
published: 2026-10-28
created: 2026-11-05
description: "Interview with Paul Copplestone and Ant Wilson about Supabase Select and agent-ready Postgres. User-provided full English timestamped WEBVTT transcript; original attachment sha256 b2c9c1f5cab0bc8355a92ba8c9d1ae3102abd99d8785895e0905a2ce7835f275."
language: en
tags:
  - clippings
  - postgres
  - agentic-development
---

# Why Agents Love Supabase

Full interview transcript (WEBVTT; user-supplied, preserved with original timestamps and wording). Transcript may contain ASR errors. Canonical URL verified independently; the user-provided second link was duplicated in error.

```vtt
WEBVTT

1
00:00:00.340 --> 00:00:04.820
Hello, it's me again. I hope, uh, you're enjoying these little episode intros that we're doing.

2
00:00:05.120 --> 00:00:14.000
Hopefully, it gives me a little chance to talk to you guys about why we're doing some of these episodes and what you should look out for in the interviews so you get more out of the interviews.

3
00:00:14.040 --> 00:00:26.320
We're also adding overlays that you can see pop up to keep it visually interesting, to explain things that maybe if you're newer to the industry you don't know, 'cause I don't have time to go over every single thing while we're having interviews.

4
00:00:27.100 --> 00:00:35.060
Um, so I was at Supabase Select recently, which is the Supabase company conference. Um, and there's a lot of stuff to cover.

5
00:00:35.320 --> 00:00:46.780
Uh, in particular, I think I should share that I have a very close relationship with this company. Um, I was an angel investor in their seed round six years ago, and they were my very, very first angel investment.

6
00:00:46.860 --> 00:00:57.340
They've done super well. They went from zero to 10 billion in re- in valuation in the last six years as a fully remote open source company, which is enormous.

7
00:00:57.520 --> 00:01:03.860
Uh, and they're pretty much becoming the standard for hosting Postgres. So I want to break down what, what makes them tick.

8
00:01:04.180 --> 00:01:09.940
Um, I also want to see why they did so well in my AEO ranking, uh, because it's not g- it's not a given for sure.

9
00:01:10.460 --> 00:01:21.880
Uh, and there's a lot of, uh, companies that are fighting for, uh, what it means to build databases for agents. They were also, I think, our very, very first sponsor for AI Engineer, the very first AI Engineer in 2023.

10
00:01:22.080 --> 00:01:36.900
Um, and they're now gonna be our first sponsors for Latenz Space, uh, which, because we're open for sponsorships and, uh, you know, who else to, to do this with, with companies that, and people that I'm familiar with and trust and can explain very well to, uh, to our audience.

11
00:01:37.320 --> 00:01:47.440
And so the main things I wanted to cover, they have, they have a whole recap here on their YouTube, which is very well executed and all that. Uh, but they have th- these three themes of build, operate, and scale.

12
00:01:47.880 --> 00:02:03.440
And I think the announcements are very much what I kind of look for in a company conference keynote. Um, so build is basically how they want to improve post- the Postgres experience for coding agents to set up.

13
00:02:04.040 --> 00:02:11.420
And the, the two that I, that really shout out to me is, uh, one, one is, is very simple one is, which is they're starting Supabase without Docker.

14
00:02:11.740 --> 00:02:19.500
That, that is like the, the less weight I can, I need in order to start up basic processes to interact with the, uh, the database, the better.

15
00:02:20.120 --> 00:02:30.520
Um, and obviously I can scale it up to, to a full VM in, in the future, but... Um, the second thing is Supabase Compute, where, uh, you can run Compute next to the database. I think co-locating that is super easy.

16
00:02:30.980 --> 00:02:41.420
I think this is honestly super underrated. Um, I think is, uh, maybe underselling what it potentially could be. Um, your app having an MCP server, uh, from a Supabase library is really good and...

17
00:02:41.740 --> 00:02:44.380
But declarative schemas is so important, right?

18
00:02:44.620 --> 00:02:54.040
Like you want declarative schemas rather than the standard SQL paradigm of, uh, set up a schema and then migrate, migrate, migrate, uh, which is something we cover in the, the, the podcast.

19
00:02:54.080 --> 00:03:02.840
Like, um, if you, you want everything to be in Git as source of truth so that your agent can crawl it, um, and figure and set up and fork and what- whatever from there.

20
00:03:03.860 --> 00:03:14.760
Um, it seems so simple, but really when Postgres was not designed to do this, uh, it, you have to kind of retrofit, uh, the schemas on top of, uh, onto a, you know, 40-year-old database.

21
00:03:15.120 --> 00:03:27.280
Um, and really I, I kind of see Supabase's momentum now as doing the last mile or like the, the really like frontier of Postgres development for agents to really use them super well.

22
00:03:28.160 --> 00:03:35.900
The beauty of it though is that it's not actually about agents. It's like we just needed this the whole time. Um, so but humans also benefit and I, I really like that.

23
00:03:35.960 --> 00:03:44.180
I don't like doing own, doing things only for agents to be happy. Um, so then the second part is operate- operating. Um, so

24
00:03:45.220 --> 00:03:58.080
that is mostly just about giving more context really, whether it's more logs, more checks, more connections, uh, markdown files for your SQL. [laughs] That's super cool. Uh, knowledge and skills.

25
00:03:58.500 --> 00:04:05.500
They've-- every year they ship, uh, some interesting pipeline work from like, you know, Stripe to, to, to, to other sort of integrations.

26
00:04:05.720 --> 00:04:15.480
Um, and I think the sort of general ETL problem as you get further and further in your AI engineering career becomes, uh, you know, more and more part of the data engineering stack.

27
00:04:16.300 --> 00:04:23.380
But now Supabase has their own first party solution. You can use a mix of both, like whatever, but sometimes it's nice to have everything in one.

28
00:04:24.060 --> 00:04:33.000
Uh, the last part is, is perhaps the most, uh, complex and, and, you know, at scale thing. Uh, this is why Supabase changing their branding to Prototype to Petabyte.

29
00:04:33.460 --> 00:04:38.040
Um, and really they're going after more and more scale obviously because they're grow- the customers are growing.

30
00:04:38.280 --> 00:04:49.480
Um, and so announcing a full V1 of Multigress, which is their, uh, their sort of port I guess of Vitess for, uh, for Postgres with the Vitess guy, which is, uh, enormous in the database world.

31
00:04:49.560 --> 00:05:00.700
If you don't know what Vitess is, uh, you're losing out. Um, you, you need to know. You're, you're watching this on YouTube, uh, on a Vitess website. Um, OrioleDB and DB...

32
00:05:00.720 --> 00:05:06.820
So like there's a lot to get in there and honestly, uh, you can see my connection with the, with the founders.

33
00:05:07.360 --> 00:05:20.000
I think this is the first interview ever that the two of them have done, and I make reference to that and try to, uh, view their chemistry and show, show you what it's like to discuss and run a $10 billion database company.

34
00:05:20.500 --> 00:05:37.800
Enjoy. [upbeat music] Okay. This podcast has been six years in the making. [laughs] We're excited to have, uh, Kapul and Ant in the studio. Welcome guys. Thanks. Thanks for having us.

35
00:05:37.920 --> 00:05:47.080
Uh, we're recording this ahead of Supabase Select, which, you know, it's your, it's your big customer conference, and we'll release this after the, the conference.

36
00:05:47.500 --> 00:05:58.720
But I just wanted to sort of celebrate the journey that you guys have been on. I've seen you guys since, uh- You guys finished YC, and you were, like, in that place in Singapore where you were sort of celebrating things.

37
00:05:59.020 --> 00:06:09.240
And I, you know, I, I met you guys for the first time, and I was like, "What is this, like, hot database company that, like, got s- like, soft launch on Hacker News by, like, you know, some random user or something?"

38
00:06:09.640 --> 00:06:21.060
Um, anyway, congrats on all the, the, the success. What are you announcing the headlines at Select? Let's just get right into that. Yeah. Yeah, sure. Um, so there's quite a few headlines. We've got a lot to cover.

39
00:06:21.700 --> 00:06:35.620
The main ones would be starting off with, um, Compute. So we offer a product called Edge Functions, and Edge Functions are powered by Deno, and they have basically a two-second limit. What we're finding is that...

40
00:06:36.040 --> 00:06:44.440
Well, what we've heard from our community for a long time is that they wanna run much longer workloads. They wanna do things like chunking embe- embedding.

41
00:06:45.140 --> 00:06:53.080
So tomorrow we're announcing, and by the time this comes out, Supabase Compute, which is you can run anything. It's long-running. It's serverless.

42
00:06:53.340 --> 00:07:02.220
It is running in the same private network as your database, so it's co-located, has very good latency, so you can run Postgres connections directly from Compute.

43
00:07:02.540 --> 00:07:13.120
And you can run anything inside it, so it's no longer constrained to just Deno. You can use it with Rust or Python. You can run agents inside it. It's basically just a, a full compute instance.

44
00:07:13.360 --> 00:07:26.380
Let's call it, uh, the comparable offerings in other clouds that others might be familiar with, uh, would this be- Yeah. So something like a, a Lambda function, but, um, the container type Lambda function. Okay. Yeah.

45
00:07:26.420 --> 00:07:34.680
Okay. You can run a full container, basically. And then there's the other stuff. Yeah. And then we have, well, three dem- uh, innovations on the database space.

46
00:07:34.860 --> 00:07:38.420
So the first one, which we talked about last year, which was OrioleDB.

47
00:07:39.100 --> 00:07:46.740
OrioleDB, we've basically put it through the ringer [chuckles] in the past year to make sure that it is rock solid and ready for the Postgres ecosystem.

48
00:07:47.260 --> 00:07:56.040
The three innovations are basically, uh, performance, scaling up, and scaling out. Uh, Postgres touches on... Uh, sorry. OrioleDB touches on performance.

49
00:07:56.520 --> 00:08:09.140
It is a drop-in replacement for the c- the current Postgres storage engine, which is Heap, and it runs about a hun- 1.5 to 2 times faster, and you don't have to change anything else. It's just completely compatible.

50
00:08:09.720 --> 00:08:16.660
It completely removes the need for some of these background tasks, like vacuum and bloat, so it's actually very efficient for your database as well.

51
00:08:17.200 --> 00:08:25.880
And basically, the innovation that all the work that we had to do this year was put it through pgregress, full compatibility with Postgres, antithesis.

52
00:08:26.000 --> 00:08:37.840
We put it through TPC-C nightly benchmarks and Jepson to make sure that it basically can never lose data. So we're releasing it tomorrow in full beta, and we also made it Apache 2 licensed.

53
00:08:38.220 --> 00:08:48.560
It comes with a patent, and the Apache 2 license covers the patent. So we actually acquired the technology, continued to develop it, and then we paid for the patent and are now giving it away for free.

54
00:08:48.920 --> 00:09:00.740
One thing that you mentioned in passing, which I still don't... I can't get over, is that you tested every operator and you said, um, every operator drops data in some situation. Well, so this is for the second- Okay...

55
00:09:00.760 --> 00:09:10.740
the second one, so scaling up. I see. So that's, that's Mu- that's Multigress. Yes. So Multigress is the second big announcement. Basically, we looked at the Postgres ecosystem, and we looked at all the operators.

56
00:09:10.780 --> 00:09:20.960
An operator, for those who aren't familiar, when you run Postgres, you start with a single node, but then with almost any database, you wanna run multiple nodes, and you want things like failover.

57
00:09:21.020 --> 00:09:26.660
You want it to manage backups. So usually you have this thing called an operator which can run the entire cluster for you.

58
00:09:27.120 --> 00:09:35.200
So there's quite a few operators in the Postgres ecosystem, and what we had found was that under, um, certain conditions, every single one of them could lose data.

59
00:09:35.580 --> 00:09:42.280
And so we decided with Multigress to do a ground up rewrite of the entire structure of a, of a operator.

60
00:09:42.700 --> 00:09:53.300
And so Multigress is essentially, while our initial goal was to become or give sharding to the Postgres community, what has turned out to be is this entire operating system.

61
00:09:53.720 --> 00:10:02.800
And we actually ran it, uh, again through very rigorous testing, and we've done a thou- uh, 1,000 sequential failovers, and it didn't lose any data.

62
00:10:02.860 --> 00:10:13.740
And we've tested it in basically every way we can, clobbering it to see whether it will ever lose data. So we're very confident now in its stability, and so we're releasing that one as well tomorrow.

63
00:10:13.779 --> 00:10:24.180
It's completely open source. It will be on our platform for customers and, uh, invite only, so people who are running serious workloads can come to us, and we'll start helping them to scale up.

64
00:10:24.580 --> 00:10:33.680
Is this the full completion of Multigress being fully sort of parallel to Vitess, or is there still le- something left to go? No, actually, yeah, it was quite interesting.

65
00:10:33.740 --> 00:10:42.380
So Suku, um, originally created, uh, Vitess in, for the MySQL ecosystem, but specifically for sharding.

66
00:10:43.040 --> 00:10:57.380
And actually, when he came along, he said, "Well, the number one goal that we wanna do for this time," because we're always catching up on compatibility when we use Vitess, you always had to change things as you move to sharded, so change some queries.

67
00:10:57.760 --> 00:11:01.340
So he said, "I wanna focus only on compatibility first."

68
00:11:01.780 --> 00:11:12.980
And so the way we've designed it is in such a way, this ground up rewrite, is specifically so that we know when we release sharding, you actually won't have to change anything for your database.

69
00:11:13.160 --> 00:11:23.020
You'll continue to run the same queries, and Multigress will just be able to handle it. Zero changes to your code. I mean, that's a incredible vision, and the, the fact that you've been able to do it in two years.

70
00:11:23.700 --> 00:11:26.220
That's one year. One year. Um, so we haven't released sharding yet.

71
00:11:26.840 --> 00:11:38.520
I've seen the early prototypes and the designs for how we're doing it, and it should, should, some of it should land by probably early next year, depending on some of the things that are happening on our platform.

72
00:11:38.800 --> 00:11:46.240
We've got a lot going on. But, um, but we're very confident. We're, and we're, we're happy with the progress. It's, it's been pretty good. Yeah.

73
00:11:46.560 --> 00:11:56.480
I mean, I think this is the last piece for the total domination of Postgres. Yeah. Right? Yeah, that's, uh, that's it. And for those who don't know, you know, look up Vitess, uh, it powers YouTube, powers, what else?

74
00:11:56.520 --> 00:12:08.116
GitHub, uh, everything. Yeah. If workloads were ever to shift away from MySQL, you need this. To, to Postgres Yeah And that's then for Supabase to win. And hopefully it, it's not just for Supabase customers, right?

75
00:12:08.236 --> 00:12:15.376
Like, it's fully open source It's community things It's anyone who's- Who's involved... who's running Postgres- Yeah... at scale, um, should be able to use Multigraph.

76
00:12:15.596 --> 00:12:21.516
Yeah, I'm sure, like, every coalition, every company that's involved in Postgres in some way is contributing to this thing, right? 'Cause we all want this. Yeah, yeah.

77
00:12:21.596 --> 00:12:32.376
We've got a whole design partner program, so, um, we're working with the likes of Booz Allen, we're working with Postman, we're working with Perplexity. So yeah, lots of customers coming on board.

78
00:12:32.416 --> 00:12:43.376
They-- A lot of people need it. They're running Postgres at scale, and they need something to sc- help them scale up. Yeah. Third. Third one is, uh, yeah, so this one's a big one. Um, scale out.

79
00:12:44.256 --> 00:12:54.956
At the moment, we launch about five million databases on our platform every single month, and kinda the future where we know we're going, we think that we're going to have to launch billions per month.

80
00:12:55.296 --> 00:12:58.556
And so scaling out is a whole different beast.

81
00:12:59.116 --> 00:13:12.596
So we decided that we would have to look at some new architectures and people within the space, the agentic database space, and there's no other leading database provider who does agentic well than Turso.

82
00:13:13.396 --> 00:13:24.716
And so actually tomorrow, and when this is announced, it would've come out, where we have announced that we've acquired Turso to help us power agentic databases. Yeah, that's an incredible...

83
00:13:24.876 --> 00:13:33.196
I- it's also, like, they're, they're primarily SQLite based, but it doesn't really matter, right? Like, it's, it's more about the architecture of, like, I guess...

84
00:13:33.776 --> 00:13:40.616
I don't have the word to describe how basically, like, broadcasts, is that the word? For, for scale out, right?

85
00:13:40.656 --> 00:13:53.036
Like, um, there's the idea for them scaling SQLite was that they would have, like, a single writer and, like, multiple readers. Yeah, so, so SQLite itself, it's only a single writer. It's a file format.

86
00:13:53.136 --> 00:13:58.196
Um, so generally it's not thought of as a- Like sort of a MVCC for SQLite. Yeah, ex- exactly, exactly.

87
00:13:58.476 --> 00:14:09.536
So then they built this Turso architecture, which basically builds MVCC for SQLite so that you can have multiple writers. Yes. And then it's also- And because SQLite is, has a weird license, they had to fork it?

88
00:14:09.596 --> 00:14:16.296
They had to fork it. [laughs] They originally started with Libsql, and then they- [laughs]... they came along, and they did this other really cool architecture.

89
00:14:16.736 --> 00:14:27.656
And actually now the architecture, actually it was very commonly discussed a few weeks ago, well, on S3. So some of the innovations in the database space are actually coming out of what's happening in object storage.

90
00:14:28.016 --> 00:14:34.556
So object storage has added a bunch of new features, which basically mean that you can start using it a little bit like a, a database.

91
00:14:34.876 --> 00:14:43.136
And because object storage itself is, I think it's 11 nines of, of data- Durability... durability. Yes Then- Which is not reliability, but whatever... yeah, not reliability.

92
00:14:43.556 --> 00:14:51.156
But it, it gives you what you need for, for, um, basically what you would typically have for a cluster of databases.

93
00:14:51.536 --> 00:15:02.136
It's kind of like your cluster underneath, so you can start doing some cool things like, yeah, there's quite a few popular databases now, or data use cases that are building directly to- on top of object storage.

94
00:15:02.596 --> 00:15:05.776
It's got some limitations, um, in our worldview.

95
00:15:06.016 --> 00:15:20.476
It's probably good for these smaller use cases in terms of transactions, because when you've got a transactional database, you've gotta do a lot of reads and writes, and so in this case, you probably don't wanna be doing something at massive scale on this, and that's why we have Multigress.

96
00:15:20.896 --> 00:15:33.236
But for these, what we're seeing, where we need to get to, these billions of databases, what we need them to be is a file format. And so that's where SQLite was super interesting. King. It's dominating.

97
00:15:33.356 --> 00:15:47.976
And actually, the thing that really piqued our interest, and I reached out to Glover, h- I said, uh, he released a blog post on how they've done their rewrite, basically makes the-- we have a pathway to get Postgres compatibility with their file format.

98
00:15:48.356 --> 00:15:52.156
So we're ac- acquiring them, and we're actually gonna keep the Turso brand.

99
00:15:52.236 --> 00:16:03.256
So Turso's gonna focus on SQLite, and then we're going to introduce this new, smaller instance type on Supabase called Supabase Spark, and it'll be compatible with all our libraries.

100
00:16:03.616 --> 00:16:13.436
And you can have one database for any idea, any prototype that, that you want, and when it takes off, then you just upgrade to full Postgres databases, all the way up to Multigress.

101
00:16:14.176 --> 00:16:23.796
I know you've been working on this for a while. This is the dream, right? Yeah, yeah. There's been-- Both scaling up and scaling down has been one of the things that we've been trying to figure out how to do. Yeah.

102
00:16:24.116 --> 00:16:31.056
And it's really when some of these innovations came along that we realized, "Oh, okay, we can do this." You know, you, you're going to five million a month.

103
00:16:31.196 --> 00:16:40.596
Let's say you see on the, the trajectory of b- billions per month. One of the secrets is they're actually kind of small databases. Yeah. Right? Like, these, these things are tiny. They're vibe coded apps. Like- Yeah...

104
00:16:41.216 --> 00:16:45.856
n- like, I, I, I don't know if you have any insights on, on the, on, like, what features were- Yeah. I mean, until they get traction, right?

105
00:16:45.996 --> 00:16:51.216
And that's the thing is, like, once you hit the front page of Hacker News, you need to know that you can go far beyond that.

106
00:16:51.876 --> 00:17:01.096
Um, and so the whole idea with, with all of this was we need to make sure we've got a really smooth pathway to migrate between the back ends, like zero downtime migrations.

107
00:17:01.156 --> 00:17:12.256
It's like we, it's just, like, a, a need to have. Because, like, we see now that there's a lot of non-technical builders who are building, like, whole companies, right?

108
00:17:12.316 --> 00:17:23.976
We have the, a customer, Magic School, and the guy was, like, a teacher, right? And he saw all these, like, uh, inefficiencies in teaching, like teachers spending time that, on, on tasks that could be automated.

109
00:17:24.496 --> 00:17:36.796
And so now you have these startups that start without a technical co-founder, without a CTO, and that's not, like, isolated incidents anymore. That's, like, becoming more- Everyone... everyone's- Yeah...

110
00:17:36.836 --> 00:17:46.776
like, a bu- a builder now. Um, and that's why we see, like, the growth we've seen over the last 18 months is crazy. It's nuts. Yeah. But, but it still feels, like, early.

111
00:17:47.276 --> 00:17:55.236
And I think, um, there's a much larger market of almost, like, consumer, like, builders, right? So people- Mm...

112
00:17:55.276 --> 00:18:02.276
inside companies, people who wanna launch their own startups, which is gonna mean a lot more databases, which- [laughs]

113
00:18:02.316 --> 00:18:14.632
Like we said, it's like if we give everyone a dedicated Postgres cluster, it's probably n- you know We'll probably run out of physical computers in the, in the world pretty fast Which is basically what's happening [laughs] Yeah [laughs] Yeah.

114
00:18:15.172 --> 00:18:25.932
I mean, like, we've faced it throughout this year. Yeah We just, our growth has, uh, has been, uh, one of the things that we've had to deal with in terms of capacity of computing. Yeah. So congrats.

115
00:18:26.172 --> 00:18:34.312
Also, I will observe that I feel like Glauber is also a meme lord. Yeah. Well, that's one of the things- Right?... why we like him [laughs] I mean, like, come on. Yeah, he's amazing.

116
00:18:34.532 --> 00:18:43.552
So for those who don't know, the, the person behind the Supabase memes is this guy. Yeah [laughs] Uh, that, you know, um, low key, low key a killer- [laughs]... I would, I would say. And, well, Glauber also.

117
00:18:44.032 --> 00:18:50.432
Yeah, yeah, yeah. Big time. Uh, and he- I don't know if you guys ex- exchange notes on, like, what's funny and- Not yet, no... things like that. No. We're gonna give him- Oh, that never came up?

118
00:18:50.472 --> 00:18:57.972
We're gonna give him access to the Supabase Twitter account- [laughs]... for sure. Oh, my God I could, I could do with some help [laughs] Uh, yeah, yeah. Wait, is it still you? Uh, I...

119
00:18:58.012 --> 00:19:04.212
We've got a small- Okay [laughs]... team of, uh, teenagers now who help me out. [laughs] You do workshops, right?

120
00:19:04.372 --> 00:19:19.632
Every week Yeah, but it, it's ha- We do a weekly workshop, a meme, basically weekly meme workshop, but it's hard to hire for because you need to understand the tech and understand, like, what developers find funny, basically, in order to do that type of marketing, right?

121
00:19:20.012 --> 00:19:30.152
Yeah. Um, ac- Actually, you're, you are also low-key- Yeah... like, meme lord. I'm not as funny as you. You're really, really funny. Where's... There was one with, like, a seagull, and you were s- like, um- Ah.

122
00:19:30.152 --> 00:19:38.992
[laughs] Yeah... standing on top of the- Supabase... turtle Standing on top of Postgres, I think it was- Yeah... with a seagull Yeah, it's like a standing seagull riding a flying seagull, and it's like- There we are.

123
00:19:39.132 --> 00:19:43.572
Oh, my God. Supabase Postgres Yeah. I, I can't, I can't find it right now. Yeah, yeah But, and this is all, like, deep Supabase history.

124
00:19:43.572 --> 00:19:55.592
[laughs] But like, you know, there, there was a time when, like, those things were just like, it was so good, people wanted to be like you, and they couldn't, and that was your moat. [laughs] Like, memes. Yeah.

125
00:19:55.612 --> 00:20:05.932
And there were some big companies trying to run memes off their Twitter accounts. I won't name any names, but, like, very large organizations. Um, but yeah, it's, it's hard.

126
00:20:05.972 --> 00:20:17.412
Like I said, it's hard to hire for- The guy who did, like, a 40,000-word essay on breaking down our meme strategy Mm Someone studied our Twitter strategy, actually really early on, and posted it on, on Hacker News.

127
00:20:17.491 --> 00:20:26.012
Yeah, on Hacker News. Uh, and, and that was funny because- [laughs]... they'd recorded the strategy in a way that we hadn't committed to paper yet.

128
00:20:26.332 --> 00:20:31.652
So then when we onboarded new marketing people, we were like, "Here's the strategy." [laughs] That was written by someone else. Yeah.

129
00:20:32.212 --> 00:20:39.372
And of course, Hacker News hated it, and then they were commenting on it, and- I found it. I found it. I found it... Ant took the, uh, the first comment This guy, this guy, this guy.

130
00:20:39.432 --> 00:20:47.432
Yeah, yeah "Learnings from four months of Supabase feed." He just looked at your work for four months. When was this? 2022. Okay. Yeah, yeah, yeah. Wait. I m- I, I mentioned it? Ooh, okay.

131
00:20:47.452 --> 00:20:56.732
There you are So he just broke it down He broke it down. [laughs] And then Hacker News hated it, on it, and so Ant took a photo of them shitting on it and posted it on our Twitter account.

132
00:20:57.132 --> 00:21:09.012
[laughs] [laughs] Yeah Your hate just fuels me. What is this? Uh, interesting article. Yeah, okay, so I commented. [laughs] Yeah. Yeah That was like, a lot of our growth was thanks to Hacker News.

133
00:21:09.072 --> 00:21:18.972
I mean, i- in the early days, I just- Yeah... had to live on there and- So we should talk about that. What deal with the devil do you have to do with Dang, uh- Oh, man... to- We, we've been scolded- [laughs] Yeah...

134
00:21:20.492 --> 00:21:31.852
by Dan G, like, many times- We have... like, for l- for launching too many things in a week- Yeah... basically. And he's, like, rightfully paranoid about the association of Hacker News- Yeah... and YC.

135
00:21:32.292 --> 00:21:43.172
Yeah So he kind of like, if something happens, he kind of wants to throw us under the bus so that- Yes... he, people know, oh, we're not doing this for YC customers. We're an independent site.

136
00:21:43.232 --> 00:21:54.672
So he's been helpful to, uh, make sure that we, we don't smear the name of, of YC- YC... or Hacker News. I mean, at this point you don't need them. But, like, for sure, I think, uh, Dang does a...

137
00:21:55.052 --> 00:21:58.892
Dang has super high credibility. Yeah No one, no one really, like, you know, uh, questions him.

138
00:21:59.292 --> 00:22:12.152
But I, I do think, like, you know, you guys innovated the strategy of launch weeks, and for a while, I think there was one of the launch weeks, I think four or five, where every single launch was n- like, number one or page one on Hacker News.

139
00:22:12.432 --> 00:22:17.472
I got told off so badly for that because I- But what-... tweeted that proudly. I was like, "Oh-" Yeah... "here we are." So what?

140
00:22:17.472 --> 00:22:27.572
And then I got told off 'cause, uh, we were, like, it basically looks bad because- [laughs] Yeah... because, like, suddenly this YC company is, like, dominating the front page of Hacker News.

141
00:22:27.612 --> 00:22:32.772
It looks like it's a biased thing. And, like, parading the fact- Parading... that you're on the front page. Yeah, yeah, yeah. It's just great. Yeah, yeah Which is true.

142
00:22:32.812 --> 00:22:40.592
Like, so, like, tip to anyone: Never screenshot the fact that you're on the front page- Yes... of Hacker News and put it on Twitter because it's, it does look like we're...

143
00:22:40.652 --> 00:22:50.312
And, and to be honest, it, it was gloating, so, so it's a fair, fair call-out. Yeah. Yeah. There's all that, which, like, I would say, I would cons- consider that somewhat ancient history now. You know- Yeah...

144
00:22:50.352 --> 00:22:59.092
it's been a few years since, since this was a relevant thing. But for those who don't know Supabase history, these are the things that you must check off as, like- [laughs] Yeah... the, the tour of things. Sure.

145
00:22:59.112 --> 00:23:08.292
What else? I mean- I, I think that the, the top post there is interesting because- This is the launch post... yeah, but, but it was someone else who launched us. Yeah. Vicky. Like, we weren't ready. Yeah, yeah, yeah.

146
00:23:08.332 --> 00:23:17.612
We weren't ready to be launched on Hacker News. And you didn't consider yourself a Firebase alternative. Oh, yeah. So that was the day that we changed the tagline. We had the tagline- What was the original tagline?

147
00:23:17.732 --> 00:23:19.032
It was real-time Postgres- Ah...

148
00:23:19.072 --> 00:23:33.512
because what had happened was I wanted, like, we, we were like, "Oh, let's build a Postgres company," but in my previous company, I had to migrate from Firebase to Postgres, but I needed a real-time f- feature, and so I ended up building this real-time engine on top of Postgres.

149
00:23:33.792 --> 00:23:41.752
And so we thought, "Oh, that's the killer thing. Like, it's getting some open source traction. This real-time engine is kinda cool." So we were like, "Oh, real-time Postgres." No one cared.

150
00:23:42.172 --> 00:23:49.732
No one cared when we had a website, and so, like, we were like, "Let's change it to open source Firebase alternative," knowing that that was the reason why I switched.

151
00:23:50.232 --> 00:23:56.852
And it was, I think, only 12 hours later or something like that- Yeah, yeah... that this article went up. Yeah Yeah. Still the top of all time.

152
00:23:57.212 --> 00:24:13.156
And at the time, we were s- running on top of DigitalOcean, and every new database was two droplets. So two $5 a month droplets. [laughs] Why two? Um, one for the, uh, database and one for the APIs. [laughs] Right.

153
00:24:13.376 --> 00:24:19.756
Because we- 'Cause we wanted to upgrade the APIs and decouple- Independently, yeah. And we only had a handful of, like, test users at that point. Yeah, yeah.

154
00:24:19.776 --> 00:24:28.236
And then all of a sudden we were- I think we only had eight users. Yeah. We went from eight to eight hundred on that, that launch alone. Yeah. And then we burned through...

155
00:24:28.276 --> 00:24:34.436
I think we had, like, 10K of Digital, uh, Ocean credits, which we just burned through in basically 48 hours.

156
00:24:35.036 --> 00:24:43.856
Um, and then we'd just gone into YC, so AWS was like, "Oh, we'll give you," you know, whatever it was, "150K in credits if you migrate to us."

157
00:24:44.236 --> 00:24:53.656
And so we spent the first week of being in YC migrating 800 databases to a different cloud, which, you know, if you've ever migrated one database, you know how painful it is.

158
00:24:54.116 --> 00:24:58.856
It's like migrating 800 is not how you wanna spend your first [laughs] week in YC. That's crazy.

159
00:24:58.896 --> 00:25:10.896
Do you remember that we could have been on Digital-- Like, bas- basically, we should still be building on DigitalOcean, 'cause when you get into YC, they have this credits program, like, huge number of credits f- on DigitalOcean at the time.

160
00:25:11.456 --> 00:25:18.536
And we're like, "Hey, can we have these credits? Because we're, like, we're blowing up here." And they said, "Oh, no, you've already used the $10,000 credit program.

161
00:25:18.956 --> 00:25:28.276
We can't give you this other one for three hundred thousand." So we're like, "Well, we have to migrate to AWS." [laughs] And so the biggest lost opportunity of DigitalOcean ever- Being too strict, yeah...

162
00:25:28.396 --> 00:25:35.176
didn't-- I know our bills with AWS now, this is, like- Nothing... probably one of their biggest customers ever that they lost- Yeah... from being too strict about that.

163
00:25:35.176 --> 00:25:45.756
But because it was COVID, it was a time when everyone was worried about, like, what's- Yeah... gonna happen. True. So I think they were like, "We don't wanna overextend ourselves." Um- It's fair. Yeah. Yeah.

164
00:25:45.916 --> 00:25:53.936
So it was, like, totally fair at the time, just given the, um, the way the world was looking. People made many irrational th- uh, decisions during COVID. Yeah. But you never know.

165
00:25:54.236 --> 00:26:04.316
I was gonna say, uh, y- you might be worth more in DigitalOcean now, but then somehow DigitalOcean has also, like, gone on a super tear. Ah, cool. Look at this. Because computers- True, true, true.

166
00:26:04.356 --> 00:26:12.936
They tripled, they tripled in the last year. Wow, that's cool. Wow. So what are they, 16- They're 16 billion now... billion, yeah. Epic. Okay. Uh, and like, and like, uh, okay, well, I guess there's a shortage of CPUs.

167
00:26:12.996 --> 00:26:23.596
Yeah, there's a shortage. [laughs] How are you guys experiencing it? [laughs] We literally... I mean, we're up against runways all the time where, like, we meet AWS, like, multiple times.

168
00:26:24.116 --> 00:26:32.136
Is there a way to spike when you have a spike? Or what do you do? Like, you, you just have agreements with people to- Yeah, we've gotta, like, plan- You just pay more... very closely. Yeah.

169
00:26:32.136 --> 00:26:39.196
We, we pay more, we partner with them. And in fact, tomorrow as well, we're announcing that we're bringing on a new investment partner, which is CapitalG.

170
00:26:39.356 --> 00:26:50.716
CapitalG basically has access to the Alphabet ecosystem, good for us on both sides. Like, we now have to consider a multi-cloud strategy. Meaning GCP. We need GCP, or we need more compute, basically.

171
00:26:50.776 --> 00:26:58.956
So GCP is a very obvious choice, and of course, we wanna partner with all the AI labs as much as possible. And so they have a suite of products.

172
00:26:59.116 --> 00:27:04.016
We work with them already on Gemini, and we wanna make sure that we're embedded deeply into all of their products.

173
00:27:04.356 --> 00:27:14.576
And that's another thing where you're mentioning how so much of the database ecosystem is being shaped by block storage and all these innovations and all these things. Clearly, AWS is, is, is the leader there. Mm-hmm.

174
00:27:15.096 --> 00:27:24.096
It's hard to be multi-cloud if you're gonna use GCS as, like, a swap for S3. Yes, as long as they've got the features. Actually, I don't know if their object storage has the,

175
00:27:25.076 --> 00:27:33.816
all the features, but I'm sure that, like, whatever S3 do, others follow, so... [laughs] I re- I still remember, I think, like, three years ago, they introduced, like, strong consistency.

176
00:27:34.016 --> 00:27:42.136
Yeah, that's the innovation basically that- Right... that helps. Yeah. And they just, like, they did it for free, and then- Yeah... just rolled it out to everybody- Yeah, yeah... and it's like it's live now. Yeah. What?

177
00:27:42.156 --> 00:27:47.636
[laughs] Yeah, yeah. And then S3 Express as well, that was a big game changer, um, because- Why?

178
00:27:48.056 --> 00:27:58.476
Well, basically now what you wanna do is, like, you typically write to a local drive, and then you need to batch it to something more durable. And that batching process, um...

179
00:27:58.756 --> 00:28:09.336
And so the write times to this are one to two milliseconds. And so before you can guarantee a write back to your client, you basically need to batch it to something that's durable.

180
00:28:09.396 --> 00:28:17.796
So this one's durable, not as durable as S3, not 11 nines, but durable- Good enough... enough that you can f- It's ef- ephemeral durable. Yes, exactly.

181
00:28:17.836 --> 00:28:27.735
And then, then in the background, you take, you take-- you use this kind of as your cache, and then you move into S3 in the background, which is cheaper. So you don't-- do we need Redis anymore?

182
00:28:28.576 --> 00:28:38.136
Uh, yes, yeah, you still need Redis. [laughs] Like, this is no, nowhere near fast enough. You need, like, basically, your cache layers are either memory, NVMe drive, um- Interesting...

183
00:28:38.176 --> 00:28:47.976
locally attached to S3, their equivalent, and then S3. Yeah. Normal. Amazing, amazing. That was a little bit of databa-- Like, we, we jumped around quite a lot- Sure. [laughs]... uh, clear business memory.

184
00:28:48.296 --> 00:28:56.496
Uh, a few more things that we're gonna talk about. You, you... your slogan was build in a weekend, scale to millions, now we're prototype to petabyte. Just-- Which is excellent.

185
00:28:56.916 --> 00:29:05.756
And really it is reflective of the evolution in scale that you guys are doing, right? Yeah. Do you have anecdotes on, like, let's say, early Supabase versus now?

186
00:29:05.976 --> 00:29:15.156
How fast are people scaling when they, when they start a thing? Yeah. Well, the big thing is, um, I think how fast people are monetizing. Oh, yeah.

187
00:29:15.236 --> 00:29:21.176
At, at the start it was like you choose your database, you build your product. At some point, you, um, add in billing.

188
00:29:21.616 --> 00:29:32.456
Now, because you can add in Stripe, like, at the agentic layer, it's like we see customers starting a project and within the same week, like, generating serious cash. Yeah.

189
00:29:32.496 --> 00:29:42.516
And, and in the early days of vibe coding, it wasn't obvious to us that this is something that's gonna stick around, this is gonna change the way software is built.

190
00:29:42.916 --> 00:29:52.036
But as soon as we saw someone earn, um, like, I think it was $10,000 within the first few days of launching their product, we were like, "Wow, this is, this is real." Yeah.

191
00:29:52.056 --> 00:29:54.396
People are making real things that generate real money.

192
00:29:54.876 --> 00:30:15.200
Um, so we knew we had to lean in, in, in a way where there was waves we'd ridden successfully in the past, like when NFTs were huge, we leaned in a bit and we added, like, sign in with Ethereum and sign in with Solana, um, but we didn't dedicate, like- Tons of dev time because everyone kinda knew it was gonna go away at some point.

193
00:30:15.600 --> 00:30:28.600
And making that decision for, for vibe coding was like, you know, we, we discussed it a lot as a team of how much do we lean in? And it was a time when we knew we needed to go slightly more upmarket.

194
00:30:28.800 --> 00:30:36.620
Like, our biggest customers were, like, stretching the limits of, of what we had at the time. And so we knew we had to then just do both.

195
00:30:37.060 --> 00:30:47.340
It was like, you know, um, innovate on the, on the small, like, prototype stuff and innovate on the, on the much larger side as well. And then you just need more people for that, so, [chuckles] right.

196
00:30:47.380 --> 00:30:57.960
That one's funny because, like, on the numbers side-- B-basically, for Supabase, there's been three chapters of AI. So the first chapter was, um, embeddings. I think we were on- Supabase Vector. Yeah.

197
00:30:58.240 --> 00:31:05.540
Which I have now transcribed, and it will always, uh... We, we, we should probably update this 'cause, uh- Yeah, yeah. It's probably super- This is the only talk you've ever done at AI. [laughs] Yeah.

198
00:31:05.560 --> 00:31:12.540
[laughs] We did this talk. Uh, basically, all these embedding databases were coming out, vector databases, create the vector.

199
00:31:12.700 --> 00:31:22.620
And so we were pushing the fact, and you can use Postgres as a vector database, and Andrew Kane, a, a completely independent guy, has developed this awesome extension.

200
00:31:23.080 --> 00:31:29.900
And we're like, "Okay," trying to educate the market. Postgres can kinda do anything. You don't need another database if you're gonna store your own embedding.

201
00:31:30.000 --> 00:31:40.720
So this was chapter one, and it was, it was really a, a good growth driver for us, uh, and also good for the Postgres ecosystem, just letting people know. Now there's a lot of innovations in, in embeddings.

202
00:31:40.960 --> 00:31:49.480
What Turbopuffer, for example, are doing, they use a lot of the innovations that Turso are doing, and I think it's a phenomenal use case for that type of stuff. So that was chapter one.

203
00:31:49.880 --> 00:31:58.980
Chapter two was, like, the vibe coding wave, whereas Lovable, Bold, all of these ones coming along. That was end of twenty twenty-four, and that's where we debated a lot. "Hey, do we really wanna be there?

204
00:31:59.420 --> 00:32:08.040
Do we wanna be servicing these? Do we even wanna have our own vibe coding type platform on top of Supabase?" But in the end, like, our mission is store the world's data.

205
00:32:08.640 --> 00:32:17.600
And to do that, we, based on our tagline, it's like, be there when you're getting started, make sure that they never wanna leave. And so we saw people were getting started.

206
00:32:17.800 --> 00:32:24.020
They were doing toy things, but still, it fit our mission. We just had to believe that over time, these tools would become better.

207
00:32:24.580 --> 00:32:37.700
And then the third one, which is the, like, crazy numbers, start of this year, the models just got better, basically. And then we started seeing our top of funnel, our, our sign-up rate start rapidly increasing.

208
00:32:38.060 --> 00:32:47.200
But usually when this happens, you're pouring a lot of dollars into marketing. Mm. We actually barely spend any dollars on marketing, and, uh, most of it's just memes and things like that.

209
00:32:47.200 --> 00:32:51.320
[laughs] So, um, so- Here, I got, I got one of your charts. There we go. Yeah.

210
00:32:51.360 --> 00:32:57.600
I mean, all, your, all your charts look the same, but because they're just, like- [laughs]...exponentially keep scaling- Super weird...you just keep, you just keep- But-... changing the Y-axis...

211
00:32:57.600 --> 00:33:07.520
the other crazy thing about this is, is often when you get, like, more consumer life traffic in the top of funnel, your activation and conversion to pay goes down. Yeah. But both of those things went up.

212
00:33:07.660 --> 00:33:16.120
Started going up quite rapidly as well. Yeah. Yeah. Because of the model. How do you know activation and conversion to pay? Oh, your-- at Supabase's. Our, our metrics, yeah. Ah. Our funnel metrics. Okay.

213
00:33:16.220 --> 00:33:26.560
Um, and, and the reason is because the sign-up to activation, the agent does it for you- Yeah... like in one step, so it, it's basically a hun- it's almost a hundred percent- The friction's gone... of people who convert.

214
00:33:26.620 --> 00:33:37.920
Yeah. Um, and so those users then were converting to pay at a higher rate than our traditional developer user. Okay. I mean, excellent. It's great. Yeah. Great. Thanks. [laughs] Good.

215
00:33:38.040 --> 00:33:47.100
Uh- But, but I'm sure, but I'm sure, I'm sure, like, like all developer tools are seeing the same- Yeah... thing, right? Well, at, at different rates. I think you guys are clearly one of the, the leaders there.

216
00:33:47.140 --> 00:33:56.420
You know, I was gonna bring out this, one of these, these things. I have this AEO tracker, uh, where, you know, if you, if you type in Supabase and there's a, there's a few categories where you're the leader.

217
00:33:56.880 --> 00:34:04.500
Uh, but basically it l- has led to every single frontier model recommending you as your primary choice for an integrated backend. What does integrated backend mean?

218
00:34:04.600 --> 00:34:12.260
It, it is your original offerings, like your, your auth, your, uh, functions, your, you know, um, and your database and, and all the other stuff, uh, APIs.

219
00:34:12.800 --> 00:34:18.600
And I think it is interesting, like you had to be in the market for three to four years, exactly your- Yeah...

220
00:34:18.660 --> 00:34:30.360
time zone before LLMs took off, and then present yourself as the leading competitor to the leading thing at the time. Yeah. And then to-- you can take over. Yeah. Yeah, yeah. [laughs] We're very lucky with our timing.

221
00:34:30.360 --> 00:34:34.160
[laughs] I mean, we couldn't have timed it better. Like it was a complete accident.

222
00:34:34.540 --> 00:34:43.160
Well, I mean, I think like on first princil-principles basis, so we have interviewed other founders who maybe started post-LLMs, and Resend was kind of their...

223
00:34:43.420 --> 00:34:54.320
I mean, we've also talked to them, like, "Why does my LLM keep recommending Resend?" And it's because they have a, a lot of good AEO practices. Sure, yeah. And of course, we invest very heavily in that.

224
00:34:54.360 --> 00:35:03.440
But, you know, when-- w-we've been at that point since the start, and that was an accident, right? So now we just need to maintain that lead. And community as well, right?

225
00:35:03.660 --> 00:35:17.620
Like our, one of our growth strategies early was just, was to spend to- so much time with the community, and it resulted in they were writing blog posts, they were making YouTube videos, they were putting out podcasts all about how to use Supabase, in what situations.

226
00:35:17.660 --> 00:35:25.260
Like, "Here's how I built this thing." I'm sure that all just got slurped up by the- Yeah... the models. And open source helps as well, of course. Yeah, yeah, yeah. Definitely. Being, being open source.

227
00:35:25.520 --> 00:35:33.300
Uh, you actually had a fun announcement on the community side because you're raising so much, and you're trying to involve your community in some, in, in, more deeply. Yeah.

228
00:35:33.360 --> 00:35:38.400
So, so last year at Supabase Select, we announced that we were gonna do a crowdfunding round.

229
00:35:38.440 --> 00:35:44.400
It's something we've always wanted to do, and we should have done it much earlier on, but we just, you know, had so many other things going on.

230
00:35:45.080 --> 00:35:57.820
And basically then we spent the last year fighting with the lawyers who are saying, you know, for the number of people we wanna be involved, there is no mechanism to do it without people being accredited investors.

231
00:35:58.320 --> 00:36:07.180
Until we asked them the question, "Well, what if they don't invest? What if we just give them the stock?" [laughs] And they were like, "Yeah, we'll look into it."

232
00:36:07.220 --> 00:36:12.800
And then they came back, and they were like, "Actually, there is a mechanism [chuckles] where if you really just wanna give the stock away, you can."

233
00:36:13.300 --> 00:36:20.480
And so now we've earmarked, like, um, a million dollars in Supabase stock that we're basically gonna give to a bunch of the community members.

234
00:36:20.820 --> 00:36:29.300
The first community member we're, we're gonna stand up on stage and sort of announce is, is this guy, his name's Gary Austin in the Supabase Discord.

235
00:36:30.320 --> 00:36:43.560
And this guy's, like, a legend of the Supabase community Yeah He-- We looked into his stats, and Gary has answered, uh, 20,000, in the last six years, 20,000, uh, questions in the Supabase Discord.

236
00:36:44.220 --> 00:36:57.620
And the crazy thing is 13,000 of them he answered within the first hour of them being asked. Hmm. And he's not a Groq bot. Like- [laughs]... he's a real human. [laughs] Yeah. Have you met him? What, what does- Yeah.

237
00:36:57.640 --> 00:37:06.900
We- What does he do? He's real. We, we have met him. He, he was basically, like, retired- Yeah... and just interested in Supabase. Gary Austin. Gary Austin. Or Gary Abbott? Yeah, Gary Abbott- Yeah... is his real name.

238
00:37:06.940 --> 00:37:16.620
Okay, this guy. Yeah. [laughs] Yeah. Okay. And, and he loved Supabase because he basically built his own som- sommelier, um, app 'cause he loves red wine. Mm-hmm.

239
00:37:16.960 --> 00:37:22.020
Um, and then was just getting a kick out of, you know, he's got the Supabase logo on his Christmas tree.

240
00:37:22.040 --> 00:37:30.440
[laughs] And he's also, like- By the way, this is my favorite Supabase memes, like, just, like, you reminding me that, like- [laughs] Yeah... I'm about to run out of my Supabase.

241
00:37:30.840 --> 00:37:41.660
That's the announcement is we're basically, like, um, anyone who's a, a legend in the Supabase ecosystem we can now- Yeah... um- Is Discord still a strong... I mean, I, I got mixed feelings about Discord.

242
00:37:41.720 --> 00:37:51.900
It, it is, it is the best chat. You know, Slack sucks. But also it is not public, right? So all the work in there is- Yeah... not scalable. Yeah. Have you found anything to solve that?

243
00:37:52.140 --> 00:38:03.400
There was some tools that we looked at, uh, in the early days. We, we decided not to do it because you still needed to police, like, what things you wanted to be public and, and what things you didn't.

244
00:38:03.820 --> 00:38:13.040
But the original debate that I remember we debated a lot was, okay, we wanna host the community. Do we do a Discord? Do we do a Slack community? Do we do a Reddit?

245
00:38:13.580 --> 00:38:24.060
And we tried a few different options, but we landed on this thing of, like, Discord users are gonna use Discord, Reddit users are gonna use Reddit, and we basically had to do all of the above. Just be where they are.

246
00:38:24.140 --> 00:38:31.920
Yeah. And be where they are, yeah. That's the answer. Which there was a lot of work. [laughs] Yeah. And it worked out, right? I mean- But-... that was the right answer...

247
00:38:31.940 --> 00:38:42.220
but then there's a lot of, like, great tools that started popping up, right? Um, Orb- I don't think anyone has la- has, uh, s- stood the test of time, let's call it. No. Um, but yeah. There, there- But, but it helped...

248
00:38:42.220 --> 00:38:52.140
there are, there are tools that are Discord mirrored to public Q&A site. That is a thing that people do. Mm-hmm. I don't know if it's been successful for anyone. Yeah. Yeah. And, and, like, Common Room, um, helped a lot.

249
00:38:52.140 --> 00:39:05.820
Actually, the only thing that we did was for ourselves. So basically anyone who had asked a legitimate question on any one of these, we then would basically scrape the question and the response into our own website.

250
00:39:06.060 --> 00:39:16.480
No, actually, we scraped it kind of into GitHub Discussions- Mm-hmm... and mirrored that onto our website. And so the content that was getting slurped up- Ah, used GitHub as a CMS. Yeah, we used it- Yeah... as a CMS.

251
00:39:16.540 --> 00:39:26.140
Exactly. Yeah. It was a great strategy because everyone-- Ultimately, everyone was asking the same questions over and over again. So we were just- It is true... like, "Okay. Well, we'll surface it each time." Yeah.

252
00:39:26.460 --> 00:39:32.240
It can be confusing because there's Gith- uh, there's Supabase, the open source- Mm-hmm... and then there's Supa- Supabase, the cloud platform. Mm-hmm.

253
00:39:32.820 --> 00:39:41.800
And s- and most people are probably gonna come into support for Supabase the cloud platform. Yep. So yeah, it is. Yeah. Do you have any idea of your, uh, uh, uh... This is very hard to tell.

254
00:39:42.160 --> 00:39:53.840
Your open source market capture. So, uh, this is a thing that, like, if you're in the developer tools circles, you, you know. You do? We, like, quite deliberately do not- Don't know... so- Yeah...

255
00:39:54.740 --> 00:39:58.820
we don't put any tracking in our open source offering. You can use it.

256
00:39:58.980 --> 00:40:10.080
And we've had enterprises, large pharmaceutical companies, for example, come to us and say, "Hey, we're running 100 instances of your open source project. Can you offer us a product?"

257
00:40:10.140 --> 00:40:21.100
So we've got this product called Control Tower, which allows enterprises to have-- monitor a fleet of databases. You won't find it on, on our website, but it- Oh, come on. Yeah. [laughs] Why not?

258
00:40:21.100 --> 00:40:30.180
'Cause it launches- [laughs] Oh... tomorrow. Tomorrow. [laughs] Oh, okay. Okay. I don't know if we're announcing it tomorrow, but yeah, basically, it's Control To- it-- All it does is, it's this fleet view.

259
00:40:30.600 --> 00:40:39.060
We've got this very popular product, Supabase, for platforms, so that's what all these AI companies are building on top of. We launch millions of databases for them.

260
00:40:39.560 --> 00:40:51.040
And so all we needed to do was repackage this for enterprises, and enterprises as well want to do the same thing, which is they wanna spin up many- Internal Supabase... many internal Supabase for all of their users.

261
00:40:51.320 --> 00:41:03.020
They wanna see and administer them. And so Control Tower is essentially a repackaging of what we've already been developing for these platform pro- providers, except specifically for, for individual enterprises.

262
00:41:03.220 --> 00:41:13.040
Yeah, I do wanna cover, because I think a lot of people think of you as bottoms up GTM, uh, you know, what the work you've been doing on the, on the enterprise side. Mm-hmm. Uh, so first of all, shout out to Wenbo. Yeah.

263
00:41:13.060 --> 00:41:21.060
[laughs] I, I think this is your most successful recent launch, which is- Uh, Supabase for platforms. Yeah. This one launched in... Yeah. Yeah, yeah. I mean, December 2025, so yeah.

264
00:41:21.100 --> 00:41:27.920
Uh, yeah, but- I saw some stats or, like- Yeah, yeah... you, you guys call this successful, I don't know. Yeah. Um, what is the enterprise side, right?

265
00:41:27.960 --> 00:41:38.480
Like, what, what are-- What is that story apart from, like, give me a dashboard? Well, first of all, we should talk about sales strategies. Okay. So Supabase is a very famously P&G company.

266
00:41:38.580 --> 00:41:52.040
[laughs] Like, we give a shit about... We have 60% of every YC batch use Supabase. We focus almost all of our attention on this, like, becoming an index company. Basically, our role model here is Stripe.

267
00:41:52.180 --> 00:42:01.720
We wanna follow in their footsteps. They're one of the only developer tools that we've ever seen that has withstood more than a decade of moving our market and still keeping that developer love.

268
00:42:01.820 --> 00:42:11.340
So that's the first thing. So to do that, all we started doing when we did sales was layer on what we call product-led sales. So we look instead for, like, product triggers.

269
00:42:11.380 --> 00:42:22.400
It could be, like, a, a logo, someone who we think is really important, but more importantly, they could be scaling up. They could be hitting some limits, having some errors, paying a certain amount.

270
00:42:22.480 --> 00:42:32.300
We've got a bunch of these triggers, and then AI came along, and we're like, "Oh, we can do some interesting stuff from this." So let's say we have 1,000 product triggers every single week.

271
00:42:33.232 --> 00:42:45.752
We send off a thousand emails to people who are having problems, and say five hundred of them respond. We take the cohort who don't respond, and we use them as a control group. Okay. And we measure how much they grow.

272
00:42:46.252 --> 00:42:56.132
Turns out they grow twenty-five percent m-month over month. Then we take all those who do respond, and we say to our sales team, "The only thing you need to do is get on a call with these people and help them."

273
00:42:56.612 --> 00:43:02.512
And because we've got all their traffic patterns, we can give them a script, we know what their problem is. AI's been great on this.

274
00:43:03.212 --> 00:43:11.272
And, uh, we give them a script just to help out, and it turns out just getting on a call and helping people out, their account then grows a hundred and twenty-five percent.

275
00:43:11.652 --> 00:43:16.432
So that a hundred percent uplift, the incremental uplift, is what we compensate our salespeople.

276
00:43:16.812 --> 00:43:22.592
Traditionally, you would say, "Get on a call with th-these people and just sell them shit," and s- then you get the full quota.

277
00:43:22.832 --> 00:43:34.612
But because we know our database grows, our platform grows at twenty-five percent month over month on this cohort of users, then we know that our sales force are adding this one hundred percent incremental uplift.

278
00:43:35.112 --> 00:43:43.012
So that's how we do our sales function. It's always focused on these logos or very specific, uh, product needs.

279
00:43:43.372 --> 00:43:54.852
So yeah, the likes of the enterprise is usually coming in because they're wanting to launch lots and lots of databases, or almost never it'll be a transfer of their production database.

280
00:43:55.312 --> 00:44:08.612
So migrating databases from, say, MySQL to Postgres or from, say, one scalable database to another scalable database almost never happens. And that was the core thesis of Supabase at the start.

281
00:44:09.092 --> 00:44:20.712
We knew that every single Postgres company we had looked at or database company we had looked at in the past that had tried to do migrations had failed over time. You just can't convince people to migrate.

282
00:44:20.872 --> 00:44:29.852
Even if you build a bigger, better, more scalable Postgres, what you have to do is land with them on day one and then make sure that they stick around to day one thousand, day ten thousand.

283
00:44:30.252 --> 00:44:42.572
So all of our focus is winning these enterprise logos on, on day one. Greenfield. Greenfield, yeah. They're still not migrating? I guarantee they'll almost never migrate. Wow. There's a cohort that will need Multigress.

284
00:44:42.892 --> 00:44:55.992
We talked to some logos who are looking at using it open source. They're very interested on making sure that, um, they can basically help us direct because they're running into problems of Postgres at scale.

285
00:44:56.532 --> 00:45:08.352
But for the next, say, five years, almost all of our focus on the enterprise side is making sure that we can handle greenfield use cases, which now in the enterprise it turns out to be a very- Hmm...

286
00:45:08.352 --> 00:45:20.452
prolific use case because they want all of their product people to be developing, innovating as much as they can. So again, it's kind of perfect timing for us because that's what we've been focused on for so long.

287
00:45:20.552 --> 00:45:30.232
This control tower is, like, one of our biggest things. Multigress of course gives us the, the opportunity to win these large workloads if and when they want to ever migrate.

288
00:45:30.572 --> 00:45:40.672
But it won't ever be one of our core focuses, or at least not for the next, say, five years. We're gonna have to focus really heavily on just landing inside these enterprises and then expanding up.

289
00:45:41.032 --> 00:45:50.652
The other thing that's changed is we obviously put in the past all of our focus into developers. So it was like selling to the developers, enable them as a champion, they help you sell internally.

290
00:45:51.392 --> 00:46:08.072
Uh, interestingly now we have like CPOs who are like, "Wow, I didn't code for the last ten years, but now because of Lovable and Supabase, I'm building all these things internally," that we now have like champions at the, at the C level and without needing to put like a huge motion around that.

291
00:46:08.332 --> 00:46:11.352
Oh, that's great. Yeah. Mentioning Lovable, mentioning Bolt.

292
00:46:12.032 --> 00:46:21.632
Lovable is gonna have their own database stuff, you know, and, and like everyone is gonna basically try to intrude on, on the, each other's turf, uh, which is normal in, in the, in the grand scheme of things.

293
00:46:22.152 --> 00:46:32.352
Which is more sticky? Which is more sticky? More s- more sticky. Like is the CPO more likely to be married to Lovable or married to Supabase? You know, like- Ah, okay... is, is that a question that comes up or?

294
00:46:32.352 --> 00:46:41.912
That's a great, that's a great question. I think ultimately running databases is very hard. Fair enough. [laughs] Well, and, and as we just discussed, it's harder to migrate your database than it is your- Yeah, yeah...

295
00:46:42.032 --> 00:46:46.932
front-end tool. Yeah. Um- Yeah... not that I don't think Lovable is sticky. I think it's amazing.

296
00:46:46.972 --> 00:46:55.492
And actually, they were the first people to do a really good job of making sure their agent didn't do stupid shit with, um, the database.

297
00:46:55.872 --> 00:47:06.972
Because we had, uh, very early on the agents were like trying to shove image data into Postgres. You know, they were turning off RLS in order to get [laughs] their projects to work. Hmm.

298
00:47:07.332 --> 00:47:17.392
Um, by paperclip maxing basically, is that Lovable wrote really good skills to stop their agents doing stupid stuff. They were, they were the first. That's the secret sauce. Yeah, yeah. Yeah.

299
00:47:17.432 --> 00:47:26.032
Is to, to solve all these- And, and, and now like the models themselves don't do that stupid stuff anymore. Yeah. So it's, it's, the situation has improved a lot.

300
00:47:26.072 --> 00:47:38.692
It's gone from like, um, Will Smith eating spaghetti circa, you know, 2022 to Will Smith eating spaghetti in 2026. Yeah. Yeah. Yeah. Um, and that's a, that's a famous meme. [laughs] Uh, talking about...

301
00:47:38.752 --> 00:47:45.392
Uh, I'll, I'll leave the migration point alone after I mention this. You know, one of the things that I got like a big aha moment was when I met Karen from Co2- Yeah...

302
00:47:45.392 --> 00:47:55.612
who's one of your board members, and she said, like her thesis is whole, like, you know, you are not just, uh, replacing Firebase, you're also like, you know, coming off as like new, new RDS, right? For- Mm. For Amazon.

303
00:47:56.072 --> 00:48:09.432
Um, if there was a, you know, stage four of, or fourth era post-AI of Supabase that is like the other, you know, the one trillion X in your, in your growth, rip out Oracle. I, I don't know. Like- Mm-hmm. Yeah...

304
00:48:09.452 --> 00:48:14.252
what, is, is, is that the- Well, that's the, that's the- Is that what the white whale there? That's the one that the famous migrations are after.

305
00:48:14.392 --> 00:48:19.832
I heard some crazy stat like that it might be different now 'cause they're trying to, Oracle are trying to move everything to the cloud.

306
00:48:19.872 --> 00:48:35.080
But I think it was like one year ago, someone said that only five percent of Oracle workloads by revenue ran in the cloud. And so, like almost everyone was saying, "Oh, let's rip out Oracle. Let's do migrations."

307
00:48:35.560 --> 00:48:47.040
People... That's what I mean, though. Yeah. Like, when I look through the history of database providers who have tried to run this strategy, it sounds amazing, and it's something that we'll of course try to do ourselves.

308
00:48:47.300 --> 00:48:57.800
Why would we not try to do this? But it is incredibly difficult, and I think you would just wanna focus, first of all, on landing inside the enterprise. Uh, yeah, that makes sense. Yeah.

309
00:48:57.840 --> 00:49:00.700
It's, it's one of those things where, like, you know, when, when I s- see...

310
00:49:00.740 --> 00:49:09.340
When I talk to coding agent people all day long, the great promise is that you can finally migrate off of all this legacy software that you have. Yeah. Right? And, like, hopefully- That's true...

311
00:49:09.360 --> 00:49:18.720
that, that means that you cut over everything. That's true, because one of the things that actually makes Oracle so sticky is, like, you end up writing these million-line stored procedures.

312
00:49:18.760 --> 00:49:29.020
Like, you stuff everything into your database. And so actually probably rewriting that is, these days, a lot easier. Right. Right. It's... So, like, hopefully coding agents are the boom. Uh, maybe they're not there yet.

313
00:49:29.120 --> 00:49:31.280
Maybe you guys have to become more on-prem.

314
00:49:31.700 --> 00:49:42.160
Most of the problem around migrations is actually not, not rewriting it, and you can do migrations, for example, on the data analytics side quite easily from one, from one warehouse to another.

315
00:49:42.580 --> 00:49:54.420
The problem is that usually your OL- OLTP database is powering your most revenue-generating application. So a minute of downtime means that you end up with basically dollars lost.

316
00:49:54.740 --> 00:50:08.920
And so then what you end up doing is having to run these two things in parallel, and then the risk of this is that you get this split brain where you've got some data running on one side, some on another, and if you try to reconcile s- split brain, anyone who's tried to do it, it's a very hard problem.

317
00:50:09.000 --> 00:50:18.640
So the risks are just so much higher when it comes to OLTP that a lot of the time people just start doing... splitting the workloads off, and they'll start new workloads.

318
00:50:19.020 --> 00:50:28.380
They'll do a lot of operations here, and hopefully they'll migrate things over. Yeah. Usually then you've got two problems, though. [laughs] Well, speaking of OLTP, I mean, I, I...

319
00:50:28.460 --> 00:50:41.100
This is just my down database indulgence. We also had two of the co-founders of Databricks here, Matei and Reynolds, where they are making a claim that they have solved HTAP. Okay. Yeah.

320
00:50:41.320 --> 00:50:48.560
Which is the sort of the white whale o- of database people, right? Yeah, yeah, yeah. If you, if you know, like, uh... Well, traditionally you need an OLTP, you need all that database. Yeah.

321
00:50:48.660 --> 00:50:56.620
Um, never the two shall meet, except that, uh, sometimes you, you would like to never have to replicate anything. Yeah. How you... Are you paying attention at all to that stuff?

322
00:50:56.660 --> 00:51:05.760
Like, is, is there, is there a story there for Supabase some- someday? Yes, we are particularly interested in Duck Lake. I think Duck Lake is a very... and DuckDB is a very interesting technology.

323
00:51:05.780 --> 00:51:12.740
Is, is it Mother Duck, but a, but a data lake? Like, what, what is, what is Duck Lake? Uh, Duck Lake. Okay, so, um- [laughs]... DuckDB- Yeah... which was recently...

324
00:51:13.080 --> 00:51:22.820
It's DuckDB, which is basically like a SQLite for analytics. Columnar storage. Yes, exactly. Exactly. It can read directly from object storage. That's typically how it's touted.

325
00:51:23.240 --> 00:51:35.580
And it can actually read from your Postgres database as well, so open source, great technology. And actually there's also, uh, DuckDB Labs, which was recently acquired by AWS. Yeah.

326
00:51:35.640 --> 00:51:40.820
So they're a foundation- [indistinct]... that are developing. Yeah. So they're building a committee, um, around the open source.

327
00:51:41.140 --> 00:51:54.120
I actually think of DuckDB a little bit like the Postgres of the analytics ecosystem in that they're trying to make it so that it's owned by no one. It does a lot of things. It's very versatile.

328
00:51:54.140 --> 00:52:00.400
It's like a professor in Netherlands? Yeah, exactly. They live, they live and work out of the Netherlands, which is pretty cool.

329
00:52:00.940 --> 00:52:12.460
So our interest mostly on the warehouse side is not trying to make Postgres an analytical database, but mostly then focusing on using the right technology for the right job. I don't know if HTAP...

330
00:52:13.060 --> 00:52:24.040
Many people have tried to slay the HTAP dragon. Object storage could be the solution to that, but generally we think once you get to a certain size on the OLTP side, you need to have sharding.

331
00:52:24.320 --> 00:52:36.260
There's a limit to the amount of NVMe disk space that you can have, so if you need to split transaction across two servers, you're basically then going to be fetching it from object storage.

332
00:52:36.340 --> 00:52:46.740
Eventually, that will slow down your database. So we think that sharding is by far the best way to do scale up into the petabytes, and then you should treat your analytics differently.

333
00:52:46.900 --> 00:52:56.480
Now, that doesn't mean that you shouldn't store your data directly on object storage, for example, and then read from it from a different route. But trying to smash these two together- Hmm...

334
00:52:56.600 --> 00:53:05.140
doesn't necessarily make that much sense in my opinion. Yeah. I, I... I'm happy to leave it there because we do have more, uh, to, uh, work on.

335
00:53:05.540 --> 00:53:17.800
I do think, you know, they, they have some innovations where they're, they're basically using their s- their spare compute on their, uh, database, uh, machines to power all this, uh, replication is, is my read- Uh, yeah...

336
00:53:17.800 --> 00:53:27.360
of what they're, of what they're doing. And actually, to be honest, I haven't looked so much into how they're doing HTAP, so I could be misquoting. Yeah, e- exactly. Yeah. It's, it's like you're, you're in your lane.

337
00:53:27.380 --> 00:53:36.680
You know, it's not exactly like your customers are, like, banging the table asking you for this. Yeah. It is just, like, if you want to become the preeminent database company, someday you have to have an answer. Yeah.

338
00:53:36.680 --> 00:53:46.640
[laughs] Yeah. Exactly. Yeah. Which, like... Yeah, it's, it's interesting. Uh, the other mention I will check in on is durable workflows and, and, you know, that world- Uh, yeah...

339
00:53:46.700 --> 00:53:54.620
which, which as you know, Temporal, uh- Yeah, yeah... I, I've been, I've been, uh, banging the drum for a while. You have made, uh... Like, every year you make... you do a little thing. Yeah, yeah.

340
00:53:54.660 --> 00:54:02.520
We're incrementing our way towards [laughs] dur- Yeah. But, like, don't you... Like, how come it's not, like, more P zero for you? Because, like, you know Temporal is doing super well, right?

341
00:54:03.100 --> 00:54:13.800
Okay, so what was missing for us to do durable workflows? Compute. Right. So you're, you're doing this now. [laughs] Yeah. Super interesting space to be in, I think. Like, yeah, now

342
00:54:14.720 --> 00:54:21.840
we have had people in the community try to build workflow engines on top of Supabase functions, and it just didn't work because of the two-second timeout. Yeah.

343
00:54:22.120 --> 00:54:27.640
Now we've got the primitive that would unlock the ability to do long-running durable workflows.

344
00:54:28.300 --> 00:54:38.580
I think my original pitch for Supabase is, like, you want the sort of the all-in-one, the, the, the sort of agentic cloud- Yeah... that, like, is the backend, integrated backend that, that people can, can use, right?

345
00:54:38.620 --> 00:54:49.624
Like, you've got sign-in with ChatGPT now, which is, uh, a great part. Like, you, you just kind of have to sort of give the AI everything it wants, and then it will be your best friend. [laughs] Yeah. Yeah, pretty much.

346
00:54:49.644 --> 00:54:51.484
[laughs] Pretty much. And be prolific.

347
00:54:51.544 --> 00:55:03.104
I mean, our P1 strategy is to partner with as many of these frontier labs and models as we can, so we've gotta be prolific there, and then we basically, uh, we see our attach rates just going up as well. Yeah.

348
00:55:03.584 --> 00:55:14.364
I mean, obviously, there's the US labs, and you're, you're, you're here in the US. Do the other labs have significant partnerships? What, what are they like? Mistral- Ah... Cohere, the Chinese labs.

349
00:55:14.424 --> 00:55:21.224
I, I don't know if- Not so much... what's in your- Well, well, they might- Okay... they might do. Uh- Okay, you primarily care about the US labs. Yeah, yeah, yeah. [laughs] Yeah, okay. Okay, that's fair enough.

350
00:55:21.264 --> 00:55:29.244
[laughs] Yeah. Yeah. Mainly just 'cause, like, that's who's delivering the most traffic- Mm... at the moment, right? That could change. Yeah. But what does partnership look like?

351
00:55:29.284 --> 00:55:36.584
Like, basically it's one thing to be on the, their app store. It's the other thing to be their default thing when they- Sure... when they launch an artifact. Yeah.

352
00:55:37.044 --> 00:55:47.744
So that one's super interesting for us to be able to hopefully be one of those providers. Mm. One of the reasons why we couldn't in the past was because we just couldn't handle their scale.

353
00:55:48.124 --> 00:55:58.044
I mean, take ChatGPT, for example. What have they got now? A billion monthly active- 1.2... 1.2 billion monthly- Yeah... active users. One of their users launching a database every single month.

354
00:55:58.224 --> 00:56:05.664
[laughs] Now we've gotta launch 1.2 billion Postgres servers. It's just, as I said, we've gotta get to the billions of databases per month.

355
00:56:05.964 --> 00:56:14.524
We just haven't been able to do it until today, where we acquire a company that means we've got the technology which can drive it up. Scale up, scale out. Okay.

356
00:56:14.604 --> 00:56:25.504
Um, a- other than that, what are other, I guess, P0 objectives for the company? Like, you know, over the, over the next year, how are you sort of guiding the, the direction?

357
00:56:26.084 --> 00:56:38.004
Our P0s are basically win the strategic labs, win the models, and, uh, continue our PLG push. Where we are focused on the enterprises is winning these- Yeah... new workloads.

358
00:56:38.044 --> 00:56:44.704
And it's more that, like, the ceiling of PLG, when we started the company we were like, "We can get to 100 million on PLG.

359
00:56:45.164 --> 00:56:57.744
We can probably get to 200 million, but then we're gonna need to do something different in terms of motion." But because of AI, like, that ceiling just lifted, and we don't know where it got [chuckles] lifted to.

360
00:56:57.784 --> 00:57:01.724
Like, is it a billion? Is it two billion? Is it... You know, you could just-- we could just keep going.

361
00:57:02.144 --> 00:57:09.644
But we still wanna do the other stuff as well, so we basically, like, last year we were like, "Well, we have to do both." Um- Yeah. [laughs]...

362
00:57:09.704 --> 00:57:20.264
the bo- the small stuff and the big stuff, and, you know, uh, maybe we're a bit greedy. [laughs] No, I, I, I think it's, it's what people want, right? Yeah. The, the same sort of mental model that, uh...

363
00:57:20.304 --> 00:57:29.364
And, you know, they'll, they'll pay you to handle the fine grain details of, uh, moving up in terms of orders of magnitude. Yeah. And I don't know how many orders of magnitude that is, but quite a bit, quite a lot.

364
00:57:29.704 --> 00:57:39.464
It's just crazy, because if you would've asked us 18 months ago, we were growing fast. If you would've said, "What can you do to 10X your top of funnel?" I would've said there's nothing. Like, it's, it's crazy, right?

365
00:57:39.564 --> 00:57:43.324
And then just this whole market just exploded, so let's see what happens.

366
00:57:43.624 --> 00:57:52.484
Yeah, I remember at our company offsite at the start of the year, we, we put this crazy ambitious revenue number out, and someone came up to me and said, "Oh, you shouldn't have said that number.

367
00:57:52.524 --> 00:57:58.404
Like, the team are gonna be so-" We're gonna miss it... we're gonna miss it. Yeah. The team are gonna be so disappointed, and it took us, like, four months to hit the number.

368
00:57:58.444 --> 00:58:07.824
It's just, like, a ridiculous growth curve from the start of this year. Amazing. Um, what are the open questions that you have?

369
00:58:07.904 --> 00:58:19.784
Like, you know, if you had a crystal ball, it, that it would change the way that you bet on things. How development will be done- Okay... and what people will develop. These are the two things that I think a lot about.

370
00:58:20.104 --> 00:58:28.464
Okay. You know, what are the possible answers? It's just more, more agents. Like- Yeah, so, like, this year we're focusing a lot, like, and I'll talk about it in my keynote, basically, that we're moving from...

371
00:58:28.684 --> 00:58:35.284
Like, we started as a dashboard company. That was the best DX. Then, like, you know, a lot of people are like, "Oh, headless mode."

372
00:58:35.844 --> 00:58:47.564
Headless was what we kind of started, Headless 360, Salesforce, all these sort of things. I mean, we had that at the start, like, you could use Supabase directly, API-driven. That's one of the reasons why we succeeded.

373
00:58:47.964 --> 00:58:52.644
This year, our big focus is moving from, from, um, to code first, Git native.

374
00:58:52.964 --> 00:59:05.363
So basically, when you launch a Supabase instance inside, um, your local machine, you get this Supabase folder, and it represents your database. It has all your functions, everything. Does this exist today?

375
00:59:05.524 --> 00:59:14.204
This exists today- Okay... if you use the RC LI. So it's a virtual file system Uh, like, it's a representation of... It's like infrastructure as code. Okay. Yeah.

376
00:59:14.424 --> 00:59:24.164
And in fact, what we're announcing tomorrow is, like, we've done our kind of final change for declarative schemas. This was a, a really challenging one actually, covering all of Postgres.

377
00:59:24.684 --> 00:59:32.184
And so now you can have a full file representation of Postgres, uh, the shape of your database declaratively in your folder.

378
00:59:32.484 --> 00:59:42.524
That's really important for agents, 'cause generally how you operate with Postgres is you have a migration file every time you make a change. You add a file to this migrations folder, and it's like a historical log.

379
00:59:42.984 --> 00:59:52.684
Okay, so that's great. It's industry standard. But imagine putting an agent across a thousand files and telling, asking it, "Oh, what is the shape of this table?"

380
00:59:52.784 --> 01:00:01.724
It has to guess through 1,000 files, so- It has to recompile basically- It has to recompile... edit weights, yeah. Or you have to launch the database, um, locally- Migrate, migrate, migrate, migrate...

381
01:00:01.764 --> 01:00:06.304
run the migrations up, and then you inspect, introspect the database. But that's too slow.

382
01:00:06.404 --> 01:00:15.844
So basically what we want to do is turn the schemas folder inside our, our Supabase folder into a completely declarative state of your database.

383
01:00:15.884 --> 01:00:26.524
And so we've captured everything from tables, policies, uh, database comments, all inside these files. So we're releasing a new library, pgdelta. You can use it with any Postgres database.

384
01:00:26.804 --> 01:00:37.704
Um, but we've got mechanisms for the, for Supabase. And so this is an important step for agents. We know that agents are gonna operate mostly on code. They don't wanna reach out to anything.

385
01:00:37.744 --> 01:00:45.684
They've gotta iterate very fast on the file system. So that's fine, and today people are using CLIs. They're happy with these harnesses.

386
01:00:46.104 --> 01:00:56.044
What I suspect we're moving more towards is, like, at the moment I'm trying to do some development just on my mobile phone, for example, and I'm quite comfortably able to do it.

387
01:00:56.104 --> 01:01:02.764
Of course, I know what's going on behind the scenes, so I'm telling it things that I know it has to do from an infrastructure point of view.

388
01:01:03.064 --> 01:01:13.524
But we're getting to a state where I can imagine you don't need to be an engineer. You, you have an idea, you say to your phone, your dot or whatever personal agent you have- [chuckles]...

389
01:01:13.524 --> 01:01:21.684
"I want to build X," and one second later, you kind of have this application live. You can iterate on, on it yourself.

390
01:01:22.044 --> 01:01:32.364
So these are the things that I'm thinking, "Okay, what are the use cases that people are going to want if this is the case? Is it personalized? What do we care about? Are these things gonna scale up?

391
01:01:32.804 --> 01:01:40.084
What are the mechanisms? How are we going to develop, and what tooling do we need to provide to make sure that we are the default provider in this new world?"

392
01:01:40.644 --> 01:01:48.564
Any questions that you're, you're interested in, uh, as for a crystal ball into the future? As someone who's been a software engineer now for, like, a few decades,

393
01:01:49.464 --> 01:01:54.024
you have strong opinions on, like, how the software should be built, right?

394
01:01:54.504 --> 01:02:06.244
Like, in terms of, like, uh, continuous integration or, like, continuous delivery or whatever, and I find myself, like, pushing my opinions on the, on the agents of, like, "Oh, you wanna do it in this way," and...

395
01:02:06.604 --> 01:02:19.524
But now more and more, like, you don't need to. But my worry there is, are they all just gonna, like, converge on one way of building software or- Yeah, mode collapse. You know- Which is great.

396
01:02:19.564 --> 01:02:21.944
They're all gonna use Supabases. Fantastic. [laughs] Yeah.

397
01:02:21.964 --> 01:02:32.744
But, but, but, like, the g- the thing that's great about, like, the software development injury is, like, i- industry is, like, these are, like, famous flame wars, right? Of, like- Yeah... what's the correct approach.

398
01:02:33.304 --> 01:02:37.024
Like, are we gonna lose that or- Yeah, so you want diversity in ideas- Yeah, exactly...

399
01:02:37.064 --> 01:02:43.144
so that the best idea can win, and but then the models are just gonna make you so lazy that nobody even bothers to look at the details.

400
01:02:43.404 --> 01:02:52.484
Yeah, and, and they just all converge on one way of building software, and then that's, you know... Is it gonna be like a local maxima in terms of- Yeah. I, I don't know. I, I, I do think, uh, yeah.

401
01:02:52.604 --> 01:02:55.824
So first of all, I think that's a valid fear. I do think it's out of your control.

402
01:02:55.824 --> 01:03:06.344
[laughs] Um, I, and, and, yes, uh, the low taste, let's call it the casual app builders will, will converge on whatever the, the mean is, uh, the, the model is, which is you guys.

403
01:03:06.904 --> 01:03:17.044
But then the, the discerning high-skill people will always really care about the details as, as they should. Yeah. Right? And which- Yeah... which will, which will then filter down eventually- Yeah... is the, is my idea.

404
01:03:17.064 --> 01:03:26.424
[chuckles] But are these high-skill people gonna continue to be trained by- Uh, I don't know. [laughs] Yeah, yeah. I mean, I think, I think people are passionate enough. Yeah. Uh, I, I...

405
01:03:26.464 --> 01:03:32.944
It's one of those things where, like, you know, I do think, like, uh, you know, the average, um, college is probably screwed, right?

406
01:03:32.984 --> 01:03:39.684
Like, they, you probably don't need to go to university anymore because you can probably self-teach and just, like, you know, uh, get, get your own, uh, job.

407
01:03:40.264 --> 01:03:49.604
It's always been, like, this top-tier people that, that are moving a lot of the, the, the needle, and you need to, uh... And, and they will always find a way to have their own self-interests, uh, be satisfied.

408
01:03:49.884 --> 01:03:59.244
Curiosity in terms of, like, what, what is possibly better. You know, the type of people that take a year off and go to the Recurse Center and just work on cool programming problems even though they could be making

409
01:04:00.164 --> 01:04:10.044
money in, in industry- Yeah, definitely... and, like, yeah. [laughs] Definitely. [laughs] Yeah. What do you disagree on between the two of you? It's rare to have the two of you have, uh- Wow. Oh, yeah. This is great...

410
01:04:10.104 --> 01:04:12.364
on, on the pod, so, you know, I wanna capture this.

411
01:04:12.944 --> 01:04:25.544
I think one of the reasons we've been so effective, like, working together is because there are definitely situations when we'll disagree, but as soon as the other person, like, pushes a little bit- Yeah...

412
01:04:25.584 --> 01:04:36.304
the other person's like, "Yeah, maybe you're right. Let's, let's try it." Yeah. Um, so we never end up in, like, big bust-ups, um, and it turns out, like, most of that stuff actually doesn't matter, right?

413
01:04:36.304 --> 01:04:46.224
Yeah, it doesn't matter. [laughs] Anyway. Like, as long as the general direction is, is correct, then, then it's gone okay. But, uh, yeah, I can't think of- Oh, you guys are really struggling here. Oh my God.

414
01:04:46.224 --> 01:04:58.104
[laughs] Yeah, yeah. Which is why, like... Because it's, it's never an important enough thing. Like, we've never had a bust-up because it's never been important enough to actually fight hard enough on it. Like...

415
01:04:58.684 --> 01:05:05.964
And also, we're fucking busy, so, like- [laughs]... usually, like- You got your thing, I got my thing... Ed's handling... Yeah. Yeah, yeah. We're trying to handle different parts of the business. Yeah.

416
01:05:05.984 --> 01:05:12.524
Maybe it's just, like, things are growing, and obviously you got your domain and, and you just need to work together, right? Yeah. Yeah. Yeah. Yeah, it's interesting, you know.

417
01:05:12.624 --> 01:05:23.004
Uh, so Laura here, uh, all three of us were in Entrepreneur First- Yeah. [laughs] Yeah... in Singapore. We were all different work- working on different companies, and then you guys stayed back after the cohort?

418
01:05:23.684 --> 01:05:33.804
Uh, you were housemates after the cohort? Yeah, yeah. Yeah. So we were all-- We lived in a house with seven people, and we were all doing different startups. Yeah. And so Em was doing his startup.

419
01:05:33.844 --> 01:05:45.464
I was doing another one. This is before Supabase. And so, like, I think somehow your energies, uh, you know, you, you, you found that you were suitable working together and, and working on this, uh, this, this project.

420
01:05:45.484 --> 01:05:53.904
Yeah, because, like, traditionally, especially in, in an accelerator model, you're pushed as a technical person to work with some domain ex- domain expert, right?

421
01:05:54.284 --> 01:06:12.064
Um, but in the house we lived in, it was basically seven people who were all builders, all technical people, and we found that pairing to just be, like, so much more effective, especially on when you're building dev tools 'cause you are the subject matter expert as a developer, is that we could, could just get so much more done.

422
01:06:12.364 --> 01:06:20.544
And so then we ended up hiring most of the other people who lived in the- Yeah... the flat, as well as our early employee- Rory... is Rory, who- Was the first employee?

423
01:06:20.984 --> 01:06:29.664
Um, not the first, but the first e- to, on go-to-market. Like, now he runs- Yeah... all of go-to-market. Uh, the Postgres guy was first. No, uh, Angelico. Angelico. Yeah. Yeah, yeah.

424
01:06:29.684 --> 01:06:42.184
We had an intern- An intern from my previous startup. Ah. We just dragged him along. [laughs] Yeah. And, and then the other, like, first, like, full-time hire was this guy Steve Chavez, who, um- Postgres, yeah...

425
01:06:42.244 --> 01:06:50.924
who was the Postgres maintainer. And the funny thing is we were in the YC batch, and the advice they give you in YC is like, "Okay, we're gonna give you a bunch of money. Don't hire anyone."

426
01:06:51.144 --> 01:07:00.952
Uh, that's the big temptation is to hire a big team. And we went to our partner, and we said, "Oh, but we've got this guy Steve, he's the lead maintainer of Postgrest," and he was like, "Hire him immediately."

427
01:07:00.972 --> 01:07:08.912
[laughs] You know? [laughs] He was like, "Forget the advice. Go and get him." W- of his reputation or because it made sense for Supabase? Well, yeah, both.

428
01:07:08.972 --> 01:07:14.812
It, it just made sense that, you know, this was a technology we were very reliant on- Yeah... and we were gonna lean in, and it was like...

429
01:07:15.252 --> 01:07:23.332
And the, the funny thing is, we hired Steve, and we said, "Don't worry about Supabase, just keep building Postgrest and just making it awesome.

430
01:07:23.972 --> 01:07:30.412
Um, and then obviously, if we have support requests or whatever, we can, we can ask him." Yeah. But, um, and the model just worked really well.

431
01:07:30.452 --> 01:07:40.552
And then we ended up, when Steve wanted to grow the Postgrest team, just hiring more people dedicated to work on that project. Well, you guys are doing so much for community and open source.

432
01:07:41.092 --> 01:07:51.392
One thing I do have in my mind is, like, what is the future of large commercial open source? Mm. Um, one, obviously there's a lot of slop, and, and- Yeah... uh, I'm sure you guys are dealing with that.

433
01:07:51.732 --> 01:08:00.952
But two, also your dependencies are now becoming, uh, optional. Like, you can just vibe code whatever you want. [laughs] Anything, yeah. Yeah, yeah.

434
01:08:00.992 --> 01:08:11.712
So I, I, uh, whatever in your, is i-in your heads about the future of open source, I'd, I'd just love to hear it. I think the rewrite in Rust is a valid mechanism.

435
01:08:12.552 --> 01:08:20.532
I mean, someone came to me on our team, and they're like, "Oh, yeah, yeah, I'm rewriting everything in Rust that we're doing." Like, uh, and I was like, "To what level? Are you gonna rewrite the database?

436
01:08:20.572 --> 01:08:27.052
Are you gonna rewrite Postgres?" Postgres is not rewritten and, uh, is not in Rust, but I doubt down to that level you care.

437
01:08:27.112 --> 01:08:38.352
So there's, like, layers upon which you want to get to where things will be rewritten, and then you don't wanna be spending your actual innovation tokens or your actual tokens rewriting everything.

438
01:08:38.372 --> 01:08:53.272
[laughs] So there's gonna be, like, a, a collapse of almost every tool probably into, let's say it's Rust, if that ends up being the, the ultimate way of writing things 'cause it's faster and more correct, and that will happen probably for most open source tools.

439
01:08:53.632 --> 01:09:05.972
But then after you've done this iteration, and everything's running on this highly effective language, then you're not gonna be rewriting it all of the things every single time. There'll be a few winners.

440
01:09:06.472 --> 01:09:18.112
A really classic one could be, say, Postgrest is written in Haskell, which is a very unusual language, and it's very hard to maintain. Could it be re-written in Rust now? Yeah, probably it could.

441
01:09:18.512 --> 01:09:29.972
And the mechanism, the, the function is still valuable, and probably there'll be, if that happens, there'll be one Rust fork of Postgrest, and that will be the winner for that particular category.

442
01:09:30.352 --> 01:09:37.492
But you haven't done it yet. And your, and y- a lot of your stuff is Elixir as well. Yeah, so that's the other thing. Then you have to think on the infrastructure side.

443
01:09:38.012 --> 01:09:48.292
Elixir is, like, a really interesting language- Beam... because of the Beam. Yeah. So, so and then you start thinking when you're operating things, what is the right mechanism for operating, so.

444
01:09:48.792 --> 01:09:59.532
But now you can change paradigms eas- pretty much easily as long as you fit all your tests and, you know. Yeah, yeah. Well, that's a good one. I haven't thought a lot about would we switch Elixir to Rust.

445
01:09:59.912 --> 01:10:07.412
It's just an option now. Yeah, Malta f- from Vercel is, uh, you know, one of his tweets that sticks in my mind. He- he's got lots of, uh, interesting thoughts.

446
01:10:07.792 --> 01:10:17.912
He set aside some amount of money and rewrite all of our dependencies, uh, at, at the C level or C++ level into Rust, um, because we just know it is better, it's safer, more correct- Yeah... what- whatever.

447
01:10:18.432 --> 01:10:28.292
And it is, it is a one-time upgrade of open source. Yeah. All the drivers, what- whatever you, you use. Um, so I, I thought that was, like, a pretty interesting call. I like that as an idea, yeah. Cool.

448
01:10:28.332 --> 01:10:38.172
I don't think it'll happen [laughs] because people love to do it themselves. Yeah. But, but as an idea, I, I would, like, we as a company would 100% get behind that. Awesome.

449
01:10:38.212 --> 01:10:47.772
And then, uh, I think closing question, which I, I should have stuck in somewhere earlier, AI coding within Supabase, right? Uh, obviously you guys are big beneficiaries of coding agents outside. Yeah.

450
01:10:47.832 --> 01:10:59.652
Uh, what is the policy internally? How much are you spending? Is there, is there concern about spend? Anything of that sort. Supabase has always felt like a bunch of different startups, like, glued together.

451
01:10:59.732 --> 01:11:13.751
[laughs] So we have, like, the auth product, and we've always been very insistent that they should make their own decisions, like, on what tools they use, like, how they behave as a team, like, the reporting structure, and the AI policy was kinda no different.

452
01:11:14.212 --> 01:11:25.612
It's like a lot of people asking, "What is the AI coding policy?" And we were like, "Well, just it's up to you as, as your team." I think we have started to consolidate a few bits, especially around cost.

453
01:11:26.172 --> 01:11:34.252
But as much as we can, we'd like to keep that model of, like, let the teams decide how they wanna run things. That's it, very decentralized. Mm.

454
01:11:34.272 --> 01:11:46.152
[laughs] I, I would say, um, I am trying to figure out a number for company leaders to take home with them as, like, what is the market standard. And so, uh, what, what are data points you can hang your head on here?

455
01:11:46.492 --> 01:11:53.432
People say, uh, you know, the average, uh, person is spending, like, $20 a month, and then, uh, average employee is maybe $200 a month.

456
01:11:53.992 --> 01:12:04.752
OpenAI, uh, you know, at the, the sort of 50th percentile is spending maybe three to five thousand a month, and the top percentile is in the maybe hundreds of thousands. Mm. Right? And so that is the rough idea.

457
01:12:05.232 --> 01:12:15.832
I think, uh, a good metric is basically what is your ratio of token spend to human spend, and it's r- like, for a lot of people, it's maybe 0.1, uh, tokens to, to one human salary.

458
01:12:16.432 --> 01:12:23.192
And, uh, you know, you can probably go up to one pretty safely, and if you're over 1.5, you're probably in trouble. [laughs] Something like that.

459
01:12:23.792 --> 01:12:33.592
So I'll, I just, uh, say, uh, luckily, as a remote company, basically everything that's- Documented, yes... ever happened is documented. [laughs] So I can ask our AI how much we're spending.

460
01:12:33.672 --> 01:12:43.472
So currently, we spend about 300K per month. Yeah, uh, for 600 people. No, for- So like 450 people... 400. Four, 450 people. Yeah. Okay. Yeah. That, it gives people an idea.

461
01:12:43.832 --> 01:12:53.972
But, but what you've said about, like, scaling the cost in terms of related to the number of employees makes sense also for us because we are hiring very quickly.

462
01:12:54.192 --> 01:13:01.968
So if we end up getting a lot of leverage out of just, like, actual spend- You should be, right?... then yeah. You, you need a whole bunch of serverless employees that can spin up and down as, as you need, right?

463
01:13:02.008 --> 01:13:09.388
Yeah, exactly. Wh- which is like, yeah. Like, you know, I, I just had a CTO of, uh, you know, a- another top startup say, like, he was worried about his company spend.

464
01:13:09.768 --> 01:13:14.828
And I'm like, "Well, actually your- that's your investment in everyone else, and probably is very skewed," right?

465
01:13:14.848 --> 01:13:22.868
Like there's, there's like two or three people that are super insane at your company, and everyone else is like probably not using AI enough. Yeah, yeah. Yeah. [laughs] That's exactly what we see as well.

466
01:13:22.888 --> 01:13:30.128
[laughs] We've got a leaderboard, and people... We put the leaderboard up, and usually people are a little bit ashamed, so they kind of like- [laughs] Yeah, 'cause you're wasting money probably. Yeah.

467
01:13:30.148 --> 01:13:37.528
[laughs] And that's also the wrong focus. Like, the focus shouldn't be on how much you're spending, but, like, how much end-to-end... Like, in terms of systems thinking- Yes...

468
01:13:37.548 --> 01:13:50.388
you should be thinking, like, in terms of how many end-to-end processes are you actually solving that where you no longer need a human in the loop, or collapsing down long-running human problems that suddenly become very short problems.

469
01:13:50.448 --> 01:14:01.588
So that's where we're spending most of our investment on, like, how we're using AI. Luckily, you know, as you saw, like, every single thing that's ever happened in Supabase is documented because we're an async company.

470
01:14:01.888 --> 01:14:10.888
Yeah. So building a company harness or, like, an agentic harness around Supabase is basically just formalizing. You can point AI at it and say, "What are our principles?"

471
01:14:11.168 --> 01:14:18.788
And it'll docu- d- document down all our decision-making principles for the whole history of Supabase. So that's where we're spending a lot of our time.

472
01:14:19.148 --> 01:14:30.008
Before we move on from people, we do have, I think, now, like, 50 open roles. [laughs] Yeah. And we are fully globally remote, so we don't care where you are. If you're very good- Same, same salary everywhere, right?

473
01:14:30.068 --> 01:14:36.668
Yeah. Yeah. Same salary regardless of where you live. If you're very good at what you do, please take a look at our job board. [laughs] Yeah. Can you, uh...

474
01:14:36.768 --> 01:14:47.908
Can you, like, one profile, just pick one, whatever is top of mind as, uh, as your highlight for what you're looking for and why? SREs. Okay. Yeah. Why? Because we're just growing at a ridiculous rate.

475
01:14:48.248 --> 01:14:55.688
We need all the SREs we can get. What is a quality that is... Like, you know, you, you probably get a lot of SRE applications and you don't look at them. Like, what, what stands out?

476
01:14:56.348 --> 01:15:05.088
The thing that we really care about is that you, you actually want to work remotely. Um, so it's- [laughs] This is a strange one, but yeah. [laughs] It, it's true.

477
01:15:05.148 --> 01:15:17.288
We get a lot of quality people, but to fit in at Supabase, you kind of need to thrive in a remote-first environment, like a fully async environment. It's actually not for everyone. We learned that pretty early on.

478
01:15:17.328 --> 01:15:25.428
People would come in and they'd be like, "Oh, this is... Like, I need to see humans." My typical model of an SRE is, like, this gray beard that's, like, sitting in a dungeon somewhere and- Yeah, yeah...

479
01:15:25.468 --> 01:15:33.148
doesn't wanna talk to humans anyway. That's the perfect- Right. [laughs] That's the perfect person. [laughs] All of those people, please apply at Supabase. [laughs] Yeah. Great. Hopefully they listen to the podcast.

480
01:15:33.388 --> 01:15:39.168
Yeah. Yeah, yeah. No, I mean- [laughs] Yeah, we, we, we probably do have a lot of, uh, gray beards, um, in SREs. I, I think one of...

481
01:15:39.328 --> 01:15:50.328
Uh, I have been on the record as saying AI SRE is one of the hardest categories for- Oh, yeah... for agent startups. I think I might be wrong soon, but so far it's been correct. Like- Okay, yeah...

482
01:15:50.548 --> 01:16:03.388
AI has not cracked SRE for, for whatever reason. No, no, no, no. Not yet. I agree. Yeah. Like, building software is, you know, debatable, solve problem. Maintaining, like keeping things running- Yeah...

483
01:16:03.468 --> 01:16:11.208
is a whole different beast. Well, okay. Well, thank you for keeping things running for everyone else. [laughs] You guys, congrats on your journey, man. Like, I'm so proud to be your friend- Thanks for this...

484
01:16:11.308 --> 01:16:19.828
uh, and, and an investor and, and just, like, just see the progress. I cannot wait for the IPO, whenever that is. [laughs] Uh, it looks like it's gonna take some more time, but it'll, it'll be, it'll be fine.

485
01:16:19.908 --> 01:16:28.748
I, I want, really wanna see you guys, like, you know, do the whole ring the, ring the bell and, you know, building the next great open source company, right? Excellent. Definitely, man. Yeah. Congrats.

486
01:16:28.748 --> 01:16:38.108
Thanks, thanks for having us. [upbeat music]
```