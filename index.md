---
layout: page
title: /home
---
{% include JB/setup %}

## /dev/chongyang

杨冲，男，86年生人，狐假虎威，现漂绵阳，目前供职于一家中型国企，初级码农，newbie of CS，热爱开源、Linux、coding.

## /usr/share

<ul class="posts">
  {% for post in site.posts %}
    <li><span>{{ post.date | date_to_string }}</span> &raquo; <a href="{{ BASE_PATH }}{{ post.url }}">{{ post.title }}</a></li>
  {% endfor %}
</ul>


