from billion_prices_india.spiders.lb.LocalBanya2Crawler import LocalBanya2Crawler

__author__ = 'satish'

from scrapy.contrib.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.contrib.spiders import Rule


class LbFruitsVegetables(LocalBanya2Crawler):
    name = "lb_fruitsvegetables"
    start_urls = ['http://www.localbanya.com/products/Fruits-&-Vegetables/Vegetables-/180/57']
    rules = (
        Rule(LxmlLinkExtractor(allow='product-details/Fruits---Vegetables/'), callback='parse_product', follow=True),
    )


'''
    def __init__(self):
        LocalBanya2Crawler.__init__(self)
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*chrome", "http://www.localbanya.com/products/Fruits-&-Vegetables/Vegetables-/180/57")
        self.selenium.start()

    def __del__(self):
        self.selenium.stop()
        print self.verificationErrors
        LocalBanya2Crawler.__del__(self)

'''

