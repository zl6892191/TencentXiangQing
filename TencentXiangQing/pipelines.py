# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from datetime import datetime
from TencentXiangQing.items import TencentxiangqingItem,TencentxiangqingContent

class TencentxiangqingPipeline(object):

    def open_spider(self,spider):
        self.f = open('tencent.json','w')


    def process_item(self, item, spider):
        if isinstance(item,TencentxiangqingItem):
            cont = json.dumps(dict(item))+',\n'
            self.f.write(cont)
        return item

    def close_spider(self,spider):
        self.f.close()


class TencentxiangqingcontentPipeline(object):
    def open_spider(self, spider):
        self.f = open('tencentContent.json', 'w')

    def process_item(self, item, spider):
        if isinstance(item,TencentxiangqingContent):
            cont = json.dumps(dict(item))+',\n'
            self.f.write(cont)
        return item

    def close_spider(self, spider):
        self.f.close()