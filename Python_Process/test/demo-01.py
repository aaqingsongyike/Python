#调试————使用命令行进行调试

def getAverage(a, b):
    result = a + b
    print("result = %d"%result)
    return result

a = 100
b = 200
c = a + b

ret = getAverage(a, b)
print(ret)

'''
调试程序命令
python -m pdb demo-01.py
命令：
    l       #list 显示当前程序运行的代码 (->)代表运行的地方
    n       #next 执行下一行程序
    c       #continue 继续执行完所有代码
    b 9     #break在第9行设置断点 
    clear 1 #取消第一个断点，及取消第9行的断点
    s       #step 进入到一个函数
    p a     #设置断点到12行并用s命令，p a表示查看a的参数
    a       #设置断点到12行并用s命令，a 表示查看所有参数
    q       #退出
    r       #快速执行到函数最后一行
'''