__author__ = 'mandeepak'
__author__ = 'mandeepak'

import re

from scrapy.log import ScrapyFileLogObserver
import scrapy
from bpp_wpi.spiders.dw_retailprice import PriceSpider
import logging

class PriceSpider(scrapy.Spider):

    name = "dw_retailprice_masoordal"
    allowed_domains = ["dataweave.in"]
    user="mandeepa"
    apikey=""
    startdate=""
    enddate=""
    AUTOTHROTTLE_ENABLED = True
    AUTOTHROTTLE_DEBUG = True
    DOWNLOAD_DELAY = 10
    DOWNLOAD_TIMEOUT = 180
    AUTOTHROTTLE_START_DELAY = 10

    start_urls = ['http://api.dataweave.in/v1/retail_prices_india/findByCityAndCommodity/?api_key=67fbcf2894171449d53099c1d3079956fe0dd8d8&city=%s&commodity=Masoor Dal&start_date=20130101&end_date=20140101&page=1&per_page=1' %city for city in ['CHANDIGARH','DELHI','HISAR','KARNAL','SHIMLA','MANDI','SRINAGAR','JAMMU','AMRITSAR','LUDHIANA','BHATINDA','LUCKNOW','KANPUR','VARANASI','AGRA','DEHRADUN','RAIPUR','AHMEDABAD','RAJKOT','BHOPAL','INDORE','MUMBAI','NAGPUR','JAIPUR','JODHPUR','KOTA','PATNA','BHAGALPUR','RANCHI','BHUBANESHWAR','CUTTACK','GUWAHATI','SAMBALPUR','KOLKATA','SILIGURI','ITANAGAR','SHILLONG','AIZWAL','DIMAPUR','AGARTALA','HYDERABAD','VIJAYWADA','BENGALURU','ERNAKULAM','THIRUCHIRAPALLI']
                 ]
    def __init__(self, *args, **kwargs):
        ScrapyFileLogObserver(open("spider.log", 'w'), level=logging.INFO).start()
        ScrapyFileLogObserver(open("spider_error.log", 'w'), level=logging.ERROR).start()

    p=PriceSpider()
    def parse(self,response):
        return self.p.getItems(response.body)



