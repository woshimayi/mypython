# Concurrent join 并发
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

    p1.start()
    p2.start()
    p3.start()

    p1.join()  # 这三个仍然是并发执行，只是等待最长的程序执行完才结束
    p2.join()
    p3.join()

    print('主', (time.time()-start))