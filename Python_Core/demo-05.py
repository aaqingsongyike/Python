#属性property升级get和set方法

class Test(object):
    def __init__(self):
        self.__num = 100

    def setNum(self, newNum):
        self.__num = newNum
    def getNum(self):
        return self.__num

    #property
    num = property(getNum, setNum)

t = Test()
t_num = t.num   #等价于 t.getNum()
print(t_num)
t.num = 30      #等价于 t.setNum()
print(t.num)

