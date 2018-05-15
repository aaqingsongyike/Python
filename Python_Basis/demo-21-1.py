#__new__方法

class Dog(object):
    def __init__(self):
       print("init方法")

    def __del__(self):
        print("del方法")

    def __str__(self):
        print("str方法")
        return "对象的描述信息"

    def print_a(self):
        print("aa")

    def __new__(cls):#cls此时是Dog指向的那个类对象
        print(id(cls))
        print("new方法")
        return object.__new__(cls)#加上这句执行init、str、del方法

print(id(Dog))
xtq = Dog()
#代码写到这里且不写return后只会执行__new__ 方法