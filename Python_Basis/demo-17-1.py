#文件操作练习

#读取数据

f = open("test.txt", "r")

content = f.read()
print(content)

f.close()