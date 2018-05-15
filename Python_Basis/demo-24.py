#私有方法
#私有方法只能在本类中使用

class Dog:
    def __init__(self, new_name):
        self.name = new_name

    def __test1(self):  #私有方法
        print("------------1----------")
    def test2(self):
        self.__test1()
        print("------------2----------")

dog = Dog("wangcai")
dog.test2()
