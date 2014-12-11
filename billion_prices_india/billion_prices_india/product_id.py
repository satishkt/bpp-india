__author__ = 'satish'

from mrjob.job import MRJob
import re
import sys
import uuid
import json


class SemicolonValueProtocol(object):
    # don't need to implement read() since we aren't using it

    def write(self, key, values):
        return ';'.join(str(v) for v in values)


class MRPoductID(MRJob):
    OUTPUT_PROTOCOL = SemicolonValueProtocol

    def init_get_pprices(self):
        self.pp = {}


    def map_by_product(self, _, line):
        decoded = json.loads(line)
        if decoded['vendor'] <> 'PepperFry':
            #print decoded['product'],decoded['vendor']
            yield decoded['product'], (decoded['category'], decoded['product'])
        #else:
            #print decoded
            #print decoded['product_name'][0],decoded['vendor']
            #yield decoded['product_name'][0], (decoded['category'], decoded['product_name'][0])


    def reduce_by_product(self, product, values):
        product_id = uuid.uuid4()
        yield product, (product, product_id)


    def steps(self):
        return [
            self.mr(mapper=self.map_by_product, reducer=self.reduce_by_product)
        ]


if __name__ == '__main__':
    MRPoductID.run()

