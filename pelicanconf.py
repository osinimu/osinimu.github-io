#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'osinimu'
SITENAME = 'osinimu'
SITEURL = 'https://osinimu.github.io'

PATH = 'content'

TIMEZONE = 'Africa/Lagos'

DEFAULT_LANG = 'en'
THEME = "themes/pelican-cid"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

SITESUBTITLE = """ Data scientist, Writer & Outlier """
AUTHOR_INTRO = """Osinimu is an alias for Ajulo Christopher. 
                  I'm constantly scanning my physical and digital worlds
                  looking for problems to be solved using data.
                  I write to not only express my views and opinions but
                   as a form of finding out what i do not know.   """

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
# Social widget
SOCIAL = (('twitter', 'http://twitter.com/_fosi'),
    ('github', 'https://github.com/osinimu'),)

# Menu
MENUITEMS = (
    ('Home', SITEURL),
    ('About', '/about/'),
    ('Blog', '/blog/'),
    ('Contact', '/contact/'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = PAGE_URL+'/index.html'

ARTICLE_PATHS = ['blog']
PAGE_PATHS = ['pages',]
STATIC_PATHS = ['images', 'pdfs']

ARCHIVES_SAVE_AS = 'blog/archives/index.html'

INDEX_SAVE_AS = 'blog/index.html'

USE_CUSTOM_MENU = True
CUSTOM_MENUITEMS = (('About', 'about'),
                   ('Blog', 'blog'),
             ('Contact', 'contact'),)


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

