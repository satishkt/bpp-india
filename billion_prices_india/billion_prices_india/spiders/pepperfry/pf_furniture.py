__author__ = 'satish'

import re
from urlparse import urlparse
import logging
import time

from scrapy.log import ScrapyFileLogObserver
import scrapy
from scrapy.selector import HtmlXPathSelector
from scrapy import log

from billion_prices_india.items import BillionPricesIndiaItem

class ClassName(object):

		"""Scrape Furniture tab from pepper fry"""

	
	name = "pf_furniture"
	allowed_domains = ["pepperfry.com"]
	start_urls = ['http://www.pepperfry.com/furniture-%s.html?type=hover-cat-nav' %s in ['-sofas-one-seater-sofas','-sofas-two-seater-sofas','-sofas-sofas-couches-three-seater','-sofas-sofa-sets','-sofas-recliners','-sofas-sofa-cum-beds','-sofa-sectionals','-futons','-poufee-stools'] ]
	crawledURL=[]
	detailedCrawled=[]

    AUTOTHROTTLE_ENABLED = True
    AUTOTHROTTLE_DEBUG = True
    DOWNLOAD_DELAY = 3
    DOWNLOAD_TIMEOUT = 30
    AUTOTHROTTLE_START_DELAY = 3

     def __init__(self, *args, **kwargs):
        ScrapyFileLogObserver(open("spider.log", 'w'), level=logging.INFO).start()
        ScrapyFileLogObserver(open("spider_error.log", 'w'), level=logging.ERROR).start()

    def __getHostURL(self,url):
    	parsed_uri = urlparse(url)
        domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
        return domain
	
	def parse(self,response):
		log.msg(response.url)
		baseurl = self.__getHostURL(response.url)	








