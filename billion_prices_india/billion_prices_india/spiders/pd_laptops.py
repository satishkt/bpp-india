__author__ = 'mandeepak'
__author__ = 'mandeepak'

from urlparse import urlparse
import logging

from scrapy.log import ScrapyFileLogObserver
import scrapy
from scrapy.selector import HtmlXPathSelector
from scrapy import log

from billion_prices_india.items import BillionPricesIndiaItem
import time


class PriceSpider(scrapy.Spider):

    name = "pd_laptops"
    allowed_domains = ["pricedekho.com"]
    start_urls = ['http://pricedekho.com/laptops/%s+laptops-price-list.html' %s for s in ['samsung','apple','hp','dell','sony']]
    crawledURL = []
    detailedCrawled = []

    def __init__(self, *args, **kwargs):
        ScrapyFileLogObserver(open("spider.log", 'w'), level=logging.INFO).start()
        ScrapyFileLogObserver(open("spider_error.log", 'w'), level=logging.ERROR).start()


    def __getHostURL(self,url):
        parsed_uri = urlparse(url)
        domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
        return domain

    def parse(self, response):
        log.msg(response.url)
        baseurl=self.__getHostURL(response.url)+"laptops/"
        for url in response.xpath('//li[@class="page"]/a/@href').extract():
            if url.split("/")[2] not in self.crawledURL:
                yield scrapy.Request(baseurl + url.split("/")[2], callback=self.search)
                self.crawledURL.append(url)

    def search(self,response):
        log.msg(response.url)
        for url in response.xpath('//li[@class="list_view"]//a/@href').extract():
            if url not in self.detailedCrawled:
                yield scrapy.Request(url, callback=self.detail)
                self.crawledURL.append(url)

    def detail(self, response):
        log.msg(response.url)
        hxs = HtmlXPathSelector(response)
        variants_price=hxs.select("//li[@class='activelist']/@data-price").extract()
        variants_seller=hxs.select("//div[@class='storeimage']/img/@alt").extract()
        quantitylist=[]
        pricelist=[]
        items=[]


        if (len(variants_price)!=0 or variants_price!=None) and (len(variants_seller) or  variants_seller!=None):
            for price, seller in zip(variants_price, variants_seller):
                item = BillionPricesIndiaItem()
                item['date'] = time.strftime("%d/%m/%Y")
                item['vendor'] = seller.split(" ")[-1:][0]
                item['product'] = response.url.split('/')[-1].split(".")[0]
                item['category'] = "laptops"
                item['price'] = price
                items.append(item)
        return items

if __name__ == '__main__':
	obj=PriceSpider()
