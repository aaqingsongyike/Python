#集合

a = "abcdef"
b = set(a)
print("this is b %s"%b)

A = "bfui"
B = set(A)
print("this is B %s"%B)
c = b&B     #交集
print("b和B的交集为: %s"%c)
print("-"*20)

d = b|B     #并集
print("b和B的并集：%s"%d)
print("-"*20)

e = b-B     #差集
print("b和B的差集：%s"%e)
print("-"*20)

f = b^B     #对称差集(除去共有部分)
print("b和B的对称差集：%s"%f)
print("-"*20)