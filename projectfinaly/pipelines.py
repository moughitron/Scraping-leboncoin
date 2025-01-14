# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from pymongo import MongoClient
import pymongo


class MongoDBPipeline(object):


    def __init__(self):
        connection = pymongo.MongoClient(
            'localhost',
            27017
        )
        db = connection['leboncoin']
        self.collection = db['Leboncoin_db_cleaned']



    def process_item(self, item, spider):    
        self.collection.insert(dict(item))
        return item