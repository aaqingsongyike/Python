#常用模块
import hashlib

m = hashlib.md5()   #创建hash对象,使用md5进行加密       (md5()也可换成sha256())
print(m)
m.update(b'itcast')  #对itcast进行加密
print(m.hexdigest())#返回十六进制数字字符串