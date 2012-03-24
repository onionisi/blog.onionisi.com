---
layout: page
title: 欢迎大家
---
{% include JB/setup %}

欢迎大家来到我的博客，我是杨冲，呵呵......

## 日记

我的生活

<ul class="posts">
  {% for post in site.posts %}
    <li><span>{{ post.date | date_to_string }}</span> &raquo; <a href="{{ BASE_PATH }}{{ post.url }}">{{ post.title }}</a></li>
  {% endfor %}
</ul>
