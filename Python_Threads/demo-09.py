#异步
from multiprocessing import pool
import time 
import os

def test():
    print("---进程池中的进程---pid=%d,ppid=%d"%(os.getpid(), os.getppid()))
    for i in range(3):
        print("---%d---"%i)
        time.sleep(1)
    return "haha"

#args的值为test函数的返回值
def test2(args):
    print("---callback func--pid=%d"%os.getpid())
    print("---callback func--args=%s"%args)

po = pool.Pool(3)

'''
当子进程执行完test函数时，唤醒主进程回调test2函数
实现异步操作
'''
po.apply_async(func=test, callback=test2)   #callback回调   实现异步

while True:
    time.sleep(1)
    print("---主进程---pid=%d"%os.getpid())