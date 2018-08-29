#udp广播

import sys, socket

dest = ("<broadcast>", 7788)	#自动识别当前的广播地址

#1. 创建udp套接字
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 

#2. 对需要发送广播数据的套接字进行修改，否则不能发送广播数据(允许发送广播数据)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)     #固定格式

#3. 以广播的形式发送数据到本地网络的所有电脑中
s.sendto("Hi", dest)

print("等待对方回复")

while True:
    (buf, address) = s.recvfrom(2048)
    print("Received from %s : %s"%(address, buf))