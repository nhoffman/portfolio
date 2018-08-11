#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Noah Hoffman'
SITENAME = 'Noah Hoffman, MD, PhD'
SITEURL = 'https://faculty.washington.edu/ngh2/home'

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'English'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('UW Laboratory Medicine', 'https://depts.washington.edu/labweb'),
    ('UW Medicie Bio', 'http://www.uwmedicine.org/bios/noah-hoffman'),
    ('borborygmi (blog)', 'https://nhoffman.github.io/borborygmi/'),
)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)
SOCIAL = None


DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = "./mytheme"

# defines order of page titles in the header
PAGE_ORDER_BY = 'page-order'

# see https://python-markdown.github.io/extensions/toc/
MARKDOWN = {
  'extension_configs': {
    'markdown.extensions.toc': {
        'baselevel': 2,
    },
    'markdown.extensions.codehilite': {'css_class': 'highlight'},
    'markdown.extensions.extra': {},
    'markdown.extensions.meta': {},
  },
  'output_format': 'html5',
}
