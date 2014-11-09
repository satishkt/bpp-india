from scrapy.contrib.loader import ItemLoader
from scrapy.contrib.spiders import CrawlSpider
from scrapy.selector import Selector
import time

from billion_prices_india.items import BillionPricesIndiaItem


__author__ = 'satish'


class LocalBanya2Crawler(CrawlSpider):
    name = "localbanya2"
    response_url = ""
    allowed_domains = ["localbanya.com"]
    category = ""

    def parse_category(self, response):
        self.response_url = response.url
        print self.response_url

    def parse_product(self, response):
        product_url = response.url
       # sel = self.selenium
        #sel.open(response.url)
        #time.sleep(2.5)


        selector = Selector(response)

        # //*[@id="product_detail_view_1"]/div/div[6]/div[2]/span[2]
        price = selector.xpath('//*[@id="product_detail_view_1"]/div/div[7]/div[2]/span[2]/text()').extract()
        if not price:
            price = selector.xpath('//*[@id="product_detail_view_1"]/div/div[6]/div[2]/span[2]/text()').extract()
        if not price:
            price = selector.xpath(
                '//*[@id="product_detail_view_1"]/div/div[5]/div[2]/span[2]/text()').extract()
        if not price:
            price = selector.xpath(
                '//*[@id="product_detail_view_1"]/div/div[4]/div[2]/span[2]/text()').extract()




        l = ItemLoader(item=BillionPricesIndiaItem(), response=response)
        l.add_xpath('product_name', '//*[@id="inner"]/div[1]/div[1]/div/div/text()')
        l.add_xpath('quantity', '//*[@id="product_detail_view_1"]/div/div[1]/div/text()')
        l.add_xpath('category', '//*[@id="inner"]/div[1]/div[1]/div/a[1]/text()')
        l.add_xpath('product', '//*[@id="inner"]/div[1]/div[1]/div/a[2]/text()')
        item = l.load_item()
        item['product_url'] = product_url
        item['price'] = price
        item['vendor'] ='Local Banya'
        item['city'] = 'Mumbai'
        item['state'] = 'Maharashtra'
        item['country'] = 'India'


        return item
