__author__ = 'mandeepa'


from mrjob.job import MRJob
import re
import sys
from mrjob.protocol import JSONValueProtocol
class MRPriceAnalysis(MRJob):

    OUTPUT_PROTOCOL = JSONValueProtocol

    def init_get_pprices(self):
        self.pp = {}

    def get_prices(self, _, line):

        record=line.split(",")
        if not len(record) is 6:
             return
        category,product,vendor,date,unitprice,quantity=record
        if product not in self.pp.keys():
                self.pp[product]=[[vendor,unitprice]]
        elif [vendor,unitprice] not in self.pp[product]:
            self.pp[product].append([vendor,unitprice])


    def final_get_prices(self):
        _prevAmazon=sys.float_info.max
        _prevFlipkart=sys.float_info.max
        store="amazon"
        for product, val in self.pp.iteritems():
            _flatVal=reduce(lambda x,y: x+y,val)
            if 'flipkart' and 'amazon' in _flatVal:
                _flip=_flatVal.count('flipkart')
                _ama=_flatVal.count('amazon')
                for store,price in val:
                    if store=='flipkart' or store=='amazon':
                        if price[-1]=="L":
                            price=float(price[:-1])*100000
                        else:
                            price=float(price)
                        if store=='amazon':
                            _ama=_ama-1
                            if price<_prevAmazon:
                                _prevAmazon=price
                            if _ama==0:
                                yield store,_prevAmazon
                        else:
                            _flip=_flip-1
                            if price<_prevFlipkart:
                                _prevFlipkart=price
                            if _flip==0:
                                yield store,_prevFlipkart

    def average_price(self, store, values):
        yield None,{'total_itemprice':sum(values),'store':store}


    def steps(self):
        return [self.mr(mapper_init=self.init_get_pprices,
                        mapper=self.get_prices,
                        mapper_final=self.final_get_prices,
                        reducer=self.average_price
                        )]


if __name__ == '__main__':
    MRPriceAnalysis.run()


