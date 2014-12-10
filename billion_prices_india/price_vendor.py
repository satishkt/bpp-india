__author__ = 'mandeepa'


from mrjob.job import MRJob
import re
import sys
class MRPriceAnalysis(MRJob):


    def init_get_pprices(self):
        self.pp = {}

    def get_prices(self, _, line):

        record=line.split(",")
        if not len(record) is 6:
             return
        category,product,vendor,date,unitprice,quantity=record
        if product not in self.pp.keys():
                self.pp[product]=[(vendor,unitprice)]
        elif [vendor,unitprice] not in self.pp[product]:
            self.pp[product].append([vendor,unitprice])


    def final_get_prices(self):
        for product, val in self.pp.iteritems():
            _price=sys.float_info.max
            _store=""
            for store,price in val:
                if store!='' and price!='':
                    if price[-1]=="L":
                        price=float(price[:-1])*100000
                    else:
                        price=float(price)
                    if price < _price:
                        _price=price
                        _store=store
            if store!='' and price!='':
                yield (product, (_store,_price))


    def steps(self):
        return [self.mr(mapper_init=self.init_get_pprices,
                        mapper=self.get_prices,
                        mapper_final=self.final_get_prices
                        )]


if __name__ == '__main__':
    MRPriceAnalysis.run()


