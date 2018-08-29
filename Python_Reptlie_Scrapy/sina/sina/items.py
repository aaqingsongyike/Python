# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SinaItem(scrapy.Item):

    # 大类的标题和url
    parentTitle = scrapy.Field()
    parentUrl = scrapy.Field()

    # 小类的标题和url
    subTitle = scrapy.Field()
    subUrl = scrapy.Field()

    # 小类的保存目录
    subFilename = scrapy.Field()

    # 小类下的子链接
    sonUrl = scrapy.Field()

    # 文章标题和内容
    time = scrapy.Field()
    img = scrapy.Field()
    imgName = scrapy.Field()
    imgFilename = scrapy.Field()

    head = scrapy.Field()
    content = scrapy.Field()
















