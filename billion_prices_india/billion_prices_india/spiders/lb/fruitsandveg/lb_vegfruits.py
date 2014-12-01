__author__ = 'satish'

import time
import logging
import scrapy
from scrapy.selector import HtmlXPathSelector
from scrapy.log import ScrapyFileLogObserver
from scrapy import log
import locale
from scrapy.http import Request



class LbFruitsVegetables(scrapy.Spider):
    name = "lb_fruitsvegetables"
    start_urls = ['http://www.localbanya.com/products/Fruits-&-Vegetables/Vegetables/180/57']

    allowed_domains = ["localbanya.com"]
    AUTOTHROTTLE_ENABLED = True
    AUTOTHROTTLE_DEBUG = True
    DOWNLOAD_DELAY = 3
    DOWNLOAD_TIMEOUT = 30
    AUTOTHROTTLE_START_DELAY = 3
    crawledURL = []
    detailedCrawled = []
    crawledPageUrls = []


    def __init__(self, *args, **kwargs):
        locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
        ScrapyFileLogObserver(open("spider.log", 'w'), level=logging.INFO).start()
        ScrapyFileLogObserver(open("spider_error.log", 'w'), level=logging.ERROR).start()

    def parse(self, response):
        log.msg("Parsing content from url "+ response.url)
        hxs = HtmlXPathSelector(response)
        total_products_lst = hxs.xpath('//*[@id="section"]/div/div[1]/h2/span/text()').extract()
        if(len(total_products_lst)>0):
            total_products_size = total_products_lst[0]
            total_products_number= int(total_products_size.replace('(',"").replace(')',"").replace('Products',"").strip())
            log.msg("Total number of products in this category url {}  is  {}".format(response.url,total_products_number))










