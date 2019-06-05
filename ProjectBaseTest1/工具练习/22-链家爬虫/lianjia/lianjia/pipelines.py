# -*- coding: utf-8 -*-
from scrapy.conf import settings
import pymongo
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class LianjiaPipeline(object):
    def __init__(self):
        host=settings['MONGODB_HOST']
        port = settings["MONGODB_PORT"]
        dbname = settings["MONGODB_DBNAME"]
        sheetname = settings["MONGODB_SHEETNAME"]
        # 创建 MongoDB 数据库连接
        client=pymongo.MongoClient("mongodb://%s:%s@%s:%s/%s"%('spider_data','spider_data',host,port,dbname))
        db=client[dbname]
        self.collections=db[sheetname]

    def process_item(self, item, spider):
        data=dict(item)
        self.collections.insert_one(data)
        return item
