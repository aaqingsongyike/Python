#文件批量重命名

import os

#1获取重命名的文件夹的名字
folder_name = input("请输入重命名的文件夹:")

#2获取指定文件夹中所有的文件名字
file_names = os.listdir(folder_name)

#改变默认操作路径
#os.chdir("重命名")
#os.chdir(folder_name)

#3重命名
for name in file_names:
    print("要重命名的文件："+name)
    #os.rename(name, "./rename"+name)
    old_file_name = folder_name+"/"+name    #旧的路径+文件名
    new_file_name = folder_name+"/"+"yyb"+name  #改变后的路径+新的文件名
    os.rename(old_file_name, new_file_name)
