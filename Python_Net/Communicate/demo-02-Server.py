from socket import *
from threading import Thread

def socketThread(clientSocket, clientAddr):
    while True:
        recvData = clientSocket.recv(1024)  #表示一次收多少个字节
        if len(recvData)>0:
            print("%s， %s"%(str(clientAddr), recvData))
            #print("$s, $s"%(str(clientAddr), recvData))
        else:
            break
        #发送数据给客户端
        sendData = input("send to client: ")
        clientSocket.send(bytes(sendData, "utf-8"))

        # 关闭套接字
        #在多进程中必须关闭客户端套接字，但在多线程中不能关闭客户端套接字
        #clientSocket.close()

def main():
    serverSocket = socket(AF_INET, SOCK_STREAM)  # 默认创建主动套接字
    # 重复使用绑定信息
    serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    serverSocket.bind(("", 7788))
    serverSocket.listen(5)  # 将主动套接字转换成被动套接字(参数为任意正整数)

    while True:
        # 新的socket, 客户端的ip以及端口
        clientSocket, clientAddr = serverSocket.accept()  # 接听客户端发送来的消息

        t = Thread(target=socketThread, args=(clientSocket, clientAddr))
        t.start()

    serverSocket.close()


if __name__ == '__main__':
    main()

