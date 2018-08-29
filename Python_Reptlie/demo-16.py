# json的解析库，对应于xml
import json
# json的解析语法，对应的xpath
import jsonpath
import urllib.request

url = "http://www.lagou.com/lbs/getAllCitySearchLabels.json"
headers = {
"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
}
request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)
# 取出json文件的内容，格式为字符串
html =response.read().decode('utf-8')
print(html)
# 把json形式的字符串转换为python形式的Unicode字符串
unicodestr = json.loads(html)
# python形式的列表（$..name表示在根下的任意位置的name $表示根，..表示任意位置）
city_list = jsonpath.jsonpath(unicodestr, "$..name")
for item in city_list:
    print(item)

# 将python类型转换为字符串
array = json.dumps(city_list, ensure_ascii=False)
with open('demo-16.json', 'w') as f:
    f.write(array)

