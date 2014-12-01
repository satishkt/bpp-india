__author__ = 'satish'

from scrapy.contrib.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.contrib.spiders import Rule
from billion_prices_india.spiders.lb.LocalBanya2Crawler import LocalBanya2Crawler


class LbColdDriedFruits(LocalBanya2Crawler):
    name = "lb_colddriedfruits"
    start_urls = ['http://www.localbanya.com/products/Fruits-&-Vegetables/Cold-Dried-Fruits/180/234']
    rules = (
        Rule(LxmlLinkExtractor(allow='product-details/Fruits---Vegetables/Cold-Dried-Fruits'), callback='parse_product',
             follow=True),
    )

