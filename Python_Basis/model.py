#定义模块

#__all__ 方法
'''
为了让别人使用指定的函数，类，全局变量
'''
__all__ = ["test1", "test2"]    #[] 中为方法名称，类以及全局变量(别人只能用方法test1,test2 而test3不能使用)

def test1():
    print(__name__) #当前模块的名字
    print("test1")

def test2():
    print("test2")  

def test3():
    print("test3")

