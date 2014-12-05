__author__ = 'mandeepak'
__author__ = 'mandeepak'

import re
import datetime
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

    name = "dw_weather"
    allowed_domains = ["dataweave.in"]
    apikey="67fbcf2894171449d53099c1d3079956fe0dd8d8"
    start_urls = ['http://api.dataweave.in/v1/retail_prices_india']

    def __init__(self, *args, **kwargs):
        ScrapyFileLogObserver(open("spider.log", 'w'), level=logging.INFO).start()
        ScrapyFileLogObserver(open("spider_error.log", 'w'), level=logging.ERROR).start()

    def parse(self, response):

        weather="http://api.dataweave.in/v1/indian_weather/findByCity/?api_key=%s"%(self.apikey)
        items=[]
        for city in ['Hyderabad']:
            for days in range(365):
                date_str=datetime.date(2013, 01, 01) + datetime.timedelta(days)
                url=weather+'&city='+city+'&date='+str(date_str).replace('-','')
                results= requests.get(url)

                for result in results.json()['data']:
                     item = BppWpiItem()
                     item[city]='Hyderabad'
                     item['date']=result['date']
                     if result['24 Hours Rainfall'][0]=='NIL':
                         item['rainfall'] ='0'

                     else:
                        item['rainfall'] =result['24 Hours Rainfall'][0]
                items.append(item)
        return items






if __name__ == '__main__':
	obj=PriceSpider()
