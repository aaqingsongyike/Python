#登录
from redis import *
from MysqlHelper import MysqlHelper
from hashlib import sha1

class RedisHelper(object):
    def __init__(self, host, port):
        self.__redis = StrictRedis(host, port)

    def set(self, key, value):  #写
        self.__redis.set(key, value)

    def get(self, key):     #获取
        return self.__redis.get(key)

# 接收输入
name = input("请输入用户名")
pwd1 = input("请输入密码")

# 加密
s1 = sha1()
s1.update(pwd1)
pwd2 = s1.hexdigest()

# 查询Redis是否存在此用户
r = RedisHelper('localhost', 6379)
m = MysqlHelper('localhost', 3306, 'py3', 'root', 'mysqo')

# 判断Redis中是否存储了此用户和密码
if r.get('name') == None:
    sql = 'select passwd from users where name=%s'
    pwd3 = m.one(sql, [name])
    if pwd3 == None:
        print("用户名错误")
    else:
        # 将MySQL中的数据存入Redis中
        r.set(name, pwd3[0])
        # 判断密码是否正确
        if pwd3[0] == pwd2:
            print('成功')
        else:
            print('密码错误')
else:
    #判断Redis中的用户密码
    if r.get(name) == pwd2:
        print("密码成功")
    else:
        print("密码错误")


