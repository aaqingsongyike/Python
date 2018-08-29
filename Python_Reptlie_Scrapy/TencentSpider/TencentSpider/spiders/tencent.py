# -*- coding: utf-8 -*-
import scrapy
# 导入链接规则匹配类，用来提取符合规则的链接
from scrapy.linkextractors import LinkExtractor
# 导入CrawlSpider类和Rule规则类
from scrapy.spiders import CrawlSpider, Rule
from ..items import TencentItem


class TencentSpider(CrawlSpider):
    name = 'tencent'
    allowed_domains = ['hr.tencent.com']   # 控制爬取范围
    start_urls = ['http://hr.tencent.com/position.php?start=0#a']

    # 匹配链接, 返回对象的列表
    pagelink = LinkExtractor(allow=("start=\d+"))
    # newlink = LinkExtractor(allow=("position.php"))

    # rules规则
    rules = (
        # 处理错误链接
        # Rule(newlink, process_links='func', follow=True),

        # 获取列表中的链接，依次发送请求，并且依次跟进，调用指定回调函数处理
        Rule(pagelink, callback='parse_item', follow=True), # follow表示是否跟进链接（表示爬完这页接着进入这页中的链接爬去）
    )

    # 当服务器给返回错误的链接（反爬虫），就调用该方法
    def func(self, links):
        '''
            修改链接
            links为pagelink匹配到的链接
        :param links:
        :return:
        '''
        # return links
        pass

    # 指定的回调函数
    def parse_item(self, response):
        for each in response.xpath("//tr[@class='even'] | //tr[@class='odd']"):
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

            yield item




    # def positionParse(self):

