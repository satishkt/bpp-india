__author__ = 'mandeepak'

from BaseBigBasket import PriceSpiderBase
class PriceSpider(PriceSpiderBase):

    name = "bb_grocery_staples"
    start_urls = ['http://bigbasket.com/cl/grocery-staples/?sid=AooQO4SiY2OjMzUxom1kA6FjA6Jhb8I%3D']

