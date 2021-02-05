# JoinableQueue 的使用
# 这就像是一个Queue对象，但队列允许项目的使用者通知生成者项目已经被成功处理。通知进程是使用共享的信号和条件变量来实现的


from multiprocessing import Process, JoinableQueue
import time
 
 
def producer(q):
    for i in range(2):
        res = '包子%s' % i
        time.sleep(0.5)
        print('生产者生产了%s' % res)
 
        q.put(res)
    q.join()
 
 
def consumer(q):
    while True:
        res = q.get()
        if res is None: break
        time.sleep(1)
        print('消费者吃了%s' % res)
        q.task_done()  # 发出信号项目已处理完成，省去了后面需另外添加的q.put(None)
 
 
if __name__ == '__main__':
    # 容器
    q = JoinableQueue()
 
    # 生产者们
    p1 = Process(target=producer, args=(q,))
    p2 = Process(target=producer, args=(q,))
    p3 = Process(target=producer, args=(q,))
 
    # 消费者们
    c1 = Process(target=consumer, args=(q,))
    c2 = Process(target=consumer, args=(q,))
    c1.daemon = True  # 若不添加守护进程，则会卡在消费者
    c2.daemon = True
 
    p1.start()
    p2.start()
    p3.start()
    c1.start()
    c2.start()
 
    p1.join()
    p2.join()
    p3.join()

    # time.sleep(5)
    print('主')