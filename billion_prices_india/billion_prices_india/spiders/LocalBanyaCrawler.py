import logging

from scrapy.log import ScrapyFileLogObserver
from scrapy import log
import scrapy
from scrapy.selector import HtmlXPathSelector, Selector


__author__ = 'satish'


class LocalBanyaCrawler(scrapy.Spider):
    name = "localbanya"
    allowed_domains = ["localbanya.com"]
    start_urls = ["http://www.localbanya.com/products/Grocery-&-Staples/Oil-&-Ghee/177/32"]
    category = ""

    def __init__(self, *args, **kwargs):
        ScrapyFileLogObserver(open("spider.log", "w"), level=logging.INFO).start()
        ScrapyFileLogObserver(open("spider_error.log", "w"), level=logging.ERROR).start()


    def parse(self, response):
        sel = Selector(response)
        atags = sel.xpath('//*[@id="second"]/div/a')
        for link in atags:
            product_names = link.xpath('div[4]/div[1]/text()').extract()
            for product_name in product_names:
                print product_name












