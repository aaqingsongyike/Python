#生成器 能生成想要的列表、值，报存计算每一种元素值的方式，并不会先生成，
# 什么时候用什么时候生成

#列表生成式
a = [x*2 for x in range(10)]
print(a)

#创建生成器————方式一
print("方式一")
b = (x for x in range(10))
print(next(b))

#创建生成器————方式二
#生成斐波拉契数列   eg. 1,1,2,3,5,8,13,21,34,55...
print("方式二")
def createNum():
    print("start")
    a, b = 0, 1
    i = 0
    while i < 5:
        print("---1---")
        yield b      #生成器的标志
        print("---2---")
        a, b = b, a+b
        print("---3---")
        i+=1
    print("stop")
number = createNum()
'''
for num in number:  #调用方式1
    print(num)
'''
#rets = number.__next__()    #调用方式2  等价于 next(number)
rets = next(number)
print(rets)


'''
ret = next(number)#让number这个生成器对象开始执行，如果第一次执行
                  #就从createNum的开始部分执行，否则就从上一次停止的
                  #地方（yield）开始执行
'''
