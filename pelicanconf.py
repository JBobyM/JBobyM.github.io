#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'John Boby Mesadieu'
SITENAME = 'DataSight'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Port-au-Prince'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

MARKUP = ('md', 'ipynb')

PLUGIN_PATH = './plugins'
PLUGINS = ['ipynb.markup','i18n_subsites']
JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}
STATIC_PATHS = ['img']

THEME = "C:\\Users\\Kathee\\Documents\\Blog\\JBobyM.github.io\\pelican-themes\\elegant"

AUTHORS = {
    u'Andy Wegner': {
        u'blurb': """ is a father, an engineer and a computer scientist. He is interested in online
            community building, tinkering with new code and building new applications.
            He writes about his experiences with each of these.""",
        u'friendly_name': "Andy Wegner",
        u'url': 'https://andrewwegner.com/'
    }
}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True