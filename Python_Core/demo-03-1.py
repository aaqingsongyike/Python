#copy和deepcopy的不同
import copy
a = [11,22,33]
b = [44,55,66]
c = [a, b]
print(id(c))

e = copy.deepcopy(c)
print(id(e))
a.append(23)
print(e)
print(c)

#copy.copy()
print("*"*20)
print("copy.copy()")
a1 = [1,2,3]
b1 = [4,5,6]
c1 = [a1, b1]
print(id(c1))
e1 = copy.copy(c1)
print(e1)
a1.append(12)
print(e1)
print(id(e1))

#copy元组的特点
print("*"*20)
print("copy元组的特点")
f1 = (a1, b1)
g1 = copy.copy(f1)
print(id(f1))
print(id(g1))
