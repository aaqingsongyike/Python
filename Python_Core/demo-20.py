#functools  工具函数

import functools

print(dir(functools))   #functools中常用函数
print("-"*20)

#partial 偏函数(第一次执行默认传入的参数)
print("偏函数partial")
def showargs(*args, **kw):
    print(args)
    print(kw)
p1 = functools.partial(showargs, 1, 2, 3)
p1()
p1(4, 5, 6)
p1(a="python", b="itcast")
print("-"*20)

#wraps
def note(func):
    "note function" #说明文档
    @functools.wraps(func)  #可以查看test()函数中的说明文档
    def wrapper():
        "wrapper function"
        print("note something")
        return func()
    return wrapper
@note
def test():
    "test function"
    print("I am test")
test()
print(test.__doc__) #查看说明文档
print(help(test))