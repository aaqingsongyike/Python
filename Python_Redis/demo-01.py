#Python与Redis交互
from redis import *

'''
#连接Redis
r = StrictRedis(host="localhost", port=6379)

#写(通过管道方式写)
pipe = r.pipeline()
pipe.set('py10', 'hello1')
pipe.set('py11', 'world1')
pipe.execute()

#读
temp = r.get('py10')
print(temp)
'''
#j将上面的内容封装
class ResisHelper(object):
    def __init__(self, host, port):
        self.__redis = StrictRedis(host, port)

    def set(self, key, value):  #写
        self.__redis.set(key, value)

    def get(self, key):     #获取
        return self.__redis.get(key)