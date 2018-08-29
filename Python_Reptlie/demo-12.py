import urllib.request
import urllib.parse
import http.cookiejar

# 构建CookieJar()类对象，用来保存Cookie的值
cookie = http.cookiejar.CookieJar()

# 通过HTTPCookieProcessor()处理器类构建一个处理器对象，用来处理cookie
# 参数就是构建的CookieJar()对象
cookie_handler = urllib.request.HTTPCookieProcessor(cookiejar=cookie)

# 构建一个自定义的openner()
openner = urllib.request.build_opener(cookie_handler)

# 添加http报头(添加User-Agent的值就行)
openner.addheaders = [("Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36")]

url = "http://www/renren.com/PLogin.do"

# 需要登录的账户名和密码
data = {"email":"YYBhard", "password": "123456"}
# 转码
data = urllib.parse.urlencode(data)
# 请求
# 第一次post请求，发送登录需要的参数获取cookie
request = urllib.request.Request(url=url, data=data)
# 生成登录后的cookie
response = openner.open(request)
print(response.read())
