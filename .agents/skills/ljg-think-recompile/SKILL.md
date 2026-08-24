---
name: ljg-think-recompile
description: Headless mechanism and boundary analysis for Claim Recompile runs. Use only when existing evidence is adequate but a claim's mechanism or applicability boundary remains unclear.
allowed-tools: Read, Grep, Glob
---

# Claim Recompile Think

Clarify one claim's mechanism or boundary without turning abstraction into evidence.

## Input contract

Require four fields in the invocation:

```text
Claim: one falsifiable proposition
Gap: Boundary | Mechanism
Evidence: concise source-grounded observations already collected by the caller
Question: the single boundary or mechanism distinction to resolve
```

If facts are too weak to support mechanism analysis, return `evidence insufficient` and name the missing observation.

## Method

Trace at most five explanatory layers. Each layer must contain:

- a more specific mechanism or boundary;
- the assumption introduced at that layer;
- an observable result that could distinguish it from an alternative.

Stop when the next layer would be a metaphor, an unfalsifiable story, a synonym, or an abstraction with no distinguishing observation. Prefer the shallowest explanation that accounts for the evidence.

The output is reasoning. It cannot increase evidence strength by itself.

## Output contract

Return only:

```text
Mechanism or boundary:
- ...

Necessary assumptions:
- ...

Live alternative:
- ...

Discriminating observation:
- ...

Stopping reason:
- ...

Reasoning delta:
- refined | no_delta
- one-sentence explanation
```

Return the result to the caller. Create no files, transcripts, notifications, menus, or follow-up questions.
