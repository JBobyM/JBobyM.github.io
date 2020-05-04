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

DEFAULT_PAGINATION = 10

MARKUP = ('md', 'ipynb')

PLUGIN_PATH = ['./plugins','./pelican-plugins']
PLUGINS = ['ipynb.markup','readtime','post_stats', 'tipue_search','photos','assets']
# for search function, [plugin = tipue_search involved]
DIRECT_TEMPLATES = ['search','index','authors', 'categories', 'tags', 'archives','404']
#'share_post'
IGNORE_FILES = [".ipynb_checkpoints"]
STATIC_PATHS = ['img']

READING_TIME_LOWER_LIMIT = 3

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

# Social widget
SOCIAL = (
('Twitter','https://twitter.com/jbobym','My Twitter account'),
('Email', 'jbobyberry@gmail.com', 'My Email Address')
)

SOCIAL_PROFILE_LABEL = u'Stay in Touch'

LANDING_PAGE_TITLE = 'Data science avec Python: comprendre. Implementer. Réussir.'

APPLAUSE_BUTTON = True
#FREELISTS_NAME = "elegant@freelists.org"

STAT_COUNTER_PROJECT = 12249412
GOOGLE_ANALYTICS = u'UA-146174561-1'

STAT_COUNTER_SECURITY = u'4138fb33'

MAILCHIMP_FORM_ACTION = 'https://github.us8.list-manage.com/subscribe/post?u=517e9014963fd595cf3dbb7d4&amp;id=65134d64e7'
EMAIL_SUBSCRIPTION_LABEL = 'Get New Release Alert'
SUBSCRIBE_BUTTON_TITLE = 'Notify me'

PHOTO_RESIZE_JOBS = -1

#SHARE_POST_INTRO = "Share me with your friends on"


#SHARE_LINKS = [ ('twitter', 'Twitter'), ('facebook', 'Facebook'), ('email', 'Email'),('linkedin','LinkedIn') ]
#SHARE_POST_INTRO = "Share me with your friends on"
#share_post_intro= "Share this article on Elegant with"

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
