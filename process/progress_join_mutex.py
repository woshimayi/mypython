# 用互斥锁，可以通过添加互斥锁的位置，实现部分程序执行达到串行的效果，其他程序仍然可以并行执行，而添加了join只能执行完了之后才能执行下一个，若作为每项都添加一个join，则都要串行执行。从而大大降低了效率。

from multiprocessing import Process, Lock
import json
import time
 
 
def search(name):
    time.sleep(1)
    dic = json.load(open('db.txt', 'r', encoding='utf-8'))
    print('<%s> 查看到剩余票数【%s】' % (name, dic['count']))
 
 
def get(name):
    time.sleep(1)
    dic = json.load(open('db.txt', 'r', encoding='utf-8'))
    if dic['count'] > 0:
        dic['count'] -= 1
        time.sleep(3)
        json.dump(dic, open('db.txt', 'w', encoding='utf-8'))
        print('<%s> 购票成功' % name)
    else:
        print('<%s> 购票失败' % name)
 
 
def task(name,):
    search(name)
    # mutex.acquire()
    get(name)
    # mutex.release()
 
 
if __name__ == '__main__':
    # mutex=Lock()
    for i in range(10):
        p = Process(target=task, args=('路人%s' % i,))
        p.start()
        p.join()