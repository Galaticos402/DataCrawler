# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import pymongo
class BccCrawlerPipeline:
    def process_item(self, item, spider):
        return item
class MongoDbPipeline:
    def __init__(self):
        connection = pymongo.MongoClient(
           'localhost',
            27017
        )
        db = connection["crawler_sample"]
        self.collection = db["news"]
    def process_item(self, item, spider):
        self.collection.insert_one(dict(item))
        return item