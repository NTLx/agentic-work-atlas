---
type: raw
title: "A Functional Taxonomy of World Models"
source: "https://x.com/drfeifei/status/2062247238143996275"
article_source: "https://x.com/i/article/2062244283940544512"
author:
  - "Fei-Fei Li"
published: 2026-06-03
created: 2026-06-06
description: "Fei-Fei Li 在 X 上发布的长文，把 world model 拆成 renderer、simulator、planner 三类，并用 POMDP 视角重新定义 state、observation 和 action，强调 simulator 是最被低估但最关键的一层。"
tags:
  - "clippings"
  - "world-model"
  - "spatial-intelligence"
  - "simulation"
  - "planning"
---

# A Functional Taxonomy of World Models

## 剪藏价值判断

**高价值，建议后续编译。**

理由:

- 这是一个很适合沉淀成稳定概念页的定义型材料：它不是泛泛宣传 world model，而是试图给这个被过度滥用的词做功能分类。
- 与本库已有 [[World-Model]] 节点直接相关，可以作为后续更新该 entity 的高质量一手材料。
- 文章把 renderer、simulator、planner 放回 POMDP 回路里解释，这比许多“world model 就是 3D/video/robotics”式说法更清楚、更可迁移。
- 作者是 Fei-Fei Li，且文本来自她在 X 上发布的长文，对空间智能和 world model 方向有持续代表性。

## 关键事实摘录

- 文中把今天被统称为 world model 的系统拆成三类：renderer、simulator、planner。
- 底层框架来自 POMDP：agent 做 action，action 影响 state，agent 只能看到 observation，world model 的不同形态本质上是这个回路的不同投影。
- renderer 输出面向人眼的 observation，重点是视觉逼真；simulator 输出可计算、可交互、受几何和物理约束的 state；planner 输出 action。
- 作者强调 simulator 是三者中最少被公众注意、但最关键的一层，因为它同时支撑 render 和 plan。

## 为什么适合本知识库

这篇文章的重要性在于，它把一个行业热词重新压回到结构上。对本库来说，这很关键，因为很多“world model”讨论其实混杂了视频生成、机器人决策、物理仿真和空间表征几条不同路线。如果不先切开，后面所有比较都会失焦。

后续编译时适合重点提取：

- renderer / simulator / planner 的功能边界
- 为什么 simulator 是空间智能中的关键中间层
- unified world model 的目标与当前数据、物理、3D 资产短缺之间的张力

## 原文摘录

> "The world is everything that is the case." — Ludwig Wittgenstein, Tractatus Logico-Philosophicus, 1921

A Functional Taxonomy of World Models

Language models have given machines an extraordinary command of concepts, vocabulary, and reasoning, but the physical world, virtual or real, runs on a different substrate. Where language models learn the statistical structure of text, world models learn the statistical structure of space and time: how light falls on a surface, how a garden looks from an angle no camera has captured, how objects respond to force and follow the laws of physics.

That makes "world model" one of the most important and most overloaded terms in AI today. Computer vision, robotics, reinforcement learning, and generative AI each claim to be building world models, and each means something quite different. A video model that produces gorgeous but physically impossible flames, a language model improvising a playable game, and a physics engine that faithfully simulates combustion all go by the same name.

Cutting through that confusion starts with a diagram older than any of the technology in question. Reinforcement learning textbooks, including the canonical Sutton and Barto, have used a version of the same picture for decades to describe how an agent interacts with a world. The formal name for this picture is the partially observable Markov decision process, or POMDP, and the original definition of the term "world model" belongs to that tradition.

An agent, which can be a person, a robot, or a software system, takes actions. Those actions affect the state of the world. The agent never sees the state directly. What reaches the agent are observations: the photons that fall on a retina, the readings from a sensor, and the pixels in a video frame. New observations inform new actions, and the loop continues.

This loop — agent to action to state to observation and back — is the structure that gave the modern term "world model" its technical meaning. The different things now being called world models are in fact different projections of this same loop. Each one outputs a different piece of it.

The first kind of world model is a renderer. A renderer outputs observations in the form of pixels meant for human eyes, and the quality that matters most is visual fidelity.

The second kind is a simulator. A simulator outputs state: a geometrically, physically or dynamically faithful representation of the world that humans and computer programs can both compute on and interact with. Where the renderer's contract is purely visual, the simulator's contract is structural, demanding geometry that holds up under inspection, physics that respects Newton's laws, and dynamics that behave the way the world needs to behave given the laws of physics.

The third kind is a planner. A planner outputs actions. Given an observation and a goal, a planner answers the question of what the agent should do next. Where a renderer takes actions as input and produces observations, a planner takes observations as input and produces actions, closing the perception-action loop.

These three categories describe most of what is actually shipping today, and the distinction between them is useful in practice. The categories are not, however, fundamentally separate. The same underlying knowledge of how the world works — geometry, physics, dynamics — sits beneath all of them.

Of the three categories, the simulator gets the least public attention, and is the most consequential of the three.

Simulation is the bridge between the two. If language is an abstraction of the world and pixels are a projection of it, then geometry, physics, and dynamics are the world itself. A simulator must work at that level: the structural backbone from which both visual appearance (for renderers) and action consequences (for planners) can be derived.

The hardest open problems in the field live there too. Three-dimensional data with explicit geometry, material properties, and physical annotations is orders of magnitude scarcer than the internet video that renderers train on. The sim-to-real gap persists. Generative simulators introduce a new risk on top of that: AI-generated geometry can look correct while containing self-intersections or wrong scale that produce nonsensical physics.

The logical endpoint is a unified world model: one foundation model that can render photorealistic views, produce physically accurate structure, and plan action sequences, switching between output modalities depending on what the downstream consumer needs.

The direction, however, is clear. The same bet the field has been making since the late 1980s — that a sufficiently rich model of the world is all that any agent needs to see worlds, build them, and act in them — is the bet now driving an entire generation of research.

Language gave machines a way to talk about that world. World models are how machines will finally come to understand, imagine, reason and interact with it.
