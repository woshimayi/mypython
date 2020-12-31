# 产看子进程存活状态alive及取名name

from multiprocessing import Process
import time, os

def task():
    print('%s is running,parent id is <%s>' % (os.getpid(), os.getppid()))
    time.sleep(3)
    print('%s is done,parent id is <%s>' % (os.getpid(), os.getppid()))


if __name__ == '__main__':
    p = Process(target=task,)
    p.start()
    # print(p.is_alive())  # True
    p.join()
    print('主', os.getpid(), os.getppid())
    print(p.pid)
    # print(p.is_alive())  # Flase


    p = Process(target=task,name='sub——Precsss')
    p.start()
    print('1', p.is_alive())
    p.terminate()  # 这里仅仅是给系统发要求让p死掉，但是是需要时间的，所以立即执行is_alive则进程还是活的
    time.sleep(3)
    print('2', p.is_alive())
    print('主')
    print(p.name)  # 如果没有，则默认位p取名，这里已经取名为sub——Precsss
