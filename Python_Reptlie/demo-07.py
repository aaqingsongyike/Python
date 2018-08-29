import urllib.request, urllib.parse

url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}

formdata = {
    "type": "11",
    "interval_id": "100:90",
    "action": "",
    "start": "20",
    "limit": "20"
}

data = urllib.parse.urlencode(formdata).encode(encoding='UTF8')

request = urllib.request.Request(url, data=data, headers=headers)
response = urllib.request.urlopen(request)
print(response.read().decode('utf-8'))