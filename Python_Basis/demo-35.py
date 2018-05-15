#列表生成式
a = [i for i in range(1, 18)]
print(a)

b = [11 for i in range(1, 18)]
print(b)

c = [i for i in range(10) if i%2==0]    #偶数
print(c)

d = [i for i in range(3) for j in range(2)]
print(d)