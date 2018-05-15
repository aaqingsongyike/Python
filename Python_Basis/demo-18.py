#文件定位读写

#seek(offset, from)

#offset 偏移量

#from:0---->文件开头
#from:1---->当前操作位置
#from:2---->文件末尾

f = open("test.txt")

f.seek(2,0) #从文件开头往后跳2个字节
contents = f.read()
print(contents)

f_tell = f.tell()   #获取当前位置
print(f_tell)