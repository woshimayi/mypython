# deamon
# 主进程创建子进程，然后将该进程设置成守护自己的进程，守护进程就好比崇祯皇帝身边的老太监，崇祯皇帝已死老太监就跟着殉葬了。
# 关于守护进程需要强调两点：
# 其一：守护进程会在主进程代码执行结束后就终止
# 其二：守护进程内无法再开启子进程,否则抛出异常：AssertionError: daemonic processes are not allowed to have children
# 如果我们有两个任务需要并发执行，那么开一个主进程和一个子进程分别去执行就ok了，如果子进程的任务在主进程任务结束后就没有存在的必要了，那么该子进程应该在开启前就被设置成守护进程。主进程代码运行结束，守护进程随即终止

from multiprocessing import Process

import time
def foo():
    print(123)
    time.sleep(1)
    print("end123")

def bar():
    print(456)
    time.sleep(3)
    print("end456")

if __name__ == '__main__':
    p1 = Process(target=foo)
    p2 = Process(target=bar)

    p1.daemon = True # 一定要在p.start()前设置,设置p为守护进程,禁止p创建子进程,并且父进程代码执行结束,p即终止运行
    p1.start()
    p2.start()
    print("main-------")
