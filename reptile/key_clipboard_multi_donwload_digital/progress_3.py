# desc:	在主进程的任务与子进程的任务彼此独立的情况下，主进程的任务先执行完毕后，主进程还需要等待子进程执行完毕，然后统一回收资源
from multiprocessing import Process
import time, os
 
def task():
    print('%s is running,parent id is <%s>' % (os.getpid(), os.getppid()))  # 查看子进程和父进程
    time.sleep(3)
    print('%s is done,parent id is <%s>' % (os.getpid(), os.getppid()))
 
if __name__ == '__main__':
    p = Process(target=task,)
    p.start()

    print('主', os.getpid(), os.getppid())  # 查看子进程和父进程，此时父进程为pycharm