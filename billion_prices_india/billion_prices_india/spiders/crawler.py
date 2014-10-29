__author__ = 'mandeepak'

import re

import scrapy
from scrapy.selector import HtmlXPathSelector
from scrapy import log
from billion_prices_india.items import BillionPricesIndiaItem


class PriceSpider(scrapy.Spider):
    name = "pricedekho"
    allowed_domains = ["bigbasket.com"]
    start_urls = ['http://bigbasket.com/cl/fruits-vegetables/?sid=YlbRwYSiY2OjNDg5om1kA6FjA6Jhb8I=#!page=%s' %s for s in "123456"]

    def __init__(self, *args, **kwargs):
        super(PriceSpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        for url in response.xpath('//div[@class="uiv2-list-box-img-block"]/a/@href').extract():
            page_url="http://www."+self.allowed_domains[0]+url
            log.msg('yield process, url:' + page_url)
            yield scrapy.Request(page_url, callback=self.detail,
            cookies={'_bb_vid':'"MzEzMTU5NTAwMg=="'}
            )


    def detail(self, response):
        productTitle=response.url.split("/")[-2]
        hxs = HtmlXPathSelector(response)
        variants=hxs.select("//div[@class='uiv2-size-variants']/label/text()").extract()
        items = []
        for variant in variants:
            quantity=variant.split('-')[0].strip()
            price=re.findall(r'\d+\.?\d*',variant)
            item = BillionPricesIndiaItem()
            item['product'] = productTitle
            item['category'] = 'fruits-vegetables'
            item['quantity'] = quantity
            if len(price)==1:
                item['price']=price[0]
            else:
                item['price']=price[1]
            items.append(item)
        return items

if __name__ == '__main__':
	obj=PriceSpider()
