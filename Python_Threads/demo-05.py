#互斥锁
from threading import Thread, Lock
import time

g_num = 0

def test1():
    global g_num

    #上锁
    mutex.acquire()
    for i in range(1000000):
        #mutex.acquire()
        g_num+=1
        #mutex.release()
    
    #开锁
    mutex.release()

    print("-test1-g_num=%d-"%g_num)

def test2():
    global g_num

    #上锁
    mutex.acquire()
    for i in range(1000000):
        #mutex.acquire()
        g_num+=1
        #mutex.release()

    #开锁
    mutex.release()

    print("-test2-g_num=%d-"%g_num)

#创建互斥锁
mutex = Lock()  #默认是开锁状态


p1 = Thread(target=test1)
p1.start()

p2 = Thread(target=test2)
p2.start()