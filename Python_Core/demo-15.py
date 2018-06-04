#类装饰器

class Test(object):
    def __init__(self, func):
        print("初始化")
        print("func name is %s"%func.__name__)
        self.__func = func
    def __call__(self):
        print("装饰器的功能")
        self.__func()

#使用Test类对象test函数进行装饰
@Test
def test():
    print("---test---")

#调用__call__方法
test()  #test()指 test = Test(test) 

class Aa(object):
    def __init__(self, func):
        print("this is Aa")
        self.__func = func
    def __call__(self):
        print("this is call")
        self.__func()

@Aa
def b():
    print("bbbbbbbbb")

#调用Aa中的__call__方法
b() #b() 指 b = Aa(b)