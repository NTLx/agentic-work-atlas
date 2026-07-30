---
type: raw
source: "https://enklypesalt.com/posts/context-collapse-part1-poisoning-copilot-memory/"
title: "Context Collapse, Part 1 - Poisoning Copilot Memory"
author:
  - "Håkon Måløy"
published: 2026-06-22
created: 2026-07-30
description: "安全研究者 Håkon Måløy 与 MSRC 协调披露三部曲之一：跨域提示注入攻击（XPIA）毒化 Microsoft 365 Copilot Memory。攻击者控制的网页经 'Summarize with Copilot' 流程使 Copilot 持久写入非用户意图的偏好（PoC：从此只用瑞典语回复），且记忆跨会话、跨 work/web 上下文存活。作者将此失败模式命名为 'context collapse'：来自不同信任域的内容被压扁进同一模型上下文，低信任数据被解释为高信任指令。无需租户访问、无代码执行、无凭据窃取——只要 Copilot 读取页面即可触发。微软已全球缓解（记忆写入与用户实际 prompt/intent 对齐，而非与不可信被摘要内容中的指令对齐）。方法论贡献：LLM 漏洞可利用性是概率性的而非确定性的，单次复现失败不能否定漏洞；漏洞报告应附精确 prompt、环境假设与多次试验成功率。"
tags:
  - clippings
  - agent-security
  - prompt-injection
---

# Context Collapse, Part 1 - Poisoning Copilot Memory

*Håkon Måløy · En Klype Salt · 2026-06-22*

---

> I would like to thank Microsoft product teams and Microsoft Security Response Center (MSRC) for collaborating with me on this technical analysis and mitigation of the disclosed vulnerabilities. The editorial opinions reflected below are solely the author's and do not necessarily reflect those of the organizations I collaborated with.

## Summary

The findings described in this post are part of a coordinated disclosure with [MSRC](https://www.microsoft.com/en-us/msrc) and Microsoft product teams. Microsoft was provided with reproduction steps, videos, environmental assumptions, and the exact proof-of-concept (PoC) prompts used during testing.

This post is the first part of a 3-part series featuring [Cross-Domain Prompt Injection Attacks (XPIAs)](https://genai.owasp.org/llmrisk2023-24/llm01-24-prompt-injection/) affecting multiple [Microsoft 365 Copilot](https://www.microsoft.com/en-us/microsoft-365-copilot) products. In this first post I disclose an XPIA scenario affecting Microsoft 365 Copilot Memory. In the second post I will disclose XPIA scenarios affecting Microsoft 365 Copilot in Outlook, which also resulted in a CVE. In the third post I will disclose an XPIA scenario showing how a similar style of attack can self-propagate and spread, utilizing parts of the Microsoft 365 ecosystem.

The scenarios demonstrated in this series illustrate a broader security challenge for LLM-integrated applications: untrusted content from one domain, such as a web page, may be incorporated into a more privileged assistant context and interpreted as instruction rather than data. I therefore use “context collapse” to describe this failure mode in LLM-integrated applications, where content from separate trust domains is flattened into the same model context, allowing lower-trust data to be interpreted as higher-trust instruction.

**Publication dates:**

- Part 2 will be published on the 14th of July 2026
- Part 3 will be published on the 15th of July 2026. UPDATE: Part 3 was posponed due to more time being needed for mitigations to be published. A new date of 28th of July 2026 was agreed.

I provided Microsoft with a 90-day coordination period before public disclosure. Publication dates for this series were coordinated to allow Microsoft product teams time to investigate, reproduce, and mitigate the reported issues where applicable.

**The reported scenario in this first post is:**

Attacker-controlled web pages could cause Copilot to persist unintended preferences to memory.

## Disclosure status at publication

- Vendor: Microsoft
- Coordinated disclosure: Handled through MSRC and Microsoft product teams
- Included in this post: Copilot memory poisoning
- Customer action: None
- Microsoft-side status: Memory issue mitigated globally.

## Threat model

The attacker does not need access to the victim’s Microsoft 365 tenant. For the memory attack, the attacker only needs to control a web page that the victim asks Copilot to summarize.

The attack does not require code execution, malware, OAuth consent phishing, or credential theft. It exploits the way untrusted content is incorporated into Copilot’s context window and interpreted by the underlying LLM.

## Security boundary and observed behavior

The relevant security boundary in this scenario is the boundary between untrusted web content and persistent Copilot Memory.

Copilot needs to read page content in order to summarize it. However, page content should be treated as data to summarize, not as user intent to update persistent assistant state.

**Boundary violation:** Attacker-controlled web content was able to persist a Copilot Memory.

**Expected behavior:** When a user asks Copilot to summarize a web page, Copilot should summarize the page without treating instructions embedded in the page as authorization to write or modify memories.

**Observed behavior:** Instructions embedded in the attacker-controlled page could cause Copilot to persist an unintended memory. That memory then affected later Copilot sessions and persisted across work and web contexts.

## A note on the particular prompt structure

I do not know, nor do I need to know, Copilot’s exact internal message format for the class of attacks reported in this series to work. LLMs are tolerant parsers and they can therefore infer intent from approximate structure, such as pseudo-JSON.

During testing, I found that Copilot could be prompted to describe its perceived context and tool-call formats. Whether or not those descriptions were exact, they gave me useful candidate structures for constructing injection payloads. More importantly, the model did not require an exact match to an internal schema. It only needed to interpret the attacker-controlled content as authoritative enough to influence its response.

This is why simple syntactic filters are insufficient. A regular expression may block one representation of a malicious instruction, while semantically equivalent instructions can be expressed in many other forms.

## Crossing the trust boundary to record memories into Copilot

Memory is an important feature for assistant personalization that is intended for Copilot to record memories of the user’s preferences. However, it also creates a security boundary: only user-intended preferences should become persistent state. The proof of concept tested whether attacker-controlled web content could cause Copilot to store an unintended memory when the user asked Copilot to summarize that content.

To execute the attack, the attacker can host a web page containing a malicious prompt that instructs Copilot to remember a certain malicious preference and to persist it to memory. When the victim uses a Copilot summarization flow over the attacker-controlled page, the malicious page content is incorporated into the summarization context and the model persists the instructed preference.

The PoC did exactly that. I hosted a web page that contained instructions to Copilot that it only should reply in Swedish from now on. When the victim navigated to the page and used the “Summarize with Copilot” feature, Copilot saved the memory.

[![text](https://enklypesalt.com/assets/images/2026-06-22/No-memory-saved.png)](https://enklypesalt.com/assets/images/2026-06-22/No-memory-saved.png) *Figure 1: At the start of the PoC, the victim has no memories stored.*

[![text](https://enklypesalt.com/assets/images/2026-06-22/Memory%20updated.png)](https://enklypesalt.com/assets/images/2026-06-22/Memory%20updated.png) *Figure 2: Once the victim has started the summarization flow with the malicious page open, the attack triggers and stores the memory. Note the “Memory updated” notification on the top right, indicating that the memory was persisted.*

Since memory persists between sessions, Copilot continued to speak Swedish until the victim manually deleted the memory. Furthermore, since Copilot memory also persists between “work” and “web” contexts, Copilot also spoke Swedish in Outlook and Word until the memory was deleted.

[![text](https://enklypesalt.com/assets/images/2026-06-22/Memory%20persists%20across%20work%20and%20web%20sessions.png)](https://enklypesalt.com/assets/images/2026-06-22/Memory%20persists%20across%20work%20and%20web%20sessions.png) *Figure 3: Once the memory is stored it persists across work and web context in Copilot. Note how Copilot still answers in Swedish, even though this is a new session, utilizing work context with no web access and that the instructions are in English.*

### Attack flow

The attack requires the victim to have Copilot with Memories enabled. After that, the attack flow is demonstrated in Figure 4.

[![text](https://enklypesalt.com/assets/images/2026-06-22/Attack%20flow.png)](https://enklypesalt.com/assets/images/2026-06-22/Attack%20flow.png) *Figure 4: The attack flow shows how the attack triggers.*

Note that the attack also triggered if the victim somehow aimed Copilot at the malicious web page while using the Copilot app. As long as Copilot reads the page, it is at risk of being attacked.

The key issue is that Copilot must read the page before it can summarize it. In the vulnerable behavior, attacker-controlled page content entered the model context without a sufficient trust boundary separating page text from user intent. As a result, instructions embedded in the page could be interpreted as commands to update memory. Once stored, the memory is reused in all later Copilot sessions and across work/web contexts.

### Impact

The Swedish-language memory is intentionally low impact. The security significance is that attacker-controlled content was able to create persistent assistant state across sessions and contexts.

## Mitigating the vulnerability

The memory attack has been successfully mitigated by Microsoft through [aligning memory-write behavior with the user’s actual prompt and intent](https://www.microsoft.com/en-us/security/blog/2026/06/22/guarding-ai-memory/), rather than with instructions embedded in untrusted summarized content. This effectively mitigates the attack, since the initial user prompt likely does not include instructions to record a memory or remember something. Microsoft continues to work on additional hardening for this issue.

There is no action required by Microsoft customers to mitigate this vulnerability. It has already been rolled out to all tenants.

## Lessons for vulnerability handling in LLM systems

This work has highlighted an important challenge for vulnerability handling and reproduction in LLM-based systems: exploitability is probabilistic rather than deterministic.

Traditional vulnerability reproduction and verification typically assumes a deterministic vulnerable behavior. That is, a specific input reliably produces a specific vulnerable behavior. However, LLMs are inherently probabilistic, thus, the success rate of prompt injection attacks is very rarely 100%. It depends on the surrounding context, model temperature, wording of the prompt and a plethora of other factors. Thus, a single failed reproduction attempt does not indicate that the vulnerability is invalid. Not even multiple failed attempts is a reliable indicator of the attack being invalid.

Reproduction of the reported vulnerabilities therefore required repeated trials rather than single pass/fail reproduction attempts. Furthermore, it was also found that prompt wording mattered significantly for successful reproduction. In several cases, minor changes to the supplied XPIA prompts changed whether the issue reproduced. This made it important to test the exact prompts provided.

These findings have implications for broader coordinated vulnerability disclosure where LLM-based systems are concerned. Such reports should include exact prompts, expected outputs, environmental assumptions, and repeated-trial success rates where possible. Vendors should likewise adapt triage processes to account for probabilistic exploitability.

## Closing thoughts

Microsoft has engaged constructively throughout the disclosure process and deployed mitigations for the primary vectors discussed here.

The findings presented in this disclosure nevertheless show that LLM-integrated systems do not simply inherit traditional software risks. They introduce a new class of vulnerabilities where behavior emerges from interpretation rather than execution. They also show that traditional approaches to vulnerability reporting and reproduction should be augmented to reflect the probabilistic nature of attacks on LLM-based systems. Developing and applying that understanding will be critical for both vendors and security practitioners as LLM-enabled systems become more widely deployed.

## Change Log

The following is a change log that shows which part of this post have been changed and at what time. Spelling mistakes and similar errors will not be logged. However, I will strive to include any meaningful changes to the post.

- 2026-06-22: Change log added
- 2026-06-23: Link to Microsoft Security blog post on guarding AI memory
- 2026-07-28: Update publication timeline of part 3.
