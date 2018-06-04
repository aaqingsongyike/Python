#闭包
'''
    在函数里面再定义一个函数，并且这个函数用到外边的变量，那么这个函数及用到的变量
    称为闭包
'''
def test(num):  #闭包
    print("--------1---------")

    def test_in(num_in):    
        print("------------2----------")
        print("in test_in 函数，num_in is %d"%num_in)
        return num + num_in

    print("-----------3---------")
    #放回闭包的结果
    return test_in

ret = test(20)
print(ret)
print("********")
print(ret(100))

print(ret(200))