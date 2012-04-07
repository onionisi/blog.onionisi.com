---
layout: page
title: /home
---
{% include JB/setup %}

## /dev/chongyang

杨冲，男，86年生人，狐假虎威，现居绵阳，newbie of CS，loving open、Linux、coding and 我妹纸。

## /usr/share

<ul class="posts">
  {% for post in site.posts %}
    <li><span>{{ post.date | date_to_string }}</span> &raquo; <a href="{{ BASE_PATH }}{{ post.url }}">{{ post.title }}</a></li>
  {% endfor %}
</ul>

