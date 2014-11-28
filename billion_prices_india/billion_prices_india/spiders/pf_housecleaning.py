from scrapy.contrib.loader import ItemLoader

__author__ = 'satish'

import time
import logging
import scrapy
from scrapy.selector import HtmlXPathSelector
from scrapy.log import ScrapyFileLogObserver
from scrapy import log
import locale
from scrapy.http import Request

from billion_prices_india.items import BillionPricesIndiaItem


class PepperFry(scrapy.Spider):
    """Scrape pet supplies tab from pepper fry"""
    name = "pf_housecleaning"
    start_urls = ['http://www.pepperfry.com/laundry-housekeeping-cleaning-%s.html' % s for s in
                  ['products-chemicals-polishes', 'products-waste-dust-bins', 'brushes-cloths', 'brooms-mops']]

    allowed_domains = ["pepperfry.com"]
    AUTOTHROTTLE_ENABLED = True
    AUTOTHROTTLE_DEBUG = True
    DOWNLOAD_DELAY = 3
    DOWNLOAD_TIMEOUT = 30
    AUTOTHROTTLE_START_DELAY = 3
    crawledURL = []
    detailedCrawled = []
    crawledPageUrls = []


    def __init__(self, *args, **kwargs):
        locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
        ScrapyFileLogObserver(open("spider.log", 'w'), level=logging.INFO).start()
        ScrapyFileLogObserver(open("spider_error.log", 'w'), level=logging.ERROR).start()

    def parse(self, response):
        log.msg(response.url)
        urls = []
        hxs = HtmlXPathSelector(response)

        # Look for category count total.
        tot_cat_count_list = hxs.xpath('//input[@id="total_category_content_count"]/@value').extract()

        if (len(tot_cat_count_list) != 0):
            tot_cat_count = int(tot_cat_count_list[0])
            log.msg("Total Category Count is {}".format(tot_cat_count))
            # log.msg("Total category count for" + response.url + " is " + tot_cat_count)
            if (tot_cat_count > 60):
                page_link = response.url + "?p=1"
                log.msg("Crawl " + page_link)
                yield scrapy.Request(page_link, callback=self.pagescrape)
                self.crawledPageUrls.append(page_link)
                page_nums = hxs.xpath('//*[@class="paginate pjaxer"]/text()').extract()
                for num in page_nums:
                    if (not num):
                        page_link = response.url + "?p=" + num
                        if page_link not in self.crawledPageUrls:
                            print page_link
                            yield scrapy.Request(page_link, callback=self.pagescrape)
                            self.crawledPageUrls.append(page_link)
            else:
                page_link = response.url + "?p=1"
                log.msg("Crawl " + page_link)
                yield scrapy.Request(page_link, callback=self.pagescrape)
                self.crawledPageUrls.append(page_link)


    def pagescrape(self, response):
        log.msg(("Crawled page " + response.url))
        hxs = HtmlXPathSelector(response)
        prod_urls = hxs.xpath('//*[@class="row"]/div/div/a/@href')
        for url in prod_urls:
            if url not in self.detailedCrawled:
                link = url.extract()
                print link
                yield scrapy.Request(link, callback=self.detail)
                self.detailedCrawled.append(url)


    def detail(self, response):
        log.msg(response.url)
        hxs = HtmlXPathSelector(response)
        product_name = hxs.xpath('//*[@id="vip_content_section"]/div[2]/h1/text()').extract()
        # //*[@id="vip_content_section"]/div[2]/h1
        if (len(product_name) != 0):
            product_name = hxs.xpath('//*[@id="vip_content_section"]/div[2]/h1/text()').extract()[0]
        product_price = hxs.xpath('//*[@id="price-val"]/text()').extract()
        if (len(product_price) != 0):
            product_price = hxs.xpath('//*[@id="price-val"]/text()').extract()[0]
        if (len(product_price) != 0 or product_price != None) and (len(product_name) or product_name != None):
            l = ItemLoader(item=BillionPricesIndiaItem(), response=response)
            l.add_xpath('product_name', '//*[@id="vip_content_section"]/div[2]/h1/text()')
            # l.add_xpath('quantity', '//*[@id="product_detail_view_1"]/div/div[1]/div/text()')
            l.add_xpath('category', '//*[@id="cat_crum"]/@value')
            l.add_xpath('product', '//*[@id="overview_tab"]/div/div/p/text()')
            item = l.load_item()
            item['product_url'] = response.url
            item['price'] = product_price
            item['vendor'] = 'PepperFry'
            item['city'] = 'Mumbai'
            item['state'] = 'Maharashtra'
            item['country'] = 'India'
            item['date'] = str(time.strftime("%d/%m/%Y"))
            return item




    

	
