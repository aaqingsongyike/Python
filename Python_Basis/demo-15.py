#匿名函数

#匿名函数当作实参
'''
    调用同一函数实现加减乘除
'''
def test(a,b,func):
    result = func(a, b)
    return result
#加
num = test(11,22, lambda x,y:x+y)
print("this is add result: %d"%num)
#减
num1 = test(33,2, lambda x,y:x-y)
print("this is less result: %d"%num1)

func_new = input("请输入一个匿名函数")
func_new = eval(func_new) #将字符串转换成表达式
num2 = test(44,55,func_new)
print("this is num2: %d"%num2)
