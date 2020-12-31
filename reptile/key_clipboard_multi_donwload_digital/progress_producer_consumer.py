# product consumer

from multiprocessing import Process, Queue
import time
 
def producer(q, name):
    for i in range(5):
        res = '包子%s' % i
        time.sleep(0.5)
        print('%s 生产了%s' % (name, res))

        q.put(res)

def consumer(q, name):
    while True:
        res = q.get()
        if res is None: break
        time.sleep(1)
        print('%s 吃了%s' % (name, res))


if __name__ == '__main__':
    # 容器
    q = Queue()
 
    # 生产者们
    p1 = Process(target=producer, args=(q, '生产者1'))
    p2 = Process(target=producer, args=(q, '生产者2'))
    p3 = Process(target=producer, args=(q, '生产者3'))
 
    # 消费者们
    c1 = Process(target=consumer, args=(q, '消费者1'))
    c2 = Process(target=consumer, args=(q, '消费者2'))
 
    p1.start()
    p2.start()
    p3.start()
    c1.start()
    c2.start()
 
    p1.join()
    p2.join()
    p3.join()
    q.put(None)
    q.put(None)
    print('主')