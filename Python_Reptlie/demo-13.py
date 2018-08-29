import urllib.request
import re

class Spider:
    def __init__(self):
        # 初始化页码
        self.page = 1
        # 爬取开关
        self.switch = True

    def loadPage(self, page):
        '''
            下载页面
        '''
        if page!=1:
            url = 'http://www.neihanx.com/article/'+ 'index_' +str(page)+'.html'
        else:
            url = 'http://www.neihanx.com/article/'
        header = {
            'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 67.0.3396.79Safari / 537.36'
        }
        request = urllib.request.Request(url=url, headers=header)
        response = urllib.request.urlopen(request)
        # 获取html源码
        html = response.read().decode('utf-8')
        # 创建正则表达式对象，匹配每一页的数据方法，re.S表示匹配全文
        pattern = re.compile('<div\sclass="desc">(.*?)</div>', re.S)
        # 将正则匹配对象，应用到html源码字符串里，返回这个页面里的所有数据的列表
       # html = html.decode('utf-8')
        connect_list = pattern.findall(html)

        self.dealPage(connect_list)

    def dealPage(self, connect_list):
        '''
            处理每页数据
            connect_list列表集合
        '''
        for item in connect_list:
            # 将集合中的数据逐个处理
            # 替换
            # item = item.replace("<p>": "").replace("</p>": "")
            self.wirtePage(item)

    def wirtePage(self, item):
        '''
            把数据逐个写入文件
        '''
        with open('duanzi.txt', 'a') as f:
            f.write(item)

    def startWork(self):
        '''
            控制爬虫运行
        '''
        while self.switch:
            comment = input("如果继续爬取按回车，否则输入quit")
            if comment == 'quit':
                print("谢谢使用")
                self.switch = False
            self.page += 1
            self.loadPage(self.page)


if __name__ == '__main__':
    duanzjSpider = Spider()
    duanzjSpider.startWork()