'''
@author: woshimayi
@license: (C) Copyright 2015-2049, Node Supply Chain Manager Corporation Limited.
@contact: xxxxxxxx@qq.com
@software: garner
@file: run.py
@time: 20/12/31 14:57
@desc: multi-download digital tail
'''
import os
import time
import keyboard
import pyperclip
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Process, Queue
from digital_tail import BeautifulPicture





# 定义一个准备作为进程任务的函数
def action(url):
    
    print("下载开始")
    be = BeautifulPicture()
    # 跳转到指定目录
    # os.chdir(r'C:/Users/zs-work/Pictures/')
    # print(os.getcwd())
    
    # 创建网页图片目录
    path = r'./get_pic' + str(time.strftime("%Y%m%d%H%M%S", time.localtime()))
    be.mk_dir(path)

    # 下载图片
    be.get_pic(url)
    print('下载结束')
    return True

def consumer(q):
    while True:
        url = q.get()
        if url is None: continue
        print('download url: %s' % url)
        action(url)
        q.task_done()  # 发出信号项目已处理完成，省去了后面需另外添加的q.put(None)

def test_1(q):
        # 获取剪贴板内容
    url = pyperclip.paste()
    
    # 过滤剪贴板内容是否符合条件
    if 'http' in url and 'html' in url:
        print('生产者生产了%s' % url)
        # q.put(url)
        # q.join()

    else:
        print('no html')


def test(q):
    #按ctrl+c输出b
    keyboard.add_hotkey('ctrl+c', test_1, args=(q,))
    #wait里也可以设置按键，说明当按到该键时结束
    keyboard.wait()



if __name__ == '__main__':
    q = Queue()

    # p1 = Process(target=consumer, args=(q, ))  # 必须加,号
    # p1.daemon = True

    p2 = Process(target=test, args=(q,))  # 必须加,号

    p2.start()
    # p1.start()
    
    p2.join()
    # q.put(None)
    # q.put(None)
    
    print("主")
