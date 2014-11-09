__author__ = 'satish'

from scrapy.contrib.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.contrib.spiders import Rule
from billion_prices_india.spiders.lb.LocalBanya2Crawler import LocalBanya2Crawler



class LbFruits(LocalBanya2Crawler):
    name = "lb_exoticfruitsveg"
    start_urls = ['http://www.localbanya.com/products/Fruits-&-Vegetables/Exotic-Fruits-&-Vegetables/180/55']
    rules = (
        Rule(LxmlLinkExtractor(allow='product-details/Fruits---Vegetables/Fruits-'), callback='parse_product', follow=True),
    )
