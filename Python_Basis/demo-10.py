#列表

#定义一个列表
names = ["wang", "li", "hu", "xu", "deng", "yang"]
names1 = ["a1", "b2", "c3"]
print("this is names: %s"%names)

#列表-----》增
names.append("song")
print("append: %s"%names)
names.insert(0, "魏")
print("insert: %s"%names)
names.extend(names1)    #列表合并   也可用 “+”
print("列表合并extend: %s"%names)

#列表-----》删
names.pop()             #删除末尾元素
print("pop: %s"%names)
names.remove("song")    #删除指定内容
print("remove: %s"%names)
del names[0]            #删除指定下标
print("del: %s"%names)

#列表-----》查
if "yang" in names:     #判断xxx在列表中
    print("yang在列表中")
else:
    print("yang不在列表中")
if "gao" not in names:  #判断xxx不在列表中
    print("gao 不在列表中")
else:
    print("gao在列表中")

#列表-----》改
names[0] = "王茂"
print("改：%s"%names)
