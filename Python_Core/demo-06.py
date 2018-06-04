#迭代器

a = [11,22,33,44]

b = iter(a)     #转换为可迭代对象

for temp in b:
    print("for")
    print(temp)

