# join 串行
from multiprocessing import Process
import time,os

def task(name,n):
    print('%s is running' % name)
    time.sleep(n)


if __name__ == '__main__':
    start = time.time()
    p1 = Process(target=task, args=('子进程1', 3))  # args根据位置传参
    p2 = Process(target=task, args=('子进程2', 1))
    p3 = Process(target=task, args=('子进程3', 2))
    p_l = [p1, p2, p3]

from multiprocessing import Process
import time,os

def task(name,n):
    print('%s is running' % name)
    time.sleep(n)


if __name__ == '__main__':
    start = time.time()
    p1 = Process(target=task, args=('子进程1', 3))  # args根据位置传参
    p2 = Process(target=task, args=('子进程2', 1))
    p3 = Process(target=task, args=('子进程3', 2))
    p_l = [p1, p2, p3]

    p1.start()  # 每个都是执行完以后再进行下一步
    p1.join()  
    p2.start()
    p2.join()
    p3.start()
    p3.join()

    print('主', (time.time()-start))