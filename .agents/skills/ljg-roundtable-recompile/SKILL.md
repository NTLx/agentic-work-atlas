---
name: ljg-roundtable-recompile
description: Headless claim falsification roundtable for Claim Recompile runs. Use only when one claim has competing explanations that source lookup alone cannot distinguish.
allowed-tools: Read, Grep, Glob
---

# Claim Recompile Roundtable

Expose competing explanations for one claim without creating evidence or artifacts.

## Input contract

Require four fields in the invocation:

```text
Claim: one falsifiable proposition
Gap: Counterexample
Evidence: concise source-grounded observations already collected by the caller
Dispute: the explanations or assumptions that remain live
```

If the input lacks a concrete claim or evidence, return `insufficient input` and the missing field. Do not broaden the topic.

## Method

Use 3–5 analytical roles chosen for the claim, such as falsifier, mechanism analyst, domain operator, measurement critic, or governance critic. Roles are lenses, not simulated real people. Do not invent quotations, biographies, MBTI types, or source facts.

Run at most three compact rounds:

1. State the strongest competing explanations.
2. Expose the assumptions on which they diverge.
3. Identify a counterexample or observation that would distinguish them.

Stop sooner when another round would only restate a position. Treat all output as reasoning; agreement among roles is not independent evidence.

## Output contract

Return only:

```text
Competing explanations:
- ...

Hidden assumptions:
- ...

Counterexamples:
- ...

Discriminating observations:
- ...

Reasoning delta:
- refined | no_delta
- one-sentence explanation
```

Return the result to the caller. Create no files, transcripts, notifications, menus, or follow-up questions.
