---
layout: page
title: RebelsNLU / 言語推論研究室
subtitle: Reading between the Lines for<br /> Natural Language Understanding
hero_image: /imgs/hero-sep.jpg
hero_height: is-medium
---

<!-- <p align="center">
  <img src="/imgs/rebels_logo_sq.png" style="width:200px"/>
</p> -->

<!-- <span style="font-size:1.0em;color:red">Dear potential students:</span> see [here](https://rebelsnlu-jaist.github.io/joinus.html) for more details. -->


**RebelsNLU** is a research lab for Artificial Intelligence (AI) and Natural Language Processing (NLP), run by [Associate Professor Naoya Inoue](https://naoya-i.github.io) at [Japan Advanced Institute of Science and Technology (JAIST)](https://www.jaist.ac.jp/english/).

We study how to create machines that can understand our human language.
Particularly, we are interested in reasoning skills for AI.
Our ultimate goal is to equip machines with an ability to *infer something*--making implicit things explicit and reading between the lines.

## ✨ Latest Headlines ✨

{% for post in site.posts limit:10 %}
- **{{ post.date | date: "%m/%-d/%Y" }}**: {{ post.content | remove: '<p>' | remove: '</p>' }}
{% endfor %}

 <!-- <a href="{{ post.url | prepend: site.baseurl }}">Read more...</a> -->

