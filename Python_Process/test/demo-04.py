#全局变量在多个进程中不共享

#多任务进程修改全局变量
import os 
import time

g_num = 100

ret = os.fork()

if ret == 0:
    g_num = 200
    print("---progress1--g_num = %d"%g_num)
else:
    time.sleep(3)
    print("---progress2--g_num = %d"%g_num)