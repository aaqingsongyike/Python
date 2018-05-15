#私有方法和私有属性在继承中的表现

'''
私有方法不会被继承
私有属性不会被继承
'''

class A:
    def __init__(self):
        self.num1 = 100
        self.__num2 = 200
    
    def test1(self):
        print("this is test1")

    def __test2(self):
        print("this is test2")

    def test3(self):
        self.__test2()
        print(self.__num2)
class B(A):
    pass

b = B()
b.test1()
#b.__test2() #私有方法不会被继承
#print(b.__num2) #私有属性不会被继承

b.test3()
