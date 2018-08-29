import urllib.request

# User-Agent 爬虫和反爬虫的第一步,是服务器误认为是浏览器访问该网站
ua_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
}

# 通过urllib.reqquest.Request() 方法构造一个请求对象
request = urllib.request.Request("http://www.baidu.com", headers=ua_headers)

# 向指定的url地址发送请求，并返回服务器响应的类文件对象
response = urllib.request.urlopen(request)

# 服务器返回的类文件对象支持Python文件对象的操作方法
# read()读取文件中的全部内容，放回字符串
html = response.read()
# 打印响应内容
print(html)

# 返回http的响应码 200表示正常，4服务器页面出错，5服务器问题
# 用于判断是否请求成功
print(response.getcode())

# 返回实际数据的URL防止重定向
print(response.geturl())

# 返回http响应的报头
print(response.info())