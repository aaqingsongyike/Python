#通用装饰器

def func(funcName):
    def func_in(*args, **kwargs):
        ret = funcName(*args, **kwargs)
        return ret
    return func_in

@func
def test1():    #有返回值
    print("test1")
    return "haha"

@func
def test2():    #无参 无返回值
    print("test2")

@func
def test3(a):   #有参
    print("test3----a=%d"%a)

ret = test1()
print("test1 return value is %s"%ret)

test2()

test3(11)