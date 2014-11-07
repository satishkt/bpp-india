# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Field


class BillionPricesIndiaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    date = Field()
    product = Field()
    product_name = Field()
    quantity = Field()
    category = Field()
    description = Field()
    vendor = Field()
    price = Field()
    store = Field()
    country = Field()
    state = Field()
    city = Field()
    discount = Field()
    weight = Field()
    product_url = Field()



class IOPIndiaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    date = Field()
    product = Field()
    product_name = Field()
    quantity = Field()
    category = Field()
    description = Field()
    vendor = Field()
    price = Field()
    store = Field()
    country = Field()
    state = Field()
    discount = Field()
    weight = Field()
    product_url = Field()



    last_updated = scrapy.Field(serializer=str)