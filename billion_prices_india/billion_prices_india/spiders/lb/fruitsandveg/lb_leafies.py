__author__ = 'satish'
from scrapy.contrib.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.contrib.spiders import Rule
from billion_prices_india.spiders.lb.LocalBanya2Crawler import LocalBanya2Crawler

class LbLeafies(LocalBanya2Crawler):
    name = "lb_leafies"
    start_urls = ['http://www.localbanya.com/products/Fruits-&-Vegetables/Leafies/180/244']
    rules = (
        Rule(LxmlLinkExtractor(allow='product-details/Fruits---Vegetables/Leafies'), callback='parse_product', follow=True),
    )



