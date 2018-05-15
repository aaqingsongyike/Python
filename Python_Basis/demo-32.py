#单例

class Dog(object):
    pass

class Cat(object):
    __instance = None
    def __new__(cls):
        if cls.__instance == None:
            cls.__instance = object.__new__
            return cls.__instance
        else:
            return cls.__instance#返回上一次对象的引用

print("id相同指同一个对象")
print("a,b")
a = Dog()
print(id(a))
b = Dog()
print(id(b))

print("c,d")
c = Cat()
print(id(c))
d = Cat()
print(id(d))