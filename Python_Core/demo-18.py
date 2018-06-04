#内建方法

#map函数    将可迭代对象变成新的可迭代对象
print("一个参数")
ret = map(lambda x:x*x, [1, 2, 3])  #参数(普通函数或匿名函数, 可迭代对象)
for tmp in ret:
    print(tmp)

print("两个参数")
ret1 = map(lambda x, y:x+y, [1, 2, 3], [4, 5, 6])
for tmp in ret1:
    print(tmp)

print("普通函数")
def f1(x, y):
    return (x, y)
l1 = [0, 1, 2, 3, 4, 5]
l2 = ["a", "b", "c", "d", "e", "f"]
ret2 = map(f1, l1, l2)
print(list(ret2))

print("-"*20)
#filter()   对指定数列进行过滤(True取, False不取)
filt = filter(lambda x:x%2, [1, 2, 3, 4])   #参数(函数， 可迭代对象)
print(list(filt))
filt1 = filter(None, "she")
print(list(filt1))

print("-"*20)
#reduce()   对参数序列中元素进行累积
from functools import reduce
red = reduce(lambda x, y:x+y, [1, 2, 3, 4])
print(red)
red1 = reduce(lambda x,y:x+y, [1,2,3,4], 5) #5给x， 1给y
print(red1)

#错误
#red2 = reduce(lambda x,y:x+y, [1,2,3,4], [1,2])
#print(red2)

red3 = reduce(lambda x,y:x+y, ["a", "b"], "c")
print(red3)

print("-"*20)
#sorted()
print("sort")
a = [1,2, 344, 45, 567, 23, 0, 1, 34]
a.sort()    #对列表排序
print(a)
a.sort(reverse=True)    #倒序排序
print(a)
print("sorted")
b = sorted([1,3,2,5,3])
print(b)
c = sorted([2,3,5,1,6,2], reverse=1)
print(c)
d = sorted(["aa", "vv", "tt", "dd"])
print(d)