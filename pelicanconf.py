#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Keith Miller'
AUTHOR_REAL = 'Keith'
AUTHOR_IMAGE = 'me.jpeg'
MOREABOUTMEURL = 'authors.html'
SITENAME = 'the packetologist'
SITEURL = ''

PATH = 'content'
PAGE_PATHS = ['pages']

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/packetologist'),
          ('linkedin', 'https://www.linkedin.com/in/keith-miller-b761073a/'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Custom settings
THEME = 'pelican-themes/uikit'
DELETE_OUTPUT_DIRECTORY = True
DISPLAY_CATEGORIES_ON_MENU = False
SUMMARY_MAX_LENGTH = 100

#UIKIT Config
DISPLAY_TAGS_ON_SIDEBAR_LIMIT = 5
DISPLAY_LINKS_ON_SIDEBAR_LIMIT = 5
LICENSE = {
    'cc_name':"by-sa",
    'hosted':False,
    'compact':True,
    'brief':False
    }
