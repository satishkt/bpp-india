from scrapy.contrib.loader import ItemLoader
from billion_prices_india.items import BillionPricesIndiaItem

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
        log.msg("Parsing content from url " + response.url)
        hxs = HtmlXPathSelector(response)
        subcat_links = hxs.xpath('//*[@id="url"]/@href')
        subcat_names = hxs.xpath('//*[@id="url"]/text()')
        for link, name in zip(subcat_links, subcat_names):
            print link.extract(), name.extract()
            print "Run Crawler for category " + name.extract()
            yield scrapy.Request(link.extract(), callback=self.detail_scrape)


    def detail_scrape(self, response):
        hxs = HtmlXPathSelector(response)
        total_products_lst = hxs.xpath('//*[@id="section"]/div/div[1]/h2/span/text()').extract()
        if (len(total_products_lst) > 0):
            total_products_size = total_products_lst[0]
            total_products_number = int(
                total_products_size.replace('(', "").replace(')', "").replace('Products', "").strip())
            log.msg(
                "Total number of products in this category url {}  is  {}".format(response.url, total_products_number))
            categ_id = (response.url).rsplit('/', 1)[1]
            self.parse_products(response)

    def parse_products(self, response):
        hxs = HtmlXPathSelector(response)
        product_containers = hxs.xpath('//*[@class="product-container floatL"]')
        for product in product_containers.xpath('..//div/a'):
            l = ItemLoader(item=BillionPricesIndiaItem(), response=response)
            item = l.load_item()
            item['product_url'] = product.xpath('@href').extract()[0]
            item['product_name'] = product.xpath('.//*[@class=""]/text()').extract()[0]
            item['price'] = product.xpath('div[3]/div[2]/div[1]/text()').extract()[0]
            item['quantity'] = product.xpath('div[3]/div[1]/span[1]/text()').extract()[0]
            item['vendor'] = 'LocalBanya'
            item['city'] = 'Mumbai'
            item['state'] = 'Maharashtra'
            item['country'] = 'India'
            item['date'] = str(time.strftime("%d/%m/%Y"))
            print item
            return item

#
#             if(total_products_number  20):
#                 left_products=total_products_number
#                 load_pg_url = 'http://www.localbanya.com/home/next_page?task=products&subcat_id={}&start={}&total={}&sort='
#                 increment=20
#                 while left_products > 0:
#                     sub_url = load_pg_url.format(categ_id,increment,total_products_number)
#                     yield scrapy.Request(sub_url,callback= self.scrape_using_bs)
#                     increment=increment+20
#                     left_products=total_products_number-increment
#                     #http://www.localbanya.com/home/next_page?task=products&subcat_id=32&start=20&total=64&sort=
#
# //*[@id="second"]/div/a/div[2]

