from billion_prices_india.spiders.lb.LocalBanya2Crawler import LocalBanya2Crawler

__author__ = 'satish'




from scrapy.contrib.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.contrib.spiders import Rule


class LbFruitsVegetables(LocalBanya2Crawler):
    name = "lb_fruitsvegetables"
    rules = (
        Rule(LxmlLinkExtractor(allow='products/'), callback='parse_category', follow=True),
        Rule(LxmlLinkExtractor(allow='product-details/Fruits---Vegetables'), callback='parse_product', follow=True),
    )

