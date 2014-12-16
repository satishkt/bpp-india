from mrjob.job import MRJob
import re
import sys


__author__ = 'satish'

class ProductID(MRJob):

    def init_get_products(self):
        self.pp={}


    def map_product(self,_,line):
        record=line.split(",")
        id,category,product,vendor,price,measure,date,unitprice,quantity=record
        prd_split=product.split(":")
        product_label,product_name = prd_split
        if product_name not in self.pp.keys():
            self.pp[product]=[(id,category,product,vendor,price,measure,date,unitprice,quantity)]
        elif [vendor,unitprice] not in self.pp[product]:
            self.pp[product].append([(id,category,product,vendor,price,measure,date,unitprice,quantity)])

    def reduce_by_product(self):








