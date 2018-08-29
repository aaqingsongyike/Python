# 添加
import pymysql


try:

    name = input("请输入用户名")

    # 打开数据库连接
    conn = pymysql.connect('localhost', 'root', 'yubiao4076', 'str')
    # 使用cursor()方法创建cursor对象
    curson1 = pymysql.cursors()

    #sql = 'insert into str(name) values("aa")'  # 添加
    #sql1 = 'update str set name="aa" where id=9' # 修改
    #sql2 = 'delete from str where id=9'     # 删除
    # 执行数据库操作
    #curson1.execute(sql)
    '''将上面sql语句参数化（等价替换防止sql注入）'''
    sql = 'insert into str(name) values(%s)'
    curson1.execute(sql, [name])
    # 关闭数据库
    curson1.close()
    conn.close()

except Exception :
    print(111)
