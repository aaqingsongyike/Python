# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import jsonpath

# 管道文件
#class MyspiderPipeline(object):
#    def process_item(self, item, spider):
#        return item

class ItcastPipeline(object):
    # 初始化(可选)
    def __init__(self):
        self.filename = open("teacher.json", "w")



    # 必须写该方法(处理数据)
    def process_item(self, item, spider):   # 参数（item指数据，spider指爬虫名）
        # 将数据转换成json格式
        item = dict(item)
        key = item.keys()
        for i in key:
            value = item.get(i).decode("utf-8")
            # 改
            item[i] = value
        jsontext =json.dumps(item, ensure_ascii=False) + "\n"
        self.filename.write(jsontext)
        return item

    # 结束时调用(可选)
    def close_spider(self, spider):
        self.filename.close()

























