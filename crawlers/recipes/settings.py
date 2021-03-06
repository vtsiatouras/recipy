# Scrapy settings for recipes project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import os
import sys

from pathlib import Path

root_path = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__))).split('crawlers')[0]
sys.path.append(str(root_path))
DJANGO_DIR = str(Path(__file__).resolve().parent.parent) + '/api'
sys.path.append(DJANGO_DIR)

import django
os.environ['DJANGO_SETTINGS_MODULE'] = 'api.conf.settings'
django.setup()

BOT_NAME = 'recipes'

SPIDER_MODULES = ['recipes.spiders']
NEWSPIDER_MODULE = 'recipes.spiders'

DUPEFILTER_DEBUG = False

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = "Scrapy/VERSION (+https://scrapy.org)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 1
# amount of time (in secs) that the downloader will wait before timing out
DOWNLOAD_TIMEOUT = 600

# The download delay setting will honor only one of:
# important: https://support.scrapinghub.com/support/solutions/articles/22000188399-using-crawlera-with-scrapy
CONCURRENT_ITEMS = 100
# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 6
CONCURRENT_REQUESTS_PER_DOMAIN = 6
CONCURRENT_REQUESTS_PER_IP = 0

# Disable cookies (enabled by default)
COOKIES_ENABLED = False
COOKIES_DEBUG = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'recipes.middlewares.RecipesSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'recipes.middlewares.RecipesDownloaderMiddleware': 543,
#}

# amount of time (in secs) that the downloader will wait before timing out
DOWNLOAD_TIMEOUT = 600

RANDOMIZE_DOWNLOAD_DELAY = True

DOWNLOADER_STATS = True

DOWNLOAD_FAIL_ON_DATALOSS = False

# RetryMiddleware
RETRY_ENABLED = True
RETRY_TIMES = 1
RETRY_HTTP_CODES = [500, 502, 503, 504, 522, 524, 408, 429]

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'recipes.pipelines.RecipesPipeline': 200,
    'recipes.pipelines.DBStoragePipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = False
# The initial download delay
AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
HTTPCACHE_ENABLED = False
HTTPCACHE_EXPIRATION_SECS = 0
HTTPCACHE_DIR = 'httpcache'
HTTPCACHE_IGNORE_HTTP_CODES = []
HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
