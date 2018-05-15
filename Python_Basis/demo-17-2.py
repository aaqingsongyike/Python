#复制文件

#将test.txt中的文件复制到test.cp.txt中

#1.获取要复制的文件名
old_file_name = input("请输入要复制的文件名")

#2.打开要复制的文件
old_file = open(old_file_name, "r")

#3-0.新文件名
position = old_file_name.rfind(".")
new_file_name = old_file_name[0:position] + ".cp" + old_file_name[position:]

#3-1.新建一个文件
new_file = open(new_file_name,"w")

#4.从旧文件中读取数据，并且写入到新文件中
while True:
    content = old_file.read(1024)
    if len(content)==0:
        break
    new_file.write(content)

#5.关闭文件
old_file.close()
new_file.close()