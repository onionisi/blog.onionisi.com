#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Chong'
AUTHOR_FULLNAME = u'Chong Yang'
SITENAME = u'onionisi'
SITEURL = 'www.onionisi.com'
SITETAGLINE = 'fprintf(post, "%s\\n", daily_life)'
DISPLAY_PAGES_ON_MENU = True

PATH = 'content'

TIMEZONE = 'Asia/Chongqing'

DEFAULT_LANG = u'en'

# Theme
THEME = "/Users/chong/code/blog_theme"
EMAIL_ADDRESSS = "iamyangchong@gmail.com"
GITHUB_ADDRESS = "github.com/onionisi"
TWITTER_ADDRESS = "twitter.com/onionisi"

# Plugin
PLUGIN_PATHS = ['/Users/chong/code/pelican-plugins']
PLUGINS = ['assets']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

DEFAULT_PAGINATION = 3

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
