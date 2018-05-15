#继承
#重写
#调用被重写的方法(使用过重写的方法之后，继续使用父类的方法)

class Animal:
    def eat(self):
        print("吃")
    def drink(self):
        print("喝")
    def sleep(self):
        print("睡觉")
    def run(self):
        print("跑")

class Dog(Animal):  #继承
    def bark(self):
        print("汪汪叫")
class Dog_xiaotianquan(Dog):
    def bark(self): #重写
        print("狂叫")

        #方式一
        #Dog.bark(self)  #调用被重写的方法
        
        #方式二
        super().bark()

a = Animal()
a.eat()

wangcai = Dog()
wangcai.drink()
wangcai.bark()

xiaotianquan = Dog_xiaotianquan()
xiaotianquan.sleep()
xiaotianquan.bark()