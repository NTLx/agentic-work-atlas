---
type: raw
source: "https://anil.recoil.org/notes/rumour-is-the-exploit"
author:
  - "Anil Madhavapeddy"
published: "2026-08-22"
created: "2026-08-29"
tags:
  - clippings
  - cybersecurity
  - agentic-engineering
  - open-source
  - vulnerability-management
---

# Just a rumour of a bug is enough to find a security exploit these days

I released a security fix for OCaml's [cohttp 6.3.0](https://discuss.ocaml.org/t/cohttp-6-3-0-released-osec-2026-16/18467) today, fixing a [path traversal issue](https://osv.dev/vulnerability/OSEC-2026-16). The patch itself was straightforward and in normal times, the security procedure would have been to fix it privately, inform affected users, and then issue a public advisory. This time around though, I noticed probes in my live webserver logs with the exact bug pattern just minutes after opening the [PR to fix the issue](https://github.com/mirage/ocaml-cohttp/pull/1145).

What's worse, I found I could use my own agents to find the exploit *just by knowing roughly what it was about* and so could have been exploiting it well before the public patch was available! Given that just the *rumour* of a security issue seems enough to give attackers enough info to find new exploits, we're going to need to change the way we deal with security responses in open source.

## The rumour of a bug is all new agentic exploit systems need

This particular report arrived privately on a Slack channel via Jane Street last week, and was itself found via Claude Fable. That compresses all timelines considerably...

### The timeline of a modern security report

Before examining the patch in detail, I pointed my own Claude at the affected code to see what else was lurking (asking it to investigate path normalisation issues). Fable frustratingly refused outright due to its security block since I [don't have access to Glasswing](https://www.anthropic.com/glasswing), but [DeepSeek V4 Pro](https://anil.recoil.org/notes/language-integrated-llms) obliged me and independently turned up several related issues. My agent also trivially created an exploit to probe a local live server in under a minute.

After some back and forth with the bug reporter about possible fixes, I quietly opened [cohttp#1145](https://github.com/mirage/ocaml-cohttp/pull/1145) publicly to [get more eyes](https://anil.recoil.org/notes/2026w33) on it. This normally takes a few days and a release within a week or two is reasonable. Within about ten minutes (!) this website was fielding probes for percent-encoded traversal sequences, indicating that automated watchers are keeping an eye on public repositories.

If it took me just a minute to create my own exploit locally, then [ten minutes actually seems quite long](https://www.icir.org/vern/papers/cdc-usenix-sec02/) for an automated attack window to start! A determined attacker who is monitoring package repositories could easily be exploiting them within seconds.

### Security embargoes are no longer effective

Conventional security process involves [embargoing](https://www.redhat.com/en/blog/Understanding-security-embargoes-at-Red-Hat) the bug, and assumes that secrecy of the details protects users. However, all an agent needs today is a broad direction to search in, and it can do its own research. [Fang et al.](https://arxiv.org/abs/2404.08144) found that when given a CVE description, their GPT-4 agent [exploited 87%](https://surrealyz.github.io/classes/llmsec-fall24/slides/14-agents-exploit-vulnerabilities.pdf) of a 15-vulnerability benchmark, and without the description, just 7%.

Two years on, the [mean time to exploit](https://cloud.google.com/blog/topics/threat-intelligence/m-trends-2026) is -7 days. In other words, exploitation now precedes the patch! That same metric looks to be around 63 days in 2018-19, and crossed zero in 2024. A quick search finds lots of other similar cases these days... marimo's [CVE-2026-39987](https://www.sysdig.com/blog/marimo-oss-python-notebook-rce-from-disclosure-to-exploitation-in-under-10-hours) went from advisory to first exploitation attempt in 9 hours, even with no public proof-of-concept in existence. Langflow's [CVE-2026-33017](https://www.sysdig.com/blog/cve-2026-33017-how-attackers-compromised-langflow-ai-pipelines-in-20-hours) took 20 hours. We seem to have crossed the rubicon for automated exploit generation...![The state of LLM exploitation in 2026 (source: Vulncheck)](https://anil.recoil.org/images/vulncheck-2026.3840.webp)

The state of LLM exploitation in 2026 (source: Vulncheck)

## Are the bugonomics against OSS maintainers now?

It looks to me like our security processes need to invert somewhat, since just one person searching for the issue class (this could be a mailing list question, an odd commit in an orphan branch, or a context leak) is sufficient to alert someone else's agent and let them get exploit code. This is wild.

A May 2026 paper coined the term " [bugonomics](https://arxiv.org/abs/2605.24632) " and argues that the bottleneck has moved to "defender remediation throughput". LLMs are merrily generating exploits, but our ability to defend against them isn't necessarily improving as maintainer validation, triage and release rates stay flat. This unfortunately matches the view from my OSS maintainer's chair:

> The question is not whether frontier models, open-weight models, or program analysis "win". The question is how to orchestrate them so that scarce validation, prioritization, and release capacity goes toward durable fixes rather than mechanical search and report drafting. A central defender opportunity is technical debt remediation: semantics-grounded, tool-verified, model-assisted workflows that help maintainers find, validate, prioritize, and fix security-relevant defects before they become tomorrow’s exploited vulnerabilities. \-- [Demystifying the Mythos or Disrupting Bugonomics?](https://arxiv.org/pdf/2605.24632), Pesoli et al, 2026

And why are maintainer capabilities staying flat? Well, not having access to frontier agents like Mythos is an obvious one, but also that the engineering of a security patch that doesn't cause any regressions is just fundamentally more work.

## So what the hell can we do about this?

We clearly need to adapt fairly quickly. I don't think the current manual triage process should disappear, but I have seen an unsustainable surge of activity since Fable came out. We are only just beginning to get a handle on how much of the incoming firehose is machine-generated, but it's obviously a lot.

The big engineering shops (like Google) have been building [microupdates directly into their software](https://blog.google/security/chrome-stronger-with-every-update/) to ensure that fixes directly reach users as a priority over (e.g.) being fixed in the Chrome code repository. We don't really have that kind of luxury in Docker or OCaml, as we don't control the endpoints our software is used in. Aside from [Docker Desktop](https://anil.recoil.org/papers/2026-decade-docker), downstream distributions quite rightly repackage OSS on their own timescales and terms.

For smaller projects like OCaml, just gaining access to the frontier models is a struggle. The Western models have security guards in place which mean that we can't use the commercially available ones. [Project Glasswing](https://www.anthropic.com/glasswing) has [expanded](https://www.helpnetsecurity.com/2026/06/03/anthropic-project-glasswing-expansion/) to 150 organisations across 15 countries including critical infrastructure operators, cloud and financial providers, the Linux Foundation, but 'mom and pop' maintainers still don't have access. I was ambivalent [back in April](https://anil.recoil.org/notes/internet-immune-system) whether this is harmful, but it's pretty obvious today that it's turning out pretty terribly.

### Super sekrit private patch development

The first remediation is to develop the fixes somewhere really private out of the reach of AI. GitHub's [temporary private forks](https://docs.github.com/en/code-security/security-advisories/working-with-repository-security-advisories/collaborating-in-a-temporary-private-fork-to-resolve-a-repository-security-vulnerability) nominally do this, but it doesn't work hugely well for us.

First, GitHub restricts it *"to keep information about vulnerabilities secure, integrations, including CI, cannot access temporary private forks"* which immediately disconnects the maintainer from the lifeblood of our CI results. Secondly, only a single PR can merge into the fork, which doesn't work well for issues that often span a few repositories. Reviewers also have to be enrolled one at a time by an admin, and in open-source land reviewers are kind of drive-by depending on who is available (especially in August!).

More broadly though, this plugs the wrong leak. The patch staying secret isn't nearly as important as ensuring the description about the issue reaches exactly the right people with no leakage to attackers.

We don't have robust *discussion* infrastructure available within OSS as it's spread through various end-to-end encrypted ones (we use Matrix) but also shared infrastructure like Discord or Slack which are extremely leaky. We do need some sort of [web-of-trust](https://blog.tangled.org/vouching/) to distinguish the good guys from the bad in a particular project context.

### No embargoes, just ship continuously

Another thing we could do is to rapidly fix issues in public, ship continuously, and improve the release path via better automation.

Bigger projects like Chrome show this is possible via [weekly security updates](https://blog.google/security/chrome-stronger-with-every-update/), two releases per week (!), and [dynamic patching](https://arstechnica.com/ai/2026/07/chrome-may-get-faster-updates-with-no-restart-required/) that swaps background processes for updated binaries without a restart. This isn't entirely new technology; I looked into integrating [live ksplice Linux patching with Xen](https://en.wikipedia.org/wiki/Ksplice) 15+ years ago. The Linux kernel also ships fixes as soon as possible, deferring at most [seven days](https://docs.kernel.org/process/security-bugs.html) and exceptionally fourteen.

However, software packaging is our primary obstacle. Chrome has a relatively easy job of shipping one binary artefact, but OSS is often a bunch of libraries that are then [embedded](https://anil.recoil.org/papers/2025-docker-icfp) in a variety of downstream products. So to do this, we'll need:

- much better [cross-ecosystem package management](https://anil.recoil.org/papers/2026-package-calculus) to discover where disparate libraries are eventually embedded. [Ryan Gibb](https://ryan.freumh.org/) will talk about this at ICFP next week!
- better scanning tools to help with triage; Andrew Nesbitt has been doing just this with [Scrutineer](https://nesbitt.io/2026/06/25/scrutineer.html) over the past few months. [Thomas Gazagnaire](https://github.com/samoht) and I have been discussing trying this out for our OCaml code, subject to getting access to a reasonable frontier model without security blocks.
- more robust quality control infra without any false positives that works across the spectrum of supported platforms. While it's relatively easy to run CI on Linux, it's a different story on [OpenBSD](https://www.tunbury.org/2026/06/30/openbsd-copy-corruption/), [FreeBSD](https://www.tunbury.org/2026/06/24/leaking-jails/), [macOS](https://www.tunbury.org/2025/10/06/overlayfs-macFuse/), and some architectures like [RISC-V](https://www.tunbury.org/2026/06/03/emulated-riscv-workers/)

### Proactive protection at the protocol layer

I've also been having more radical thoughts about how we could slam in protections dynamically to protect endpoints using our libraries. If we just accept that upstream patch fixes will always trail an exploit, then we *must* put something faster to get ahead.

For example, this cohttp bug fixed today has a simple mitigation: just normalise percent-encoded path separators in the request URL. This rule was implementable the minute the report arrived, and also deployable while the full fix went through review, testing and packaging. Virtual patching is routine on cloud infrastructure these days; Cloudflare deployed [managed rules](https://blog.cloudflare.com/how-cloudflare-security-responded-to-log4j2-vulnerability) to plug Log4shell back in 2021.

But open source lacks a distribution mechanism for such rules outside of a commercial CDN. That's what the [antibotty network](https://anil.recoil.org/notes/internet-immune-system) idea from our [internet ecology paper](https://anil.recoil.org/papers/2025-internet-ecology) is trying to plug via [more software diversity](https://anil.recoil.org/notes/rewilding-the-web-report) around the global Internet. How can we have local, fast-propagating defences that hear about a vulnerability and act on their immediate infrastructure within seconds?![](https://anil.recoil.org/images/aarhus-1.1920.webp)

## Some research followups

I think we'll need some combination of all three options in the short-term. A lightweight web-of-trust for OSS contributors (like the venerable [Advogato used to be](https://anil.recoil.org/notes/opam-ai-disclosure-update)), as well as more focus on OSS packaging and continuous rollout and triage mechanisms that don't overwhelm our precious human contributors.

I've also posted a couple of new MPhil research ideas for anyone incoming to Cambridge next month and is looking for a project.

- " [An antibotty defensive testbed to protect network services](https://anil.recoil.org/ideas/antibotty-testbed) " puts a MirageOS gateway in front of a home network, and investigates whether a set of mitigation rules can be made trustworthy enough to deploy automatically. There's a fun capture-the-flag game we could play by giving the same rumour to an attacking agent and a defending one and seeing which one gets there first.
- " [Compiling Lean specifications into OxCaml enforcement automata](https://anil.recoil.org/ideas/lean-dijkstra-automata) " defines what a library is permitted to do across filesystem, parser and network layers using [Dijkstra monads](https://anil.recoil.org/papers/2024-hope-bastion). This would compiles that Lean specification into an OxCaml automaton that enforces it at runtime. It's a modern spin on the [statecall automata](https://anil.recoil.org/papers/2009-icfem-spl) I built during my PhD.

And if anyone from Project Glasswing is listening, team OCaml could use access now:-)

*(The cohttp fix was not a solo effort. Sapphire Livingstone found and reported the issue, guided the fix and co-developed the remediation; [Michael Dales](https://mynameismwd.org/), [Török Edwin](https://github.com/edwintorok) and [Patrick Ferris](https://patrick.sirref.org/) reviewed the patch; [Hannes Mehnert](https://github.com/hannesm) coordinated the advisory; and [Thomas Gazagnaire](https://github.com/samoht) has been thinking through the wider triage problem. Thank you all! The bugonomics may be against us, but we will crest this hump.)*
