__author__ = 'mandeepak'

import re

from scrapy.log import ScrapyFileLogObserver
import scrapy
import json
from scrapy.selector import HtmlXPathSelector
from scrapy import log
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from bpp_wpi.items import BppWpiItem
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
import requests
class PriceSpider(scrapy.Spider):

    name = "dw_retailprice"
    allowed_domains = ["dataweave.in"]
    apikey="98f8ff1940ba3da0d8a6b70bb1e02510b9d2d7cb"
    start_urls = ['http://api.dataweave.in/v1/retail_prices_india']
    start_date="20130101"
    end_date="20140101"

    def __init__(self, *args, **kwargs):
        ScrapyFileLogObserver(open("spider.log", 'w'), level=logging.INFO).start()
        ScrapyFileLogObserver(open("spider_error.log", 'w'), level=logging.ERROR).start()

    def parse(self, response):

        urlcities="http://api.dataweave.in/v1/retail_prices_india/listAllCities/?api_key=%s"%(self.apikey)
        urlcommodities="http://api.dataweave.in/v1/retail_prices_india/listAllCommodities/?api_key=%s"%(self.apikey)

        cities= requests.get(urlcities)
        commodities=requests.get(urlcommodities)
        for city in cities.json()["data"]:
            for commodity in commodities.json()["data"]:
                url="http://api.dataweave.in/v1/retail_prices_india/findByCityAndCommodity/?api_key=%s&city=%s&commodity=%s&start_date=%s&end_date=%s&page=1&per_page=10"%(self.apikey,city,commodity,self.start_date,self.end_date)
                results= requests.get(url)
                for result in results.json()['data']:
                    item = BppWpiItem()
                    item['date']=result['date']
                    item['zone'] = result['zone']
                    item['center'] = result['centre']
                    item['commodity'] = result['commodity']
                    item['price'] = float(result['price'])
                    yield item






if __name__ == '__main__':
	obj=PriceSpider()
