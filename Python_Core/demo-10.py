#带有参数的装饰器
'''
1、调用函数funcArg
2、调用装饰器@func
3、装饰test()
'''
def funcArg(pre="hello"):
    print("args is " + pre)
    def func(funcName):
        def func_in():
            print("记录日志---arg=%s"%pre)
            funcName()
        return func_in
    return func

@funcArg("heihei")
def test():
    print("test")

test()
