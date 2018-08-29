#TFTP下载器

from socket import *

udpSocket = socket(AF_INET, SOCK_DGRAM)

#0. 绑定本地相关信息
bindAddr = ("", 7788)
udpSocket.bind(bindAddr)

#1. 创建一个空文件
f = open("text.jpg", "w")

#2. 向里面写数据
while True:
	recvDate = udpSocket.recvfrom(1024)
	if xxx:
		break
	else:
		f.write(recvDate)

#3. 关闭
f.close()