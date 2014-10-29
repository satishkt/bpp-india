# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.contrib.exporter import CsvItemExporter

from billion_prices_india.items import BillionPricesIndiaItem

# os = rawes.Elastic('http://localhost:9200')

# class ElasticSearchPipeline(object):
#     def process_item(self, item, spider):
#         os.post('prices/mobiles/',data=dict(item))
#         return item
#     import json
from scrapy import signals
from scrapy.contrib.exporter import XmlItemExporter

class NaivePipeline(object):
    def process_item(self, item, spider):
        for field in item:
            print field + ': ' + item[field][0]
        return item


class CSVWriterPipeline(object):
    filename=""
    def __init__(self):
        self.files = {}
        self.exporter1 = CsvItemExporter(fields_to_export=BillionPricesIndiaItem.fields.keys(),file=open("mobiles.csv",'wb'))

	@classmethod
	def from_crawler(cls, crawler):
		pipeline = cls()
		crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
		crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
		return pipeline

    def spider_opened(self, spider):
    	self.exporter1.start_exporting()

    def spider_closed(self, spider):
        self.exporter1.finish_exporting()
        file = self.files.pop(spider)
        file.close()

    def process_item(self, item, spider):
        self.exporter1.export_item(item)
        return item


class XmlExportPipeline(object):

    def __init__(self):
        self.files = {}

    @classmethod
    def from_crawler(cls, crawler):
        pipeline = cls()
        crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
        crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
        return pipeline

    def spider_opened(self, spider):
        file = open('%s_products.xml' % spider.name, 'w+b')
        self.files[spider] = file
        self.exporter = XmlItemExporter(file)
        self.exporter.start_exporting()

    def spider_closed(self, spider):
        self.exporter.finish_exporting()
        file = self.files.pop(spider)
        file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item


import json
import codecs

class JsonWithEncodingPipeline(object):

    def __init__(self):
        self.file = codecs.open('data_utf8.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item

    def spider_closed(self, spider):
        self.file.close()
