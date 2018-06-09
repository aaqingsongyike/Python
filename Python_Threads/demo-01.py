#threading模块

from threading import Thread
import time


def saySorry(name, a):
    print("%s, 我错了"%name)
    a+=1
    print(a)
    time.sleep(1)

def main():
    a = 0
    for i in range(5):
        t = Thread(target=saySorry, args=("小杨", a,))
        t.start()
    print(a)

if __name__ == '__main__':
    main()