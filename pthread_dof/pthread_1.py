#!/usr/bin/env python
# encoding: utf-8
'''
@author: woshimayi
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited. 
@contact: woshidamayi@gmail.com
@software: garner
@file: pthread_1.py
@time: 23/5/5 15:59
@desc:
'''

# 1:导入包
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


# ThreadPoolExecutor线程池ProcessPoolExecutor进程池
def asd(data):
    # print()
    # while True:
    print('zzzzz : {:>10d}:{:<}'.format(data, data))


# 2:在线程池中创建几个线程
pool = ThreadPoolExecutor(10)  # 创建10个线程

# 3:在线程池中发任务
for i in range(100):
    print()
    pool.submit(asd, i)
# 4:等待线程池把任务都执行完毕
pool.shutdown()

if __name__ == '__main__':
    print('hello world')
