#多进程拷贝多个文件
from multiprocessing import pool
from multiprocessing import managers    #进程池当中的队列
import os

def copyFileTask(name, oldFolderName, newFolderName, mq):
    "完成一个文件copy的功能"
    fr = open(oldFolderName+"/"+name)
    fw = open(newFolderName+"/"+name, "w")

    content = fr.read()
    fw.write(content)

    fr.close()
    fw.close()

    mq.put(name)

def main():
    #1. 获取用户要copy的文件夹的名字
    oldFolderName = input("请输入文件夹的名字")
    newFolderName = oldFolderName + "-cp"

    #2. 创建一个文件夹
    os.mkdir(newFolderName)

    #3. 获取old文件夹中的所有文件名
    fileNames = os.listdir(oldFolderName)

    #4. 使用多进程方式copy原文件新文件夹当中去
    po = pool.Pool(5)
    #4.1 查看是否拷贝完
    mq = managers.queue.Queue()
    for name in fileNames:
        po.apply_async(copyFileTask, args=(name, oldFolderName, newFolderName, mq,))
    
    num = 0
    allNum = len(fileNames)
    while True:
        mq.get()
        num+=1
        copyRate = num/allNum
        print("\rcopy的进度是：%.2f%%"%(copyRate*100), end="")
        if num == allNum:
            break
        print("拷贝完毕")

#    po.close()
#    po.join()

if __name__ == '__main__':
    main()