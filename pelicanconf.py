#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'cjer'
SITENAME = 'OpenBus'
SITEURL = ''

PATH = 'content'
ARTICLE_PATHS = ['blog']
PAGE_PATHS = ['']

#OUTPUT_PATH = 'output'

TIMEZONE = 'Asia/Jerusalem'

DEFAULT_LANG = 'en'

import platform
if platform.system() == 'Windows':
    DATE_FORMATS = {'en': ('usa', '%b %d, %Y')}
else:
    DATE_FORMATS = {'en': ('en_US.UTF-8', '%b %d, %Y')}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('simplistic', 'http://simplistic.me/'),)

# Social widget
#SOCIAL = ()

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# m.css
THEME = 'm.css/pelican-theme'
THEME_STATIC_DIR = 'static'
STATIC_PATHS = ['static']

STATIC_URL = '{path}'

M_CSS_FILES = ['https://fonts.googleapis.com/css?family=Source+Sans+Pro:400,400i,600,600i%7CSource+Code+Pro:400,400i,600',
               '/static/m-dark.css']
M_THEME_COLOR = '#22272e'

PLUGIN_PATHS = ['m.css/pelican-plugins']
PLUGINS = ['m.htmlsanity', 'm.components', 'm.filesize', ]

M_BLOG_NAME = 'OpenBus Blog'
M_BLOG_URL = 'blog/'

M_SITE_LOGO_TEXT = 'OpenBus'

M_LINKS_NAVBAR1 = [('למה?', 'why/', 'why', []),
                   ('כלים', 'tools/', 'tools', [
                   		('דירוגובוס', 'tools/buscore/', ''),
                   		('אוטונגישות', 'tools/accessibility/', '')
                   		]),
                   ('מידע', 'data/', 'data', [
                        ('GTFS', 'data/gtfs/', ''),
                    	('SIRI', 'data/siri/', '')
                   	])]

M_LINKS_NAVBAR2 = [('בלוג', 'blog/', '[blog]', []),
                   ('צור קשר', 'contact/', 'contact', [])]


M_LINKS_FOOTER1 = [('OpenBus', '/'),
                   ('למה?', 'why/'),]

M_LINKS_FOOTER2 = [('שימושי', ''),
				   ('כלים', 'tools/'),
                   ('מידע', 'data/'),]

M_LINKS_FOOTER3 = [('צור קשר', ''),
                   ('GitHub', 'https://github.com/hasadna/open-bus'),
                   ('Slack', 'https://hasadna.slack.com'),
                   ('googlegroup', 'https://groups.google.com/forum/#!forum/openbus-israel'),]

M_FINE_PRINT = """
OpenBus. Copyright © `EMAIL <mailto:filler@email.address>`_, 2018. All rights
reserved.
"""

# Defaults to ['index', 'categories', 'authors', 'archives']
DIRECT_TEMPLATES = ['archives']

# Defaults to ['index']
PAGINATED_DIRECT_TEMPLATES = ['archives']

FORMATTED_FIELDS = ['summary', 'description', 'landing', 'badge', 'header', 'footer']

M_NEWS_ON_INDEX = ("Latest news on our blog", 3)

M_METADATA_AUTHOR_PATH = 'blog/authors'
M_METADATA_CATEGORY_PATH = 'blog/categories'
M_METADATA_TAG_PATH = 'blog/tags'

SLUGIFY_SOURCE = 'basename'
PATH_METADATA = '(blog/)?(?P<slug>.+).rst'

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
ARCHIVES_URL = 'blog/'
ARCHIVES_SAVE_AS = 'blog/index.html'
ARTICLE_URL = '{slug}/' # category is part of the slug (i.e., examples)
ARTICLE_SAVE_AS = '{slug}/index.html'
AUTHOR_URL = 'author/{slug}/'
AUTHOR_SAVE_AS = 'author/{slug}/index.html'
CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'
