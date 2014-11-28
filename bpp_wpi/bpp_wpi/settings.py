# -*- coding: utf-8 -*-

# Scrapy settings for bpp_wpi project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'bpp_wpi'

SPIDER_MODULES = ['bpp_wpi.spiders']
NEWSPIDER_MODULE = 'bpp_wpi.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'bpp_wpi (+http://www.yourdomain.com)'

DOWNLOADER_MIDDLEWARES = {
    'bpp_wpi.middleware.CustomHttpProxyMiddleware': 543,
    'bpp_wpi.middleware.CustomUserAgentMiddleware': 545,
    'scrapy.contrib.downloadermiddleware.retry.RetryMiddleware': 200,
}

COOKIES_ENABLED = True
COOKIES_DEBUG = True
#NEWSPIDER_MODULE = 'billion_prices_india.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'billion_prices_india (+http://www.yourdomain.com)'

# ITEM_PIPELINES = {
#     'billion_prices_india.pipelines.ElasticSearchPipeline': 300,
#     'billion_prices_india.pipelines.CSVWriterPipeline': 800,
# }
# ELASTICSEARCH_SERVER = 'localhost' # If not 'localhost' prepend 'http://'
# ELASTICSEARCH_PORT = 9200 # If port 80 leave blank
# ELASTICSEARCH_USERNAME = ''
# ELASTICSEARCH_PASSWORD = ''
# ELASTICSEARCH_INDEX = 'billion_prices_india'
# ELASTICSEARCH_TYPE = 'items'
# ELASTICSEARCH_UNIQ_KEY = 'description'
# ELASTICSEARCH_LOG_LEVEL = log.DEBUG

ITEM_PIPELINES = {
    'scrapy_mongodb.MongoDBPipeline': 900,
}

LOG_LEVEL = 'INFO'
MONGODB_URI = 'mongodb://54.148.179.83:27017'
MONGODB_DATABASE = 'scrapy'
MONGODB_COLLECTION = 'bpp_wpi'