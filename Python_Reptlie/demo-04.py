import urllib.request
import urllib.parse # 编码 解码

# urllib.request.urlencode()接收的是一个字典

url = "http://www.baidu.com"

wd = {"wd": "杨郁彪"}

# 编码
# 出现错误 可以在末尾加encode("utf-8)
values = urllib.parse.urlencode(wd)
print(values)

# 解码
devalues = urllib.parse.unquote(values)
print(devalues)

'''
request = urllib.request.Request(url, vaules)
response = urllib.request.urlopen(request)
print(response.read().decode())
'''