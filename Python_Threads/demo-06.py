#避免死锁---》添加超时时间

import threading
import time

class MyThread1(threading.Thread):
    def run(self):
        if mutexA.acquire([blocking=True, timeout=2]):  #添加超时时间
            print(1)
            mutexA.release()
        pass

class MyThread2(threading.Thread):
    def run(self):
        pass

mutexA = threading.Lock()
mutexB = threading.Lock()
def main():

    t1 = MyThread1()
    t2 = MyThread2()
    t1.start()
    t2.start()

if __name__ == '__main__':
    main()