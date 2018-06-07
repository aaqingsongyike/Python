#并发

#fork()
import os
import time

#只能在Linux和Mac中使用
ret = os.fork() #fork()的返回值是 等于0(主进程)和大于0(子进程)
print("父进程和子进程都执行")
"""
os.getpid()     获取当前进程的值（pid）
os.getppid()    获取父进程的pid
"""
if ret == 0:
    while True:
        print("-父进程-%d"%os.getpid())
        time.sleep(1)
else:
    while True:
        print("-子进程-%d-%d"%(os.getppid(), os.getpid()))
        time.sleep(2)
