# -*- coding: utf-8 -*-
import scrapy
from ..items import TencentItem


class TencentpositionSpider(scrapy.Spider):
    name = 'tencentPosition'
    allowed_domains = ['tencent.com']
    url = "http://hr.tencent.com/position.php?start="
    offset = 0
    start_urls = [url + str(offset)]

    def parse(self, response):
        for each in response.xpath('//tr[@class="even"] | //tr[@class="odd"]'):
            # 初始化模型对象
            item = TencentItem()
            # 职位名称
            item['positionName'] = each.xpath("./td[1]/a/text()").extract()[0]
            # 详情连接
            item['positionLink'] = each.xpath("./td[1]/a/@href").extract()[0]
            # 职位类别
            item['positionType'] = each.xpath("./td[2]/text()").extract()[0]
            # 招聘人数
            item['peopleNum'] = each.xpath("./td[3]/text()").extract()[0]
            # 工作地点
            item['workLocation'] = each.xpath("./td[4]/text()").extract()[0]
            # 发布时间
            item['publishTime'] = each.xpath("./td[5]/text()").extract()[0]

            # 将数据发到管道文件
            yield item

        # scrapy里重新发请求(处理完一页之后重新发请求)
        if self.offset < 1680:
            self.offset += 10
        else:
            # break
            raise("结束工作")
        # 请求处理下一页
        # callback 为回调函数
        yield scrapy.Request(url=(self.url + str(self.offset)), callback=self.parse)

















