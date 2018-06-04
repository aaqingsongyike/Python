#内建属性————__getattribute__
'''
调用类属性和方法前，会先调用__getattribute__
'''

class Test(object):
    def __init__(self, sub1):
        self.sub1 = sub1
        self.sub2 = "cpp"
    
    #属性访问时拦截器，打log
    def __getattribute__(self, log):
        print("===>%s"%log)
        if log == "sub1":
            print("log sub1")
            return "redirect obj"
        else:
            #测试时，注释带这两行，将找不到sub2
            temp = object.__getattribute__(self, log)
            print("===>%s"%str(temp))
            return temp

    def show(self):
        print("this is itcast")

s = Test("python")
print(s.sub1)   
print(s.sub2)
s.show()