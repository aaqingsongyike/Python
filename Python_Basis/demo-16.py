#文件操作

#打开文件
f = open("test.py","r") #文件名, 打开方式(r,w)

#读文件
f.read()        #读所有
f.read(1)       #读一个字节(适合大文件操作)
f.readline()    #读一行
f.readlines()   #读所有并存到列表中

#写文件
f.write("hahaha")

#关闭文件
f.close()

