# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
from scrapy.utils.project import get_project_settings
from .settings import IMAGES_STORE
import scrapy
import os


class SinaPipeline(ImagesPipeline):

    def process_item(self, item, spider):
        # 保存内容
        print("#"*20)
        filename = open((item['subFilename'] + item['subTitle'] + '.txt'), 'w')
        filename.write(item['content'])
        return item
'''
    # 保存图片
    # 获取settin.py文件设置的变量值
    IMAGES_STORE = get_project_settings().get("IMAGES_STORE")
    # 获取图片链接，并发送图片的请求
    def get_media_request(self, item, info):
        img_url = item['img']
        yield scrapy.Request(img_url)

    def item_completed(self, results, item, info):
        image_path = [x["path"] for ok, x in results if ok]
        # os.rename(self.IMAGES_STORE + "/" + image_path[0], self.IMAGES_STORE + "/" + item["nickname"] + ".jpg")
        os.rename(item['imgFilename'], item['imgFilename']+"/"+item['img']+".jpg")
        #os.rename(self.IMAGES_STORE + "/" + image_path[0], self.IMAGES_STORE + "/" + item["img"] + ".jpg")
        #item["imagepath"] = self.IMAGES_STORE + "/" + item["img"]
        return item
'''