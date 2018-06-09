#线程共享全局变量
#线程之间全局变量是公用的

from threading import Thread
import time

g_num = 100

def work1():
    global g_num
    for i in range(3):
        g_num+=1
        print("---in work1, g_num is %d---"%g_num)

def work2():
    global g_num
    print("---in work2, g_num is %d---"%g_num)

print("---线程创建之前, g_num is %d---"%g_num)

t1 = Thread(target=work1)
t1.start()

#延时，保证线程t1的事情做完
time.sleep(1)

t2 = Thread(target=work2)
t2.start()
    