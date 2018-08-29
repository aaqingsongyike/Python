#greenlet
from greenlet import greemlet
import time


def A():
    print("---A---")
    gr2.switch()
    print("---A1---")
    time.sleep(0.5)

def B():
    print("---B---")
    gr1.switch()
    print("---B2---")
    time.sleep(0.5)

gr1.greenlet(A)
gr2.greenlet(B)

#切换到gr1中运行
gr1.switch()