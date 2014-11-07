__author__ = 'mandeepak'

__author__ = 'mandeepak'

import re

from scrapy.contrib.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.contrib.loader import XPathItemLoader
from scrapy.log import ScrapyFileLogObserver
import scrapy
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

    name = "iocl_petrolprices"
    allowed_domains = ["iocl.com"]
    start_urls = ['http://www.iocl.com/Products/PetrolDomesticPrices.aspx']
    crawledURL = []
    detailedCrawled = []

    def __init__(self, *args, **kwargs):
        ScrapyFileLogObserver(open("spider.log", 'w'), level=logging.INFO).start()
        ScrapyFileLogObserver(open("spider_error.log", 'w'), level=logging.ERROR).start()


    def __getHostURL(self,url):
        parsed_uri = urlparse(url)
        domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
        return domain

    def __group_iter(self,iterator, n=2):
        """ Given an iterator, it returns sub-lists made of n items
        (except the last that can have len < n)
        inspired by http://countergram.com/python-group-iterator-list-function"""
        accumulator = []
        for item in iterator:
            accumulator.append(item)
            if len(accumulator) == n: # tested as fast as separate counter
                yield accumulator
                accumulator = [] # tested faster than accumulator[:] = []
                # and tested as fast as re-using one list object
        if len(accumulator) != 0:
            yield accumulator

    def parse(self, response):
        log.msg(response.url)
        hxs = HtmlXPathSelector(response)
        items=[]
        variants_date=hxs.select("//span[@class='normal']//text()").extract()
        variants_price=hxs.select("//table[@id='objContPreviousPrices_grdPreviousPrices']//tr//td[@class='normal']//text()").extract()

        price_items=self.__group_iter(variants_price,4)
        av_price=[]
        for price_list in price_items:
             av_price.append(reduce(lambda x, y: float(x) + float(y) / float(len(price_list)), price_list, 0))
        for price, date in zip(variants_price, variants_date):
            item = BillionPricesIndiaItem()
            item['date'] = date
            item['vendor'] = "ioc"
            item['product'] = "gasoline"
            item['category'] = "oil and gas"
            item['price'] = price
            items.append(item)
        return items

if __name__ == '__main__':
	obj=PriceSpider()

