__author__ = 'mandeepak'

import re

from scrapy.log import ScrapyFileLogObserver
import scrapy
import json
from scrapy.selector import HtmlXPathSelector
from scrapy import log
from billion_prices_india.items import BillionPricesIndiaItem
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.http import Request
from scrapy import log
from os import path
import os
import urllib
import string
from bs4 import UnicodeDammit
from urlparse import urlparse
import logging
import time

class PriceSpider(scrapy.Spider):

    name = "pc_products"
    allowed_domains = ["pricecheckindia.com"]
    user="mandeepa"
    key="UPIFDOZVNPOVPFSF"
    start_urls = ['http://api.pricecheckindia.com/feed/product/speakers.json?user=%s&key=%s'%(user,key),
                  'http://api.pricecheckindia.com/feed/product/otg.json?user=%s&key=%s'%(user,key),
                  'http://api.pricecheckindia.com/feed/product/projectors.json?user=%s&key=%s'%(user,key),
                  'http://api.pricecheckindia.com/feed/product/refrigerators.json?user=%s&key=%s'%(user,key),
                  'http://api.pricecheckindia.com/feed/product/scanners.json?user=%s&key=%s'%(user,key),
                  'http://api.pricecheckindia.com/feed/product/tablets.json?user=%s&key=%s'%(user,key),
                  'http://api.pricecheckindia.com/feed/product/vacuum_cleaners.json?user=%s&key=%s'%(user,key),
                  'http://api.pricecheckindia.com/feed/product/video_players.json?user=%s&key=%s'%(user,key),
                  'http://api.pricecheckindia.com/feed/product/washing_machines.json?user=%s&key=%s'%(user,key),
                  'http://api.pricecheckindia.com/feed/product/water_purifiers.json?user=%s&key=%s'%(user,key),
                  'http://api.pricecheckindia.com/feed/product/music_systems.json?user=%s&key=%s'%(user,key),
                  'http://api.pricecheckindia.com/feed/product/microwave_ovens.json?user=%s&key=%s'%(user,key),
                  'http://api.pricecheckindia.com/feed/product/home_theaters.json?user=%s&key=%s'%(user,key),
                  'http://api.pricecheckindia.com/feed/product/gaming_consoles.json?user=%s&key=%s'%(user,key),
                  'http://api.pricecheckindia.com/feed/product/dslrs.json?user=%s&key=%s'%(user,key),
                  'http://api.pricecheckindia.com/feed/product/binoculars_telescopes.json?user=%s&key=%s'%(user,key),
                  'http://api.pricecheckindia.com/feed/product/air_conditioners.json?user=%s&key=%s'%(user,key),
                  'http://api.pricecheckindia.com/feed/product/mobile_phones.json?user=%s&key=%s'%(user,key),
                  'http://api.pricecheckindia.com/feed/product/landline_phones.json?user=%s&key=%s'%(user,key),
                  'http://api.pricecheckindia.com/feed/product/mobile_bluetooth_headsets.json?user=%s&key=%s'%(user,key),
                  'http://api.pricecheckindia.com/feed/product/mobile_headphone_headsets.json?user=%s&key=%s'%(user,key),
                  'http://api.pricecheckindia.com/feed/product/mobile_batteries.json?user=%s&key=%s'%(user,key),
                  'http://api.pricecheckindia.com/feed/product/mobile_chargers.json?user=%s&key=%s'%(user,key),
                  'http://api.pricecheckindia.com/feed/product/mobile_memory.json?user=%s&key=%s'%(user,key),
                  'http://api.pricecheckindia.com/feed/product/point_shoots.json?user=%s&key=%s'%(user,key),
                  'http://api.pricecheckindia.com/feed/product/camcorders.json?user=%s&key=%s'%(user,key),
                  'http://api.pricecheckindia.com/feed/product/digital_photo_frames.json?user=%s&key=%s'%(user,key),
                  'http://api.pricecheckindia.com/feed/product/desktops.json?user=%s&key=%s'%(user,key),
                  'http://api.pricecheckindia.com/feed/product/laptops.json?user=%s&key=%s'%(user,key),
                  'http://api.pricecheckindia.com/feed/product/monitors.json?user=%s&key=%s'%(user,key),
                  'http://api.pricecheckindia.com/feed/product/printers_single.json?user=%s&key=%s'%(user,key),
                  'http://api.pricecheckindia.com/feed/product/printers_multi.json?user=%s&key=%s'%(user,key),
                  'http://api.pricecheckindia.com/feed/product/lcd_tv.json?user=%s&key=%s'%(user,key),
                  'http://api.pricecheckindia.com/feed/product/led_tv.json?user=%s&key=%s'%(user,key),
                  'http://api.pricecheckindia.com/feed/product/plasma_tv.json?user=%s&key=%s'%(user,key),
                  'http://api.pricecheckindia.com/feed/product/crt_tv.json?user=%s&key=%s'%(user,key),
                  'http://api.pricecheckindia.com/feed/product/home_theaters.json?user=%s&key=%s'%(user,key),
                  'http://api.pricecheckindia.com/feed/product/video_players.json?user=%s&key=%s'%(user,key),
                  'http://api.pricecheckindia.com/feed/product/gaming_consoles.json?user=%s&key=%s'%(user,key),
                  'http://api.pricecheckindia.com/feed/product/ipods.json?user=%s&key=%s'%(user,key),
                  'http://api.pricecheckindia.com/feed/product/mp3_players.json?user=%s&key=%s'%(user,key),
                  'http://api.pricecheckindia.com/feed/product/mp4_players.json?user=%s&key=%s'%(user,key),
                  'http://api.pricecheckindia.com/feed/product/irons.json?user=%s&key=%s'%(user,key),
                  'http://api.pricecheckindia.com/feed/product/induction_cooktops.json?user=%s&key=%s'%(user,key),
                  'http://api.pricecheckindia.com/feed/product/electric_cookers.json?user=%s&key=%s'%(user,key),
                  'http://api.pricecheckindia.com/feed/product/mixer_grinder_juicer.json?user=%s&key=%s'%(user,key),
                  'http://api.pricecheckindia.com/feed/product/hand_blenders.json?user=%s&key=%s'%(user,key),
                  'http://api.pricecheckindia.com/feed/product/food_processors.json?user=%s&key=%s'%(user,key),
                  'http://api.pricecheckindia.com/feed/product/sandwich_makers.json?user=%s&key=%s'%(user,key),
                  'http://api.pricecheckindia.com/feed/product/popup_toasters.json?user=%s&key=%s'%(user,key),
                  'http://api.pricecheckindia.com/feed/product/coffee_makers.json?user=%s&key=%s'%(user,key),
                  'http://api.pricecheckindia.com/feed/product/electric_kettles.json?user=%s&key=%s'%(user,key),
                  'http://api.pricecheckindia.com/feed/product/pen_drives.json?user=%s&key=%s'%(user,key),
                  'http://api.pricecheckindia.com/feed/product/external_hard_disks.json?user=%s&key=%s'%(user,key),
                  'http://api.pricecheckindia.com/feed/product/data_cards.json?user=%s&key=%s'%(user,key),
                  'http://api.pricecheckindia.com/feed/product/routers.json?user=%s&key=%s'%(user,key),
                  'http://api.pricecheckindia.com/feed/product/switches.json?user=%s&key=%s'%(user,key),
                  'http://api.pricecheckindia.com/feed/product/processors.json?user=%s&key=%s'%(user,key),
                  'http://api.pricecheckindia.com/feed/product/graphic_cards.json?user=%s&key=%s'%(user,key),
                  'http://api.pricecheckindia.com/feed/product/rams.json?user=%s&key=%s'%(user,key),
                  'http://api.pricecheckindia.com/feed/product/tv_tuners.json?user=%s&key=%s'%(user,key),
                  'http://api.pricecheckindia.com/feed/product/mouse.json?user=%s&key=%s'%(user,key),
                  'http://api.pricecheckindia.com/feed/product/keyboards.json?user=%s&key=%s'%(user,key),
                  'http://api.pricecheckindia.com/feed/product/webcams.json?user=%s&key=%s'%(user,key),
                  'http://api.pricecheckindia.com/feed/product/laptop_batteries.json?user=%s&key=%s'%(user,key),
                  'http://api.pricecheckindia.com/feed/product/laptop_adapters.json?user=%s&key=%s'%(user,key)


                  ]

    AUTOTHROTTLE_ENABLED = True
    AUTOTHROTTLE_DEBUG = True
    DOWNLOAD_DELAY = 3
    DOWNLOAD_TIMEOUT = 180
    AUTOTHROTTLE_START_DELAY = 3
    category=""

    def __init__(self, *args, **kwargs):
        ScrapyFileLogObserver(open("spider.log", 'w'), level=logging.INFO).start()
        ScrapyFileLogObserver(open("spider_error.log", 'w'), level=logging.ERROR).start()

    def parse(self, response):
        results = json.loads(response.body)
        items=[]
        for result in results['product']:
            item = BillionPricesIndiaItem()
            item['product'] = result['model']
            category=result['section']
            item['category'] = category[0].upper()+category[1:]
            if len(result['stores']) >0:
                for store in result['stores']:
                    price=float(store['price'])
                    item['date']=str(time.strftime("%d/%m/%Y"))
                    item['vendor']=store['website']
                    item['quantity'] = 1
                    item['measure']= 'pcs'
                    item['price']=price
                    item['unitprice']=price
                    items.append(item)
        return items




if __name__ == '__main__':
	obj=PriceSpider()
