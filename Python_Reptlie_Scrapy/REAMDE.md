创建一个爬虫项目命令：
    scrapy startproject mySpider
创建爬虫项目代码文件：
    方式一：
        在mySpider/mySpider/items.py文件中创建字段
        在mySpider/mySpider/spiders目录下输入命令：scrapy genspider 文件名(myspider) 域名(itcast.cn)
    方式二：
        在mySpider/mySpider/items.py文件中创建字段
        在mySpider/mySpider/spiders目录下创建爬虫文件
运行
    scrapy crawl 爬虫名字(itcast)
    将数据保存到文件中去：
        scrapy crawl itcast -o itcast.json


mySpider:
    爬虫模板
tencent：
    爬取腾讯工作岗位并保存，实现自动翻页
douyu:
    爬取斗鱼并保存图片模板

CrawlSpider:
    TencentSpider:
        创建项目命令：
                    scarpy startproject TencentSpider
                    scarpy genspider -t crawl 名字(tencent) 域(tencent.com)
        修改链接
            process_link = 'func'
中间件：
    douban：
        添加Mongodb的中间件
