#装饰器

def w1(func):   #func指向f1, f2, f3...
    def inner():
        print("正在验证权限")
        func()  #func()指向f1(), f2(), f3()....
    return inner

@w1
def f1():
    print("f1")

@w1
def f2():
    print("f2")

f1()
f2()

#装饰器装饰无参数的函数
print("装饰器装饰无参的函数")
def funcs(functionName):
    print("---funcs---1")
    def funcs_in():
        print("---funcs_in---1")
        functionName()
        print("---funcs_in---2")
    print("---funcs---2")
    return funcs_in

@funcs
def test():
    print("test")
test()

#使用装饰器对有参数的函数装饰
print("装饰器装饰有参的函数")
def funcs_s(functionName):
    def funcs_in(a, b):
        functionName(a, b)
    return funcs_in
@funcs_s
def test1(a, b):
    print("test1---a=%d, b=%d---"%(a, b))
test1(1, 3)

#装饰器装饰有参数的函数
print("装饰器装饰有参数的函数")
def funcs_s_s(functionName):
    def funcs_in(*args, **kwargs):
        functionName(*args, **kwargs)
    return funcs_in
@funcs_s_s
def test2(a, b, c):
    print("a=%d, b=%d, c=%d"%(a, b, c))
test2(11, 22, 33)

#装饰器装饰带有返回值的函数
print("装饰器装饰带有返回值的函数")
def funcs_s_s_s(functionName):
    def funcs_in():
        result = functionName() #保存返回来的值
        return result   #将返回来的值返回到对象中调用（69行res = test3()）
    return funcs_in
@funcs_s_s_s
def test3():
    print("test3")
    return "HAHA"
res = test3()
print("test3 return value is %s"%res)

