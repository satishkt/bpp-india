__author__ = 'satish'

import time
import logging
import scrapy
from scrapy.selector import HtmlXPathSelector
from scrapy.log import ScrapyFileLogObserver
from scrapy import log
import locale
import string
from scrapy.http import Request


class BasePepperFry(scrapy.Spider):
    """Scrape pet supplies tab from pepper fry"""
    allowed_domains = ["ocl-cal.gc.ca"]
    name = "ocl_spyder"

    start_urls = ['https://ocl-cal.gc.ca/app/secure/orl/lrrs/do/lbbLstg?pfx=%s&showAll=false' % s for s in
                  string.ascii_uppercase]
    crawledURL = []
    detailedCrawled = []
    crawledPageUrls = []


    def __init__(self, *args, **kwargs):
        locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
       # ScrapyFileLogObserver(open("spider.log", 'w'), level=logging.INFO).start()
        #ScrapyFileLogObserver(open("spider_error.log", 'w'), level=logging.ERROR).start()

    def parse(self, response):
        log.msg(response.url)
        urls = []
        hxs = HtmlXPathSelector(response)

        # Look for category count total.
        tot_cat_count_list = hxs.xpath('/html/body/div/div/div[6]/div[2]/ul/li/a/text()')
        for li in tot_cat_count_list:
            print li.extract()
