#异常

#1)异常处理
#   异常名字有（NameError、）
try:
    print(num)
    print("1111111111")
except NameError:    #异常名字
    print("异常处理方式")
try:
    open("xxx.txt")
    print("22222222")
#except Exception:   #Exception 是通用异常名字
except FileNotFoundError:
    print("文件不存在")
else:
    print("如果没有异常才会去做")
finally:
    print("无论是否有异常都会去做")
    print("this is finally")

#2)异常处理中抛出异常
class Test(object):
    def __init__(self, switch):
        self.switch = switch
    def calc(self, a, b):
        try:
            return a/b
        except Exception as result:
            if self.switch:
                print("捕获到异常,信息如下：")
                print(result)
            else:
                #重新抛出这个异常给系统
                raise
test = Test(True)
test.calc(11, 0)
#test.switch = False
#test.calc(11, 0)

#3)自定义异常
class ShortInputException(Exception):
    #自定义异常类
    def __init__(self, length, atleast):
        self.length = length
        self.atleast = atleast
def main():
    try:
        s = input("请输入---》")
        if len(s) < 3:
            #raise引发自定义的异常(可以是类也可以是函数)
            raise ShortInputException(len(s), 3) #ShortInputExpection为自定义的异常
    except ShortInputException as result:
        print("ShortInputExpection: 输入的长度为 %d，长度至少为：%d"%(result.length, result.atleast))
    else:
        print("没有异常")
main()
