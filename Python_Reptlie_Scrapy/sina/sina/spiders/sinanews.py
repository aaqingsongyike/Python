# -*- coding: utf-8 -*-
import os
import scrapy
from ..items import SinaItem


class SinanewsSpider(scrapy.Spider):

    name = 'sinanews'
    allowed_domains = ['news.sina.com.cn/guide/']

    url = "http://news.sina.com.cn/guide/"

    start_urls = [
        url
    ]

    def parse(self, response):
        # 获取所有的url
        allUrl = response.xpath('//div[@class="article"]//a/@href').extract()
        allTitle = response.xpath('//div[@class="article"]//a/text()').extract()

        # 获取所有大类标题和url
       # parentTitle = response.xpath('//div[@class="clearfix"]/h3/a/text()').extract()
       # parentUrl = response.xpath('//div[@class="clearfix"]/h3/a/@href').extract()

        # 获取所有小类的标题和url
       # subTitle = response.xpath('//div[@class="clearfix"]/ul/li/a/text()').extract()
       # subUrl = response.xpath('//div[@class="clearfix"]/ul/li/a/@href').extract()

        # 爬取所有大类
        for i in range(0, len(allUrl)):
            item = SinaItem()
            # 若是以.com.cn结尾的则表示是parentUrl
            print("#"*10)
            if_belong_pa = allUrl[i].endswith('.com.cn/')
            if if_belong_pa:
                # 存入parent
                item['parentUrl'] = allUrl[i]
                item['parentTitle'] = allTitle[i]
                # 判读是否存在该大类的文件夹
                parentFilename = './Data/' + allTitle[i]
                if (not os.path.exists(parentFilename)):
                    os.makedirs(parentFilename)
            print(parentFilename)
            '''
            # 若不是以.com.cn 和 .shtml结尾，则是subUrl
            if_belong_sub = allUrl[i].endswith('.shtml')
            if (not (if_belong_pa and if_belong_sub)):
                # 存入sub
                item['subUrl'] = allUrl[i]
                item['subTitle'] = allTitle[i]
                # 判断是否存在小类的文件夹
                subFilename = parentFilename + allTitle[i]
                if (not os.path.exists(subFilename)):
                    os.makedirs(subFilename)

'''

            # 判断是否是该大类下的小类


            # 爬取该大类下的小类名和链接



    # 对于返回的小类的url，再进行递归请求
    def second_parse(self, response):
        pass

    # 数据解析方法，获取文章标题和内容
    def detail_parse(self, response):
        pass






















