import urllib.request, urllib.parse

def loadPage(url, filename):
    '''
        作用：根据url发送请求，获取服务器响应文件
        url：需要爬取url地址
        filename： 处理的文件名
    '''
    print("正在下载" + filename)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
    }
    request = urllib.request.Request(url, headers=headers)
    return urllib.request.urlopen(request).read()

def writePage(html, filename):
    '''
        作用：将html内容写入到本地
        html：服务器响应文件内容
    '''
    print("正在保存" + filename)
    # 文件写入
    with open(filename, "wb") as f:
        f.write(html)
    print("-"*20)

def tiebaSpider(url, beginPage, endPage):
    '''
        作用：贴吧爬虫调度器，负责组合处理u每个页面的url
        url：贴吧的前部分
        beginPage：起始页
        endPage：结束页
    '''
    beginPage = int(beginPage)
    endPage = int(endPage)
    for page in range(beginPage, endPage+1):
        pn = (page - 1) * 50
        filename = "第" + str(page) + "页.html"
        fullurl = url + "&pn=" + str(pn)
        # print(fullurl)
        html = loadPage(fullurl, filename)
        # print(html)
        writePage(html, filename)

if __name__ == '__main__':
    kw = input("请输入要爬取的贴吧名: ")
    beginPage = input("请输入起始页：")
    endPage = input("请输入结束页：")

    # ?kw=%E4%BC%A0%E6%99%BA%E6%92%AD%E5%AE%A2&ie=utf-8&pn=50
    url = "http://tieba.baidu.com/f?"
    key = urllib.parse.urlencode({"kw": kw})
    fullurl = url + key
    tiebaSpider(fullurl, beginPage, endPage)