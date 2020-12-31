# join方法
# desc: 如果主进程的任务在执行到某一个阶段时，需要等待子进程执行完毕后才能继续执行，就需要有一种机制能够让主进程检测子进程是否运行完毕，在子进程执行完毕后才继续执行，否则一直在原地阻塞，这就是join方法的作用
from multiprocessing import Process
import time,os
 
def task():
    print('%s is running,parent id is <%s>' % (os.getpid(), os.getppid()))
    time.sleep(3)
    print('%s is done,parent id is <%s>' % (os.getpid(), os.getppid()))
 
if __name__ == '__main__':
    p = Process(target=task,)
    p.start()
 
    p.join()  # 加入join方法后一定会等到子进程结束以后才会执行主进程
    print('主', os.getpid(), os.getppid())
    print(p.pid)  # 验证了存在僵尸进程