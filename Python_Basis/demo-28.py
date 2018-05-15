#多继承

class Base(object):
     def test(self):
         print("Base")

class A(Base):
    def test1(self):
        print("test1")

class B(Base):
    def test2(self):
        print("test2")

class C(A, B):  #多继承
    def test3(self):
        print("test3")

c = C()
c.test1()
c.test2()
c.test3()

#决定这调用一个方法的时候，搜索的顺序，如果在某个类中
#找到了方法，就停止搜索
print(C.__mro__)