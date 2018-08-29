import urllib.request
import urllib.parse
import re
from lxml import etree

class Spider:
    def __init__(self, url, beginPage, endPage):
        # 初始化页码
        self.url = url
        self.beginPage = beginPage
        self.endPage = endPage
        self.page = 1
        # 爬取开关
        self.switch = True
        self.header = {
            'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 67.0.3396.79Safari / 537.36'
        }

    def loadPage(self, fullurl):
        '''
            下载页面
        '''
        print("2")
        request = urllib.request.Request(url=fullurl, headers=self.header)
        response = urllib.request.urlopen(request)
        # 获取html源码
        html = response.read()
        # 解析HTML文档为HTML_DOM模型
        content = etree.HTML(html)
        print("this is content ")
        print(content)
        print(2.1)
        # 返回成功匹配的列表集合
        #link_list = content.xpath('//div/a/@href')
        link_list = content.xpath('//div[@class="threadlist_detail clearfix"]/div/div/ul/li/div/a/img/@src')
        print(2.2)
        print("this is list")
        print(link_list)
        for link in link_list:
            print(2.3)
            #fulllink = "http://tieba.baidu.com" + link
            self.loadImage(link)

    # 取出帖子里的图片链接
    def loadImage(self, link):
        print(3)
        request = urllib.request.Request(url=link, headers=self.header)
        html = urllib.request.urlopen(request).read()
        print("aaa")
        content = etree.HTML(html)
        #content = etree.parse(html)
        print(content)
        print(3.1)
        # 返回帖子里所有图片链接的列表集合
        link_list = content.xpath('//img[@class="BDE_Image"]/@src')
        for link in link_list:
            self.wirteImage(link)
    # 下载图片（写）
    def wirteImage(self, link):
        '''
            把数据逐个写入文件
        '''
        print("wirteStart")
        request = urllib.request.Request(url=link, headers=self.header)
        image = urllib.request.urlopen(request).read()
        filename = link[-10:]
        with open(filename, 'wb') as f:
            f.write(image)
        print("wirteEnd")

    def tiebaSpider(self):
        '''
            作用：贴吧爬虫调度器，负责组合处理每个页面的url
            url：贴吧url的前部分
            beginPage：起始页
            endPage：结束页
        '''
        print("1")
        beginPage = int(self.beginPage)
        endPage = int(self.endPage)
        for page in range(beginPage, endPage+1):
            pn = (page - 1)*50
            # filename = "第" + str(page) + "页.html"
            fullurl = self.url + "&pn=" + str(pn)
            self.loadPage(fullurl)

def main():
    kw = input("请输入要爬去的贴吧名：")
    beginPage = input("请输入起始页")
    endPage = input("请输入结束页")
    url = "http://tieba.baidu.com/f?"
    key = urllib.parse.urlencode({"kw": kw})
    fullurl = url + key
    spoder = Spider(fullurl, beginPage, endPage)
    spoder.tiebaSpider()


if __name__ == '__main__':
    main()