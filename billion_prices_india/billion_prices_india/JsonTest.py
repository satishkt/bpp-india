__author__ = 'satish'


import json
import uuid
with open('/Users/satish/test_sample.json') as f:
    for line in f:
        decoded = json.loads(line)
        print json.dumps(decoded, sort_keys=True, indent=4)
        print decoded['category']
        print decoded['product']
        print uuid.uuid4()



