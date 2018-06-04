#__slots__
class Person(object):
    __slots__ = ("name", "age")
p = Person()
p.name = "老王"
p.age = 10
print("%s的年龄：%d"%(p.name, p.age))

#p.addr = "北京"    报错 （不存在该属性）及不能添加该属性
#print(p.addr)