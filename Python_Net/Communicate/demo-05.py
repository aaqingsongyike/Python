#epoll
import socket
import select

#创建套接字
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#设置可以重复使用绑定的信息
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)
#绑定本机信息
s.bind(("", 7788))
#变为被动
s.listen(10)

#创建一个epoll对象
epoll = select.epoll()
#注册
epoll.reg
