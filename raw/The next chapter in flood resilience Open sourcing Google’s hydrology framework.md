---
type: raw
title: "The next chapter in flood resilience: Open sourcing Google’s hydrology framework"
source: "https://research.google/blog/the-next-chapter-in-flood-resilience-open-sourcing-googles-hydrology-framework/"
author:
  - "Grey Nearing"
  - "Deborah Cohen"
published: 2026-06-03
created: 2026-06-04
description: "Google Research open-sources its hydrology modeling framework so forecasting agencies can combine advanced AI with local data, knowledge, and operational workflows."
tags:
  - clippings
  - AI-deployment
  - AI-for-science
  - open-source
---

We have open-sourced our hydrology model to enable National Meteorological and Hydrological Services to integrate advanced AI-based flood forecasting into their own workflows.

Floods are one of the most devastating natural hazards worldwide, often arriving with little warning and leaving long-term damage. Over several years, Google Research has built state-of-the-art AI models for more accurate [flood forecasting](https://research.google/blog/using-ai-to-expand-global-access-to-reliable-flood-forecasts/), ensuring this technology reaches frontline responders to give them time to act. To help further protect vulnerable communities, we are now open-sourcing our [hydrology modeling framework](https://github.com/google-research/flood-forecasting) on GitHub for others to use and build upon.

This open source modeling framework allows researchers and forecasters to train AI flood forecasting models with the same architecture and similar training data to what is used to power riverine flood forecasts on Google’s Flood Hub. It is developed to allow hydrological scientists to build on what we have done at Google Research by adding and testing new models, data, and approaches. It also allows operational forecasters — people whose job entails providing actionable flood warnings for specific areas — to incorporate local data and knowledge into state-of-the-art AI-based flood forecasting.

We believe that a [scientific breakthrough](https://research.google/blog/catalyzing-scientific-impact-through-global-partnerships-and-open-resources/) reaches its full potential when it empowers others to replicate and expand upon findings, ensuring that innovation is a catalyst for worldwide progress. That's why we developed this framework internally and tested it with partners like the [Czech Hydrometeorological Institute](https://en.chmi.cz/) (CHMI). Releasing our model architecture and training pipeline represents a fundamental shift in global flood preparedness, allowing National Meteorological and Hydrological Services (NMHSs), other meteorological agencies, and authorities to retain full control of their data while empowering local experts to refine models using specialized datasets.

## How it works

Our hydrology model is a Python package that uses the open source [PyTorch machine learning modeling package](https://pytorch.org/) to implement the river forecast model that drives the Google Flood Hub. These models take input data in the form of geographical features related to climate, soils, topography, and land cover, along with meteorological forecasts related to rainfall, temperature, and other weather conditions to predict the daily flow rate of rivers around the world.

The hydrology modeling package includes [model architectures](https://hess.copernicus.org/articles/29/6221/2025/) based on [Long Short Term Memory](https://hess.copernicus.org/articles/23/5089/2019/) (LSTM) Networks, and a training pipeline that allows these models to be trained using historical river data from the [open source Caravan dataset](https://www.nature.com/articles/s41597-023-01975-w). Researchers and flood forecasting agencies can add their own data to this open source data repository to train or [fine tune](https://arxiv.org/abs/2504.12559) models to their local watersheds.

To get started with implementation, check out [this interactive tutorial notebook in Python](https://github.com/google-research/flood-forecasting/blob/main/tutorial/GoogleHydrology%20Tutorial.ipynb) and the associated [video tutorial on Youtube](https://www.youtube.com/watch?v=431Kr3mxidU) on navigating [the model code](https://github.com/google-research/flood-forecasting).

## Model improvements

This code repository includes two distinct versions of our hydrological model: the original version tested in our [benchmarking study published in 2024](https://www.nature.com/articles/s41586-024-07145-1), and an upgraded model that currently powers real-time global flood forecasting on [Flood Hub](http://g.co/floodhub). The new model builds upon the foundational success of our initial research by transitioning to a new model architecture. This framework allows us to process diverse, multi-source meteorological inputs into a unified flood prediction system, illustrated in the figure below. [Our recent benchmarking study](https://egusphere.copernicus.org/preprints/2026/egusphere-2026-2283/) shows that this new model extends the reliable predictive horizon by six days in gauged basins and by one day in ungauged basins relative to the previous version.

![CHMI_open_sourcing_2](https://storage.googleapis.com/gweb-research2023-media/images/CHMI_open_sourcing_2.width-1250.png)

*The v2 model uses an ME-LSTM architecture to process disparate weather data into a unified flood prediction. Each weather product is embedded by a different network; these outputs are fed into an LSTM network, which generates a probability distribution for streamflow. Timesteps are noted by forecast & lead time. The system integrates global weather products:* [*Graphcast*](https://www.science.org/doi/10.1126/science.adi2336) *(GC);* [*European Centre for Medium-Range Weather Forecasts*](https://www.ecmwf.int/en/forecasts/datasets/set-i) *(IFS);* [*NASA’s satellite rainfall estimates*](https://link.springer.com/chapter/10.1007/978-3-030-24568-9_19) *(IMERG);* [*CPC =* *NOAA’s* *CPC gauge-based daily precipitation*](https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2007JD009132)*.*

## From theory to operational reality

In the [Global Status of Multi-Hazard Early Warning Systems 2025 report](https://wmo.int/resources/publication-series/global-status-of-multi-hazard-early-warning-systems/global-status-of-multi-hazard-early-warning-systems-2025), the [World Meteorological Organization](https://wmo.int/) recognizes that both local data and Indigenous and Local Knowledge (ILK) are critical components of effective disaster warnings, and notes that *“\[t\]he systematic integration of ILK into risk knowledge production is still the exception rather than the norm.”* Our open source flood forecasting workflow addresses the report’s finding by allowing regional forecasters to take direct, hands-on control over AI-powered forecasting models. These frameworks are relatively easy and inexpensive to train, providing accuracy without the complexity of traditional hydrological forecasting models and allowing users to incorporate their own specialized data for training and prediction.

Readily adoptable open-source tools are critical for bridging the gap between technological innovation and the real-world effectiveness of flood hazard systems, particularly for accelerating capacity development around early warning systems.

The operational potential of this release is best illustrated by our partnership with CHMI. Their collaboration was key to validating that our AI-based model provides forecasts comparable in quality to traditional, locally calibrated conceptual models. CHMI also developed an adapter that integrates the hydrology open source framework into the [Delft-FEWS](https://www.deltares.nl/en/software-and-data/products/delft-fews-platform) platform, a popular operational flood forecasting tool used by national and local flood forecasting agencies, NGOs, and private companies to drive predictive models. Delft-FEWS is operated and maintained by the [Deltares](https://www.deltares.nl/en) research institute. This allows CHMI and other hydrological services worldwide to use the model in their standard workflows. This integration serves as a blueprint for how global agencies can include machine learning in their water management workflows.

Beyond larger institutions like CHMI, the open source model release offers a scalable, accessible tool, democratizing access to advanced forecasting and opening the door for resource-constrained regions and local teams to leverage high caliber insights without the need for costly traditional forecasting infrastructure.

The international meteorological community has recognized the value of this open-science approach. Dr. Hwirin Kim, Chief of Hydrological Modelling and Forecasting Section at the [World Meteorological Organization](https://wmo.int/), notes: “I welcome the expansion of open-source hydrological modeling tools that are critical to supporting how societies manage water resources and respond to environmental challenges. We at WMO are keen to support open-source, interoperable, Member-driven models and tools that can help save lives and advance the global mission to ensure communities everywhere are forewarned about hazards to protect their lives and livelihoods.”

## A unified framework for climate action

The model architecture, comprehensive documentation, and training materials are now [live](https://github.com/google-research/flood-forecasting) on GitHub under an Apache 2.0 license, making the framework fully accessible to both researchers and operational forecasting professionals.

By putting our hydrology model into the hands of the global hydrology community, we can build a more flood-resilient world. More details about Google’s broader flood forecasting initiatives and resources are available on the [Google Research site](https://sites.research.google/gr/floodforecasting/). We invite the worldwide hydrology community to build upon these open tools.

## Acknowledgements

*Many people were involved in the development of this effort. We would especially like to thank Jakub Krejci and Jan Daňhelka from CHMI for their partnership and feedback as well as the following individuals across Google Research and the Social Impact Partnerships Team: Amit Markel, Avinatan Hassidim, Deborah Cohen, Emily Reinstein, Gila Loike, Grey Nearing, Nina Bekele, Omri Shefi, Reuven Sayag, Rony Amira, Shmulik Fronman, Stephanie Rees, and Yossi Matias.*
