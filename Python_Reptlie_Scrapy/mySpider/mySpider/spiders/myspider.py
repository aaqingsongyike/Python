# -*- coding: utf-8 -*-
import scrapy
from ..items import ItcastItem


# 创建一个爬虫类
class ItcastSpider(scrapy.Spider):
    name = 'itcast'   # 爬虫名字
    allowed_domains = ['http://www.itcast.cn'] # 创建域（运行爬虫作用的范围）
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml#']    # 爬虫起始的url

    def parse(self, response):
        # 保存页面
        #with open('mySpider.html', 'wb') as f:
        #    f.write(response.body)

        # 通过scrapy自带的xpath匹配根节点
        teacher_list = response.xpath('//div[@class="li_txt"]')
        # 信息集合
        # teacherItem = []
        # 用来保存数据
        item = ItcastItem()

        # 遍历根节点的列表集合
        for each in teacher_list:
            # name, extract()将匹配出来的结果转换成UNcode字符串
            name = each.xpath('./h3/text()').extract()
            # title
            title = each.xpath('./h4/text()').extract()
            # info
            info = each.xpath('./p/text()').extract()

            # 存入ItcastItem中
            item['name'] = name[0].encode("utf-8")
            item['title'] = title[0].encode("utf-8")
            item['info'] = info[0].encode("utf-8")

            # 管道取代列表方式
            yield item

            # teacherItem.append(item)

            # 打印
           # print(name[0])
           # print(title[0])
           # print(info[0])
        # return teacherItem