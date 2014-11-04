from scrapy.contrib.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.contrib.loader import XPathItemLoader
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from billion_prices_india.items import BillionPricesIndiaItem

__author__ = 'satish'


class LocalBanya2Crawler(CrawlSpider):
    name = "localbanya2"
    response_url = ""
    allowed_domains = ["localbanya.com"]
    start_urls = ["http://www.localbanya.com"]
    category = ""

    rules = (
        Rule(LxmlLinkExtractor(allow='products/'), callback='parse_category', follow=True),
        Rule(LxmlLinkExtractor(allow='product-details/Fruits---Vegetables'), callback='parse_product', follow=True),
        Rule(LxmlLinkExtractor(allow='product-details/Personal-Care'),callback= 'parse_product',follow= True),
    )

    def parse_category(self, response):
        self.response_url = response.url
        print self.response_url

    def parse_product(self,response):
        product_url = response.url
        print product_url
        l = XPathItemLoader(item = BillionPricesIndiaItem(),response=response)
        l.add_xpath('product_name','//*[@id="inner"]/div[1]/div[1]/div/div/text()')
        l.add_xpath('price','//*[@id="product_detail_view_1"]/div/div[7]/div[2]/span[2]/text()')
        l.add_xpath('quantity','//*[@id="product_detail_view_1"]/div/div[1]/div/text()')
        l.add_xpath('category','//*[@id="inner"]/div[1]/div[1]/div/a[1]/text()')
        l.add_xpath('product','//*[@id="inner"]/div[1]/div[1]/div/a[2]/text()')
        i = l.load_item()
        return i
