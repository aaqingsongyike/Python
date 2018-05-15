#字典
#info ={键：值，键：值，...}

info = {"name":"杨郁彪", "xuehao":"1110", "age":18}
print("name, num, age: %s,%s,%d"%(info["name"], info["xuehao"], info["age"]))

infos = {"name":"aa轻松一刻", "age":10}
#增
infos["QQ"] = "12345"
print("this is add: %s"%infos)

#删
del infos["QQ"]
print("this is del: %s"%infos)

#改
infos["age"] = 20
print("this is modify: %s"%infos)

#查
print("this is find_1: %s"%infos["name"])
print("this is find_2: %s"%infos.get("name"))

#len字典长度
Len = len(infos)
print("this is len: %d"%Len)

#key 获取key
Key = infos.keys()
print("this is key: %s"%Key)

#get 获取指定key的值（value）
Get = infos.get("name")
print("this is get: %s"%Get)
if "name" in infos.keys():  #判断name是否在字典中
    print("name: %s"%infos['name'])

#value 获取所有的value值
Value = infos.values()
print("this is value: %s"%Value)

#items 将字典封装成元组
Items = infos.items()
print("this is items: %s"%Items)