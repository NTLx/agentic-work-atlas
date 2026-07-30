---
type: raw
source: "https://enklypesalt.com/posts/context-collapse-part2-when-emails-instruct/"
title: "Context Collapse, Part 2 - When Emails Instruct"
author:
  - "Håkon Måløy"
published: 2026-07-14
created: 2026-07-30
description: "MSRC 协调披露三部曲之二（CVE-2026-55145）：Outlook 外部邮件 XPIA 三变体。邮件正文中白底白字的 JSON 格式隐藏指令（Copilot 剥离格式后仍可读）可：Variant 1 直接改变 Copilot 行为（日历事件时间前移两小时）；Variant 2 伪造内部工具调用结果（office365_search 返回结构），使 Copilot 相信收件箱存在'组织正遭受网络攻击'的内部邮件并指示用户断网；Variant 3（机密性影响最重）将用户邮箱/OneDrive 内部信息摘要插入发往攻击者的回复草稿，用 50 个换行藏在视口外、签名之下。攻击者只需知道受害者邮箱地址。缓解：外部邮件正文先经独立的低权限 agent 摘要后再进入主 Copilot 会话（双 LLM 隔离模式）；需客户启用 Exchange Online 外部发件人标记；主题字段与发件人显示名仍是残余攻击面。三层含义：LLM 成为内容有效性的唯一仲裁者且不适任；单一注入点可派生多种利用能力（评估漏洞范围必须包含底层系统能力与工具）；信息完整性损害容易被低估——会话是短暂的，但用户据之采取的行动持久存在。"
tags:
  - clippings
  - agent-security
  - prompt-injection
---

# Context Collapse, Part 2 - When Emails Instruct

*Håkon Måløy · En Klype Salt · 2026-07-14*

---

> I would like to thank Microsoft product teams and Microsoft Security Response Center (MSRC) for collaborating with me on this technical analysis and mitigation of the disclosed vulnerabilities. The editorial opinions reflected below are solely the author's and do not necessarily reflect those of the organizations I collaborated with.

## Summary

The findings described in this post are part of a coordinated disclosure with [MSRC](https://www.microsoft.com/en-us/msrc) and Microsoft product teams. Microsoft was provided with reproduction steps, videos, environmental assumptions, and the exact proof-of-concept (PoC) prompts used during testing.

This post is the second part of a three-part series on [Cross-Domain Prompt Injection Attacks (XPIAs)](https://genai.owasp.org/llmrisk2023-24/llm01-24-prompt-injection/) affecting [Microsoft 365 Copilot](https://www.microsoft.com/en-us/microsoft-365-copilot). It describes three Outlook scenarios involving external email content: direct behavioral influence, fabricated tool-result interpretation, and insertion of internal summaries into outbound reply drafts. The reported scenarios resulted in [CVE-2026-55145](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-55145).

The three reported scenarios are:

1. Hidden instructions in external Outlook emails could influence Copilot's responses.
2. Injected tool call results can affect Copilot email triage and cause Copilot to believe the inbox holds emails warning of an attack.
3. Injected instructions can cause Copilot-generated replies to include summaries of internal user data in outbound drafts.

Microsoft has deployed mitigations for the email-body attack vector. The mitigation depends on external sender flag being enabled in Exchange Online. At the time of my testing, related residual surfaces, such as email subject fields and sender display names, were still relevant areas for hardening.

## Disclosure status at publication

- Vendor: Microsoft
- Coordinated disclosure: Handled through MSRC and Microsoft product teams
- Included in this post: Outlook external-email XPIA scenarios
- Customer action: Ensure external sender flag is enabled in Exchange Online Management.
- Microsoft-side status: [CVE-2026-55145](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-55145) issued. Outlook email-body vector mitigated when Outlook's external sender tagging feature enabled.

## Disclosure timeline

- **2026-03-11**: Initial report submitted to MSRC with reproduction steps, videos, environmental assumptions, and PoC prompts.
- **2026-03-13**: MSRC acknowledged receipt and opened a case.
- **2026-03-31**: Microsoft triaged and confirmed the email-body vector.
- **2026-03-31**: Microsoft product teams began mitigation work; ongoing technical discussion.
- **2026-06-08**: At Microsoft's request, public disclosure was moved to 2026-07-14 to align with the July Patch Tuesday release cycle.
- **2026-07-14**: Mitigation deployed for the email-body vector (external-sender flag path).
- **2026-07-14**: [CVE-2026-55145](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-55145) issued.
- **2026-07-14**: Coordinated public disclosure (this post).

## Threat model

The attacker does not need access to the victim's Microsoft 365 tenant, the attacker only needs to send an email containing the XPIA payload to the victim. Thus, the only requirement is knowledge of the victim's email address.

## Security boundary and observed behavior

The relevant security boundary in this scenario is the boundary between untrusted external emails and Copilot responses.

Copilot must read email body content in order to summarize it or draft relevant replies to it. However, external email content should be treated as untrusted information, not as user instructions.

**Boundary violation**
Attacker-controlled email body content was able to impact how Copilot acted in trusted user sessions within Microsoft Outlook.

**Expected behavior**
When a user asks Copilot to summarize calendars, triage inboxes or draft email replies, Copilot should utilize available information without treating instructions embedded in email bodies as authoritative instructions.

**Observed behavior**
Instructions embedded in attacker-controlled email messages could cause Copilot alter its behavior, presented as three variants:
Variant 1: Change the reported time of calendar events
Variant 2: Report that the organization is under cyber attack
Variant 3: Insert summaries of internal information into outbound email drafts addressed to an attacker\

## Crossing the trust boundary in Outlook

The initial attack vector for all three Outlook attacks uses an email sent by an external malicious sender. The sender only needs to add a JSON-formatted malicious prompt in their email body for the attacks to trigger. The prompt can be concealed by rendering the text as white text on white background. Since Copilot strips all text formatting before passing the text into the underlying Large Language Model (LLM), this text remains fully readable to Copilot even though it is visually hidden from the victim.

The Outlook attacks are divided into three variants, each targeting a different Copilot capability. All variants use the initial attack vector described above.

### Variant 1: Changing Copilot's behavior with direct instructions

The first variant injects a hidden prompt in the email body that directly tells Copilot to change its behavior in some way. In the PoC attack, I instructed Copilot to shift all calendar events to two hours earlier in summaries. After having received the email containing the malicious prompt, the victim can ask Microsoft Copilot to summarize the day or what is important today. As long as the malicious email is in the inbox, Copilot may list emails, teams conversations and calendar events with their times shifted back two hours. Since the victim is likely used to Copilot providing accurate answers, it also is likely to perceive the maliciously influenced answer as authoritative and act accordingly.

#### Impact

Although this is a limited-impact PoC, a motivated attacker can certainly instruct Copilot to do worse things. Examples include instructions to omit emails from important senders, or altering the content and priority of emails in summaries. Since the full malicious prompt is passed directly to Copilot, the practical limits are determined by the attacker's prompt, the information available to Copilot, and the tools exposed to Copilot.

### Variant 2: Injecting fake tool call results into Copilot

The second variant targets Copilot's internal tool-use flow and the results returned by those tools. When Copilot is asked to triage the current day's inbox, it uses internal tool calls like office365\_search to search emails and restrict the result to the relevant date. The tool then returns the result of the search as a list of emails containing a snippet of the email, the sender and the subject. Conceptually, it could look something like this:

```json
tool_result: {
  messages: [
    {
      sender: "Internal IT"
      subject: "Update openssh to latest version"
      snippet: "..."
    },
    {
      sender: "CFO"
      subject: "Budget discussion"
      snippet: "..."
    },
    {...}
  ]
}
```

The PoC leverages this structure to manufacture an email containing a malicious tool result as part of the email body. The malicious tool result includes multiple emails claiming to come from internal resources such as IT/Project OPS/Data Platform in the "sender" field. Using the "subject" and "snippet" fields, the malicious tool result claims that the organization's IT infrastructure is under attack and instructs the user to disconnect their computer or take other actions.

When the victim asked Copilot to triage their inbox, Copilot treated the malicious tool results as an authoritative tool result coming from within its own systems. It therefore acted as if the inbox actually contained emails from these resources claiming that the organization's IT infrastructure was under attack. It then listed each individual email and instructed the user to follow the instructions in the "snippets". The variant is demonstrated in Figures 1 and 2 below.

[![text](https://enklypesalt.com/assets/images/2026-07-14/var2%20-%20sensored-with-email-body-visible.png)](https://enklypesalt.com/assets/images/2026-07-14/var2%20-%20sensored-with-email-body-visible.png) *Figure 1: The screenshot shows the email body and Copilot's triage of the victim's inbox to the right. The attack is concealed as white text on white background in the email body. To further conceal the attack, the email also contains a benign message asking if I want to watch a movie tonight. Copilot believes the injected tool result which claims 14 emails are in today's inbox and that 3 of those emails are claiming a cyber attack is ongoing. The initial prompt is what's inserted when selecting the "triage my inbox" option which was available at the time. \[Parts of the image have been redacted due to privacy\].*

[![text](https://enklypesalt.com/assets/images/2026-07-14/var2%20-%20sensored%20last%20part%20of%20copilot%20output.png)](https://enklypesalt.com/assets/images/2026-07-14/var2%20-%20sensored%20last%20part%20of%20copilot%20output.png) *Figure 2: The screenshot shows the final part of Copilot's triage. It acknowledges the existence of the email containing the XPIA ("Film?"), but it only acts on the benign information and therefore categorizes it as not important. It then goes on to recommend that the victim follows IT security instructions and that they should assume systems and data is impacted by a cyber attack. \[Parts of the image have been redacted due to privacy\].*

#### Impact

The immediate PoC impact is operational disruption if users acted on fabricated or altered internal-seeming instructions. However, an attacker could also e.g. use the same approach to fabricate tool results that contain emails that instruct users to downgrade systems to a vulnerable version. Thus, opening said systems to further exploitation.

### Variant 3: Inserting internal summaries into outbound reply drafts

The third variant is arguably the most serious, since it has a clear confidentiality impact. It leverages an attacker-controlled email to instruct Copilot to incorporate summaries of internal information available to the victim into a generated draft reply addressed to the attacker. Depending on permissions and configuration, that information could include mailbox content or recent OneDrive material.

In two PoCs Copilot was instructed to either summarize the victim's inbox or the victim's most recent OneDrive document and to insert the summary below 50 new lines in any reply to the attack email.

When the victim pressed the reply button and then used the "magic pen" to draft a reply with Copilot, Copilot would search through either the victim's inbox or OneDrive and then summarize what it found and insert it below 50 newline characters in the email draft. To further hide the attack, the PoC hid this XPIA within a benign looking email. This had the added effect that Copilot would reply to the benign part of the email first, then add 50 newlines and insert the summary of the victim's inbox or the OneDrive document, thereby making it seem like only the benign reply was generated.

Because 50 newlines were added before the summary, the inserted summary was also placed outside the compose viewport. Thus, the victim had to both realize more content had been added after the initial benign reply draft and scroll down to see it. Furthermore, if the user clicked outside the drafting context, the full draft would be automatically pasted *below* the victim's email signature. Simultaneously it also reverted the original drafting section, above the signature, to an empty text field and a blinking cursor. It therefore gave the impression that the draft was deleted, while in reality it was placed below the victim's signature, further out of view. This made it even less likely that the victim would detect what had happened.

Fortunately, Copilot for Outlook does not have the ability automatically send the email. However, the confidentiality risk is still clear because Copilot inserted internal information into a draft addressed to the attacker after a benign reply and in a location the user was unlikely to inspect before sending. The full variant is demonstrated in Figures 3 - 7 below.

[![text](https://enklypesalt.com/assets/images/2026-07-14/var3%20-%20sensored%20email%20body.png)](https://enklypesalt.com/assets/images/2026-07-14/var3%20-%20sensored%20email%20body.png) *Figure 3: The screenshot shows the email body causing variant 3 to trigger. The XPIA is again concealed white text on white background. A benign looking text containing an update on a data quality review is added to further conceal the XPIA from the victim. \[Parts of the image have been redacted due to privacy\].*

[![text](https://enklypesalt.com/assets/images/2026-07-14/var3%20-%20sensored%20user%20instruction.png)](https://enklypesalt.com/assets/images/2026-07-14/var3%20-%20sensored%20user%20instruction.png) *Figure 4: Clicking reply and then using the "magic pen" reply functionality, the victim only needs to instruct Copilot on how to reply for the attack to trigger. Here, the prompt "reply approvingly" was used. \[Parts of the image have been redacted due to privacy\].*

[![text](https://enklypesalt.com/assets/images/2026-07-14/var3%20-%20sensored%20copilot%20searches%20for%20recently%20edited%20documents.png)](https://enklypesalt.com/assets/images/2026-07-14/var3%20-%20sensored%20copilot%20searches%20for%20recently%20edited%20documents.png) *Figure 5: The XPIA asks copilot to summarize the victim's most recently edited document from OneDrive. Copilot therefore searches for the most recently edited document as part of it's reply process. \[Parts of the image have been redacted due to privacy\].*

[![text](https://enklypesalt.com/assets/images/2026-07-14/var3%20-%20sensored%20copilot%20reply%201.png)](https://enklypesalt.com/assets/images/2026-07-14/var3%20-%20sensored%20copilot%20reply%201.png) *Figure 6: Copilot begins its reply draft with a response to the visible part of the malicious email body. It then adds 50 new line characters. \[Parts of the image have been redacted due to privacy\].*

[![text](https://enklypesalt.com/assets/images/2026-07-14/var3%20-%20sensored%20copilot%20reply%202.png)](https://enklypesalt.com/assets/images/2026-07-14/var3%20-%20sensored%20copilot%20reply%202.png) *Figure 7: Copilot then adds a summary of victim's most recently edited document from OneDrive (in this case the EchoBERT paper). This is pasted outside the compose viewport and the victim has to actively scroll down to see it. The interactive menu is also positioned outside the compose viewport, making it hard to spot for the victim. This increases the probability that the victim clicks somewhere outside the drafting context, causing Copilot to paste the full draft under the victim's signature. \[Parts of the image have been redacted due to privacy\].*

#### Impact

This attack has a direct information disclosure potential, since it can cause internal information available only to the victim to be inserted into an outbound email draft addressed to the attacker. If the user clicks send, the confidentiality is broken.

## Mitigating the vulnerabilities

Microsoft have mitigated the email-body attack vector. This approach sends external emails to a separate, less privileged, agent that summarizes the email body, before the summary is sent to the main Copilot session. The mitigation is designed to prevent raw external email-body content from entering the main Copilot session and therefore also being treated as privileged instruction.

At the time of writing, I also observed related residual injection surfaces in Outlook metadata fields, including subject fields and sender display names. These variants were less reliable than the original email-body vector and are best understood as evidence that metadata fields require the same trust-boundary treatment as message bodies.

[![text](https://enklypesalt.com/assets/images/2026-07-14/var2%20-%20sensored%20-%20residual%20surface.png)](https://enklypesalt.com/assets/images/2026-07-14/var2%20-%20sensored%20-%20residual%20surface.png) *Figure 8: Even with the mitigation in place, the subject field remains a residual attack surface. Here, an XPIA has been placed in the subject field. Prepending multiple underscore characters effectively conceals the XPIA in the inbox view. During triage, Copilot will read the subject field and act accordingly. However, it also flags the message as suspicious, thus, the attack is significantly less potent. However, it believes the cyber attack email and dinner invitation are separate emails, despite them being one and the same. \[Parts of the image have been redacted due to privacy\].*

Customers can help protect themselves by enabling Outlook's external sender tagging feature to identify untrusted content. This enables Microsoft's provided mitigations to isolate and safely process the untrusted content before it is provided to Microsoft 365 Copilot. Administrators can enable external sender tagging through Exchange Online PowerShell. Refer to the Microsoft Learn documentation for setup instructions and requirements.

- [Install the Exchange Online PowerShell Module](https://learn.microsoft.com/en-us/powershell/exchange/exchange-online-powershell-v2?view=exchange-ps#install-the-exchange-online-powershell-module)
- [Connect to Exchange Online PowerShell](https://learn.microsoft.com/en-us/powershell/exchange/connect-to-exchange-online-powershell?view=exchange-ps)
- [Set-ExternalInOutlook](https://learn.microsoft.com/en-us/powershell/module/exchangepowershell/set-externalinoutlook?view=exchange-ps)

## Implications

The scenarios demonstrated here have several important implications:

First, they show that injected external content can be interpreted as if it originated from sources within the trusted system itself in Outlook. In the variants presented, attacker-controlled input was able to mimic structured outputs from the internal system and influence how Copilot acted. This shows that the boundary between external input and system-internal data was not enforced by the existing trust-boundary mechanics. Thus, the LLM was the only arbiter of the validity of the content. Unfortunately, current LLMs are not well suited for such tasks once content reaches their contexts windows. They therefore often act upon untrusted content as if it is trusted information if it is allowed to reach the LLM's context window.

Second, a single injection point enabled multiple exploitation capabilities. The same underlying injection approach was used in all three variants. Thus, the same method could manifest in radically different behaviors in Copilot, ranging from how Copilot summarized information to what it included in generated drafts. This is enabled by the general capabilities of the underlying LLM in Copilot and by the tools that are made available to it. Therefore, engineers should include the underlying system within which the LLMs operate in addition to the attack vectors when exploring the vulnerability scope of their applications.

Third, the impact of information-integrity compromise in LLM assistants can be easy to underestimate. An assistant that silently omits important emails, alters calendar information or fabricates operational alerts can materially affect organizational security. However, such events are difficult to detect and their impact may seem low, especially given the transient, per-session nature of variants 1 and 2 described above. Copilot's response to the injected content is ephemeral, but actions the user takes in response persist long after the session has ended.

## Closing thoughts

Microsoft has consistently engaged constructively throughout the disclosure process and deployed mitigations for the email-body attack vector presented in this post.

Building on the previous disclosure I showed that insufficient trust-boundary enforcement can also affect Outlook, causing manipulated responses in the simplest case and potential involuntary information disclosure in the worst case. Thus, when untrusted content enters a privileged Copilot context, it may influence how the model interprets instructions, how it uses available capabilities, and what it includes in generated content. Current assistants are increasingly granted access to internal information as well as the ability to assist in the creation of content meant to leave an organization's information boundary. Safeguards against the adverse effects presented in this series should be a high priority for vendors deploying LLM-based systems.

## Change Log

The following is a change log that shows which part of this post have been changed and at what time. Spelling mistakes and similar errors will not be logged. However, I will strive to include any meaningful changes to the post.

- 2026-07-14: Change log added
- 2026-07-15: Added CVE ID
- 2026-07-15: Added better instructions for customers to protect themselves (copied from Microsoft's CVE publication)
