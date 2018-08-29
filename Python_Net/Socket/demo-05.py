#发送请求测试

import struct
from socket import *

#构造下载请求数据(组包)
'''
参数：！====》指网络方式
	  H====》指1转换为2个字节
	  8s===》指text.jpg占8个字节
	  b====》指0占1个字节
	  5s===》指octet占5个字节
'''
sendData = struct.pack("!H8sb5sb", 1, "text.jpg", 0, "octet", 0)	

udpSocket = socket(AF_INET, SOCK_DGRAM)
socket.sendto(sendData, ("182.168.119.210", 69))

#解包
'''
每2个字节处理成一个字节
返回值是一个元组
'''
result = struct.unpack("!HH", recvData[:4])
print(result)

udpSocket.close()