# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

from scrapy.item import Field

class BppWpiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    date = Field()
    zone = Field()
    center = Field()
    commodity = Field()
    price = Field()
    last_updated = scrapy.Field(serializer=str)
