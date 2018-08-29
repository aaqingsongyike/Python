#单进程非堵塞服务器
from socket import *

#创建服务端socket
serverSocket = socket(AF_INET, SOCK_STREAM)
#绑定
localaddr = ("", 7788)
serverSocket.bind(localaddr)
serverSocket.listen(5)
#将serverSocket转换成非堵塞
serverSocket.setblocking(False)
#保存客户端信息
clientInfo = []
while True:
    try:
        clientSocket, clientAddr = serverSocket.accept()
    except:
        pass
    else:
        print("一个新的客户端到来：%s"%str(clientAddr))
        clientSocket.setblocking(False)
        clientInfo.append((clientSocket, clientAddr))
    for clientSocket, clientAddr in clientInfo:
        try:
            recvData = clientSocket.recv(1024)
        except:
            pass
        else:
            if len(recvData)>0:
                print("----4----")
                print("%s, %s"%(str(clientAddr), recvData))
            else:
                clientSocket.close()
                clientInfo.remove((clientSocket, clientAddr))
                print("%s 已经下线"%str(clientAddr))