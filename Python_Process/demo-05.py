#多个fork

import os
import time

#父进程
ret = os.fork() 
if ret == 0:
    #子进程
    print("-1-")
else:
    #父进程
    print("-2-")

#父子进程
ret = os.fork()
if ret == 0:
    #父子进程中的父
    print("-11-")
else:
    #父子进程中的子
    print("-22-")
