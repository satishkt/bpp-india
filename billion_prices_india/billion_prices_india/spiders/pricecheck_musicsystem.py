__author__ = 'mandeepak'

import re

from scrapy.log import ScrapyFileLogObserver
import scrapy
import json
from scrapy.selector import HtmlXPathSelector
from scrapy import log
from billion_prices_india.items import BillionPricesIndiaItem
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.http import Request
from scrapy import log
from os import path
import os
import urllib
import string
from bs4 import UnicodeDammit
from urlparse import urlparse
import logging
import time

class PriceSpider(scrapy.Spider):

    name = "pc_musicsystem"
    allowed_domains = ["pricecheckindia.com"]
    start_urls = ['http://api.pricecheckindia.com/feed/product/music_systems.json?user=mandeepa&key=UPIFDOZVNPOVPFSF']

    AUTOTHROTTLE_ENABLED = True
    AUTOTHROTTLE_DEBUG = True
    DOWNLOAD_DELAY = 3
    DOWNLOAD_TIMEOUT = 180
    AUTOTHROTTLE_START_DELAY = 3
    category=""

    def __init__(self, *args, **kwargs):
        ScrapyFileLogObserver(open("spider.log", 'w'), level=logging.INFO).start()
        ScrapyFileLogObserver(open("spider_error.log", 'w'), level=logging.ERROR).start()

    def parse(self, response):
        results = json.loads(response.body)
        items=[]
        for result in results['product']:
            item = BillionPricesIndiaItem()
            item['product'] = result['model']
            item['category'] = "Music System"
            if len(result['stores']) >0:
                for store in result['stores']:
                    price=float(store['price'])
                    item['date']=str(time.strftime("%d/%m/%Y"))
                    item['vendor']=store['website']
                    item['quantity'] = 1
                    item['measure']= 'pcs'
                    item['price']=price
                    item['unitprice']=price
                    items.append(item)
        return items




if __name__ == '__main__':
	obj=PriceSpider()
