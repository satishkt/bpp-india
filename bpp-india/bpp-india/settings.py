# -*- coding: utf-8 -*-

# Scrapy settings for priceup project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

from scrapy import log

#BOT_NAME = 'priceup'

SPIDER_MODULES = ['priceup.spiders']
#NEWSPIDER_MODULE = 'priceup.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'priceup (+http://www.yourdomain.com)'

ITEM_PIPELINES = {
    'priceup.pipelines.ElasticSearchPipeline': 300,
    'priceup.pipelines.JsonWriterPipeline': 800,
}
ELASTICSEARCH_SERVER = 'localhost' # If not 'localhost' prepend 'http://'
ELASTICSEARCH_PORT = 9200 # If port 80 leave blank
ELASTICSEARCH_USERNAME = ''
ELASTICSEARCH_PASSWORD = ''
ELASTICSEARCH_INDEX = 'priceup'
ELASTICSEARCH_TYPE = 'items'
ELASTICSEARCH_UNIQ_KEY = 'description'
ELASTICSEARCH_LOG_LEVEL = log.DEBUG
