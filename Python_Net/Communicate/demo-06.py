#简单协程的实现(生成器实现协程)
import time

def A():
    while True:
        print("---A---")
        yield
        time.sleep(0.5)

def B(c):
    while True:
        print("---B---")
        c.__next__()
        time.sleep(0.5)

if __name__ == "__main__":
    a = A()
    b = B(a)
