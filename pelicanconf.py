#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import re
import os
import shutil

AUTHOR = 'JOHN BOBY MESADIEU'
AUTHOR_LOWER = 'John Boby Mesadieu'
AUTHOR_SHORTENED = 'JBobyM'
AUTHOR_SUBTITLE = 'Data Scientist, full-stack mobile app developper, statistician-economist'
SITENAME = 'DataSight'
SITESUBTITLE = u'Stories about Python, R, Data Science and Statistics'
SITE_DESCRIPTION = 'DataSight | Stories about Python, R, Data Science and Statistics'
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

DEFAULT_PAGINATION = False
USE_SHORTCUT_ICONS = True

# Regional Settings
DATE_FORMATS = {'en': '%b %d, %Y'}

# Plugins and extensions
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {
            'css_class': 'highlight'
        },
        'markdown.extensions.extra': {},
        'markdown.extensions.toc': {
            'permalink': 'true'
        },
        'markdown.extensions.meta': {},
        'markdown.extensions.admonition': {},
    }
}



MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./plugins_','./pelican-plugins']
PLUGINS = ['pelican-ipynb.markup','sitemap',
           'extract_toc',
           'neighbors',
           'render_math',
           'related_posts',
           'share_post',
           'series',
           'tipue_search',
           'summary',       # auto-summarizing articles
           'feed_summary',  # use summaries for RSS, not full articles
           'pelican-ipynb.liquid',  # for embedding notebooks
           'liquid_tags.img',  # embedding images
           'liquid_tags.video',  # embedding videos
           'liquid_tags.include_code',  # including code blocks
           'liquid_tags.literal',
           'tag_cloud',
           ]

IGNORE_FILES = ['.ipynb_checkpoints']
STATIC_PATHS = ['figures', 'images', 'downloads']


SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'hourly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

# Appearance
THEME = "C:\\Users\\Kathee\\Documents\\aegis-blog\\theme\\pelican-aegis-jupyter-theme"
DEFAULT_PAGINATION = False

# Defaults
DEFAULT_CATEGORY = 'Miscellaneous'
USE_FOLDER_AS_CATEGORY = True
ARTICLE_URL = u'{slug}'
PAGE_URL = u'{slug}'
PAGE_SAVE_AS = u'{slug}.html'

# Feeds
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
CATEGORY_FEED_ATOM = None
CATEGORY_FEED_RSS = None

#CLAIM_GOOGLE = "ZsWFnpirKDgtbmwb1YRymDnSfvnUrpzCbf6LD1F_4TY"
#CLAIM_BING = "8FF1B025212A47B5B27CC47163A042F0"

DIRECT_TEMPLATES = (('index', 'archives', 'search', '404', 'about'))
AUTHOR_SAVE_AS = ''
#USE_SHORTCUT_ICONS = True

# Labels
RELATED_POSTS_LABEL = 'Related Posts'       # articles that share common tags
SHARE_POST_INTRO = 'Share This Post :'
CARD_TEXT = 'MOST POPULAR'

# SMO
FEATURED_IMAGE = SITEURL + '/theme/img/logo_icon_background.png'
ENABLE_MATHJAX = True

# files are actually saved in /aegis-jupyter/static/img/, but its copied to /output/theme/img/.
# just store any meta files in /aegis-jupyter/static/, and you are good.
PROFILE_PHOTO_FOOTER = "theme/img/profile_photo_footer.jpg"
PROFILE_PHOTO_ABOUT = "theme/img/profile_photo_about.jpg"
INDEX_BANNER_IMAGE = "theme/img/index_banner_image.jpg"
LOGO_WITH_SUBTITLE = "theme/img/logo_with_subtitle.png"  # logo created at "https://vectr.com/"

GITHUB_LINK = 'https://github.com/JBobyM'
LINKEDIN_LINK = 'https://www.linkedin.com/in/john-boby-mesadieu-9662635b/'

ABOUT_PAGE = 'about.html'
ARCHIVE_PAGE = 'archives.html'

# when developing offline, set it as False.
USE_CDN = False
NOTEBOOK_DIR = 'downloads/notebooks'
MISC_DIR = 'downloads/misc'



RESUME_PDF_LINK = 'downloads/misc/J_Boby_Mesadieu_CV_.pdf'
RESUME_BUTTON_TEXT = 'Download CV'

# copies files that are used when writing jupyter notebook to output directory
JUPYTER_IMAGES_DIR = 'content/downloads/notebooks/jupyter_images'

def copy_jupyter_images_to_output(dir):
    jupyter_image_dir = re.split('\\\\|\\/|\\/\\/', dir)[-1]

    if not os.path.exists(os.path.join('output', jupyter_image_dir)):
        os.makedirs(os.path.join('output', jupyter_image_dir))

    for file in os.listdir(dir):
        shutil.copy2(os.path.join(dir, file), os.path.join('output', jupyter_image_dir))


copy_jupyter_images_to_output(JUPYTER_IMAGES_DIR)


############################ Social Media Shares ############################

# About Page
ABOUT_PAGE_TITLE = 'About JBobyM'
ABOUT_PAGE_DESCRIPTION = u'Stories about Python, R, Data Science and Statistics | by John Boby Mesadieu'

# Archive Page
ARCHIVE_PAGE_TITLE = 'Archive'
ARCHIVE_PAGE_DESCRIPTION = 'Full Archives of DataSight'

# landing(index) page description
INDEX_PAGE_TITLE = 'DataSight'
INDEX_PAGE_DESCRIPTION = u'Stories about Python, R, Data Science and Statistics | by John Boby Mesadieu'

### social media share debugger
# Twitter: https://cards-dev.twitter.com/validator
# Facebook: https://developers.facebook.com/tools/debug/


FOOTER_TITLE = 'ABOUT JBobyM'
TEXT_FOOTER = 'Statistician-Economist, Data Scientist and self-taught full-stack mobile app developer who"s letting ' \
              'his passion of intriguing astonishing insights from data and implementing ready-to-use best-in-class software solutions lead his path.' \
              'I am good at creating clean, easy-to-read codes for data ' \
              'analysis. I enjoy assisting my fellow scientists by developing accessible and reproducible codes.'
EMAIL = 'jbobyberry@gmail.com'
LOCATION = 'Petion-ville, Haïti'
COPYRIGHT_NOTICE = 'Handcrafted by aegis4048 @2018'

CARD_POSTS = {
    'Parse PDF Files While Retaining Structure with Tabula-py': 'parse-pdf-files-while-retaining-structure-with-tabula-py',
}


INCLUDE_PROGRESSBAR = True
PROGRESSBAR_COLOR = '#370028'


# code snippet for processing variables for auto-generation of Tech Stacks
NUM_MAX_STAR = 5
TECH_STACKS = {'Python': 5,
               'Bootstrap': 4,
               'HTML': 4,
               'Django': 4,
               'jQuery': 4,
               'CSS': 4,
               }

def process_techstacks(tech_dict, num_max_star):
    num_stacks = len(tech_dict)
    tech_stacks_list = [{key: {'filled_star': value, 'empty_star': num_max_star - value }} for key, value in tech_dict.items()]
    tech_stacks_left = tech_stacks_list[:num_stacks // 2 + num_stacks % 2]
    tech_stacks_right = tech_stacks_list[num_stacks // 2 + num_stacks % 2:]
    return tech_stacks_left, tech_stacks_right


TECH_STACKS_LEFT, TECH_STACKS_RIGHT = process_techstacks(TECH_STACKS, NUM_MAX_STAR)

PORT = 8000

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
