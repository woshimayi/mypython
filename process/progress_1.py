# 创建并开启子进程的方式:1

import time
import random
from multiprocessing import Process

def piao(name):
    print('%s piaoing' %name)
    time.sleep(random.randrange(1,5))
    print('%s piao end' %name)

if __name__ == '__main__':
    #实例化得到四个对象
    p1=Process(target=piao,args=('egon',)) #必须加,号
    p2=Process(target=piao,args=('alex',))
    p3=Process(target=piao,args=('wupeqi',))
    p4=Process(target=piao,args=('yuanhao',))

    #调用对象下的方法，开启四个进程
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    print('主')