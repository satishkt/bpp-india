from scrapy.contrib.loader import ItemLoader

__author__ = 'satish'

import time
import logging
import scrapy
from scrapy.selector import HtmlXPathSelector
from scrapy.log import ScrapyFileLogObserver
from scrapy import log

from billion_prices_india.items import BillionPricesIndiaItem


class PepperFry(scrapy.Spider):
    """Scrape pet supplies tab from pepper fry"""
    name = "pf_petsupplies"
    start_urls = ['http://www.pepperfry.com/pet-supplies-%s.html' % s for s in
              ['dogs-food-treats']]
    allowed_domains = ["pepperfry.com"]
    AUTOTHROTTLE_ENABLED = True
    AUTOTHROTTLE_DEBUG = True
    DOWNLOAD_DELAY = 3
    DOWNLOAD_TIMEOUT = 30
    AUTOTHROTTLE_START_DELAY = 3
    crawledURL = []
    detailedCrawled = []


    def __init__(self, *args, **kwargs):
        ScrapyFileLogObserver(open("spider.log", 'w'), level=logging.INFO).start()
        ScrapyFileLogObserver(open("spider_error.log", 'w'), level=logging.ERROR).start()


    def parse(self, response):
        log.msg(response.url)
        urls=[]
        hxs = HtmlXPathSelector(response)

        prod_urls= hxs.xpath('//*[@class="row"]/div[1]/div[1]/a/@href')

        for url in prod_urls:
            if url not in self.detailedCrawled:
                link = url.extract()
                print link
                yield scrapy.Request(link, callback=self.detail)
                self.detailedCrawled.append(url)


    def detail(self, response):
        log.msg(response.url)
        hxs = HtmlXPathSelector(response)
        product_name = hxs.select('//*[@id="vip_content_section"]/div[2]/h1/text()').extract()[0]
        product_price = hxs.select('//*[@id="price-val"]/text()').extract()[0]
        product_category = hxs.select('//*[@id="cat_crum"]/@value').extract()[0]
        if (len(product_price) != 0 or product_price != None) and (len(product_name) or product_name != None):
            l = ItemLoader(item=BillionPricesIndiaItem(), response=response)
            l.add_xpath('product_name', '//*[@id="vip_content_section"]/div[2]/h1/text()')
            #l.add_xpath('quantity', '//*[@id="product_detail_view_1"]/div/div[1]/div/text()')
            l.add_xpath('category', '//*[@id="cat_crum"]/@value')
            l.add_xpath('product', '//*[@id="overview_tab"]/div/div/p/text()')
            item = l.load_item()
            item['product_url'] = response.url
            item['price'] = float(product_price)
            item['vendor'] ='PepperFry'
            item['city'] = 'Mumbai'
            item['state'] = 'Maharashtra'
            item['country'] = 'India'
            item['date']=str(time.strftime("%d/%m/%Y"))

            return item




    

	
