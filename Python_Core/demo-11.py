#python语音的动态性

#给对象动态添加属性
#给对象动态添加方法

import types    #动态添加方法时使用
class Person(object):
    def __init__(self, newName, newAge):
        self.name = newName
        self.age = newAge

def run(self):
    print("%s正在跑"%self.name)

laowang = Person("老王", 23)
print(laowang.name)
print(laowang.age)

laowang.addr = "北京"   #动态添加属性
print(laowang.addr)

laozhang = Person("老张", 20)
Person.num = 100    #动态添加属性

print(laowang.num)
print(laozhang.num)
laozhang.run = types.MethodType(run, laozhang) #动态添加方法（方法，对象）
laozhang.run()

