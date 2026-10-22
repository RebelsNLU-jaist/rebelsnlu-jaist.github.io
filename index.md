---
layout: site
title: Home
browser_title: RebelsNLU — Reading Between the Lines for Natural Language Understanding
page_id: index
permalink: /
stylesheet: /assets/css/pages/index.css
hero:
  home: true
  line1: Understanding the Inner Workings of AI
  emphasis: Building Safe and Trustworthy AI
  line2: ""
  subhead:
    - Language Reasoning Laboratory
    - AI Wisdom Research Area
    - Graduate School of Advanced Science and Technology
  tagline: Reading Between the Lines for Natural Language Understanding
---

<section class="about" id="about">
  <div class="container about-grid">
    <img class="about-logo" src="{{ '/imgs/rebels_logo.png' | relative_url }}" alt="RebelsNLU logo">
    <div class="about-text" markdown="1">

<h2 class="title">About</h2>

**RebelsNLU** is an international research lab for Artificial Intelligence (AI) and Natural Language Processing (NLP) at the [Japan Advanced Institute of Science and Technology (JAIST)](https://www.jaist.ac.jp/english/), founded in 2022 and led by [Associate Professor Naoya Inoue](https://naoya-i.info/). Its name is short for **Re**ading **be**tween the **L**ine**s** for **N**atural **L**anguage **U**nderstanding.

Our goal is AI that can read between the lines: infer what a text leaves implicit, in ways we can inspect and trust. We pursue this goal from three directions: understanding how language models work inside, making them safe and trustworthy, and strengthening their reasoning.

  </div>
  </div>
</section>

<section class="research alt" id="research">
  <div class="container">
    <h2 class="title">Research</h2>
    {%- assign projects_url = '/projects.html' | relative_url %}
    {% include theme-cards.html href_prefix=projects_url %}
  </div>
</section>

<section class="news" id="news">
  <div class="container">
    <h2 class="title">Latest News</h2>
{% include home-x-card.html limit=1 %}
  </div>
</section>

<section class="join-band">
  <div class="container">
    <h2>Interested in doing research with us?</h2>
    <p>We welcome students who want to understand and improve how AI reasons.</p>
    <a class="join-btn" href="{{ '/joinus.html' | relative_url }}">How to join →</a>
  </div>
</section>
