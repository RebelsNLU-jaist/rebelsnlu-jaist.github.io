---
layout: site
title: Projects
page_id: projects
permalink: /projects.html
stylesheet: /assets/css/pages/projects.css
hero:
  title: Projects
---

<section id="overview">
  <div class="container">
    {% include theme-cards.html more="Jump to section ↓" %}
  </div>
</section>

{% for theme in site.data.projects %}
<section id="{{ theme.id }}"{% cycle '', ' class="alt"' %}>
  <div class="container prose">
    <h2 class="title">{{ theme.name }}</h2>
    <p class="theme-lead"><span class="theme-q">{{ theme.question }}</span> {{ theme.summary }}</p>
{%- for topic in theme.topics %}
    <article class="topic{% if topic.image %} has-image{% endif %}{% if topic.image_wide %} wide{% endif %}">
      <div class="topic-text">
        <h3>{{ topic.title }}</h3>
        <p>{{ topic.summary }}</p>
        <p class="papers">{% for paper in topic.papers %}<a href="{{ paper.url }}">{{ paper.label }}</a>{% endfor %}</p>
      </div>
{%- if topic.image %}
      <figure class="topic-fig"><img src="{{ topic.image | relative_url }}" alt="{{ topic.image_alt }}" loading="lazy"></figure>
{%- endif %}
    </article>
{%- endfor %}
  </div>
</section>
{% endfor %}

{% include content-section-start.html id="grants" class="alt" container_class="prose" title="Grants" %}

- **井之上 直也 (PI)**. 解釈可能な分散表現に基づく言語モデリング. JSPS Grant-in-Aid for Scientific Research (KAKENHI 基盤C). 2026/04-2029/03, 3,500,000JPY.
- **井之上直也 (PI)**. 人々が頼りたくなる自己批判的思考力を備えた言語処理機構. JST 2023年度 創発的研究支援事業, 2024/10-2028/03, 20,000,000JPY.
- **井之上直也 (PI)**. 自己認識的に推論ができる信頼性の高いAIの研究. 中島国際交流財団 日本人独立研究者始動助成金, 2024/04-2027/03, 5,000,000JPY.
- 日高昇平, 鳥居拓馬, **井之上直也**, 大関洋平. 自然言語の計算原理の解明による最小言語モデルの開発. JSPS Grant-in-Aid for Scientific Research (KAKENHI 基盤A). 2026/04-2030/03, 31,800,000JPY.
- 水本正晴, 和泉悠, Nguyen Minh Le, **井之上直也**, 窪田悠介. Cross-Linguistic Semantic Alignment for Universal Philosophical Concepts. JSPS Grant-in-Aid for Scientific Research (KAKENHI 基盤A). 2025/04-2029/03, 44,000,000JPY.
- 乾健太郎, **井之上直也**, 中川智皓, HEINZERLING BENJAMIN, 吉川 将司. 深い論述理解の計算モデリングと論述学習支援への応用. JSPS Grant-in-Aid for Scientific Research (KAKENHI 基盤A). 22H00524. 2022/04-2027/03, 41,470,000JPY.
{: .list}

Past grants can be found [here](https://naoya-i.info/activities.html).
{: .note}

{% include content-section-end.html %}
