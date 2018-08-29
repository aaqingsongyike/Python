import urllib.request

'''
    构建Handler和Opener
'''
# 构建一个Handler处理器对象，支持处理http请求
http_handler = urllib.request.HTTPHandler()

# 调用build_opener()方法构建一个自定义的opener对象，参数是构建处理器的对象
opener = urllib.request.build_opener(http_handler)

request = urllib.request.Request("http://www.baidu.com")
response = opener.open(request)
print(response.read().decode('utf-8'))

'''
    代理
'''

# 代理开关，表示是否启用代理
proxywitch = True

# 构建一个Handler处理器对象，参数是一个字典类型，包括代理类型和代理服务器IP和端口
httpproxy_handler = urllib.request.ProxyHandler({"http": "183.56.177.130:808"}) # 公用代理
#httpproxy_handler = urllib.request.ProxyHandler({"http": "用户名:密码@183.56.177.130:808"}) # 私密代理
# 构建一个没有代理的处理器对象
nullproxy_handler = urllib.request.ProxyHandler({})

if proxywitch:
    opener = urllib.request.build_opener(http_handler)
else:
    opener = urllib.request.build_opener(nullproxy_handler)

# opener.open() #若只用一次请求可以使用这种方式，否则用下面的方式
# 构建一个全局的opener，之后所有的请求都可以用urlopen()方式去发送，也可附带Handler功能
urllib.request.install_opener(opener=opener)
request = urllib.request.Request("http://www.baidu.com")
response = urllib.request.urlopen(request)
print(response.read().decode('utf-8'))

