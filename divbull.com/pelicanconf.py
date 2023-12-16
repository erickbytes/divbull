import getpass

AUTHOR = "Erick"
SITENAME = "Diversified Bullish"
SITESUBTITLE = "An Investing and Stocks Blog"
SITEURL = "https://divbull.com"
PATH = "content"
TIMEZONE = "America/Chicago"
DEFAULT_LANG = "en"
GITHUB_URL = "https://github.com/erickbytes/divbull"
# Feed generation is usually not desired when developing
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
FEED_ALL_ATOM = "feeds/all.atom.xml"
TAG_FEED_ATOM = "feeds/{slug}.tag.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"
FEED_ALL_RSS = "feeds/all.rss.xml"
CATEGORY_FEED_RSS = "feeds/{slug}.rss.xml"
MENUITEMS = [
    ["RSS", "feeds/all.rss.xml"],
    ["Atom", "feeds/all.atom.xml"],
    ["Github", "https://github.com/erickbytes/divbull"],
]
DEFAULT_PAGINATION = 10
THEME = "/home/erickbytes/projects/divbull/blue-penguin"
STATIC_PATHS = ["images", "blog", "extra"]
ARTICLE_PATHS = ["images", "blog"]
EXTRA_PATH_METADATA = {
    "extra/robots.txt": {"path": "robots.txt"},
    "extra/favicon.ico": {"path": "favicon.ico"},
    "extra/ads.txt": {"path": "ads.txt"},
}
