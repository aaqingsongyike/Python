# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

# 存储数据
class ItcastItem(scrapy.Item):
    # define the fields for your item here like:
    # 创建字段
    name = scrapy.Field()   # 姓名
    title = scrapy.Field()  # 职称
    info = scrapy.Field()   # 简介
