#给对象添加方法
#types.MethodType

import types

class Person(object):
    def __init__(self, newName, newAge):
        self.name = newName
        self.age = newAge

laowang = Person("老王", 22)
#给对象动态添加实例方法
def eat(self):
    print("%s在吃东西"%self.name)
laowang.eat = types.MethodType(eat, laowang)
laowang.eat()

#添加静态方法
@staticmethod
def test():
    print("staticMethod")
Person.test = test
laowang.test()
Person.test()

#添加类方法
@classmethod
def printNum(cls):
    print("classMethod")
Person.printNum = printNum
laowang.printNum()
Person.printNum()
