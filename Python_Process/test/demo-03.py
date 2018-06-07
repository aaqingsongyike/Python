"""
如果主进程先结束，则主进程结束。
不会因为子进程没结束，而主进程等待子进程
"""

import os
import time

ret = os.fork()

if ret == 0:
    print("---子进程---")
    time.sleep(5)
    print("---子进程over---")
else:
    print("---父进程---")
    time.sleep(3)