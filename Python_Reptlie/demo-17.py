import pyximport
pyximport.install()
import threading    # 线程库
import urllib.request
import json # json处理
from queue import Queue # 队列库
from lxml import etree # 解析库


class ThreadCrawl(threading.Thread):
    def __init__(self, threadName, pageQueue, dataQueue):
        # 调用父类初始化方法
        # threading.Thread.__init__(self)   #适合单继承
        super(ThreadCrawl, self).__init__() #适合多继承
        self.threadName = threadName    # 线程名
        self.pageQueue = pageQueue      # 页码队列
        self.dataQueue = dataQueue      # 数据队列
        self.headers = {
            "User-Agent": "Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 55.0.2883.87Safari / 537.36"
        }
    def run(self):
        print("启动" + self.threadName)
        while not CRAWL_EXIT:
            try:
                # 取出队列中的一个数字，先进先出
                # 可选参数block,默认值为True
                # 1.如果队列为空，block为True的话，会进入阻塞状态直到有新的数据
                # 2.如果队列为空，block为False的话，会弹出一个Queue.empty()异常
                page = self.pageQueue.get(False)
                url = "http://www.qiushibaike.com/8hr/page/" + str(page) + "/"
                content = urllib.request.Request(url=url, headers=self.headers)
                self.dataQueue.put(content)
            except:
                pass
            print("结束" + self.threadName)

# 解析类
class ThreadParse(threading.Thread):
    def __init__(self, threadName, dataQueue, filename):
        super(threading.Thread, self).__init__()
        self.threadName = threading
        self.dataQueue = dataQueue
        self.filename = filename
    def run(self):
        while not PARSE_EXIT:
            try:
                html = self.dataQueue.get(False)
                self.parse(html)
            except:
                pass
    def parse(self, html):
        html = etree.HTML(html)
        node_list = html.xpath('//div[contains(@id, "qiushi_tag")]')

        for node in node_list:
            # xpath返回的列表，这个列表就这一个参数，用索引方式取出来，用户名
            username = node.xpath('./div/a/@title')[0]
            # 图片连接
            image = node.xpath('.//div[@class="thumb"]//@src')  # [0]
            # 取出标签下的内容,段子内容
            content = node.xpath('.//div[@class="content"]/span')[0].text
            # 取出标签里包含的内容，点赞
            zan = node.xpath('.//i')[0].text
            # 评论
            comments = node.xpath('.//i')[1].text

            items = {
                "username": username,
                "image": image,
                "content": content,
                "zan": zan,
                "comments": comments
            }

            # with 后面有两个必须执行的操作：__enter__ 和 _exit__
            # 不管里面的操作结果如何，都会执行打开、关闭
            # 打开锁、处理内容、释放锁
            with self.lock:
                # 写入存储的解析后的数据
                self.filename.write(json.dumps(items, ensure_ascii=False).encode("utf-8") + "\n")

CRAWL_EXIT = False  # 采集
PARSE_EXIT = False  # 解析

def main():
    # 页码队里，10表示可以存储10页
    pageQueue = Queue(10)
    # 循环放了1-10的数字
    for i in range(1, 11):
        pageQueue.put(i)

    # 采集结果的数据(每页的html源码)队列，参数为空表示无限制
    dataQueue = Queue()

    filename = open("demo-17.json", "a")

    # 采集线程集合
    crawlList = ["采集线程1号", "采集线程2号", "采集线程3号"]
    # 存储3个采集线程
    threadcrawl = []
    for threadName in crawlList:
        thread = ThreadCrawl(threadName, pageQueue, dataQueue)
        thread.start()
        threadcrawl.append(thread)

    # 3个解析线程的名字
    parseList = ["解析线程1号", "解析线程2号", "解析线程3号"]
    # 存储3个解析线程
    threadparse = []
    for threadName in parseList:
        thread = ThreadParse(threadName, dataQueue, filename)
        thread.start()
        threadparse.append(thread)


    # 等待pageQueue队列为空，也就是等待之前的操作执行完毕
    while not pageQueue.empty():
        pass
    # 如果pageQueue为空，采集线程退出循环
    global CRAWL_EXIT
    CRAWL_EXIT = True
    print("pageQueue为空")

    # 阻塞，退出每个线程
    for thread in threadcrawl:
        thread.join()
        print(1)



if __name__ == "__main__":
    main()