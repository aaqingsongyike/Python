#列表当作线程的参数

from threading import Thread
import time

g_num = [11, 22, 33]

def work1(nums):
    nums.append(44)
    print("-in work1-", nums)

def work2(nums):
    #延时，保证t1线程中的事情做完
    time.sleep(1)
    print("-in work2-", nums)

def main():
    t1 = Thread(target=work1, args=(g_num,))
    t1.start()

    t2 = Thread(target=work2, args=(g_num,))
    t2.start()
    
if __name__ == '__main__':
    main()