__author__ = 'satish'

from mrjob.job import MRJob
import re
import sys
import uuid
import json


class SemicolonValueProtocol(object):
    # don't need to implement read() since we aren't using it

    def write(self, key, values):
        return ','.join(str(v) for v in values)


class MRPoductURL(MRJob):
    OUTPUT_PROTOCOL = SemicolonValueProtocol

    def init_get_pprices(self):
        self.pp = {}


    def map_by_product(self, _, line):
        decoded = json.loads(line)
        if decoded['vendor'] == 'PepperFry' and 'product_name' not in decoded:
            yield decoded['product_url'], (decoded['vendor'],decoded['price'])


    def reduce_by_product(self, product_url, values):
        product_id = uuid.uuid4()
        for val in values:
            x =','.join(str(v) for v in val)
            yield product_url,(product_url,product_id,x)
        #yield product, (product,product_id, values)


    def steps(self):
        return [
            self.mr(mapper=self.map_by_product,reducer=self.reduce_by_product)
        ]


if __name__ == '__main__':
    MRPoductURL.run()

