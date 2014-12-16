__author__ = 'mandeepa'


from mrjob.job import MRJob
import re
import sys
import operator
from mrjob.protocol import JSONValueProtocol

class MRPriceAnalysis(MRJob):

    OUTPUT_PROTOCOL = JSONValueProtocol
    count=0
    def init_get_pprices(self):
        self.pp = {}

    def get_prices(self, _, line):

        record=line.split(",")
        if not len(record) is 6:
             return
        category,product,vendor,date,unitprice,quantity=record
        self.count+=1
        if self.count!=1:
            product=product[1:-1:].strip()
            date=date[1:-1:].strip()
            vendor=vendor[1:-1:].strip()
            if product!='' and vendor!='PepperFry':
                if unitprice!='':
                    if unitprice[-1]=="L":
                        unitprice=float(unitprice[:-1])*100000
                    else:
                        unitprice=float(unitprice)
                else:
                    unitprice=0.0
                if product not in self.pp.keys():
                    self.pp[product]=[[vendor,unitprice]]
                elif [vendor,unitprice] not in self.pp[product]:
                    self.pp[product].append([vendor,unitprice])


    def sorted_get_prices(self):
        for product, val in self.pp.iteritems():
            flatVal=reduce(lambda x,y: x+y,val)
            output={}
            for store,price in val:
                output.update({store:price})
            sorted_output = sorted(output.items(), key=operator.itemgetter(1))
            flat_sortedOutput=reduce(lambda x,y: x+y,sorted_output)
            yield None,{'storesLtoH':flat_sortedOutput,'product':product}




    def steps(self):
        return [self.mr(mapper_init=self.init_get_pprices,
                        mapper=self.get_prices,
                        mapper_final=self.sorted_get_prices

                        )]


if __name__ == '__main__':
    MRPriceAnalysis.run()


