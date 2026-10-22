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
  <div class="container narrow" markdown="1">

<h2 class="title">About</h2>

**RebelsNLU** is an international research lab for Artificial Intelligence (AI) and Natural Language Processing (NLP), run by [Associate Professor Naoya Inoue](https://naoya-i.info/) at [Japan Advanced Institute of Science and Technology (JAIST)](https://www.jaist.ac.jp/english/) (since 2022). RebelsNLU is short for **Re**ading **be**tween the **L**ine**s** for **N**atural **L**anguage **U**nderstanding.

We want machines that understand human language the way people do — by reading between the lines and making implicit things explicit. To get there, we study how language models work inside, how to make them safe and trustworthy, and how to strengthen their reasoning.

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
    <h2>Want to do research with us?</h2>
    <p>We welcome students who want to understand, and improve, how AI reasons.</p>
    <a class="join-btn" href="{{ '/joinus.html' | relative_url }}">How to join →</a>
  </div>
</section>
