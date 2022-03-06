import glob
from pathlib import Path

from pelican.settings import DEFAULT_CONFIG
from pelican.readers import MarkdownReader

config = DEFAULT_CONFIG.copy()

AUTHOR = 'Noah Hoffman'
SITENAME = 'Noah Hoffman, MD, PhD'
SITEURL = 'https://faculty.washington.edu/ngh2/home'

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('DLMP Bio', 'https://dlmp.uw.edu/faculty/hoffman'),
    ('UW Medicine Bio', 'http://www.uwmedicine.org/bios/noah-hoffman'),
    ('borborygmi (blog)', 'https://nhoffman.github.io/borborygmi/'),
)

GITHUB_CORNER_URL = 'https://github.com/nhoffman/portfolio'

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)
SOCIAL = []

DEFAULT_PAGINATION = False

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

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

THEME = "./Flex"
# does nothing?
# THEME_COLOR = 'light'

# defines order of page titles in the header
PAGE_ORDER_BY = 'page-order'

# prevent Pelican from reading files matching the following patterns
IGNORE_FILES = ['.#*', 'includes', 'templates', 'README.md']
# place files replacing theme templates in ./content/templates
THEME_TEMPLATES_OVERRIDES = ['./content/templates']
DIRECT_TEMPLATES = (('index',))

# render markdown contents from files in /content/includes and make
# accesible from INCLUDES variable in html templates
INCLUDES = {}
for fname in glob.glob('./content/includes/*.md'):
    pth = Path(fname)
    INCLUDES[pth.stem], _ = MarkdownReader(config).read(fname)
