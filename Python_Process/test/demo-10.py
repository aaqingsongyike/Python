#进程间通信--->Queue(队列)

from queue import Queue

#创建一个队列，最多容纳3个消息
q = Queue(3)
print("队列中的消息数为：%d"%q.qsize())


q.put("添加1个消息")
print("队列中的消息数为：%d"%q.qsize())

q.put("添加2个消息")
print("队列中的消息数为：%d"%q.qsize())

q.put("添加3个消息")
print("队列中的消息数为：%d"%q.qsize())

#判断队列是否为满
print("判断队列是否为满：%s"%q.full())

#取出队列中的消息
i = 1
while not q.empty():    #判断队列是否为空
    print("队列中第%d个消息为：%s"%(i, q.get()))
    i+=1

#取完之后的消息数
print("取完之后的消息数：%d"%q.qsize())


q.put("123")
try:
    print(q.get_nowait())
except Exception:
    print("error")
