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

class PriceSpider(scrapy.Spider):

    name = "dw_retailprice_Tea"
    allowed_domains = ["dataweave.in"]
    user="mandeepa"
    apikey=""
    startdate=""
    enddate=""
    start_urls = ['http://api.dataweave.in/v1/retail_prices_india/findByCityAndCommodity/?api_key=67fbcf2894171449d53099c1d3079956fe0dd8d8&city=%s&commodity=Tea Loose&start_date=20130101&end_date=20140101&page=1&per_page=1' %city for city in ['CHANDIGARH','DELHI','HISAR','KARNAL','SHIMLA','MANDI','SRINAGAR','JAMMU','AMRITSAR','LUDHIANA','BHATINDA','LUCKNOW','KANPUR','VARANASI','AGRA','DEHRADUN','RAIPUR','AHMEDABAD','RAJKOT','BHOPAL','INDORE','MUMBAI','NAGPUR','JAIPUR','JODHPUR','KOTA','PATNA','BHAGALPUR','RANCHI','BHUBANESHWAR','CUTTACK','GUWAHATI','SAMBALPUR','KOLKATA','SILIGURI','ITANAGAR','SHILLONG','AIZWAL','DIMAPUR','AGARTALA','HYDERABAD','VIJAYWADA','BENGALURU','ERNAKULAM','THIRUCHIRAPALLI']
                 ]


    AUTOTHROTTLE_ENABLED = True
    AUTOTHROTTLE_DEBUG = True
    DOWNLOAD_DELAY = 3
    DOWNLOAD_TIMEOUT = 180
    AUTOTHROTTLE_START_DELAY = 3
    category=""

    def __init__(self, *args, **kwargs):
        ScrapyFileLogObserver(open("spider.log", 'w'), level=logging.INFO).start()
        ScrapyFileLogObserver(open("spider_error.log", 'w'), level=logging.ERROR).start()


    def getItems(self,jsonstr):
        results = json.loads(jsonstr)
        print(results)
        items=[]
        for result in results['data']:
            item = BppWpiItem()
            item['date']=result['date']
            item['zone'] = result['zone']
            item['center'] = result['centre']
            item['commodity'] = result['commodity']
            item['price'] = float(result['price'])
            items.append(item)
        return items


    def parse(self, response):
        self.getItems(response.body)






if __name__ == '__main__':
	obj=PriceSpider()
