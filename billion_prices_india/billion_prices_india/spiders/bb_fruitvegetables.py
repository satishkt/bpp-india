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
import time

class PriceSpider(scrapy.Spider):

    name = "fruits_vegetables"
    allowed_domains = ["bigbasket.com"]
    start_urls = ['http://bigbasket.com/cl/fruits-vegetables/?sid=AooQO4SiY2OjMzUxom1kA6FjA6Jhb8I%3D']

    category=""

    def __init__(self, *args, **kwargs):
        ScrapyFileLogObserver(open("spider.log", 'w'), level=logging.INFO).start()
        ScrapyFileLogObserver(open("spider_error.log", 'w'), level=logging.ERROR).start()


    def __getHostURL(self,url):
        parsed_uri = urlparse(url)
        domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)

        return domain

    def parse(self, response):

        baseurl=response.url+"#!page=1"
        response_home=scrapy.Request(baseurl)
        for pageno in range(1,9):
            page_url=response_home.url+"#!page="+str(pageno)

            log.msg("Page URL -"+page_url)
            scrapy.Request(page_url)
            self.category=page_url.split("/")[4]
            yield scrapy.Request(page_url, callback=self.search
                )

    def search(self,response):
        for url in response.xpath('//div[@class="uiv2-list-box-img-block"]/a/@href').extract():
            hostURL=self.__getHostURL(response.url)
            page_url=hostURL+url[1:]
            log.msg(page_url)
            log.msg('yield process, url:' + page_url)
            yield scrapy.Request(page_url, callback=self.detail,
            cookies={'_bb_vid':'"MzEzMTU5NTAwMg=="'}
            )

    def detail(self, response):
        log.msg(response.url)
        productTitle=response.url.split("/")[-2]
        hxs = HtmlXPathSelector(response)
        variants=hxs.select("//div[@class='uiv2-size-variants']/label/text()").extract()
        quantitylist=[]
        pricelist=[]
        if len(variants)!=0 or variants!=None:
            items = []
            for variant in variants:
                quantity=variant.split('-')[0].strip()
                price=re.findall(r'[Rs ]\d+\.?\d*',variant)
                if quantity not in quantitylist or price not in pricelist:
                    item = BillionPricesIndiaItem()
                    quantitylist.append(quantity)
                    item['quantity'] = quantity
                    if len(price)==1:
                        pricelist.append(price)
                        item['price']=price[0]
                    elif len(price)!=1:
                        pricelist.append(price)
                        item['price']=price[1]

                    item['date']=str(time.strftime("%d/%m/%Y"))
                    item['product'] = productTitle
                    item['category'] = self.category
                    items.append(item)
            else:

                price=hxs.select("//div[@class='uiv2-price']/text()").extract()
                quantity=hxs.select("//div[@class='uiv2-field-wrap mt10']/text()").extract()[0].strip()
                item = BillionPricesIndiaItem()
                item['date']=str(time.strftime("%d/%m/%Y"))
                item['product'] = productTitle
                item['category'] = self.category
                item['quantity'] = quantity
                if len(price)==1 and price not in pricelist:
                    item['price']=price[0]
                elif len(price)!=1 and price not in pricelist:
                    item['price']=price[1]
                items.append(item)

        return items

if __name__ == '__main__':
	obj=PriceSpider()
