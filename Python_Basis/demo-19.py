#文件相关操作

import os

#文件重命名
#os.rename("rename.txt", "rename-01.txt")

#删除文件
#os.remove("xxx.txt")

###############################
#文件夹的相关操作

#创建文件夹
#os.mkdir("test")
#os.mkdir("test1")

#删除文件夹
#os.rmdir("test1")

#获取当前的操作路径
cwd = os.getcwd()
print(cwd)

#改变默认路径
Chdir = os.chdir("..")  #参数为路径
print(Chdir)

#获取目录列表
LisDir = os.listdir("./")   #当前目录的列表
print(LisDir)