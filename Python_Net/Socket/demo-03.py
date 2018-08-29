#绑定端口以及接收

from socket import *

#1. 创建套接字
udpSockket = socket(AF_INET, SOCK_DGRAM)

#2. 绑定本地的相关信息(接收方绑定)
bindAddr = ("", 7788)   #ip不用写， 表示当前电脑的ip
udpSockket.bind(bindAddr)

#3. 等待接收方接收数据数据
recData = udpSockket.recvfrom(1024) #1024表示最多能收1024个字节
content, desInfo = recData  #content为接收到的内容，desInfo为发送方的信息IP等
content.decode("utf-8") #解码

#4. 发送数据
sendData = "发送的内容"
socket.sendto(sendData.encode("utf-8"), 8080)   #encode("utf-8")发送编码

#5. 显示接收到的内容
print(recData)

#6. 关闭套接字
socket.close()