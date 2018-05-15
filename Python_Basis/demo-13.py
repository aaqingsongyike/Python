#函数

#定义函数
def func():
    print("this is funtion")
#调用函数
func()

#带参数的函数
def fun_add(num1, num2):
    sum = num1 + num2
    print("%d + %d = %d"%(num1, num2, sum))
fun_add(10, 20)

#函数返回值
def func_return(num1, num2):
    less = num1 - num2
    return num1, num2, less
    #return [num1, num2, less]
    #return {"a":num1, "b":num2, "c":less}
    #return (num1, num2, less)
num1, num2, less = func_return(22, 11)
print("this is return less:%d - %d = %d"%(num1, num2, less))

#函数嵌套
def func_test1():
    print("this is func_test1")
    func_test2()
def func_test2():
    print("this is func_test2")
func_test1()

#修改全局变量
g_wendu = 0
def get_wendu():
    global g_wendu   #修改全局变量
    g_wendu = 33
get_wendu()
print("this is 修改全局变量：%d"%g_wendu)

#列表、字典当作全局变量
#列表、字典不需要加 global
nums = [11,22,33]
def test():
    nums.append(44)
    nums[0] = 0
def test2():
    print("this is nums: %s"%nums)
test()
test2()

#缺省参数
def test3(a, b = 22, c = 33):
    print("this is a:%d"%a)
    print("this is b:%d"%b)
    print("this is c:%d"%c)
test3(11)
test3(22, 33)
test3(11, c=99)

#不定长参数
def test4(a1, b1, *args, **kwargs):   #*args是元组  **kwargs是字典
    print("this is a1: %d"%a1)
    print("this is b1: %d"%b1)
    print("this is args: ", end = "")
    print(args)
    print("this is kwargs %s:"%kwargs)
test4(1, 2)
test4(1, 2, 3)
test4(1, 2, 3, 4, task=5, done=6)
def test5(a2, b2, *args):
    sum = a2 + b2
    for num in args:
        sum+=num
    print("this is sum: %d"%sum)
test5(1, 2, 3, 4, 5)

#拆包
def test6(a3, b3, *args, **kwargs):
    print("this is a3: %d"%a3)
    print("this is b3: %d"%b3)
    print(args)
    print("this is kwargs: %s"%kwargs)
A = (44,55)
B = {"name":"aa", "sex":"man"}
test6(11,22,A,B)
test6(11,22,*A,**B)

#id 打印aa和bb存储100的地址
aa = 100
bb = aa
cc = bb
print(id(aa))
print(id(bb))
print(id(cc))

#可变类型和不可变类型
#数字、字符串、元组是不可变类型
#列表和字典是可变类型

#递归
result = 1
def digui(num):
    if num > 1:
        return  num * digui(num-1)
    else:
        return num
result = digui(5)
print("this is digui result: %d"%result)
