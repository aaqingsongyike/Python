from socket import *

tcpClientSocket = socket(AF_INET, SOCK_STREAM)

#链接服务器
#tcpClientSocket.connect(("localhost:8080", 8899))
tcpClientSocket.connect(("192.168.0.102", 7788))

tcpClientSocket.send("haha")
recvData = tcpClientSocket.recv(1024)
print("recvData: %s"%recvData)

tcpClientSocket.close()