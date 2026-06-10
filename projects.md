---
layout: page
title: Projects
---

# Research / Projects

## Overview

<img src="https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/70048022-8e6e-4270-8cf7-7e2c9f0f6bd7/Untitled/public" alt="Research overview" style="width:100%;height:auto;"/>

<!-- <img src="https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/3f4f6bcc-178d-4c88-8146-0ab0c2b9cb65/Untitled/public" alt="Research overview details" style="width:100%;height:auto;"/> -->

## Individual Projects

* [Mechanistic Interpretability](#mechanistic-interpretability)
* [Machine Unlearning](#machine-unlearning)
* [Towards Improving Reasoning Capability of LLMs](#towards-improving-reasoning-capability-of-llms)
* [Reasoning and Probing for Vision-Language Models](#reasoning-and-probing-for-vision-language-models)

## Mechanistic Interpretability

<img src="https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/a4d70879-7740-411a-b1a4-cec3c45a46de/Fig1/public" alt="Mechanistic interpretability" style="width:100%;height:auto;"/>

**Mechanistic Interpretability.** We are dedicated to simplifying the complex inference of language models into a sequence of simpler processes. For instance, in the work shown in the figure, we break down the In-context Learning process of language models into three straightforward steps with careful measurements, and use such a decompose to explain many observed phenomena.

This approach falls under mechanistic interpretability, offering a transparent, step-by-step understanding of how neural networks perform tasks. While this type of decomposition may not always yield precise models, as the saying goes, "all models are wrong, but some are useful." Rather than pursuing traditional machine learning theory's theoretical elegance and precision, we prioritize empirical practicality to guide better practice.

**Our Efforts:** [Cho et al.](https://arxiv.org/pdf/2410.04468) **ICLR 2025** (shown in the figure), [Cho et al.](https://arxiv.org/pdf/2406.01468) **COLING 2025**

**Application: Improve the In-context Learning Performance.** If we input a text-label paired prompt and leave the final label blank (as shown in the figure), the language model will predict the missing label using its causal language modeling operation. This allows us to prompt the language model to learn from the few-shot text-label pairs and generate a response to the question, which is called [In-context Learning](https://ai.stanford.edu/blog/understanding-incontext/).

As previously mentioned, we also focus on analyzing and improving the in-context learning capabilities of language models. For example, in the work shown in the figure, we examine the decision boundaries in in-context learning and refine them to boost both accuracy and stability. We believe our work can significantly enhance the practical utility of language models in downstream tasks.

<div class="columns">
  <div class="column">
    <img src="https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/f850646b-d097-4b7d-b75e-6c4590de0f4a/Fig2/public" alt="In-context learning figure" style="width:100%;height:auto;"/>
  </div>
  <div class="column">
    <img src="https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/a5cd2bda-d33b-4671-a5b9-a2f79d0df096/Fig3_Method/public" alt="In-context learning method" style="width:100%;height:auto;"/>
  </div>
</div>

**Our Efforts:** [Cho et al.](https://arxiv.org/pdf/2406.16535) **NAACL 2025** (shown in the figure, [Japanese](https://ipsj.ixsq.nii.ac.jp/ej/index.php?active_action=repository_view_main_item_detail&page_id=13&block_id=8&item_id=235105&item_no=1)), [Cho et al. 2024](https://arxiv.org/pdf/2402.05515)

## Machine Unlearning

**Introduction.** As a human, forgetting some basic knowledge seems "impossible" once learned. For example, for basic facts such as "the sun rises every day," it is much harder to forget them than the rare, unusual ones. Let's imagine that Alice claims that she forgot something. It might be one of two cases: (1) She knows about it, but intentionally decided to act as if she does not, or (2) She knows about it, but not well enough to be able to claim that she has learn it.

We ask whether Machine Unlearning (MU) algorithms can help ML models truly unlearn (or erase) knowledge, or do they, much like humans, merely conceal it, deciding that the model should "act" as if it does not know? And who's to say unlearning should be in any different forms?

**Topics.** We are currently working on the following topics:

(1) Fundamental mechanisms, new definitions, and evaluations of MU

(2) Efficient and robust MU algorithms

**Our efforts:** [Dang et al.](https://arxiv.org/pdf/2408.06223) **AAAI 2025**, [Dang et al.](https://arxiv.org/pdf/2501.19202) **arXiv Preprint**

## Towards Improving Reasoning Capability of LLMs

**Benchmarking Multi-hop QA in Japanese.** JEMHopQA is a multi-hop QA dataset in Japanese for the development of explainable QA systems, consisting of question-answer pairs with two types of questions, and derivation triples of supporting evidence. It is created based on Japanese Wikipedia using both crowd-sourced human annotation as well as prompting a large language model (LLM). Evaluating several state-of-the-art LLMs on proposed dataset show that the dataset is sufficiently challenging.

<div class="columns">
  <div class="column">
    <img src="https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/da7c869c-3307-4e65-b442-a55b3ed08e74/4/public" alt="JEMHopQA figure 1" style="width:100%;height:auto;"/>
  </div>
  <div class="column">
    <img src="https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/ffc48556-5c2c-49ab-b3bf-69ad2301e2b4/5/public" alt="JEMHopQA figure 2" style="width:100%;height:auto;"/>
  </div>
</div>

<img src="https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/bee54709-218b-444e-b799-358a61639e7d/6/public" alt="JEMHopQA figure 3" style="width:100%;height:auto;"/>

**Our Efforts:** [Ai Ishii et al.](https://aclanthology.org/2024.lrec-main.831/) **LREC-COLING 2024**

**Datasets for Logical Fallacy Detection.** This paper introduces four sets of templates for common informal logical fallacies. Using proposed templates, an annotation study is conducted on top of 400 fallacious arguments taken from LOGIC dataset and achieves a high agreement score and reasonable coverage. Extensive experiments are conducted for detecting the structure of fallacies and discover that state-of-the-art language models struggle with detecting fallacy templates.

<div class="columns">
  <div class="column">
    <img src="https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/8fff47c2-795c-48fb-a8e6-d48dad4c7330/7/public" alt="Logical fallacy detection figure 1" style="width:100%;height:auto;"/>
  </div>
  <div class="column">
    <img src="https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/f3c422bd-d804-4f18-b95f-757bc08d0d25/8/public" alt="Logical fallacy detection figure 2" style="width:100%;height:auto;"/>
  </div>
</div>

<img src="https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/497f0616-1397-4b88-8c00-604ba703b3c1/9/public" alt="Logical fallacy detection figure 3" style="width:100%;height:auto;"/>

**Our Efforts:** [Irfan Robbani et al.](https://aclanthology.org/2024.emnlp-main.1142/) **EMNLP 2024**

## Reasoning and Probing for Vision-Language Models

**Benchmark for Inductive Visual Reasoning.** We introduce Find-the-Common (FTC) benchmark, which consists of 353 instances, each of which provides (i) four 3D scenes consisting of 2-6 objects and (ii) four multiple choices, including a decoy choice that is partially true in scenes. Models are required to identify an answer that explains the common attributes across visual scenes. We propose Image-Based Reasoning, Text-Based Reasoning, and Image-Text-Based Reasoning for evaluating various VL models. Extensive experiments show that even state-of-the-art models like GPT-4V struggle on FTC, showing FTC as a new challenge for visual reasoning.

<div class="columns">
  <div class="column">
    <img src="https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/d3f63bbe-e403-4d02-ba39-fdab383e2275/10/public" alt="Find-the-Common figure 1" style="width:100%;height:auto;"/>
  </div>
  <div class="column">
    <img src="https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/be3b00fb-1b16-434c-a381-5899a59b3322/11/public" alt="Find-the-Common figure 2" style="width:100%;height:auto;"/>
  </div>
</div>

<img src="https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/198a5061-c7a9-4b81-8708-e61f86dceeaa/12/public" alt="Find-the-Common figure 3" style="width:100%;height:auto;"/>

**Our Efforts:** [Yuting Shi et al.](https://aclanthology.org/2024.lrec-main.642/) **LREC-COLING 2024**

## Grants

* **井之上 直也 (PI)**. 解釈可能な分散表現に基づく言語モデリング. JSPS Grant-in-Aid for Scientific Research (KAKENHI 基盤C). 2026/04-2029/03, 3,500,000JPY.
* **井之上直也 (PI)**. 人々が頼りたくなる自己批判的思考力を備えた言語処理機構. JST 2023年度 創発的研究支援事業, 2024/10-2028/03, 20,000,000JPY.
* **井之上直也 (PI)**. 自己認識的に推論ができる信頼性の高いAIの研究. 中島国際交流財団 日本人独立研究者始動助成金, 2024/04-2027/03, 5,000,000JPY.
* 日高昇平, 鳥居拓馬, **井之上直也**, 大関洋平. 自然言語の計算原理の解明による最小言語モデルの開発. JSPS Grant-in-Aid for Scientific Research (KAKENHI 基盤A). 2026/04-2030/03, 31,800,000JPY.
* 水本正晴, 和泉悠, Nguyen Minh Le, **井之上直也**, 窪田悠介. Cross-Linguistic Semantic Alignment for Universal Philosophical Concepts. JSPS Grant-in-Aid for Scientific Research (KAKENHI 基盤A). 2025/04-2029/03, 44,000,000JPY.
* 乾健太郎, **井之上直也**, 中川智皓, HEINZERLING BENJAMIN, 吉川 将司. 深い論述理解の計算モデリングと論述学習支援への応用. JSPS Grant-in-Aid for Scientific Research (KAKENHI 基盤A). 22H00524. 2022/04-2027/03, 41,470,000JPY.

Past grants can be found [here](https://naoya-i.github.io/grant.html).

## Main Collaborators

* Tohoku NLP Lab
* RIKEN AIP: Natural Language Understanding Team, Language Information Access Technology Team

[Previous Projects](https://rebelsnlu.super.site/projects/previous-pojects)
