__author__ = 'mandeepak'
__author__ = 'mandeepak'

import re
from bpp_wpi.spiders.dw_retailprice import PriceSpider
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

from scrapy.contrib.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.contrib.spiders import Rule

class PriceSpider(scrapy.Spider):

    name = "dw_retailprice_Tea"
    allowed_domains = ["dataweave.in"]
    user="mandeepa"
    apikey=""
    startdate=""
    enddate=""
    AUTOTHROTTLE_ENABLED = True
    AUTOTHROTTLE_DEBUG = True
    DOWNLOAD_DELAY = 10
    DOWNLOAD_TIMEOUT = 180
    AUTOTHROTTLE_START_DELAY = 10

    start_urls = ['http://api.dataweave.in/v1/retail_prices_india/findByCityAndCommodity/?api_key=67fbcf2894171449d53099c1d3079956fe0dd8d8&city=%s&commodity=Sugar&start_date=20130101&end_date=20140101&page=1&per_page=1' %city for city in ['CHANDIGARH','DELHI','HISAR','KARNAL','SHIMLA','MANDI','SRINAGAR','JAMMU','AMRITSAR','LUDHIANA','BHATINDA','LUCKNOW','KANPUR','VARANASI','AGRA','DEHRADUN','RAIPUR','AHMEDABAD','RAJKOT','BHOPAL','INDORE','MUMBAI','NAGPUR','JAIPUR','JODHPUR','KOTA','PATNA','BHAGALPUR','RANCHI','BHUBANESHWAR','CUTTACK','GUWAHATI','SAMBALPUR','KOLKATA','SILIGURI','ITANAGAR','SHILLONG','AIZWAL','DIMAPUR','AGARTALA','HYDERABAD','VIJAYWADA','BENGALURU','ERNAKULAM','THIRUCHIRAPALLI']
                 ]
    def __init__(self, *args, **kwargs):
        ScrapyFileLogObserver(open("spider.log", 'w'), level=logging.INFO).start()
        ScrapyFileLogObserver(open("spider_error.log", 'w'), level=logging.ERROR).start()

    p=PriceSpider()
    def parse(self,response):
        return self.p.getItems(response.body)



