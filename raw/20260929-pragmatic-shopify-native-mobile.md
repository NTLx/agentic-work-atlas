---
type: raw
source: "https://newsletter.pragmaticengineer.com/p/shopify-native-mobile"
title: "Why has Shopify dropped React Native?"
author:
  - "Gergely Orosz"
published: "2026-09-29"
created: "2026-10-12"
tags:
  - clippings
  - agentic-engineering
---

# Why has Shopify dropped React Native?

> Capture limitation: this file records a concise paraphrase of the publicly accessible portion, not its full verbatim text. It does not include or reconstruct any paid-only material.

## Publicly accessible portion (paraphrase)

The article introduces Shopify's move toward native mobile development, attributing the changed tradeoff to coding agents becoming better at implementing, translating, testing, and reviewing Swift and Kotlin code. Its outline covers Shopify's earlier move to React Native, its reported benefits and drawbacks, the newer native direction, prior industry reversals, Notion's long migration, Kotlin Multiplatform, and possible next steps.

The first section describes why Shopify adopted React Native: mobile was important, and native Android development could be slow and difficult. Clubhouse is presented as an example of the cost of a delayed Android release. Shopify's Arrive (later Shop) rewrite is cited as an early positive React Native experience that enabled an Android version and shared code. The article also recounts Shopify's 2020 rationale: share implementation, improve talent portability, and ship more value. A later company account described six apps moved to React Native, faster screen loads, high crash-free rates, and productivity and feature-parity benefits, alongside debugging, native-code, and third-party-library drawbacks.

The second section begins by revisiting Shopify's positive five-year assessment of React Native and recaps its stated gains, then notes the engineering team's appreciation for performance, hot reload, and TypeScript alongside debugging and library limitations.

The third section reports Shopify's changed decision. In comments attributed to Head of Mobile Mustafa Ali, the article says coding models reduced the cost of building for two platforms while native development retained closer access to platform capabilities and tooling. It discusses React Native's rendering abstractions and New Architecture, reported modest startup gains from migration to that architecture, and the potential performance control available in native apps. It also relays the expectation that one engineer may work across iOS and Android with agent help, that agents can port and compare separate implementations, and that Shopify uses a shared headless test suite for Swift and Kotlin business logic. The section closes with Shopify's stated plan to migrate its apps using AI, with Shop already native after a 12-week rewrite and other apps to follow, subject to quality requirements.

## Public boundary

The last publicly accessible substantive text is the closing paragraph of section 3: “Best of luck to the team with this migration! I’m looking forward to hearing about what they learn with this move.” The page then exposes the heading “4. Haven’t we seen this back-and-forth before?” and immediately displays “This post is for paid subscribers.” The canonical capture stops at that paid-subscriber wall. No section 4 body or later paid content is included or inferred.
