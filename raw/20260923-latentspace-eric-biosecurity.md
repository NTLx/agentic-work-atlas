---
title: "🔬Bio-security is an AI Arms Race - Eric Nguyen (CEO, Radical Numerics)"
source: "https://www.latent.space/p/bio-security-is-an-ai-arms-race-eric"
author:
  - "[[RJ Honicky]]"
published: 2026-09-23
created: 2026-09-24
description: "Radical Numerics is using biological chain-of-thought and multimodal perception to keep up with the bio-defense arms race, design new genomes and gain insights into biology itself."
tags:
  - "clippings"
---
<audio src="https://api.substack.com/api/v1/audio/upload/c5daecec-8262-4632-b94a-ac5fcbb74077/src">Audio playback is not supported on your browser. Please upgrade.</audio>

The design side is going to get more capable. The defensive side needs to try to get ahead. So I think inherently there is this arms race style dynamic that the defensive side has been far, far lagging. And so what we want to do is bring The defensive side to par, essentially.

We felt it was important as a lab that a team that was both building the design capabilities is actually also best suited for building the defense capabilities because they're basically the same models. A model that is good at generating turns out The result is also very good at discriminating or predicting if a sequence is pathogenic or not.

For us, we as a company thought it was very important to have a dual mandate. It's this idea of essentially being cognizant and feeling responsible for the capabilities that we're enabling on the design side. So if we're going to create models that can design function into sequences,

we believe and see a gap in companies being able to safeguard that technology

Welcome to Latent Space. I'm Brandon. I build RNA therapeutics at Atomic AI. I'm joined by my co-host RJ Honicky, CTO and co-founder of Mirroromics. Today, it's a pleasure to have with us Eric Gwynne, CEO and co-founder of Radical. Eric got his PhD in Chris Ray's group.

He spent a lot of time thinking about how to do long context genomic models before long context or genomic models were cool. He was the first author and I think basically visionary behind the Evo generative model, one of the first generative genomics platforms developed Evo2, which naturally led into radical numerics. Yeah. Thank you for being here.

Did I miss anything?

That sounds great.

Cool.

Welcome. Thank you. So Eric, let's talk about Omni and the blog posts that you guys did about the benchmarking. But I want to hear first, okay, what is a genetic language model? Why do I care? What does it do? And then let's talk about the top line results from the blog post.

So a genome language model, or GLM, is a large language model trained on DNA sequences. So very much like natural language. And chatbots you see, but not trained on words or natural language, but on the raw fabric of life, which is these sequence of letters that make up DNA. And we ourselves, our company,

our team is known for creating the first generative genomics models, which are models trained on DNA, not just to read, but also write, meaning able to generate new sequences of DNA. And we felt this was a An area that was overlooked and that if AI could read and write DNA, it could change a lot.

You know, scientific discovery and understanding of human health and how to treat it. And so we felt that it was a big opportunity to train AI on the genome. What kind of things can you potentially do with a model like this? Great to start for us when we first started working on DNA models.

We worked on this model called Hyena DNA. Which is a large language model, but it used a convolution instead of a tension. So a little more technical details. DNA has this property that, well, it's very long, right? At the time, these large language models had limited constraints on context, right? Being able to fit long sequences.

And so we were looking for a more efficient algorithm to be able to handle something like DNA. And so we came up with this, what we call the hyena algorithm. Operator uses convolutions. Long story short, it let us process longer sequences, in this case up to a million,

and at the time was the largest context for a language model. And what we did with it was essentially used it to read DNA, predict function. So given a sequence of DNA, a string of characters, we predict its regulatory function, its effect on a genome.

And this is interesting to scientists because a lot of the DNA in our bodies is Um, you know, perhaps people are less aware, but actually we don't know a lot that much about our genome. It's, we know it, obviously it encodes the information for making us us and how, you know, all the different At the same time,

the grammar, sort of grammar rules about how the combination of those letters are sort of formed, what they encode and how they encode function and traits is not fully understood. The hope was using these DNA models, language models, to be able to map some function from the raw DNA sequence.

And so our first generation models was able to show that, yes, we can train AI to be able to read and understand to some degree. DNA sequences, and especially what we call the longer range interactions, meaning over sequences, you know, if you use chatbots, for example, like if you've heard of the phrase context rot, you know,

the longer the input you put into a language model, it starts to deteriorate. And so being able to pick up long range information And sort of patterns, motifs, grammar over long sequences was what we were trying to accomplish. And so we showcase in that first generation of hyena DNA that that was possible over a million contexts.

And then really what started the field now known as generative genomics was the model called EVO. And Evo, we should try to showcase there was this idea of not just reading DNA, but being able to generate it. And so we wanted to accelerate essentially how biologists and scientists have learned from biology and particular genomics.

And we felt like This whole field of generative AI being applied to language, great. Accelerated, obviously, our understanding and ability to manipulate the natural language. But here's this other language, DNA, the genome, that we don't understand. And it's barely being applied with AI at the time, a few years ago. Models that we saw were really small models.

Short context, so they can only pick up small patterns and limited context, and none of them generated DNA. So they all just would read. And we felt that the idea of generation was so powerful and transformative in natural language. What if we could bring that to biology and DNA in particular?

What can you accomplish that you can't do in a lab? Right. So what does that unlock for you if you could do that very well?

I think one of the... First things that we showcased that got folks sort of intrigued by the potential of this was a CRISPR-Cas system. So it's an enzyme that's able to cut DNA itself. And I think what was particularly enabled by the EVO models was the ability

to generate over not just one modality or one type of sequence, but a Spanning multiple modalities and spanning multiple scales. So CRISPR-Cas, it's a molecule made up of both RNA and proteins. And so at the time, you hadn't really seen models that can generate multiple modalities. They had protein language models that can generate proteins.

Sometimes you had RNA models that can generate RNA, but you didn't have a single system to sort of co-design. We showcased that a single DNA model, sort of the foundation of both of those, right, from DNA you can get RNA and proteins, that we can design a single system to generate and also function in the real world.

So we asked Evo, we showcased it a bunch of natural CRISPR-Cas systems and essentially asked it, can you make a new one? And we're able to sample from that model that we trained. And indeed, we showcased that Eva was able to discover a new CRISPR-Cas system

and folks were intrigued by it and cover Science Magazine and later get to give it Yeah. Just last year showcased what you can do with a generative DNA model was to generate the first genome from scratch using AI. So this is something not possible by humans, right? Humans usually,

you can think of it like copy and paste parts of other genomes or other DNA, put it into something else. But they would just take out small motifs that, you know, they know the function and they understand the rules. But to build something from scratch in the ground up had not been done before at the genome level.

And so EVO, Turns out, was able to generate a functional genome. And in this case, it's known as a bacteriophage, also known as a virus. And this was a key turning point for, I think, the scientific community and for us as a company at Radical Numerics,

because we felt this was such an indicative manifestation of the potential to create a whole organism. Not existing in nature, but also the potential harm that that means as well. If you can control, if you can manipulate the fabric of life itself, control its function, what kind of implications does that mean?

What are you enabling into the world? And so we actually got a lot of feedback, a lot of comments, a lot of Outreach from folks both excited and concerned about this capability, this kind of capability, and just the trajectory, right? This is the early stages,

the first thing one can sort of project and imagine what this could lead to. And so we felt as a company, it was important to not only push on the biological design capabilities of these models, But also the ability to use them as defensive tools for the potential of misuse and biological risk that emerges.

And I think indeed, a lot of companies, a lot of frontier labs are also being concerned about this emerging risk of AI models being capable of designing biological sequences. And, you know, at the same time, It's being mostly attacked from like a natural language standpoint, like safeguards and things like Claude.

You know, if you talk about viruses, they'll just like shut you down, which is great. I think it's to some degree you need safeguards at the natural language level. But I think what you always... What you also need clearly is safeguards at the biological sequence level too. So you need models that not just can understand language and,

you know, the trajectory of your chat, but to understand the substrate itself is the next step in ultimate limit, right? If you can have models can understand, you know, if the sequence is pathogenic or a virus, that's the level of a defensive Capabilities that you want. And then, you know,

being able to push that out into surveillance systems, national security of, you know, being able to monitor, you know, emerging sequences and environment. This is what that kind of capability makes possible. And then we think bringing this frontier technology to that community as well is also important, just as important as using this for human health,

which is what we primarily focus on.

There was this evolution that you mentioned, there's the hyena DNA, and then there's EVO, EVO2, and now Omni. Can you just talk a little bit about EVO and EVO2 struggled to beat sort of specialized models across many tasks, whereas in the blog post you talk about how across a wide range of tasks

that Omni is actually able to outperform them now. So can we just talk a little bit about that?

So yeah, EVO was intriguing to folks in many ways, showcase the potential for applying to multiple types of modalities. But it's still in many ways underperformed sort of the specialist DNA models, especially on human genetics or genomics. And so although EVO was competitive, it still wasn't state of the art or kind of pushing the needle.

And so, you know, some parts of the community thought like, why use a giant LLM when I can use these smaller, more specialized models? And so what we wanted to do with Omni So the way we think about language models and bio and jhonos in particular is that Mostly, you've only seen base models trained.

So they're pre-trained, but they're basically unaligned. So in the analogous space for natural language, it's like you're doing all the pre-training, but to make it actually useful in the real world and answer questions that users actually want and that is in the form factor they find actually useful. Informative.

There's a bunch of alignment and post-training and mid-training done to get the models to be production ready and actually useful. And so we felt Evo was just showcasing the potential of that pre-training. But Omni is a step of actually making it useful for folks like scientists, right?

And so we spend a lot of time on alignment and mid and post training, which is essentially showcasing tasks in the form that people generally would want to understand. You know, given a wild type and a mutation sequence, you know, help me find the causal variant, right?

These types of questions and form factors for how you might want to analyze genomics doesn't just emerge necessarily easily on its own from pre-training. Pre-training is, you know, this next token predictions task or infilling. And basically, I think of it as like the raw information. Pattern making ability that you're teaching it is in the pre-training.

But then taking those learned embeddings or features and pointing at specific tasks or a bunch of tasks really and aligning it, meaning have it Show you the output in a way that is meaningful to you. Takes a little bit of teasing and manipulating that so far, like the furniture labs are the ones that drive that research in

the natural language community. And so we wanted to bring a lot of that research and more to genomics. And so I think Omni is really just a preview to showcase... That potential, right? And I think once you do that, even just a little bit, you know,

we were surprised that it did start being state of the art and pushing the boundaries, not just being affected of multiple tasks, just broadly, like Eva was, but actually pushing the frontier of each of those areas of variant effects prediction, causal mutations for disease. It could start actually being useful for human genomics.

And so we're really excited to share that with folks. And it was just a preview in that sense because we're still actively training and incorporating additional techniques into the model, like additional modernity. But I think we were basically too excited and we wanted to get this in the hands of folks faster.

And some of the feedback we got in early interest, lots of hospital systems, nonprofits that have tons of genetic data and For example, they know there's some kind of condition or symptom for the patient, but they can't figure out which parts of the DNA are causing it. So they've got these VUSs or variants of unknown significance

that we're extremely excited to apply these models to and actually help diagnose a lot of these patients is one example of a real use application.

I'd like to talk more about the applications in a bit, but I am curious, just from a technical standpoint, what does it look like? What does it mean to align a genomics model? I can imagine with large language models, there's a sort of natural chain of thought, you know,

Yeah, I mean, I think in many ways one could describe it as fine tuning, but then

And introducing, I'd say, sort of the key components are the right structure of the inputs. So feeding them in a certain sequence so that the model is aware that a certain task is being asked of it. So there's a mix of special tokens to basically you can think of as like,

if you're going to do disease prediction for, you know, for disease A, expect this special token, right? Just kind of like a way to prompt it. If you expect it to do design, have another special token and then showcase the examples kind of like in a chain of thought manner,

meaning showcase a sequence of desired outputs and the trajectory of it. This is a little vague sort of intentionally because it's part of our secret sauce that we're still developing. And over time, we want to showcase more and more of it. But But in many ways, it does mimic a lot of the natural language community.

A lot of it is fine tuning, but really it's also carving out specific data sets that you want it to focus on and then structuring the questions or tasks in specific ways as opposed to pre-training. Pre-training is really just feeding it in and everything in really.

And just doing next token prediction or mask infilling if you're doing mask language modeling. And it has no sense of like this Q&A type structure where you have a question, you know, a prompt and then an output. And you can think of mid and post training as starting to showcase given this type of input.

I expect this type of output, whether it's score, prediction score or design is largely possible. The mid and post training. The post training also includes things like reinforcement learning too. But I think the bigger steps are, you know, introducing structure of like question and answering.

Do the models have multiple heads that are task-specific? Or are you training one set of heads or whatever that can answer multiple questions at the same time? Just change the input tokens or whatever?

Yeah. Broadly, I think we're flexible on this. The idea... Yeah, sometimes you can use different heads, but the idea for us is to unify more so. And so I think early experiments, we did have different heads, but in some cases, the different heads do better. In some cases, a single model does better.

And so I think we're flexible on that, but I think broadly the direction that we are moving toward is Is a single. And the reason for a special motivation for that is that we're trying to unlock a lot of modality, a lot of generalization. And I think the more unifying we're able to make these models,

I think that's when you see more emerging capabilities happen. And in large part, that's what motivated the DNA work. We felt like a lot of models were specialized into other modalities, a little more downstream from DNA. So like RNA or proteins or molecules, we largely felt DNA is the foundation and that from DNA, you can learn And

I think other modalities is sort of like additional context that you're showing the model. That's how I kind of view it philosophically in my head. But yeah, the idea that single models unifying across modalities, scales is what the lab builds and builds toward.

Can you walk through a few of the tasks that you talk about in the blog and just explain and remembering to, you know, narrate for the listener only audience, but talk about some of these top line results and you can maybe dig into them a little bit.

Sure. Sure. One of the areas that we thought was really interesting for showcasing in this particular release for Omni was on understanding variants and their effects, which are essentially in DNA, a change in a position, you know, changing the letter of one of the other three letters in your genome in DNA. And in many cases...

Because the combinations of these changes in the genome, over 3 billion letters, right, is so vast that for clinicians and scientists, we actually know only a very small portion of which variants are causal to disease. And so there's these benchmarks from folks who collect variants, different hospital systems and clinics,

and some are known and some are still unknown. Folks have created some benchmarks from ClinVar or Trachem to basically the idea is given a mutation in a DNA, can you tell if it's going to cause a disease or not, right? They're probabilistic. And so when you do make a change,

it basically can modify its confidence or probability of predicting an X letter. And in this case, we've sort of leveraged that predictability of these models. They've essentially seen and been trained on so much DNA, in particular human DNA, they kind of understand what's common, and usually common or conserved across different other folks, usually typically means healthier.

And so if it's less common, you can think of it this way, if it's less common, the model can pick it up and sort of predict it. That it's potentially pathogenic or disease causing. And so we've taken some of these benchmarks. And when you introduce a variant or a mutation, there's different types of mutations in variants.

So sometimes you can delete a letter altogether. You can just flip it. You can remove big portions of the DNA, but these are generally single variants. In this case, this is where previous DNA models really struggled, especially on humans. And so we showcase that not only is it competitive or capable for humans,

but in many cases, it's state of the art. And actually, most of these cases, it's state of the art. And I think the exciting part is that areas where other models that were You know, currently on the frontier, they still were lagging behind quite a bit in terms of where in the genome.

So in the genome, there's coding and non-coding regions, like protein areas, protein regions.

Meaning areas that are actually coding the structure of a protein versus other areas that do other things like regulate what genes are expressed.

Yeah. Yeah. And so these non-coding regions are largely regulatory. They kind of control how much or when to use a certain gene or turn them on. And in many cases, these non-coding regions, these regulatory regions, variants there... Mutations there are much harder to predict if they cause disease or not.

And I think what's exciting about the new generation of models we're building with Omni is that that's where we shine, especially. The models are able to pick up mutations and be able to distinguish if it's disease-causing. Yeah. You know, one and a half, two percent of the genome.

And turns out many, if not most of the diseases are in these non-coding regions. And so there's been a real desire to build models that can actually pick up these variants of disease causing variants in these non-coding regions.

I have several questions. First, just while we're here, you know, for the listeners, there's this column on this benchmark chart called Bordzoi, reference number four in the blog post. I think for maybe some historical context, could you talk about what this column represents?

And, you know, maybe this also helps give context for, you know, the Omni column on the right.

Yeah.

Yeah.

Yeah, great point. So what we show in this benchmark here is really taking some of the representative models or the strongest models in the deep learning side and also in the traditional methods. So we have EVO2 is the latest previous genomic model that our team had worked on.

And then Borzo is, it's also a DNA model, but a very different kind. Essentially, it's a supervised model that predicts from DNA functional genomic tracks. So it too is inherently multimodal, but it's not a language model. So it doesn't predict like a next token prediction. It goes from a DNA sequence directly to

a functional genomic track like chromatic flexibility or gene expression.

And these tracks have been annotated extensively by people writing their dissertations and all that.

Yeah, yeah. Right. So the big difference there is that it's a supervised task, right? So it requires labeled outputs. And in our case, these language models, they do not require labeled outputs, right? So you're doing raw pre-training on annotated. So, you know, why is that desirable?

Well, there's a lot more data, a lot more genomic data that's not annotated. Actually, most of it, pretty much in many ways, almost all of it is not annotated. And so being able to learn from an unsupervised manner, hugely desirable, right? For us, we wanted to showcase the benefit of pre-training on raw genomic sequences and,

you know, Comparing it to state-of-the-art models in other spaces in DNA.

And so your prediction is when you say it's unsupervised, how does the unsupervised property work? Like how do you convert the output of whatever your model is to an actionable like ranker, score, whatever?

What I talked about before is to train the Omni model, it's pre-trained, so it's unsupervised, but when you're pointing it at a specific task, there is a supervised step. So it's taking a smaller data set that is labeled, but essentially what we're doing is using the likelihood scores. So the raw outputs of the language model,

which basically you can think of it like a probability for predicting what the next letter is. We can essentially showcase the Probability score, the likelihood score for the mutation versus the wild type. So that's seen in the reference genome versus the mutation in this particular case. And then we'll have two scores.

And then you can think of it as like using a ratio of the two to showcase basically how different are you from, how different is this mutation from normal or baseline basically. And then that's, you can think of it as like a surprise factor. That the model is able to use and leverage.

And then we can use that to essentially score an actual prediction for disease or not. Does that make sense?

Yeah. So Omni autoregressive is that, or is it diffusion or something else that you can't tell me?

Yeah. Yeah. This time we're not describing the exact makeup, but Evo was autoregressive. It was the first large scale autoregressive. And so I think For us, we don't tie ourselves down to a specific training objective. We use every tool in the toolbox, essentially.

Okay. But for the specific benchmark, you're going along and you're just using The likelihood distribution of, you know, the tokens and some tokens are, you know, the model thinks these are unlikely. And that is probably because some evolutionary constraint, like this doesn't show up often. And because it doesn't show often across genomes,

it is probably going to cause problems and, you know, people will not survive. So on. So you think that is a basically your Your ranking metric or something.

Yeah, it's one interpretation of how the model's thinking about it. And very similar to in natural language, you can describe the same kind of paradigm. And there is additional case in mid and post training to leverage more than that, I suppose, because we can teach it specific structure and benchmarks so that It can build

on top of what you just described, which is like what's common in nature, but also because it's a specific task for disease variant prediction, then the model has additional training introduced during mid-training to showcase and to add additional learning power, essentially. What are some examples of that?

Again, probably secret sauce to some extent, but can you give just a gist of what that looks like? What are the kinds of things you would throw in there?

We would actually throw in the score to itself. So, you know, like I mentioned a ratio, it's a ratio of wild type versus mutation. I would say that's more of a zero shot method where you don't even have to do any mid training. And that's what EVO 2 is doing in particular in this column.

So EVO 2 is not fine-tuned, essentially. There's a EVE column, which people are basically fine-tuning, you know, using them scores from EVO 2. That's from Goodfire. And that's also, you know, folks that We greatly respect and they kind of showcase that these models are able

to be state of the art when you can fine tune them as well, not just zero shot. And then our model is introducing sort of a step about that, not just fine tuning, but also introducing structure. By structure, I mean the format of these benchmarks into the model itself.

That Q&A style formatting during mid-training, which is what gives us an extra boost even. I see. An extra boost, but I think the other benefit too that we didn't Emphasize too much in the blog, but I think it's really convenient for practical use for scientists is

that you don't you're doing this without taking the embeddings and then tapping on ahead and then, you know, doing some regression, which is the extra step. It's extra hurdle. Can you imagine if Chachapiti? Like every time you ask a question, you had to like fine tune it for a certain domain.

We've done it so that the model is flexible during mid-training to be trained on many tasks at once. And so that fine tuning, that last step of training the embeddings doesn't have to be done. It's out of the box at that point. You just prompt in a certain format and it will,

you know, that certain format tells it which tasks you're going to do. And then we'll output the answers in that, in the desired format, basically.

How careful were you in designing this post-training scheme to avoid kind of data leakage with the ClinVar trait gem, RNA gem, and so on? Like these data sets, like how confident are you that there is no data leakage, either like accidental or something upstream? And that, you know,

because I would not be surprised if a lot of these sequences showed up also in your training data, even in a, you know, unsupervised sort of way.

Yeah. The short answer is we're extremely cognizant of the risk of data leakage and extremely hard to not mislead or, you know, be careful. And so we have bioinformaticians that are able to basically comb through the data and curate, dedupe and align sequences to make sure that things that are similar potentially

to what's in the benchmark are not there. And if they are there, we remove it. And so, yes, we actually have steps to QC the data quite extensively.

Yeah, cool. Yeah, I guess maybe before we move on, I think it's really cool seeing that there are these supervised methods, which previously several of these numbers were, let's say, within the error bars, if not just straight up beating what came before them. And now you have... Yeah, we're super excited.

And I think for the longest time, there's this area of this other method called CAD, which has been state of the art and state of the art for a reason, which is what they sort of by design, they'll take the best methods and kind of do Do an ensemble, right? So they'll take up another,

even if the best method is another previous model, they'll mix it with like an SVM and just like throw the kitchen sink at it. And so you can see why it would be the best, right? And so that was the bar for us. We're like, if they're going to throw the kitchen sink at it,

like we're not going to cherry pick one model and say we're better than that. We need to beat what's possible, humanly possible now, like across everything. And so, yeah, our researchers were like, We're setting their sights on that to see if they can actually improve performance across every method.

I'd be interested to see there's some discussion of chain of thought. And that broke my brain a little bit when I was first... First hearing about that, I'm really interested to hear about what that even means. Yeah. I had to pour through the blog post to really understand that.

Yeah. Yeah. I think this is really just a taste of where we think the design capabilities can move toward and be more usable for folks. So chain of thought. Yeah. Stems from natural language community. I believe Jason Wei at OpenAI showcased the first examples. And really what the breakthrough there was showcasing

that these language models perform better when you just show your work, essentially. You show the steps of how you came to a conclusion or an argument. And it turns out, even if they were like simple steps, but it just gave the model a chance to Maybe it's sort of like philosophically who knows exactly why it works,

but essentially feeding more tokens in and giving it more scratch space to think. And so people just think this is sort of the beginning of reasoning for these language models, this ability to kind of... Get to an answer by thinking to itself by itself. And so it seemed quite successful in language, very successful.

And that's why you have a lot of agents that just spent tons of tokens, right? Just showing its work, right? And in biology, we saw very little of that. We started to see some of that in protein design a little. And so we wanted to push that and showcase that, you know, we're Is that possible in DNA?

Like, what does that even mean in genomics? Because you don't really have words that describe, you know, it's thinking. So how do you take that same paradigm and introduce it to a DNA language? And so what we did was a simpler version in many ways. We had this data set of RNA aptamers.

So just think of it as these desired sequences with some kind of fitness score associated with them. So we took this large data set that had RNA input and a fitness score. The fitness score go high. It's good. The simplest version. It's a big data set. And so what we wanted to showcase was that if we show

the model progressively Can the model continue that trajectory on its own? And then, you know, in the final step, does it self-optimize to a point where it's like the best That was the experiment. Can we do that? And so we took a data set, a large data set of aptamers.

We held out a portion of the best performing ones and we showed it only the lower ones, but then we ranked it. So we showcased lower scores with the RNA aptamers and then progressively got higher and then asked the model to just continue with that pattern.

And it turns out it was able to And recapitulate some of those higher scores that we had not shown it yet. We were actually in the process of validating the wet lab right now. So we didn't get to show it here, but we wanted to know, right? Actually, can it not just do this in silico,

which it can, it showcased that it was able to continue And now we think this is a, you know, obviously, if this works in the lab, we think this is a hugely, hugely valuable paradigm that can be, that can be pretty And if we can get models to eventually learn that structure and, you know,

basically just show a series of progressively stronger sequences, the model can then predict the rest. That's a very powerful paradigm.

Honestly, a bit surprised about this, that specifically this task saw strong improvement. Maybe my personal bias is coming in here, but RNA is somewhat notorious for not having good co-evolution data in terms Yeah. Yeah. I mean, I'm wondering, like, genomes carry lots of different information. They code for proteins, they have regulatory elements,

and, you know, different types of genomes have different types of structure. So I'm wondering, where do you think this capability might have emerged in this language model? Oof.

That's a good question. And honestly, I'm not sure. We're surprised too. One, because the model is pre-trained on DNA and it's really just like mid-trained on RNA very, very, you know, in a small way. Yeah, I think what your intuition about the DNA having a lot of evolutionary effects or information is probably where.

And so I think this is hinting at the idea of Mm-hmm. What I didn't talk about for the company as well is this idea of a building toward general biological intelligence where we are unifying a lot of the different so-called languages or modalities of biology. At the end of the day, they still... Stem from DNA.

And I think people have not exploited that fact as much. It's usually really specialized, the domain specific model or modality specific models and not leveraging a lot of inherent shared structure from other modalities. And so one example of that is like, you know, when people talk about virtual cells, there's a little bit tangent, but, you know,

they tend to focus on just RNA and, you know, transcripts and they Want to generalize to describing an entire cell, but obviously a cell has a lot more things than that. In my mind, if you want to learn a system, you want to learn from all the signals or sensors of that world or that system. You know,

if it's a cell, you want to fuse, you want to understand the DNA, you want to understand the metabolomics, the epigenomics, the proteomics. And that's when you get closer to like, quote unquote, a virtual cell. And in our minds, we don't even want to stop at just the cell,

but we want to fuse all of these sensors across all of biology. Will it get us to a super intelligence that understands every component of minutia of biology? Who knows? But I am confident that this type of paradigm will get us a hell of a lot further than we are now. Like that's my bar.

Can you make something far more useful than now?

So I'm curious, are you focusing on eukaryotic cells? Are you focusing on like human genomes? Do you have you gone so far as to do viral genomes? I mean, there's a lot of DNA viruses, but it seems like possible that. There's a lot of RNA sequence, virus sequences out there.

And I'm not sure fundamentally they would be much different in terms of training. I'm curious, what's the scope of that, if you can talk about it?

Yeah, absolutely. We are interested in all domains of life. So here we focused on humans in particular because we thought this was an area of previous models, EVO and EVO2, were not as strong and sort of got a lot of So we want to showcase, we think this

This is actually useful and it can be applied to humans. And it's sort of the most complex of the complex in some ways. But I think there's opportunity to apply these models generally to every form of life. So we absolutely are interested in pro carryouts and vitality.

Viral in particular, we care about it especially for biodefense and biosecurity especially. And I think there are also lots of therapeutic applications that we can learn from microbial life of, you know, maybe obviously for some folks. In particular, they mentioned that folks had used Evo to generate The first AI genome, a bacteriophage.

Turns out you can use bacteriophages potentially for AMR or antimicrobial resistance. You know, if you have a superbug bacteria infection, which in the world is about 2 million deaths from bacteria infections still, the idea of Using viruses, designed viruses to target specific bacteria has been done for a long time, particularly in Eastern Europe.

And there's a potential to make a new class of antimicrobials that are Not like antibiotics, but very similar that can be used just like it. And so I think we're gravitating toward things that are high impact and the potential to save lives. And so we don't stop at just one type of genome.

I think we're interested in anything that's beneficial to humans.

Maybe going back to my question about SOLEX and RNA predicting kind of a chain of thoughts of RNA evolution. I'm curious, was this model trained on RNA sequences or sequences which might have evolutionary pressure on RNA structure? Only during mid-training. So pre-training is all

just genomes in DNA. And so the only time we introduced RNA was for this specific task where, and only RNA from this data set. So not even outside. I see.

So this really was something along the, there is something encoding RNA structure in this model to some degree, maybe.

Or either that or... Implicitly. Yeah, implicitly. I would say implicitly. That's cool. Yeah, because I'd say sequences, as we know from proteins, implicitly should learn structure from just sequence. Yeah, and so we don't add in 2D or 3D information at this point, but we absolutely plan to. Yeah.

So just so I understand, first of all, the chain of thought idea is, this is a demonstration of it, but the idea is that anything that you can get sort of a training set that has a sequentially better measurement of some sort is maybe a candidate for this technique.

And so can you just describe for this particular experiment, just so we can understand how we're mapping chain of thought to... I know this wasn't your data set, but how was the data collected in such a way that you could map accurately from fitness or whatever to a particular phase or part of the data set?

Yeah, so I'm less familiar with how the data was actually generated from the experimental viewpoint, but they are validated from a wet lab in the real world when it was collected. So it has some kind of fitness score, I believe through...

I can maybe provide a better context on this if you want. I mean, so the idea here is you just generate a bunch of random sequences and then you take those sequences and so you have like an aptamer structure, which is essentially like a switch with RNA, which sort of When something binds to it,

it will do something like cleave off a sequence. And you can use an NGS, like Big Generation Sequencing Readout. I'm very high throughput. So you create lots of these different sequences. I guess in this case, they were targeting a Specific HIV protein or genome or something.

And if it binds, you basically get the signal of you get more reads of that. And so the more time, the more sequences which are floating around to Kind of like the more fitness, the more likely it is to bind. And then you take those and then you mutate them again and you kind of iterate on this.

Right.

So you have this iterative experiment where you're progressively using the Petri dish to basically identify the most fit thing. So and then what you're doing here is you're basically doing this same experiment in silico.

And they're actually doing very high throughput. Like I think there's like 10 to the 11 or something sequences. Some like... Really high number of kind of sequences explored in parallel for this experiment.

But the key is the biology of the experiment is actually doing the filtering, right? Yes, yes. Yeah. And so you can imagine other types of experiments where you could apply the same kind of idea where you're doing this like progressive refinement of something which is very common in biological lab work.

And so if you're capturing those intermediate states and you can maybe feed them into the model and...

Absolutely. Yeah. So another example is for the antimicrobial resistance. I think that's something we're very interested in as well. And the ability to selectively target specific bacteria strains or kill bacteria strains. Yeah, that's measured basically a score zero to one of how effectively that is done. And so should Showing progressively more effective phage genomes

and their associated scores for effectiveness fits that paradigm very well. There's another design task that we're working with a national lab to do this with as well. And an area that is quite different for us, but it's on designing proteins to extract rare earth minerals. Right.

And so it turns out that you don't just care about proteins that could bind to something, but you want it to be selective. You want it to be bind to one type of rare earth mineral. And so you have scores associated with how much affinity or binding affinity for each type of mineral.

We want to essentially do the similar exercise with Rare earth minerals and show it a series of progressively desirable scores, not just for binding to this, but lower binding scores for other ones. You can selectively do it. So I think the creativity in which you can showcase sequence and desirable sequence

with some kind of fitness or functional output is a relatively intuitive way for people to design just by prompt engineering essentially, which I think is very exciting to see. To explore more.

Following up on the rare earth mineral extraction, I find that is an interesting use case for this. In fact, maybe one where you probably wouldn't have a comparative advantage compared to some other techniques because it seems like your strengths are probably And I'm curious, like going to talk about ClinVar,

the argument here is that the model now is a really good statistical reference. Representation of what type of mutations are common or not common. And I think in order to do design as a, if you want to design structures, I think you want to understand structure.

If you want to understand disease, I think that is, I think, more natural. For many diseases, it's much more natural in terms of like a population genomic sort of way. So I'm curious, where do you think your strongest competitive advantage is? And do you think that your model understands structure in addition to function?

Yeah, I'd say what drew us to this particular application, Rare Earths, and our strengths in general, why we thought it might be suited for it is two things. One is, I think in areas where... Yeah, you're right. And what matters here possibly is certain microorganisms with proteins that have the function that we desire.

We can potentially prompt and provide us context for this is the neighborhood in which, you know, Tell Omni, this is the neighborhood of genomes or microorganisms that you should search for new proteins. So it's really sort of like a mining exercise. And what we can showcase to our models that other folks can't, you know,

like Protein structure models is that we can feed in non-coding regions before that gene of interest or that protein of interest and then ask for the model to provide variants, essentially. So like mutate this protein, but know that... That you're in this microorganism, but show me different variants that you've seen in nature

or combine different things that you've seen in nature given this context. And I think that is one reason why we can make very evolutionary diverse sequences and potentially phages. Folks have used EVO models to do this with toxin and anti-toxins in a very similar technique. They've prompted on things upstream from the proteins of interest and then asked

the model to kind of generate a bunch of plausible other ones. And I think that's... In this case, for rare earths, that's super exciting because then we can come up with plausible variants and then test them relatively simply for what they bind to and selectively bind to, which I think is really interesting for this partner who cares,

for example, about securing the supply chain of rare earths for the U.S. strategically. And so we thought that's absolutely worth something that...

It's worth supporting. So your point is not just you're designing a protein, but you're designing an organism which generates a protein and this protein has an action. But for yours, it's that the way to design this is you need to understand how through the tree of life interactions of proteins with rare earths have or

with certain minerals have occurred.

Yeah, I'd say in this particular case for like the rare earths, we're not really interested in the organism, like designing the whole organism, but I think the organism does tell us about what proteins are plausible and their selectivity is not, or the way they evolve. And so I just think of it. Going back to that word,

the context, I think context matters in many of these applications, or at least in some of them.

Yeah, I think context matters a lot in biology. I think maybe one of our big bottlenecks is the lack of context and how We as humans mostly approach biology in terms of a very engineering, like let's isolate individual systems and systems biology approaches very hard to get any sort of meaningful quantitative predictive power.

So maybe going off on a tangent, but I mean, I'm curious, you know, going to context and thinking about how context scales to an organism, you're talking about right now, two million length context, right? You know, I think the human genome is roughly, you know, a thousand times longer. So... But even like a lot of, you know,

say bacterial genomes, if you're trying to engineer them, are quite a bit longer than that. So how do you leverage something which has a long but still finite context compared to do synthetic biology across like large organisms? Maybe for context, how did the EVO2 bacteriophage design work,

which was probably much more than 2 million for that as well?

Yeah, so I could speak to the evobacteriophage just a little bit because it's actually a separate group that worked on that. But that context was actually pretty short. Actually, the reason why they started with phages is because it's amongst the shortest genomes. And so I believe it was something around 6,000 base pairs. Oh, wow. That's really short.

Yeah, yeah, yeah. So extremely short. Viruses are insane. They're incredibly efficient. They packed a lot in there. Yeah. Yeah. But yeah, no, I think your question about how do you get longer contacts with something smaller is a very key question that we, I think broadly the AI community is constantly trying to fix and And so, I mean,

I think that's a large part why we as a company are an AI research lab first, because we think the innovation needs to be constantly pushed. It's not a space where we can just grab open source models and And expect that many of the tasks that we care about are just going to be solved.

We want to continually push the envelope. And so context is one of the key researchers that we drive in. I would say that's probably how we got our name because we worked on long context before it was a... It was a thing, I guess, like 2023, 2022, long context.

You and your team, I mean, your collaborators have a long history of these space models doing, you know, pushing context, like what seemed insane. Yeah. Yeah, absolutely. Yeah.

And they're like, wait, did someone say kernels? And they start trying to figure out, you know, how to make things fast. Yeah, long context was a special place in my heart because that's what I focused on in my PhD at Stanford.

And that's how we started thinking about DNA and, you know, going back a little bit for fun. We were looking at working on language models in general. And then we noticed our models were good at long context. And so that's the progression of like how we started working in the space was like,

oh, these models seem to be really efficient on long context. And then with Michael Polley, my lab mate, he worked on the first design of Hyena, this convolutional architecture. And then we started thinking like, let's push this further. Let's see what new applications open up if we really lean into long context.

And we asked, what's the longest sequence out there? And eventually, unsurprisingly, we landed on DNA. We were like, DNA has got to be the longest, 3 billion base pairs. And we started thinking like, okay, what's being done there? Like what kind of context lanes are people doing there? They were doing super sharp.

They're doing like 1 or 2,000 base pairs or tokens at time. It's like, you know, way smaller than what one would want for DNA.

I mean, most human transcripts are like 3K or so. So that's not even like, you know, most, that's not even what you need to represent like a protein or most of the time.

And so it's clearly a need there and overlooked. And we saw it as a way to initially, like, let's see if we can do something that we had no idea if it was going to work and no idea who would want it. And so we just started tinkering around and it turns out out of the box,

relatively It was doing pretty well at reading DNA. And then it led to, okay, people keep asking about DNA. They didn't really care about our language stuff as much. And they would say, can you do longer? What can you do with it? They always ask, what can you do with it? We didn't know really.

And then for some reason, it latched on to this idea of like, well, no one's writing DNA. Can we get it to write DNA? And that was a really simple question, but In hindsight, it almost seems obvious that, yeah, you would want to write DNA and design it.

But when I was first pitching the idea of Evo to folks, I spent six months, which I guess in BioWare is not that long, but I spent six months going around saying like, hey, if I generate DNA, would you find that useful? What would you do with it? Would you back us?

Would you want to be a part of this? And crazy enough, almost every scientist at Stanford I talked to thought it was a stupid idea. Yeah. I was like, this would be so cool. Generating DNA, how much would we accelerate the field? And then people would say, what would you do with it? I'm like, I don't know.

And then I would get that comment or comments like... That's not possible. We as humans don't understand the rules. How could you expect an AI to learn it? You can't even tell if it's right or wrong. You can't tell the AI, yes, that's right or wrong. How can you expect it to learn it?

Or there's too many repeat characters or DNA is too noisy of a distribution. There's no real rules and there's just a bunch of junk in there. I heard all the reasons and I was just so stubborn about it. There's got to be a use case from being able to generate DNA. It just feels right.

And I didn't know what it was. So it really was an experiment of like what happens. And so when we first trained Evo, I remember we had no idea if it was going to work. We had no idea. We didn't know what thing was going to emerge. We just thought, let's just train a big one.

Which is kind of ridiculous. But somehow, you know, folks at Arc, they're like, sure. Yeah, why not? Why not? Let's see what happens. Let's pay some money for the GPUs and let these crazy kids train the model. And I remember when the first result came back and it kind of gave us chills of like, oh,

maybe there's something going on, which was somebody took the model checkpoint, the first one, And threw it at a protein gym, one of the protein benchmarks and turned out to be competitive with protein specific models. And we were like, okay, that is pretty surprising because we never told the model what's proteins versus not.

And there's actually, it was, you know, there's also protein and DNA, right? So there was one piece, I think it was just surprising that it was actually competitive with protein specific models. And this was like the first experience And then they just kind of kept on coming one after another,

like, oh, this competitive here, oh, it's state of the art on RNA and DNA. And we started seeing like, oh, it can learn across different modalities, like not just DNA. And then we felt like, okay, there's something there. And so So it kind of went from there.

And then, you know, folks at NVIDIA were like, let's back to Evo 2. Let's make this even bigger. And then Greg Brockman from OpenAI was like, I'll take a break from OpenAI and take a four-month sabbatical and like help these crazy kids out. And, you know, then we're Slack messaging Greg Brockman at 3 a.m.

trying to debug our code, which is wild. Yeah. So it just, it went... The trajectory was very surprising in many ways. But at the same time, you still got a lot of feedback like, you know, what are these models good for? What are they, you know, what are they useful for in the real world?

And so that's really motivated us to start a company. We thought what we showed was just really just the taste from like an academic flavor. In a similar way, the language models, when they first two, you know, for natural language came out, people asked similar questions like, what are these things good for? Oh, cool.

It can write some jokes for me. Is this going to lead to like an all All, you know, I'll come to see AGI that can automate everything. They did not think that, right? They thought it's like a toy. It's got emerging capabilities and they would extrapolate the potential. And in many ways,

I think what we're seeing here is even more exciting or reminiscent of that trajectory for DNA.

But EVO2 even was showing the bacteriophage and that wasn't a persuasive. I mean, that's almost a scary example, right? As you mentioned. So... That people didn't see that, like that isn't a light bulb moment for people.

Yeah. So, I mean, some people, right, I think either fair or, you know, rough critiques, you can even, you know, play devil's advocate and say what it's generating is kind of, you know, pretty close to nature and you're kind of recapitulating. And so there's, I think there's a lot of ways to critique and kind of,

you know, minimize the potential, which can be fair argument. Like, so I think at this point, we think what is more important is not just pushing on the science and like, cool, this can be done. And like, Kind of leave it there as a sort of thought experiment. But like,

how do we actually use this to improve human understanding of disease, improve treatments, make better rare earth mineral extractors? How do we actually make this useful is what we care about now as a company, in addition to some of these more scientific questions.

So maybe that's a good segue. That brings up two things for me. One is the McInturk. Stuff that's in the end of the blog post and then also the biosafety stuff. Those are both, I think, important applications. So let's do McInterp first. Can you talk a little bit about...

And this is actually kind of building on the work that Evo did as well, I think. I remember in the Evo paper, there was some McInterp work in which they were discussing using... Reversing the question and using the model to extract insights about biology. And this has actually become a common theme with, I think,

maybe biology more than any other domain, is that people, because it's a scientific question and it's learning patterns about the world, you can actually say, okay, well, what patterns did you learn?

Yeah, so I think Mechanterp is an emerging field in bio that we're extremely excited about. And admittedly, we are on the early side, I'd say. So we're building up that team. But so far, what we've showcased and been excited about is looking, really analyzing the embeddings and some of the activations in the model.

And so this idea of Mechanterp for bio is borrowing a lot from the natural language community currently. You could think of what the models are doing as compressing And so in this compression, it's really basically distilling it down into the key components, key patterns that helps it understand the data or learns the distribution the data.

And so what we're trying to do is probe the model. And so for us, we started off with a lot of the outputs of the model, so the activations, and we wanted to see what kind of structure, what kind of visualizations

Can we see that help us understand some of the complexities of DNA, which is a ton, right? And so some of these complexities can range around GC content, certain motifs of transcription factors. There's a bunch of regulatory types of patterns and motifs that the model,

we believe, Has to pick up to be able to do its tasks, right? To understand whether a disease is caused by a variant. And generally, it's going to compress all these different motifs and distill them into the model weights. And so our job is to then find these and see if we can distill a pattern

or structure that can be generalized to other cases where we don't understand the patterns, right? So that's sort of largely the goal. So in this case, GC means the two nucleotides that are...

The fraction of those

in a sequence. Exactly. Yeah. So the fraction of the G and C letters in a genome, which I guess is amongst the more simpler things, but also, you know, simple things as repeats, number of retiefs. I think transcription factor or TF motifs is another. One that is especially interesting for folks,

because eventually we're going to get to a case where we can design transcription factors, meaning we'll have certain transcription factor patterns via like ChipSeq modalities.

Transcription factors are, well, you can go ahead.

Transcription factors are molecules that combine to DNA and they would alter essentially the gene expression pattern. And so it has this regulatory effect that doesn't modify the DNA itself, but can modify sort of the effects of DNA in the products that DNA makes. And it can have a lot of implications on, well...

Pretty much everything in your body. So it can modify disease states, it can modify, I guess it's a lot of aging related research is around transcription factor design. And so we think being able to understand some of the motifs via DNA, but also additional modalities will eventually let us be able to design transcription factor patterns as well.

And so I think this is very exciting. In many ways, the combinatorial space of learning these transcription factors, like what binds and where they bind and what effects it causes, is just far too vast to be able to do this in a manual way.

And so we want to take a data-driven approach to learn some of these motifs.

The complexity here is partly because the transcription factors themselves Coding genes. And so that you can write those can regulate each other. And so that you have this that's where that combinatorial effect. Yeah. So like just narrating for the listeners only, we're kind of marching through these increasingly complex

and higher level factors all the way from GC content. We started now we're looking at disease, which is maybe the most complex thing you could or you were Yeah,

so I think what we, our first idea for previewing this was, and what we're working toward just broadly, is this idea of mapping the manifold of disease, right? So manifold, there's like the sort of representation space of what disease looks like to a model, right? In terms of the output scores or embeddings,

we believe that there's a lot more structure that can be gleaned from understanding some of these outputs. And so, you know, mapping this manifold or the landscape of what the structure of disease and obviously as many diseases. And so I think would be A big,

exciting area of research for us to actually drive motivation for mechinterp in bio. I think we're just really scratching the surface because if you can get this much of, clean this much of insight potentially from just DNA, which is in my mind just one of the sensors that you want to ultimately fuse into, you know, modeling biology.

Then being able to do something similar across all modalities is something like, by all modalities I mean protein, RNA, epigenomics, you know, the attack, chromatin accessibility and methylation patterns. All these other different types of sort of molecular phenotypes around DNA just presents such a huge opportunity

that is kind of laid in front of us that is all green space, green green field. No, I haven't seen anybody do this level of sophisticated techniques from, you know, machine learning, deep learning into what I think is going to be the most important impactful process. Area of understanding and applications for AI. That's what we're excited about.

And I think we're just showing a preview, a very simple preview from the DNA only models. But in our next generation of models, which will be increasingly multimodal, we're talking dozens, it's a very exciting moment for us to showcase. Sidebar on that is language,

natural language, one of the most

Not yet. Yeah, but it will be. So I'd say there's a lot of questions about how to fuse that with bio, but I actually think it's pretty, will be relatively straightforward. I think the more tricky, the tricky part for us is actually how to fuse the biological signals more so.

Fusing language, there's a lot of examples with that, with image and video space. So we feel We're pretty good about that. And we've done some early experiments with language, and I think that will make it extra accessible for folks when you can connect it to language. But I think the part,

that recipe that folks still are trying to figure out is how to do this across biological modalities. It just seems like a natural way to be able to do chain of thought, right? Exactly. Yeah, absolutely. And I think, you know, especially when you start having a chain of thoughts from orchestrating tools, things like cloud science,

I think the idea of incorporating language is already in a lot of people's minds.

If you don't have any

questions, let's talk about the biosecurity. We as a company thought it was very important to have a dual mandate, what we call a dual mandate. It's this idea of essentially being cognizant and feeling responsible or wanting to feel responsible for the capabilities that we're enabling on the design side.

So if we're going to create models that can design function into sequences, we believe and see a gap in companies being able to Safeguard that technology and make sure that it's used responsibly increasingly more. I was just at a panel last night, a panel on AI scientists, agents that can do scientific discovery.

And one of the last questions was, what are What are some of the biggest risks or doomsday scenarios with AI learning about science? And every one of them talked about biological weapons. And at the same time, I was curious because I was like, okay, so then what are any of these folks doing about that?

And basically, I didn't hear anything about that. And I, you know, these companies, I won't say their names, but, and I look at the companies, they don't have big efforts in those spaces. So anyways, we felt it was important as a lab, in the lab, that we A team that was both building

the design capabilities is actually also best suited for building the defense capabilities because they're basically the same models. A model that is good at generating turns out is also very good at discriminating or predicting if So we felt it was not just, you know, from a principle standpoint necessary to work on both bioscurity and the design,

but that it was, you know, strategically, it just made sense as well. And so we felt this resonated with And so, yeah, we felt it was necessary to build it into our mission. And so for us, what we have done and plan to do, When you look at it, or I should say biodefense,

biosecurity sort of has three or four different pillars of strategy for biodefense. The first one is around detection and surveillance. Broadly, can you detect from the environment if a sequence This sequence has a pathogen in it, something that can cause disease. Let's say from, you know, swabs at an airport, a nasal swab or a sewage system, right?

Collecting samples. The next is attribution, which is once you detect danger, Can you figure out where it came from? Is it natural? Is it from, you know, a random country abroad? Is it engineered by a human from a specific lab in a country? And that helps you figure out, you know, what to do about it, right?

So this next idea is around countermeasure. So once you've detected, figure out where it's from, what do you do about it? Can you make a counteragent? Can you make an antiviral or antimicrobial? And then the fourth one's generally about deterrence, but that's more of like a government kind of level thing.

But yeah, so we focus primarily on the first three. So we create tools that can, given a sequence, detect if it's pathogenic, but also what we felt was missing from the community was not just detect, you know, broadly if it's pathogenic, but characterize the heck out of it, meaning what Parts of the sequence are dangerous with genes,

for example, attributing where it came from, being able to not just look at its, you know, sequence and match it to a database, but be able to attribute its signatures. And then also a big component to make this effective in the first place. The community, the biodefense community, broadly focuses on sequence information.

So they'll take a sequence and they'll basically align it to a known database and say, have I seen this before? Does it match this list of known pathogens? But I think what's emerging and a concern for a lot of labs is, well, one, new stuff, right? If it's not on your list. And two,

things that were intentionally obfuscated to not be detected in sequence space, meaning the letters matching up exactly. But also function space, right? Because basically models that we're enabling now, they will be able to be function aware or structure aware. And so that means for concretely, you can have a sequence that has the same function,

like a pathogen, but actually look different in terms of the letters.

And you can imagine based on actually what we have on the screen here still is this Mechinterp thing. And there's this sort of manifold that the model constructs internally that is kind of coding for these, among other things, functions. And so that you can imagine how it would be able to say, oh, well,

that's maybe genetically quite different or at least somewhat different, but it still has a similar function.

Exactly, exactly. So what we talk about in our defense blog is this idea of things that can function similarly. They can start having separation in terms of what the sequence looks like while maintaining the same functionality, right? So this can happen in nature sort of naturally,

but also what these AI models allow you to do is also intentionally do that as well. So have the same function, functional capability, but have diverse letters, basically, diverse spelling, but describe the same thing, basically. And so in this case, this work from Microsoft called Paraphrases. So it's like, you know,

kind of reworking things where they showcase that you can, for example, use protein language models to. You essentially keep the same structure, which structure implies similar function, but then change the spelling, right? And not just that, they wanted to test that if you have this capability and you send this through existing detection Right. Right. Right.

Back a DNA molecule like it's an Amazon package. Like you just send it off and they'll send you the physical DNA of the design. They'll manufacture it for you. And this runs the scientific community, right? It's the pipeline that It allows people to do research and understand biology and make drugs and everything.

So it's prevalent and it's public. And so I think one of the concerns for folks is, well, and one of the concerns for us when we first started working on this was in a world, for example, where agents are prolific online. Presumably billions and trillions of patients building and taking all sorts of actions on the internet.

It's wild that they don't have any tools to basically tell it if it's making anything dangerous or not. And so that was literally our first motivation of like, we We should probably make something that can detect if something is dangerous or not, right?

Do you have a filter for these manufacturers that they can say, what am I making here? Is this dangerous or whatever?

Yeah.

And maybe you could have an exception if you were like some licensed lab or something and I'm doing something dangerous. I know I'm doing it. Please let me do it anyway or something.

All sorts of cases. So that's one scenario. To be fair, many of the DNA synthesis companies have detection tools, but I would strongly hypothesize that they're not AI-based and fairly, they're probably not as robust. Yeah, they're all pattern-matching mostly. Sorry, maybe this...

I should ask this question later. I'm just curious about, you know, we've all, everyone who is working in bio has tried to use Fable and instantly got picked out on literally everything you type in. My website, for example. Yeah, yeah. You know, you can't do anything in Fable without.

But in terms of people like scientists exploring synthetic biology and creating new sequences and designing new sequences, it seems like it'd be very hard to get To have an ROC curve, which you can live on, that doesn't impede novel scientific research for legitimate purposes. How do you avoid, even with an F1 of 0.99,

which you're not even close to right now, I think, that still could easily, if there are billions of sequences, Sequent generated a day or at least like a year. I mean, I think you could really have a lot of, it seems like a very hard balance to.

Yeah, it's a tough question, right? So I think broadly, the way we look at it is, you know, if we thought about like, how do we 100% stop the dangerous design? I think it's a harder question to ask. I think the question we asked is on the capabilities design side,

There's plenty of folks pushing the frontier of that. When we look at the defense side, do we see frontier technology being applied there? And the answer to that was no, right? So we saw this huge gap and we wanted to sort of aid,

come to its defense, I said, come to its aid to give it a boost, right? So I think that perspective, it's an easy choice for us to say, let's push, let's bring that to a better level. Head to head match against the design side. Is it going to solve everything?

Well, I think that's what we're going to aspire to be. But realistically, there's always going to be cases where it can get around. And I think that's a big motivation for why we think safety for language models and chatbots is one layer. But also, you're right,

there may be things that kind of just get out there, get past that anyways. And so what do you do about those cases is it's already past, you know, the chatbots, right? It's already aided someone into making dangerous sequences. So it's out there. I think the cool thing What we're building is tools for the folks that care

about things that's already out there, out there in the environment that's made it somewhere. And now there's this whole ecosystem that we want to build into that does the surveillance, that does the attribution, that does the countermeasures. We want to boost that community, right? And build stronger tools for that space.

Does it have to be perfect to be useful there? I don't think so. I think we can be helpful and move the biodefense community forward in terms of bringing So, threat model, it's not even clear what threat model you're actually trying to defend against at this point.

Defabilities don't currently exist at all. So, you know, you provide something and now this can be worked on with in terms of a larger regulatory framework or government or, you know, nonprofit, whatever larger framework is now provides you a tool that the community can build upon. Even if it's not perfect, it's it provides a starting point.

And if you don't have a tool, then you can't do anything.

Yeah, the bar is the improvement, right? So the bar is like, where are you at now? Can we move the needle? Can we move beyond sequence-based matching, alignment matching? Absolutely. I think there's tons. And I think the interest is only growing. I think we're hitting a lot of chatter at the... Right now, it does feel like

There's a lot of talk. And one of the reasons why we felt like, let's build tools and like put it out and give access to people. Because there's been a lot of talk about AI companies saying like, we should do buy-off defense. But then like, okay, what does that mean?

Like, what are you going to do about it? And so that was our approach.

So I can just steel man this for a minute though. Can you go to the other diagram where you have the, yeah. And if you click on them, then they show other... Similar compounds or similar genomes. So arguably just steelmanning the opposing viewpoint. If you are on the frontier, which it seems like you are,

and you certainly strive to be, you're moving the frontier of the attack and the defense at the same time. So like right now that what you're doing clearly helps, but that maybe if you're on the frontier, then that doesn't really matter in the long term. So how do you think about that?

I mean, I guess you just have to nerf what people are doing or something.

Yeah. The mindset of what was hoping to get folks to Start thinking about it as less of a, oh, let's make a biodefense tool and like call it day. It's basically an arms race, right? Similar to the cybersecurity community. You're gonna make better technology, especially with something like Fable. That can potentially attack.

And that means you're going to have this back and forth. The design side is going to get more capable. The defensive side needs to try to get ahead, right? And then that just motivates other folks to do past that too, right? On the design side.

I think inherently there is this arms race style dynamic that the way it appears to us is that the defensive side has been far, far lagging. And so what we want to do is bring the defensive side closer to par essentially. So that's the mindset I picture or the framing I think about it.

The cybersecurity analogy is interesting, but I think it differs in some key points. So first of all, I think that with cybersecurity, with a sufficiently strong model, you might actually be able to close all loopholes, which are not sociological. There are certain ones which will always be hard, always be ways of getting around things.

But you could, in principle, catch every single exploit. And I think that might be possible in the future. And then you can patch them. And as long as people say updated, you're secure. We have fixed genomes, right? So you can't patch a human. I mean, so I think that in some sense,

the attack surfaces or the way that you defend against that is much higher or much harder. But then maybe the converse is that it seems much less likely that someone would have the incentive to go on offense to the same degree. And also the barrier to entry, even if you can print out arbitrary DNA.

And the process of going from that to making a successful, you know, virus, especially one which doesn't kill the person designing it, is actually quite large. So I guess maybe I'm curious, like what is the single, from your opinion, what is like the single biggest threat that we actually have?

What would the thing which keeps you asleep or keeps you awake at night? Is there something in particular or is this like you just think this is something we need to build and let's build it?

One, it's hard to get in the mindset of a person wanting to design a battle weapon. So we're not trying to necessarily think of all the potential people or scenarios that bad actors might work on. What I think broadly, what I worry about is... We're lowering the bar for how much expertise is needed and the speed at

which folks can engineer this kind of things. And that means the volume is going to just exponentially increase at some point. And so there's a mix of, yes, there's intentional work. And one of our advisors on a company has, you know, physically seen these facilities and decommissioned them.

And so we've heard a lot of stories about states actually being motivated to create such weapons. That is one concern. And I think during peacetime, it's less scary. During wartime, it's particularly scary. I think the unintentional ones are also things that, in my mind, potentially more likely in the near term,

where folks do try to generate things and control function and inadvertently things that maybe they tried to make a certain thing to understand and to study, but it got out, right? Because these things can be hard to contend. Yeah. Far outweigh the potential harm.

And so that's why we work on it because ultimately we do think it's going to be an engine for discovery and human health improvement. But at the same time, we just felt like the defensive side was sort of losing control. It's this arms race. And so we work on it as well and try to push the frontier.

But I'd say overall, I think as a community of researchers, but also folks in the policy side, I think the community is resilient enough and has the ability to mobilize to get ahead of it. And so I'm very optimistic about it.

We have two questions that we like to ask every guest. So the first one is if you could, by fiat, remove a bottleneck that is important to you, what would that be?

Interesting. Could I get two answers on this one? Sure. The first one is kind of a cop-out because every AI lab says this, like, GPUs. GPUs. Yeah, we've done that a few times. We can use GPUs. The other one, which I think is a little more philosophical, I think in this space, what we're trying to do,

aspire to do, is reinvent how scientists do their work in this space. And I think one hurdle we run into is... Folks who, and you see this in many domains, folks who are, the more expertise you have in something, the more pessimistic you become about that space. And I think you especially see this in bio,

where you know a disease area or modality And then someone introduced something else new and you're like, oh, but what about this and this and that? And they're very pessimistic and probably rightfully so. But also, I think what I've noticed at the company,

what we strive to do and the folks that we try to bring in are domain experts that do know that field, but also are still dreamers, meaning they still do have that imagination and desire to change how things are done. I think that barrier, we see that a lot in the field.

I think if we embrace that more, we can see a lot more progress and step change that I would love to see.

Brings us to the last question, which is, yeah, is there something that you want the audience to take away, a single message?

Yeah, I think one message is, I think folks have had, especially into the AI research community, Felt like there was a choice they had to make sometimes to either work on the frontier of AI technology. And that was like consumer related apps or enterprise related apps. And like they just had to work on chatbots.

And that's the cutting edge technology. But also doing, you know, I think when people think about the true potential, what AI can do, and I think a lot of it is about improving human health, understanding our biology. But people have felt like they have had to choose.

And like, if I work in that space, I can't work on the frontier of AI. And what I would like people to take away is that you don't have to choose. I think we can work on things you truly care about that you think will push humanity and work on cutting edge technology.

And that's what we're trying to build at Radical Generics.

Yeah. And I mean, clearly, and I encourage people to read the blog posts, the architecture, the mech and turf. There's a lot of innovation that is going into building these models. And I firmly believe that biology is really on the forefront of AI.

Awesome.

Yeah.

Glad you feel that way. Amazing. Thanks for chatting. Yeah.

Thank you for making the long trip. Anytime.

Appreciate the invite. I had a blast. Great. Thank you.