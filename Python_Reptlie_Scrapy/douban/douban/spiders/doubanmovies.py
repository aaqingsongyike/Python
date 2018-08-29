# -*- coding: utf-8 -*-
import scrapy
from ..items import DoubanItem


class DoubanmoviesSpider(scrapy.Spider):
    name = 'doubanmovies'
    allowed_domains = ['movie.douban.com']

    url = "http://movie.douban.com/top250?start="
    offset = 0
    fullurl = url + str(offset)

    start_urls = [
        fullurl,
    ]

    def parse(self, response):
        item = DoubanItem()
        # /div[@class="hd"]/a/span[@class="title"][1]/text()
        for each in response.xpath('//div[@class="info"]'):
            item['title'] = each.xpath('./div[@class="hd"]/a/span[@class="title"][1]/text()').extract()[0]
            item['bd'] = each.xpath('./div[@class="bd"]/p/text()').extract()[0]
            item['star'] = each.xpath('./div[@class="bd"]/div[@class="star"]/span[@class="rating_num"]/text()').extract()[0]
            item['quote'] = each.xpath('./div[@class="bd"]/p[@class="quote"]/span/text()')

            yield item

        if self.offset < 225:
            self.offset += 25
            fullurl = self.url + str(self.offset)
            yield scrapy.Request(fullurl, callback=self.parse)



