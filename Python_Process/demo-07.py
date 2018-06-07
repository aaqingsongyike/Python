#在Windows中实现多任务

from multiprocessing import process
import os

#子进程运行的代码
def run_proc(name):
    print("子进程运行中，name=%s, pid=%d"%(name, os.getpid()))

def main():
    print("父进程运行中 %d"%os.getpid())
    p = process.Process(target=run_proc, args=('test'))
    print("子进程将要运行")
    p.start()
    p.join()
    print("子进程运行结束")

if __name__ == '__main__':
    main()