#静态服务器
import socket
import multiprocessing
import re
import sys

# 设置静态文件根目录
HTML_ROOT_DIR = "./html"
WSGI_PYTHON_DIR = "./wsgipython"

class HttpServer(object):
    """"""
    def __init__(self):
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # 防止端口占用
        self.serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def startHandle(self, status, headers): # 状态码，响应头
        """
        status = "200 OK"
        headers = [
        ("Content-Type", "text/plain")
        """
        response_headers = "HTTP/1.1" + status + "]r]n"
        print("this is status: " + status)
        print(headers)
        for header in headers:
            response_headers += "%s: %s\r\n" % header
        self.resonse_headers = response_headers

    # 启动
    def serverStart(self):
        self.serverSocket.listen(128)
        while True:
            clientSocket, clientAddr = self.serverSocket.accept()
            print("[%s, %s]用户连接上了："%(clientSocket, clientAddr))
            handleClientProcess = multiprocessing.Process(target=self.handle, args=(clientSocket,))
            handleClientProcess.start()

            clientSocket.close()

    def handle(self, clientSocket):
        """处理客户端请求"""

        # 获取客户端请求数据
        requestData = clientSocket.recv(1024)
        print("request data: ", requestData)

        # 解析字符串
        requestLine = requestData.splitlines()
        for lines in requestLine:
            print(lines)

        # 解析请求报文
        # 'GET / HTTP/1.1'
        requestStartLine = requestLine[0]
        # 提取用户请求的文件名
        print(requestStartLine.decode("utf-8"))
        fileName = re.match(r"\w+ +(/[^ ]*) ", requestStartLine.decode("utf-8")).group(1)  # 对'GET / HTTP/1.1'进行正则匹配
        method = re.match(r"(\w+) +/[^ ]* ", requestStartLine.decode("utf-8")).group(1)

        # 动态改写
        # 执行py文件    "/mtime.py"
        if fileName.endswith(".py"):
            try:
                # 导包
                m = __import__(fileName[1:-3])
            except Exception:
                self.resonse_headers = "HTTP/1.1. 404 Not Found\r\n"
                responseBody = "not found"
            else:
                env = {
                    "PATH_INFO": fileName,
                    "METHOD": method
                }
                responseBody = m.application(env, self.startHandle)
            response = self.resonse_headers + "\r\n" + responseBody
        else:
            if "/" == fileName:
                fileName = "/index.html"
            # 打开文件读取内容
            try:
                file = open(HTML_ROOT_DIR + fileName, "rb")  # b代表以二进制的方式打开
            except IOError:
                responseStartLine = "HTTP/1.1 404 OK\r\n"  # 起始行
                responseHeaders = "Server: My Server \r\n"  # 响应头
                responseBody = "the file not found!!!"  # 响应体
            else:
                fileData = file.read()
                file.close()

                # 构造响应数据
                responseStartLine = "HTTP/1.1 200 OK\r\n"  # 起始行
                responseHeaders = "Server: My Server \r\n"  # 响应头
                responseBody = fileData.decode("utf-8")  # 响应体

            response = responseStartLine + responseHeaders + "\r\n" + str(responseBody)  # 响应报文
            print("resonse data: ", response)

        # 向客户端返回数据
        clientSocket.send(bytes(response, "utf-8"))

        # 关闭客户端连接
        clientSocket.close()

    # 绑定端口
    def setBind(self, port):
        self.serverSocket.bind(("", port))


def main():
    sys.path.insert(1, WSGI_PYTHON_DIR)
    httpServer = HttpServer()
    httpServer.setBind(8000)
    httpServer.serverStart()

if __name__ == "__main__":
    main()
