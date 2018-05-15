demo:
    print   输出
demo-01:
    input   输入
demo-02:
    print           输出整数、小数以及字符串
    random.randint  随机数生成
demo-03:
    类型转换
    int(input("****"))  str--->int
    str(int)            int--->str
    len(str)            长度

    if                  条件判断
    if……else
    if……elif
demo-04:
    num = num1 // num2          两数想出取整
    num = num1**num2            num1的num2的次方
    print("a"*5)                重复输出多个相同的值
    print("%d%d"%(num1,num2))   输出多个不同的值
demo-05:
    逻辑判断
    or      或
    and     并且
    not     取反
demo-06:
    while   循环
    for     循环
    for……else
demo-07:
    break       结束本次循环
    continue    结束当前条件循环
demo-08:
    字符串拼接
    字符串常见操作：
        find    rfind   index   rindex      count      replace
        split   capitlize       startwith   endwith
        lower       upper       ljust       rjust      center
        lstrip      rstrip     strip        partition   rpartition
        splitlines  isalpha     isdigit     isalnum     join
demo-09:
    数组
    切片
demo-10:
    列表
    列表的增删改查
    列表也可用下标与切片
demo-11:
    字典
    字典的增删改查
    字典的常用操作
        len     keys    get     value   items   value
demo-12:
    元组
    只能实现查，不能增删改
demo-13:
    函数
    函数嵌套
    修改全局变量
    列表、字典当作全局变量
    缺省参数
    不定长参数
    拆包
    id
    可变类型和不可变类型
    递归
demo-14:
    列表排序 sort()小到大
            sort(reverse=True)大到小
            reverse()倒叙
    字典排序 sort(key=lambda x:x['name'])
demo-15:
    匿名函数
demo-16:
    文件操作
demo-17:
    文件操作练习——写入数据
demo-17-1:
    文件操作练习——读数据
demo-17-2:
    复制文件
demo-18:
    文件定位读写   seek   tell
demo-19:
    文件相关操作（必须导入import os 包）
        文件重命名
        文件删除
    文件夹的相关操作（必须导入 os 包）
        创建文件夹
        删除文件夹
        获取当前的操作路径
        改变默认路径
        获取目录列表
demo-20:
    文件批量重命名
demo-21:
    定义类
    创建对象
    调用对象方法
    添加属性
    获取对象属性
    __init__ 方法(初始化对象)
    __str__ 方法(获取对象的描述信息)
demo-21-1.py:
    __new__ 方法(是谁该创建的对象)
    参考demo-32单例
demo-22:
    对象中存放另一个对象
demo-23:
    保护（隐藏）对象的属性
demo-24:
    私有方法
demo-25:
    __del__()方法
demo-26:
    继承
    重写
    调用被重写的方法
demo-27:
    私有方法和私有属性在继承中的表现
demo-28:
    多继承
demo-29:
    多态
demo-30:
    类属性-实例属性
demo-31:
    实例方法、类方法、静态方法
demo-32:
    单例(参考demo-21-1.py中__new__方法)
demo-33:
    异常
        1)异常处理
        2)异常处理中抛出    
        3)抛出自定义异常
model:
    定义模块
    __all__
model-2:
    导入模块
    给模块起别名
package:
    导入Package文件夹中的model
        注意：
            Package文件夹中必须有__init__.py 文件
demo-34:
    给程序传参数
demo-35:
    列表生成式
demo-36:
    集合、元组、列表




