# ==、is
# == 指值是否相等
# is 指是否指的是同一个东西

a = [1,2,3]
b = [1,2,3]
print(a == b)   #True
print(a is b)   #False
c = a
print(c is a)   #True