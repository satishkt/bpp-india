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
        if unitprice!='':
            if unitprice[-1]=="L":
                unitprice=float(unitprice[:-1])*100000
            else:
                unitprice=float(unitprice)
        else:
            unitprice=0.0
        if product+" "+date not in self.pp.keys():
            self.pp[product+" "+date]=[[vendor,unitprice]]
        elif [vendor,unitprice] not in self.pp[product+" "+date]:
            self.pp[product+" "+date].append([vendor,unitprice])


    def final_get_prices(self):
        for product, val in self.pp.iteritems():
            _flatVal=reduce(lambda x,y: x+y,val)
            if 'flipkart' in _flatVal and 'snapdeal' in _flatVal :
                _flip=_flatVal.count('flipkart')
                _snap=_flatVal.count('snapdeal')
                _prevFlipkart=sys.float_info.max
                _prevSnapdeal=sys.float_info.max
                for store,price in val:
                        if store=="flipkart":
                            _flip=_flip-1
                            if price<_prevFlipkart:
                                _prevFlipkart=price
                            if _flip==0:
                                yield store,_prevFlipkart
                        elif store=="snapdeal":
                            _snap=_snap-1
                            if price<_prevSnapdeal:
                                _prevSnapdeal=price
                            if _snap==0:
                                yield store,_prevSnapdeal

    def average_price(self, store, values):
        values_cnt = list(values)
        count = len(values_cnt)
        total=sum([value for value in values_cnt])
        yield None,{'total':total,'itemcount':count,'average':total/count,'store':store}



    def steps(self):
        return [self.mr(mapper_init=self.init_get_pprices,
                        mapper=self.get_prices,
                        mapper_final=self.final_get_prices,
                        reducer=self.average_price
                        )]


if __name__ == '__main__':
    MRPriceAnalysis.run()


