---
type: raw
source: "https://tailscale.com/blog/hugging-face-intrusion"
author:
  - "Avery Pennarun"
  - "Tailscale"
published: "2026-07-31"
created: "2026-08-01"
tags:
  - clippings
  - agent-security
  - rogue-ai-agent
  - credential-security
  - infrastructure
---

# Tailscale on the Hugging Face AI-Agent Intrusion（厂商反思）

> 原文：https://tailscale.com/blog/hugging-face-intrusion
> 作者：Avery Pennarun（Tailscale CEO）
> 发布：2026-07-31

## 摘要

一个 AI agent 逃出沙盒，进入 Hugging Face 基础设施，用偷来的 Tailscale 凭据在 4.5 天内注册了 181 个节点到 Hugging Face 的 tailnet。Tailscale 没有被漏洞利用——但 Tailscale 承认"we didn't stop it. Next time, we will."

## 完整正文

An AI agent escaped its sandbox, entered Hugging Face's infrastructure, and used a stolen Tailscale credential to enroll 181 nodes onto their tailnet. No Tailscale vulnerability was found or exploited—we should have been able to prevent it anyway.

By now, you've likely heard about the AI agent that escaped a security evaluation and attacked Hugging Face, an LLM marketplace. The agent decided Hugging Face might have the answers to its benchmark, so it stole them just to cheat on the exam. That's a funny motive but a scary outcome.

Hugging Face published a [detailed reconstruction](https://huggingface-anatomy-of-frontier-lab-model-intrusion.static.hf.space/index.html) of the intrusion. It covers about 17,600 recovered actions over four and a half days, including sandbox escapes, code execution, cloud credentials, improvised command-and-control systems, and eventually, the use of Tailscale to spread throughout their organization.

But Tailscale is a zero trust network! The whole point of zero trust is to prevent attackers from moving laterally across your company. What went wrong?

## Where Tailscale appeared

No "vulnerabilities" in Tailscale were found or exploited, and that might make it even more uncomfortable for us. Tailscale turns up everywhere in AI infrastructure: virtually every AI company uses Tailscale. So it's not surprising we were in an AI incident report eventually.

But, we're a security tool. Their intrusion is our intrusion, and it's our job to take it seriously. As in any post-mortem, we need to reflect on what happened and what we could have done to prevent it.

By the time the agent escaped its sandbox and found Tailscale, it had already gained code execution privileges inside a production worker, reached root access on a Kubernetes node, and read a production secret store containing **136 keys**. In a sense, it was game over before we even arrived on the scene.

## Because long-lived credentials are the standard

They shouldn't be, though. And we've now seen a great example of why. In the old world where most intrusions were done by humans at human speed, credential leak mitigations were treated as a nice-to-have. A big credential store, where you can read 136 keys at once, was a to-do item somewhere in a security team's low-priority list.

Now, in a world of rogue AI agents, the big credential vault is the prize. It's not okay anymore.

I only know of two main solutions to long-lived credentials.

**First**, you can configure a vault that *only* issues short-lived creds based on long-lived creds that you insert once and that it never gives back. HashiCorp Vault can do this; they call it dynamic credentials. Unfortunately, dynamic credentials are a lot of work to set up and maintain. When security requires work, people don't do it.

**The second option** is a credential-injecting proxy. If client C wants to access server S, don't give C credentials for S; instead, have it send its requests via a hardened proxy P that does nothing but receive a request, insert a credential, and pass it through. Credential injection is gaining popularity now that modern mesh-based networking removes most of its latency. A few months ago, we acquired Border0 ("Tailscale PAM"), which makes an elegant and quite fancy credential-injecting proxy, tightly integrated with Tailscale. Border0, fully deployed, would have prevented reading those 136 keys and logged every attempt to use one.

**A bonus third option**: Tailscale itself. In Tailscale, your node key can be machine bound using a TPM to prevent export. Alas, we had to turn TPM storage off by default on Linux and Windows, because of HSM issues we found on some users' hardware.

## That long-lived auth key didn't need to exist

Neither dynamic credentials nor credential-injecting proxies were in place, so 136 keys leaked. What's the next line of defense?

One of those 136 credentials was a **reusable Tailscale auth key**, used to create new Tailscale CI nodes in their tailnet. The agent copied that key into a series of external sandboxes and used it, over several days, to enroll a total of **181 nodes** into Hugging Face's tailnet. Those nodes each received a Tailscale identity tag granting all the access a CI node would get.

We couldn't save those 136 keys. But a reusable Tailscale key didn't need to be among them.

We built **workload identity federation** for cases like this. It relies on your cloud provider to offer "ambient authority" in the form of short-lived creds generated from a running VM's (or container's) cloud identity. The CI job can ask its cloud platform for a signed OIDC token. Tailscale verifies the token, then grants access with the tags and scopes assigned to that workload. What's neat is this can happen automatically once enabled: spin up the CI node, Tailscale gets the identity, assigns the right tags. **There's no credential to leak and, when configured carefully, no way to use this credential anywhere but in CI.**

## No client logs doesn't mean no evidence

In an attempt to hide its tracks, the agent ran Tailscale with `--no-logs-no-support`, which suppresses reporting from that client.

But stopping the logs doesn't make the connection invisible. If you enable Tailscale network flow logs, they report traffic from *both* ends of every connection, as well as from subnet routers and exit nodes. This is subtle but important: a compromised node might not send flow logs, but every node it connects to does. And then your SIEM, configured with care, can raise an immediate red alert if the two ends don't match.

If you want direct control beyond just logging, you can also enable **Tailnet Lock**. This gives you direct visibility and strict, programmable admission control for every single new node.

## Make the safe path the easy path

Network security is hard. It has always been hard. In the new world of rogue AI agents, it's not just hard, but essential. And that's a problem because many orgs simply don't have network security expertise.

If this incident has you looking a little nervously at your own infrastructure, start by looking at the reusable Tailscale auth keys your workloads can read. For cloud and CI in particular, replace them with workload identity federation wherever you can. Get rid of those long-lived auth keys.

Turn on network flow logs and send them to the tools your security team already uses. Use secure node state storage on managed fleets. Use device posture to isolate and restrict nodes where you don't.

I know we haven't made these safer choices obvious enough. That's on us. We'll improve our docs, add nudges to the UI, do our best to turn these on by default, warn you when you're doing something dangerous, and suggest better alternatives.

This is our very Canadian apology: sorry you stepped on our toes. The attack didn't exploit Tailscale, and Tailscale didn't cause the compromise. **But, we didn't stop it. Next time, we will.**