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

PLUGIN_PATH = ['./plugins','./pelican-plugins']
PLUGINS = ['ipynb.markup','post_stats']
IGNORE_FILES = [".ipynb_checkpoints"]
STATIC_PATHS = ['img']

READING_TIME_LOWER_LIMIT = 4

THEME = "C:\\Users\\Kathee\\Documents\\Blog\\JBobyM.github.io\\pelican-themes\\elegant"

# This part is for estimating the reading time
ERT_WPM = 200
ERT_FORMAT = '{time} read'
ERT_INT = True

AUTHORS = {
    "John Boby Mesadieu": {
        "url": "https://jbobym.github.io/",
        "blurb": "is the creator and lead developer of Elegant theme. This is for testing the blurb feature; and obviously it will remove its place to other more interesting content. Far away frow here, ther is lots of different types of people, the main ones are happy and not-happy ones. I'd rather stand it like so because speaking of happiness, we might only refer to high segmented real duality ",
        "avatar": "https://avatars0.githubusercontent.com/u/50599667?s=400&u=546490185c7aa72c309351ba05a720bc4bc645eb&v=4"
    },
    "Pablo Iranzo Gómez": {
        "url": "http://iranzo.github.io",
        "blurb": " opensource enthusiast and Lego fan doing some python simple programs like @redken_bot in telegram, etc",
        "avatar": "https://avatars.githubusercontent.com/u/312463",
    },
    "Jack De Winter": {
        "url": "http://jackdewinter.github.io",
        "blurb": "ever evolving, ever learning",
    },
}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
