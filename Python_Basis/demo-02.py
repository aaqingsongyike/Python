import random
#print  输出

print('hello world')

age = 22
print("age: %d"%age)    #整数

name = "aa"
print("My name is %s"%name) #字符串

price = 12.3
count = 4
print("this is price %f"%price) #小数
print("this is price %s"%price) #小数
money = price*count
print("this is money %s"%money)

print("="*9)
#随机数生成
print("随机数生成")
num = random.randint(0,10)
print("this is num: %d"%num)