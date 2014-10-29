__author__ = 'mandeepak'

import re

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

class PriceSpider(scrapy.Spider):
    name = "pricedekho"
    allowed_domains = ["bigbasket.com"]
    start_urls = ['http://bigbasket.com/cl/%s/?sid=uGJsxoSiY2OjMzgxom1kA6FjA6Jhb8I=#' %s for s in ['grocery-staples','fruits-vegetables']]
    category=""
    def __init__(self, *args, **kwargs):
        ScrapyFileLogObserver(open("spider.log", 'w'), level=logging.INFO).start()
        ScrapyFileLogObserver(open("spider_error.log", 'w'), level=logging.ERROR).start()


    def parse(self, response):
        allpages=['#!page=1']
        log.msg(response.url)
        for pageno in response.xpath('//a[@class="num uiv2-pagination-link"]/@href').extract():
            if pageno not in allpages:
                allpages.append(pageno.strip())

        for pageno in allpages:
            page_url=response.url+pageno
            self.category=page_url.split("/")[4]
            yield scrapy.Request(page_url, callback=self.search,
                cookies={'_bb_vid':'"MzEzMTU5NTAwMg=="'}
                )

    def search(self,response):
        for url in response.xpath('//div[@class="uiv2-list-box-img-block"]/a/@href').extract():
            parsed_uri = urlparse(response.url)
            domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
            page_url=domain+url[1:]
            log.msg('yield process, url:' + page_url)
            yield scrapy.Request(page_url, callback=self.detail,
            cookies={'_bb_vid':'"MzEzMTU5NTAwMg=="'}
            )

    def detail(self, response):
        log.msg(response.url)
        productTitle=response.url.split("/")[-2]
        hxs = HtmlXPathSelector(response)
        variants=hxs.select("//div[@class='uiv2-size-variants']/label/text()").extract()
        items = []
        for variant in variants:
            quantity=variant.split('-')[0].strip()
            price=re.findall(r'\d+\.?\d*',variant)
            item = BillionPricesIndiaItem()
            item['product'] = productTitle
            item['category'] = self.category
            item['quantity'] = quantity
            if len(price)==1:
                item['price']=price[0]
            else:
                item['price']=price[1]
            items.append(item)
        return items

if __name__ == '__main__':
	obj=PriceSpider()
