#定义类

class Cat: 
    #属性
    height = 100

    #初始化对象(自动调用)
    def __init__(self, new_name, new_sex):
        self.name = new_name
        self.sex = new_sex

    #一般是获取对象的描述信息
    def __str__(self):
        return self.name+self.sex   #必须是return

    #方法
    def eat(self):  #必须加self
        print("this cat eat fish")
    def drink(self):
        print("this cat drink water")
    def intrduce(self):
        print(self.name)   
        print(self.sex)     

#创建对象
tom = Cat("汤姆", "man")  #参数为__init__里的参数

#调用对象方法
tom.eat()
tom.drink()

#添加属性
tom.age = 40

#获取对象的属性
#print(tom.name)    #方式1
#print(tom.age)
tom.intrduce()      #方式2

langmao = Cat("蓝猫", "woman")
langmao.age = 10
langmao.intrduce()

#__str__
print(tom)
print(langmao)