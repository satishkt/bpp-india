__author__ = 'mandeepak'

from pymongo import MongoClient
from bson.son import SON

client = MongoClient("54.148.179.83", 27017)
db = client.scrapy
coll = db['bpp_india']
print(coll.count())

print(db.bpp_india.aggregate([
    {"$group": {"_id":{"category":"$category","date":"$date"},"total": { "$avg": "$unitprice" }}}
] ))
