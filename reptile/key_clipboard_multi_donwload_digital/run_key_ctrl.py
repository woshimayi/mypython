'''
@author: woshimayi
@license: (C) Copyright 2015-2049, Node Supply Chain Manager Corporation Limited.
@contact: 2638288078@qq.com
@software: garner
@file: run.py
@time: 20/12/31 14:57
@desc: multi-download digital tail
'''
import os
import time
import keyboard
import pyperclip
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
    os.chdir(r'../')
    print(os.getcwd())
    return True

def test():
    # 获取剪贴板内容
    url = pyperclip.paste()

    print(url)
    # 过滤剪贴板内容是否符合条件
    if 'http' in url and 'html' in url:
        print('download url: %s' % url)
        action(url)
    else:
        print('no html')




if __name__ == '__main__':
    #按ctrl+c输出b
    keyboard.add_hotkey('ctrl+c', test)
    #wait里也可以设置按键，说明当按到该键时结束
    keyboard.wait()
