#__del__ 方法

class Dog:
    def __del__(self):  #在对象删除之前做临时处理
        print("over")

dog = Dog()
dog1 = dog #dog1指向Dog()对象

del dog #删除dog当不影响dog1
print("*************")
#del dog1
print("============")

