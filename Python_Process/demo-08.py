#进程池

from multiprocessing import pool
import os
import time
import random


def worker(num):
    for i in range(random.randint(1,3)):
        print("===pid = %d===num = %d==="%(os.getpid(), num))
        time.sleep(1)

po = pool.Pool(3)    #创建进程池，最大进程数为3

for i in range(10):
    print("---%d---"%i)

    #向进程池中添加任务，如果进程池中进程的个数超出，不会导致添加不进去
    po.apply_async(worker, (i,))    #(i,)表示worker函数中的参数num

print("---start---")
po.close()  #关闭进程池

#创建/添加任务后，主进程默认不会等待进程池中任务完成后结束，而是主进程
#   的任务做完之后，立马结束
po.join()   #主进程，等待子进程结束，必须放在close之后
print("---end---")

