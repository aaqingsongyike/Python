"""
深拷贝不共享对象数据（一个对象中的数据改变不会引起其他对象中的数据发生改变）
浅拷贝共享对象数据（一个对象中的数据发送改变会引起其他对象中的数据发生改变）
"""

#深拷贝
import copy
a1 = [11,22,33]
c1 = copy.deepcopy(a1)
print(id(a1))
print(id(c1))

#浅拷贝
a = [1,2,3]
b = a
print(id(a))
print(id(b))
