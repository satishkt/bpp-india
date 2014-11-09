__author__ = 'satish'
from billion_prices_india.spiders.lb.LocalBanya2Crawler import LocalBanya2Crawler

__author__ = 'satish'

from scrapy.contrib.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.contrib.spiders import Rule


class LbStationery(LocalBanya2Crawler):
    name = "lb_stationery"
    start_urls = ['http://www.localbanya.com/products/Stationery/Paper/221/222']
    rules = (
        Rule(LxmlLinkExtractor(allow='product-details/Stationery/Paper/'), callback='parse_product', follow=True),
    )


