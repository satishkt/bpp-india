from billion_prices_india.spiders.lb.LocalBanya2Crawler import LocalBanya2Crawler

__author__ = 'satish'

from scrapy.contrib.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.contrib.spiders import Rule


class LbFruits(LocalBanya2Crawler):
    name = "lb_fruits"
    start_urls = ['http://www.localbanya.com/products/Fruits-&-Vegetables/Fruits-/180/54']
    rules = (
        Rule(LxmlLinkExtractor(allow='product-details/Fruits---Vegetables/Fruits-'), callback='parse_product', follow=True),
    )

