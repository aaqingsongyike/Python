#Thread子类创建多线程
import threading
import time


class MyThread(threading.Thread):
    def run(self):
        for i in range(5):
            time.sleep(1)
            msg = "I'm " + self.name + " @ " + str(i)
            print(msg)
if __name__ == '__main__':
    t = MyThread()
    t.start()