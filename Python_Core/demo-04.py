#私有化

class Test(object):
    def __init__(self):
        self.__num = 100    #__表示私有属性

    #调用私有属性
    def setNum(self, newNum):   #设置值
        self.__num = newNum
    def getNum(self):           #获取值
        return self.__num

t = Test()
#print(t.__num)
print(t.getNum())

'''
尽可以在本模块中使用
不允许使用from mokuai import *其他模块使用
但是允许 import mokuai 其他模块使用
'''
_num = 20