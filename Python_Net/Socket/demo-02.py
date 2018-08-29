#socket 通信
from socket import *


#1. 创建套接字socket
udpSocket = socket(AF_INET, SOCK_DGRAM)

#2. 发送
udpSocket.sendto(b"haha", ("192.168.0.1", 8080)) #参数(内容， 地址以及端口)
