import urllib.request
import ssl

# 创建ssl证书
ssl._create_default_https_context = ssl._create_unverified_context

url = "https://www.12306.cn/mormhweb/"

request = urllib.request.Request(url=url)
response = urllib.request.urlopen(request)
print(response.read().decode('utf-8'))
