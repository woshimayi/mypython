#!/usr/bin/env python
# encoding: utf-8
'''
 * @FilePath: multiprocess_.py
 * @version: (C) Copyright 2010-2049, Node Supply Chain Manager Corporation Limited. 
 * @Author: dof
 * @Date: 2022/7/8 14:40
 * @LastEditors: dof
 * @LastEditTime: 2022/7/8 14:40
 * @Descripttion: 多进程调用
'''
import time
from multiprocessing import Process
import os

from GUI.Pyqt5.wand_test.wand_test import HttpdTest


def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())

def f(name):
    be = HttpdTest()
    while True:
        # info('function f')
        print('hello', name)
        be.wanget_set()

if __name__ == '__main__':
    info('main line')
    p = Process(target=f, args=("bob",))
    p.start()
    # p.join()
    num = 0
    while True:
        time.sleep(1)
        if num == 5:
            p.terminate()
        print("zzzzz")
        num += 1
