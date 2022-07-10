AUTHOR = 'Erick'
SITENAME = 'Diversified Bullish'
SITESUBTITLE = 'An Investing and Stocks Blog'
SITEURL = 'https://divbull.com'
PATH = 'content'
TIMEZONE = 'America/Chicago'
DEFAULT_LANG = 'en'
GITHUB_URL = 'https://github.com/erickbytes/divbull'
# Feed generation is usually not desired when developing
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
FEED_ALL_ATOM = 'feeds/all.atom.xml'
TAG_FEED_ATOM = 'feeds/{slug}.tag.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/{slug}.rss.xml'
MENUITEMS = [
    ['RSS', "feeds/all.rss.xml"],
    ['Atom', "feeds/all.atom.xml"],
    ['Github', "https://github.com/erickbytes/divbull"],
]
DEFAULT_PAGINATION = 10
THEME = "/home/erick/Desktop/Projects/divbull/blue-penguin"
STATIC_PATHS = [
    'images',
    'extra/robots.txt',
    'extra/favicon.ico',
]
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
}
# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
# Blogroll
# LINKS = (('Pelican', 'https://getpelican.com/'),
#          ('Python.org', 'https://www.python.org/'),
#          ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
#          ('You can modify those links in your config file', '#'),)